---
title: "Novae achieves the highest ARI and FIDE on a 5-slide / 7-domain synthetic spatial transcriptomics benchmark"
slug: novae-best-ari-fide-synthetic-dataset
status: supported
confidence: 0.85
tags:
  - spatial-transcriptomics
  - benchmark
  - synthetic-data
  - methodological
domain: methods
source_papers:
  - novae-graph-based-foundation-model-spatial
evidence:
  - source: novae-graph-based-foundation-model-spatial
    type: supports
    strength: strong
    detail: "Synthetic dataset: 5 slides, 7 spatial domains, shared gene panel. Across 5 random seeds, Novae (fine-tuned) achieves the highest mean ARI and FIDE with notably low s.d., outperforming SpaceFlow, GraphST, STAGATE, SEDR, Scanpy (Fig. 3f-g)."
conditions: "Synthetic gene expression — zero-shot Novae excluded because pretraining priors do not apply; NicheCompass excluded because synthetic data lacks ligand-receptor / TF-target structure required for its priors."
date_proposed: 2026-05-26
date_updated: 2026-05-26
---

## Statement

On a controlled synthetic spatial-transcriptomics benchmark (5 slides, 7 ground-truth domains, shared panel), fine-tuned Novae achieves the highest mean ARI and FIDE across 5 random seeds with low variance, beating SpaceFlow, GraphST, STAGATE, SEDR, and Scanpy.

## Evidence summary

Fig. 3f (ARI box plots, n=5 seeds), Fig. 3g (FIDE box plots, n=5 seeds).

## Conditions and scope

Synthetic data — useful as a controlled-ground-truth benchmark but not a complete test of real-tissue performance.

## Counter-evidence

Zero-shot Novae and NicheCompass not included; results are for fine-tuned Novae only.

## Linked ideas

— none yet.

## Open questions

- Whether synthetic-data ARI rankings transfer to real DLPFC-style annotated benchmarks.
