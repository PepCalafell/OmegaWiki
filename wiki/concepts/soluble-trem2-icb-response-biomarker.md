---
title: "Soluble TREM2 (sTREM2) as a serum biomarker for ICB response"
aliases:
  - "sTREM2"
  - "soluble TREM2"
  - "shed TREM2 ectodomain"
tags:
  - sTREM2
  - serum-biomarker
  - immune-checkpoint-blockade
  - predictive-biomarker
  - HCC
  - ELISA
maturity: emerging
key_papers:
  - trem2-macrophages-associated-enhanced-response-pd
first_introduced: "Hamon et al. 2025 (bioRxiv preprint) — first systematic ICB-response application; sTREM2 itself characterised earlier in Alzheimer's, NASH"
date_updated: 2026-05-26
related_concepts:
  - trem2-tumor-associated-macrophage
  - hepatic-trem2-protective-tam-program
---

## Definition

The shed soluble ectodomain of TREM2 (released by ADAM10/17-mediated cleavage of membrane TREM2), measured in serum or plasma by ELISA, used as an accessible predictive biomarker for immune checkpoint blockade response — first systematically validated in HCC PD-1 blockade (Hamon et al. 2025) where baseline sTREM2 is elevated in responders.

## Intuition

If intratumoral TREM2-mac abundance gates ICB response in HCC (the central finding of Hamon 2025), then the serum-shed product of TREM2 from those tumor-resident macs becomes an attractive surrogate — easier to sample longitudinally, cheaper than tissue scRNA-seq.

## Formal notation

- Analyte: soluble ectodomain of TREM2 (~25 kDa)
- Source: ADAM10/17 cleavage of membrane TREM2 on myeloid surface
- Detection: standard sandwich ELISA
- Predictive use (HCC): baseline serum, pre-treatment

## Variants

- Baseline sTREM2 (pre-treatment) — predictive
- On-treatment ΔsTREM2 — not yet characterised
- CSF sTREM2 in Alzheimer's biomarker work — separate clinical use

## Comparison

vs intratumoral TREM2 mac frequency: stronger anatomical specificity but less accessible.
vs PD-L1 IHC: comparable accessibility (IHC is tissue, sTREM2 is blood).
vs IFN-γ signature scores: comparable predictive intent but distinct biology.

## When to use

When considering blood-based predictive biomarkers for ICB in HCC; when stratifying neoadjuvant ICB candidates without access to scRNA-seq.

## Known limitations

- Modest cohort sizes; prospective validation needed.
- Non-tumor sources of sTREM2 (Kupffer cells, microglia, BM monocytes, NASH liver) limit anatomical specificity.
- Assay variability across commercial ELISA kits.

## Open problems

- Does treatment-induced ΔsTREM2 add predictive value beyond baseline?
- Does sTREM2 generalise to HCC patients receiving non-PD-1 ICB regimens?
- How does sTREM2 cross-tissue context (HCC vs NSCLC) interact with the tissue-specific TREM2-mac function?

## Key papers

- [[papers/trem2-macrophages-associated-enhanced-response-pd]] — first demonstration of baseline serum sTREM2 elevation in HCC PD-1 responders across two cohorts
