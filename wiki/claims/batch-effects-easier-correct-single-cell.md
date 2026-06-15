---
title: "Batch effects are easier to correct in single-cell graphs than in embeddings or expression matrices"
slug: batch-effects-easier-correct-single-cell
status: supported
confidence: 0.75
tags:
  - batch-integration
  - benchmarking
  - single-cell
domain: methods / benchmarking / single-cell
source_papers:
  - defining-benchmarking-open-problems-single-cell
evidence:
  - source: papers/defining-benchmarking-open-problems-single-cell
    type: supports
    strength: moderate
    detail: "Best-practice finding from the batch-integration task (Supplementary Note 1.4)."
conditions: "Open Problems batch-integration task across the three output representations (graph, embedding, gene matrix)."
date_proposed: 2026-06-15
date_updated: 2026-06-15
---

## Statement

Correcting batch effects is easier in single-cell neighbourhood graphs than in latent embeddings or full expression matrices.

## Evidence summary

"it is easier to correct for batch effects in single-cell graphs than in latent embeddings or expression matrices" (p.1038; Supplementary Note 1.4). This matches the scIB design, where integration outputs are evaluated at graph, embedding and gene-matrix levels.

## Conditions and scope

Comparison is across the three output representations the platform scores; "easier" is in terms of the platform's batch-removal metrics.

## Counter-evidence

Graph-level correction discards quantitative expression structure needed for some downstream analyses, so easier correction is not free.

## Linked ideas

Refines the [[concepts/batch-removal-vs-bioconservation-tradeoff]]; evaluated by [[foundations/scib-benchmark-pipeline]].

## Open questions

Whether graph-level correction sacrifices bio-conservation that matters for downstream differential analysis.
