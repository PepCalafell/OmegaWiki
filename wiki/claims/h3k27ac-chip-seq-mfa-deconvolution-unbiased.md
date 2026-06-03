---
title: "Genome-wide H3K27ac with MFA deconvolution is an unbiased functional readout of kinase-inhibitor effects on macrophages"
slug: h3k27ac-chip-seq-mfa-deconvolution-unbiased
status: supported
confidence: 0.8
tags:
  - methodological
  - H3K27ac
  - kinase-inhibitors
  - macrophages
domain: methods / epigenomics
source_papers:
  - integrative-epigenome-based-strategy-unbiased-functional
evidence:
  - source: integrative-epigenome-based-strategy-unbiased-functional
    type: supports
    strength: strong
    detail: "~600 H3K27ac ChIP-seq datasets across 58 CKIs + DMSO, two stimuli and five timepoints were structured into 59 tables and deconvolved by Multiple Factor Analysis into per-CRE perturbation likelihoods."
conditions: "Primary mouse BMDMs; LPS (TLR4) and IL-4 (IL-4R) stimulation; H3K27ac ChIP-seq."
date_proposed: 2026-06-03
date_updated: 2026-06-03
---

## Statement

Reading signal-induced changes in H3K27ac genome-wide and deconvolving them with Multiple Factor Analysis provides an unbiased, information-rich, interpretable readout of the functional cellular effects of clinical kinase inhibitors on macrophage activation.

## Evidence summary

The authors generated ~600 H3K27ac ChIP-seq samples (58 CKIs + DMSO × LPS/IL-4 × 0/0.5/1/2/4 h), centered CREs on ATAC-seq accessible regions, and applied [[foundations/multiple-factor-analysis]] to recover temporal kinetics and a per-CRE perturbation likelihood. See [[concepts/epigenome-based-functional-profiling-kinase-inhibitors]] and [[foundations/h3k27ac-histone-acetylation-mark]].

## Conditions and scope

Demonstrated in primary mouse bone-marrow-derived macrophages ([[foundations/bone-marrow-derived-macrophage-bmdm]]) under TLR4/LPS and IL-4 stimulation only.

## Counter-evidence

None within the paper; the approach is explicitly not suited to primary high-throughput library screening.

## Linked ideas

## Open questions

- Does the readout generalize to other cell types and slower-kinetic signaling systems?
