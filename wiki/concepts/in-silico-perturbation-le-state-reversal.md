---
title: "In-silico Dynamo perturbation predicts drug efficacy via LE-state reversal"
aliases:
  - in silico drug perturbation cancer
  - Dynamo drug screen
  - LE state reversal drug response
  - LE outgoing transition probability drug
  - in silico cell-fate perturbation anticancer
  - dynamo high AAC LE reversal
  - in silico screen Alvocidib OSCC
  - dynamo drug perturbation pipeline
  - velocity-based drug efficacy prediction
tags: [in-silico-screen, drug-response, RNA-velocity, OSCC, leading-edge]
maturity: emerging
key_papers:
  - spatial-transcriptomics-reveals-distinct-conserved-tumor
first_introduced: "Arora & Cao et al. 2023 Nat Commun"
date_updated: 2026-05-22
related_concepts: []
---

## Definition
A pipeline that uses Dynamo vector-field perturbations on spatially deconvolved cancer cells to predict drug efficacy: drugs whose DGIdb-derived gene effects increase outgoing-LE transition probability (i.e. push LE-state cells back toward TC) are predicted to be effective. The prediction is calibrated against PharmacoDB AAC values across HPV-negative HNSCC cell lines.

## Intuition
If LE is the bad state and TC is the better state, then "good" drugs should push cells from LE → TC. Vector-field perturbation lets us simulate that push for any drug whose gene targets and directions are annotated.

## Variants
- AAC-stratified pipeline (high vs low AAC drugs at median 0.164)
- Class-stratified pipeline (drug-class level aggregation)
- Immunotherapy-target perturbations (anti-PD-1, anti-CTLA-4)

## Comparison
Connectivity-Map-style approaches compare drug-induced expression to a target signature; Dynamo perturbation differs by simulating the cell-fate consequence of a specific perturbation in the learned dynamics, rather than just signature similarity.

## When to use
- Prioritising drug candidates for OSCC or LE-driven tumours
- Re-purposing drugs whose original indication is unrelated (e.g. Alvocidib in AML → OSCC candidate)
- Generating mechanistic hypotheses for known-effective drugs

## Known limitations
- Dynamo perturbations remain unvalidated in vivo for OSCC
- Drugs with hits not annotated in DGIdb (140/417 in this paper) are silently dropped
- Several drug classes are underpowered (few drugs per class)

## Open problems
- Experimental validation of top hits (e.g. Alvocidib) in OSCC patient-derived models
- Extending the pipeline to combination drugs

## Key papers
- [[papers/spatial-transcriptomics-reveals-distinct-conserved-tumor]]

## My understanding
The most speculative part of the paper, but also the highest-leverage if it holds. It turns spatial transcriptomics from a descriptive into a generative tool for drug repurposing — provided the LE-outgoing → efficacy correlation generalises.
