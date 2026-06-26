import csv
import json
from pathlib import Path

from scripts import wq_brain_alpha


def test_init_creates_required_artifacts(tmp_path: Path) -> None:
    exit_code = wq_brain_alpha.main(
        [
            "init",
            "--source-title",
            "Goodwill Burden",
            "--source-path",
            "paper.pdf",
            "--output-root",
            str(tmp_path),
            "--run-id",
            "run-goodwill",
        ]
    )
    assert exit_code == 0

    run_dir = tmp_path / "run-goodwill"
    assert (run_dir / "00_source" / "source_metadata.json").exists()
    assert (run_dir / "01_research_card.md").exists()
    assert (run_dir / "02_candidates.csv").exists()
    assert (run_dir / "03_simulation_queue.csv").exists()
    metadata = json.loads((run_dir / "00_source" / "source_metadata.json").read_text())
    assert metadata["source_title"] == "Goodwill Burden"
    assert metadata["live_brain_simulation"] is False


def test_append_candidate_and_validate(tmp_path: Path) -> None:
    wq_brain_alpha.main(
        [
            "init",
            "--source-title",
            "Quality Change",
            "--output-root",
            str(tmp_path),
            "--run-id",
            "run-quality",
        ]
    )
    run_dir = tmp_path / "run-quality"
    settings = '{"region":"USA","universe":"TOP3000","delay":1}'

    exit_code = wq_brain_alpha.main(
        [
            "append-candidate",
            "--run-dir",
            str(run_dir),
            "--candidate-id",
            "alpha-001",
            "--hypothesis-id",
            "H01",
            "--expression",
            "rank(ts_delta(ts_backfill(operating_income/cap, 120), 60))",
            "--settings-json",
            settings,
            "--queue",
        ]
    )
    assert exit_code == 0

    with (run_dir / "02_candidates.csv").open(newline="", encoding="utf-8") as handle:
        rows = list(csv.DictReader(handle))
    assert rows[0]["candidate_id"] == "alpha-001"
    assert rows[0]["static_checks"] == "balanced_parentheses"

    assert wq_brain_alpha.main(["validate", "--run-dir", str(run_dir)]) == 0
