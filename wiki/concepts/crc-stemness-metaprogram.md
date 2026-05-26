---
title: "CRC stemness metaprogram (LGR5/PROM1/ASCL2)"
aliases:
  - CRC stemness MP
  - colorectal cancer stemness program
  - intestinal stem-cell-like CRC signature
  - LGR5 stemness signature
  - CRC stem-like program
  - colorectal cancer stem cell program
  - ASCL2 stem program
  - intestinal stemness MP
tags: [crc, colorectal-cancer, stemness, metaprogram, lgr5, intestinal-stem-cell, scrna-seq]
maturity: emerging
key_papers:
  - curated-cancer-cell-atlas-provides-comprehensive
first_introduced: "2025 (Tyler et al., 3CA v2)"
date_updated: 2026-05-26
related_concepts: [recurrent-malignant-metaprograms-nmf, curated-cancer-cell-atlas-3ca]
---

## Definition

A recurrent malignant metaprogram capturing an intestinal stem-cell-like phenotype in colorectal cancer (CRC) cells. Anchored by canonical intestinal stem-cell markers **LGR5**, **PROM1 (CD133)**, **ASCL2** along with TESC, BAMBI, COL9A3, ASPSCR1, APCDD1, RNF43, SMOC2 and Wnt-target genes.

## Intuition

A subset of malignant cells in many CRC tumours adopt an LGR5+/ASCL2+ stem-like state reminiscent of normal intestinal crypt stem cells. The 3CA v2 expansion of CRC samples enabled detection of this MP as a distinct recurrent program for the first time; it had been suspected from prior CRC scRNA-seq work but was not previously captured as a pan-cohort MP.

## Variants

- High-LGR5 vs low-LGR5 sub-populations within the MP.
- Overlap with WNT-pathway activation signatures.
- Possible relation to BMI1+ reserve stem-cell states (not directly captured).

## When to use

- Score CRC malignant cells for stem-like character.
- Compare with bulk CRC stemness signatures (e.g. CMS4 subtypes).
- Distinguish proliferative-differentiated vs stem-like malignant cells in CRC.

## Known limitations

- Identified in 3CA v2 — needs independent validation in cohorts not in 3CA.
- Stemness markers overlap with normal intestinal stem cells; CNA inference required to confirm malignancy.
- The MP may capture multiple biological axes (Wnt-high, regenerative crypt-like, transit-amplifying).

## Key papers

- [[curated-cancer-cell-atlas-provides-comprehensive]] — first cross-study recurrent CRC stemness MP.

## My understanding

A clean example of how scale unlocks new MP detection: the CRC stemness signature only became visible once 3CA expanded CRC representation. The clinical relevance (LGR5+ cells drive metastasis and chemoresistance in CRC) makes this a high-value MP for follow-up.
