---
title: "SpatialBench — spatial transcriptomics agent benchmark"
slug: spatialbench-spatial-transcriptomics-agent-benchmark
domain: methods
status: mainstream
aliases:
  - SpatialBench
first_introduced: "2025"
date_updated: 2026-06-12
source_url: "https://github.com/latchbio"
---

## Definition

SpatialBench is a benchmark of verifiable problems derived from real spatial
transcriptomics workflows, evaluating AI agents under the mini-SWE-agent harness
with deterministic graders. It is the sibling benchmark to scBench (scRNA-seq);
together they cover the two dominant transcriptional assays. SpatialBench was
introduced by the same LatchBio group (Workman et al., 2025).

## Intuition

SpatialBench established the design template that scBench follows: data
snapshots paired with natural-language tasks and deterministic graders, the
"specify what, not how" principle, three evaluation types (scientific /
procedural / observational), and two-stage statistical aggregation.

## Formal notation

146 evaluations across 5 platforms and 7 task categories. Top model accuracy
38.4%, bottom model 20.1%, top–bottom spread 18.3 pp. Best-model easiest task:
normalization 76%; best-model hardest task: QC 22%.

## Key variants

- SpatialBench (spatial transcriptomics) and scBench (scRNA-seq) share harness,
  grader families, and statistical design; scBench reuses and extends the
  SpatialBench methodology.

## Known limitations

- Spatial transcriptomics has fewer public datasets and less tooling
  documentation than scRNA-seq, which the authors argue contributes to lower
  absolute agent accuracy than on scBench.
- Same structural limitations as scBench: deterministic graders discretize
  scientific judgment; each evaluation snapshots a single workflow step.

## Open problems

- Whether agent improvements transfer across the two modalities, given that
  model rankings are preserved at the extremes (Opus leads both, Gemini last
  in both).

## Relevance to active research

SpatialBench is the prior-art anchor that scBench complements; the comparison
between the two benchmarks (preserved rankings, consistently higher scRNA-seq
accuracy, shared platform effects) is a central result of the scBench paper.
