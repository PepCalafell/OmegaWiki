---
title: "CXCL8 / IL-8 — interleukin-8 chemokine"
slug: cxcl8-il8
domain: "molecular-biology / immunology / chemokine"
status: mainstream
aliases:
  - "CXCL8"
  - "IL-8"
  - "IL8"
  - "interleukin-8"
  - "neutrophil chemotactic factor"
  - "neutrophil-activating peptide-1"
  - "NAP-1"
  - "monocyte-derived neutrophil chemotactic factor"
  - "T-cell chemotactic factor"
  - "GCP-1 granulocyte chemotactic protein-1"
  - "CXCR1 ligand"
  - "CXCR2 ligand"
first_introduced: "Yoshimura et al. 1987 PNAS / Walz et al. 1987 BBRC (purified neutrophil chemotactic factor); Holmes et al. 1991 Science (CXCR1 cloning); Murphy & Tiffany 1991 Science (CXCR2 cloning)"
date_updated: 2026-05-08
source_url: "https://www.uniprot.org/uniprot/P10145"
---

## Definition

CXCL8 (also known as IL-8, interleukin-8) is a small (~8 kDa) ELR+ CXC chemokine that is the principal chemoattractant for neutrophils and a powerful pro-inflammatory mediator in human innate immunity. It binds two receptors: CXCR1 and CXCR2, both Gαi-coupled GPCRs expressed on neutrophils, monocytes, T cells, NK cells, and many cancer cells. In the tumor microenvironment, CXCL8 is produced by tumor cells, by macrophages (especially under hypoxia), and by stromal cells; it drives neutrophil and myeloid-derived suppressor cell (MDSC) recruitment, tumor proliferation/invasion, angiogenesis, and resistance to immunotherapy. Mouse does not have a direct CXCL8 ortholog (functional analogues are KC/CXCL1 and MIP-2/CXCL2), which complicates translation of mouse cancer models.

## Intuition

CXCL8 is the canonical "send neutrophils here" signal in human innate immunity, and it has been hijacked by tumors to recruit immune cells that paradoxically support tumor growth (neutrophils in NETs, MDSCs). It is also a direct mitogen for tumor cells (via CXCR1/2 expression) and an angiogenic factor in some contexts. In the hypoxic-niche TME, hypoxic macrophages secrete CXCL8 abundantly; tumor cells respond via CXCR1/2-JAK-STAT1, driving a positive-feedback loop with TAM M2 polarization (Bai 2022 gastric-cancer mechanism).

## Formal notation

Receptor-ligand:
- CXCL8 → CXCR1 (binds CXCL8 and CXCL6 with high affinity)
- CXCL8 → CXCR2 (binds CXCL8, CXCL1-3, CXCL5-7)

Hypoxic regulation:
- HIF-1α can drive CXCL8 transcription via HRE.
- NF-κB also drives CXCL8.
- Bai 2022 specifically notes: "Hypoxia increases IL-8 secretion significantly in macrophages but only slightly in gastric cancer cells."

Tumor-TAM crosstalk loop (gastric cancer, Bai 2022):
- Hypoxic macrophage-derived CXCL8 → CXCR1/2 on GC cells → JAK/STAT1.
- STAT1 → IL-10 transcription in tumor cells.
- IL-10 → TAM IL-10/NF-κB → M2 polarization.
- M2 TAMs produce more CXCL8 → positive-feedback loop.

Therapeutics:
- **Reparixin**: CXCR1/2 inhibitor; tested in TNBC and metastatic breast cancer.
- **Ladarixin**: CXCR1/2 inhibitor.
- **AZD5069**: CXCR2 antagonist; tested in oncology and respiratory.
- **HuMab-IL8 (BMS-986253)**: anti-CXCL8 monoclonal antibody.

## Key variants

- *CXCL6, CXCL1-3, CXCL5-7*: related ELR+ CXC chemokines that share CXCR1/2 binding to varying extents.
- *Mouse functional analogues*: KC (CXCL1) and MIP-2 (CXCL2) — mouse lacks a direct CXCL8 ortholog, complicating preclinical translation.

## Known limitations

- Mouse-human ortholog gap (mouse has no direct CXCL8; uses CXCL1/CXCL2 functionally) limits translation.
- CXCR1/2 inhibitors have shown variable efficacy across trials.
- CXCL8's pro- vs anti-tumor effects are context-dependent (cancer-type, tumor stage).
- Plasma CXCL8 measurement as a biomarker is unreliable due to circadian variation and assay differences.

## Open problems

- Optimal cancer indication for CXCR1/2 antagonism.
- Combination with checkpoint blockade — does CXCR2 blockade reduce immunosuppressive MDSC recruitment and unmask response?
- Hypoxic vs normoxic CXCL8 sources within a single tumor — selective targeting strategy.

## Relevance to active research

CXCL8/IL-8 is foundational for tumor-TAM crosstalk in hypoxic settings. In [[papers/hypoxia-driven-crosstalk-between-tumor-tumor]] (Bai 2022), CXCL8 is the centerpiece of the gastric-cancer positive-feedback loop linking hypoxic TAM CXCL8 → tumor JAK/STAT1 → IL-10 → TAM NF-κB → more CXCL8 / M2 polarization. For my hypoxia-NF-κB-macrophage thesis, CXCL8 is a candidate readout of hypoxic macrophage activation that I should track in my datasets.
