---
title: "Tahoe-100M — giga-scale single-cell perturbation atlas"
slug: tahoe-100m-single-cell-perturbation-atlas
domain: data / single-cell
status: mainstream
aliases:
  - Tahoe-100M
  - Tahoe dataset
  - Tahoe
first_introduced: "Zhang et al. 2025 bioRxiv (Tahoe-100M)"
date_updated: 2026-05-28
source_url: "https://www.biorxiv.org/content/10.1101/2025.02.20.639398"
---

## Definition

Tahoe-100M is a giga-scale single-cell perturbation atlas comprising on the order of 100 million single-cell transcriptomes profiling drug perturbations across many cancer cell lines, designed to study context-dependent gene function and to train large cellular models. It provides both perturbed profiles and unperturbed baselines at unprecedented scale.

## Intuition

Most perturbation datasets are small and context-narrow. Tahoe-100M scales drug-perturbation single-cell profiling to ~100M cells, giving foundation/world models enough interventional data to learn generalizable dynamics.

## Formal notation

n/a (dataset).

## Key variants

- Perturbed (drug) profiles vs unperturbed baseline samples (used for base-model pretraining).

## Known limitations

- Cancer-cell-line-centric; in-vitro context may limit transfer to primary tissue.

## Open problems

- Coverage of primary/in-vivo contexts and genetic (vs chemical) perturbations.

## Relevance to active research

A major training corpus for AlphaCell: ~80M perturbed profiles feed the Flow Model and ~80M baseline profiles contribute to the 220M-cell Base Model; also one of the three benchmark datasets (large-scale drug perturbation).
