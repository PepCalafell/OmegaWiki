---
title: "Verifiable deterministic bioinformatics benchmark grading"
aliases:
  - deterministic grader
  - verifiable analysis benchmark
tags: []
maturity: emerging
key_papers:
  - scbench-evaluating-ai-agents-single-cell
first_introduced: "2025"
date_updated: 2026-06-12
related_concepts:
  - llm-agent-single-cell-rna-seq
---

## Definition

A benchmark-design methodology in which each problem pairs a data snapshot and a
natural-language task with a deterministic grader that maps the agent's
structured JSON output to a binary pass/fail, with no subjective interpretation.
It is the core construction principle of scBench (and SpatialBench), enabling
reproducible, data-grounded evaluation of analysis agents.

## Intuition

The overarching rule is "specify what, not how": the task states the scientific
goal and exact output format but does not prescribe the method or parameters
(except for procedural tasks). Tolerances are calibrated by running multiple
valid methods so the grader accepts reasonable methodological variation while
still being deterministic.

## Formal notation

scBench uses five grader families:
- NumericTolerance — absolute/relative/min/max/asymmetric tolerance on numeric
  fields (cell counts, fold changes, QC metrics).
- MultipleChoice — agent answer matched (case-insensitive) against correct set.
- MarkerGenePrecisionRecall — precision@K = |P∩G|/|P|, recall@K = |P∩G|/|G|
  against canonical marker sets (defaults τ_r=0.50, τ_p=0.60).
- LabelSetJaccard — J(A,B)=|A∩B|/|A∪B| ≥ τ (default 0.90).
- DistributionComparison — per-category |p_agent − p_gt| ≤ ε (default 3.0 pp),
  all ground-truth categories must pass.

## Variants

- Three evaluation types governing tolerance width: scientific (widest),
  procedural (tighter), observational (most relaxed).
- Anti-shortcut hardening: precomputed embeddings (`X_pca`, `X_umap`) and cached
  labels are stripped so the agent must compute the answer from raw data.

## Comparison

Contrasts with recall/interpretation/literature-style biology benchmarks
(PubMedQA-style) that do not require empirical interaction with data. Contrasts
with method benchmarks ([[openproblems-benchmark]], [[scib-benchmark-pipeline]])
that score algorithm outputs rather than an agent's end-to-end analysis.

## When to use

When building or interpreting agentic benchmarks for data analysis where
answers must be automatically checkable, reproducible, and resistant to
shortcuts or label leakage.

## Known limitations

Deterministic graders necessarily discretize scientific judgment into
automatically checkable chunks, and each evaluation snapshots a single workflow
step rather than long-horizon iteration where errors compound. Subjective tasks
("interesting", "meaningful") without an operational definition are rejected.

## Open problems

- Calibrating tolerances so they neither reward shortcuts nor penalise valid
  methodological variation.
- Extending deterministic grading to multi-step, long-horizon workflows.

## Key papers

- [[scbench-evaluating-ai-agents-single-cell]] — defines the five grader families and the "specify what, not how" construction pipeline.

## My understanding

This is the methodological backbone that makes agent benchmarks comparable and
trustworthy; it is reusable far beyond scRNA-seq and is the part of scBench most
likely to be cited by future agent-evaluation work.
