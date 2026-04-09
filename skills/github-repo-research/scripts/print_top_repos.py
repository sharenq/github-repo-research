#!/usr/bin/env python3
from __future__ import annotations

import json
import sys
from pathlib import Path


def main() -> int:
    if len(sys.argv) < 2:
        print("usage: print_top_repos.py <normalized.json> [limit]", file=sys.stderr)
        return 2

    path = Path(sys.argv[1])
    limit = int(sys.argv[2]) if len(sys.argv) > 2 else 10
    rows = json.loads(path.read_text())

    for row in rows[:limit]:
        print(
            f"{row['owner_repo']}\tstars={row.get('stars')}\tlang={row.get('language')}"
            f"\tupdated={row.get('updated_at')}\tqueries={row.get('query_count')}"
        )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
