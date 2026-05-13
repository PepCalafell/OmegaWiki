---
title: "TREM2 — triggering receptor expressed on myeloid cells 2"
slug: trem2-receptor
domain: "immunology / cell-biology"
status: mainstream
aliases:
  - "TREM2"
  - "triggering receptor expressed on myeloid cells 2"
  - "Trem2"
  - "lipid-sensing macrophage receptor"
  - "DAP12-coupled myeloid receptor"
  - "TREM2/DAP12 signaling"
  - "TREM2 receptor"
  - "TREM2 lipid receptor"
first_introduced: "Bouchon et al. 2000 (gene cloning); Daws et al. 2003 (DAP12 coupling)"
date_updated: 2026-05-06
source_url: "https://www.uniprot.org/uniprotkb/Q9NZC2/"
---

## Definition

TREM2 is a single-pass type-I transmembrane immunoglobulin-superfamily receptor expressed predominantly on myeloid cells (microglia, alveolar macrophages, osteoclasts, dendritic cells, tumor-associated macrophages, lipid-associated macrophages). It signals through the ITAM-bearing adaptor DAP12 (TYROBP), driving downstream SYK / PI3K / mTOR / β-catenin activity.

## Intuition

TREM2 is the canonical "lipid-sensing / damage-sensing" receptor of myeloid biology. Its ligands include phospholipids, sulfatides, ApoE, ApoJ/clusterin, β-amyloid, and bacterial lipopolysaccharide-like molecules. TREM2 signaling promotes phagocytosis, lipid handling, survival, and an immunosuppressive / tissue-repair-leaning state.

## Key variants

- TREM2 (full length, membrane)
- sTREM2 (soluble, shed by ADAM10/17)
- LOF risk variants: R47H, R62H, D87N (Alzheimer's, Nasu-Hakola disease)
- TREM2-high "lipid-associated macrophage" (LAM) / "DAM" / "TREM2 TAM" populations across tissues

## Known limitations

- TREM2 expression is shared across multiple distinct macrophage states (LAM, DAM, TREM2 TAM); cluster identity requires multi-marker context
- Soluble vs membrane TREM2 have distinct biology and are often conflated by bulk readouts
- Anti-TREM2 antibodies in cancer trials are still maturing; agonist vs antagonist mode-of-action is contested

## Open problems

- Molecular ligand specificity in tumor microenvironment
- Cross-talk with IL4I1 / FOLR2 / lipid-handling pathways in TAM populations
- Precise role in MoMac immunosuppression vs tissue repair vs antigen presentation

## Relevance to active research

[[papers/cross-tissue-single-cell-landscape-human]] uses TREM2 as the defining marker of MoMac-VERSE cluster #3 (TREM2_Mac), a tumor-associated macrophage subset that accumulates across all six cancer types studied (lung, colon, liver, breast, stomach, pancreas) and is shown by Ms4a3 fate-mapping in mouse to be predominantly monocyte-derived. The paper situates TREM2 TAM alongside IL4I1 and HES1 macs in a shared landscape of tumor-conditioned myeloid states.

[[papers/using-pan-cancer-atlas-investigate-tumour]] resolves TREM2-positive TAMs into two distinct clusters in the 23-cluster pan-cancer atlas: `3_ICIMac1` (TREM2/SPP1/RNASE1/NUPR1) and `4_ICIMac2` (TREM2/APOE/APOC1, lipid-associated). Both clusters recapitulate a melanoma immunotherapy-resistance signature from prior literature yet — counterintuitively — are themselves *enriched* in ICI responders in CPI1000+ pan-cancer bulk RNAseq, highlighting context-dependence of the TREM2-TAM-ICI axis.
