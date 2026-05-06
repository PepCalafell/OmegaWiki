---
title: "IL4I1⁺ PD-L1⁺ IDO1⁺ tumor-associated macrophage (IL4I1 TAM)"
aliases:
  - "IL4I1 TAM"
  - "IL4I1 Mac"
  - "IL4I1⁺ macrophage"
  - "IL4I1+PD-L1+IDO1+ TAM"
  - "tryptophan-degrading TAM"
  - "AHR-activating TAM"
  - "MoMac-VERSE cluster #6"
  - "immunosuppressive IL4I1 TAM"
  - "IL4I1 TAM tumor periphery"
  - "tumor-periphery macrophage IL4I1"
  - "T-cell-induced IL4I1 macrophage"
  - "IL4I1 IFNγ-primed TAM"
tags:
  - macrophage
  - tumor-microenvironment
  - IL4I1
  - immunosuppression
  - tryptophan-metabolism
  - AHR
  - PD-L1
  - single-cell
maturity: active
key_papers:
  - cross-tissue-single-cell-landscape-human
  - nf-kb-tet2-promote-macrophage-reprogramming
first_introduced: "Mulder et al. 2021 *Immunity* (MoMac-VERSE cluster #6)"
date_updated: 2026-05-06
related_concepts:
  - momac-verse-mnp-verse-atlas
  - tumor-associated-macrophage-immunosuppression
  - mmac1-hypoxic-inflammatory-macrophage
  - trem2-tumor-associated-macrophage
---

## Definition

A tumor-associated macrophage state (MoMac-VERSE cluster #6) defined by co-expression of IL4I1, PD-L1 (CD274), PD-L2 (PDCD1LG2), IDO1, CD40, CD80, CD86, MHC-II, CCR7, and the chemokines CXCL9, CXCL10, CXCL11. IL4I1_Mac accumulates in the tumour periphery (vs core) of multiple human cancers in a T-cell–dependent manner, driven by IFNγ from CD8⁺ T cells and CD40L from CD4⁺ T cells, and acts as an immunosuppressive node through tryptophan catabolism (AHR pathway), PD-L1/PD-L2 surface display, and CXCR3-ligand-mediated Treg recruitment.

## Intuition

IL4I1_Mac is the macrophage-side counterpart of mregDC: a T-cell-induced, IFNγ-primed, PD-L1/IDO1-displaying, tryptophan-degrading subset that suppresses the very T cells that brought it into being. It is one of the two principal pan-cancer immunosuppressive TAM populations in MoMac-VERSE (the other being TREM2_Mac), and unlike TREM2_Mac it is concentrated in the tumour-T-cell interface zone (periphery), suggesting it is a feedback brake on infiltrating T cells.

## Formal notation

- MoMac-VERSE cluster #6
- Membrane / surface markers: PD-L1 (CD274), PD-L2 (PDCD1LG2), MHC-II (HLA-DR/DP/DQ), CD80, CD86, CD40, CCR7, CD9
- Soluble outputs: CXCL9, CXCL10, CXCL11 (CXCR3 ligands → Treg recruitment); kynurenine / indole-pyruvate (AHR ligands)
- Enzymatic activity: IL4I1 (L-amino-acid oxidase, AHR ligand producer), IDO1 (tryptophan dioxygenase)
- Origin (Ms4a3 fate-mapping in mouse, Mulder et al. 2021): predominantly monocyte-derived
- Putative precursor: ISG_Mo (cluster #4), an IFNγ-primed monocyte that shares many DEtGs and DERs with IL4I1_Mac
- Top SCENIC TFs: STAT1, STAT2, ETV7, IRF1, IRF7
- Top NicheNet upstream ligands: IFNG (from CD8⁺ T cells), CD40LG (from CD4⁺ T cells)

## Variants

- ISG_Mo (cluster #4) — putative monocyte precursor; IFN-primed, weaker IL4I1 program
- IL4I1_Mac in mouse liver — Ms4a3-dTomato⁺ (monocyte-derived), Spp1⁻, distinct from murine Trem2 Macs
- IL4I1⁺ TAM in severe COVID-19 BAL — same IFN/IL4I1 programme appears in viral inflammation, not tumour-specific
- mMAC1 (in vitro hypoxic LPS-activated MAC) — proposed in vitro correlate of IL4I1_Mac with NF-κB-driven C2 demethylation overlay

## Comparison

vs TREM2_Mac (cluster #3): both monocyte-derived and immunosuppressive, but IL4I1 is IFNγ-primed, T-cell-interaction-located in periphery, and uses tryptophan/PD-L1; TREM2 is lipid-driven, more dispersed, and uses MERTK/efferocytosis.
vs mregDC (Maier et al. 2020): IL4I1_Mac shares the regulatory-DC-like programme (CCR7, CD40, IDO1) and may belong to the same T-cell-induced immunoregulatory family on the macrophage side.
vs ISG_Mo (cluster #4): putative precursor, weaker IL4I1/IDO1 programme, more upstream in the differentiation trajectory.
vs mMAC1 (in vitro): the in vivo correlate proposed by Calafell et al. 2024 — shares NF-κB-driven and IFN-driven programmes; IL4I1 and mMAC1 are not identical but transcriptomically and epigenetically overlap.

## When to use

- Annotating immunosuppressive TAM populations in tumour-periphery scRNA-seq data
- Building bulk RNA-seq signatures for prognostic / response-prediction analyses
- Designing T-cell→TAM cell-cell communication studies in IFNγ-rich tumours
- Mapping in-vitro stimulated MAC populations onto a clinically relevant in-vivo state

## Known limitations

- Functional immunosuppression demonstrated by gene programme + flow cytometry, not direct T-cell suppression in matched human tumour tissue
- IL4I1 vs IDO1 individual contributions to the AHR ligand pool are not dissected
- Spatial periphery-vs-core characterisation available only for liver and colon cancers
- IL4I1_Mac signature overlap with mregDC may complicate annotation in DC-rich datasets

## Open problems

- Whether targeting IL4I1 (pharmacological inhibitor available) suffices to reverse the immunosuppressive phenotype in vivo
- Compensatory induction of IL4I1 after PD-1/PD-L1 blockade
- Tumour-type-specific dependencies on IL4I1 vs IDO1 vs both
- Whether the ISG_Mo → IL4I1_Mac trajectory is reversible or terminally differentiated

## Key papers

- [[papers/cross-tissue-single-cell-landscape-human]] — original MoMac-VERSE definition, T-cell-dependent accumulation in tumour periphery, NicheNet IFNG + CD40L upstream regulators, AHR-tryptophan immunosuppressive function (with Sadik et al. 2020 cited for IL4I1 → AHR)
- [[papers/nf-kb-tet2-promote-macrophage-reprogramming]] — proposed mMAC1 as the in vitro correlate of IL4I1_Mac, with shared NF-κB-driven regulatory layer and C2 DNA demethylation signature

## My understanding

IL4I1_Mac is the most therapeutically interesting MoMac-VERSE cluster for tumour immunology because it is (a) clearly immunosuppressive, (b) T-cell-induced (so it scales with immune infiltration), (c) druggable through AHR / IL4I1 / PD-L1 axes, and (d) the putative in vivo correlate of the hypoxic mMAC1 phenotype that the Calafell 2024 paper anchors. For HypoxiaVERSE it is the central anchor population for projecting in vitro hypoxic signatures.
