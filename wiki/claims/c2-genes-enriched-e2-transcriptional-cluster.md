---
title: "C2-associated genes are specifically enriched in transcriptional cluster E2 with Fisher P = 3.03×10⁻⁴⁴"
slug: c2-genes-enriched-e2-transcriptional-cluster
status: supported
confidence: 0.95
tags:
  - cluster-C2
  - cluster-E2
  - methylation-expression
  - LPS-response
  - GSEA
domain: "epigenetics"
source_papers:
  - nf-kb-tet2-promote-macrophage-reprogramming
evidence:
  - source: nf-kb-tet2-promote-macrophage-reprogramming
    type: supports
    strength: strong
    detail: "Fisher's exact test for overlap between C2-associated genes and E1-E4 transcriptional clusters: only E2 (LPS-up, more in mMAC1) is significantly enriched (P = 3.03×10⁻⁴⁴). GSEA of C2-associated genes on mMAC1 vs mMAC21: NES = 1.8, FDR = 0.001 (Calafell 2024 Fig. 2A,D-E)."
conditions: "EPIC + bulk RNA-seq cross-omic, M-CSF MACs."
date_proposed: 2026-05-11
date_updated: 2026-05-11
---

## Statement

The set of genes associated with cluster C2 CpGs is specifically and highly significantly enriched in transcriptional cluster E2 (genes up-regulated after LPS activation, with a stronger increase in mMAC1) — Fisher's exact test P = 3.03×10⁻⁴⁴. GSEA confirms up-regulation of C2-associated genes in the mMAC1 vs mMAC21 comparison (NES = 1.8, FDR = 0.001).

## Evidence summary

- Direct overlap test between C2 CpG nearest-gene assignments and DEG clusters (Calafell 2024 Fig. 2A, D).
- GSEA on the mMAC1 vs mMAC21 ranking (Fig. 2E).

## Conditions and scope

- Cross-omic methylation-transcription coupling, M-CSF MACs only.

## Counter-evidence

- CpG-to-gene assignment by nearest-neighbor may miss distal regulatory contributions, but the magnitude of enrichment (P ~ 10⁻⁴⁴) is robust.

## Linked ideas

- Quantitative anchor for the methylation-expression coupling at NF-κB enhancers.

## Open questions

- Whether C2 demethylation is causally required for E2 up-regulation (TET2 inhibition partially answers: yes for the tested genes).
