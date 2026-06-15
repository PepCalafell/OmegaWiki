---
title: "dN/dS positive selection inference"
slug: dn-ds-positive-selection-inference
domain: "genomics"
status: mainstream
aliases:
  - dN/dS
  - dNdS
  - Ka/Ks
  - nonsynonymous-to-synonymous ratio
  - dNdScv
first_introduced: "1986"
date_updated: 2026-06-15
source_url: "https://en.wikipedia.org/wiki/Ka/Ks_ratio"
---

## Definition

dN/dS is the ratio of nonsynonymous (amino-acid-changing) to synonymous (silent) substitution rates per site. dN/dS > 1 indicates positive (Darwinian) selection on a gene; ≈1 neutral; <1 purifying selection. In cancer genomics, methods such as dNdScv estimate per-gene dN/dS from somatic mutations to detect driver genes under positive selection.

## Intuition

If a gene accumulates protein-changing mutations far faster than silent ones, those changes are likely being favored (selected), flagging it as a driver under the prevailing selective pressure.

## Key variants

- Sequence-evolution dN/dS (germline, across species)
- Somatic dNdScv (cancer driver detection)

## Known limitations

Sensitive to mutation-rate covariates and sample size; extreme ratios for low-mutation genes require careful significance testing (q-values).

## Open problems

- Calibration in small, tissue-specific cohorts

## Relevance to active research

In Arenillas et al., dN/dS identified EPAS1 as the sole gene under strong positive selection in CCHD-PPGL (dN/dS = 702; 926 in the sympathetic subcohort).
