---
title: "Differential expression is the hardest scRNA-seq task for agents"
slug: differential-expression-hardest-scrna-seq-task
status: supported
confidence: 0.85
tags:
  - benchmark
  - differential-expression
  - task-difficulty
domain: methods
source_papers:
  - scbench-evaluating-ai-agents-single-cell
evidence:
  - source: scbench-evaluating-ai-agents-single-cell
    type: supports
    strength: strong
    detail: "Difficulty gradient: normalization easiest (cross-model mean 70.4%), then QC (55.3%), clustering (38.3%), cell typing (34.9%), differential expression hardest (27.0%). 7 of 8 models follow the same ordering."
conditions: "Seven task categories; cross-model means."
date_proposed: 2026-06-12
date_updated: 2026-06-12
---

## Statement

scBench tasks form a consistent difficulty gradient in which differential
expression is the hardest (cross-model mean 27.0%) and normalization the easiest
(70.4%), with QC, clustering, and cell typing in between; seven of eight models
follow the same ordering.

## Evidence summary

Judgment-heavy stages (DE, cell typing) require multi-step reasoning and
contextual scientific judgment, whereas procedural stages (normalization, QC)
apply well-understood transformations.

## Conditions and scope

scBench task taxonomy; trajectory-analysis category has only 7 evaluations.

## Counter-evidence

One of eight models deviates from the common ordering.

## Linked ideas

## Open questions

Whether the gradient reflects task intrinsic difficulty or grader tolerance
design.
