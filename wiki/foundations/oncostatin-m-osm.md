---
title: "Oncostatin M (OSM) — IL-6 family cytokine"
slug: oncostatin-m-osm
domain: "molecular-biology / immunology / cytokine"
status: mainstream
aliases:
  - "OSM"
  - "Oncostatin M"
  - "OSMR ligand"
  - "IL-6 family member"
  - "IL-6 superfamily cytokine"
  - "gp130-utilizing cytokine"
  - "macrophage M2 polarization OSM"
  - "OSM type-I OSMR"
  - "OSM type-II LIFR"
first_introduced: "Zarling et al. 1986 PNAS (OSM purified from U-937 melanoma growth-inhibitor)"
date_updated: 2026-05-08
source_url: "https://www.uniprot.org/uniprot/P13725"
---

## Definition

Oncostatin M (OSM) is a member of the IL-6 family of cytokines. It signals through the OSM receptor (OSMR, type II receptor) or LIF receptor (LIFR, type I receptor) in combination with the common gp130 (IL6ST) co-receptor, activating JAK1/JAK2/TYK2-STAT3 / STAT1 / STAT5 cascades and, downstream, mTORC2-AKT, MAPK (p38, ERK), and PI3K signaling. OSM is produced by activated macrophages, T cells, and tumor cells and has pleiotropic effects on hematopoiesis, inflammation, tissue remodeling, and oncology. In the hypoxic TME, OSM is part of the tumor-cell secretome that drives M2 macrophage polarization via the mTORC2-AKT1 axis (rather than PKCα), and is implicated in tumor proliferation, metastasis, and angiogenesis.

## Intuition

OSM was discovered as a melanoma growth inhibitor in 1986, but the modern view is more nuanced: it inhibits some cancer cell lines (the original M-stat reading) but promotes many others, and it has powerful effects on macrophages — driving M2 polarization in the TAM context. The mTORC2-AKT1-via-OSM mechanism (not PKCα) is the recent mechanistic refinement that distinguishes OSM-driven from IL-4-driven M2 polarization (the latter uses PKCα). In the hypoxic TME, OSM is one of the dominant cytokines tumors use to instruct TAM polarization.

## Formal notation

Receptor system:
- **Type I OSMR**: gp130 + OSMR (OSM-only).
- **Type II OSMR**: gp130 + LIFR (OSM and LIF).
- Human OSM binds both types; mouse OSM binds only type II.

Signaling:
- JAK1/JAK2/TYK2 phosphorylation on receptor → STAT3 (dominant), STAT1, STAT5.
- mTORC2-AKT1 (relevant for M2 polarization in TAM, Bai 2022).
- MAPK (p38, ERK) and PI3K branches.

OSM in TAM polarization (Bai 2022):
- Hypoxic cancer cell secretome contains OSM.
- OSM → mTORC2 activation in macrophages → AKT1 phosphorylation (specifically; not PKCα).
- Outputs: CD206, CD163 (M2 surface markers), Arg-1, COX-2 (M2 functional markers).
- IL-4 is the classical mTORC2-driven M2 inducer; OSM uses the same pathway but starts from a different receptor.

OSM in fibrosis / tissue remodeling:
- OSM is a potent inducer of fibroblast activation and ECM remodeling.
- Implicated in lung, liver, kidney fibrosis.

## Key variants

- *Type I (OSMR)* vs *Type II (LIFR)* receptor signaling — different downstream balance.
- *Mouse vs human OSM*: human OSM is more promiscuous; mouse OSM signals only through LIFR.
- *Soluble vs membrane-bound forms*: OSM is mostly soluble.

## Known limitations

- OSM has both pro- and anti-tumor effects depending on cancer type — context-dependent.
- Therapeutic OSM-axis blockade has been hard to develop selectively.
- Mouse-human signaling differences complicate preclinical-clinical translation.

## Open problems

- Selective OSMR antagonism vs OSM-LIFR signaling — therapeutic differentiation.
- The role of OSM in driving M2 TAM polarization in vivo (vs in vitro evidence) is incompletely characterized.
- Whether OSM-driven M2 differs functionally from IL-4-driven M2 (despite both using mTORC2).

## Relevance to active research

OSM is a key cytokine in hypoxic tumor-TAM crosstalk. In [[papers/hypoxia-driven-crosstalk-between-tumor-tumor]] (Bai 2022), OSM is highlighted as the IL-6-family secretome component that drives M2 polarization via mTORC2-AKT1 (not PKCα), contrasting with the canonical IL-4 pathway. For my hypoxia-NF-κB-macrophage thesis, OSM is a candidate cytokine to test as a co-stimulus in hypoxic TAM-like in vitro models.
