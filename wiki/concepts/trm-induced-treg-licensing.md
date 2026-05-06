---
title: "TRM-induced Treg licensing (CD73/CTLA-4)"
aliases:
  - "TRM Treg licensing"
  - "macrophage Treg axis"
  - "TRM-induced regulatory T cell suppression"
  - "tissue-resident macrophage Treg expansion"
  - "CCL17 TGFβ macrophage Treg"
  - "macrophage CD73 CTLA-4 Treg"
  - "TRM Treg differentiation"
  - "macrophage-Treg crosstalk"
  - "lung-resident macrophage Treg axis"
  - "alveolar macrophage Treg licensing"
  - "tumor TRM-Treg niche"
tags:
  - macrophage
  - regulatory-T-cell
  - immunosuppression
  - CD73
  - CTLA-4
  - tumor-microenvironment
  - tissue-resident-macrophage
  - lung-cancer
  - immune-evasion
maturity: emerging
key_papers:
  - tissue-resident-macrophages-provide-pro-tumorigenic
first_introduced: "Soroosh et al. *J Exp Med* 2013 (lung TRM-Treg axis); mechanistically extended to cancer in Casanova-Acebes et al. *Nature* 2021"
date_updated: 2026-05-06
related_concepts:
  - tissue-resident-macrophage-tumor-niche
  - tumor-associated-macrophage-immunosuppression
  - macrophage-ontogeny-resident-vs-monocyte-derived
---

## Definition

The selective ability of tissue-resident macrophages (TRMs) — and not bone-marrow monocyte-derived macrophages (MDMs) — to enhance the suppressive programme of differentiating regulatory T cells (Tregs), specifically by upregulating the ectoenzyme CD73 (NT5E) and the co-inhibitory receptor CTLA-4. While both TRMs and MDMs can drive naive CD4⁺ T cells into FOXP3⁺ Tregs, only TRMs equip those Tregs with a heightened suppressive toolkit. In NSCLC, TRMs additionally produce CCL17 and TGFβ1 that recruit and sustain Tregs in proximity within the tumour parenchyma.

## Intuition

Treg differentiation has historically been described as TGFβ-driven and lineage-agnostic among professional APCs/macrophages. The licensing concept refines this: who *makes* a Treg matters less than who *equips* it. TRMs add a "premium-suppression" upgrade to the standard Treg, while MDMs deliver only the basic version. Because CD73 generates immunosuppressive adenosine and CTLA-4 directly counter-stimulates effector T cells, the Tregs licensed by TRMs are functionally more potent — and the impact on the surrounding effector T cell compartment (CD8⁺) is correspondingly larger.

## Formal notation

- Inputs: naive CD4⁺ T cells + TGFβ-permissive conditions + macrophages (TRM vs MDM)
- TRM-derived signals (candidates): CCL17 (chemokine for Treg recruitment), TGFβ1 (Treg differentiation), unidentified factor(s) for CD73/CTLA-4 induction
- Treg outputs: FOXP3⁺ stable, Ki67⁺ proliferative, CD25⁺ IL-2-responsive — both TRM and MDM compartments produce; only TRMs upregulate CD73 and CTLA-4
- Spatial correlate: FOXP3⁺ Tregs cluster within ~30 μm of MRC1⁺ TRMs in tumour lesions
- Functional consequence: TRM depletion reduces tumour Treg numbers, reduces CD73 / CTLA-4 expression on remaining Tregs, increases CD3⁺ infiltration, IFNγ⁺TNF⁺CD8⁺ cells, and CD8⁺/Treg ratio

## Variants

- Lung TRM-Treg axis at homeostasis (Soroosh 2013) — establishes airway tolerance
- Cancer-context TRM-Treg licensing (Casanova-Acebes 2021) — pathologically subverted at the early tumour niche
- MDM-driven Treg differentiation without licensing — partial / "standard" Treg
- CCL17 / CCL22 chemokine-driven Treg recruitment in established tumours (Mizukami 2008) — distinct kinetic from TRM contact-licensing

## Comparison

vs IL4I1⁺ TAM tryptophan/AHR axis: IL4I1 TAMs immunosuppress via T-cell tryptophan starvation and AHR activation; TRM-Treg licensing operates via Treg CD73/CTLA-4 upregulation — distinct mechanisms
vs TREM2⁺ TAM lipid-driven immunosuppression: TREM2 TAMs (MDM-derived) deliver lipid-handling immunosuppression in established tumours; TRM-Treg licensing is upstream and earlier
vs PD-L1-mediated T cell exhaustion: PD-L1 affects effector T cells directly; TRM-Treg licensing acts indirectly via Treg quality
vs general TGFβ-induced Treg differentiation: shares TGFβ1 dependency but differs in ontogeny-restricted CD73/CTLA-4 enhancement

## When to use

- Interpreting Treg phenotypic heterogeneity in tumour datasets (CD73⁺/CTLA-4ʰⁱ Tregs may indicate TRM-driven licensing)
- Designing TRM-targeted immunotherapy strategies that aim to relieve Treg suppressive tone
- Mapping spatial transcriptomic data: co-localisation of MRC1⁺/PPARG⁺ macrophages with FOXP3⁺ Tregs implies TRM-Treg axis activity
- Distinguishing early-niche Treg accumulation (TRM-driven) from established-tumour Treg recruitment (MDM/chemokine-driven)

## Known limitations

- Mechanism is operationally defined; the molecular basis for selective CD73/CTLA-4 licensing by TRMs is unknown
- Direct molecular evidence is mouse-centric; human licensing inferred from cross-species signature
- TRM-Treg co-localisation is correlative; causality is supported by depletion experiments but specific contact-dependent vs soluble factor balance remains unresolved
- CD73 and CTLA-4 are both targets of clinical immunotherapy; whether TRM-driven licensing alters response to anti-CTLA-4 is not directly tested

## Open problems

- Molecular basis of CD73/CTLA-4 induction by TRMs (vs MDMs)
- Whether TRM licensing renders Tregs resistant to anti-CTLA-4 (ipilimumab) clinical efficacy
- Generalisability beyond NSCLC and B16-OVA melanoma
- Single-cell phenotyping of TRM-licensed vs MDM-induced Tregs in human tumours
- Therapeutic exploitation: blocking TRM-Treg licensing without depleting TRMs

## Key papers

- [[papers/tissue-resident-macrophages-provide-pro-tumorigenic]] — first explicit demonstration of TRM-selective Treg licensing (CD73/CTLA-4 enhancement) in cancer; CD169-DTR depletion phenotype confirms TRM dependence; spatial co-localisation of FOXP3⁺ Tregs with MRC1⁺ TRMs in tumour lesions

## My understanding

The TRM-Treg licensing concept is one of the cleanest examples of macrophage ontogeny mapping to functional output. The fact that CD73 and CTLA-4 — both clinically targeted — are differentially imprinted by TRM contact suggests an underexplored mechanism for ipilimumab response heterogeneity in early-stage NSCLC. For thesis work it positions TRM-Treg axis as a parallel immunosuppressive axis distinct from the IL4I1 / TREM2 MDM axis, and provides a baseline against which any reprogramming-induced state (such as hypoxic mMAC1) should be benchmarked.
