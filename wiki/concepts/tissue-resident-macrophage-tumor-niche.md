---
title: "Tissue-resident macrophage pro-tumorigenic niche"
aliases:
  - "TRM tumor niche"
  - "alveolar macrophage tumor niche"
  - "tissue-resident macrophage cancer niche"
  - "TRM pro-tumorigenic niche"
  - "early tumor TRM niche"
  - "alveolar TRM in NSCLC"
  - "lung tissue-resident macrophage cancer"
  - "PPARG MARCO tumor macrophage"
  - "embryonic-origin TAM"
  - "TRM-driven cancer initiation"
  - "early-stage lung cancer macrophage niche"
  - "self-renewing tumor macrophage"
tags:
  - macrophage
  - tissue-resident
  - tumor-microenvironment
  - lung-cancer
  - NSCLC
  - alveolar-macrophage
  - cancer-niche
  - early-tumor
  - macrophage-ontogeny
maturity: emerging
key_papers:
  - tissue-resident-macrophages-provide-pro-tumorigenic
  - physiology-diseases-tissue-resident-macrophages
  - macrophages-targets-next-generation-cancer-immunotherapy
first_introduced: "Casanova-Acebes et al. *Nature* 2021 (this paper); precursor framings in Lavin 2017, Mantovani 2017; broader TRM-disease context in Lazarov & Geissmann 2023 Nature review"
date_updated: 2026-05-27
related_concepts:
  - macrophage-ontogeny-resident-vs-monocyte-derived
  - macrophage-induced-emt-tumor-invasiveness
  - trm-induced-treg-licensing
  - trem2-tumor-associated-macrophage
  - tumor-associated-macrophage-immunosuppression
---

## Definition

The role of tissue-resident macrophages (TRMs) — embryonically-seeded, locally self-renewing — as a pro-tumorigenic niche during the earliest stages of cancer progression. In NSCLC, alveolar TRMs (PPARG⁺/MARCO⁺/SIGLEC1⁺/STMN1⁺) physically accumulate close to seeded tumour cells, induce an EMT/invasiveness programme in adjacent epithelial tumour cells, and uniquely license regulatory T cell (Treg) suppressive programmes — together creating an immune-evasive niche that supports tumour establishment.

## Intuition

Most TAM biology focuses on monocyte-derived TAMs (TREM2⁺, IL4I1⁺, lipid-associated, immunosuppressive) that dominate established tumours. This concept inverts the focus to the **earliest** stage of cancer, when only a few tumour cells have seeded the tissue and no MDM influx has occurred yet — at this stage, the only macrophage available to interact with the tumour is the resident TRM. The pro-tumorigenic niche concept proposes that TRMs are not passive bystanders but active **founders** of the TME, providing a transient pro-EMT and pro-Treg signal that helps tumour cells establish before being eclipsed by MDM dominance.

## Formal notation

- Population: PPARG⁺/MARCO⁺/SIGLEC1⁺/CD68⁺/MRC1⁺ alveolar TRMs (lung); embryonically seeded; self-renewing locally
- Spatial signature: TRMs in close contact with KP / NSCLC tumour cells until day ~15 of tumour growth, then redistribute to tumour periphery (granuloma-like)
- Tumour-induced TRM transcriptional change: ~1,670 DEGs vs healthy lung TRMs; upregulation of MMP12/MMP14/ADAMDEC1, TSPAN4, MHC-II, CCL17, CXCL9, TGFβ1; downregulation of IL1B and inflammasome regulators
- Functional outputs: EMT induction in tumour cells (TWIST1/ZEB1↑, E-cadherin↓); Treg licensing (CD73/CTLA-4↑ on differentiated Tregs)
- Temporal restriction: niche function is restricted to early lesions (≤ day 12); TRM depletion in established lesions has no effect

## Variants

- Alveolar TRM in NSCLC (this paper) — primary instantiation
- Kupffer cell in early hepatocellular carcinoma — analogous TRM-cancer contact (untested but conceptually parallel)
- LYVE1⁺ tissue-resident MAC (Chakarov 2019) — another TRM lineage that may serve niche roles in vasculature-proximal tumours
- Microglia in early CNS tumours — analogous TRM role in glioma initiation

## Comparison

vs MDM-dominated TAM compartment: MDMs (TREM2⁺/SPP1⁺/APOE⁺) dominate established tumours and are the canonical immunosuppressive TAM target; TRM niche is upstream and earlier
vs M1/M2 polarisation: M1/M2 is a state framework; TRM niche is an ontogeny + temporal stage framework, orthogonal
vs IL4I1 TAM tumour-periphery axis: IL4I1⁺ TAMs are MDM-derived peripheral TAMs in established tumours; TRM niche is intra-tumoural and early-only
vs granuloma topology: late-stage TRM redistribution to tumour periphery resembles M. tuberculosis granuloma topology, suggesting a shared "exclusion" architecture

## When to use

- Designing prevention or early-intervention strategies for NSCLC and other early-stage epithelial cancers
- Interpreting why some cancers progress despite immune surveillance: TRM niche may evade detection at the smallest lesion size
- Distinguishing early vs late TAM biology in single-cell or spatial datasets
- Mapping ontogeny dimensions of macrophage state in tumours where lineage tracing is unavailable

## Known limitations

- Direct evidence is from mouse KP NSCLC and B16-OVA melanoma; human relevance is inferred from cross-species signature similarity
- The niche function is operationally defined by CD169-DTR depletion outcomes; the secreted factor(s) remain unidentified
- "Early" is restricted to days 0-12 in mouse models; the human equivalent in clinical staging is unclear
- TRM niche concept is largely untested in non-lung cancers

## Open problems

- Identification of the secreted factor(s) (VEGFA? PLAU? TGFβ1?) that mediate the EMT-niche signal
- Mechanism of temporal restriction: why does TRM dependence end at day 12-15?
- Generalisability across tumour types — is there a Kupffer-cell-driven HCC niche, microglia-driven glioma niche, etc.?
- How TRM niche functions interface with hypoxia-driven macrophage reprogramming
- Therapeutic targeting strategies that selectively impair the niche function without compromising surfactant clearance and homeostatic TRM functions

## Key papers

- [[papers/tissue-resident-macrophages-provide-pro-tumorigenic]] — establishes the concept in NSCLC: spatial localisation, transcriptional reprogramming, EMT induction, Treg licensing, CD169-DTR depletion phenotype, and temporal restriction to early lesions

## My understanding

This concept is the missing link between "TAMs are bad" (general TAM biology, dominated by MDMs) and "tissue-resident macrophages are mostly homeostatic" (TRM/MDM ontogeny literature). The pro-tumorigenic niche framing reconciles both: TRMs are usually homeostatic, but in the very earliest tumour lesions they are subverted into an EMT-permissive, Treg-licensing state that supports tumour establishment. For thesis work the concept matters as the contextual frame for why MDM-derived hypoxic mMAC1 (monocyte-derived) is functionally different from any TRM-derived state — the two lineages encode distinct niche functions at distinct tumour stages.
