---
title: "STING TME outcomes are context- and cell-type-dependent"
aliases:
  - compartmentalized STING signaling
  - STING TME cell-type heterogeneity
  - context-dependent STING activation
tags:
  - cgas-sting
  - tumor-microenvironment
  - cell-type-specificity
  - innate-immunity
maturity: stable
key_papers:
  - targeting-sting-generate-therapeutic-anti-tumor
first_introduced: "2014"
date_updated: 2026-05-27
related_concepts: []
---

## Definition

The functional outcome of STING pathway activation in the tumor microenvironment is not uniform — it varies by (a) cell type (tumor, myeloid, T cell, NK cell, CAF, endothelial), (b) acute vs chronic activation, and (c) extrinsic (paracrine cGAMP) vs intrinsic (intrinsic dsDNA sensing) engagement. The same STING agonist can produce antitumor immunity in DCs/ECs/NK while simultaneously inducing T-cell death and chronic pro-tumor NF-κB output in tumor cells.

## Intuition

Tumor and TME cell types each impose their own "filter" on STING output: DCs upregulate antigen cross-presentation, macrophages polarize toward M1, ECs upregulate adhesion molecules to traffic immune cells, NK cells gain cytotoxicity, T cells undergo apoptosis or impaired proliferation, CAFs produce CXCR3 ligands, tumor cells either silence the pathway or chronically engage non-canonical NF-κB.

## When to use

When interpreting clinical STING-agonist failures or designing combination strategies. Effective therapy requires *cell-type-targeted* delivery (ADCs, masked antibodies, exosomes) or *cell-type-specific protection* (e.g., engineering STING-agonist-resistant CAR T cells).

## Open problems

- How to deliver STING agonists selectively to DCs, ECs, or NK cells while sparing T cells
- How to dose temporally so that acute TME activation precedes adoptive T cell therapy without bystander T-cell death

## Key papers

- [[papers/targeting-sting-generate-therapeutic-anti-tumor]] — central thesis: STING TME outcomes are compartmentalized and divergent

## My understanding

This is the defining conceptual update in the cGAS-STING field over the last 5 years and the framing that re-organizes all subsequent therapeutic strategy. The old model ("STING agonism = anti-tumor immunity") is wrong; the right model is "STING agonism = a context-dependent reweighting of cell-type-specific outputs whose net direction depends on TME composition and delivery method."
