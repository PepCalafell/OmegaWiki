---
title: "ERK1/2 inhibition (SCH772984) suppresses PD-L1 upregulation during monocyte-to-macrophage maturation; STAT1, Akt, PI3K, NF-κB, mTOR inhibitors do not"
slug: erk-inhibition-blocks-pd-l1-monocyte-maturation
status: supported
confidence: 0.85
tags:
  - PD-L1
  - ERK
  - MAPK
  - monocyte
  - SCH772984
  - small-molecule-screen
  - mechanism
domain: "immunology / pharmacology"
source_papers:
  - pd-l1-expressing-tumor-associated-macrophages
evidence:
  - source: pd-l1-expressing-tumor-associated-macrophages
    type: supports
    strength: medium
    detail: "Wang 2024 Fig. 5I: small-molecule inhibitor screen during 8h ex vivo resting of BC patient monocytes (n=6). SCH772984 (ERK1/2, 0.5 μM) significantly suppresses PD-L1 upregulation (*p<0.05). Fludarabine (STAT1, 50 μM), MK-2206 (Akt, 0.5 μM), LY294002 (PI3K, 5 μM), QNZ (NF-κB, 5 μM), and rapamycin (mTOR, 0.1 μM) do not significantly reduce PD-L1. ERK dependence is partial — a single inhibitor screen, not a multi-pathway combination experiment."
conditions: "Patient-derived peripheral monocytes; single-pathway inhibitors at indicated concentrations; 8h treatment."
date_proposed: 2026-05-12
date_updated: 2026-05-12
---

## Statement

The ERK1/2 MAPK pathway is partially required for PD-L1 upregulation during monocyte-to-macrophage maturation. SCH772984 reduces but does not abolish PD-L1 induction; STAT1, Akt, PI3K, NF-κB, and mTOR pathways are dispensable as single nodes. This pinpoints ERK as the most prominent identified upstream node in the maturation-driven PD-L1 induction program, while leaving the full network open.

## Evidence summary

- Wang 2024 Fig. 5I (inhibitor screen).

## Conditions and scope

- Single inhibitor doses; off-target effects not addressed (e.g., SCH772984 specificity for ERK1/2).
- Combination inhibition not tested — pathway redundancy may explain incomplete blockade.
- Genetic perturbation (ERK1/2 knockdown) not performed.

## Counter-evidence

- None directly; AP-1 / CEBPD transcriptional activators (downstream of ERK) are upregulated in PD-L1+ TAMs (Fig. 1H), consistent with the pharmacological readout.

## Linked ideas

- Supports the ERK→AP-1→PD-L1 axis hypothesized in [[concepts/monocyte-macrophage-maturation-pd-l1-induction]].

## Open questions

- Identity of the upstream receptor activating ERK (CSF1R / adhesion integrins are candidates).
- Whether ERK inhibition phenocopies the IFN-γ-blockade-resistant pathway specifically, or also affects shared inflammatory routes.
