#!/usr/bin/env python3
"""
resolve_args.py

Shared placeholder resolver for every aibdd-xxx skill.

Reads arbitrary text from stdin, substitutes every `${dotted.key}` placeholder
with the corresponding value from `.aibdd/arguments.yml` (path is hard-coded
relative to CWD), and writes the resolved text to stdout.

Behavior:
  - Substitution is single-pass (values that themselves contain `${...}` are
    NOT recursively resolved).
  - Missing `.aibdd/arguments.yml` -> exit 1, message on stderr.
  - Any `${key}` whose key cannot be resolved -> exit 2, list of missing keys
    on stderr; stdout stays empty so callers cannot silently consume a
    partially-resolved blob.

Usage:
  echo 'feature_dir=${specs.root}/${feature.slug}' \\
    | python3 .claude/skills/aibdd-core/scripts/python/resolve_args.py
"""
import re
import sys
from pathlib import Path

import yaml

ARGS_PATH = Path(".aibdd/arguments.yml")
PLACEHOLDER = re.compile(r"\$\{([^}]+)\}")


def lookup(data, dotted_key):
    cur = data
    for part in dotted_key.split("."):
        if not isinstance(cur, dict) or part not in cur:
            return None
        cur = cur[part]
    return cur


def main():
    if not ARGS_PATH.exists():
        sys.stderr.write(
            f"[resolve-args] arguments.yml not found at {ARGS_PATH.resolve()}\n"
        )
        sys.exit(1)

    try:
        data = yaml.safe_load(ARGS_PATH.read_text()) or {}
    except yaml.YAMLError as e:
        sys.stderr.write(f"[resolve-args] failed to parse {ARGS_PATH}: {e}\n")
        sys.exit(1)

    raw = sys.stdin.read()
    missing = []

    def sub(match):
        key = match.group(1).strip()
        val = lookup(data, key)
        if val is None:
            missing.append(key)
            return match.group(0)
        return str(val)

    out = PLACEHOLDER.sub(sub, raw)

    if missing:
        sys.stderr.write("[resolve-args] missing keys in .aibdd/arguments.yml:\n")
        for k in sorted(set(missing)):
            sys.stderr.write(f"  - {k}\n")
        sys.exit(2)

    sys.stdout.write(out)


if __name__ == "__main__":
    main()
