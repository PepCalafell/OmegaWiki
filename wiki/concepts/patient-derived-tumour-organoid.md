---
title: "Patient-derived tumour organoid (PDO)"
aliases:
  - PDO
  - patient-derived organoid
  - tumour organoid
  - cancer organoid
  - conventional cancer organoid
  - submerged tumour organoid
  - 3D tumour organoid
  - patient-derived cancer organoid
  - tumour-only organoid
  - epithelial tumour organoid
  - tumour epithelium organoid
  - cancer 3D culture
tags: [oncology, organoids, in-vitro-models]
maturity: stable
key_papers:
  - cancer-organoids-modelling-complexity-tumour-immune
first_introduced: ""
date_updated: 2026-05-21
related_concepts: [air-liquid-interface-tumour-organoid, patient-derived-organotypic-tumour-spheroid, tumour-immune-microenvironment]
---

## Definition

A patient-derived tumour organoid (PDO) is a 3D stem-cell-derived in vitro culture grown from dissociated tumour cells (or, in native variants, from minimally processed tumour fragments) and embedded in extracellular matrix (Matrigel, BME2, collagen, hydrogels). PDOs self-organize, retain interpatient genetic and morphological variability, and can be passaged and biobanked.

## Intuition

PDOs sit between 2D cancer cell lines and patient-derived xenografts (PDX): more physiological than cell lines (recapitulating 3D architecture, growth-factor dependencies and patient-specific genetics) but more rapid and economical than PDX. Standard ("conventional") PDOs are epithelial-only and lack stromal and immune components — a critical limitation for modelling immuno-oncology questions.

## Variants

- **Conventional submerged PDO** — single-cell suspensions in Matrigel/BME under medium with WNT3A, R-spondin, EGF, FGF, Noggin, GSK3i (CHIR99021), ROCK1i (Y27632), HDAC inhibitor, TGFβRi (A83-01).
- **Reconstituted immune PDO** — conventional PDO co-cultured with autologous PBMCs, expanded TILs, CAR-T, NK cells or monocyte-derived DCs.
- **Native immune PDO** — [[air-liquid-interface-tumour-organoid]] and [[patient-derived-organotypic-tumour-spheroid]] systems preserving the original immune-stromal architecture.
- **Micro-organosphere (MOS)** — droplet-emulsion microfluidic variant generating thousands of small organospheres from a single-cell tumour suspension.
- **Assembloid** — multi-cell-type fusion organoid (e.g. bladder assembloids with epithelium + CAFs + endothelium + immune + muscle).
- **FNA-derived PDO** — generated from fine-needle aspiration biopsies.

## When to use

- Predicting patient-specific responses to chemotherapy, radiotherapy, targeted agents and (with immune-augmented variants) immunotherapy.
- Functional genomic screens (CRISPR-Cas9, CRISPRa/i, CRISPR-HOT, perturb-seq) on tumour-cell-autonomous processes.
- Biobanking patient-matched tumour-normal pairs for retrospective and prospective studies.

## Known limitations

- Conventional PDOs lack immune and stromal cells, limiting immuno-oncology modelling.
- Variable efficiency of derivation across anatomic sites and disease stages.
- ECM additives (Matrigel) impose non-physiological viscoelasticity.
- Long-term therapy-response prediction accuracy not yet established.

## Open problems

- Generating PDOs from FNA biopsies with sufficient cellular biomass for immune analyses.
- Standardizing organoid-based ICB prediction across tumour types.
- Reproducible incorporation of vasculature and physiologically relevant oxygen gradients.

## Key papers

- [[cancer-organoids-modelling-complexity-tumour-immune]]

## My understanding

The defining axis for PDO-based immuno-oncology work is "reconstituted vs native": reconstituted PDOs are easier to engineer and screen but lose architecture; native PDOs (ALI, PDOTS) preserve immune-TME context at the cost of throughput. The user's hypoxia-immune-evasion projects will most likely benefit from ALI or PDOTS variants combined with hypoxia perturbation.
