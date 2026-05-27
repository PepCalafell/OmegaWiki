---
title: "An atlas of metabolic-task activities across ~30M CELLxGENE cells recovers known organ- and cell-type-specific metabolic functions"
slug: cellxgene-atlas-recovers-organ-and-cell-type-specific-metabolic-functions
status: supported
confidence: 0.7
tags:
  - cellxgene
  - metabolic-atlas
  - lens
  - hepatocyte
  - adrenal
  - pancreas
domain: "metabolism / single-cell atlases"
source_papers:
  - atlas-scale-metabolic-activities-inferred-single
evidence:
  - source: atlas-scale-metabolic-activities-inferred-single
    type: supports
    strength: moderate
    detail: "Figure 3c,d: glutathionate synthesis peaks in lens fiber cells; starch degradation peaks in pancreatic acinar cells; adrenaline production peaks in sympathetic neurons + chromaffin cells (adrenal gland); taurocholate synthesis peaks in hepatocytes (liver). Atlas covers 2,195 cell-type × organ combinations."
conditions: "April 2024 CELLxGENE snapshot; cell types with <50 cells per organ excluded. Recovery shown qualitatively against literature priors; no quantitative benchmark vs. tissue metabolomics."
date_proposed: 2026-05-27
date_updated: 2026-05-27
---

## Statement

Applying scCellFie to ~30 million cells across 668 datasets in the CZI CELLxGENE human cell atlas yields a metabolic atlas spanning 2,195 cell-type × organ combinations that recapitulates known organ- and cell-type-specific biochemical functions (e.g. lens-fiber glutathione, pancreatic-acinar amylase/starch degradation, adrenal chromaffin adrenaline, hepatocyte bile-acid synthesis).

## Evidence summary

Selected confirmatory cases include glutathionate synthesis in eye→lens fiber cells (oxidative-stress defence in transparent tissue), starch-degradation in pancreatic acinar cells (digestive amylase production), adrenaline biosynthesis in adrenal sympathetic neurons + chromaffin cells, and taurocholate synthesis in liver hepatocytes. The atlas is browsable at https://www.sccellfie.org.

## Conditions and scope

Cross-tissue absolute comparison of metabolic scores is discouraged by the authors — scores are interpretable within-task across cell types. Coverage limited to tasks defined in scCellFie's database.

## Counter-evidence

No quantitative benchmark vs. tissue metabolomics is presented. Many additional tasks may also show organ-specific enrichment unrelated to known biology that the authors did not annotate as false positives.

## Linked ideas

None yet.

## Open questions

- How many of the 2,195 cell-type × organ × task combinations would replicate on an updated CELLxGENE snapshot or on Tabula Sapiens / HCA equivalents?
- Are the recovered patterns robust to choice of expression threshold and to integration strategy?
