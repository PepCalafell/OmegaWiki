---
title: "High-AAC anticancer drugs induce LE→TC state reversal in Dynamo in-silico perturbation, vs low-AAC controls"
slug: dynamo-effective-drugs-induce-le-state-reversal
status: weakly_supported
confidence: 0.6
tags: [pharmacological, Dynamo, RNA-velocity, OSCC, in-silico]
domain: oncology/drug-response
source_papers:
  - spatial-transcriptomics-reveals-distinct-conserved-tumor
evidence:
  - source: spatial-transcriptomics-reveals-distinct-conserved-tumor
    type: supports
    strength: moderate
    detail: "Dynamo perturbation across 70 DGIdb-annotated, PharmacoDB-stratified drugs shows that high-AAC drugs (median 0.164) significantly increase outgoing-LE transition probabilities relative to low-AAC drugs (p<0.05). Effective drugs reverse baseline LE flow; ineffective drugs preserve it. TC incoming probability difference is not significant (p>0.05)."
conditions: "417 drugs filtered to 140 with DGIdb gene effects and ≥25 HPV-negative HNSCC cell lines; 70 retained for analysis"
date_proposed: 2026-05-22
date_updated: 2026-05-22
---

## Statement
In silico Dynamo perturbations across a curated drug panel show that effective drugs (high AAC) reverse the LE→TC cell-fate flow direction, supporting LE-state reversal as a candidate mechanism of efficacy.

## Evidence summary
Fig. 6e–l; Supplementary Fig. 6 and Supplementary Data 7.

## Conditions and scope
HPV-negative HNSCC cell lines; PharmacoDB-derived AAC values; DGIdb-annotated drug-gene effects; no in-vivo validation in this paper.

## Counter-evidence
Outliers in the effective-drug set; TC incoming probabilities do not differ significantly; several drug classes are underpowered.

## Linked ideas

## Open questions
Whether top hits (e.g. Alvocidib) show LE-reducing effects in OSCC PDX or organoid models.
