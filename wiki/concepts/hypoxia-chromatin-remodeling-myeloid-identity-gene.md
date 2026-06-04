---
title: "Hypoxia-driven chromatin remodeling of myeloid identity gene promoters"
aliases: []
tags: [hypoxia, chromatin-accessibility, ATAC-seq, microglia, P2RY12, epigenomics, transcription-factors]
maturity: emerging
key_papers:
  - hypoxic-stress-dysregulates-functions-glioma-associated
first_introduced: "2025"
date_updated: 2026-06-04
related_concepts: [open-chromatin-predefined-macrophage-activation-tr, tissue-specific-lineage-determining-factors-macrophage, hif1a-nf-kb-cooperative-chromatin-binding, hypoxia-confounds-gam-subtype-marker-classification, direct-glioma-microglia-co-culture-under]
---

## Definition

The mechanism by which hypoxia — especially combined with glioma contact — reshapes chromatin accessibility at the promoters of myeloid/microglial identity genes, fine-tuning their expression. Hypoxia alone reduces promoter accessibility globally, while glioma co-culture under hypoxia drives extensive promoter remodeling: the *P2ry12* promoter loses accessibility at a peak bearing SPI1/PU.1 and IRF8 motifs, whereas the *Lgals3* promoter gains an accessible region enriched for AP1/ATF3 motifs.

## Intuition

Beyond the immediate transcriptional response to hypoxia (driven by HIF and other fast-acting TFs), a slower epigenomic layer opens and closes specific identity-gene promoters. Closing the PU.1/IRF8-controlled *P2ry12* promoter erodes microglial identity; opening the AP1/ATF3-controlled *Lgals3* promoter installs a monocytic/lipid program.

## Formal notation

- Readout: ATAC-seq differential peaks (promoter vs genic vs distal), TF-motif enrichment (HOMER/FIMO).
- Concordance with RNA is partial (Pearson/Spearman ≈ 0.24), so chromatin remodeling explains only a subset of expression changes.

## Variants

- Promoter-only vs genic peaks: HIF-target genes gain accessibility predominantly at genic (non-promoter) regions.
- Hypoxia-alone (accessibility loss) vs hypoxia+glioma (promoter opening) regimes.

## Comparison

Builds on lineage-determining-factor logic ([[concepts/tissue-specific-lineage-determining-factors-macrophage]], [[concepts/open-chromatin-predefined-macrophage-activation-tr]]) and complements fast HIF/NF-κB transcriptional responses ([[concepts/hif1a-nf-kb-cooperative-chromatin-binding]]).

## When to use

Invoke when explaining how hypoxia produces durable, identity-level myeloid changes rather than only transient gene induction, and when interpreting ATAC-seq in tumor myeloid cells.

## Known limitations

- Partial RNA–ATAC concordance; some accessibility changes lack expression consequences (possibly 3D-structure or timing effects).
- Motif enrichment is correlative; TF causality not established.

## Open problems

- Which chromatin modifiers execute the closing/opening (HDACs, demethylases)?
- Time-resolved and chromatin-conformation studies to link accessibility to expression.

## Key papers

- [[papers/hypoxic-stress-dysregulates-functions-glioma-associated]]

## My understanding

This is the epigenomic core of the paper and the most thesis-relevant concept: hypoxia as a chromatin-level regulator of myeloid identity, acting partly through loss of accessibility at PU.1/IRF8 sites.
