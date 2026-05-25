#!/usr/bin/env python3
# /// script
# requires-python = ">=3.12"
# dependencies = [
#   "ruamel.yaml>=0.18,<0.19",
#   "prance>=25.4.8,<26",
#   "openapi-spec-validator>=0.7.1",
# ]
# ///
"""Portable PEP 723 entry for dsl_cli.

Preferred invocation (auto-installs runtime deps via uv):

    uv run .claude/skills/aibdd-core/scripts/run_dsl_cli.py query --help

Fallback when uv is unavailable (caller must install runtime deps first):

    python3 .claude/skills/aibdd-core/scripts/run_dsl_cli.py query --help

Backward-compatible package entry remains available:

    PYTHONPATH=.claude/skills/aibdd-core/scripts python3 -m dsl_cli query --help
"""

from __future__ import annotations

import sys
from pathlib import Path

_SCRIPTS_DIR = Path(__file__).resolve().parent
if str(_SCRIPTS_DIR) not in sys.path:
    sys.path.insert(0, str(_SCRIPTS_DIR))

from dsl_cli.cli import main

if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
