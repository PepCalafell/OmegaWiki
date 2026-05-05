---
title: "IL4I1 macrophages are the in vivo correlates of in vitro mMAC1"
slug: il4i1-macrophages-vivo-correlates-mmac1
status: supported
confidence: 0.8
tags:
  - macrophage
  - IL4I1
  - tumor-microenvironment
  - signature-mapping
  - in-vivo
domain: "immunology"
source_papers:
  - nf-kb-tet2-promote-macrophage-reprogramming
evidence:
  - source: nf-kb-tet2-promote-macrophage-reprogramming
    type: supports
    strength: strong
    detail: "MoMac-VERSE projection: mMAC1 transcriptomic + C2 demethylation signatures preferentially enriched on cluster #6 IL4I1 Mac (and to lesser extent IL1B Mo, ISG Mo). Sorted IL4I1 MACs from primary OC recapitulate C2 hypomethylation; p65 motif most enriched in their demethylated CpGs; RELA + HIF1A regulons up-regulated only in IL4I1 vs TREM2/FOLR2."
conditions: "Primary OC tissue MACs sorted by flow cytometry; MoMac-VERSE atlas projection."
date_proposed: 2026-05-05
date_updated: 2026-05-05
---

## Statement

In vitro hypoxic LPS-activated MACs (mMAC1) correspond most closely in vivo to IL4I1⁺ MACs in human tumor tissues, sharing transcriptomic signature, NF-κB-driven C2 DNA demethylation, p65 motif enrichment in demethylated CpGs, and elevated RELA + HIF1A regulon activity.

## Evidence summary

- mMAC1 gene expression signature enriched on MoMac-VERSE cluster #6 (IL4I1 Mac), as well as #15 (IL1B Mo) and #4 (ISG Mo) (Fig. 5A-C).
- C2-associated genes enriched in the same MoMac-VERSE clusters.
- Sorted IL4I1 MACs from primary ovarian carcinoma show lowest C2 methylation among all sorted populations (Fig. 5J).
- p65 motif most enriched in demethylated CpGs specific to IL4I1 (Fig. 5K).
- RELA and HIF1A regulons up-regulated only in IL4I1 (not in TREM2 or FOLR2) MACs (Fig. 5L).

## Conditions and scope

- Validation in OC; bladder cancer scRNA-seq used for cell-cell communication but not population sorting.
- The "correspondence" is signature-level and does not imply identical ontogeny.

## Counter-evidence

- IL1B Mo and ISG Mo also enrich for mMAC1 signatures, suggesting partial mapping rather than 1:1 correspondence.
- IL4I1 MACs have additional features (efferocytosis, cited 42) not directly captured by the in vitro mMAC1 model.

## Linked ideas

(none yet)

## Open questions

- Are IL4I1 MACs always derived from monocytes, or can tissue-resident MACs adopt the IL4I1 state?
- Does forced p65 activation in normoxic MACs phenocopy the IL4I1 epigenetic signature?
- Tissue-of-residence-specific variants of IL4I1 MACs across cancers.
