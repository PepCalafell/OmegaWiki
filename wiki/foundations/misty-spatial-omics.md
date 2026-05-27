---
title: "MISTy — Multiview Intercellular SpaTial modeling framework"
slug: misty-spatial-omics
domain: "methods / spatial-transcriptomics / cell-cell-interaction"
status: mainstream
aliases:
  - "MISTy"
  - "mistyR"
first_introduced: "Tanevski et al. Genome Biology 2022"
date_updated: 2026-05-27
source_url: "https://github.com/saezlab/mistyR"
---

## Definition

MISTy is a multi-view machine-learning framework that predicts intra-tissue marker expression as a function of three spatial views: intraview (same spot), juxtaview (direct neighbors), and paraview (extended neighborhood via Gaussian kernel). Per-view random-forest regressors are combined to estimate marker-importance contributions of each view, yielding interpretable functional spatial interactions.

## Intuition

Decomposes a marker's spatial behavior into "what is at this spot", "what is right next to it", and "what is in the broader local zone". The trade-off: random-forest importance is unsigned, making it harder than NiCo's logistic-regression coefficients to read out positive vs negative interactions.

## Known limitations

- Importance scores from random forests do not encode interaction sign.
- Paraview Gaussian-kernel radius is a manual hyperparameter.
- Benchmarked by NiCo as less consistent with simulated cell-type interaction strengths than NiCo's logistic regression module.

## Relevance to active research

Most directly comparable peer to NiCo's "Interactions" module; widely used for spatial cell-cell interaction inference in Saez-Rodriguez lab pipelines.
