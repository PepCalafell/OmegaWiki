---
title: "Allelic loss of PTEN co-occurs with elevated hypoxia in localized prostate cancer and synergistically predicts relapse"
slug: pten-loss-co-occurs-with-hypoxia-localized-pca
status: supported
confidence: 0.9
tags:
  - PTEN
  - hypoxia
  - prostate-cancer
  - relapse
  - prognostic
  - synergy
  - nimbosus
domain: "oncology / cancer-genomics / prostate-cancer"
source_papers:
  - molecular-landmarks-tumor-hypoxia-across-cancer
evidence:
  - source: molecular-landmarks-tumor-hypoxia-across-cancer
    type: supports
    strength: strong
    detail: "Three-cohort PTEN-hypoxia association in localized PCa: CPC-GENE primary discovery (FDR=2.69×10⁻⁴, OR_loss/neutral=3.50, 95% CI 2.14–5.79, Fisher's exact); TCGA replication (Mann-Whitney P=1.26×10⁻⁵); third cohort of n=130 (Spearman ρ=−0.41 between PTEN mRNA and hypoxia, P=9.65×10⁻⁷). Synergy on outcome: hypoxia + PTEN loss vs all others — 2-year biochemical relapse hazard ratio 4.4 (95% CI 1.7–11.0, P=1.95×10⁻³, Wald test) even after controlling for T category, Gleason score, pretreatment PSA. Quote (p.314): 'Subjects whose prostate tumors had both loss of PTEN and high hypoxia were significantly higher risk of biochemical relapse within 2 years.'"
conditions: "Localized prostate cancer; assessed at radical prostatectomy with matched WGS + hypoxia measurement (extrinsic Eppendorf and/or mRNA Buffa)."
date_proposed: 2026-05-06
date_updated: 2026-05-06
---

## Statement

In localized prostate cancer, allelic loss of PTEN is statistically associated with elevated tumor hypoxia (CPC-GENE FDR=2.69×10⁻⁴, OR=3.50; replicated in TCGA P=1.26×10⁻⁵ and a third cohort of n=130 with Spearman ρ=−0.41, P=9.65×10⁻⁷ between PTEN mRNA and hypoxia). The combination of high hypoxia + PTEN loss is *synergistically* prognostic for 2-year biochemical relapse-free survival (HR=4.4, 95% CI 1.7–11.0, P=1.95×10⁻³), even after controlling for clinical T category, Gleason score, and pretreatment PSA. PTEN loss is a defining pillar of the proposed "nimbosus" aggressive phenotype.

## Evidence summary

- [[papers/molecular-landmarks-tumor-hypoxia-across-cancer]] — three-cohort discovery + functional validation: CPC-GENE → TCGA → 130-tumor third cohort.
- HR=4.4 for biochemical relapse, multivariable-adjusted.
- PTEN loss is one of six pillars of the nimbosus phenotype (with hypoxia, mutant TP53, chromothripsis, telomere shortening, IDC-CA).

## Conditions and scope

- Localized PCa, radical prostatectomy specimens, matched WGS + hypoxia.
- Not yet validated in metastatic / castration-resistant PCa.
- Allelic loss of PTEN (heterozygous deletion) is the assayed state; full deletion or point mutation may behave differently.

## Counter-evidence

- Direct causality (does hypoxia *cause* PTEN loss, or vice versa, or is a third factor responsible?) is not established.
- Mechanistic prior: Zundel 2000 (PTEN loss facilitates HIF1A-mediated gene expression) suggests bidirectional links.

## Linked ideas

(none yet)

## Open questions

- Does hypoxia drive PTEN loss (selection) or does PTEN loss potentiate hypoxia (HIF1α stabilization)?
- Is the synergy on outcome additive at the molecular level (e.g., HIF1α-AKT crosstalk) or due to independent contributions to nimbosus features?
- Whether anti-hypoxia therapy is differentially effective in PTEN-loss tumors
