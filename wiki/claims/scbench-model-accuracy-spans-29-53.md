---
title: "scBench model accuracy spans 29–53% with a 23.6 pp spread"
slug: scbench-model-accuracy-spans-29-53
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
    detail: "Aggregate accuracy ranges 29.2% (Gemini 2.5 Pro) to 52.8% (Opus 4.6); 23.6 pp spread exceeds SpatialBench's 18.3 pp, indicating scBench discriminates capability."
conditions: "8 frontier models from 4 providers under mini-SWE-agent."
date_proposed: 2026-06-12
date_updated: 2026-06-12
---

## Statement

Across eight frontier models, aggregate scBench accuracy ranges from 29.2% to
52.8%, a 23.6 percentage-point spread that exceeds SpatialBench's 18.3 pp spread
and demonstrates that scBench discriminates model capability despite higher
overall accuracy.

## Evidence summary

Anthropic models occupy the top four positions (Opus 4.6, Opus 4.5, then GPT-5.2,
then Sonnet 4.5); bottom tier is GPT-5.1, Grok-4.1, Grok-4, Gemini 2.5 Pro.

## Conditions and scope

Specific to the 2026 model lineup and the scBench suite/harness.

## Counter-evidence

None within the paper.

## Linked ideas

## Open questions

Whether the spread widens or narrows as models improve on underrepresented
platforms.
