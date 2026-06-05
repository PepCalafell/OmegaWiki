---
title: "IREA enables inference of cytokine activities and immune cell polarization from any transcriptomic data"
slug: irea-enables-inference-cytokine-activities-cell
status: supported
confidence: 0.9
tags: [IREA,cytokine-inference,polarization-inference,scRNA-seq,methodology]
domain: immunology
source_papers:
  - dictionary-immune-responses-cytokines-single-cell
  - immune-dictionary-immune-response-enrichment-analysis
evidence:
  - source: dictionary-immune-responses-cytokines-single-cell
    type: supports
    strength: strong
    detail: "Quote (p.383): 'IREA implements statistical tests to assess the enrichment of either cell polarization or cytokine signatures in transcriptomes, which can then be used to derive cell–cell communication networks'."
  - source: immune-dictionary-immune-response-enrichment-analysis
    type: supports
    strength: moderate
    detail: "AAI 2025 web-portal abstract reaffirms the gap and IREA's role: 'software tools for inferring cytokine activities based on RNA-seq data have been limited. To address this gap, we created a web application ... Immune Response Enrichment Analysis (IREA), that allows assessment of cytokine activities and immune cell polarization from gene expression data' (p.1008)."
conditions: "Applicable to any immune-relevant transcriptomic dataset (bulk or single-cell)."
date_proposed: 2026-05-13
date_updated: 2026-06-04
---

## Statement

Immune Response Enrichment Analysis (IREA) is a statistical-test-based method that, given gene sets or transcriptome matrices, infers enrichment of cytokine response signatures and polarization states defined in the Immune Dictionary, enabling cell–cell communication network reconstruction.

## Evidence summary

Reported in [[papers/dictionary-immune-responses-cytokines-single-cell]] (Cui, Hacohen et al., *Nature* 2024) and reaffirmed by the web-portal companion [[papers/immune-dictionary-immune-response-enrichment-analysis]] (Lai, …, Cui; AAI 2025 abstract).

## Conditions and scope

Applicable to any immune-relevant transcriptomic dataset (bulk or single-cell).

## Counter-evidence

None within the paper's scope.

## Linked ideas

## Open questions
