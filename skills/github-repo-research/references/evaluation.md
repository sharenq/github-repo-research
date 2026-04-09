# Evaluation Guide

Use this guide to rank repositories in a way that supports decisions, not just popularity sorting.

## Core evaluation lens

Score candidates using a practical blend of:

1. Relevance
   - How directly does the repo address the user’s actual problem?

2. Intended-use fit
   - Is it suitable for direct adoption, forking, study, or benchmarking?

3. Maturity
   - Does it look coherent, documented, and usable?

4. Maintenance signals
   - Recency, signs of active upkeep, visible issue or PR health when easy to inspect

5. Ecosystem fit
   - Language, architecture style, deployment assumptions, licensing compatibility

6. Popularity
   - Stars and ecosystem visibility are supporting signals, not the primary rank driver

## Repo type taxonomy

Classify candidates before comparing them. Suggested types:

- Product
  - Something users can run or adopt directly

- Framework
  - A toolkit or foundation for building a solution

- Infrastructure
  - A lower-level component such as storage, orchestration, runtime, or protocol layer

- Integration or service
  - Connector, plugin, MCP server, provider bridge, adapter

- Curated list
  - Awesome list, catalog, directory, resource list

- Research or methodology
  - Experimental, academic, conceptual, benchmark-heavy, or design-oriented repo

## What to watch for

Positive signals:
- clear README and positioning
- examples or quickstart
- active maintenance or at least stable completeness
- sane license
- clean scope and boundaries

Caution signals:
- vague positioning
- stale or archived
- stars inflated relative to actual substance
- repo title matches but content does not
- commercial wrapper with thin open source core
- tutorial or demo repo mistaken for a production candidate

## Recommendation framing

For each shortlisted repo, explain:
- what role it plays
- why it fits this user request
- where it is weak or mismatched

When helpful, label candidates as:
- best to use now
- best to fork
- best to learn from
- best landscape map
