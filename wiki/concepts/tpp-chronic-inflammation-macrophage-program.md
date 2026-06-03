---
title: "TPP chronic-inflammation macrophage program"
aliases:
  - TPP macrophage program
  - MTPP macrophages
  - TNF PGE2 P3C macrophage activation
tags:
  - macrophage
  - immunology
  - chronic-inflammation
  - STAT4
maturity: emerging
key_papers:
  - transcriptome-based-network-analysis-reveals-spectrum
  - transcriptional-regulator-network-human-inflammatory-macrophages
first_introduced: "Xue et al. 2014 Immunity"
date_updated: 2026-06-03
related_concepts:
  - spectrum-model-macrophage-activation
  - m1-m2-polarization-paradigm
---

## Definition
A distinct human macrophage activation program induced by the combination of TNF, prostaglandin E2 (PGE2), and the TLR2 ligand Pam3CSK4 (P3C) — abbreviated TPP (or MTPP for the resulting macrophages). It is transcriptionally, phenotypically, and functionally separable from both M1 (IFN-γ) and M2 (IL-4) macrophages and is associated with chronic granulomatous inflammation.

## Intuition
TPP mimics a chronic-inflammatory microenvironment (e.g. tuberculosis/granulomatous tissue) better than single canonical cytokines. Macrophages exposed to it occupy a region of the activation spectrum that the bipolar M1/M2 axis cannot describe, and they acquire a unique surface phenotype, secretome, miRNA profile, and a STAT4-driven transcriptional signature.

## Formal notation
- Stimulus: TNF + PGE2 + P3C (TLR2 ligand); WGCNA modules 30, 32, 33 positively correlated
- Surface markers elevated vs M1/M2/Mb: CD14, CD23, CD25, CXCR7, CD197 (51 markers total)
- TF: STAT4 (selectively induced); secretome: CXCL5 (strong), IL-1α (unique)
- miRNA: elevated hsa-miR-125a-5p

## Variants
- MTPP (TPP applied to baseline macrophages)
- TPP+IFN-β, MTTP-related chronic-inflammation cocktails in the resource

## Comparison
vs M1 (IFN-γ / STAT1): TPP lacks the IFN-γ inflammatory module 8 signature; shares only partial overlap (CD86). vs M2 (IL-4 / STAT6): TPP is not anti-inflammatory and is more T-cell-suppressive.

## When to use
- Modeling chronic / granulomatous inflammation in vitro
- As a concrete example that the macrophage spectrum contains non-M1/M2 programs

## Known limitations
- Defined in vitro from monocyte-derived macrophages; in-vivo prevalence not established here.
- STAT4's downstream macrophage targets remain uncharacterised.

## Open problems
- The mechanistic role of macrophage STAT4 in granulomatous disease.
- Whether TPP-like programs appear in human tissue macrophages.

## Key papers
- [[papers/transcriptome-based-network-analysis-reveals-spectrum]] — Xue et al. 2014: defined and functionally characterised the TPP/MTPP program.

## My understanding
TPP is the paper's flagship example proving the spectrum model has teeth — a reproducible, functionally distinct, STAT4-marked program that simply does not fit M1/M2. Useful as a citable instance of macrophage states beyond the binary.
