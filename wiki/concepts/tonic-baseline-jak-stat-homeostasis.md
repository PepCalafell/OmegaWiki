---
title: "Tonic / baseline JAK-STAT signaling in homeostatic immune cells"
aliases:
  - "baseline JAK-STAT signaling"
  - "tonic JAK-STAT signaling"
  - "tonic interferon signaling"
  - "constitutive type I IFN signaling"
  - "homeostatic JAK-STAT activity"
  - "low-level ISG expression homeostasis"
  - "unstimulated JAK-STAT activity"
  - "baseline ISGF3 activity"
  - "poised JAK-STAT state"
  - "steady-state ISG expression"
  - "tonic STAT2-IRF9 priming"
tags: [immunology, jak-stat, interferon, homeostasis, ISG, epigenetics]
maturity: active
key_papers:
  - jak-stat-signaling-maintains-homeostasis-cells
first_introduced: "2024"
date_updated: 2026-05-22
related_concepts: [isgf3-independent-irf9-function, tissue-context-dependence-immune-signaling, stat1-isoform-specificity-alpha-beta]
---

## Definition

A pathway-level transcriptional and chromatin-accessibility state in unstimulated immune cells in vivo, in which JAK-STAT components — particularly the ISGF3 complex (STAT1/STAT2/IRF9), TYK2, STAT3, and STAT5 — maintain low-level expression of interferon-stimulated genes (ISGs) and other target genes under steady-state, non-inflammatory conditions. It is **distinct from acute cytokine-driven JAK-STAT signaling** by (i) gene-set partial overlap with the ISG-core only, (ii) cell-type-specific cooperative architecture (STAT3/STAT5 cooperate with ISGF3 members in macrophages), and (iii) cell-extrinsic dependence on the in vivo tissue context.

## Intuition

Immune cells need to be **ready** to respond to stimuli, not just **able** to respond. The JAK-STAT pathway, classically described as inducible, also maintains the homeostatic transcriptional and chromatin state that primes cells for rapid activation. This baseline activity collapses when cells leave the tissue niche and is partially restored by type I IFN stimulation.

## Variants

- **ISGF3-driven baseline** (STAT1/STAT2/IRF9 cooperating, tonic IFN): the canonical low-level antiviral/ISG axis.
- **ISGF3-independent IRF9 baseline**: IRF9 regulates Rdh14, Tprkb, Usb1 and partially overlaps with STAT3/STAT5 macrophage targets.
- **Epigenome-maintenance baseline**: STAT5/STAT6 act as repressors of macrophage chromatin under homeostasis (M1-enhancer repression); STAT1 has a chromatin effect that exceeds its transcriptional footprint.

## When to use

- Interpreting low-level ISG expression in unstimulated immune cells as **active** signaling, not background noise.
- Designing experiments that compare in vivo vs ex vivo immune cells — expect collapse of baseline JAK-STAT after ~20 h ex vivo culture.
- Reading bulk RNA-seq of TILs / tissue macrophages: high ISG signature can reflect tonic baseline activity, not necessarily acute IFN exposure.

## Known limitations

- Mechanistic origin (which ligand, which producer cell type) is not yet pinpointed — CellChat-nominated candidate pairs (KLRB1-CLEC2B, SIGLEC1-SPN, LILRB1-HLA-F, HAVCR2-LGALS9) are computational hypotheses.
- All current evidence is in mouse spleen; cross-tissue and human generalization is open.
- Cannot fully separate "tonic IFN-driven" from "non-IFN-driven baseline JAK-STAT" in vivo.

## Open problems

- Map cell-extrinsic ligands and source cells for baseline JAK-STAT in each tissue.
- Determine whether baseline activity itself shapes responsiveness to cytokine stimulation (priming gain).
- Test whether disease-associated JAK-STAT variants disrupt baseline more than induced signaling.

## Key papers

- [[jak-stat-signaling-maintains-homeostasis-cells]] — Fortelny et al. 2024 Nature Immunology: the comprehensive 12-mutant epigenome+transcriptome dissection that defines this concept.
