---
title: "PADIT-seq (Protein Affinity to DNA by In vitro Transcription and sequencing)"
aliases:
  - "PADIT-seq"
  - "PADIT seq"
  - "Protein Affinity to DNA by In vitro Transcription"
  - "PADIT high-throughput TF binding assay"
  - "ALFA-tag T7 reporter affinity assay"
  - "low-affinity TF binding screen"
  - "all-10-mer TF binding library"
  - "T7-coupled TF affinity assay"
  - "nbALFA T7 RNAP TF assay"
  - "Khetan PADIT-seq"
tags:
  - transcription-factor
  - in-vitro-binding
  - high-throughput
  - low-affinity
  - synthetic-biology
  - RNA-seq-reporter
maturity: emerging
key_papers:
  - multiple-overlapping-binding-sites-determine-transcription
first_introduced: "Khetan, Carroll & Bulyk 2025 Nature"
date_updated: 2026-05-26
related_concepts:
  - low-affinity-tf-binding-site
  - overlapping-binding-sites-model
---

## Definition

PADIT-seq is a high-throughput in vitro assay that quantifies TF–DNA binding affinity by coupling TF binding directly to transcriptional output of a barcoded reporter. An ALFA-tagged DBD binds candidate TFBSs upstream of a minimal T7 promoter; an anti-ALFA nanobody (nbALFA) fused to T7 RNA polymerase is recruited proportionally to TF occupancy, producing reporter RNA whose abundance — read out by RNA-seq of TFBS-linked barcodes — is directly proportional to TF affinity. The all-10-mer library (n=1,048,576) provides exhaustive coverage of decanucleotide binding preferences and detects lower-affinity sites that uPBM, HT-SELEX, and PWM-based methods systematically miss.

## Intuition

Whereas SELEX uses repeated selection (which discards lower-affinity sequences across cycles) and PBMs measure direct fluorescent intensity (with limited dynamic range at low affinity), PADIT-seq converts binding into transcriptional amplification — a single nbALFA-T7 RNAP recruitment event yields many RNA molecules — boosting effective sensitivity for weak TF–DNA interactions while preserving quantitative ordering across affinities. The barcoded readout further decouples binding signal from probe-position artefacts seen on microarrays.

## Formal notation

- Reporter library: TGGCCTCGGC-[10N]-GGAACCTCTA upstream of D1 minimal T7 promoter; ~10^6 TFBS variants × multiple barcodes
- Readout: log2(DBD / no-DBD) per TFBS, termed PADIT-seq activity
- Active call: DESeq2-style FDR threshold; produces e.g. 554 active 10-mers (EGR1) or 1,780 active 8-mers (HOXD13)
- Validation cross-checks: MITOMI Kd (Pearson r=0.94 for EGR1), uPBM E-score AUROC > 0.97 across six TFs, custom PBM differential binding

## Variants

- All-10-bp library (genome-scale): exhaustive screen
- 9-bp focused library (896 TFBS): robustness control
- Custom PBM follow-up: differential binding of ref-vs-alt SNP probes for HOXD13/EGR1

## Comparison

- vs uPBM: PADIT-seq is concordant with uPBM at high affinity (AUROC > 0.97) but extends sensitivity into the lower-affinity regime that uPBM E-scores cannot reliably rank.
- vs HT-SELEX: HT-SELEX cycles enrich for high-affinity sequences and drop lower-affinity hits; PADIT-seq retains a flat sensitivity profile across affinity.
- vs MITOMI: MITOMI gives true Kd but at much lower throughput; PADIT-seq trades absolute Kd for genome-scale coverage with high relative ordering accuracy (r=0.94 with MITOMI).
- vs BET-seq: BET-seq measures the same 16-bp NNNNN-core-NNNNN landscape but with a much smaller flanking-only window; PADIT-seq pairs with BET-seq for paralog-competition analyses.

## When to use

- Quantifying lower-affinity TF–DNA interactions when uPBM/HT-SELEX are insufficient
- Building all-k-mer affinity tables for use in overlapping-binding-sites or partition-function models
- Predicting noncoding variant effects when PWM-based predictors underperform
- Dissecting paralog competition when paralog motifs share a core E-box

## Known limitations

- Sensitivity depends on TF and nbALFA-T7 RNAP concentrations (suboptimal levels mask lower-affinity hits)
- Sequencing depth limits FDR power for low-affinity sites
- Flanking nucleotides in the library must be chosen to avoid spurious adjoining sites — PADIT-seq libraries pre-exclude flanking 8-mers with E-score > 0.25 for the target TF
- Currently demonstrated on six TFs; extension to large DBD panels untested
- In vitro by construction — chromatin context not modelled

## Open problems

- Generalisation to all major DBD families (the paper benchmarks 4 human + 2 yeast TFs)
- Adapting the assay for very weak/transient TFs (pioneer factors, cofactor-dependent TFs)
- Combining PADIT-seq affinity tables with cellular ATAC-seq to predict in vivo occupancy de novo
- Coupling PADIT-seq with cell-state-specific cofactor pools

## Relevance to active research

PADIT-seq is the methodological foundation of [[papers/multiple-overlapping-binding-sites-determine-transcription]] and enables the central biological claim of that paper — that TF genomic occupancy is best explained by the [[overlapping-binding-sites-model]], not single-site recognition. The same all-k-mer affinity table directly feeds the [[noncoding-variant-tf-binding-effect]] analysis and the [[tf-paralogue-competition]] dissection of Pho4 vs Cbf1.
