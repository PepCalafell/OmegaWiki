---
title: "snRNA-seq vs scRNA-seq metaprogram differences"
aliases:
  - snRNA-seq vs scRNA-seq programs
  - single-nucleus vs single-cell metaprogram
  - snRNA-seq cell-cycle MP
  - snRNA-seq cilia MP
  - nucleus-vs-cytosol transcript distribution
  - frozen-tissue snRNA-seq programs
  - snRNA-seq-specific MP
  - protocol-dependent metaprogram
tags: [snrna-seq, scrna-seq, metaprograms, frozen-tissue, technical-comparison]
maturity: emerging
key_papers:
  - curated-cancer-cell-atlas-provides-comprehensive
first_introduced: "2025 (Tyler et al., 3CA v2)"
date_updated: 2026-05-26
related_concepts: [recurrent-malignant-metaprograms-nmf, curated-cancer-cell-atlas-3ca]
---

## Definition

Systematic differences between recurrent malignant metaprograms recovered from snRNA-seq (single-nucleus) vs scRNA-seq (whole-cell) samples in the 3CA compendium. snRNA-seq samples disproportionately contribute to a distinct cell-cycle MP and a second cilia MP not seen in scRNA-seq.

## Key findings (Tyler et al. 2025)

- A largely **snRNA-seq-specific cell-cycle MP** correlates and partially overlaps with the standard scRNA-seq-derived G1/S and G2/M MPs but is its own cluster.
- A **second cilia MP** appears mostly in snRNA-seq samples, containing cilia-associated genes (HYDIN, RFX3, CFAP44, DNAH7) absent from the scRNA-seq cilia MP.
- Other MPs (NPC/OPC, Unfolded protein response, Stress, EMT, etc.) also show variant pairs across protocols.

## Mechanistic interpretation

Authors suggest two non-exclusive explanations:
1. **Biological**: nuclear transcript distribution differs from cytosolic — nuclear-retained or nascent transcripts (e.g. introns of cilia-related genes, replication-coupled cell-cycle transcripts) are over-represented in snRNA-seq.
2. **Compositional**: snRNA-seq disproportionately samples frozen-tissue cohorts and certain cancer types (e.g. brain, breast snRNA-seq cohorts) which skews the MP detection.

## When to apply this caveat

- When pooling snRNA-seq and scRNA-seq data in a single analysis.
- When mapping a new dataset's programs to the 3CA MP catalogue — match protocol-specific MP variants where available.
- When interpreting cell-cycle scoring in snRNA-seq cohorts (frozen-tissue clinical samples).

## Known limitations

- Hard to fully separate biological vs compositional drivers given current cohort sizes.
- snRNA-seq cell-cycle scoring may require its own signature, not the canonical scRNA-seq G1/S/G2/M panel.

## Key papers

- [[curated-cancer-cell-atlas-provides-comprehensive]] — first systematic side-by-side MP comparison.

## My understanding

Critical for any pan-cancer scRNA/snRNA-seq pooled analysis. The practical takeaway: keep protocol as a covariate, and consider running MP discovery separately by protocol before merging.
