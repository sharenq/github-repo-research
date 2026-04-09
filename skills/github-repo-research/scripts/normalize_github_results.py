#!/usr/bin/env python3
"""
Normalize and deduplicate GitHub repo search results.

Input: JSON from stdin in one of these forms:
1. A list of query bundles:
   [{"query": "...", "items": [...]}, ...]
2. A single query bundle:
   {"query": "...", "items": [...]} 
3. A raw list of repo items

Output: normalized JSON list sorted by stars desc then updated_at desc.
"""

from __future__ import annotations

import json
import sys
from collections import defaultdict
from datetime import datetime
from typing import Any


def pick(d: dict[str, Any], *path: str) -> Any:
    cur: Any = d
    for key in path:
        if not isinstance(cur, dict) or key not in cur:
            return None
        cur = cur[key]
    return cur


def owner_login_of(item: dict[str, Any]) -> str | None:
    owner = item.get("owner")
    if isinstance(owner, dict):
        return owner.get("login")
    if isinstance(owner, str):
        return owner
    return item.get("owner_login")


def to_owner_repo(item: dict[str, Any]) -> str | None:
    owner_login = owner_login_of(item)
    name = item.get("name")
    full_name = item.get("full_name") or item.get("fullName")
    if full_name:
        return full_name.lower()
    if owner_login and name:
        return f"{owner_login}/{name}".lower()
    return None


def normalize_item(item: dict[str, Any], query: str | None = None) -> dict[str, Any]:
    owner_login = owner_login_of(item)
    language = pick(item, "primaryLanguage", "name") or item.get("language")
    license_id = (
        pick(item, "licenseInfo", "spdxId")
        or pick(item, "license", "spdx_id")
        or pick(item, "license", "spdxId")
        or item.get("license")
    )
    stars = item.get("stargazersCount")
    if stars is None:
        stars = item.get("stargazers_count")
    updated_at = item.get("updatedAt") or item.get("updated_at") or item.get("pushed_at")
    archived = item.get("isArchived")
    if archived is None:
        archived = item.get("archived")

    owner_repo = to_owner_repo(item)
    if not owner_repo:
        raise ValueError("Could not determine owner/repo")

    return {
        "owner_repo": owner_repo,
        "owner": owner_login,
        "repo": item.get("name") or owner_repo.split("/", 1)[1],
        "description": item.get("description"),
        "url": item.get("url") or item.get("html_url"),
        "stars": stars or 0,
        "updated_at": updated_at,
        "language": language,
        "license": license_id,
        "archived": bool(archived),
        "topics": item.get("topics") or [],
        "queries": [query] if query else [],
    }


def parse_input(data: Any) -> list[tuple[str | None, dict[str, Any]]]:
    out: list[tuple[str | None, dict[str, Any]]] = []

    if isinstance(data, dict) and isinstance(data.get("items"), list):
        query = data.get("query")
        for item in data["items"]:
            if isinstance(item, dict):
                out.append((query, item))
        return out

    if isinstance(data, list):
        for entry in data:
            if isinstance(entry, dict) and isinstance(entry.get("items"), list):
                query = entry.get("query")
                for item in entry["items"]:
                    if isinstance(item, dict):
                        out.append((query, item))
            elif isinstance(entry, dict):
                out.append((None, entry))
        return out

    raise ValueError("Unsupported input shape")


def dt_key(value: str | None) -> tuple[int, str]:
    if not value:
        return (0, "")
    try:
        iso = value.replace("Z", "+00:00")
        dt = datetime.fromisoformat(iso)
        return (1, dt.isoformat())
    except Exception:
        return (1, value)


def main() -> int:
    data = json.load(sys.stdin)
    parsed = parse_input(data)

    merged: dict[str, dict[str, Any]] = {}
    query_hits: dict[str, set[str]] = defaultdict(set)

    for query, raw in parsed:
        try:
            item = normalize_item(raw, query=query)
        except ValueError:
            continue

        key = item["owner_repo"]
        if query:
            query_hits[key].add(query)

        existing = merged.get(key)
        if not existing:
            merged[key] = item
            continue

        if (item.get("stars") or 0) > (existing.get("stars") or 0):
            existing["stars"] = item["stars"]
        if dt_key(item.get("updated_at")) > dt_key(existing.get("updated_at")):
            existing["updated_at"] = item.get("updated_at")

        for field in ["description", "url", "language", "license"]:
            if not existing.get(field) and item.get(field):
                existing[field] = item[field]

        existing["archived"] = bool(existing.get("archived") or item.get("archived"))

        existing_topics = set(existing.get("topics") or [])
        existing_topics.update(item.get("topics") or [])
        existing["topics"] = sorted(existing_topics)

    results = []
    for key, item in merged.items():
        item["queries"] = sorted(query_hits.get(key, set()))
        item["query_count"] = len(item["queries"])
        results.append(item)

    results.sort(
        key=lambda x: (
            int(x.get("stars") or 0),
            dt_key(x.get("updated_at")),
        ),
        reverse=True,
    )

    json.dump(results, sys.stdout, ensure_ascii=False, indent=2)
    sys.stdout.write("\n")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
