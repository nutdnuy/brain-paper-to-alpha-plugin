# brain-alpha-plugin

Claude Code and Codex plugin for turning papers, reports, raw ideas, alpha
examples, and failed WorldQuant BRAIN results into disciplined alpha research
artifacts.

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
codex plugin marketplace add nutdnuy/brain-alpha-plugin
```

Then install `brain-alpha-plugin` from the Codex plugin UI.

The Codex plugin manifest is `.codex-plugin/plugin.json`; the GitHub
marketplace manifest is `.agents/plugins/marketplace.json`.

## Install In Claude Code

Add this GitHub repository as a marketplace:

```text
/plugin marketplace add https://github.com/nutdnuy/brain-alpha-plugin
/plugin install brain-alpha-plugin
```

The Claude plugin manifest is `.claude-plugin/plugin.json`; the marketplace
manifest is `.claude-plugin/marketplace.json`.

## Skill

The main skill is `brain-alpha-plugin`.

Example prompts:

```text
Use brain-alpha-plugin to turn this paper into BRAIN alpha candidates.
Use brain-alpha-plugin to create a research run from this alpha idea.
Use brain-alpha-plugin to diagnose and repair this failed simulation result.
```

## Local Artifact CLI

The bundled CLI creates lightweight run folders and checks artifact shape. It
uses only the Python standard library.

```bash
python scripts/wq_brain_alpha.py init \
  --source-title "Goodwill burden paper" \
  --source-path ./paper.pdf \
  --output-root ./outputs

python scripts/wq_brain_alpha.py append-candidate \
  --run-dir ./outputs/<run_id> \
  --candidate-id paper-alpha-001 \
  --hypothesis-id H01 \
  --expression "rank(ts_delta(ts_backfill(goodwill/sales, 252), 126))" \
  --settings-json '{"region":"USA","universe":"TOP3000","delay":1}'

python scripts/wq_brain_alpha.py validate --run-dir ./outputs/<run_id>
```

The CLI intentionally does not authenticate to WorldQuant BRAIN.

## Development

```bash
python -m pytest
python /Users/nuthdanai/.codex/skills/.system/plugin-creator/scripts/validate_plugin.py .
```

## License

MIT
