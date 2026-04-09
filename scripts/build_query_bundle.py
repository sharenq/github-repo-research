#!/usr/bin/env python3
from __future__ import annotations

import json
import sys
from pathlib import Path


def main() -> int:
    if len(sys.argv) < 3:
        print("usage: build_query_bundle.py <queries.txt> <query-json>...", file=sys.stderr)
        return 2

    queries_path = Path(sys.argv[1])
    json_paths = [Path(p) for p in sys.argv[2:]]
    queries = [line.strip() for line in queries_path.read_text().splitlines() if line.strip()]

    if len(queries) != len(json_paths):
        print("query count does not match json file count", file=sys.stderr)
        return 2

    out = []
    for query, path in zip(queries, json_paths):
        data = json.loads(path.read_text())
        if isinstance(data, list):
            items = data
        elif isinstance(data, dict):
            items = data.get("items", [])
        else:
            items = []
        out.append({"query": query, "items": items})

    json.dump(out, sys.stdout, ensure_ascii=False, indent=2)
    sys.stdout.write("\n")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
