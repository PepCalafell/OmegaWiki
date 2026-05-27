---
title: "Ingenuity Pathway Analysis (IPA) — curated pathway and upstream-regulator inference"
slug: ingenuity-pathway-analysis
domain: methods/bioinformatics
status: mainstream
aliases:
  - IPA
  - Ingenuity Pathway Analysis
  - QIAGEN IPA
  - IPA canonical pathway analysis
  - IPA upstream regulator analysis
  - z-score pathway activation prediction
  - canonical signalling pathway enrichment
first_introduced: "QIAGEN/Ingenuity 2005"
date_updated: 2026-05-22
source_url: "https://digitalinsights.qiagen.com/products/ingenuity-pathway-analysis/"
---

## Definition
IPA is a commercial bioinformatics platform that maps DEG lists onto a curated knowledge base of canonical pathways, upstream regulators and disease/function networks, returning activation z-scores and overlap p-values.

## Intuition
Statistical enrichment on top of an expert-curated graph beats GO/KEGG for clinical and translational questions because the database explicitly encodes activation direction and regulator-target edges.

## Key variants
- Canonical pathway analysis (z-score and p-value of overlap)
- Upstream regulator analysis (predicted activation of TFs / drugs)
- Disease & function annotation
- Comparison analysis across samples

## Known limitations
- Commercial / closed knowledge base; reproducibility depends on database version
- Z-score interpretation requires care for small DEG lists
- Biased toward well-studied pathways and pharma-relevant targets

## Open problems
- Aligning IPA predictions with newer mechanistic graphs (Omnipath, SIGNOR)
- Calibrating z-scores against orthogonal experimental data

## Relevance to active research
[[papers/spatial-transcriptomics-reveals-distinct-conserved-tumor]] uses IPA to predict TC- and LE-specific canonical pathways (e.g. GP6, EIF2, HOTAIR in LE; MSP-RON, IL-33, p38 MAPK in TC) and upstream regulators (EHF, BCL3, SORL1, EGFR).

[[papers/multi-omics-profiling-cachexia-targeted-tissues]] uses IPA combined-omics analysis to integrate transcriptomics + metabolomics across five cachexia target tissues and to nominate LPS/inflammation, IL6 and TGFB1 as the top upstream regulators of cachexia metabolic reprogramming — the analytical step that bridged from the empirical multi-tissue one-carbon signature to the testable IL6 perturbation experiments.
