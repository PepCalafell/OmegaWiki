---
title: "Cytokine-mediated immune cell–cell interactome (production × response matrix)"
aliases:
  - cytokine-mediated cell-cell interactome
  - cytokine interactome
  - cytokine production-response map
  - immune cell-cell network
  - cytokine cell-cell communication graph
  - FRC cytokine hub
  - cDC1 IL-1β broadcaster
  - cytokine bipartite graph
  - immune network connectivity
  - interactome from Immune Dictionary
maturity: stable
tags:
  - cytokine-networks
  - cell-cell-communication
  - immune-network
  - lymph-node
key_papers:
  - dictionary-immune-responses-cytokines-single-cell
  - single-cell-cytokine-dictionary-human-peripheral
first_introduced: "2024"
date_updated: 2026-05-13
related_concepts:
  - cytokine-cell-type-specific-response-pleiotropy
  - cytokine-receptor-expression-insufficient-cytokine-response
  - rare-immune-cell-types-produce-many
---

## Definition

The Immune Dictionary cytokine-mediated cell–cell interactome combines (i) per-cell-type cytokine production levels (from baseline + perturbation expression) with (ii) per-cell-type cytokine response signatures, yielding a bipartite production × response graph. The graph reveals that most immune cell types can affect most other cell types through at least one cytokine — a highly interconnected network — with FRCs and cDC1s as broadcast hubs.

## Intuition

The Immune Dictionary makes the cell–cell cytokine network quantitative and per-cell-type-resolved, replacing earlier qualitative ligand–receptor wiring diagrams. Specific edges (e.g., cDC1 → many cells via IL-1β) are testable hypotheses for in vivo immune coordination.

## Variants

- FRC-centric interactome (broadcasts >40 cytokines)
- cDC1-centric interactome (concentrated on IL-1β)
- Pairwise cell type → cell type edges per cytokine

## When to use

Reference network for any tissue-immune communication analysis; useful when designing perturbation experiments to test source → sink hypotheses.

## Open problems

- Whether the lymph-node interactome generalizes to inflamed tissue / tumours
- Spatial constraints (which interactions occur in which microniche)
- Temporal dynamics of network reconfiguration during disease

## Key papers

- [[papers/dictionary-immune-responses-cytokines-single-cell]]
- [[papers/single-cell-cytokine-dictionary-human-peripheral]] — human PBMC interactome via sender-strength × receiver-sensitivity interaction scores; IL-32 emerges as a dominant connector from all T-cell subtypes, NK CD56hi signals to nearly all cell types, NK CD56low signals to none

## My understanding

The most concrete cytokine network to date in mouse immunology. For HypoxiaVERSE TAM/NK work, this is a reference template against which the hypoxic tumour cytokine network can be benchmarked.
