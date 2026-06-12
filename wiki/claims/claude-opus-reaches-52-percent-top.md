---
title: "Claude Opus 4.6 reaches 52.8% top accuracy on scBench"
slug: claude-opus-reaches-52-percent-top
status: supported
confidence: 0.9
tags:
  - benchmark
  - llm-agent
  - scrna-seq
domain: methods
source_papers:
  - scbench-evaluating-ai-agents-single-cell
evidence:
  - source: scbench-evaluating-ai-agents-single-cell
    type: supports
    strength: strong
    detail: "Table 2 / Fig 2: Claude Opus 4.6 achieves 52.8% (95% CI 48.3–57.2), the highest of 8 frontier models; 394 evals, 3 replicates."
conditions: "Under the mini-SWE-agent harness, 100-step cap, no retries; deterministic graders."
date_proposed: 2026-06-12
date_updated: 2026-06-12
---

## Statement

The best-performing frontier model on scBench, Claude Opus 4.6, reaches 52.8%
accuracy (95% CI 48.3–57.2%), leaving substantial room for progress on
data-grounded scRNA-seq analysis.

## Evidence summary

Measured over 394 verifiable evaluations with 3 replicates each, aggregated via
two-stage aggregation with the t-distribution. Opus 4.6 leads Opus 4.5 (49.9%)
and GPT-5.2 (45.2%).

## Conditions and scope

Specific to the mini-SWE-agent harness and the scBench evaluation suite as of
the 2026 preprint. No explicit seed or temperature control.

## Counter-evidence

None within the paper; absolute accuracy is harness- and suite-dependent.

## Linked ideas

## Open questions

How much of the headroom above 52.8% is closable by harness engineering versus
model training?
