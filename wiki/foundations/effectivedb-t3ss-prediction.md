---
title: "EffectiveDB (secretion system & effector prediction)"
slug: effectivedb-t3ss-prediction
domain: methods
status: mainstream
aliases:
  - EffectiveDB
  - Effective DB
first_introduced: ""
date_updated: 2026-05-28
source_url: ""
---

## Definition

EffectiveDB is a widely used bioinformatic resource and toolset for identifying
bacterial protein secretion systems (including T3SS) in genomes and for predicting
secreted effector proteins from sequence features.

## Intuition

Scans an annotated genome for the gene clusters encoding a complete secretion
apparatus and flags candidate substrate effectors by their characteristic
sequence signals.

## Formal notation

A genome is called "T3SS-complete" when the required apparatus components are detected;
prediction performance is benchmarked by cross-validation.

## Key variants

Complemented by machine-learning effector predictors and by jackhmmer/HMM-based
homology searches against large sequence databases (e.g. UniRef90).

## Known limitations

May miss divergent or atypical secretion systems, underestimating prevalence; effector
prediction has false positives/negatives that require experimental validation.

## Relevance to active research

Used to establish that ~79% of gut-commensal Pseudomonadota reference genomes encode
complete T3SS, motivating functional and interactome follow-up.
