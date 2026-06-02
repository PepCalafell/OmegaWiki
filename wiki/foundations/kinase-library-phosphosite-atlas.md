---
title: "The Kinase Library — substrate-specificity atlas for kinase prediction"
slug: kinase-library-phosphosite-atlas
domain: methods
status: mainstream
aliases:
  - Kinase Library
  - kinase library
  - serine/threonine kinome atlas
  - tyrosine kinome atlas
first_introduced: "Johnson et al. 2023 Nature (Ser/Thr kinome atlas); Yaron-Barir et al. 2024 Nature (Tyr kinome atlas)"
date_updated: 2026-06-02
source_url: "https://kinase-library.phosphosite.org/"
---

## Definition

The Kinase Library is a prediction tool, built on a systematic synthetic-peptide screen of the human kinome's substrate specificities, that scores and ranks the most likely upstream kinases for a given phosphosite based on the amino-acid sequence motif surrounding the phosphorylated residue. It is hosted at phosphosite.org.

## Intuition

Rather than relying on observed kinase–substrate annotations (which are sparse), the Kinase Library learns each kinase's preferred substrate motif from peptide screens, so any phosphosite sequence can be matched to candidate kinases — enabling motif-based "kinase activity footprinting" from phosphoproteomics data.

## Formal notation

- Inputs: phosphosite sequence windows (centered on the phospho-residue)
- Per-kinase position-specific scoring matrices from synthetic-peptide screens
- Output: ranked upstream kinases; enrichment of upregulated phosphosites tested (e.g. one-sided Fisher's exact test with BH correction)

## Key variants

- Serine/threonine kinome atlas (Johnson 2023) and tyrosine kinome atlas (Yaron-Barir 2024)
- Motif-based prediction vs knowledge-based (curated) kinase–substrate inference

## Known limitations

- Motif-only prediction ignores context (localization, scaffolds, co-expression)
- Closely related kinases share motifs, limiting individual-kinase resolution
- Predicts capability, not whether the kinase is expressed/active in the sample

## Open problems

- Integrating motif predictions with abundance/expression to improve specificity
- Resolving kinase families with overlapping substrate preferences

## Relevance to active research

Used to infer upstream kinases from phosphoproteomic footprints of primary human macrophages — recovering known M1 routes (JNK1/2/3, p38) and nominating novel immunosuppressive-state kinases (e.g. IRAK1/4 in M2a; CAMKK2/GAK in M2c).
