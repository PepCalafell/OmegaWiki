---
title: "Tryptophan→kynurenine→AHR signaling is active in endometrial epithelial cells in health and is elevated in malignant regions of endometrial carcinoma"
slug: kynurenine-ahr-axis-active-endometrial-epithelium-and-elevated-in-eec
status: weakly_supported
confidence: 0.55
tags:
  - kynurenine
  - AHR
  - tryptophan-metabolism
  - endometrial-carcinoma
  - cell-cell-communication
domain: "metabolism / immuno-oncology / endometrial-biology"
source_papers:
  - atlas-scale-metabolic-activities-inferred-single
evidence:
  - source: atlas-scale-metabolic-activities-inferred-single
    type: supports
    strength: moderate
    detail: "Figure 4c,f,g: scCellFie infers high conversion of tryptophan to L-kynurenine / anthranilate / N-formylanthranilate in glandular and luminal epithelial subtypes of HECA, with strong inferred CCC scores via kynurenine→AHR; Visium of secretory endometrium shows co-localization of kynurenine synthesis and AHR expression in glands/lumen. Figures 7g,h, S8e,f: in EEC Visium, N-formylanthranilate synthesis shows the highest Pearson correlation with an EEC tumorigenesis signature and L-kynurenine→AHR CCC is significantly elevated in malignant regions."
conditions: "Inferred from transcriptomics only. Receptor expression used as a proxy for downstream signaling; no functional AHR-reporter or pharmacological perturbation reported."
date_proposed: 2026-05-27
date_updated: 2026-05-27
---

## Statement

The tryptophan→kynurenine→AHR signaling axis is active in healthy endometrial epithelial cells (supporting redox balance and inflammation control during cyclical remodeling) and is elevated in malignant regions of endometrial carcinoma, where N-formylanthranilate synthesis correlates most strongly with an EEC tumorigenesis gene signature and metabolite-mediated CCC scores for L-kynurenine→AHR are significantly increased.

## Evidence summary

In HECA scRNA-seq, glandular and luminal epithelial cells score highest for tryptophan→kynurenine/anthranilate/N-formylanthranilate. CCC scores between epithelial cell types reflect a coordinated potential for kynurenine signaling. In secretory-endometrium Visium, kynurenine synthesis and AHR co-localize in glands/lumen. In the EEC Visium dataset (Barkley et al. 2022), N-formylanthranilate synthesis from tryptophan shows the highest Pearson correlation with the EEC tumorigenesis score (signature: S100A9, S100A8, LCN2, CTS1, LTF, CXCL1, SAA1, SAA2), and L-kynurenine→AHR neighborhood-CCC scores are significantly higher in malignant regions. Connects to the [[ahr-ido1-tryptophan-axis]] foundation literature.

## Conditions and scope

All inferences are transcriptomic. Activity in EEC is shown for one Visium dataset; replication across additional EEC cohorts not performed. No metabolomic validation of kynurenine levels.

## Counter-evidence

Prior bulk metabolomics in endometrial cancer report elevated kynurenine consistent with the inference, but bulk measurements cannot disambiguate epithelial vs. immune origin.

## Linked ideas

None yet.

## Open questions

- Does pharmacological AHR antagonism or IDO1 inhibition slow EEC progression in PDX or organoid models?
- Is the kynurenine→AHR axis causally regulating endometrial-epithelial oxidative-stress response in health?
