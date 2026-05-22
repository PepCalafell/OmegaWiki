---
title: "Embedding outputs of integration methods tend to outperform gene-corrected matrix outputs of the same method"
slug: embedding-outputs-outperform-gene-corrected
status: supported
confidence: 0.75
tags:
  - data-integration
  - scRNA-seq
  - output-type
  - embeddings
domain: single-cell-methods
source_papers:
  - benchmarking-atlas-level-data-integration-single
evidence:
  - source: "[[papers/benchmarking-atlas-level-data-integration-single]]"
    type: supports
    strength: medium
    detail: "Comparing Scanorama (embedding) > Scanorama (gene), FastMNN (embedding) > FastMNN (gene) — higher-abstraction output ranks higher in aggregate scIB score on RNA tasks."
conditions: "Holds when the downstream analysis is cluster-based (cell-type identification, embedding visualization). For analyses requiring corrected gene-expression values (functional gene scoring, trajectory pseudotime in gene space), gene-corrected outputs remain necessary."
date_proposed: 2026-05-22
date_updated: 2026-05-22
---

## Statement

For integration methods that produce both an embedding output and a gene-corrected matrix output (Scanorama, FastMNN), the embedding output consistently outperforms the gene-corrected output on the scIB aggregate score for RNA atlas tasks. Higher-abstraction representations are more robust to residual batch noise than per-gene correction.

## Evidence summary

Quote (p.45): "The methods with a higher level of abstraction tended to rank higher (in particular comparing Scanorama and FastMNN's embeddings and corrected expression matrix output)."

## Conditions and scope

- For cluster-based downstream analyses, prefer embedding outputs.
- For functional gene-program scoring or per-gene trajectory analysis, gene-corrected outputs are still required despite lower aggregate score.
- The advantage applies within-method; cross-method, the best gene-corrected outputs (Scanorama gene, ComBat) still outperform many weak embedding outputs.

## Counter-evidence

- Gene-corrected outputs of scGen rank top of overall list when scalability is not the bottleneck.

## Linked ideas

(none yet)

## Open questions

- Is the gap driven by lossy gene-level reconstruction or by the embedding's denoising effect?
