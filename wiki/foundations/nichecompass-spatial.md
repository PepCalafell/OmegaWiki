---
title: "NicheCompass — quantitative characterization of cell niches"
slug: nichecompass-spatial
domain: "methods / spatial-transcriptomics / graph-neural-networks"
status: mainstream
aliases:
  - NicheCompass
  - Birk NicheCompass
  - quantitative niche characterization
  - NicheCompass spatial niche
  - prior-gene-program niche method
  - NicheCompass GNN
  - cell-niche characterization spatial omics
first_introduced: "Birk et al. 2025 Nature Genetics"
date_updated: 2026-05-26
source_url: "https://github.com/Lotfollahi-lab/nichecompass"
---

## Definition

NicheCompass is a graph deep-learning method that uses prior gene programs (ligand-receptor pairs, transcription factor-target relationships) to guide embedding of spatial omics data into interpretable niche representations.

## Strengths

- Biologically interpretable via prior gene programs.
- Cross-platform demonstrated.

## Known limitations

- Relies on prior gene programs — does not run on synthetic data lacking biological meaning.
- Performance depends on quality and coverage of the prior knowledge base.

## Relevance to active research

Benchmark comparator in [[papers/novae-graph-based-foundation-model-spatial]] on real spatial datasets (excluded from the synthetic-data benchmark because the priors require real gene programs).
