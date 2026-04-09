# GitHub CLI Playbook

Use this reference when executing a repo research run with GitHub CLI.

## Preferred command styles

### 1. Fast repo search

Use `gh search repos` when a query is simple and you want quick structured output.

Example:

```bash
gh search repos "agent memory" \
  --limit 30 \
  --json owner,name,description,stargazersCount,updatedAt,url,language,isArchived,license
```

Good for fast candidate collection.

### 2. Search API for richer filtering

Use `gh api /search/repositories` when you want REST search qualifiers in one query.

Example:

```bash
gh api /search/repositories \
  -f q='agent memory stars:>100 archived:false fork:false' \
  -f per_page=30
```

Useful qualifiers:
- `stars:>100`
- `archived:false`
- `fork:false`
- `language:Python`
- `pushed:>=2025-01-01`
- `topic:mcp`

## Suggested run pattern

### Step 1: build 3 to 6 queries

Example query set for a normal task:
- `agent memory`
- `long-term memory agent`
- `persistent memory framework`
- `MCP memory server`

### Step 2: collect JSON per query

Store raw outputs if needed, or pipe directly into local processing.

### Step 3: normalize and dedupe

Use the bundled script when combining multiple query outputs.

Example shape for piped JSON input:

```json
[
  {
    "query": "agent memory",
    "items": [ ... ]
  },
  {
    "query": "persistent memory framework",
    "items": [ ... ]
  }
]
```

### Step 4: inspect top candidates

For the top slice, read:
- README or repo description
- language
- license
- updated date
- obvious maintenance signals

## Practical field set

For `gh search repos`, try to keep a stable minimum field set:
- `owner`
- `name`
- `description`
- `stargazersCount`
- `updatedAt`
- `url`
- `language`
- `isArchived`
- `license`

For `gh api /search/repositories`, expect REST-shaped items such as:
- `owner.login`
- `name`
- `description`
- `stargazers_count`
- `updated_at`
- `html_url`
- `language`
- `archived`
- `license.spdx_id`

## Follow-up inspection ideas

### Repo README

Use raw README URL when available, or `web_fetch` on the repo page if needed.

### Commit recency

Example:

```bash
gh api repos/OWNER/REPO/commits --jq '.[0] | {date: .commit.committer.date, message: .commit.message}'
```

### Open issue signal

Example:

```bash
gh api repos/OWNER/REPO --jq '{openIssues: .open_issues_count, forks: .forks_count, watchers: .subscribers_count}'
```

## Notes

- `gh search repos --json ...` returns a raw list, not an `{items: [...]}` wrapper.
- `gh search repos` and `gh api /search/repositories` return different field shapes. Normalize before comparing across both.
- Prefer fewer broader searches over many narrow ones.
- Do not over-read weak candidates.
- Search is for recall. README inspection is for judgment.
- If the user wants implementation help after selection, hand off to a coding workflow.
