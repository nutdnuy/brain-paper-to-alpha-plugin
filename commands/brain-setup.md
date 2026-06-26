---
description: Check local WQ BRAIN alpha artifact utilities
argument-hint: ""
allowed-tools: Bash(cd:*), Bash(python:*), Bash(python3:*)
---

Check the plugin-local artifact helper.

Run:

```bash
cd "${CLAUDE_PLUGIN_ROOT:-$PWD}" && python3 scripts/wq_brain_alpha.py --help
cd "${CLAUDE_PLUGIN_ROOT:-$PWD}" && python3 -c "from scripts import wq_brain_alpha; print('brain artifact helper ok')"
```

Report whether the CLI and tests are available. Also remind the user that this
plugin does not store credentials and does not run live WorldQuant BRAIN
simulations unless explicitly requested in a trusted workspace.
