---
title: "Single-shot DIA-MS in TPCPA quantifies 5,000–6,000 proteins per sample with ~4-orders-of-magnitude dynamic range"
slug: tpcpa-5000-6000-proteins-per-sample
status: supported
confidence: 0.9
tags: [dia-ms, proteome-depth, dynamic-range, throughput]
domain: methods
source_papers:
  - pan-cancer-proteome-atlas-mass-spectrometry
evidence:
  - source: pan-cancer-proteome-atlas-mass-spectrometry
    type: supports
    strength: strong
    detail: "Per-sample identification rate clusters around 5,000–6,000 proteins, spanning roughly four orders of magnitude in abundance; seven 'missing proteins' per HUPO HPP Portal definitions are detected, including USP17L10 with four peptides."
conditions: "Single-shot LC-MS, no sample multiplexing; bulk-tissue inputs of various preparation methods."
date_proposed: 2026-05-25
date_updated: 2026-05-25
---

## Statement
TPCPA single-shot DIA-MS achieves ~5,000–6,000 identified proteins per sample at ~4-orders-of-magnitude dynamic range, including the detection of HUPO HPP "missing proteins". This depth is sufficient for unsupervised cancer-type clustering and downstream signature-based analyses without TMT multiplexing.

## Evidence summary
- Knol et al. 2025 Figure 1B and surrounding text.

## Conditions and scope
- Single-shot DIA-MS workflow; FF and FFPE inputs across labs.

## Counter-evidence
- Depth is below modern multi-day TMT or fractionated workflows, which routinely exceed 10,000 proteins/sample.

## Linked ideas

## Open questions
- Would per-sample depth improve materially with longer gradients or DIA-PASEF on this cohort?
