---
title: "Hypoxia upregulates PD-L1 on TAMs through HIF-1α, exosome cargo, lactate, and IL-6/STAT3 inputs"
slug: hypoxia-tam-pd-l1-immune-evasion
status: supported
confidence: 0.75
tags:
  - PD-L1
  - hypoxia
  - TAM
  - immune-evasion
  - HIF-1α
  - exosome
  - lactate
  - IL-6
  - STAT3
  - immune-checkpoint
  - intermittent-hypoxia
  - obstructive-sleep-apnea
domain: "oncology / immunology / hypoxia"
source_papers:
  - hypoxia-driven-crosstalk-between-tumor-tumor
evidence:
  - source: hypoxia-driven-crosstalk-between-tumor-tumor
    type: supports
    strength: strong
    detail: "Bai 2022 review (DOI 10.1186/s12943-022-01645-2) synthesizes four convergent inputs to TAM PD-L1 under hypoxia: (1) HIF-1α-driven CD274 transcription (p.12, citing CD47/PD-L1 HIF activation across cancer types); (2) exosome cargo from intermittently hypoxic NSCLC cells upregulates macrophage PD-L1 (p.10, providing rationale for OSA-cancer comorbidity, citing Almendros 2019 mechanism); (3) hypoxic-niche lactate elevates TAM PD-L1 protein (p.13, multiple references); (4) Galectin-3 → STAT3 phosphorylation → PD-L1 (p.11, citing Capalbo 2019). HGSOC TAMs commonly express PD-L1 at primary and metastatic sites (p.10)."
conditions: "Multiple convergent inputs at the same TAM in the hypoxic-niche TME. Quantitative partitioning across the four routes is not done in any single study. HGSOC has clear TAM-dominant PD-L1 expression; in lung adenocarcinoma tumor-cell PD-L1 dominates. The intermittent-hypoxia (OSA) → exosome → TAM PD-L1 axis is mechanistically distinct from chronic-hypoxia → HIF-1α → TAM PD-L1."
date_proposed: 2026-05-08
date_updated: 2026-05-08
---

## Statement

Tumor-associated macrophages (TAMs) in the hypoxic niche of solid tumors upregulate the immune-checkpoint ligand PD-L1 (CD274), enabling them to suppress CD8+ T-cell cytotoxicity through PD-1 engagement. The hypoxic upregulation has multiple, partially additive routes: (1) direct HIF-1α-driven transcription of CD274 in macrophages; (2) hypoxic-tumor-cell exosome cargo (especially under intermittent / cyclic hypoxia, e.g. OSA) inducing PD-L1 in recipient macrophages; (3) lactic acid in the hypoxic-niche TME elevating PD-L1 protein on TAMs; (4) IL-6 / STAT3-mediated PD-L1 induction (downstream of Galectin-3 and other hypoxic mediators). PD-L1+ TAMs are particularly enriched in high-grade serous ovarian cancer (HGSOC) at both primary and metastatic sites, suggesting that anti-PD-(L)1 therapy in HGSOC may have a TAM-targeting component.

## Evidence summary

- [[papers/hypoxia-driven-crosstalk-between-tumor-tumor]] — Bai 2022 *Molecular Cancer* review (p.10, p.11, p.12, p.13) synthesizes the four convergent inputs.
- Underlying primary studies (cited in Bai 2022): Noman 2014 *J Exp Med* (HIF-1α-PD-L1 in MDSCs); Hartley 2018 (HGSOC TAM PD-L1); Almendros et al. 2019 (intermittent-hypoxia exosome PD-L1); multiple lactate-PD-L1 studies; Capalbo 2019 (Galectin-3-STAT3-PD-L1).

## Conditions and scope

- Multiple convergent inputs at the same TAM in the hypoxic-niche TME.
- HGSOC has clear TAM-dominant PD-L1 expression; in lung adenocarcinoma tumor-cell PD-L1 dominates — cancer-type-specific weighting differs.
- Intermittent / cyclic hypoxia (OSA setting) drives a mechanistically distinct exosome-mediated TAM PD-L1 induction, with implications for sleep-apnea cancer comorbidity.
- Chronic hypoxia drives TAM PD-L1 through HIF-1α direct transcription and through lactate accumulation.

## Counter-evidence

- Quantitative partitioning across the four input routes is not done in any single study; the relative dominance of each is unclear.
- Whether TAM PD-L1 is functionally equivalent to tumor PD-L1 in mediating anti-PD-(L)1 response is debated.
- TAM PD-L1 has historically been overshadowed by tumor-cell PD-L1 in clinical biomarker development; staining protocols vary.
- The OSA-hypoxia-cancer comorbidity story is based on retrospective epidemiology plus mouse mechanistic work; prospective clinical evidence is limited.

## Linked ideas

(none yet)

## Open questions

- A definitive in vivo demonstration that TAM-specific PD-L1 deletion (LysM-Cre × CD274-floxed) phenocopies pan-PD-L1 deletion in hypoxic tumor models.
- Single-cell-resolved mapping of PD-L1+ TAM subsets across cancer types and oxygen levels.
- Therapeutic implications of intermittent vs chronic hypoxia: should OSA cancer patients receive different immunotherapy strategies?
- Mechanism of lactate-driven PD-L1 induction (transcription vs protein stabilization vs trafficking).
- Cross-talk with the intrinsic hypoxic NF-κB / TET2 macrophage program: does that intrinsic program enhance or compete with PD-L1 upregulation?
