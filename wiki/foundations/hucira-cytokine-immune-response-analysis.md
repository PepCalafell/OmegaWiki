---
title: "huCIRA — human Cytokine Immune Response Analysis"
slug: hucira-cytokine-immune-response-analysis
domain: "immunology"
status: mainstream
aliases:
  - "huCIRA"
  - "human Cytokine Immune Response Analysis"
first_introduced: "Oesinghaus et al. 2025 (bioRxiv)"
date_updated: 2026-05-28
source_url: "https://doi.org/10.64898/2025.12.12.693897"
---

## Definition

An open-source Python tool that decodes cytokine activity in user-supplied human transcriptomic datasets by enrichment against the gene sets of the Human Cytokine Dictionary. It interfaces gseapy and accepts (1) the Dictionary's per-cytokine differential gene sets and (2) the DRVI-derived cytokine-induced immune program (CIP) gene sets, then computes normalized enrichment scores (NES) for cytokine and program activity across user-specified conditions, plus differential cell–cell communication inference.

## Intuition

huCIRA is to the human Dictionary what [[irea-immune-response-enrichment-analysis-software]] is to the mouse Immune Dictionary: a signature-enrichment engine that asks "which cytokines are active here?" from any transcriptome, rather than inferring signaling from ligand–receptor transcript co-expression. Because it scores against empirically measured human PBMC response signatures, it sidesteps the receptor-expression-insufficiency problem of L–R inference tools.

## Key variants

- Cytokine-activity mode: NES per cytokine per cell type across conditions
- CIP-activity mode: NES per cytokine-induced immune program
- Differential cell–cell communication mode: sender DE × receiver receptor × receiver enrichment

## Known limitations

- Reference signatures derived from in vitro 24 h PBMC stimulation — transfer to tissue/spatial contexts is approximate
- Enrichment, not causal inference — high NES indicates signature match, not proven active signaling
- Human-only signatures (not cross-species)
- Depends on quality/comparability of the user's DE input

## Open problems

- Calibration across platforms (scRNA-seq vs spatial vs bulk)
- Multi-timepoint signature libraries
- Integration with genetic / clinical metadata for biomarker discovery

## Relevance to active research

Applied in the source paper to SLE, multiple sclerosis, and NSCLC spatial transcriptomics. Directly usable for inferring active cytokines in tumor scRNA-seq / spatial data (HypoxiaVERSE: cytokine activity in hypoxic vs normoxic myeloid niches). Complements [[irea-immune-response-enrichment-analysis-software]], [[cellchat-cell-cell-communication]], and [[nichenet-ligand-target-inference]].
