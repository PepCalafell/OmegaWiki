---
title: "IREA — Immune Response Enrichment Analysis"
slug: irea-immune-response-enrichment-analysis-software
domain: immunology / bioinformatics
status: mainstream
aliases:
  - IREA
  - Immune Response Enrichment Analysis
  - cytokine response enrichment
  - cytokine activity inference
  - IREA software
  - Cui & Hacohen IREA
  - polarization state inference IREA
  - cytokine signature enrichment scRNA-seq
first_introduced: "2024"
date_updated: 2026-05-13
source_url: "https://github.com/cui-lab/IREA"
---

## Definition

IREA (Immune Response Enrichment Analysis) is the companion software for the Immune Dictionary. Given gene sets or transcriptome matrices from any immune response, IREA infers (i) active cytokine signatures, (ii) immune cell polarization states, and (iii) cell–cell communication networks, by enrichment testing against the Immune Dictionary reference panel of 86 cytokine × 17 cell-type signatures and 66 polarization states.

## Intuition

Receptor expression alone is a poor predictor of cytokine response because ligands may not reach the cell or downstream pathways may be non-functional. IREA tests whether the *downstream response signature* (i.e., the cytokine's transcriptomic footprint per cell type) is enriched — a more direct readout of in vivo cytokine action.

## Key variants

- Cytokine response enrichment (per cell type, vs control)
- Polarization-state enrichment (radar-plot output)
- Cytokine network reconstruction (production × response matching)

## Relevance to active research

IREA enables systematic cytokine inference from any scRNA-seq or bulk transcriptomic dataset — including tumour ICB cohorts, COVID-19 cohorts and vaccine response data. Reproduces canonical findings (M1 polarization after anti-PD-1, TGFβ1 negative regulation, IL-12 axis in checkpoint response).
