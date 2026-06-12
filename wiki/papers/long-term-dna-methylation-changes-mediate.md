---
# === Identification ===
title: "Long-term DNA methylation changes mediate heterologous cytokine responses after BCG vaccination"
slug: long-term-dna-methylation-changes-mediate
arxiv: ""
doi: "10.1186/s13059-025-03611-9"
pmid: "40629459"
venue: "Genome Biology"
year: 2025
authors: ["Cancan Qi", "Zhaoli Liu", "Gizem Kilic", "Andrei S. Sarlea", "Priya A. Debisarun", "Xuan Liu", "Yonatan Ayalew Mekonnen", "Wenchao Li", "Martin Grasshoff", "Ahmed Alaswad", "Apostolos Petkoglou", "Valerie A. C. M. Koeken", "Simone J. C. F. M. Moorlag", "L. Charlotte J. de Bree", "Vera P. Mourits", "Leo A. B. Joosten", "Yang Li", "Mihai G. Netea", "Cheng-Jian Xu"]
first_author: "Cancan Qi"
corresponding_author: "Cheng-Jian Xu"

# === Source & metadata ===
source_type: pdf
s2_id: "d17303f54b814632857930a657995ff12ddbb7cf"
date_added: 2026-06-12
ingested_date: 2026-06-12
ingest_version: 1
last_reviewed:

# === Classification ===
importance: 4
tier: TIER_1
tags: [trained-immunity, dna-methylation, bcg, ewas, cytokine, ifn-gamma, epigenetic-memory, systems-immunology, sex-differences, mediation]
keywords: ["BCG vaccination", "DNA methylation", "trained immunity", "heterologous cytokine response", "EWAS", "kisspeptin", "mediation analysis"]
domain: epigenetics

# === Biomedical domain ===
tissue: [blood]
condition: [healthy]
disease_specific: []
species: [human]
hypoxia_relevant: false
contains_immune_cells: true
contains_myeloid: true

# === Technique ===
techniques: [EPIC_array, flow_cytometry, ELISA, genotyping_array, olink_proteomics, metabolomics]
n_samples: 284
n_cells_total:
integration_method: ""

# === Biology captured ===
key_cell_types: [monocytes, T_cells, neutrophils, PBMCs]
key_markers: [IFN-gamma, IL-1beta, IL-6, TNF-alpha, KISS1, SLC12A3, GSDMC, MC3R, PLD2]
key_pathways: [trained-immunity, kisspeptin-receptor-system, mTOR-signaling, VEGFA-VEGFR2, GnRH-secretion, TLR-signaling]

# === User project membership ===
projects: [thesis]
priority: reference
read_status: not_read

# === HypoxiaVERSE-specific ===
hypoxiaverse_status:
exclusion_reason:
data_availability: "EGA: EGAS00001007498"

# === Cross-references ===
code_url: "https://github.com/CiiM-Bioinformatics-group/BCG_methylation_project"
cited_by: []
---

## Problem

Epigenetic reprogramming underlies BCG-induced trained immunity, but most evidence concerns histone modifications. Whether dynamic **DNA methylation** changes encode innate immune memory and shape post-vaccination heterologous cytokine responses in adults — and how genetics and sex modify this — was unresolved.

## Key idea

In a longitudinal cohort of healthy adults (300BCG), profile genome-wide whole-blood DNA methylation (EPIC array) and ex vivo cytokine responses at baseline (T0), 14 days (T14), and 90 days (T90) after BCG vaccination, then integrate genetic, epigenetic, protein, metabolite, and cytokine layers to: (1) map short- and long-term methylation dynamics, (2) test whether baseline and BCG-induced methylation predict/associate with trained-immunity cytokine responses, (3) infer causal ordering via mediation, and (4) dissect sex specificity. A candidate pathway (kisspeptin) is functionally validated.

## Method

- Cohort: 303 vaccinated healthy Dutch adults, 284 after QC (126 M / 158 F, mean age 25, 86.3% <30). Standard 0.1 mL intradermal BCG-Bulgaria.
- Methylation: Infinium MethylationEPIC array; preprocessed with [[foundations/minfi-methylation-array-preprocessing]]; cross-reactive/polymorphic/sex-chromosome probes removed; 751,564 probes; M-values modeled. Cell proportions via [[foundations/houseman-methylation-cell-composition-deconvolution]] (and [[foundations/epidish-cell-type-deconvolution-methylation]] for 12-type sensitivity).
- EWAS ([[foundations/epigenome-wide-association-study-ewas]]): linear mixed-effects models over timepoints (subject random effect; age, sex, plate, cell counts covariates); FDR<0.05 significant, P<1e-5 suggestive.
- Cytokines: PBMCs stimulated with heat-killed [[foundations/staphylococcus-aureus]]; TNF-α/IL-6/IL-1β at 24 h, IFN-γ at 7 days by ELISA; trained-immunity = fold change T90/T0.
- Annotation/enrichment: [[foundations/great-cis-regulatory-region-annotation]], [[foundations/consensuspathdb-cpdb-pathway-enrichment]], [[foundations/eforge-epigenomic-element-overlap-enrichment]] (chromatin state).
- Integration: variance partition across omics ([[foundations/polygenic-risk-score]], proteins, metabolites, methylation); cytokine-QTL and SNP–methylation via [[foundations/matrix-eqtl]]; bidirectional [[foundations/causal-mediation-analysis]].
- Validation: independent BCG booster replication cohort (n=17); in vitro [[foundations/kisspeptin-kiss1-gpr54-system]] (KP-10) functional assay.

## Results

- **11 CpGs** significantly changed over 90 days (FDR<0.05; 5 up, 6 down); 8/11 reverse direction between T14 and T90.
- Short-term (T14) changes revert by T90 (recovery phase); long-term (T90) changes persist, enriched in infection pathways — a delayed **"late" epigenetic effect** that opposes aging-associated hypermethylation.
- BCG CpGs correlate strongly with **neutrophil** proportion (strongest at T90).
- **41 baseline CpGs** associate with TI(IFN-γ) (strongest cg16685860 near PLD2); baseline methylation explains the **largest variance** of TI(IFN-γ) (combined model R²≈56.1%).
- **Kisspeptin receptor system** is the top-enriched pathway; **KP-10 functionally inhibits IFN-γ** production (selective; IL-17/IL-22 unaffected).
- Long-term (T90–T0) methylation changes associate with cytokine changes (IFN-γ N=28, IL-1β N=14).
- **Bidirectional mediation** infers methylation mediates SNP→cytokine effects (e.g. SLC12A3 cg21375332: 32.7% of rs604639→IFN-γ; GSDMC cg25926804: 28.6% of rs6991078→IFN-γ).
- Strong **sex specificity**: non-overlapping CpGs, divergent pathways (female hormone/GnRH, male nervous/infection), and far more baseline associations in males; female IFN-γ CpGs correlate with cortisol.

## All claims (exhaustive)

- `[c1]` BCG induces 11 genome-wide significant CpG changes over 90 days (5 up, 6 down) (p.3-4) "we identified 11 CpG sites that were significantly (false discovery rate (FDR) < 0.05) changed following BCG vaccination" — confidence: high — type: quantitative — links: [[concepts/dna-methylation-substrate-trained-immunity-epigenetic]] [[foundations/epigenome-wide-association-study-ewas]] [[foundations/illumina-methylationepic-array]] [[claims/bcg-vaccination-induces-11-genome-wide]]
- `[c2]` Short-term (T14) changes reverse during a T14–T90 recovery phase (p.7) "the later time period, from T14 to T90, might represent a recovery phase following BCG vaccination" — confidence: medium — type: mechanistic — links: [[concepts/biphasic-short-term-reversible-long-term]] [[foundations/eforge-epigenomic-element-overlap-enrichment]] [[claims/short-term-t14-bcg-methylation-changes]]
- `[c3]` Long-term (T90) changes reflect lasting epigenetic memory enriched in infection pathways (p.7) "The long-term effect of BCG vaccination on epigenetics at 90 days post-vaccination reflects a lasting epigenetic memory" — confidence: medium — type: mechanistic — links: [[concepts/dna-methylation-substrate-trained-immunity-epigenetic]] [[concepts/biphasic-short-term-reversible-long-term]] [[claims/long-term-t90-bcg-methylation-changes]]
- `[c4]` A "late" epigenetic effect develops mostly after day 14 (p.7) "the majority of the increased CpG sites (64.7%) first slightly decreased at T14 and then increased at T90" — confidence: medium — type: mechanistic — links: [[concepts/biphasic-short-term-reversible-long-term]] [[claims/late-epigenetic-reprogramming-after-bcg-occurs]]
- `[c5]` The late BCG effect opposes natural-aging methylation direction (p.17-18) "the 'late' effect of BCG vaccination opposes the DNA methylation changes associated with natural aging" — confidence: low — type: mechanistic — links: [[concepts/biphasic-short-term-reversible-long-term]] [[claims/bcg-late-epigenetic-effect-opposes-natural]]
- `[c6]` BCG-associated CpGs correlate strongly with neutrophil proportion (p.5) "strong correlations were observed between the CpG sites and estimated neutrophil proportion, with T90 showing the strongest associations" — confidence: high — type: correlational — links: [[foundations/houseman-methylation-cell-composition-deconvolution]] [[claims/bcg-associated-cpg-methylation-correlates-neutrophil]]
- `[c7]` Short-term changes associate with reduced circulating inflammatory proteins (CD6, OPG) (p.8-9) "the DNA methylation changes in four CpG sites identified from T14 vs T0 comparison were significantly associated with alterations in two proteins" — confidence: medium — type: correlational — links: [[foundations/il-6-cytokine]] [[claims/short-term-bcg-methylation-changes-associate]]
- `[c8]` 41 baseline CpGs associate with TI(IFN-γ); strongest cg16685860 near PLD2 (p.9) "41 CpG sites at baseline were significantly associated with the increased IFN-γ production capacity at T90 compared to T0" — confidence: high — type: quantitative — links: [[concepts/baseline-dna-methylation-predicts-heterologous-trained]] [[foundations/ifn-gamma-cytokine]] [[claims/baseline-dna-methylation-41-cpg-sites]]
- `[c9]` Baseline methylation explains largest variance of TI(IFN-γ); combined model 56.1% (p.10) "baseline DNA methylation explained the largest proportion of variance of TI (IFN-γ)... A combined model of all data layers explained 56.1% variance" — confidence: high — type: quantitative — links: [[concepts/baseline-dna-methylation-predicts-heterologous-trained]] [[foundations/polygenic-risk-score]] [[claims/baseline-dna-methylation-explains-largest-variance]]
- `[c10]` Baseline methylation predicts IFN-γ but not IL-1β/TNF-α TI (only one CpG for IL-6) (p.9) "We did not find any significant associations between baseline DNA methylation and TI (IL-1β) or TI (TNF-α), except for one CpG site... TI (IL-6)" — confidence: high — type: correlational — links: [[concepts/baseline-dna-methylation-predicts-heterologous-trained]] [[claims/baseline-methylation-predicts-ifn-gamma-il]]
- `[c11]` Kisspeptin receptor system is the top-enriched pathway among baseline IFN-γ CpGs (p.11) "the kisspeptin receptor system pathway showed the strongest enrichment, with the lowest P value and the largest number of enriched genes" — confidence: medium — type: methodological — links: [[concepts/kisspeptin-kiss1-immunomodulation-ifn-gamma-production]] [[foundations/consensuspathdb-cpdb-pathway-enrichment]] [[claims/kisspeptin-receptor-pathway-top-enriched-among]]
- `[c12]` Recombinant KP-10 selectively inhibits IFN-γ production in PBMCs (p.11) "Kisspeptin significantly inhibited IFN-γ production capacity, validating its immunomodulatory role... no effects on IL-17 and IL-22" — confidence: high — type: pharmacological — links: [[concepts/kisspeptin-kiss1-immunomodulation-ifn-gamma-production]] [[foundations/kisspeptin-kiss1-gpr54-system]] [[foundations/ifn-gamma-cytokine]] [[claims/recombinant-kisspeptin-10-inhibits-ifn-gamma]]
- `[c13]` Long-term (T90–T0) changes associate with cytokine production changes for all four cytokines (p.11) "T90–T0 DNAm-C showed a significant association with trained immunity for all four traits... IFN-γ N = 28, IL-1β N = 14" — confidence: high — type: quantitative — links: [[concepts/dna-methylation-substrate-trained-immunity-epigenetic]] [[foundations/il-1-beta-cytokine]] [[claims/long-term-bcg-methylation-changes-associate]]
- `[c14]` Long-term, not short-term/recovery, changes underlie trained-immunity memory (p.12) "the BCG-induced long-term DNA methylation changes, rather than those observed during the vaccine phase... may play a more important role in the trained immunity response" — confidence: medium — type: mechanistic — links: [[concepts/dna-methylation-substrate-trained-immunity-epigenetic]] [[claims/long-term-short-term-methylation-changes]]
- `[c15]` IFN-γ TI methylation changes enriched in mTOR and VEGFA-VEGFR2 pathways (p.11-12) "changes in IFN-γ heterologous production were enriched in changes in DNA methylation of genes involved in the mTOR signaling pathway... the VEGFA-VEFGR2 signaling pathway" — confidence: medium — type: correlational — links: [[foundations/mtor-kinase]] [[foundations/vegf]] [[claims/ifn-gamma-trained-immunity-methylation-changes]]
- `[c16]` Methylation changes mediate SNP effects on cytokine changes (in silico) (p.12-13) "mediation analysis demonstrated that most of the identified DNA methylation changes played a mediating role between genetic variants and cytokine responses" — confidence: medium — type: mechanistic — links: [[concepts/dna-methylation-mediates-genetic-variant-effects]] [[foundations/causal-mediation-analysis]] [[foundations/matrix-eqtl]] [[claims/dna-methylation-changes-mediate-genetic-variant]]
- `[c17]` cg21375332 near SLC12A3 mediates 32.7% of rs604639→IFN-γ (p.13) "cg21375332 (near SLC12 A3 and NUP93) mediated 32.7% of the effect of rs604639 on IFN-γ changes" — confidence: medium — type: quantitative — links: [[concepts/dna-methylation-mediates-genetic-variant-effects]] [[foundations/slc12a3-ncc-sodium-chloride-cotransporter]] [[foundations/il-18-cytokine]] [[claims/cg21375332-near-slc12a3-mediates-genetic-effect]]
- `[c18]` cg25926804 near GSDMC mediates 28.6% of rs6991078→TI(IFN-γ) (p.13) "cg25926804, located near the TMEM75 and GSDMC gene, mediated 28.6% of the effect of rs6991078 on TI (IFN-γ)" — confidence: medium — type: quantitative — links: [[concepts/dna-methylation-mediates-genetic-variant-effects]] [[foundations/gsdmc-gasdermin]] [[claims/cg25926804-near-gsdmc-mediates-genetic-effect]]
- `[c19]` BCG methylation changes are sex-specific and non-overlapping (p.14) "there were suggestive significant short-term changes in 18 CpG sites among males and 31 CpG sites among females... without any overlap" — confidence: medium — type: correlational — links: [[concepts/sex-specific-epigenetic-cytokine-effects-bcg]] [[claims/bcg-induced-dna-methylation-changes-sex]]
- `[c20]` Sex-specific pathway enrichment (female hormone/GnRH, male nervous/infection/TLR) (p.14-15) "the short-term changes in methylation following BCG vaccination were enriched to functions related to sex hormones in females and the nervous system in males, while the long-term changes were associated with pathways related to pathogenic immune responses in males" — confidence: medium — type: correlational — links: [[concepts/sex-specific-epigenetic-cytokine-effects-bcg]] [[claims/sex-specific-pathway-enrichment-bcg-methylation]]
- `[c21]` Baseline methylation–TI associations stronger in males (3579 vs 584 CpGs for IFN-γ) (p.16) "we identified 3579 CpG sites at baseline that were significantly associated with TI (IFN-γ) males, whereas only 584 sites showed significant association in females, without any overlap" — confidence: medium — type: quantitative — links: [[concepts/sex-specific-epigenetic-cytokine-effects-bcg]] [[claims/baseline-methylation-trained-immunity-associations-stronger]]
- `[c22]` Female IFN-γ CpGs correlate with cortisol; male sites do not (p.16) "10 CpG sites associated with TI (IFN-γ) in females were strongly associated with cortisol... for the sites identified in males, we did not identify any significant links with sex hormones" — confidence: medium — type: correlational — links: [[concepts/sex-specific-epigenetic-cytokine-effects-bcg]] [[claims/female-ifn-gamma-associated-cpg-sites]]
- `[c23]` Findings partially replicate in an independent BCG booster cohort (n=17) (p.8,16) "Among these, 21 CpG sites showed the same direction, and two out of the 21 CpG sites showed nominal significance" — confidence: low — type: methodological — links: [[concepts/baseline-dna-methylation-predicts-heterologous-trained]] [[claims/bcg-methylation-findings-replicate-independent-booster]]
- `[c24]` Findings apply primarily to young adults (<30) (p.8) "These findings suggest that the results of this study are most applicable to young adults" — confidence: medium — type: correlational — links: [[claims/bcg-methylation-findings-apply-primarily-young]]

## Discussion captured

### Authors' interpretation

The authors interpret persistent (T90) DNA methylation changes as a form of epigenetic memory partly underlying BCG-induced innate immune memory, complementing histone-based mechanisms. They argue epigenetic memory reflects a combination of innate training and heterologous adaptive (T-cell) memory, with crosstalk between innate and adaptive compartments important for trained-immunity development. Baseline methylation is framed as an intrinsic determinant of individual differences in long-term vaccine-induced immune effects, supporting personalized/epigenetic-based interventions.

### Comparisons with prior literature (made by authors)

- Histone-focused trained-immunity epigenetics (refs 41, 42 — Quintin 2012; Saeed 2014) contrasted with this DNA-methylation focus.
- Neonatal-monocyte BCG methylation signature (ref 20 — Bannister, Sci Adv 2022) and prior adult methylation suggestion (ref 22 — Verma 2017) positioned as motivation; this study fills the adult comprehensive gap.
- SLC12A3/IL-18→IFN-γ link (ref 38); GSDMC antimicrobial pyroptosis (refs 36, 37); mTOR in trained immunity/T-cell activation (refs 33, 34); kisspeptin immunomodulation (refs 30, 47, 48).
- Sex-dimorphic BCG clinical effects (refs 50, 51 — Stensballe; Biering-Sørensen) and prior sex-dependent BCG inflammatory-protein changes (ref 9 — Koeken JCI 2020).

### Mechanistic hypotheses proposed

- Long-term DNA methylation acts as a modulator relaying genetic-variant effects onto cytokine production (mediation).
- Kisspeptin (via *KISS1* methylation) tunes IFN-γ production; "DNA methylation of KISS1 likely impacts interferon production" (p.11).
- Innate–adaptive crosstalk (IFN-γ amplifying trained immunity) operates at the epigenetic level.

### Caveats and self-criticism

Authors caution that cell-type-driven signals require careful interpretation (some CpGs lose significance after 12-cell-type adjustment), sex analyses lack genome-wide significance and male external validation, and the absence of a non-vaccinated control limits causal attribution to BCG-induced trained immunity.

### Future directions suggested

Functional/molecular studies of mediating CpGs; transcriptional readouts of affected genes; validation in larger, older, and more diverse cohorts; exploration of neuro-immune/hormonal crosstalk.

## Limitations

- Whole-blood methylation masks cell-type-specific changes.
- EPIC array covers only ~3% of genomic CpGs.
- Replication cohort underpowered (n=17; few males).
- No genome-wide-significant sex-stratified CpGs; male-specific results unvalidated.
- No transcriptional (expression) confirmation of affected genes.
- Associations/mediation are in silico; no functional mechanism beyond kisspeptin.
- Young-adult population limits generalizability.
- No non-vaccinated control group.

## Open questions

### Open questions raised by authors

- What molecular machinery drives the delayed "late" demethylation?
- Are mediating CpGs (SLC12A3, GSDMC, MC3R) causal for cytokine changes?
- How do sex hormones mechanistically shape sex-specific epigenetic-immune responses?
- Do these methylation changes generalize to older and non-European populations?

### Open questions identified during ingest

- Is methylation memory cell-intrinsic (within trained cells across divisions) or a composition shift (given strong neutrophil correlation)?
- How does DNA-methylation memory integrate with histone-mark memory quantitatively?
- Could baseline methylation serve as a deployable clinical predictor of vaccine responsiveness?

## My take

A strong systems-immunology demonstration that DNA methylation — not only chromatin marks — is a substrate of human trained immunity, with the standout result being baseline methylation explaining the most variance in heterologous IFN-γ responses and the functional kisspeptin validation moving beyond pure association. The heavy reliance on whole-blood, suggestive-threshold, and in silico mediation evidence tempers causal claims, but the sex-specificity and the predictive framing are the most reusable ideas. Methodologically rich (EWAS + mediation + variance partition + functional assay) — a good template for multi-omics immune-epigenetics.

## Related

- Concepts introduced: [[concepts/dna-methylation-substrate-trained-immunity-epigenetic]], [[concepts/baseline-dna-methylation-predicts-heterologous-trained]], [[concepts/biphasic-short-term-reversible-long-term]], [[concepts/kisspeptin-kiss1-immunomodulation-ifn-gamma-production]], [[concepts/dna-methylation-mediates-genetic-variant-effects]], [[concepts/sex-specific-epigenetic-cytokine-effects-bcg]]
- Foundations: [[foundations/trained-immunity]], [[foundations/bcg-vaccine-bacillus-calmette-guerin]], [[foundations/epigenome-wide-association-study-ewas]], [[foundations/illumina-methylationepic-array]], [[foundations/kisspeptin-kiss1-gpr54-system]], [[foundations/staphylococcus-aureus]], [[foundations/causal-mediation-analysis]], [[foundations/matrix-eqtl]]
- People: [[people/cancan-qi]], [[people/zhaoli-liu]], [[people/cheng-jian-xu]], [[people/yang-li]], [[people/mihai-netea]], [[people/leo-joosten]]
