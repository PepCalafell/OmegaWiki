---
title: "scRNA-seq analysis is more tractable for agents than spatial transcriptomics"
slug: scrna-seq-analysis-more-tractable-agents
status: supported
confidence: 0.8
tags:
  - benchmark
  - scrna-seq
  - spatial-transcriptomics
domain: methods
source_papers:
  - scbench-evaluating-ai-agents-single-cell
evidence:
  - source: scbench-evaluating-ai-agents-single-cell
    type: supports
    strength: moderate
    detail: "Top model: 52.8% on scBench vs 38.4% on SpatialBench; bottom model 29.2% vs 20.1%. Gap holds across leaderboard; rankings preserved at extremes (Opus leads both, Gemini last in both). Attributed to more public scRNA-seq datasets and Scanpy documentation."
conditions: "Comparison under the same mini-SWE-agent harness; cross-benchmark."
date_proposed: 2026-06-12
date_updated: 2026-06-12
---

## Statement

scRNA-seq analysis is more tractable for agents than spatial transcriptomics:
across models, scBench accuracy is consistently higher than SpatialBench
(52.8% vs 38.4% top model; 29.2% vs 20.1% bottom model), while model rankings
are preserved at the extremes.

## Evidence summary

The authors attribute the gap to training data — scRNA-seq has far more public
datasets and dominant, well-documented tools (Scanpy) than spatial
transcriptomics — most visible in the QC task category.

## Conditions and scope

Same harness; the two benchmarks share grader families and statistical design.

## Counter-evidence

None within the paper; cross-benchmark comparison is correlational.

## Linked ideas

## Open questions

Whether agent improvements transfer across the two modalities.
