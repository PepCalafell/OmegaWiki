---
title: "Mevalonate (MVA) pathway is a metabolic marker of endometrial epithelial cells in early secretory phase and is co-opted by malignant cells in endometrial carcinoma"
slug: mva-pathway-shared-marker-endometrial-epithelium-and-malignant-eec-cells
status: weakly_supported
confidence: 0.55
tags:
  - mevalonate
  - HMGCR
  - endometrial-carcinoma
  - cholesterol-biosynthesis
  - epithelial-cells
domain: "metabolism / oncology / endometrial-biology"
source_papers:
  - atlas-scale-metabolic-activities-inferred-single
evidence:
  - source: atlas-scale-metabolic-activities-inferred-single
    type: supports
    strength: moderate
    detail: "Figure 4c: MVA synthesis is a marker task of endometrial epithelial cells (luminal slightly higher than glandular) in HECA. Figures 7d, 8b: MVA synthesis is significantly associated with malignant-cell regions in EEC Visium data (scCellFie TF-IDF marker detection). Figure 6f: MVA synthesis active in luminal-epithelial-rich regions of peritoneal endometriotic lesions."
conditions: "Transcriptomic inference only. Pharmacological validation (statin / MVA-inhibitor effect on EEC organoids or models) not performed in this paper."
date_proposed: 2026-05-27
date_updated: 2026-05-27
---

## Statement

The mevalonate pathway — feeding cholesterol and ubiquinone biosynthesis via [[hmg-coa-reductase]] — is a marker of endometrial epithelial cells across the menstrual cycle (highest in luminal cells in early secretory phase) and is preserved as a marker of malignant cells in endometrial carcinoma (EEC) and luminal-epithelial-rich regions of peritoneal endometriotic lesions, consistent with reported MVA-pathway activation across cancers and with the antitumor activity of MVA inhibitors in ovarian carcinoma.

## Evidence summary

Three lines of inferred evidence in [[atlas-scale-metabolic-activities-inferred-single]]: (a) HECA scRNA-seq marker analysis ranks MVA synthesis as an epithelial marker (Fig 4c); (b) EEC Visium data show MVA synthesis significantly associated with malignant-cell regions (Fig 7d); (c) endometriotic-lesion Visium data show MVA synthesis active where luminal epithelial cells reside (Fig 6f). The authors connect this to prior MVA-pathway literature in cancer.

## Conditions and scope

Restricted to endometrial tissues studied (HECA, two endometriotic-lesion donors, one EEC dataset). No statin / MVA-inhibitor experiment was performed. Whether MVA activity is *causal* for malignant proliferation in EEC remains untested.

## Counter-evidence

None reported in this work; cross-cancer literature on MVA-pathway inhibitors (statins) is mixed.

## Linked ideas

None yet.

## Open questions

- Does statin or MVA-inhibitor treatment reduce proliferation or in-vivo growth of EEC organoids/PDX?
- Is MVA-pathway activation an early or late event in EEC tumorigenesis?
