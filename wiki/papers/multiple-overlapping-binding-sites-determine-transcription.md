---
# === Identification ===
title: "Multiple overlapping binding sites determine transcription factor occupancy"
slug: multiple-overlapping-binding-sites-determine-transcription
arxiv: ""
doi: "10.1038/s41586-025-09472-3"
pmid: "40903577"
venue: "Nature"
year: 2025
authors: ["Shubham Khetan", "Brent S. Carroll", "Martha L. Bulyk"]
first_author: "Shubham Khetan"
corresponding_author: "Martha L. Bulyk"

# === Source & metadata ===
source_type: pdf
s2_id: "6f725683c7170d606efd1ca9eb1789132c626c8a"
date_added: 2026-05-26
ingested_date: 2026-05-26
ingest_version: 1
last_reviewed:

# === Classification ===
importance: 4
tier: TIER_1
tags: [transcription-factor, DNA-binding, low-affinity-TFBS, overlapping-binding-sites, paralog-competition, noncoding-variants, regulatory-genomics, method-development]
keywords: [PADIT-seq, overlapping binding sites, lower-affinity TFBS, HOXD13, EGR1, NKX2.5, TBX5, Pho4, Cbf1, ChIP-nexus, SNP effects, paralog competition, TFBS weavability]
domain: regulatory-genomics

# === Biomedical domain ===
tissue: [in_vitro_only, multi]
condition: [healthy]
disease_specific: [preaxial_polydactyly]
species: [human, mouse, yeast]
hypoxia_relevant: false
contains_immune_cells: false
contains_myeloid: false

# === Technique ===
techniques: [PADIT-seq, uPBM, HT-SELEX, ChIP-seq, ChIP-nexus, custom_PBM, BET-seq, MPRA, MITOMI, SNP-SELEX]
n_samples:
n_cells_total:
integration_method: ""

# === Biology captured ===
key_cell_types: [in_vitro, mouse_forelimb_bud, mouse_frontal_cortex, human_cardiomyocyte, S_cerevisiae]
key_markers: [HOXD13, EGR1, NKX2.5, TBX5, Pho4, Cbf1, CACGTG_E-box]
key_pathways: [TF-DNA_binding, cis-regulatory_grammar, paralog_competition, noncoding_variant_interpretation]

# === User project membership ===
projects: [thesis]
priority: high
read_status: read

# === HypoxiaVERSE-specific ===
hypoxiaverse_status:
exclusion_reason:
data_availability: "Supplementary Information at https://doi.org/10.1038/s41586-025-09472-3"

# === Cross-references ===
code_url: ""
cited_by: []
---

## Problem

Transcription factors (TFs) regulate gene expression by sequence-specific DNA binding, but high-throughput in vitro methods (uPBM, HT-SELEX) systematically miss lower-affinity binding sites, which developmental biology has long shown are functionally critical. Two open consequences of this blind spot remained unresolved: (1) how paralogous TFs with shared core motifs achieve distinct in vivo binding, and (2) how noncoding variants alter TF binding when they do not destroy or create a consensus motif match. Khetan et al. develop PADIT-seq to comprehensively measure lower-affinity sites and use the resulting all-10-mer affinity tables to propose a unifying overlapping-binding-sites model.

## Key idea

A TF's genomic occupancy at a locus is the additive sum of binding contributions from multiple, consecutive, 1-bp-offset overlapping TFBSs — a single high-affinity central k-mer flanked by lower-affinity overlapping k-mers — with each overlapping site bound independently by a separate TF molecule. The model is built on the all-10-mer PADIT-seq affinity table ([[concepts/padit-seq]]) and unifies (i) the additive in vivo occupancy signature (ChIP-nexus footprint grows in 1-bp increments per added overlapping site), (ii) paralog competition at shared E-box cores ([[concepts/tf-paralogue-competition]] — Pho4 vs Cbf1), and (iii) noncoding-variant effects that PWM/MotifBreakR miss ([[concepts/noncoding-variant-tf-binding-effect]]). It rests on the intrinsic [[concepts/tfbs-weavability]] property that high-affinity k-mers form a densely-connected (k-1)-overlap graph across 199/200 surveyed eukaryotic TFs.

## Method

- **PADIT-seq** ([[concepts/padit-seq]]): TF DBD with ALFA tag recruits nbALFA-T7 RNA polymerase to a barcoded reporter with TGGCCTCGGC-[10N]-GGAACCTCTA candidate TFBSs upstream of a minimal T7 promoter; RNA-seq counts of barcoded reporter transcripts encode TF–DNA affinity log2(DBD/no-DBD). Reporter library covers all 1,048,576 10-mers per TF.
- **Six benchmark TFs** spanning four DBD families: [[foundations/hoxd13-tf]] (homeodomain), [[foundations/egr1-tf]] (C2H2 zinc-finger), [[foundations/nkx2-5-tf]] (homeodomain), [[foundations/tbx5-tf]] (T-box), [[foundations/pho4-tf]] and [[foundations/cbf1-tf]] (bHLH yeast paralogs).
- **Validation orthogonals**: MITOMI Kd (Pearson r=0.94 EGR1), [[foundations/upbm-protein-binding-microarray]] (AUROC > 0.97 across all six TFs), custom PBMs.
- **In vivo occupancy**: ChIP-seq for HOXD13 (mouse forelimb bud), EGR1 (mouse cortex), NKX2.5/TBX5 (human cardiomyocytes), Pho4/Cbf1 (yeast); [[foundations/chip-nexus]] for Pho4/Cbf1 with 5'-end cut-position analysis.
- **Sliding-window k-mer scoring**: 1-bp-step counting of consecutive PADIT-seq active k-mers within peaks; comparison to length-matched genomic background; PhastCons conservation across overlapping k-mer regions.
- **Paralog competition**: re-analysis of published BET-seq ΔΔΔG for Pho4 vs Cbf1 across all 1,048,576 NNNNN-CACGTG-NNNNN sequences; PWM-only vs OBS regression comparison; genomic-context PBMs + in vivo ChIP-seq in Δpho80 and Δpho80Δcbf1 yeast.
- **Variant-effect prediction**: PADIT-seq scoring of 5,748 HOXD13 and 4,136 EGR1 noncoding variants from [[foundations/snp-selex]]; custom PBMs on ~280 variants per TF; benchmark against [[foundations/motifbreakr]] (PWM) and SNP-SELEX PBS; allele-specific ChIP-seq concordance; MPRA expression validation.
- **Weavability**: directed (k-1)-overlap k-mer networks for the six PADIT-seq TFs and for top-500 8-mers of 200 human/mouse TFs from UniPROBE across 9 DBD classes; permutation test against 1,000 random size-matched networks.

## Results

- PADIT-seq detects hundreds of new lower-affinity binding sites per TF (e.g. 1,780 active 8-mers HOXD13; 554 EGR1 10-mers), agreeing with uPBM E-scores (AUROC > 0.97) and MITOMI Kd (Pearson 0.94) while extending into the lower-affinity regime that HT-SELEX cycle scoring misses.
- ChIP-seq/ChIP-nexus peaks of all six TFs are enriched for multiple consecutive overlapping active k-mers (e.g. HOXD13 peaks with 6 consecutive active 8-mers, n=8,122).
- Sum of PADIT-seq activity at overlapping k-mers correlates with ChIP-seq signal at Pearson r=0.29-0.50, outperforming high-affinity-only summaries.
- ChIP-nexus footprints grow by exactly 1 bp per additional overlapping active 8-mer (Cbf1: 28→29→30 bp; Pho4: 27→28 bp) with one extra significant 5' cut per strand — the unique signature of independent TF–DNA contact.
- Re-analysing HT-SELEX and uPBM signal shows that overlapping active k-mers explain progressive enrichment across SELEX cycles and linear signal scaling on uPBM probes.
- Differential count of overlapping Pho4 vs Cbf1 active 8-mers predicts BET-seq ΔΔΔG at Pearson r=0.796; differential summed PADIT-seq activity raises this to r=0.948 (r²=0.898), explaining ~50% of the residual PWM variance.
- Genomic context PBMs and in vivo ChIP-seq confirm: more Pho4-specific overlapping sites → Pho4 displaces Cbf1, and vice versa.
- PADIT-seq scoring predicts allelic TF binding at AUROC 0.943 (HOXD13) / 0.962 (EGR1), beating MotifBreakR (0.790 / 0.872) and SNP-SELEX PBS.
- Variant effect magnitude scales with the number of overlapping active k-mers altered. The pathogenic SNP rs606231230 (preaxial polydactyly) creates multiple overlapping HOXD13 binding sites in a limb-specific enhancer.
- Allele-specific ChIP-seq concordance with PADIT-seq predictions: 91%. MPRA confirms that PADIT-seq-flagged variants alter expression.
- TFBS weavability is general: 199/200 UniPROBE TFs across 9 DBD families show > 80% nodes in the largest (k-1)-overlap component (permutation P<0.001).

## All claims (exhaustive)

- `[c01]` PADIT-seq detects hundreds of lower-affinity TFBSs that uPBM and HT-SELEX miss (p.1-2, Fig.1) — "we developed protein affinity to DNA by in vitro transcription and RNA sequencing (PADIT-seq), with which we comprehensively assayed the binding preferences of six TFs to all possible ten-base-pair DNA sequences, detecting hundreds of novel, lower-affinity binding sites" — confidence: high — type: methodological — links: [[concepts/padit-seq]] [[foundations/upbm-protein-binding-microarray]] [[foundations/ht-selex]] [[claims/padit-seq-detects-lower-affinity-tfbs-undetected-by-upbm-htselex]]
- `[c02]` EGR1 PADIT-seq activities correlate with MITOMI Kd at Pearson r=0.94 (Fig.1b) — "Pearson r = 0.94" — confidence: high — type: quantitative — links: [[concepts/padit-seq]] [[foundations/egr1-tf]] [[claims/padit-seq-correlates-with-mitomi-kd-pearson-094]]
- `[c03]` uPBM E-scores predict PADIT-seq active k-mers with AUROC > 0.97 across all six TFs (Fig.1d) — "uPBM E-scores showed strong predictive power across all TFs (AUROC > 0.97), HT-SELEX enrichment scores demonstrated substantially lower performance" — confidence: high — type: methodological — links: [[foundations/upbm-protein-binding-microarray]] [[foundations/ht-selex]] [[claims/upbm-escore-aurocs-above-097-for-padit-seq-active-kmers]]
- `[c04]` ChIP-seq/ChIP-nexus peaks of all six TFs are enriched for multiple consecutive overlapping active k-mers (p.4-5, Fig.2b) — "Across all 6 TFs, we found that ChIP-seq and ChIP-nexus peaks were significantly enriched for having a larger number of consecutive, active k-mers" — confidence: high — type: correlational — links: [[concepts/overlapping-binding-sites-model]] [[foundations/chip-nexus]] [[claims/chip-seq-peaks-enriched-for-consecutive-overlapping-active-kmers]]
- `[c05]` Sum of overlapping PADIT-seq activities correlates with ChIP-seq signal at r=0.29-0.50 (Extended Data Fig.3b-c) — "the sum of PADIT-seq activity levels of all active k-mers within individual peaks was significantly correlated, albeit modestly, with normalized ChIP-seq and ChIP-nexus read counts (Pearson r = 0.29-0.50)" — confidence: medium — type: quantitative — links: [[concepts/overlapping-binding-sites-model]] [[claims/sum-of-overlapping-padit-activity-correlates-with-chipseq-signal]]
- `[c06]` ChIP-nexus footprint grows by 1 bp per added overlapping site (Cbf1 28→29→30, Pho4 27→28; Fig.3) — "With each additional, overlapping binding site, we observed precisely one additional cut on each strand, leading to 1-bp increments in total footprint size" — confidence: high — type: mechanistic — links: [[concepts/overlapping-binding-sites-model]] [[foundations/chip-nexus]] [[foundations/pho4-tf]] [[foundations/cbf1-tf]] [[claims/chip-nexus-footprint-grows-1bp-per-overlapping-site]]
- `[c07]` HT-SELEX cycle progression enriches sequences with more consecutive overlapping active k-mers (Extended Data Fig.8a) — "sequences containing more overlapping active k-mers became progressively more abundant across successive rounds of selection" — confidence: medium — type: methodological — links: [[foundations/ht-selex]] [[concepts/overlapping-binding-sites-model]] [[claims/htselex-cycle-progression-enriches-overlapping-active-kmers]]
- `[c08]` uPBM signal scales linearly with number of consecutive overlapping active k-mers across ~40,000 probes for all six TFs (Extended Data Fig.8b) — "uPBM signal intensities correlated linearly with the number of consecutive, overlapping active k-mers across around 40,000 60-bp probes for all 6 TFs" — confidence: medium — type: quantitative — links: [[foundations/upbm-protein-binding-microarray]] [[concepts/overlapping-binding-sites-model]] [[claims/upbm-signal-linear-with-number-of-consecutive-active-kmers]]
- `[c09]` Differential summed Pho4/Cbf1 PADIT-seq activity predicts BET-seq ΔΔΔG at r=0.948 (r²=0.898); explains ~50% of residual PWM variance (Fig.4e) — "Pearson r = 0.948; r² = 0.898 ± 0.0004 ... The overlapping binding sites model explains about 50% of the remaining variance that PWM models fail to capture" — confidence: high — type: quantitative — links: [[concepts/tf-paralogue-competition]] [[concepts/overlapping-binding-sites-model]] [[foundations/pho4-tf]] [[foundations/cbf1-tf]] [[claims/pho4-cbf1-paralog-competition-explained-by-overlapping-sites-r-0948]]
- `[c10]` In vivo Pho4/Cbf1 ChIP-seq dominance tracks paralog-specific overlapping site counts (Fig.4f) — "DNA sequences with a larger number of Pho4-specific consecutive active 8-mers showed reduced Cbf1 binding when Pho4 was present and vice versa ... in vivo, where ChIP-seq peaks containing more Pho4-specific consecutive active 8-mers showed higher Pho4 occupancy in the presence of Cbf1" — confidence: medium — type: correlational — links: [[concepts/tf-paralogue-competition]] [[claims/in-vivo-pho4-cbf1-binding-resilience-tracks-overlapping-site-counts]]
- `[c11]` PADIT-seq outperforms MotifBreakR and SNP-SELEX at predicting variant effects (AUROC 0.943/0.962 vs 0.790/0.872; Fig.5c) — "PADIT-seq outperformed existing approaches in identifying differential TF binding, achieving AUROC values of 0.943 for HOXD13 and 0.962 for EGR1" — confidence: high — type: methodological — links: [[concepts/noncoding-variant-tf-binding-effect]] [[foundations/motifbreakr]] [[foundations/snp-selex]] [[claims/padit-seq-outperforms-motifbreakr-and-snpselex-for-variant-effects]]
- `[c12]` Variant effect magnitude scales with the number of altered overlapping active k-mers (Fig.5e-g) — "the magnitude of differential binding scaled with the number of overlapping binding sites altered" — confidence: high — type: quantitative — links: [[concepts/noncoding-variant-tf-binding-effect]] [[concepts/overlapping-binding-sites-model]] [[claims/variant-effect-magnitude-scales-with-number-of-altered-overlapping-kmers]]
- `[c13]` Pathogenic SNP rs606231230 (preaxial polydactyly) creates multiple overlapping HOXD13 binding sites in a limb enhancer (Fig.5e) — "rs606231230 is pathogenic for preaxial polydactyly and occurs in a limb-specific enhancer bound by HOXD13 in the developing mouse limb bud. The risk allele creates multiple overlapping HOXD13 binding sites" — confidence: high — type: pharmacological — links: [[concepts/noncoding-variant-tf-binding-effect]] [[foundations/hoxd13-tf]] [[claims/rs606231230-pathogenic-preaxial-polydactyly-creates-overlapping-hoxd13-sites]]
- `[c14]` Allele-specific ChIP-seq concordance with PADIT-seq predictions is 91% (Extended Data Fig.9c) — "PADIT-seq identified the preferred allele with 91% concordance, substantially outperforming MotifBreakR" — confidence: high — type: methodological — links: [[concepts/noncoding-variant-tf-binding-effect]] [[claims/allele-specific-chipseq-91-percent-concordance-with-padit-seq]]
- `[c15]` MPRA confirms PADIT-seq-flagged variants impact EGR1-driven expression (Extended Data Fig.9d-f) — "variants predicted by PADIT-seq to alter binding also significantly impact gene expression" — confidence: medium — type: methodological — links: [[concepts/noncoding-variant-tf-binding-effect]] [[foundations/egr1-tf]] [[claims/mpra-confirms-padit-seq-variant-effects-on-expression]]
- `[c16]` 199/200 UniPROBE TFs have >80% of active k-mers in a single (k-1)-overlap connected component (Extended Data Fig.10i) — "For 199 out of 200 TFs, the largest connected component contained more than 80% of nodes (P < 0.001, permutation test)" — confidence: high — type: correlational — links: [[concepts/tfbs-weavability]] [[foundations/upbm-protein-binding-microarray]] [[claims/tfbs-weavability-is-general-property-of-eukaryotic-tfs]]
- `[c17]` Genomic regions with multiple consecutive overlapping active k-mers are more conserved than flanking sequence (Fig.2d) — "genomic regions containing consecutive active k-mers were significantly more conserved than flanking sequences" — confidence: medium — type: correlational — links: [[concepts/overlapping-binding-sites-model]] [[claims/conserved-overlapping-active-kmer-regions-evolutionarily-conserved]]

## Discussion captured

### Interpretation

The expanded lower-affinity repertoire revealed by PADIT-seq supports a single unifying model in which flanking nucleotides adjacent to high-affinity sites create overlapping lower-affinity sites that additively shape TF occupancy. This reframes flanking-sequence effects from "extended motif tweaks" to "discrete, independent extra binding events" and gives a single mechanism for paralog competition and noncoding-variant effects.

### Contrast with prior work

The model differs from partition-function STR-flanking-motif models (Horton 2023) and from homotypic-cluster (Crocker 2015, iMITOMI) frameworks: STRs and iMITOMI feature multiple TF molecules across spatially separated low-affinity sites, while OBS focuses on a single TF molecule across consecutive overlapping sites within < 30 bp.

### Ruling out alternative interpretations

The "partial motif recognition" alternative is ruled out by (1) custom PBMs showing low-affinity k-mers are bound independently; (2) single-site-altering variants produce significant effects in custom PBMs; and (3) ChIP-nexus footprint grows by exactly 1 bp per added overlapping site — the molecular signature of independent contacts.

### Implications

The model provides an interpretive framework for noncoding GWAS variants where MotifBreakR predicts no effect but ChIP-seq/MPRA disagree, and offers a quantitative path for engineering paralog-selective binding outcomes by tuning flanking sequences.

## Limitations

- Sensitivity depends on TF / nbALFA-T7 RNAP concentration, sequencing depth, and FDR threshold; very weak TFs may still be missed.
- Flanking nucleotides in the PADIT-seq library must pre-exclude adjoining high-E-score 8-mers; designing libraries for arbitrary TFs requires care.
- The OBS model captures the affinity component of paralog competition but not the kinetic / nuclear-translocation component.
- Demonstrated for 6 TFs in vitro and 200 in uPBM secondary analysis; prokaryotic TFs and pioneer factors untested.
- Per-peak ChIP-seq correlations remain modest (r=0.29-0.50) — chromatin/cofactor contributions are not yet integrated.

## Open questions

- Does OBS extend to prokaryotic TFs?
- Can OBS be cast in absolute thermodynamic (partition-function) form?
- Have flanking sequences at paralog-shared sites evolved under selection to encode differential overlapping-site counts?
- Can PADIT-seq affinity tables be combined with ATAC-seq + cofactor presence to predict in vivo TF occupancy de novo?
- Does TFBS weavability correlate with TF dosage robustness or cofactor dependence?

## My take

The strongest piece is the ChIP-nexus footprint result: a discrete 1-bp expansion per overlapping site is the kind of molecular signature that's nearly impossible to fake with extended-motif or partial-recognition models, and it directly anchors the additive interpretation. The variant-effect arc (rs606231230 → multiple overlapping HOXD13 sites in a limb enhancer) is a clean clinical translation. Where I'd push back: ChIP-seq correlations of 0.29-0.50 are modest, the model is silent on cofactors/chromatin, and the BET-seq r²=0.898 is partly a re-analysis of an existing landscape engineered for this kind of question — so the "50% of residual PWM variance" framing should be read as "in this controlled landscape", not as a global claim. Most useful for thesis-adjacent work: this gives a defensible framework for re-interpreting noncoding GWAS hits whose PWM-based predictors fail, and a vocabulary (weavability, overlapping site counts) that translates the lower-affinity-developmental-enhancer literature into a quantitative scoring scheme.

## Related

- [[concepts/padit-seq]] — method introduced here
- [[concepts/overlapping-binding-sites-model]] — central model proposed here
- [[concepts/low-affinity-tf-binding-site]] — established concept refined here
- [[concepts/tfbs-weavability]] — new structural property described here
- [[concepts/tf-paralogue-competition]] — long-standing question answered quantitatively here
- [[concepts/noncoding-variant-tf-binding-effect]] — variant-effect framework introduced here
- [[foundations/hoxd13-tf]], [[foundations/egr1-tf]], [[foundations/nkx2-5-tf]], [[foundations/tbx5-tf]], [[foundations/pho4-tf]], [[foundations/cbf1-tf]] — benchmark TFs
- [[foundations/chip-nexus]], [[foundations/ht-selex]], [[foundations/upbm-protein-binding-microarray]], [[foundations/snp-selex]], [[foundations/motifbreakr]] — methods used
