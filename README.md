# brain-paper-to-alpha-plugin

Claude Code and Codex Agent-native plugin for turning papers, reports, raw
ideas, alpha examples, and failed WorldQuant BRAIN results into disciplined
alpha research artifacts.

[![Version](https://img.shields.io/badge/version-0.1.1-green)](https://github.com/nutdnuy/brain-paper-to-alpha-plugin)
[![Python](https://img.shields.io/badge/python-3.9+-blue)](https://python.org)
[![License](https://img.shields.io/badge/license-MIT-blue)](LICENSE)

This repo adapts a general `Paper_to_code` pipeline into a BRAIN-specific
paper-to-alpha workflow:

```text
source intake -> research card -> BRAIN primitives -> candidate batch
-> static checks -> simulation queue -> result evaluation -> repair loop
-> memory update
```

It does not include credentials and does not run live BRAIN simulations by
default. The plugin is designed to prepare reproducible candidates and handoffs;
live simulation should only happen after an explicit user request in a trusted
workspace.

## Install In Codex

```bash
codex plugin marketplace add nutdnuy/brain-paper-to-alpha-plugin
```

Then install `brain-paper-to-alpha-plugin` from the Codex plugin UI.

The Codex plugin manifest is `.codex-plugin/plugin.json`; the GitHub
marketplace manifest is `.agents/plugins/marketplace.json`.

## Install In Claude Code

Add this GitHub repository as a marketplace:

```text
/plugin marketplace add https://github.com/nutdnuy/brain-paper-to-alpha-plugin
/plugin install brain-paper-to-alpha-plugin
```

The Claude plugin manifest is `.claude-plugin/plugin.json`; the marketplace
manifest is `.claude-plugin/marketplace.json`.

## Skill

The main skill is `brain-paper-to-alpha-plugin`.

Example prompts:

```text
Use brain-paper-to-alpha-plugin to turn this paper into BRAIN alpha candidates.
Use brain-paper-to-alpha-plugin to create a research run from this alpha idea.
Use brain-paper-to-alpha-plugin to diagnose and repair this failed simulation result.
```

## Commands

Claude Code slash-command workflows:

- `/brain-setup`
- `/brain-init-run`
- `/brain-intake`
- `/brain-generate-candidates`
- `/brain-validate-run`
- `/brain-repair`

The same command files are useful as Codex workflow prompts when the plugin is
installed in Codex.

## Local Artifact CLI

The bundled CLI creates lightweight run folders and checks artifact shape. It
uses only the Python standard library.

```bash
python3 scripts/wq_brain_alpha.py init \
  --source-title "Goodwill burden paper" \
  --source-path ./paper.pdf \
  --output-root ./outputs

python3 scripts/wq_brain_alpha.py append-candidate \
  --run-dir ./outputs/<run_id> \
  --candidate-id paper-alpha-001 \
  --hypothesis-id H01 \
  --expression "rank(ts_delta(ts_backfill(goodwill/sales, 252), 126))" \
  --settings-json '{"region":"USA","universe":"TOP3000","delay":1}'

python3 scripts/wq_brain_alpha.py validate --run-dir ./outputs/<run_id>
```

The CLI intentionally does not authenticate to WorldQuant BRAIN.

## Development

```bash
python3 -m pytest
python3 /Users/nuthdanai/.codex/skills/.system/plugin-creator/scripts/validate_plugin.py .
```

## License

MIT
