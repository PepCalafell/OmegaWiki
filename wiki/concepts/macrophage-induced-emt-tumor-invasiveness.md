---
title: "Macrophage-induced EMT and tumor invasiveness"
aliases:
  - "macrophage-induced EMT"
  - "TAM-driven epithelial-mesenchymal transition"
  - "TRM-induced EMT"
  - "macrophage-driven tumor invasiveness"
  - "TAM EMT axis"
  - "macrophage TWIST1 induction"
  - "macrophage ZEB1 induction"
  - "macrophage E-cadherin downregulation"
  - "macrophage-induced tumor cell migration"
  - "TAM-tumor crosstalk EMT"
  - "TGFβ TAM EMT"
tags:
  - macrophage
  - EMT
  - tumor-invasiveness
  - tumor-cell-plasticity
  - TWIST1
  - ZEB1
  - E-cadherin
  - cancer-cell-biology
  - tumor-microenvironment
maturity: active
key_papers:
  - tissue-resident-macrophages-provide-pro-tumorigenic
first_introduced: "Conceptual roots in Pollard et al. (1990s-2000s); direct demonstration with TRM-specific specificity in Casanova-Acebes et al. *Nature* 2021"
date_updated: 2026-05-06
related_concepts:
  - tissue-resident-macrophage-tumor-niche
  - tumor-associated-macrophage-immunosuppression
  - macrophage-ontogeny-resident-vs-monocyte-derived
---

## Definition

The induction of an epithelial-mesenchymal transition (EMT) programme in tumour cells through paracrine or contact-dependent signalling from macrophages. Hallmarks include reduced E-cadherin (CDH1) protein, induction of EMT transcription factors TWIST1 and ZEB1, increased β-catenin activity, and gain of invasive/migratory phenotype with the formation of invasive protrusions in 3D matrix assays. In NSCLC, the EMT-inducing capacity is selective to the **tissue-resident macrophage (TRM)** lineage and is not shared by bone-marrow monocytes or established monocyte-derived MDMs.

## Intuition

EMT is the textbook explanation for tumour cell migration, invasion, and metastasis-initiating plasticity. Many factors trigger EMT — TGFβ, WNT, Notch, hypoxia. The macrophage-induced version specifically asks which TAM populations are EMT-inducers. Finding that only TRMs (not BMMs, not MDMs) are EMT-competent in NSCLC implies that the EMT signal originates from a defined macrophage state, not generic TAM activity, and that the same "macrophage" can have very different effects on tumour cell plasticity depending on its ontogeny and tissue context.

## Formal notation

- Tumour cell readouts: ↓E-cadherin (CDH1) protein at cell membrane; ↑TWIST1 nuclear staining; ↑ZEB1 nuclear staining; ↑invasive protrusions in 3D Matrigel; ↑transwell migration with cell-free conditioned medium
- Macrophage transcriptional outputs paralleling EMT: ↑VEGFA, PLAU/uPA, TGFB1, MMP12, MMP14, ADAMDEC1
- Selective competence: TRM-CM (conditioned medium) suffices; BMM-CM and tMDM-CM do not produce the same effect
- In vivo correlate: TWIST1⁺/ZEB1⁺ KP cells reduced in TRM-depleted mice (CD169-DTR + DT) at day 5

## Variants

- TRM-induced EMT in NSCLC (this paper) — selective to alveolar TRM lineage
- TGFβ-driven TAM-EMT axis — generic mechanism; TGFB1 is among the candidate mediators here
- TWIST1-mediated EMT vs ZEB1-mediated EMT — partially redundant, both induced
- Contact-dependent vs soluble factor — both contribute (CM works; co-culture is stronger)

## Comparison

vs canonical TGFβ-induced EMT: shares TWIST1/ZEB1 induction but anchored in TRM-specific paracrine signalling
vs hypoxia-induced EMT: complementary; hypoxic environments may prime tumour cells for TRM-EMT signal but the TRM signal works in normoxia in vitro
vs cancer-associated fibroblast (CAF) EMT: CAFs and TRMs may both contribute EMT signals; in early NSCLC the TRM contribution is non-redundant
vs MDM-driven cell-cycle programme: in 3D co-culture KP cells with BMMs upregulate cell-cycle/DNA replication genes (Cdk4, Mcm4, Brca1/2) instead of EMT — distinct programme

## When to use

- Interpreting heterogeneity in TAM-tumour cell co-culture experiments
- Designing assays to measure EMT-inducing capacity of macrophage subsets
- Linking ontogeny (TRM vs MDM) to functional output (EMT vs proliferation)
- Selecting therapeutic targets that block the TRM-EMT axis without affecting general TAM biology

## Known limitations

- The specific secreted factor(s) responsible are not yet identified (VEGFA, PLAU, TGFB1 are candidates but not proven)
- Demonstrated in mouse KP NSCLC and 3D spheroid systems; human translation pending
- The relevant tumour cell populations may be heterogeneous in their EMT-competence
- Whether the EMT induced by TRMs leads to true metastasis or only local invasion is not directly tested

## Open problems

- Identification of the necessary and sufficient TRM-secreted EMT inducer(s)
- Whether the TRM-EMT axis generalises to non-lung early epithelial cancers
- Interplay with hypoxic / WNT / Notch EMT signalling
- Therapeutic blockade strategies (anti-TGFβ, anti-uPAR, etc.) and timing requirements

## Key papers

- [[papers/tissue-resident-macrophages-provide-pro-tumorigenic]] — first to establish that TRMs (not MDMs or BMMs) are the EMT-inducing macrophage lineage in early NSCLC, with selective TRM-CM effect, in vivo TWIST1/ZEB1 reduction in TRM-depleted mice, and 3D spheroid invasive-protrusion assay

## My understanding

The strongest aspect of this concept is the **lineage selectivity** — that not every macrophage induces EMT, and the one that does is the resident embryonic-origin lineage. This forces a rethink of "TAMs and EMT": rather than treating TAMs as a uniform pro-tumour mass, the concept demands sub-typing by ontogeny. For thesis work it implies that hypoxic mMAC1 (monocyte-derived) is unlikely to be an EMT inducer (it maps to MDM territory) — but it leaves open whether reprogramming MDMs toward an alveolar-TRM-like state could reproduce EMT competence, and whether the EMT signal is intrinsic to TRM ontogeny or extrinsic (e.g. tissue-imprinted).
