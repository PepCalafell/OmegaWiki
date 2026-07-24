---
title: "HeLa — human cervical carcinoma cell line"
slug: hela-cell-line
domain: "cell biology / oncology models"
status: mainstream
aliases:
  - "HeLa"
  - "HeLa S3"
  - "CVCL_0058"
first_introduced: "Gey, Coffman & Kubicek 1952"
date_updated: 2026-07-24
source_url: "https://www.cellosaurus.org/CVCL_0030"
---

## Definition

HeLa is the first human immortalized cell line, established in 1951 from the cervical adenocarcinoma of Henrietta Lacks. It is the most widely used mammalian cell line in biology. The HeLa_S3 clone (CVCL_0058) used in the source paper is a suspension-adapted subline that, in this study's hands, **does not detectably express endogenous HIF-2α** (only HIF-1α).

## Intuition

Serves as a non-hepatic comparison to Huh7: HeLa cells depend on HIF-1α to adapt to hypoxia but — unlike HCC cells — do NOT require HIF-1α for growth or metabolic maintenance under normoxia. This contrast is what isolates the cell-type-specific normoxic HIF-1α phenotype of liver cancer cells.

## Formal notation

- Cellosaurus: HeLa CVCL_0030; HeLa S3 subclone CVCL_0058
- HPV18-positive; p53 and Rb functionally inactivated by viral oncoproteins
- Culture: DMEM + 10% FBS

## Key variants

- HeLa HIF1A⁻/⁻ — CRISPR/Cas9 knockout derivative (previously reported by the same group)
- HeLa cells stably expressing GFP or GFP-HIF-1α for rescue experiments

## Known limitations

- Extensively cross-contaminated and karyotypically unstable across labs; subclone-dependent phenotypes (e.g. HIF-2α expression) must be verified per stock
- Cervical, non-hepatic origin — not a liver-cancer model

## Open problems

- Which coactivator/isoform repertoire differences underlie HeLa's lack of a normoxic HIF-1α growth requirement

## Relevance to active research

Negative-control cell line establishing that the normoxic HIF-1α dependency is HCC-specific, not a universal cancer property. Broadly relevant across the vault as a standard reference line.
