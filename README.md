# github-repo-research

A lightweight OpenClaw skill for researching, comparing, and shortlisting GitHub repositories from natural-language requests.

## What this is

This repo packages an OpenClaw skill that helps an agent turn a vague repo hunt into a structured shortlist.

Use it when you want to:
- find open source projects in a topic area
- compare multiple GitHub repositories
- shortlist candidate repos to adopt, study, fork, or benchmark
- turn broad GitHub exploration into a decision-ready summary

## Example requests

Examples of prompts an OpenClaw agent can handle with this skill:
- Find 5 strong open source OCR repositories in Python
- Compare self-hosted analytics tools on GitHub
- Help me shortlist alternatives to n8n
- Find actively maintained MCP-related repositories
- Search GitHub for open source PDF parsing libraries and recommend the best 3

## How it works

The skill is designed around a simple workflow:
1. clarify the request if key criteria are missing
2. build a small set of balanced GitHub queries
3. search GitHub using `gh`
4. merge, normalize, and deduplicate results
5. inspect the strongest candidates
6. return a shortlist with tradeoffs and recommendations

## Repository layout

- `SKILL.md` — the main skill definition and workflow
- `references/` — supporting guidance for intake, search strategy, evaluation, output formats, and GitHub CLI usage
- `scripts/` — helper scripts for bundling, normalizing, and printing search results

## Requirements

To use the helper scripts directly, you should have:
- GitHub CLI (`gh`) installed
- `gh auth login` completed
- Python 3 available

## Notes

- This is a decision-support skill, not a deep code-review tool.
- It is intentionally general-purpose and not tuned to one specific topic.
- The helper scripts support a practical GitHub search workflow, but the main value lives in how the agent applies the skill.
