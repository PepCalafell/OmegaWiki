---
title: "Protein co-expression modules and hub-protein drug targets in pan-cancer proteome"
aliases:
  - WGCNA pan-cancer proteome
  - protein co-expression modules
  - hub proteins as drug targets
  - eigenprotein modules
  - WGCNA hub protein targets
  - co-expression network cancer
  - protein module drug discovery
  - WGCNA proteome modules
  - pan-cancer co-expression
  - hub-protein nomination
tags: [wgcna, co-expression, hub-protein, drug-target, proteomics]
maturity: active
key_papers:
  - pan-cancer-proteome-atlas-mass-spectrometry
first_introduced: ""
date_updated: 2026-05-25
related_concepts: []
---

## Definition
Weighted gene co-expression network analysis (WGCNA) applied to bulk protein expression yields modules of co-regulated proteins; the top five proteins by eigenprotein correlation per module are termed hub proteins. Module hubs surface candidate drug targets that may be missed by single-gene DE analyses.

## Intuition
WGCNA captures emergent biology beyond individual proteins by grouping co-regulated nodes. In cancer, modules trace tissue-of-origin signatures plus universal stress / proliferation / immune programs. Hub proteins of universal modules are particularly interesting as cross-cancer therapeutic handles.

## Formal notation
- Bulk protein expression matrix → soft-thresholded adjacency → topological overlap → hierarchical clustering → modules
- Hub: top 5 nodes by correlation with module eigenprotein

## Variants
- Tissue-correlated modules (e.g., TPCPA modules 5, 6 → colon)
- Pan-cancer modules (e.g., module 11 → antigen presentation)

## Comparison
- vs **single-gene DE**: WGCNA surfaces functional programs and emergent hub structure.
- vs **gene-set enrichment**: WGCNA defines modules de novo rather than relying on prior annotation.

## When to use
- Discovery of co-regulated drug-target ensembles in large proteomics or transcriptomics datasets.
- Cross-cancer functional pattern mining where DE comparisons are too noisy.

## Known limitations
- Modules track tissue identity as well as malignancy.
- Hub identity is correlation-based, not mechanistic.

## Open problems
- Wet-lab validation of hub-protein dependency across cancer types.
- Integration with single-cell co-expression networks.

## Key papers
- [[papers/pan-cancer-proteome-atlas-mass-spectrometry]]

## My understanding
WGCNA on proteome data nominates hub proteins with the right tradeoff between novelty and tractability — e.g., GFPT1/HSP90 in TPCPA — but the framework is descriptive, not mechanistic. Downstream targeting decisions still need a perturbation experiment.
