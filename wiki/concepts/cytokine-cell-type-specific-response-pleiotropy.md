---
title: "Cytokine pleiotropy: most cytokines induce highly cell-type-specific responses"
aliases:
  - cytokine pleiotropy
  - cell-type-specific cytokine response
  - cytokine response heterogeneity
  - cytokine pleiotropic effects
  - cytokine cell-type-specific gene programmes
  - cytokine signature heterogeneity across cell types
  - coordinated multicellular cytokine response
  - non-redundant cytokine action
  - cytokine cell-type specificity
  - per cell-type cytokine signature
tags:
  - cytokines
  - immunology
  - single-cell
  - gene-programmes
maturity: stable
key_papers:
  - dictionary-immune-responses-cytokines-single-cell
  - single-cell-cytokine-dictionary-human-peripheral
  - immune-dictionary-immune-response-enrichment-analysis
first_introduced: "2024"
date_updated: 2026-06-04
related_concepts:
  - cytokine-driven-immune-polarization-states-atlas
  - cytokine-mediated-immune-cell-cell-interactome
---

## Definition

Across the Immune Dictionary (86 cytokines × 17+ immune cell types), the majority of cytokine-induced DEGs are specific to one cell type rather than shared across cell types. Even single cytokines such as IL-1β induce distinct gene programmes in almost every cell type, producing a coordinated multicellular response rather than uniform pathway activation.

## Intuition

Cytokine pleiotropy is not noise — it is the rule. The same cytokine triggers neutrophils to chemokine-amplify (Cd14), MigDCs to migrate (Ccr7), and Tregs to suppress (Hif1a/Ctla4). Drug development targeting "the cytokine" must account for cell-type-divergent effects.

## Variants

- Universal/autonomous response (type I IFNs → ISG-I across all cell types)
- Coordinated multicellular response (IL-1 family → distinct programmes per cell type)
- Lineage-selective response (IL-21 → lymphoid; IL-3 → myeloid)
- Single-cell-type response (IL-3 → pDCs; GM-CSF → MigDCs; IL-10 → cDC1)

## When to use

Cite whenever interpreting cytokine signatures in scRNA-seq data — never assume cytokine effects from receptor expression alone, always require cell-type-specific response signature enrichment (e.g., via IREA).

## Open problems

- Combinatorial cytokine perturbation atlases (>2 cytokines simultaneously)
- Dose-response and temporal dynamics of cell-type-specific programmes
- Human translation of the mouse Immune Dictionary — now addressed by the Human Cytokine Dictionary (Oesinghaus 2025), which confirms cell-type-specific responses in human PBMCs but finds only weak human↔mouse gene-level concordance

## Key papers

- [[papers/dictionary-immune-responses-cytokines-single-cell]]
- [[papers/single-cell-cytokine-dictionary-human-peripheral]] — human PBMC counterpart; confirms cytokine pleiotropy/cell-type specificity in humans (IL-1, common γ-chain, IL-4, IL-10, interferons, IL-32-β as the broadest responders)

## My understanding

This is the central conceptual takeaway of Cui & Hacohen 2024: cytokine pleiotropy is structurally encoded in differential cell-type-specific transcriptional programmes. Has direct implications for cytokine-based therapy interpretation in tumours and inflammatory disease.
