---
title: "Overlapping binding sites model of TF occupancy"
aliases:
  - "overlapping binding sites model"
  - "OBS model"
  - "overlapping TFBS model"
  - "consecutive overlapping binding sites"
  - "additive overlapping TFBS model"
  - "single-TF multiple-overlapping-site binding"
  - "Khetan-Bulyk overlapping sites model"
  - "lower-affinity overlapping site framework"
  - "TF additive site occupancy model"
  - "flanking-nucleotide additive TFBS model"
tags:
  - transcription-factor
  - DNA-binding
  - low-affinity
  - additivity
  - paralogue-competition
  - noncoding-variants
maturity: emerging
key_papers:
  - multiple-overlapping-binding-sites-determine-transcription
first_introduced: "Khetan, Carroll & Bulyk 2025 Nature"
date_updated: 2026-05-26
related_concepts:
  - padit-seq
  - low-affinity-tf-binding-site
  - tfbs-weavability
  - tf-paralogue-competition
  - noncoding-variant-tf-binding-effect
---

## Definition

The overlapping binding sites model states that TF genomic occupancy at a locus is the additive sum of binding contributions from multiple, consecutive, partially overlapping TFBSs — typically a single high-affinity central k-mer flanked by lower-affinity overlapping k-mers offset by 1 bp. A single TF molecule occupies each overlapping site independently rather than recognising one extended motif. Increasing the number of consecutive overlapping active k-mers additively increases binding strength, and is observed as a 1-bp incremental footprint expansion in ChIP-nexus.

## Intuition

Classical PWM/motif models score a TF binding site as one match per location. In reality, the lower-affinity sequence neighbourhood around a high-affinity match also contributes — every 1-bp shift produces another (weaker) k-mer that the same TF can bind. The flanking nucleotides therefore matter not because they tweak the "extended motif" but because they create or destroy additional independent binding events that sum into total occupancy.

## Formal notation

- Binding contribution at position p: sum over k of activity(s_{p..p+k-1})
- Active k-mers: k-mers passing the PADIT-seq active threshold (FDR-controlled)
- Consecutive count C: number of consecutive active k-mers in 1-bp steps inside a window
- Footprint signature (ChIP-nexus): 1-bp increment in 5'-cut span per additional overlapping site
- Variant effect predictor: ΔPADIT-seq summed across all overlapping k-mers covering the SNP

## Variants

- Single-TF additive (this paper): one TF molecule per overlapping site
- vs homotypic clustering: multiple non-overlapping low-affinity sites tens-to-hundreds of bp apart; same TF, multiple molecules at once
- vs STR partition function (Horton 2023): TF binding to short tandem repeats flanking core motifs; multiple molecules across STR units
- vs iMITOMI homotypic clusters (Razo-Mejia 2020-ish; cited as ref 76): multiple molecules at distinct clustered sites
- Generalisation to weavability: arbitrary TF whose top-affinity k-mers form a densely-connected (k-1)-overlap graph (~199/200 TFs in UniPROBE)

## Comparison

vs PWM-only models: PWMs treat each motif match independently and ignore flanking lower-affinity sites; the OBS model reduces residual variance unexplained by PWMs by ~50% (Pho4/Cbf1 paralog discrimination).
vs partition-function STR model: OBS focuses on a single TF molecule across overlapping sites in <30 bp; STR model focuses on multiple TFs across repeat tracts.
vs extended-motif models: extended-motif would predict a smooth flanking preference and a fixed footprint size; OBS predicts discrete 1-bp footprint increments, which is what ChIP-nexus shows.

## When to use

- Predicting in vivo TF ChIP-seq peak intensities when ranked by single-site affinity underperforms (Pearson r 0.29-0.50 with sum of overlapping activities)
- Interpreting paralog-TF competition at shared core motifs (Pho4 vs Cbf1 at CACGTG)
- Scoring noncoding variant effects when MotifBreakR misses subtler multi-site effects
- Designing synthetic enhancers when flanking nucleotides need to be tuned for additive control

## Known limitations

- Demonstrated mainly on 6 TFs in vitro and validated in vivo on a subset; broad-spectrum in vivo generalisation untested
- Energy contributions are not yet expressed in absolute thermodynamic units
- The model focuses on single-TF binding; cofactor- and chromatin-mediated effects are not modelled
- Effect sizes for chromatin-bound TF occupancy remain modest (r 0.29-0.50)

## Open problems

- Quantitative formulation in thermodynamic / partition-function form
- Whether weavability and overlapping-site additivity extends to prokaryotic TFs
- Evolution: did flanking sequences evolve to tune paralog specificity by tuning number of overlapping sites?
- Coupling with chromatin accessibility / cofactor interactions to improve in vivo prediction

## Relevance to active research

Defined and validated in [[papers/multiple-overlapping-binding-sites-determine-transcription]]. The model unifies three open problems in TF biology: lower-affinity site interpretation (via [[padit-seq]]), paralog binding specificity (via [[tf-paralogue-competition]]), and noncoding-variant effects (via [[noncoding-variant-tf-binding-effect]]). It also predicts the [[tfbs-weavability]] property — that TF binding sites form densely connected (k-1)-overlap graphs.
