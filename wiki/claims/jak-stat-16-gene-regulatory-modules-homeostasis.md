---
title: "JAK-STAT-perturbed homeostatic immune cells partition into 16 gene-regulatory modules via UMAP + walktrap"
slug: jak-stat-16-gene-regulatory-modules-homeostasis
status: supported
confidence: 0.85
tags: [jak-stat, gene-modules, umap, methodological, gene-regulatory-landscape]
domain: immunology
source_papers:
  - jak-stat-signaling-maintains-homeostasis-cells
evidence:
  - source: jak-stat-signaling-maintains-homeostasis-cells
    type: supports
    strength: strong
    detail: "Fig. 2: 6,247 DE genes (|FC|>2, Padj<0.05 in ≥1 mutant) projected by UMAP on log2FC matrix; walktrap clustering of k-NN graph yields 16 modules (A–P, 16–1,247 genes each) annotated by gene-set enrichment."
conditions: "Mouse spleen CD8+ T cell and macrophage homeostasis; 12 JAK-STAT mutant log2FCs vs WT."
date_proposed: 2026-05-22
date_updated: 2026-05-22
---

## Statement

Differentially expressed genes (n=6,247, twofold change in ≥1 JAK-STAT mutant) across homeostatic CD8+ T cells and macrophages partition into 16 gene-regulatory modules (labeled A–P) via UMAP-based similarity + walktrap graph clustering. Each module has distinct mutant-specific effect patterns and characteristic biological-process enrichments (e.g. module P = ISG core; module D = oxidative phosphorylation/mRNA splicing; module M = β1-integrin/NCAM1; module F = ribosomal/translation).
