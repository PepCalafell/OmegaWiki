---
title: "TF paralogue competition for shared binding sites"
aliases:
  - "TF paralog competition"
  - "TF paralogue binding specificity"
  - "paralog TF competition"
  - "paralog TF binding specificity"
  - "shared-motif paralog TFs"
  - "Pho4 Cbf1 competition"
  - "co-expressed paralog TFs"
  - "paralog displacement at shared motifs"
  - "differential flanking specificity paralog TF"
tags:
  - transcription-factor
  - paralog
  - DNA-binding
  - evolution
  - flanking-nucleotides
maturity: stable
key_papers:
  - multiple-overlapping-binding-sites-determine-transcription
first_introduced: "Multiple — formalised in Khetan, Carroll & Bulyk 2025 via OBS model"
date_updated: 2026-05-26
related_concepts:
  - overlapping-binding-sites-model
  - low-affinity-tf-binding-site
---

## Definition

TF paralogue competition is the phenomenon by which two or more paralogous TFs that recognise highly similar core motifs achieve distinct genomic binding outcomes. Specificity arises despite shared cores because the flanking nucleotides create differential numbers of overlapping low-affinity binding sites for each paralog, generating quantitative binding-affinity differences that determine which paralog wins at each locus under competing concentrations.

## Intuition

Paralogous TFs with identical core motifs (e.g. CACGTG for Pho4 and Cbf1) cannot be told apart by PWMs alone, yet in vivo each has a distinct ChIP-seq footprint. Khetan 2025 shows that 5 bp of flanking sequence on each side of the shared core changes how many of the nine overlapping 8-mers are active for Pho4 vs Cbf1; the difference in counts (and especially the difference in summed PADIT-seq activity) predicts BET-seq ΔΔΔG (r=0.948), in vitro competition outcomes, and in vivo ChIP-seq dominance.

## Formal notation

- For paralogs A and B sharing core motif M with flanks F: predict ΔΔΔG(A,B) ∝ Σ activity_A(k-mers in F-M-F) − Σ activity_B(k-mers in F-M-F)
- Adjusted r² = 0.898 (Pho4/Cbf1 BET-seq, n=1,048,576 flanking variants)
- ~50% reduction in unexplained variance vs PWM-only models (r² 0.633 PWM → 0.898 with OBS contribution)

## Variants

- bHLH paralogs at E-box (Pho4 vs Cbf1; bHLH/HLH families)
- HOX paralogs with shared homeodomain cores
- bZIP/AP-1 family (referenced via flanking studies — Cohen 2018, Chaudhari 2018)

## Comparison

vs cooperative-cofactor models: paralog competition here is purely flanking-sequence-driven, no obligate cofactor needed
vs concentration-only models: Pho4 nuclear translocation in low phosphate is necessary but not sufficient; flanking-determined overlapping site counts determine which loci Pho4 wins
vs PWM-only specificity: PWM captures core preference but residual variance is high; OBS contribution explains ~50% of that residual

## When to use

- Predicting which paralog dominates at a locus with shared core motif
- Designing perturbation experiments (paralog KO) to confirm shared-vs-private site predictions
- Interpreting evolution of flanking sequence at paralog-divergent enhancers

## Known limitations

- Demonstrated cleanly for Pho4/Cbf1; quantitative dissection for higher-paralog families (Hox A/B/C/D) untested
- Concentration-driven displacement still matters; model decomposes the affinity component but not the kinetic competition

## Open problems

- Whether flanking sequences at paralog-shared sites have evolved under selection to encode differential overlapping-site counts
- Extension to >2 paralog systems
- Generalising to bZIP, MADS-box, and other shared-core TF families

## Relevance to active research

In [[papers/multiple-overlapping-binding-sites-determine-transcription]], the Pho4/Cbf1 competition system is the cleanest demonstration of the [[overlapping-binding-sites-model]] as a quantitative predictor of paralog binding specificity — providing the mechanistic answer to a long-standing puzzle in transcriptional regulation.
