---
title: "HepG2 — human hepatoblastoma/hepatocellular carcinoma cell line"
slug: hepg2-hepatoma-cell-line
domain: "cell biology / oncology models"
status: mainstream
aliases:
  - "HepG2"
  - "Hep-G2"
  - "CVCL_0027"
first_introduced: "Knowles et al. 1980"
date_updated: 2026-07-24
source_url: "https://www.cellosaurus.org/CVCL_0027"
---

## Definition

HepG2 is a widely used human liver cancer cell line derived in 1980 from the tumor of a 15-year-old male (originally described as hepatocellular carcinoma; later reclassified by some as hepatoblastoma). It retains many differentiated hepatic functions and is a standard model for hepatocyte metabolism, drug metabolism, and lipid/cholesterol biosynthesis studies.

## Intuition

A second, independent HCC-derived line used to test whether a phenotype seen in Huh7 reflects a general property of liver cancer cells rather than a Huh7 idiosyncrasy. In the source paper, HepG2 confirmed both the normoxic HIF-1α-dependence of glycolytic enzymes (HK2, GAPDH) and the cell-cycle-dependent transient normoxic HIF-1α expression.

## Formal notation

- Cellosaurus: CVCL_0027
- Culture: DMEM + 10% FBS
- HIF-1α silenced here via shRNA (pSuper-shHIF-1α) rather than CRISPR knockout

## Key variants

- Huh7 ([[huh7-hepatoma-cell-line]]) — the primary HCC model in the paper

## Known limitations

- Immortalized single-donor line; hepatoblastoma vs HCC classification ambiguity
- shRNA knockdown is partial (residual HIF-1α) versus complete CRISPR knockout

## Open problems

- Whether the shared Huh7/HepG2 normoxic HIF-1α metabolic dependency holds across the full spectrum of primary HCC

## Relevance to active research

Orthogonal HCC validation model supporting the paper's claim that normoxic HIF-1α control of glycolysis is a cancer-type property of hepatocellular carcinoma. Relevant to liver-cancer metabolism and hypoxia themes.
