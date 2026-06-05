---
title: "Bladder cancer stratifies into five immune subtypes (A-E) with Class E enriched for Macro-CXCL9"
slug: five-immune-subtypes-bladder-cancer-class
status: weakly_supported
confidence: 0.5
tags: [bladder-cancer, immune-subtypes, consensus-clustering, CXCL9, classification]
domain: oncology / immunology
source_papers:
  - multiomics-analysis-cxcl9-macrophages-immunotherapy-response
evidence:
  - source: multiomics-analysis-cxcl9-macrophages-immunotherapy-response
    type: supports
    strength: moderate
    detail: "Quote (p.5): 'Using ConsensusClusterPlus package, we identified five stable bladder cancer subtypes in the IMvigor210 cohort ... labeled A through E. Unsupervised clustering revealed that Class E patients had significantly more Macro-CXCL9 than other classes (all P < 0.001).'"
conditions: "Consensus clustering on IMvigor210; in the TCGA BLCA cohort the Macro-CXCL9-high class was instead labelled Class B, so class labels are cohort-specific."
date_proposed: 2026-06-05
date_updated: 2026-06-05
---

## Statement

Consensus clustering of the IMvigor210 bladder cancer cohort yields five stable immune-based subtypes (Classes A–E), with Class E showing significantly higher Macro-CXCL9 abundance; in TCGA BLCA the Macro-CXCL9-high group corresponds to Class B.

## Evidence summary

Subtype-discovery finding from [[papers/multiomics-analysis-cxcl9-macrophages-immunotherapy-response]] using [[foundations/consensusclusterplus-consensus-clustering]]. Defines the concept [[concepts/macrophage-abundance-immune-subtypes-bladder-cancer]].

## Conditions and scope

Cohort-specific class labels; subtype number depends on consensus-clustering parameter choices.

## Counter-evidence

Stability does not guarantee biological or clinical actionability; labels differ between IMvigor210 and TCGA.

## Linked ideas

## Open questions

- Do these five immune subtypes replicate prospectively and predict differential drug response?
