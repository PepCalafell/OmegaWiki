---
title: "OSCC tumours organise into spatially distinct, patient-conserved TC and LE transcriptional compartments"
slug: oscc-tc-le-spatial-architectures-conserved
status: supported
confidence: 0.85
tags: [spatial-transcriptomics, OSCC, mechanistic, TC-LE]
domain: oncology/spatial-transcriptomics
source_papers:
  - spatial-transcriptomics-reveals-distinct-conserved-tumor
evidence:
  - source: spatial-transcriptomics-reveals-distinct-conserved-tumor
    type: supports
    strength: strong
    detail: "Unsupervised Louvain clustering of 13950 malignant ST spots across 12 OSCC samples (10 patients) yields three nodal clusters that map to TC, transitory and LE via literature-validated markers; TC-TC and LE-LE inter-patient correlation is high while within-patient TC vs LE correlation is low."
conditions: "HPV-negative OSCC, Visium 10x ST, ≥0.99 CARD or Numbat malignancy threshold"
date_proposed: 2026-05-22
date_updated: 2026-05-22
---

## Statement
HPV-negative OSCC tumours organise spatially into transcriptionally distinct TC and LE compartments that are conserved across patients.

## Evidence summary
DGEA across 12 samples identifies 117 TC-up and 91 LE-up genes (≥10/12 samples, adj. p<0.001). Pearson correlation across whole-transcriptome profiles shows high TC-TC and LE-LE inter-patient correlation but low intra-patient TC-vs-LE correlation.

## Conditions and scope
HPV-negative OSCC, surgical resections, 10x Visium platform, Seurat SCTransform normalisation, Louvain resolution 1.0.

## Counter-evidence
None within this paper. Earlier histopathological LE definitions did not capture transitory cells.

## Linked ideas

## Open questions
Whether the same conservation holds in HPV-positive OSCC and other subsites of HNSCC.
