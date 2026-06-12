---
title: "Differential expression is the most model-discriminative scRNA-seq task"
slug: differential-expression-most-model-discriminative-scrna
status: supported
confidence: 0.8
tags:
  - benchmark
  - differential-expression
  - discriminability
domain: methods
source_papers:
  - scbench-evaluating-ai-agents-single-cell
evidence:
  - source: scbench-evaluating-ai-agents-single-cell
    type: supports
    strength: moderate
    detail: "Differential expression shows the largest best-worst spread of any task (27.7 pp); model differences concentrate in judgment-heavy stages (DE and cell typing) rather than procedural ones."
conditions: "Cross-model best-worst spread per task category."
date_proposed: 2026-06-12
date_updated: 2026-06-12
---

## Statement

Differential expression is the most discriminative scBench task, with a 27.7 pp
spread between the best and worst models; model capability differences
concentrate in judgment-heavy stages (DE, cell typing) rather than procedural
ones.

## Evidence summary

Complements the difficulty-gradient claim: DE is both hardest and most
separating, making it the most informative task for ranking agents.

## Conditions and scope

scBench suite; per-task best-worst spread.

## Counter-evidence

None within the paper.

## Linked ideas

## Open questions

Whether DE discriminability persists as models improve overall.
