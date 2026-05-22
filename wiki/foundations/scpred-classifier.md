---
title: "scPred — probabilistic cell-type / spot classification on PC space"
slug: scpred-classifier
domain: methods/single-cell
status: mainstream
aliases:
  - scPred
  - scPred classifier
  - PCA-based single-cell classification
  - reference-based scRNA-seq classification
  - scPred SVM
  - scPred radial SVM
  - probability-based spatial spot classifier
first_introduced: "Alquicira-Hernandez 2019 Genome Biol"
date_updated: 2026-05-22
source_url: "https://github.com/powellgenomicslab/scPred"
---

## Definition
scPred trains supervised classifiers (typically radial SVMs) on informative principal components of a labelled reference scRNA-seq dataset and projects query cells (or ST spots) into that space, returning per-cell class probabilities.

## Intuition
Cell identity is encoded in low-dimensional PC structure; a discriminative model on those PCs generalises better than gene-wise classifiers and tolerates technical noise.

## Key variants
- Default radial SVM
- glm/ranger alternative model backends
- Spatial-spot adaptation: train on ST spot annotations rather than scRNA-seq

## Known limitations
- Requires a balanced and well-labelled reference
- Performance degrades when query cell types are absent from the reference
- Discrete labels lose continuity in cancer cell-state continua

## Open problems
- Probability calibration across batches
- Joint multimodal (RNA + protein + spatial) classification

## Relevance to active research
[[papers/spatial-transcriptomics-reveals-distinct-conserved-tumor]] uses scPred to project an OSCC TC/LE classifier onto 30 ST samples spanning 17 cancer types and demonstrate LE conservation.
