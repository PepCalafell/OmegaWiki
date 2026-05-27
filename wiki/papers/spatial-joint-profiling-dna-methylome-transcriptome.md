---
# === Identification ===
title: "Spatial joint profiling of DNA methylome and transcriptome in tissues"
slug: spatial-joint-profiling-dna-methylome-transcriptome
arxiv: ""
doi: "10.1038/s41586-025-09478-x"
pmid: "40903587"
venue: "Nature"
year: 2025
authors:
  - "Chin Nien Lee"
  - "Hongxiang Fu"
  - "Angelysia Cardilla"
  - "Wanding Zhou"
  - "Yanxiang Deng"
first_author: "Chin Nien Lee"
corresponding_author: "Chin Nien Lee; Wanding Zhou; Yanxiang Deng"

# === Source & metadata ===
source_type: pdf
s2_id: "3f8258f762b0e7d9245fd7c81f53d841991278c7"
date_added: 2026-05-27
ingested_date: 2026-05-27
ingest_version: 1
last_reviewed: null

# === Classification ===
importance: 4
tier: TIER_1
tags:
  - spatial-omics
  - spatial-multi-omics
  - DNA-methylation
  - methylome
  - transcriptome
  - spatial-DMT
  - EM-seq
  - DBiT-seq
  - WNN
  - mouse-embryo
  - postnatal-brain
  - mCH
  - mCA
  - VMR
  - PMD
  - oligodendrogenesis
  - epigenetic-priming
  - methods-development
keywords:
  - spatial DNA methylome
  - spatial methylation transcriptome co-profiling
  - spatial-DMT
  - whole-genome spatial methylation
  - EM-seq tissue methylation
  - DBiT-seq spatial barcoding
  - WNN multimodal integration
  - mouse embryogenesis methylome
  - postnatal brain mCA
  - partially methylated domains mitotic clock
  - VMR positive expression coupling
  - oligodendrogenesis spatial pseudotime
domain: "spatial omics / epigenetics / developmental biology / methods"

# === Biomedical domain ===
tissue:
  - in_vitro_only
condition:
  - healthy
disease_specific: []
species:
  - mouse
hypoxia_relevant: false
contains_immune_cells: false
contains_myeloid: false

# === Technique ===
techniques:
  - spatial_DBiT-seq
  - EM-seq
  - scRNA-seq_10x
  - Tn5_tagmentation
  - WNN_Seurat_v4
  - HOMER_motif_analysis
  - UMAP
n_samples: 5
n_cells_total: null
integration_method: "WNN (Seurat v4, Hao 2021)"

# === Biology captured ===
key_cell_types:
  - oligodendrocyte_progenitor
  - premature_oligodendrocyte
  - telencephalon_progenitor
  - GABAergic_cortical_interneuron
  - olfactory_sensory_neuron
  - cortical_excitatory_neuron_TEGLU
  - DG_granule_neuron_DGGRC2
  - hippocampal_CA1_CA2_CA3_neuron
  - fibrous_astrocyte
  - embryonic_cardiomyocyte
key_markers:
  - Runx2
  - Mapt
  - Trim55
  - Ank3
  - Atp11c
  - Cyfip2
  - Lmln
  - Khdrbs2
  - Hand2
  - Tbx20
  - Meis1
  - Ebf1
  - Pbx1
  - Sox9
  - Zeb2
  - Nrg3
  - Pdgfra
  - Usp9x
  - Shank2
  - Dnmt1
  - Dnmt3a
  - Mecp2
  - Tet1
  - Prox1
  - Bcl11b
  - Ntrk3
  - Satb1
  - Cux1
  - Foxi1
  - Tlx1
  - Foxo4
  - Neurog2
  - Hoxc9
key_pathways:
  - DNA_methylation_writing_DNMT1_DNMT3A
  - DNA_demethylation_TET
  - non_CpG_methylation_reading_MeCP2
  - polycomb_repressive_complex
  - oligodendrogenesis
  - neural_tube_patterning
  - cardiogenesis

# === User project membership ===
projects:
  - thesis
  - methods
priority: useful
read_status: read

# === HypoxiaVERSE-specific ===
hypoxiaverse_status: not_included
exclusion_reason: "not hypoxia-focused — included as methods/spatial-multi-omics reference and for the PMD-as-spatial-mitotic-clock concept relevant to TME proliferation maps"
data_availability: "GEO accession expected via Nature 2025 publication; processed objects through the paper's online content link"

# === Cross-references ===
code_url: ""
cited_by: []
---

## Problem

Spatial omics has matured rapidly for transcription, histone modifications, chromatin accessibility, and a handful of protein panels — but DNA cytosine methylation, arguably the most-studied mammalian epigenetic mark, has been completely absent from the spatial-omics catalogue. Existing single-cell DNA-methylation assays (sciMETv2, snmC-seq2) require tissue dissociation, destroying the spatial context that matters most for development, brain anatomy, and tumour architecture. The paper asks whether a microfluidic DBiT-seq-style spatial barcoding chassis can be combined with EM-seq enzymatic methylation conversion to co-profile DNAm and the transcriptome on the same intact tissue section at near single-cell resolution.

## Key idea

Spatial-DMT combines DBiT-seq spatial barcoding ([[foundations/dbit-seq-deterministic-barcoding-in-tissue]]) with EM-seq enzymatic conversion ([[foundations/em-seq-enzymatic-methyl-sequencing]]) and a streptavidin separation of cDNA from gDNA after barcoding. The cDNA stream is processed with standard template-switching scRNA-seq library prep; the gDNA stream is subjected to TET2+APOBEC conversion, splint ligation of a uracil-tolerant PCR handle, and library construction. The result is paired DNAm + RNA maps at 10–50 μm pixel resolution on the same tissue section. Joint analysis via WNN ([[foundations/wnn-weighted-nearest-neighbor-integration]]) reveals (i) ~10⁵ CpGs per pixel comparable to single-cell methylome assays, (ii) Pearson r ≈ 0.98 (DNAm) / 0.97 (RNA) replicate concordance, (iii) WNN modality weights identifying anatomical regions where DNAm dominates cell-identity (e.g., craniofacial W11) vs RNA (e.g., cardiac W6), (iv) both canonical negative and non-canonical positive coupling of methylation to gene expression, (v) non-CpG (mCH/mCA) accumulation specifically in the postnatal brain with gene-specific mCG-vs-mCA regulatory partitioning (Prox1, Bcl11b, Ntrk3, Cux1), (vi) PMD methylation as a spatial mitotic-history readout distinguishing proliferative from differentiated tissue compartments, and (vii) intra-cluster epigenetic heterogeneity (W7 forebrain vs spinal cord; D0 vs D4 within RNA cluster R3) revealing "epigenetically primed" subpopulations that single-modality maps cannot see.

## Method

**Tissue preparation**: Fresh-frozen mouse embryo (E11 at 10 and 50 μm; E13 at 50 μm) and P21 brain (20 μm) sections fixed with 1% formaldehyde, permeabilised with 0.5% Triton X-100, treated with 0.1 N HCl to remove histones and improve Tn5 accessibility.

**Spatial barcoding**: Two-round Tn5 tagmentation inserts a universal ligation linker into gDNA; biotinylated poly-dT reverse transcription primer captures mRNA. Two sets of microfluidic barcodes (A1–A50, B1–B50) flow perpendicularly to create a 50×50 grid of spatial barcodes (2,500 pixels per ROI). Pixel sizes: 50 μm (whole-embryo overview), 10 μm (E11 face/forebrain zoom), 20 μm (P21 brain).

**DNAm vs RNA stream separation**: Reverse crosslinking; streptavidin beads enrich biotinylated cDNA; gDNA stays in supernatant.

**DNAm stream**: TET2 oxidation of 5mC/5hmC + APOBEC deamination of unmodified C; SLP5 splint adapter with random H (A/C/T) ligated to 3′ ends; Vera-Seq uracil-tolerant polymerase PCR with modified P7 (N70X-HT). Barcodes designed so no crosstalk under C→T deamination is possible.

**RNA stream**: Template-switching reaction; Nextera XT library construction.

**Sequencing**: 2.8–3.9 billion raw reads per sample; 32.2–65.7% retention post-QC; 355,069–753,052 reads per pixel; 1,699–2,493 pixels per sample (Supplementary Table 5).

**Computational pipeline** (Supplementary Fig. 1): pixel filtering by knee-plot threshold; VMR identification on top-variable methylated regions; HVG-based RNA clustering; WNN integration ([[foundations/wnn-weighted-nearest-neighbor-integration]]); HOMER motif enrichment ([[foundations/homer-motif-enrichment-analysis]]); cell-type deconvolution against external scRNA-seq references (Qiu 2024 for embryo, Zeisel 2018 for P21 brain).

## Results

### 1. Method performance (Fig. 1c–e)
- 136,639–281,447 CpGs per pixel — comparable to sciMETv2 single-cell methylome assays.
- CpG retention 70–80%; mCA < 1% in embryos; mCA ≈ 3–4% in P21 brain.
- > 99% non-CpG conversion efficiency from linker-sequence QC.
- 1,890–4,626 genes per pixel and 3,596–16,709 UMIs per pixel — comparable to prior spatial transcriptomics (Liu 2020; Zhang 2023).
- Pearson r = 0.9836 (DNAm) and r = 0.9752 (RNA) between E11 replicates.

### 2. E11 mouse embryo joint methylome–transcriptome (Fig. 1f–h, Fig. 2)
- 14 WNN clusters (W0–W13) match anatomical regions (craniofacial W0, brain/spinal cord W2, heart W6, telencephalon W7/W11, olfactory W5/W10).
- Some clusters defined by RNA (W6 cardiac), others by DNAm (W11 craniofacial) — modality dominance is region-specific.
- Tissue-specific marker genes (Runx2, Mapt, Trim55) show canonical inverse coupling to nearby VMR methylation.
- A separate set (Ank3, Atp11c, Cyfip2, Lmln, Khdrbs2) shows positive VMR–expression coupling, validating [[concepts/methylation-positive-coupling-gene-expression]].
- HOMER motif enrichment at hypomethylated VMRs identifies tissue-specific TFs that are themselves expressed in the same cluster: Hand2/Tbx20/Meis1 in heart W6; Ebf1/Pbx1 in brain W2; Sox9/Ebf1/Zeb2 in craniofacial W0. EBF1 is enriched across all three — consistent with prior reports of EBF1 as a TET2 interaction partner.
- 10 μm resolution resolves W11 telencephalon progenitors (ventricular zone) from W7 GABAergic cortical interneurons (mantle zone).

### 3. E11 → E13 spatiotemporal dynamics (Fig. 3)
- Spatial pseudotime captures oligodendrocyte progenitor → premature oligodendrocyte migration from subpallium to pallium.
- Methylation loss couples bidirectionally: Nrg3 activated, Pdgfra silenced.
- E13 brain pixels upregulate Usp9x, Ank3, Shank2 with concomitant methylation loss (Wilcoxon p down to 8.5×10⁻⁸⁰).
- DNAm machinery itself (Dnmt1, Dnmt3a, Mecp2, Tet1) is upregulated in E13 vs E11 brain.

### 4. P21 mouse brain mCH–mCG–RNA co-mapping (Fig. 4)
- mCG and mCA jointly partition brain anatomy (DG, CA1, CA2, CA3, cortex).
- Gene-specific modality coupling: Prox1/Bcl11b ↔ both; Ntrk3/Satb1 ↔ mCG only; Cux1 (CA1/2) ↔ mCA only.
- Across both contexts, negative coupling predominates over positive.
- Cell-type deconvolution against Zeisel reference recovers cortical-layer laminar distribution (TEGLU7–8 layers 2/3, TEGLU3 layer 6), CA1/2 (TEGLU24), CA3 (TEGLU23), DG (DGGRC2).

### 5. Region-specific epigenetic variations (Fig. 5a–b)
- Differential methylation between ventricular and mantle zone of hindbrain/spinal cord enriches H3K4me1 marks and neural-progenitor-specific TFs (FOXO4, NEUROG2, HOXC9).
- Same WNN cluster (W7) at distant locations carries distinct hypomethylation signatures: FOXI1 in forebrain, TLX1 in spinal cord — intra-cluster epigenetic heterogeneity.

### 6. PMD spatial mitotic-history readout (Fig. 5c–e)
- PMD methylation low in embryonic heart (active cardiogenesis) and adult dentate gyrus (postnatal neurogenesis); high in P21 cortex (post-mitotic neurons).
- Gradient from mantle (high) to ventricular (low) zone in forebrain and hindbrain/spinal cord.

### 7. Epigenetic priming within transcriptionally similar pixels (Fig. 5f–g)
- Same RNA cluster (R3) splits into DNAm subclusters D0 (PITX1, AP2, EBF1, EBF2 — facial) and D4 (HOXA1/2/3, HOXC9, GATA1/2/4/6 — cardiac) with minimal gene-expression divergence — interpretable as epigenetically primed subpopulations.

## All claims (exhaustive)

- `[c01]` Spatial-DMT enables simultaneous whole-genome DNA-methylation + transcriptome profiling on the same tissue section at near single-cell resolution (p.1, abstract; Fig. 1a–b) "we introduce a method for whole-genome spatial co-profiling of DNA methylation and the transcriptome of the same tissue section at near single-cell resolution" — confidence: high — type: methodological — links: [[concepts/spatial-dmt-method]] [[foundations/em-seq-enzymatic-methyl-sequencing]] [[foundations/dbit-seq-deterministic-barcoding-in-tissue]] [[claims/spatial-dmt-co-profiles-methylation-transcriptome-tissue]]
- `[c02]` Per-pixel CpG coverage of 136,639–281,447 CpGs is comparable to existing single-cell DNA-methylation studies (p.3, Fig. 1c; Supplementary Table 5) "on average, 136,639–281,447 CpGs were covered per pixel across E11, E13 and P21 samples... comparable to previous single-cell DNA-methylation studies" — confidence: high — type: quantitative — links: [[concepts/spatial-dmt-method]] [[claims/spatial-dmt-cpg-coverage-comparable-scbsseq]]
- `[c03]` Replicate concordance is Pearson r=0.9836 for DNAm and r=0.9752 for RNA between E11 embryo maps at matched body parts (p.3, Extended Data Fig. 2a) "DNA methylation and RNA expression had high concordance (Pearson's r = 0.9836 for DNA methylation and r = 0.9752 for RNA expression)" — confidence: high — type: quantitative — links: [[concepts/spatial-dmt-method]] [[claims/spatial-dmt-replicate-pearson-concordance-e11-embryo]]
- `[c04]` CpG retention 70–80%; mCA < 1% in embryos; mCA ≈ 3–4% in P21 brain — consistent with known postnatal mCH accumulation (p.3, Fig. 1d, Extended Data Fig. 3d) "The CpG retention rates were consistently between 70% and 80% across all samples, whereas... mCA < 1% in embryos; mCA ≈ 3–4% in the postnatal brain... consistent with the known increase in non-CpG methylation in postnatal neuronal tissues" — confidence: high — type: quantitative — links: [[concepts/non-cpg-methylation-postnatal-brain]] [[foundations/em-seq-enzymatic-methyl-sequencing]] [[claims/cpg-retention-70-80pct-mch-low-embryos-3-4pct-p21-brain]]
- `[c05]` WNN multimodal integration of DNAm + RNA yields clusters with enhanced resolution beyond either single modality (p.3-4, Fig. 1f) "their integration through WNN analysis yielded clusters with enhanced resolution" — confidence: high — type: methodological — links: [[foundations/wnn-weighted-nearest-neighbor-integration]] [[concepts/spatial-dmt-method]] [[claims/wnn-multimodal-integration-improves-cluster-resolution-vs-single-modality]]
- `[c06]` Per-pixel WNN modality weights vary by anatomy: cardiac cluster W6 is RNA-defined; craniofacial cluster W11 is DNAm-defined (p.4, Extended Data Fig. 4g) "some clusters were defined predominantly by gene expression (for example, W6, cardiac tissue), whereas others by DNA methylation (for example, W11, craniofacial region)" — confidence: medium — type: methodological — links: [[foundations/wnn-weighted-nearest-neighbor-integration]] [[claims/modality-weights-differ-cardiac-rna-craniofacial-dnam-defined]]
- `[c07]` Spatial cluster-specific gene expression is frequently associated with low methylation at neighbouring VMRs (Runx2 craniofacial; Mapt brain; Trim55 heart) (p.4, Fig. 2a–c) "Spatial cluster-specific gene expression is frequently associated with low DNA methylation at the neighbouring VMRs, as exemplified by signature genes Runx2, Mapt, and Trim55" — confidence: high — type: correlational — links: [[concepts/variably-methylated-regions-vmr]] [[claims/vmr-hypomethylation-correlates-cluster-specific-expression]]
- `[c08]` A subset of genes (Ank3, Atp11c, Cyfip2, Lmln, Khdrbs2) shows positive correlation between expression and nearby VMR methylation in E11 embryo — non-canonical methylation–expression coupling (p.4, Fig. 2c–d) "we also identified genes, for example, Ank3, Atp11c, Cyfip2, Lmln and Khdrbs2, for which expression is positively correlated with the methylation levels of the associated VMRs" — confidence: high — type: correlational — links: [[concepts/methylation-positive-coupling-gene-expression]] [[concepts/variably-methylated-regions-vmr]] [[claims/positive-vmr-methylation-expression-coupling-ank3-atp11c-cyfip2-lmln-khdrbs2]]
- `[c09]` Tissue-specific TFs (Hand2/Tbx20/Meis1 heart; Ebf1/Pbx1 brain; Sox9/Ebf1/Zeb2 craniofacial) are expressed in spatial clusters whose hypomethylated VMRs are enriched for their binding motifs (p.4, Fig. 2e) "TFs associated with heart development, Hand2, Tbx20 and Meis1, were expressed in cluster W6, the corresponding hypomethylated VMRs of which were enriched in the binding motifs of these TFs" — confidence: high — type: correlational — links: [[foundations/homer-motif-enrichment-analysis]] [[claims/tissue-specific-tf-motifs-hypomethylated-vmrs-tf-coexpression]]
- `[c10]` EBF1 is expressed and motif-enriched at hypomethylated VMRs across three distinct E11 tissue clusters (heart, brain/spinal cord, craniofacial) — consistent with EBF1's reported partnership with TET2 (p.4, Fig. 2e) "Notably, Ebf1 was expressed and its binding motif was also enriched across all three tissue regions... EBF1 was reported as an interaction partner for TET2" — confidence: medium — type: mechanistic — links: [[foundations/tet-mediated-dna-demethylation]] [[claims/ebf1-expressed-binding-motif-across-three-tissue-clusters-e11-embryo]]
- `[c11]` Joint DNAm + RNA spatial pseudotime in E11 embryo reconstructs subpallium → pallium oligodendrocyte-progenitor migration during oligodendrogenesis (p.5, Fig. 3a) "Spatial mapping of the pseudotime of each pixel revealed the organized migration of oligodendrocyte progenitor cells from the subpallium to the pallium during oligodendrogenesis" — confidence: medium — type: methodological — links: [[concepts/spatial-dmt-method]] [[claims/spatial-pseudotime-oligodendrogenesis-subpallium-to-pallium-migration]]
- `[c12]` Methylation loss in oligodendrogenesis couples bidirectionally to expression: Nrg3 activated, Pdgfra silenced (p.5, Fig. 3b) "loss of DNA methylation can be both associated with gene activation (for example, Nrg3, an oligodendrocyte marker) and silencing (for example, Pdgfra, an oligodendrocyte precursor marker)" — confidence: medium — type: mechanistic — links: [[concepts/methylation-positive-coupling-gene-expression]] [[claims/methylation-loss-bidirectional-coupling-nrg3-pdgfra-oligodendrogenesis]]
- `[c13]` From E11 to E13 brain/spinal cord, neuronal genes Usp9x, Ank3, Shank2 are upregulated with concomitant methylation loss (Wilcoxon RNA P down to 4e-37; DNAm P down to 8.55e-80) (p.5, Fig. 3e–f) "we identified genes upregulated in E13 (Fig. 3e) associated with notable loss of DNA methylation (Fig. 3f)... Usp9x, Ank3 and Shank2" — confidence: high — type: quantitative — links: [[claims/e13-vs-e11-brain-neuronal-genes-upregulated-methylation-decrease-usp9x-ank3-shank2]]
- `[c14]` DNA-methylation machinery genes (Dnmt1, Dnmt3a, Mecp2, Tet1) are elevated in expression in E13 vs E11 mouse embryo brain (p.5, Fig. 3h) "some DNA methylation writers, readers and eraser enzymes, for example, Dnmt1, Dnmt3a, Mecp2 and Tet1, showed higher expression in the E13 embryo" — confidence: medium — type: correlational — links: [[foundations/dnmt1-maintenance-methyltransferase]] [[foundations/dnmt3a-de-novo-dna-methyltransferase]] [[foundations/mecp2-methyl-cpg-binding-protein]] [[foundations/tet-mediated-dna-demethylation]] [[claims/dna-methylation-machinery-dnmt1-dnmt3a-mecp2-tet1-elevated-e13-vs-e11-brain]]
- `[c15]` In P21 brain, mCG and mCA regulate gene expression in a gene-specific manner: Prox1 and Bcl11b correlate with both; Ntrk3 and Satb1 with mCG only; Cux1 (CA1/2) with mCA only (p.6, Fig. 4c–h) "Prox1 and Bcl11b expression was significantly associated with both mCG and mCA... Ntrk3... correlating primarily with mCG levels but not with mCA... Satb1 expression in the cortex was strongly correlated with mCG but not with mCA levels... Cux1 expression showed a negative correlation only with CA hypermethylation and seemed independent of mCG levels" — confidence: high — type: mechanistic — links: [[concepts/non-cpg-methylation-postnatal-brain]] [[foundations/mecp2-methyl-cpg-binding-protein]] [[claims/mcg-mca-gene-specific-regulation-p21-brain-prox1-bcl11b-ntrk3-satb1-cux1]]
- `[c16]` PMD methylation acts as a spatial mitotic-history readout: low in proliferative tissue (embryonic heart, P21 dentate gyrus), high in differentiated tissue (P21 cortex); gradients from mantle (high) to ventricular zone (low) in developing brain (p.7, Fig. 5c–e) "partially methylated domains (PMDs), which lose methylation over successive mitotic divisions, serve as indicators of mitotic activity... embryonic heart tissue demonstrated lower PMD methylation levels... In the P21 brain... cortical layers displayed higher PMD methylation... DG has comparatively lower PMD methylation" — confidence: medium — type: mechanistic — links: [[concepts/partially-methylated-domains-mitotic-clock]] [[foundations/dnmt1-maintenance-methyltransferase]] [[claims/pmd-methylation-spatial-mitotic-history-readout-embryos-brain]]
- `[c17]` Spatially distant pixels in the same WNN cluster (W7) carry distinct methylation signatures: FOXI1 motif enrichment in forebrain pixels vs TLX1 motif enrichment in spinal-cord pixels (p.7, Fig. 5b) "In the forebrain, regions with loss of methylation were enriched for binding sites of FOXI1, TFs crucial for auditory development. By contrast, spinal-cord-specific hypomethylation correlated with occupancy by TLX1" — confidence: medium — type: methodological — links: [[claims/intracluster-epigenetic-heterogeneity-w7-forebrain-vs-spinal-cord-foxi1-tlx1]]
- `[c18]` Within RNA cluster R3, DNAm subclusters D0 (PITX1/AP2/EBF1 facial-morphogenesis motifs) and D4 (HOXA/GATA cardiac-morphogenesis motifs) split pixels with similar transcription into distinct epigenetically primed states (p.8, Fig. 5f–g) "DNA methylation-defined cluster 0 (D0) and 4 (D4) cells had distinct subpopulations when stratified by their VMRs. Motif enrichment analysis... identified regulatory elements associated with facial and cardiac morphogenesis... whereas corresponding gene-expression changes were limited... This may reflect epigenetically primed subpopulations that share similar transcriptional states" — confidence: medium — type: mechanistic — links: [[foundations/homer-motif-enrichment-analysis]] [[claims/epigenetic-subclustering-d0-d4-within-rna-cluster-r3-distinct-tf-motifs]]
- `[c19]` At 10 μm resolution, spatial-DMT separates W11 telencephalon progenitors (ventricular zone) from W7 GABAergic cortical interneurons (mantle zone) in E11 embryo forebrain, recovering the canonical neurogenic-niche → migrating-neuron lineage (p.4, Fig. 1g–h, Extended Data Fig. 8) "W11 was enriched for telencephalon progenitors in the ventricular zone... whereas W7 corresponded to γ-aminobutyric-acid-releasing (GABAergic) cortical interneurons localized in the mantle zone" — confidence: high — type: methodological — links: [[concepts/spatial-dmt-method]] [[claims/spatial-dmt-10um-resolves-telencephalic-progenitors-vs-gabaergic-cortical-interneurons-e11]]

## Discussion captured

### Authors' interpretation

The authors frame spatial-DMT as the first method to bring DNA cytosine methylation into spatial multi-omics, on equal footing with the already-spatial transcriptome, histone-modification, and chromatin-accessibility assays. They interpret the per-pixel WNN modality weights as biologically meaningful: regions where methylation dominates cell identity (e.g., craniofacial W11) reveal epigenetically distinct cell states that transcriptome-only spatial assays cannot resolve. The bidirectional VMR–expression couplings (negative for most genes, positive for Ank3 and others) are interpreted as evidence for the established but under-recognised mechanisms in which methylation positively regulates transcription (enhancer-bound, gene-body, Polycomb-target). The mCH partitioning in postnatal brain — where some genes respond to mCG only, others to mCA only, others to both — is interpreted as a sequence-context-specific regulatory grid layered on top of mCG. The PMD-as-mitotic-clock finding is positioned as a free additional readout of any methylome assay that becomes spatially powerful in spatial-DMT.

### Comparisons with prior literature (made by authors)

- **DBiT-seq (Liu 2020, ref 1)** — the spatial-barcoding chassis spatial-DMT inherits.
- **Spatial ATAC–RNA (Zhang 2023, ref 2)** — the closest prior spatial multi-omics method; same chassis, different modality.
- **MOSAIC / multiplexed spatial chromatin (Guo 2025, ref 3)** — multiplexed spatial multi-omics framework spatial-DMT complements.
- **sciMETv2 (Nichols 2022, ref 12); snmC-seq (Liu 2021, ref 5); Hernando-Herraez 2019 (ref 10); Shareef 2021 (ref 14); He 2020 (ref 16)** — single-cell methylome assays used as the per-pixel CpG-coverage benchmark.
- **Yin 2017 (ref 21); Yang 2014 (ref 22); Li 2018 (ref 23)** — prior literature on positive methylation–expression coupling at enhancers, gene bodies, and Polycomb targets.
- **Guilhamon 2013 (ref 24)** — EBF1 as a TET2 interaction partner; the spatial-DMT EBF1 finding is interpreted in light of this.
- **Qiu 2024 (ref 25); Zeisel 2018 (ref 44)** — scRNA-seq references used for cell-type deconvolution in E11 embryo and P21 brain.
- **Guo 2014 (ref 15); Lister 2013** — prior work on non-CpG methylation in the postnatal brain that spatial-DMT spatialises.
- **Kremer 2024 (ref 18)** — MethSCAn; reference VMR analysis pipeline.
- **Hao 2021 (ref 19)** — Seurat WNN integration; backbone used here for joint DNAm + RNA clustering.

### Mechanistic hypotheses proposed

- Hypomethylated VMRs are likely TF-driven: motif enrichment for TFs that are themselves expressed in the same cluster supports a local-recruitment model in which TF binding induces TET-mediated demethylation.
- EBF1 may be a general TET2-recruitment partner across multiple embryonic tissues.
- Positive methylation–expression coupling at gene bodies and Polycomb targets explains the Ank3-class genes.
- The mCH/mCA regulatory grid in post-mitotic neurons is read primarily by MeCP2 and complements the mCG-based regulatory grid in a gene-specific manner.
- D0 vs D4 "epigenetically primed" subpopulations may represent precursors that will later commit to divergent fates (facial vs cardiac) — testable by sampling E12.

### Caveats and self-criticism

- Most couplings are correlational; no in vivo causal manipulation in any of the tissues.
- The current chemistry cannot distinguish 5mC from 5hmC.
- The 10 μm pixel size is "near single-cell" but still multi-cellular.
- Deconvolution depends on the quality of external scRNA-seq references.
- No FFPE adaptation yet, limiting clinical translation.

### Future directions suggested

- Incorporate additional modalities — chromatin conformation (HiC), accessibility (ATAC), histone marks (CUT&Tag), metabolome (MSI), surface proteins (CITE-seq).
- Couple with long-read sequencing (Nanopore, PacBio) to simplify modification detection and increase coverage.
- Adapt to FFPE specimens for clinical samples.
- Develop spatial computational deconvolution to recover single-cell methylomes from multi-cellular pixels.
- Broader application across tissues, developmental stages, species — generalisability proof.

## Limitations

- 5mC vs 5hmC chemically indistinguishable in current implementation.
- 10 μm pixels still average over multiple cells in most tissue contexts.
- Limited to fresh-frozen sections; no FFPE protocol yet.
- HCl + Tn5 tissue treatment may degrade labile RNA; mitigated by two-round multi-tagmentation but not eliminated.
- Whole-section profiling requires tiling; not yet whole-organ.
- Pipeline depends on external scRNA-seq references for cell-type deconvolution.
- Validation limited to mouse; no human-tissue benchmark.

## Open questions

### Open questions raised by authors

- Whether 5mC and 5hmC can be distinguished at spatial resolution using emerging methylation chemistry.
- Whether spatial-DMT can be combined with chromatin conformation / accessibility / histone marks / metabolome / protein in a single pixel.
- Whether long-read EM-seq integration can extend coverage and resolve haplotype-specific methylation in tissue.
- Whether FFPE samples can be made spatial-DMT-compatible.
- Whether spatial computational deconvolution can recover single-cell methylomes from multi-cellular pixels.

### Open questions identified during ingest

- Inter-laboratory reproducibility of spatial-DMT — the paper's r ≈ 0.98 / 0.97 numbers are intra-lab.
- Quantitative model linking PMD methylation to absolute mitotic count, validated against orthogonal proliferation markers (Ki67, EdU).
- Genome-wide rule predicting which genes show positive vs negative VMR–expression coupling from sequence + chromatin features.
- Direct EBF1–TET2 functional test in mouse embryo by EBF1 KO or TET2 KO with spatial-DMT readout.
- D0 vs D4 fate tracing — do these populations later diverge transcriptionally?
- Methylation distance to nearest VMR matters: the paper aggregates "neighbouring VMRs" without a sensitivity analysis on neighbourhood definition.
- How spatial-DMT performs in tumours, particularly where PMD hypomethylation is heavy — is the PMD mitotic-clock interpretable in cancer tissue, or does global PMD hypomethylation dominate the signal?

## My take

This paper closes the last big modality gap in spatial multi-omics. The methodological contribution is real: bringing DNA cytosine methylation to tissue scale at near single-cell resolution removes a long-standing blind spot for developmental, neurological, and tumour biology. Three findings are genuinely novel rather than confirmatory:

1. **WNN modality weights as biology**: the per-pixel modality weight is itself a biological signal — DNAm-dominated regions identify epigenetically distinct cell states that look transcriptionally bland.
2. **Spatial PMD-as-mitotic-clock**: spatial PMD gradients recapitulate proliferative-to-post-mitotic anatomy. This is a "free" readout that any single-cell methylome assay had access to but never exploited spatially.
3. **Epigenetic priming of D0/D4 within RNA cluster R3**: pixels that look transcriptionally identical but carry distinct lineage-specific TF-motif methylation signatures — interpretable as primed but uncommitted progenitors. A direct, methylome-only window into lineage decision-making.

The thesis-relevant lens: for any future TME / cancer / hypoxia methylome work, the PMD-as-spatial-mitotic-clock framing is the cleanest transferable concept. PMD-based mitotic mapping in tumours would let one read "how many times has this region divided" directly from a single methylome assay — orthogonal to Ki67 IHC and immune-cell-infiltration markers.

The biggest limitation is the inability to distinguish 5mC from 5hmC, which matters in any context with active demethylation (cancer hypoxia, inflammatory macrophages, neuronal maturation). Until that limitation is solved, spatial-DMT in those contexts will conflate the two marks.

## Related

- [[foundations/dbit-seq-deterministic-barcoding-in-tissue]] — spatial-barcoding chassis spatial-DMT extends.
- [[foundations/em-seq-enzymatic-methyl-sequencing]] — conversion chemistry used in spatial-DMT.
- [[foundations/wnn-weighted-nearest-neighbor-integration]] — multimodal integration backbone.
- [[foundations/dnmt1-maintenance-methyltransferase]] — maintenance methyltransferase; PMD decay model.
- [[foundations/dnmt3a-de-novo-dna-methyltransferase]] — de novo methyltransferase; embryonic dynamics.
- [[foundations/mecp2-methyl-cpg-binding-protein]] — non-CpG methylation reader in postnatal brain.
- [[foundations/tet-mediated-dna-demethylation]] — active demethylation; EBF1–TET2 partnership.
- [[foundations/homer-motif-enrichment-analysis]] — TF-motif enrichment at hypomethylated VMRs.
- [[foundations/scrna-seq-10x-chromium]] — transcriptome chemistry; reference scRNA-seq atlases used for deconvolution.
- [[foundations/atac-seq]] / [[foundations/spatial-atac-seq]] — closest prior spatial-epigenome method (different modality).
- [[foundations/illumina-methylationepic-array]] / [[foundations/medip-methylated-dna-immunoprecipitation]] — non-spatial methylation profiling alternatives.
- [[concepts/spatial-dmt-method]] — concept page for the method.
- [[concepts/variably-methylated-regions-vmr]] — VMR concept used throughout.
- [[concepts/partially-methylated-domains-mitotic-clock]] — PMD mitotic-history concept.
- [[concepts/non-cpg-methylation-postnatal-brain]] — mCH/mCA brain concept.
- [[concepts/methylation-positive-coupling-gene-expression]] — positive VMR–expression coupling.
