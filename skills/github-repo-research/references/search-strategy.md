# Search Strategy

Use this guide to build a compact but effective GitHub search plan.

## Query design goals

Balance recall and precision.
Do not rely on one literal query unless the topic is unusually narrow.

## Query dimensions

Combine a few of these:

1. Core phrase
   - Example: agent memory

2. Synonym or adjacent phrase
   - Example: long-term memory, persistent memory, contextual memory

3. Scenario term
   - Example: coding agent, MCP, browser automation, retrieval, orchestration

4. Technical implementation term
   - Example: sdk, framework, server, plugin, database, runtime

5. Ecosystem term
   - Example: openclaw, claude, codex, langgraph, openai, anthropic

## Default query count

- Narrow request: 3 to 4 queries
- Normal request: 4 to 6 queries
- Broad or ambiguous landscape: 6 to 10 queries

Quality matters more than hitting an arbitrary count.

## Example patterns

### Pattern A: direct + synonym
- "agent memory"
- "long-term memory for agents"
- "persistent memory agent framework"

### Pattern B: product vs framework split
- "browser automation platform"
- "browser automation framework"
- "browser automation sdk"

### Pattern C: ecosystem-anchored
- "MCP server memory"
- "openclaw memory plugin"
- "agent memory sdk"

## Filtering ideas

Use filters as needed, not by reflex:
- stars threshold
- pushed date or recent update requirement
- language
- exclude archived repos
- optionally exclude forks when the task needs original projects

## Practical execution notes

When using GitHub CLI, prefer a few broader searches over many tiny searches.
Merge first, dedupe by `owner/repo`, then score.
After coarse filtering, fetch README details only for the top slice.
