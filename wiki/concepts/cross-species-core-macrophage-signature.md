---
title: "Cross-species core macrophage signature"
aliases:
  - core macrophage signature
  - activation-independent macrophage core signature
  - human-mouse macrophage core genes
tags:
  - macrophage
  - comparative-transcriptomics
  - signature
maturity: emerging
key_papers:
  - transcriptome-based-network-analysis-reveals-spectrum
first_introduced: "Xue et al. 2014 Immunity (refinement of ImmGen core)"
date_updated: 2026-06-02
related_concepts:
  - spectrum-model-macrophage-activation
  - macrophage-ontogeny-resident-vs-monocyte-derived
---

## Definition
A refined, activation-independent set of genes (and a small surface-marker panel) that identifies macrophages across both human and mouse, obtained by overlaying human macrophage activation transcriptomes onto the ImmGen-defined murine macrophage and dendritic-cell core signatures and retaining genes whose macrophage-vs-DC differential expression is conserved irrespective of activation state.

## Intuition
ImmGen's murine core signatures do not all transfer to human, and some genes lose their macrophage-defining differential expression upon activation. Filtering for genes that stay macrophage-specific across all human stimulation conditions yields a robust, species-portable core.

## Formal notation
- Human orthologs of ImmGen murine macrophage (Gautier 2012) and DC (Miller 2012) core genes
- Three gene groups: (1) conserved differential expression irrespective of activation; (2) lost differential expression after certain stimuli; (3) non-conserved / oppositely regulated
- Surface markers distinguishing macrophages from DCs + monocytes: CD14, FCGR2A (CD32), MERTK, FCGR1A (CD64), ANPEP (CD13)

## Variants
- Macrophage core signature vs DC core signature (analysed in parallel)

## Comparison
vs ImmGen raw murine core: refined to exclude activation-sensitive and non-conserved genes, making it applicable to human data and to animal-model design.

## When to use
- Discriminating macrophages from DCs / monocytes by flow cytometry across species
- Choosing animal-model markers that reflect human macrophage biology

## Known limitations
- Derived from monocyte-derived macrophages and blood-cell comparators, not tissue-resident populations.
- Surface-marker panel validated by flow cytometry on limited samples.

## Open problems
- Extending the core to tissue-resident macrophage ontogenies.
- Same-tissue human↔mouse comparisons in homeostasis and disease.

## Key papers
- [[papers/transcriptome-based-network-analysis-reveals-spectrum]] — Xue et al. 2014: proposed the refined cross-species core signature and surface-marker panel.

## My understanding
The "housekeeping macrophage identity" complement to the activation spectrum: what stays macrophage regardless of stimulus, and which markers travel between mouse and human. Practically useful for marker-panel design.
