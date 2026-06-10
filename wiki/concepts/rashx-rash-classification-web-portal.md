---
title: "RashX — web portal for patient-level rash scRNA-seq classification"
aliases:
  - RashX
tags: [resource, tool, skin, scrna-seq, classification, web-portal]
maturity: active
key_papers:
  - classification-human-chronic-inflammatory-skin-disease
first_introduced: "Liu et al. 2022, Science Immunology"
date_updated: 2026-06-10
related_concepts: [trm1-th2-th17-molecular-classification-inflammatory, molecular-stratification-indeterminate-rash-predicts-dupilumab]
---

## Definition

RashX (https://rashX.ucsf.edu) is a proof-of-principle web interface that places a user's individual rash scRNA-seq dataset into the Trm1 TH2/TH17 AD-PV stratification framework. It accepts standard 10x Genomics immune-cell matrices (RDS format), identifies cells most similar to the reference Trm1 population, performs differential expression of Trm1 disease-specific genes against the study's healthy-control Trm1 cells, and returns heatmaps and a hyperdimensionality plot positioning the sample on the AD↔PV axis.

## Intuition

It operationalizes the paper's classification method as a shared community resource, so any lab can map a new rash sample onto an existing large reference without re-deriving the signature.

## Variants

- Ships with example AD and PV input matrices that segregate to their parent classes as a demonstration.

## When to use

When a researcher or clinician has scRNA-seq from an individual rash and wants to position it within the TH2/TH17 reference framework for endotyping or hypothesis generation.

## Known limitations

- Proof-of-principle scale; requires scRNA-seq input (not routine clinical data) and depends on the original reference cohort.

## Open problems

- Extending input to spatial or bulk modalities and to larger, multi-center reference cohorts.

## Key papers

- [[papers/classification-human-chronic-inflammatory-skin-disease]] — introduces RashX as the deployable interface to its classification framework.

## My understanding

RashX is the translational hook of the paper — a resource/tool that turns the Trm1 signature into something other groups can actually run.
