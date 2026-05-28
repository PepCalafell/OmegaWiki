---
title: "Cytokine-induced immune programs (CIPs)"
aliases:
  - CIP
  - cytokine-induced immune program
  - cytokine-induced gene program
maturity: emerging
tags:
  - gene-programs
  - cytokines
  - latent-factors
  - functional-modules
key_papers:
  - single-cell-cytokine-dictionary-human-peripheral
first_introduced: "2025"
date_updated: 2026-05-28
related_concepts:
  - cytokine-driven-immune-polarization-states-atlas
  - cytokine-cell-type-specific-response-pleiotropy
---

## Definition

CIPs are data-driven functional modules — groups of genes jointly up- or downregulated upon cytokine stimulation — derived by applying DRVI (Disentangled Representation Variational Inference) to the Human Cytokine Dictionary. Each CIP corresponds to a disentangled latent dimension linked to a largely exclusive gene set. The Dictionary defines 82 CIPs, manually annotated and grouped into 11 broad biological categories; one or several cytokines can modulate a given CIP.

## Intuition

Instead of describing cytokine responses gene-by-gene, CIPs compress them into interpretable building blocks (e.g. ViralResponse, MyeloidRemodel, CytokineProd, Recruitment-2, Cytotoxic-1, NK-Immuno, IgE-Humoral). A cell's response to a cytokine becomes a combination of activated/repressed programs, and the same program can be driven by multiple cytokines — providing a shared vocabulary for comparing responses across cytokines, cell types, and diseases.

## Variants

- Myeloid CIPs (57 — the majority)
- Lymphoid CIPs (12)
- Shared/cross-compartment CIPs (10)

## Comparison

Conceptually parallel to the mouse Immune Dictionary's [[cytokine-driven-immune-polarization-states-atlas]] (66 polarization states), but CIPs are gene-program latent factors (DRVI decomposition) rather than subcluster-defined cell states, and they are explicitly many-to-many with cytokines.

## When to use

As an interpretation layer for human cytokine-perturbed transcriptomes; consumed by huCIRA to score program activity in independent datasets (disease, spatial).

## Known limitations

- Program count and labels depend on model and expert annotation
- Derived from in vitro 24 h PBMC — transfer to tissue contexts is approximate
- Myeloid-heavy, reflecting PBMC biology and the experimental window

## Open problems

- Stability of CIPs across datasets / platforms
- Causal vs correlational interpretation of program activity
- Mapping CIPs onto in vivo tissue and tumor states

## Key papers

- [[papers/single-cell-cytokine-dictionary-human-peripheral]]

## My understanding

CIPs are the human Dictionary's interpretability deliverable and the substrate huCIRA scores. For tumor work, program-level readouts (e.g. MyeloidRemodel, ViralResponse) may transfer better across contexts than individual DE genes.
