---
# === Identification ===
title: "Atlas-guided discovery of transcription factors for T cell programming"
slug: atlas-guided-discovery-transcription-factors-cell
arxiv: ""
doi: "10.1038/s41586-025-09989-7"
pmid: ""
venue: "Nature"
year: 2025
authors: ["H. Kay Chung", "Cong Liu", "Anamika Battu", "Alexander N. Jambor", "Brandon M. Pratt", "Fucong Xie", "Brian P. Riesenberg", "Eduardo Casillas", "Ming Sun", "Elisa Landoni", "Yanpei Li", "Qidang Ye", "Daniel Joo", "Jarred Green", "Zaid Syed", "Nolan J. Brown", "Matthew Smith", "Shixin Ma", "Shirong Tan", "Brent Chick", "Victoria Tripple", "Z. Audrey Wang", "Jun Wang", "Bryan McDonald", "Peixiang He", "Qiyuan Yang", "Timothy Chen", "Siva Karthik Varanasi", "Michael LaPorte", "Thomas H. Mann", "Dan Chen", "Filipe Hoffmann", "Josephine Ho", "Jennifer Modliszewski", "April Williams", "Yusha Liu", "Zhen Wang", "Jieyuan Liu", "Yiming Gao", "Zhiting Hu", "Ukrae H. Cho", "Longwei Liu", "Yingxiao Wang", "Diana C. Hargreaves", "Gianpietro Dotti", "Barbara Savoldo", "Jessica E. Thaxton", "J. Justin Milner", "Susan M. Kaech", "Wei Wang"]
first_author: "H. Kay Chung"
corresponding_author: "H. Kay Chung; Susan M. Kaech; Wei Wang"

# === Source & metadata ===
source_type: pdf
s2_id: "b9a19111438e333b621481c8a1b26d28530f6654"
date_added: 2026-05-22
ingested_date: 2026-05-22
ingest_version: 1
last_reviewed:

# === Classification ===
importance: 5
tier: TIER_1
tags: [cd8-t-cells, exhaustion, tissue-resident-memory, transcription-factor, taiji, perturb-seq, immunotherapy]
keywords: [CD8 T cells, TEXterm, TRM, ZSCAN20, JDP2, KLF6, HIC1, Taiji, in vivo Perturb-seq, anti-PD1 synergy]
domain: immunology

# === Biomedical domain ===
tissue: [small_intestine, spleen, blood, multi]
condition: [cancer, healthy]
disease_specific: [melanoma, chronic_LCMV]
species: [mouse, human]
hypoxia_relevant: false
contains_immune_cells: true
contains_myeloid: false

# === Technique ===
techniques: [scRNA-seq_10x, ATAC-seq, bulk_RNA-seq, CRISPR-Cas9, in_vivo_Perturb-seq, flow_cytometry, scATAC-seq]
n_samples: 121
n_cells_total: 32468
integration_method: "Harmony"

# === Biology captured ===
key_cell_types: [naive_CD8_T, MP, TE, TEM, TCM, TRM, TEXprog, TEXeff, TEXterm]
key_markers: [PD1, TIM3, CD101, CD39, CX3CR1, SLAMF6, CD69, CD103, ITGAE, CCR7, LAG3, IFNG, TNF]
key_pathways: [TF_PageRank_activity, proteasome_catabolism, TGFbeta_response, cell_adhesion, intrinsic_apoptosis, AP-1_signalling]

# === User project membership ===
projects: [thesis]
priority: core
read_status: read

# === HypoxiaVERSE-specific ===
hypoxiaverse_status:
exclusion_reason:
data_availability: "Supplementary Tables 1–8; code in TaijiChat web interface (Supplementary Methods)"

# === Cross-references ===
code_url: ""
cited_by: []
---

## Problem

CD8+ T cells in cancer and chronic infection differentiate into highly heterogeneous states with overlapping transcriptomes — most acutely, the **protective tissue-resident memory (TRM)** and **dysfunctional terminally exhausted (TEXterm)** states share a tissue niche, multiple key TFs (BLIMP1, BHLHE40, NR4A2) and even correlated open chromatin. Identifying TFs that selectively repress TEXterm differentiation without compromising TRM formation is required to engineer durable, functional T cells for adoptive cell therapy and CAR-T applications. Standard differential-expression screens cannot resolve this overlap, and existing CRISPR screens have largely surfaced broadly active multi-state TFs.

## Key idea

Build a 9-state CD8+ T cell multi-omics atlas (RNA-seq + ATAC-seq), use the [[taiji-tf-activity-pipeline]] (personalized [[pagerank-algorithm]] on TF→target GRNs) to score TF activity per state, then classify TFs as **single-state vs multi-state** (see [[single-state-vs-multi-state-tf-classification]]) and resolve **state-specific TF networks** via [[tf-community-analysis-grn]]. Validate predictions with [[in-vivo-perturb-seq]] in parallel acute and chronic LCMV models so the same TF KO is read out for TEXterm and TRM differentiation simultaneously.

## Method

- **Atlas**: 121 samples (69 bulk RNA-seq + 52 ATAC-seq) across naive, MP, TE, TEM, TCM, [[tissue-resident-memory-cd8-t-cell-trm|TRM]], TEXprog, TEXeff, [[cd8-t-cell-exhaustion-texterm|TEXterm]] (Fig. 1c).
- **Taiji pipeline**: TF–target GRN weighted by motif-binding affinity × ATAC accessibility × expression of TF and target; PageRank yields per-state TF activity score; statistical filtering classifies single-/multi-state TFs.
- **TF community analysis**: regulatee-adjacency matrix → Leiden clustering → pathway enrichment per community per state.
- **In vivo Perturb-seq**: retroviral dual-gRNA library (4 gRNAs/target across 2 dual-gRNA vectors; 76 TF gRNAs + 4 gScramble; 19 TF genes — 12 TEXterm single-state + 7 multi-state) transduced into Cas9+ [[p14-tcr-transgenic|P14 TCR transgenic]] CD8+ T cells; adoptive transfer into chronic LCMV-Clone 13 ([[lcmv-clone13-chronic-infection-model]]; 17,257 cells) and acute LCMV-Armstrong ([[lcmv-armstrong-acute-infection-model]]; 15,211 cells); droplet scRNA-seq day 18+.
- **Functional validation**: flow cytometry of donor cells; cytokine production; viral titres; CD69+CD103+ TRM quantification; [[b16-gp33-melanoma-act-model|B16-GP33 melanoma ACT]] tumour control and anti-PD1 ICB synergy.
- **Cross-species**: scTaiji on paired scRNA-seq + scATAC-seq across 6 human tumour types plus comparative RNA across 15 tumour types; Cas9 RNP KO of `ZSCAN20` and `JDP2` in human PBMC-derived CD8+ T cells with 18-day chronic anti-CD3/CD28 stimulation.

## Results

- Taiji partitioned the 9-state atlas into 136 single-state and 173 multi-state TF genes.
- TEXterm holds 34 single-state TFs (ZSCAN20, JDP2, ZFP324, IRF8, …); TRM holds 20 single-state TFs (FOSB, KLF6, JUNB, ATF4, …); 30 multi-state TFs are shared (HIC1, GFI1, PRDM1, BHLHE40, NR4A2, …).
- TF community analysis distinguishes TRM (TGFβ, adhesion, RNA metabolism) from TEXterm (proteasome catabolism, autophagy, intrinsic apoptosis) communities even when TFs are shared.
- Proteasome activity is highest in TEXterm cells of chronic LCMV and tumour TILs; proteasome-high OT-1 cells exhibit reduced B16F10-OVA tumour control.
- Multi-state TF KOs (Hic1, Stat3, Prdm1, Ikzf3) reduce TEXterm by ~90%; single-state TF KOs (Zfp324, Zscan20, Jdp2) reduce TEXterm by 78%, 54%, 43%.
- Eight TEXterm single-state TF KOs (Zfp324, Irf8, Zfp410, Nfatc1, Zscan20, Jdp2, Arid3a, Etv5) do **not** impair TRM formation; Hic1 and Gfi1 multi-state KOs reduce both states.
- KLF6 overexpression yields 15× small-intestinal enrichment and 42× more CD69+CD103+ TRM-like cells without increasing terminal exhaustion.
- Zscan20 KO outperforms Hic1 KO in B16-GP33 tumour control; effector marker (CX3CR1, GZMB) and cytokine expression are higher.
- 19/34 mouse TEXterm single-state TFs and 22/30 multi-state TFs are conserved in human pan-cancer scTaiji.
- ZSCAN20 or JDP2 KO in human CD8+ T cells reduces LAG3/PD1/TIM3 and increases CCR7+ memory-like and polyfunctional cytokine producers.
- Zscan20 or Jdp2 KO + anti-PD1 produces synergistic tumour shrinkage and improved survival in B16-GP33.

## All claims (exhaustive)

- `[c01]` Multi-omics atlas integrates 121 RNA-seq+ATAC-seq samples across 9 CD8+ T cell states (p.3) — "we analysed assay for transposase-accessible chromatin using sequencing (ATAC-seq) and RNA sequencing (RNA-seq) datasets from 121 CD8+ T cell samples spanning nine distinct states" — confidence: high — type: methodological — links: [[concepts/taiji-tf-activity-pipeline]] [[claims/taiji-cd8-atlas-9-states-121-samples]]
- `[c02]` Taiji partitions the atlas into 136 single-state and 173 multi-state TF genes (p.3) — "This identified TF genes, of which 136 were predominantly 'single-state' TF genes ... By contrast, 173 TFs, including Tcf7 and Tbx21, were key regulators in more than one cell state" — confidence: high — type: quantitative — links: [[concepts/single-state-vs-multi-state-tf-classification]] [[claims/cd8-tf-classification-136-single-173-multi-state]]
- `[c03]` TEXterm has 34 single-state TFs, TRM has 20, with 30 shared multi-state TFs (p.3–4) — "we identified 20 and 34 TFs as single-state TFs of TRM and TEXterm cells, respectively, and 30 multi-state TFs that were active in both" — confidence: high — type: quantitative — links: [[concepts/cd8-t-cell-exhaustion-texterm]] [[concepts/tissue-resident-memory-cd8-t-cell-trm]] [[claims/texterm-vs-trm-34-and-20-single-state-tfs]]
- `[c04]` TEXterm and TRM share more TF genes than any other state pair (p.4) — "these two cell states share the most TF genes compared with other cell states (for example, Egr2, Crem and Prdm1)" — confidence: medium — type: correlational — links: [[claims/texterm-trm-share-most-tf-genes-due-to-tissue-residency]]
- `[c05]` TF community analysis links TRM-c3 to TGFβ response/adhesion and TEXterm-c3 to apoptosis (p.5) — "TRM community-3 was associated with cell adhesion and TGFβ response ... TEXterm community-3 was linked to apoptosis" — confidence: high — type: mechanistic — links: [[concepts/tf-community-analysis-grn]] [[claims/tf-community-rewiring-trm-vs-texterm]]
- `[c06]` TEXterm community-1 maps to proteasome/catabolism while TRM-c1 maps to RNA metabolism (p.5) — "Community-1 in TRM cells controlled RNA metabolism, whereas in TEXterm cells, it was tied to catabolism, proteolysis and autophagy" — confidence: high — type: mechanistic — links: [[concepts/tf-community-analysis-grn]] [[claims/tf-community-rewiring-trm-vs-texterm]]
- `[c07]` Proteasome activity is highest in TEXterm cells of chronic LCMV and mouse TILs (p.5) — "proteasome activity—measured by a validated fluorescent probe—was highest in TEXterm cells from chronic LCMV and in tumour-specific TILs" — confidence: high — type: quantitative — links: [[claims/proteasome-pathway-hallmark-texterm]]
- `[c08]` Proteasome-high OT-1 cells exhibit reduced B16F10-OVA tumour control vs proteasome-low cells (p.5) — "Proteasomehigh cells showed reduced tumour control compared with proteasomelow cells" — confidence: high — type: quantitative — links: [[claims/proteasome-pathway-hallmark-texterm]]
- `[c09]` Perturb-seq library targets 19 TF genes (12 TEXterm single-state + 7 multi-state) across 17,257 P14 CD8+ T cells (p.5–6) — "Our Perturb-seq guide RNA library targeted 19 TF genes ... analysing 17,257 cells with unique gRNA expression" — confidence: high — type: methodological — links: [[concepts/in-vivo-perturb-seq]] [[foundations/p14-tcr-transgenic]] [[foundations/lcmv-clone13-chronic-infection-model]] [[claims/perturb-seq-19-tf-chronic-lcmv-17257-cells]]
- `[c10]` KO of Hic1/Stat3/Prdm1/Ikzf3 reduces TEXterm differentiation by ~90% (p.6) — "KOs of multi-state TF genes such as Hic1, Stat3, Prdm1 and Ikzf3 (which encodes AIOLOS) resulted in a profound reduction of approximately 90% in TEXterm differentiation" — confidence: high — type: quantitative — links: [[foundations/hic1-tf]] [[foundations/prdm1-blimp1-tf]] [[foundations/aiolos-tf]] [[claims/multi-state-tf-ko-90-percent-texterm-reduction]]
- `[c11]` Zfp324, Zscan20, Jdp2 KO reduce TEXterm differentiation by 78%, 54%, 43% (p.6) — "Depletion of new TEXterm single-state TF genes—including Zfp324, Zscan20 and Jdp2—reduced TEXterm differentiation significantly, by 78%, 54% and 43%, respectively" — confidence: high — type: quantitative — links: [[foundations/zscan20-tf]] [[foundations/jdp2-tf]] [[claims/zscan20-jdp2-zfp324-ko-texterm-reduction]]
- `[c12]` Loss of Prdm1 or Stat3 expands TEXprog cells and signature; loss of Hic1/Zscan20/Zfp324/Jdp2 expands TEXeff (p.7) — "Loss of Prdm1 and Stat3 markedly increased the frequency of TEXprog cells ... whereas loss of Hic1, Zscan20, Zfp324 or Jdp2 expanded primarily the TEXeff cell population" — confidence: high — type: mechanistic — links: [[claims/prdm1-stat3-ko-expands-texprog]]
- `[c13]` Zscan20/Jdp2 KO increase IFNγ+TNF+ production and reduce LCMV-Cl13 viral titres (p.7) — "Deletion of the Zscan20 and Jdp2 significantly enhanced effector cytokine production ... and reduced viral loads in recipient mice" — confidence: high — type: mechanistic — links: [[foundations/zscan20-tf]] [[foundations/jdp2-tf]] [[claims/zscan20-jdp2-ko-improves-cytokine-and-viral-load]]
- `[c14]` Eight TEXterm single-state TF KOs do not impair TRM formation in acute LCMV (p.8) — "none of the eight TEXterm single-state TF gene KOs (Zfp324, Irf8, Zfp410, Nfatc1, Zscan20, Jdp2, Arid3a and Etv5) negatively affected TRM formation significantly" — confidence: high — type: mechanistic — links: [[concepts/tissue-resident-memory-cd8-t-cell-trm]] [[concepts/single-state-vs-multi-state-tf-classification]] [[claims/texterm-single-state-tf-ko-spares-trm]]
- `[c15]` Hic1 and Gfi1 KO reduce TRM cell frequency and TRM signature, like Prdm1 (p.8) — "Disruption of these multi-state TFs significantly reduced TRM cell frequency and TRM-signature gene expression ... mirroring the effects of disruption of Prdm1" — confidence: high — type: mechanistic — links: [[foundations/hic1-tf]] [[foundations/gfi1-tf]] [[foundations/prdm1-blimp1-tf]] [[claims/hic1-gfi1-ko-reduces-both-trm-and-texterm]]
- `[c16]` KLF6 overexpression yields ~15× small-intestinal enrichment and ~42× more CD69+CD103+ TRM-like cells (p.8) — "Klf6-OE cells robustly outcompeted control cells, resulting in 15-fold enrichment in the small intestine ... around 42 times more CD69+CD103+ double-positive TRM-like cells" — confidence: high — type: quantitative — links: [[foundations/klf6-tf]] [[claims/klf6-overexpression-15x-trm-enrichment]]
- `[c17]` Zscan20 KO yields better B16-GP33 tumour control than Hic1 KO (p.8–9) — "depleting the TEXterm single-state TF gene Zscan20 resulted in improved tumour control [...] Zscan20 KO robustly enhanced effector marker expression (CX3CR1), granzyme B and cytokine production in TILs, whereas Hic1 KO did not seem to improve effector function to the same degree" — confidence: high — type: pharmacological — links: [[foundations/zscan20-tf]] [[foundations/hic1-tf]] [[foundations/b16-gp33-melanoma-act-model]] [[claims/zscan20-ko-better-tumour-control-than-hic1]]
- `[c18]` 19/34 mouse TEXterm single-state TFs and 22/30 multi-state TFs are conserved in human (p.9) — "Of 34 mouse TEXterm single-state TF genes, 19 showed conserved activity patterns in human TEXterm cells ... 22 of the 30 mouse TF genes that were active in both TEXterm and TRM states showed similar activity profiles in human datasets" — confidence: high — type: quantitative — links: [[claims/cross-species-conservation-19-of-34-texterm-tfs]]
- `[c19]` ZSCAN20/JDP2 KO in human CD8+ T cells reduces inhibitory receptors and increases polyfunctional cytokines (p.9–10) — "ZSCAN20- or JDP2-deficient CD8+ T cells exhibited increased expression of CCR7 ... and decreased levels of inhibitory receptors, including LAG3, PD1 and TIM3 ... These KO cells also produced higher levels of effector cytokines" — confidence: high — type: mechanistic — links: [[foundations/zscan20-tf]] [[foundations/jdp2-tf]] [[claims/zscan20-jdp2-ko-human-cd8-functional-rescue]]
- `[c20]` Zscan20 or Jdp2 KO synergizes with anti-PD1 to reduce B16-GP33 tumour burden and improve survival (p.10) — "The combination of Zscan20 or Jdp2-KO with anti-PD1 therapy significantly reduced tumour burden and improved survival" — confidence: high — type: pharmacological — links: [[foundations/zscan20-tf]] [[foundations/jdp2-tf]] [[foundations/b16-gp33-melanoma-act-model]] [[claims/zscan20-jdp2-ko-synergizes-anti-pd1-b16]]

## Discussion captured

### Authors' interpretation

Authors argue the platform delivers context-specific "TF fingerprints": TFs that drive distinct CD8+ T cell states can be pinpointed with PageRank even when transcriptomes overlap, because the regulatory **wiring** differs even when the **roster** does not. They frame TEXterm single-state TF KOs as the key actionable category for T-cell engineering — they "decouple exhaustion from protection". The proteasome-catabolism community emerges as a previously unrecognized functional hallmark of TEXterm cells consistent with prior protein-homeostasis work.

### Comparisons with prior literature (made by authors)

- Compares with recent CRISPR screens (Pritykin/Doench/Lacar et al.; refs 40–43, 56, 57) that identified broadly active TFs (cJUN, BATF/BATF3, TFAP4) and argues their pipeline surfaces state-selective TFs that those screens missed.
- Connects findings to BLIMP1 (refs 5,20–22), BHLHE40 (refs 23,24), NR4A2 (refs 9,25,26), Eomes (refs 36,37) and the Hic1/Gfi1 literature (refs 38, 39).
- Frames proteasome activity in TEXterm as consistent with published protein-homeostasis work (refs 45, 58, 59).

### Mechanistic hypotheses proposed

- "Although multi-state TFs shaped overall community topology, single-state TFs drove unique interaction patterns specific to TRM or TEXterm cells within each community" (p.5) — single-state TFs are wire-changers, not roster-changers.
- Sorted proteasome-high vs proteasome-low OT-1 tumour control supports a causal role for proteasome catabolism in dysfunction (p.5).
- "Differences in their ability to promote functional effector-like states may underlie the differential tumour control observed" (p.9) between Zscan20 and Hic1 KO.

### Caveats and self-criticism

- Authors note "there is no absolute threshold for defining cell state specificity, and some misclassification is expected" — explicitly cite Eomes being called TEXterm single-state despite known TEM/TCM/TRM functions (p.3).
- ZSCAN20 cannot be Taiji-scored because of a missing DNA-binding motif; relevance is supported by comparative expression only (p.10).

### Future directions suggested

- Combine enforced expression of TRM-promoting TFs (KLF6) with targeted depletion of TEXterm TFs into "TF recipes" for cell therapy.
- Refine TF recipes with AI models.
- Generalize the single-state vs multi-state framework beyond CD8+ T cells.
- TaijiChat web interface enables natural-language queries over the dataset (Supplementary Methods).

## Limitations

- Mouse-derived screens; human extension is limited to in vitro CD3/CD28 chronic stimulation and cross-species TF activity correlation — no human in vivo validation.
- TFs without curated motifs (e.g. ZSCAN20) cannot be scored by Taiji and rely on RNA evidence alone.
- The 9-state classification is bulk-defined; finer states within TEXterm or within TRM-Itgaelow may exist but are not resolved.
- TF community pathway enrichments depend on Leiden parameters and gene-set choice.
- Statistical thresholds for single- vs multi-state classification are arbitrary; misclassification near borders.
- No CAR-T or TIL clinical validation; tumour models are syngeneic B16-GP33 and MCA-205 only.

## Open questions

### Open questions raised by authors

- Which combinatorial TF KO + enforced-expression recipes yield the most durable anti-tumour T cells?
- How do TF recipes generalize to CAR-T and TIL platforms?
- Can the same atlas-guided strategy uncover state-selective TFs in CD4+ T cells, NK cells, or myeloid lineages?

### Open questions identified during ingest

- Do TEXterm single-state TFs identified in viral models behave identically in TILs across diverse human cancers (especially hypoxic tumours)?
- How does ZSCAN20 KO interact with HIF1α/HIF2α-driven exhaustion programmes in hypoxic tumour microenvironments?
- Is the proteasome-catabolism community a tractable pharmacological target (bortezomib analogues) in TIL therapy?

## My take

This sets a strong template for "atlas + multi-omics TF activity + in vivo Perturb-seq" pipelines. The single-state vs multi-state framing is the operational insight: it converts dense TF lists into actionable engineering targets and avoids the trap of CRISPR screens that surface only broadly active regulators. For my thesis, the relevant connection is that the proteasome catabolism axis and TGFβ axis they expose are also touchpoints in hypoxic TIL dysfunction — KLF6-OE plus ZSCAN20 KO is a candidate "exhaustion-resistant TIL" recipe worth tracking. The cross-species partial conservation (~56% of TEXterm single-state TFs) is a useful realism check before assuming mouse → human translation.

## Related

- [[concepts/cd8-t-cell-exhaustion-texterm]]
- [[concepts/tissue-resident-memory-cd8-t-cell-trm]]
- [[concepts/taiji-tf-activity-pipeline]]
- [[concepts/in-vivo-perturb-seq]]
- [[concepts/single-state-vs-multi-state-tf-classification]]
- [[concepts/tf-community-analysis-grn]]
- [[foundations/zscan20-tf]]
- [[foundations/jdp2-tf]]
- [[foundations/klf6-tf]]
- [[foundations/hic1-tf]]
- [[foundations/gfi1-tf]]
- [[foundations/prdm1-blimp1-tf]]
- [[foundations/aiolos-tf]]
- [[foundations/pagerank-algorithm]]
- [[foundations/p14-tcr-transgenic]]
- [[foundations/lcmv-clone13-chronic-infection-model]]
- [[foundations/lcmv-armstrong-acute-infection-model]]
- [[foundations/b16-gp33-melanoma-act-model]]
- [[foundations/scrna-seq-10x-chromium]]
- [[foundations/atac-seq]]
- [[people/h-kay-chung]]
- [[people/cong-liu]]
- [[people/susan-m-kaech]]
- [[people/wei-wang-ucsd]]
