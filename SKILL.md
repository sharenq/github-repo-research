---
name: github-repo-research
description: Research, compare, and recommend GitHub repositories from natural-language requests. Use when the user wants to find open source projects, compare GitHub repos, shortlist candidate repositories, explore a technical direction on GitHub, or turn a vague repo hunt into a structured recommendation. Prefer this over ad hoc searching when the goal is decision support, not just a few links.
---

# GitHub Repo Research

Use this skill to turn a GitHub repo hunt into a decision-ready shortlist.

## When to use

Use this skill when the user wants to:
- find open source projects in a topic area
- compare multiple GitHub repositories
- identify good repos to study, adopt, fork, or benchmark
- search GitHub for tools, frameworks, products, MCP servers, plugins, or reference implementations
- get a structured shortlist instead of raw links

Do not use this skill for:
- simple one-off repo lookups when a direct answer is enough
- GitHub issue or PR operations on a known repo
- deep code review of a chosen repo, where a coding workflow is more appropriate

## Core workflow

1. Clarify the request if key selection criteria are missing.
2. Build a small set of search queries that balance precision and recall.
3. Search GitHub using the most suitable available tools.
4. Merge, deduplicate, and filter candidates.
5. Classify repo types so unlike things are not compared blindly.
6. Deep-read the top candidates only.
7. Deliver a shortlist with reasons, tradeoffs, and next-step guidance.

## Clarification rules

If the request is vague, clarify the most decision-shaping points first:
- topic or problem area
- desired output size, for example top 5 or top 10
- minimum maturity, for example stars or recency
- preference for product, framework, infrastructure, or curated list
- preferred language or stack
- exclusions

If the request is already specific enough, start immediately and state any assumptions briefly in the output.
Do not force a confirmation loop when the user has already given actionable criteria.

## Search strategy

Use 3 to 10 queries depending on task complexity.
Balance these dimensions:
- core terms
- close synonyms
- scenario terms
- technical implementation terms
- ecosystem terms, when relevant

Read `references/search-strategy.md` when you need query construction patterns.

## Recommended tools

Prefer the most direct reliable source first:
- `exec` with `gh search repos` or `gh api` when GitHub CLI is available
- `web_fetch` for README or repo page follow-up reads
- `web_search` only when GitHub search needs outside context or discovery help

Use lightweight reads first. Deep-read only the top candidates.
Read `references/github-cli-playbook.md` when you need concrete command patterns.

## Execution pattern

A good default flow is:
1. build a compact query set
2. run a few GitHub searches
3. capture structured JSON
4. normalize and deduplicate results
5. inspect the top slice more deeply
6. write a recommendation, not a dump

When GitHub CLI is available, prefer structured output and local post-processing over repeated manual reading.
Use the bundled normalization script when it saves time.

## Evaluation model

Judge candidates using a practical mix of:
- relevance to the stated goal
- suitability for the user’s intended use, such as adopt, study, fork, or benchmark
- project maturity and clarity
- maintenance signals
- ecosystem fit
- stars as a supporting signal, not the main ranking signal

Read `references/evaluation.md` for the scoring lens and repo type taxonomy.

## Output modes

Pick the lightest useful output format:
- quick shortlist for fast recommendation
- comparison table for side-by-side decisions
- categorized list when the candidate pool spans different repo roles
- research memo when the user wants a deeper scan

Read `references/output-formats.md` for default output templates.

## Delivery rules

Good output should help the user decide what to inspect next.
Do not dump a long link list without explanation.
For each shortlisted repo, explain:
- what it is
- why it made the cut for this request
- any key limitation, risk, or mismatch

When useful, end with one of these:
- best starting point
- best production candidate
- best reference architecture
- best repo to fork

## Notes for OpenClaw environments

This skill is for research and recommendation. If the user wants implementation help after choosing a repo, hand off the build or code-inspection phase to a coding workflow.

If this skill grows, keep SKILL.md lean. Put detailed rubrics, examples, and domain-specific variants into `references/`.
