---
title: "ESTIMATE — Stromal and Immune Score Algorithm"
slug: estimate-stromal-immune-score
domain: methods
status: mainstream
aliases:
  - ESTIMATE
  - ESTIMATE algorithm
  - stromal score
  - immune score
  - tumor purity estimation
  - ESTIMATE immune-stromal scoring
first_introduced: "Yoshihara et al. 2013 Nat Commun"
date_updated: 2026-05-25
source_url: "https://bioinformatics.mdanderson.org/public-software/estimate/"
---

## Definition
A gene-signature method that scores bulk tumour samples for stromal and immune-cell content using single-sample gene set enrichment of curated stromal and immune signatures. Combined with a tumour-purity estimate, ESTIMATE separates malignant from microenvironment contributions to bulk tissue measurements.

## Intuition
Bulk expression confounds tumour and microenvironment. ESTIMATE recovers a stromal- and immune-content estimate per sample from canonical gene-signature enrichment, which can then be used as a sample-level covariate or stratifier.

## Formal notation
- Stromal score = ssGSEA(stromal signature, sample)
- Immune score = ssGSEA(immune signature, sample)
- ESTIMATE score = stromal + immune
- Tumour purity ≈ f(ESTIMATE score)

## Key variants
- Pan-cancer TCGA ESTIMATE scores
- ESTIMATE applied to bulk proteomes (e.g., TPCPA pan-cancer landscape)

## Known limitations
- Trained on transcriptomic data; protein-level application is an extrapolation.
- Signatures may not capture niche-specific stromal or immune subsets.

## Open problems
- Protein-trained ESTIMATE signatures for direct application to MS proteomes.

## Relevance to active research
ESTIMATE remains the default first-pass immune / stromal scoring tool for bulk tumour cohorts and is now being applied to bulk proteomes to quantify TME composition without dedicated deconvolution.
