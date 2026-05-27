---
title: "scCellFie infers metabolic-task activities from single-cell and spatial transcriptomics at atlas scale via GPR-rule aggregation over GEMs"
slug: sccellfie-scales-metabolic-task-inference-to-single-cell-and-spatial
status: supported
confidence: 0.75
tags:
  - sccellfie
  - metabolic-task
  - GPR-rules
  - single-cell
  - spatial-transcriptomics
domain: "methods / metabolism"
source_papers:
  - atlas-scale-metabolic-activities-inferred-single
evidence:
  - source: atlas-scale-metabolic-activities-inferred-single
    type: supports
    strength: strong
    detail: "scCellFie ran on ~30M cells from CZI CELLxGENE (April 2024 snapshot) and on multiple Visium datasets (endometrium, endometriotic lesions, endometrial carcinoma); the framework integrates with Scanpy, uses precomputed CELLxGENE-derived thresholds, GPR rules (min over subunits, max over isoenzymes), and weighted task aggregation."
conditions: "Requires sufficient expression of metabolic genes; thresholds are CELLxGENE-derived and may need re-calibration for non-10x/non-human technologies. Transcript-level proxy assumes expression correlates with enzyme activity."
date_proposed: 2026-05-27
date_updated: 2026-05-27
---

## Statement

scCellFie infers the activity of 218 (human) / 203 (mouse) metabolic tasks from single-cell and spatial transcriptomics data by converting expression to gene scores via CELLxGENE-derived thresholds, then aggregating via gene–protein–reaction (GPR) rules and task-specific reaction weights. The method scales to ~30M cells while preserving biochemical interpretability through enzyme-complex (AND/min) and isoenzyme (OR/max) logic.

## Evidence summary

The original [[atlas-scale-metabolic-activities-inferred-single]] preprint validates the approach on (a) ovarian scRNA-seq where androgenic theca cells and granulosa cells recover known sex-hormone biosynthesis activities (Figure 2c), (b) the CELLxGENE atlas where organ-specific tasks recover known biology (lens glutathione, pancreatic amylase, adrenal adrenaline, hepatocyte taurocholate — Figures 3c,d), and (c) Visium datasets (endometrium, endometriotic lesions, EEC) where spatial patterns matched expected anatomy.

## Conditions and scope

Inference accuracy is bounded by GEM completeness, task-annotation curation, and the assumption that mRNA approximates enzyme activity. Best applied as a hypothesis generator coupled with orthogonal metabolomics or proteomics.

## Counter-evidence

No direct counter-evidence in the paper. The authors themselves note that mRNA-to-activity correspondence can break under post-transcriptional regulation or enzyme kinetics; lacks paired metabolomics validation in any dataset reported.

## Linked ideas

None yet.

## Open questions

- How well do scCellFie task scores correlate with paired single-cell metabolomics where available?
- What is the calibration of CELLxGENE-derived thresholds for non-10x technologies (SMART-seq, BD Rhapsody, snRNA-seq)?
- Can task scores be calibrated to absolute flux via FBA priors?
