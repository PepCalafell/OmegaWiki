---
title: "PHF2 and PHF8 are negatively associated with cGAS activation; combined copy-number loss elevates it"
slug: phf2-phf8-negatively-associated-cgas-activation
status: weakly_supported
confidence: 0.6
tags: [PHF2, PHF8, cGAS, copy-number, genomic-instability, correlational]
domain: oncology / epigenetics
source_papers:
  - genomic-investigation-innate-sensing-pathways-tumor
evidence:
  - source: genomic-investigation-innate-sensing-pathways-tumor
    type: supports
    strength: moderate
    detail: "Among 11 genes strongly correlated with cGAS score, PHF2 and PHF8 (Jumonji-C demethylases) were negatively associated (Fig. 3A). Tumors losing both PHF2 copies + one PHF8 copy had significantly elevated cGAS activation; no tumor had both genes fully deleted (Fig. 3C)."
conditions: "Copy-number stratification in TCGA; single-gene copy-number gave inconsistent patterns — the effect emerges only for combined PHF2/PHF8 loss."
date_proposed: 2026-06-03
date_updated: 2026-06-03
---

## Statement

PHF2 and PHF8 transcript levels negatively correlate with tumor cGAS activation, and tumors with combined PHF2/PHF8 copy-number loss show elevated cGAS activation, consistent with these demethylases acting as genome stabilizers that limit cGAS-activating DNA damage.

## Evidence summary

Partial-correlation heatmap flagged PHF2/PHF8 among top cGAS-anticorrelated genes; combined copy-loss tumors had higher cGAS scores while single-gene stratification was inconsistent.

## Conditions and scope

Pan-cancer TCGA correlation/copy-number analysis controlling for purity and infiltrate; correlative evidence preceding the in vitro knockdown test.

## Counter-evidence

Single-gene copy-number alone did not consistently predict cGAS activation.

## Linked ideas

## Open questions

See [[concepts/phf-histone-demethylase-genomic-stability-cgas]] — is the genome-stability mechanism the cause of reduced cGAS activation?
