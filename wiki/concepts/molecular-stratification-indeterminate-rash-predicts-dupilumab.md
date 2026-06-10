---
title: "Molecular stratification of indeterminate rashes predicts dupilumab response"
aliases:
  - CIR molecular endotyping
  - clinically indeterminate rash stratification
tags: [immunology, skin, scrna-seq, classification, dupilumab, precision-medicine]
maturity: emerging
key_papers:
  - classification-human-chronic-inflammatory-skin-disease
first_introduced: "Liu et al. 2022, Science Immunology"
date_updated: 2026-06-10
related_concepts: [trm1-th2-th17-molecular-classification-inflammatory, rashx-rash-classification-web-portal]
---

## Definition

Clinically/histopathologically indeterminate rashes (CIRs) — adult-onset rashes with overlapping eczematous and psoriasiform features that resist definitive AD-vs-PV diagnosis — can be molecularly stratified onto the AD↔PV axis using Trm1 disease-specific DEGs, and this molecular assignment tracks with response to the IL4R-blocking AD therapy dupilumab.

## Intuition

If a CIR's Trm1 transcriptome resembles AD (TH2-biased), it is predicted to respond to dupilumab; if it resembles PV (TH17-biased), it is predicted not to. Molecular class, not histopathology, carried the predictive signal in this initial test set.

## Formal notation

CIR samples scored on the (S_AD, S_PV) plane; proximity to AD vs PV centroid tested by one-sided Mann-Whitney. CIR-A, CIR-B, CIR-C stratified with AD; CIR-E, CIR-F with PV.

## Comparison

Notably, histopathology of CIRs did not predict their molecular class — the molecular signature is orthogonal to morphologic appearance.

## When to use

As a precision-medicine hypothesis generator for therapy selection in ambiguous inflammatory dermatoses; motivates larger prospective trials.

## Known limitations

- Very small test set (3 dupilumab-treated CIRs); associations are suggestive, not validated for clinical use.

## Open problems

- Prospective, blinded trials linking molecular class to therapeutic outcome across drug classes (IL4R, IL17, IL23 blockers).

## Key papers

- [[papers/classification-human-chronic-inflammatory-skin-disease]] — stratifies CIRs and links class to dupilumab response.

## My understanding

This is the clinical payoff narrative of the paper: it converts a descriptive classification into a testable treatment-selection hypothesis, but the evidence is anecdotal-scale and explicitly framed as proof-of-principle.
