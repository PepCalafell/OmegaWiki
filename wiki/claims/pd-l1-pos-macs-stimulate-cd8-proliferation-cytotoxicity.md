---
title: "PD-L1+/hi macrophages stimulate CD8+ T cell proliferation more than PD-L1−/lo macrophages in autologous co-culture; phagocytosis capacity also higher"
slug: pd-l1-pos-macs-stimulate-cd8-proliferation-cytotoxicity
status: supported
confidence: 0.9
tags:
  - PD-L1
  - macrophage
  - CD8
  - T-cell-proliferation
  - phagocytosis
  - functional
  - breast-cancer
domain: "immunology / functional assay"
source_papers:
  - pd-l1-expressing-tumor-associated-macrophages
evidence:
  - source: pd-l1-expressing-tumor-associated-macrophages
    type: supports
    strength: strong
    detail: "Wang 2024 Fig. 7A-D: PBMCs from BC patients (n=16) rested ex vivo, phagocytosis measured with pHrodo Green E. coli bioparticles. PD-L1+/hi monocytes/macrophages have significantly higher phagocytic uptake than PD-L1−/lo (paired t test). For T-cell stimulation (n=6), flow-sorted PD-L1+ vs PD-L1− monocytes co-cultured with CellTrace-labeled autologous T cells under TCR stimulation for 4 days: PD-L1+/hi macrophages significantly elevate CD8+ T cell proliferation stimulatory index over PD-L1−/lo macrophages. CD4+ T cell proliferation is similar between subsets (Fig. S11G-H). PD-L1 blocking antibody does NOT change the PD-L1+ macrophage stimulatory effect on CD8+ T cells, despite confirmed PD-1 expression on T cells (Fig. S11I) — i.e., the stimulatory function is PD-L1:PD-1-independent."
conditions: "Patient-derived monocytes + autologous T cells; ex vivo flow sorting + co-culture; pHrodo phagocytosis."
date_proposed: 2026-05-12
date_updated: 2026-05-12
---

## Statement

In ex vivo functional assays with breast cancer patient PBMCs, PD-L1+/hi monocytes/macrophages are functionally more activated than their PD-L1−/lo counterparts: they show higher phagocytic uptake of pHrodo-labeled bacteria and stimulate CD8+ T cell proliferation more strongly in autologous TCR-stimulated co-culture. The stimulatory effect is *not* mediated via PD-L1:PD-1 (blocking antibody does not abolish it), suggesting alternative co-stimulatory or chemokine-based mechanisms.

## Evidence summary

- Wang 2024 Fig. 7A-B (phagocytosis), 7C-D (T cell proliferation), Fig. S11G-H (CD4+ T cells), S11I (PD-1 expression on T cells).

## Conditions and scope

- Autologous PBMC system (not tumor-infiltrating); 4-day co-culture.
- Stimulatory index = (CD8/CD4+CD14)/(CD8/CD4) cell number ratio.
- n=6 patients for the T-cell proliferation assay.

## Counter-evidence

- Murine PD-L1-knockout-in-TAM tumor models (refs 5–7) showed enhanced anti-tumor immunity upon TAM PD-L1 loss — apparent contradiction. Wang 2024 argues this reflects PD-L1-protective rather than PD-L1-suppressive function in TAMs.

## Linked ideas

- Together with [[claims/pd-l1-neg-macs-suppress-cd8-bite-killing]] establishes the functional axis of [[concepts/pd-l1-immunostimulatory-tam-phenotype]].
- Mechanism is PD-L1:PD-1-independent — candidates include CD80:CD28 (PD-L1:CD80 cis-heterodimerization preserving CD28 co-stim), AREG-ICAM1, ANXA1, MIF.

## Open questions

- Identity of the dominant PD-L1+ TAM → CD8+ T cell co-stimulatory ligand-receptor pair.
- Whether the same effect holds for tumor-infiltrating (not just peripheral) PD-L1+ TAMs in autologous TIL co-culture.
- Whether the effect is preserved after anti-PD-L1 ICI treatment in vivo.
