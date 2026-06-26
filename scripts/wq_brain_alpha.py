#!/usr/bin/env python3
"""Local artifact helper for the brain-paper-to-alpha-plugin plugin.

This script creates and validates paper-to-alpha run folders. It intentionally
does not authenticate to WorldQuant BRAIN or run live simulations.
"""

from __future__ import annotations

import argparse
import csv
import datetime as dt
import json
import re
import sys
from pathlib import Path
from typing import Any


CANDIDATE_COLUMNS = [
    "candidate_id",
    "hypothesis_id",
    "source_id",
    "family",
    "expression",
    "settings_json",
    "expected_effect",
    "static_checks",
    "status",
    "notes",
]

QUEUE_COLUMNS = [
    "queue_id",
    "candidate_id",
    "expression",
    "settings_json",
    "priority",
    "reason",
    "run_policy",
    "status",
]

STATUS_VALUES = {
    "draft",
    "static-pass",
    "queued",
    "simulated",
    "hard-pass",
    "near-pass",
    "failed",
    "archive",
}


def slugify(value: str) -> str:
    slug = re.sub(r"[^a-zA-Z0-9]+", "-", value.strip().lower()).strip("-")
    return slug[:64] or "brain-alpha-run"


def utc_stamp() -> str:
    return dt.datetime.now(dt.timezone.utc).strftime("%Y%m%d-%H%M%S")


def write_text_if_missing(path: Path, content: str) -> None:
    if not path.exists():
        path.write_text(content, encoding="utf-8")


def write_csv_header_if_missing(path: Path, columns: list[str]) -> None:
    if path.exists():
        return
    with path.open("w", newline="", encoding="utf-8") as handle:
        csv.writer(handle).writerow(columns)


def load_template(name: str) -> str:
    root = Path(__file__).resolve().parents[1]
    template_path = root / "skills" / "brain-paper-to-alpha-plugin" / "templates" / name
    return template_path.read_text(encoding="utf-8")


def create_run(args: argparse.Namespace) -> Path:
    run_id = args.run_id or f"{utc_stamp()}-{slugify(args.source_title)}"
    run_dir = Path(args.output_root).expanduser().resolve() / run_id
    run_dir.mkdir(parents=True, exist_ok=False)

    (run_dir / "00_source").mkdir()
    (run_dir / "04_results").mkdir()

    metadata = {
        "run_id": run_id,
        "created_utc": dt.datetime.now(dt.timezone.utc).isoformat(),
        "source_title": args.source_title,
        "source_path": args.source_path,
        "live_brain_simulation": False,
    }
    (run_dir / "00_source" / "source_metadata.json").write_text(
        json.dumps(metadata, indent=2, ensure_ascii=False) + "\n",
        encoding="utf-8",
    )

    write_text_if_missing(run_dir / "01_research_card.md", load_template("research-card.md"))
    write_csv_header_if_missing(run_dir / "02_candidates.csv", CANDIDATE_COLUMNS)
    write_csv_header_if_missing(run_dir / "03_simulation_queue.csv", QUEUE_COLUMNS)
    write_text_if_missing(run_dir / "05_evaluation_record.yaml", load_template("evaluation-record.yaml"))
    write_text_if_missing(
        run_dir / "06_memory_update.md",
        "# Memory Update\n\n- Status: draft\n- Next action:\n",
    )
    return run_dir


def parse_settings_json(raw: str) -> str:
    try:
        data = json.loads(raw)
    except json.JSONDecodeError as exc:
        raise ValueError(f"settings_json is not valid JSON: {exc}") from exc
    if not isinstance(data, dict):
        raise ValueError("settings_json must be a JSON object")
    return json.dumps(data, sort_keys=True, separators=(",", ":"))


def parentheses_balanced(expression: str) -> bool:
    stack: list[str] = []
    pairs = {")": "(", "]": "[", "}": "{"}
    for char in expression:
        if char in "([{":
            stack.append(char)
        elif char in pairs:
            if not stack or stack.pop() != pairs[char]:
                return False
    return not stack


def append_candidate(args: argparse.Namespace) -> Path:
    run_dir = Path(args.run_dir).expanduser().resolve()
    candidate_path = run_dir / "02_candidates.csv"
    queue_path = run_dir / "03_simulation_queue.csv"
    if not candidate_path.exists():
        raise FileNotFoundError(f"Missing candidate file: {candidate_path}")
    settings_json = parse_settings_json(args.settings_json)
    static_checks = []
    static_checks.append("balanced_parentheses" if parentheses_balanced(args.expression) else "unbalanced_parentheses")
    status = args.status
    if status not in STATUS_VALUES:
        raise ValueError(f"Invalid status {status!r}. Allowed: {sorted(STATUS_VALUES)}")

    row = {
        "candidate_id": args.candidate_id,
        "hypothesis_id": args.hypothesis_id,
        "source_id": args.source_id,
        "family": args.family,
        "expression": args.expression,
        "settings_json": settings_json,
        "expected_effect": args.expected_effect,
        "static_checks": ";".join(static_checks),
        "status": status,
        "notes": args.notes,
    }
    with candidate_path.open("a", newline="", encoding="utf-8") as handle:
        writer = csv.DictWriter(handle, fieldnames=CANDIDATE_COLUMNS)
        writer.writerow(row)

    if args.queue:
        queue_id = args.queue_id or f"Q-{args.candidate_id}"
        queue_row = {
            "queue_id": queue_id,
            "candidate_id": args.candidate_id,
            "expression": args.expression,
            "settings_json": settings_json,
            "priority": args.priority,
            "reason": args.queue_reason,
            "run_policy": "manual-only",
            "status": "queued",
        }
        with queue_path.open("a", newline="", encoding="utf-8") as handle:
            writer = csv.DictWriter(handle, fieldnames=QUEUE_COLUMNS)
            writer.writerow(queue_row)
    return candidate_path


def read_csv_rows(path: Path) -> list[dict[str, str]]:
    with path.open(newline="", encoding="utf-8") as handle:
        return list(csv.DictReader(handle))


def read_csv_fieldnames(path: Path) -> list[str]:
    with path.open(newline="", encoding="utf-8") as handle:
        return list(csv.DictReader(handle).fieldnames or [])


def validate_run(args: argparse.Namespace) -> int:
    run_dir = Path(args.run_dir).expanduser().resolve()
    required = [
        "00_source/source_metadata.json",
        "01_research_card.md",
        "02_candidates.csv",
        "03_simulation_queue.csv",
        "05_evaluation_record.yaml",
        "06_memory_update.md",
    ]
    issues: list[str] = []
    for relative in required:
        if not (run_dir / relative).exists():
            issues.append(f"missing:{relative}")

    candidate_path = run_dir / "02_candidates.csv"
    if candidate_path.exists():
        header = read_csv_fieldnames(candidate_path)
        rows = read_csv_rows(candidate_path)
        missing = [col for col in CANDIDATE_COLUMNS if col not in header]
        if missing:
            issues.append(f"candidate_columns_missing:{','.join(missing)}")
        for row in rows:
            expression = row.get("expression", "")
            if expression and not parentheses_balanced(expression):
                issues.append(f"candidate_unbalanced:{row.get('candidate_id', '<missing-id>')}")
            settings = row.get("settings_json", "")
            if settings:
                try:
                    parse_settings_json(settings)
                except ValueError as exc:
                    issues.append(f"candidate_bad_settings:{row.get('candidate_id', '<missing-id>')}:{exc}")

    if issues:
        for issue in issues:
            print(f"ISSUE {issue}")
        return 1
    print(f"OK {run_dir}")
    return 0


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description="Create and validate WQ BRAIN alpha research artifacts.")
    subparsers = parser.add_subparsers(dest="command", required=True)

    init_parser = subparsers.add_parser("init", help="Create a new alpha research run folder.")
    init_parser.add_argument("--source-title", required=True)
    init_parser.add_argument("--source-path", default="")
    init_parser.add_argument("--output-root", default="outputs")
    init_parser.add_argument("--run-id")
    init_parser.set_defaults(func=lambda args: print(create_run(args)))

    candidate_parser = subparsers.add_parser("append-candidate", help="Append a candidate expression row.")
    candidate_parser.add_argument("--run-dir", required=True)
    candidate_parser.add_argument("--candidate-id", required=True)
    candidate_parser.add_argument("--hypothesis-id", required=True)
    candidate_parser.add_argument("--expression", required=True)
    candidate_parser.add_argument("--settings-json", required=True)
    candidate_parser.add_argument("--source-id", default="")
    candidate_parser.add_argument("--family", default="")
    candidate_parser.add_argument("--expected-effect", default="")
    candidate_parser.add_argument("--status", default="draft")
    candidate_parser.add_argument("--notes", default="")
    candidate_parser.add_argument("--queue", action="store_true")
    candidate_parser.add_argument("--queue-id")
    candidate_parser.add_argument("--priority", default="medium")
    candidate_parser.add_argument("--queue-reason", default="manual review before live simulation")
    candidate_parser.set_defaults(func=lambda args: print(append_candidate(args)))

    validate_parser = subparsers.add_parser("validate", help="Validate a run folder.")
    validate_parser.add_argument("--run-dir", required=True)
    validate_parser.set_defaults(func=validate_run)
    return parser


def main(argv: list[str] | None = None) -> int:
    parser = build_parser()
    args = parser.parse_args(argv)
    result: Any = args.func(args)
    return result if isinstance(result, int) else 0


if __name__ == "__main__":
    sys.exit(main())
