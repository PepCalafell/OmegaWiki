---
title: "Tumor core (TC) vs leading edge (LE) — spatially distinct transcriptional architectures of solid tumors"
aliases:
  - tumor core
  - leading edge
  - tumour core leading edge
  - TC vs LE
  - TC LE spatial architecture
  - invasive edge transcriptional program
  - tumor invasive front
  - core-edge tumor compartments
  - leading edge OSCC
  - tumour core gene signature
  - invasive front signature
  - TC LE compartments
tags: [spatial-transcriptomics, tumor-microenvironment, OSCC, pan-cancer, EMT, keratinization]
maturity: active
key_papers:
  - spatial-transcriptomics-reveals-distinct-conserved-tumor
first_introduced: "Arora & Cao et al. 2023 Nat Commun (formalised as ST-derived TC/LE)"
date_updated: 2026-05-22
related_concepts: []
---

## Definition
TC and LE are two transcriptionally distinct, spatially defined compartments of a solid tumour. The TC sits in the central, more differentiated bulk and is enriched for keratinization and epithelial programs; the LE is the invasive front, enriched for ECM remodelling, partial-EMT, angiogenesis and cell-cycle programs.

## Intuition
The boundary of a tumour is biologically different from its centre. ST captures that difference quantitatively: cells in the same patient that share a CNV lineage and lineage history nonetheless adopt sharply different transcriptional programs based on their spatial position.

## Variants
- OSCC TC/LE (this paper's reference definition)
- pan-cancer-projected TC/LE via scPred classifier
- earlier IHC-based LE definitions (low-throughput, limited markers)

## Comparison
Older histopathological LE definitions (Bryne et al.) used cellular morphology and tumour-budding scores. The ST-derived TC/LE definition is transcriptome-wide and includes a transitory cluster that bridges the two.

## When to use
- Stratifying tumours by spatial transcriptional architecture
- Designing therapies that target invasive-front biology
- Re-interpreting bulk RNA-seq with single-sample TC/LE enrichment scores

## Known limitations
- TC programs are tissue-specific; TC annotations transfer poorly to e.g. hepatocellular carcinoma or medulloblastoma
- Visium spots are 55 µm — TC/LE boundaries within a spot are unresolved
- LE program may capture both true invasive cells and reactive stromal neighbours

## Open problems
- Mechanistic upstream regulators that switch TC → LE in vivo
- Whether TC-like induction is therapeutically achievable

## Key papers
- [[papers/spatial-transcriptomics-reveals-distinct-conserved-tumor]]

## My understanding
TC vs LE behaves more like a continuum of cancer cell states than a hard binary; the transitory cluster is consistent with that. The most useful claim downstream is the prognostic one — LE-high → worse outcomes in many cancers — because it makes the architecture clinically actionable.
