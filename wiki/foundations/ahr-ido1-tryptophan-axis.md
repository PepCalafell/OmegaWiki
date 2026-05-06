---
title: "AHR / IDO1 / IL4I1 tryptophan-degradation immunosuppression axis"
slug: ahr-ido1-tryptophan-axis
domain: "immunology / metabolism"
status: mainstream
aliases:
  - "AhR-IDO1 axis"
  - "tryptophan-kynurenine pathway"
  - "IDO1 immune checkpoint"
  - "aryl hydrocarbon receptor signalling"
  - "kynurenine immunosuppression"
  - "IL4I1 tryptophan degradation"
  - "tryptophan catabolism in tumours"
  - "Trp-Kyn-AhR axis"
  - "AhR metabolic immune checkpoint"
first_introduced: "Mellor & Munn 1999 (IDO1 immunosuppression); Sadik et al. 2020 (IL4I1/AHR)"
date_updated: 2026-05-06
source_url: "https://www.uniprot.org/uniprotkb/P14902/"
---

## Definition

A metabolic immune-checkpoint axis in which the enzymes IDO1 (indoleamine 2,3-dioxygenase 1) and IL4I1 (interleukin-4-induced gene 1, an L-amino-acid oxidase) deplete extracellular tryptophan and produce kynurenine-pathway and indole-pathway metabolites that activate the aryl hydrocarbon receptor (AHR). AHR activation suppresses effector T-cell function, induces FOXP3⁺ regulatory T cells, and reprograms myeloid cells toward an immunosuppressive phenotype.

## Intuition

T cells are exquisitely sensitive to tryptophan deprivation (via GCN2 stress response and mTOR shutdown) and to AHR-binding catabolites. By co-expressing IDO1 + IL4I1 + tryptophan transporters, certain tumour-associated macrophages turn local tryptophan metabolism into a soluble immunosuppressive shield around the tumour.

## Key variants

- IDO1 — tryptophan → N-formyl-kynurenine (canonical, IFNγ-induced)
- IDO2 — paralog, weaker activity, distinct expression
- TDO2 — hepatic and tumour-cell tryptophan dioxygenase
- IL4I1 — phenylalanine/tryptophan oxidase producing indole pyruvate / H₂O₂; identified by Sadik et al. 2020 as a more potent AHR activator than IDO1

## Known limitations

- IDO1 inhibitor monotherapy (epacadostat) failed in late-phase melanoma trials; combination strategies are actively explored
- Cell-type-specific contributions of IDO1 vs IL4I1 vs TDO2 are still being mapped
- AHR has both immunosuppressive and immune-promoting effects depending on ligand and context

## Open problems

- Whether co-targeting IL4I1 + IDO1 outperforms either alone in patients
- Mapping the tryptophan-metabolite gradient at single-cell, spatial resolution
- AHR ligand specificity in tumour microenvironment vs gut / barrier tissues

## Relevance to active research

[[papers/cross-tissue-single-cell-landscape-human]] characterises the IL4I1⁺PD-L1⁺IDO1⁺ macrophage subset (MoMac-VERSE cluster #6) as the dominant cellular substrate of this axis in human tumours. The authors propose that CD40L (from CD4⁺ T cells) plus IFNγ (from CD8⁺ T cells) reprograms IFN-primed monocytes into IL4I1_Mac, which then suppress T-cell function via PD-L1/PD-L2 and tryptophan catabolism, and recruit FOXP3⁺ Tregs through CXCL9/CXCL10/CXCL11. This frames IL4I1_Mac and the AHR-IDO1 axis as the mechanistic substrate of the immunosuppressive tumour periphery.
