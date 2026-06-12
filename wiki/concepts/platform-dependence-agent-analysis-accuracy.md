---
title: "Platform dependence of agent analysis accuracy"
aliases:
  - platform generalization gap
tags: []
maturity: emerging
key_papers:
  - scbench-evaluating-ai-agents-single-cell
first_introduced: "2026"
date_updated: 2026-06-12
related_concepts:
  - llm-agent-single-cell-rna-seq
---

## Definition

The empirical observation that an analysis agent's accuracy depends strongly on
the sequencing platform / library-prep technology of the data, often as much as
or more than on the choice of model. In scBench, cross-model mean accuracy
ranges from 59.1% on CSGenetics to 26.4% on MissionBio — a 32.7 pp gap that
exceeds the 23.6 pp spread between the best and worst models.

## Intuition

Platforms that dominate public repositories and tool documentation (Chromium,
Illumina) are well-represented in training data; less-documented platforms with
non-standard data structures (MissionBio Tapestri, ParseBio) expose the
fragility of memorized techniques. Models that overfit on Scanpy tutorials
without learning transferable analysis techniques collapse on underrepresented
platforms.

## Formal notation

Quantified as the cross-platform spread of cross-model mean accuracy, and as
per-model platform swings (e.g., Gemini drops 42 pp between CSGenetics 52.4% and
MissionBio 10.3%; even the most consistent model, Opus 4.5, loses 39 pp between
its best and worst platforms).

## Variants

- Ranking inversion: on the hardest platform (MissionBio), overall-weaker models
  can beat overall-stronger ones (Grok-4 > GPT-5.2; Sonnet 4.5 > GPT-5.2 by 11 pp).

## Comparison

Parallel to, and often larger than, the task-dependence effect (the
normalization→differential-expression difficulty gradient). The platform effect
is also observed in SpatialBench, with 30–40 pp swings across technologies.

## When to use

When reasoning about how to deploy or evaluate analysis agents across diverse
assays, and when interpreting aggregate benchmark scores that average over
platforms of uneven training-data representation.

## Known limitations

The causal attribution to "uneven training data" is inferential; the benchmark
measures the effect but does not directly manipulate training-data exposure.

## Open problems

- Whether platform-aware context, assay-specific tooling, and self-calibration
  heuristics can close the gap, versus one-size-fits-all reasoning.

## Key papers

- [[scbench-evaluating-ai-agents-single-cell]] — quantifies the 32.7 pp cross-platform gap and the MissionBio collapse.

## My understanding

This concept warns against reading a single aggregate benchmark number as
"agent capability"; the platform breakdown is where the practical reliability
story lives.
