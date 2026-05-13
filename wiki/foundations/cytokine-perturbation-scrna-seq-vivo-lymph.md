---
title: "In vivo cytokine perturbation scRNA-seq (lymph-node injection)"
slug: cytokine-perturbation-scrna-seq-vivo-lymph
domain: immunology / methods / single-cell
status: mainstream
aliases:
  - in vivo cytokine perturbation
  - lymph node cytokine injection scRNA-seq
  - skin-draining lymph node perturbation
  - subcutaneous cytokine injection mouse
  - 4-hour cytokine response scRNA-seq
  - Cui Hacohen lymph node perturbation protocol
  - droplet scRNA-seq cytokine perturbation
  - PBS-controlled cytokine atlas
first_introduced: "2024"
date_updated: 2026-05-13
source_url: "https://doi.org/10.1038/s41586-023-06816-9"
---

## Definition

Methodology for systematic in vivo cytokine perturbation profiling: subcutaneous/intradermal injection of recombinant carrier-free cytokine (5 μg in 100 μl PBS) in the abdominal flank of wild-type C57BL/6 mice, collection of bilateral skin-draining inguinal lymph nodes 4 h post-injection, enzymatic dissociation, cell sorting to rebalance frequencies and high-throughput sample multiplexing for 10x droplet scRNA-seq.

## Intuition

The 4-hour timepoint captures the majority of immediate-early transcriptomic responses while minimizing secondary cytokine-induced waves. Cell sorting ensures rare cell types (basophils, ILCs, FRCs) are represented at analysable depths. PBS controls per batch enable robust DEG calling.

## Relevance to active research

Reusable protocol template for in vivo cytokine perturbation profiling. Generalizable to other tissues (e.g., tumour-draining LNs, mucosal LNs) and to combinatorial cytokine perturbations.
