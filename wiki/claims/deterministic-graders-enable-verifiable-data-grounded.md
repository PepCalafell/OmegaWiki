---
title: "Deterministic graders enable verifiable, data-grounded scRNA-seq agent evaluation"
slug: deterministic-graders-enable-verifiable-data-grounded
status: supported
confidence: 0.85
tags:
  - benchmark
  - methodology
  - deterministic-grading
domain: methods
source_papers:
  - scbench-evaluating-ai-agents-single-cell
evidence:
  - source: scbench-evaluating-ai-agents-single-cell
    type: supports
    strength: strong
    detail: "Each of 394 problems pairs a data snapshot + natural-language task + deterministic grader scoring structured JSON pass/fail, via five grader families. 'Specify what, not how' + anti-shortcut hardening (strip X_pca/X_umap, cached labels) ensures answers require empirical data interaction."
conditions: "Five grader families; three evaluation types calibrate tolerances."
date_proposed: 2026-06-12
date_updated: 2026-06-12
---

## Statement

Pairing data snapshots and natural-language tasks with deterministic graders
(five grader families, "specify what, not how", anti-shortcut hardening) enables
verifiable, reproducible, data-grounded evaluation of analysis agents without
subjective interpretation.

## Evidence summary

Tolerances are calibrated by running multiple valid methods; precomputed
embeddings and cached labels are stripped so the agent must compute answers from
raw data. A deterministic linter blocks malformed evals.

## Conditions and scope

This is a methodological design claim; it asserts feasibility/utility of the
grading scheme, not a biological result.

## Counter-evidence

The authors note graders discretize scientific judgment and snapshot single
steps — a limitation, not a refutation, of verifiability.

## Linked ideas

## Open questions

How to extend deterministic grading to long-horizon, multi-step workflows.
