---
title: "CellCharter reveals spatial cell niches associated with tissue remodeling and cell plasticity"
slug: cellcharter-reveals-spatial-cell-niches-associated
arxiv: ""
doi: "10.1038/s41588-023-01588-4"
pmid: "38066188"
venue: "Nature Genetics"
year: 2024
authors:
  - "Marco Varrone"
  - "Daniele Tavernari"
  - "Albert Santamaria-Martínez"
  - "Logan A. Walsh"
  - "Giovanni Ciriello"
first_author: "Marco Varrone"
corresponding_author: "Giovanni Ciriello"

source_type: pdf
s2_id: "26b2656b8050c4bb7828828a74793407038c332d"
date_added: 2026-05-22
ingested_date: 2026-05-22
ingest_version: 1
last_reviewed:

importance: 4
tier: TIER_1
tags:
  - spatial-transcriptomics
  - spatial-proteomics
  - cellular-niches
  - tumor-microenvironment
  - hypoxia
  - tumor-associated-neutrophil
  - LUAD
  - clustering-methods
keywords:
  - CellCharter
  - cellular niches
  - spatial omics
  - GMM clustering
  - variational autoencoder
  - tumor-associated neutrophil
  - response to hypoxia
  - cluster neighborhood enrichment
  - cluster shape
domain: "methods / oncology / immunology / spatial-omics"

tissue:
  - lung
  - spleen
  - brain
  - multi
condition:
  - cancer
  - autoimmune
  - healthy
disease_specific:
  - LUAD
  - LUSC
  - systemic_lupus_erythematosus
species:
  - human
  - mouse
hypoxia_relevant: true
contains_immune_cells: true
contains_myeloid: true

techniques:
  - spatial_visium
  - CosMx_spatial_transcriptomics
  - MERFISH_spatial
  - CODEX_multiplexed_imaging
  - imaging_mass_cytometry
  - spatial_ATAC
  - bulk_RNA-seq
  - variational_autoencoder
  - GMM_clustering
n_samples: "12 (DLPFC Visium) + 42 (extended DLPFC) + 9 (CODEX spleen) + 8 (NSCLC CosMx, 5 patients) + 2 (MERFISH lung) + 416 (IMC LUAD TMA cores) + 9 LUAD bulk cohorts"
n_cells_total: ">2M (across all datasets)"
integration_method: "scVI / per-modality VAE + batch correction"

key_cell_types:
  - tumor cells (LUAD)
  - tumor-associated neutrophil
  - CD4 memory T cell
  - NK cell
  - fibroblast
  - monocyte
  - macrophage
  - normal epithelial
  - B cell
  - B follicle
  - marginal zone macrophage
  - granulocyte
key_markers:
  - NDRG1
  - VEGFA
  - S100A8
  - S100A9
  - CXCL1
  - CXCL2
  - CXCL3
  - MKI67
  - FGFR1
  - FGFR2
  - EZH2
  - MPO
  - HIF1A
  - CD31
  - Ly6G
  - PanCK
  - alphaSMA
  - CD45
  - CD20
  - CD14
  - Ki67
  - PDL1
key_pathways:
  - response to hypoxia
  - epithelial-to-mesenchymal transition
  - chemokine signaling
  - neutrophil chemotaxis
  - cytokine-cytokine receptor interaction
  - cell proliferation

projects:
  - hypoxia
  - thesis
  - methods
priority: core
read_status: deep_read

hypoxiaverse_status: included
exclusion_reason:
data_availability: "Code at https://github.com/CSOgroup/cellcharter; datasets are public (10x Visium DLPFC GSE160190, CODEX spleen Goltsev 2018, CosMx NSCLC He 2022 Nat Biotechnol, MERFISH Vizgen public, IMC LUAD Sorin 2023)"

code_url: "https://github.com/CSOgroup/cellcharter"
cited_by: []
---

## Problem

Spatial omics technologies produce large, heterogeneous datasets in which tissue architecture is encoded as cellular niches — sets of cells with characteristic compositions and spatial interactions. Existing clustering tools (BayesSpace, STAGATE, SEDR, DR-SC, SOTIP, UTAG, SpaGCN) cannot simultaneously (a) scale to hundreds of samples and millions of cells, (b) operate jointly across donors with batch correction, (c) generalise across spatial proteomics, transcriptomics, ATAC and multiome platforms, and (d) characterise / compare clusters beyond identification (cluster proportions, cell-type enrichment, neighbourhood enrichment, shape).

## Key idea

CellCharter combines four steps: (1) data-type-appropriate VAEs for dimensionality reduction and batch correction; (2) feature concatenation across `l`-hop spatial neighbourhoods; (3) GMM clustering with stability auto-selection via the Fowlkes–Mallows Index; (4) downstream cluster characterization (cell-type enrichment, symmetric/asymmetric NE, differential NE, cluster shape via curl/elongation/linearity/purity). The modular design — only the VAE depends on the data modality — yields a technology-agnostic, scverse-compatible pipeline.

## Method

- Inputs: cells/spots × features (mRNA, protein, ATAC) + spatial coordinates; multiple samples may be passed jointly.
- Per-modality VAEs (scVI for scRNA-derived, Poisson-NB for ATAC, Gaussian for protein) embed inputs and correct batch.
- For each cell A, feature vector concatenated with feature averages over neighbours at 1..l steps in a proximity graph.
- GMM clustering repeated n=10 times; stability assessed via FMI across runs at n−1, n, n+1.
- Downstream: cluster cell-type enrichment, analytical symmetric/asymmetric NE, differential NE, cluster shape descriptors.

## Results

- DLPFC Visium benchmark (9 test samples, joint): CellCharter mean ARI 0.62 vs STAGATE 0.49, DR.SC 0.51, BayesSpace 0.45, SEDR 0.45, UTAG 0.36 (P<0.05 to P=1e-7).
- Memory (Fig. 1c): 5.8–6.1 GB CellCharter vs 40–84 GB for STAGATE/SOTIP/SEDR. ~4× faster than STAGATE on 707k-cell mouse spleen.
- FMI-stability selects n=9 for DLPFC (12 and 42 samples), matching biological expectation (~7 cortical layers + WM).
- Joint RNA+ATAC multiome clustering of mouse brain recovers anatomy better than either modality alone (Fig. 2c).
- MRL lupus mouse spleen: B-follicle (C3), B-PALS-boundary (C2), marginal-zone (C4) gain curl and lose linearity (Wilcoxon P=9.6e-5 to 0.0064); two distinct trabecular niches (CD31+/Ly6G− C10, CD31−/Ly6G+ C11) emerge in lupus (Fig. 3).
- NSCLC CosMx (5 patients): three stable solutions (n=3/8/20) reflect cancer/individual-tumour/intratumour-state hierarchy. In LUAD-9, cluster C0 expresses NDRG1, VEGFA, S100A8/9, CXCL1/2/3 (hypoxia + chemokine state); cluster C12 expresses MKI67, FGFR1/2, EZH2 (proliferative state). C0 surrounds neutrophil cluster C11; signature scores spatially anticorrelate with cell-proliferation signatures (Fig. 4–5).
- MERFISH LUAD (2 samples) and IMC LUAD TMA (416 cores) reproduce the hypoxic-tumour + TAN niche: in IMC, MPO+/HIF1A+ tumour cluster C23 is invariably surrounded by neutrophil cluster C7 (Fig. 6).
- Across 9 LUAD bulk-transcriptomic cohorts (TCGA-LUAD n=513, Shedden, Schabath, Okayama, Der, Chen, Mezheyeuski, Ding, Tavernari): response-to-hypoxia signature correlates with TAN signature (Sorin 2023) but not NAN; both response-to-hypoxia and TAN signatures associate with worse OS in multivariate Cox; NAN does not.

## All claims (exhaustive)

- `[c01]` CellCharter outperforms STAGATE/BayesSpace/SEDR/DR-SC/SOTIP/UTAG on joint DLPFC Visium clustering (p.76) "CellCharter outperformed existing tools when jointly clustering all samples, both in terms of average ARI ... and best ARI" — confidence: high — type: methodological — links: [[claims/cellcharter-outperforms-stagate-bayesspace-sedr-dr]] [[foundations/cellcharter-framework]] [[foundations/10x-visium-spatial-transcriptomics]]
- `[c02]` CellCharter scales to millions of cells with the lowest memory among benchmarked tools (p.76) "CellCharter exhibited the lowest memory usage, both in its GPU and CPU versions" — confidence: high — type: methodological — links: [[claims/cellcharter-scales-millions-cells-lowest-memory]] [[foundations/cellcharter-framework]]
- `[c03]` FMI-stability identifies biologically meaningful cluster counts (n=9 DLPFC, n=4/11 spleen, n=3/8/20 NSCLC) (p.76–77, 80) "CellCharter indicated n = 9 as the optimal number of clusters, close to the number of manually annotated regions" — confidence: medium — type: methodological — links: [[claims/fowlkes-mallows-stability-identifies-biologically-meaningful]] [[foundations/fowlkes-mallows-index]]
- `[c04]` Joint RNA+ATAC spatial multiome clustering recapitulates brain anatomy better than single-modality (p.77) "CellCharter identified ten spatial clusters that better recapitulated the tissue anatomy when jointly using both data modalities than when using either of them alone" — confidence: medium — type: methodological — links: [[claims/joint-multimodal-rna-plus-atac-spatial]] [[foundations/atac-seq]] [[foundations/cellcharter-framework]]
- `[c05]` Batch correction is essential for joint multi-sample spatial clustering on DLPFC (p.76) "without batch correction, clusters were associated with donors rather than tissue anatomy" — confidence: high — type: methodological — links: [[claims/batch-correction-essential-joint-multi-sample]] [[foundations/cellcharter-framework]]
- `[c06]` Cluster shape descriptors detect loss of spleen architecture in systemic lupus (p.78) "both the B-PALS and B follicle clusters significantly increased their curl values, whereas B-PALS and marginal zone clusters significantly lost linearity" — confidence: high — type: correlational — links: [[claims/cluster-shape-descriptors-detect-loss-spleen]] [[concepts/cluster-shape-analysis-spatial]] [[foundations/codex-multiplexed-imaging]]
- `[c07]` MRL lupus spleen shows differential B-follicle / marginal-zone / B-PALS interactions vs healthy (p.78) "the B follicle cluster (C3) decreased interaction enrichment with the marginal zone (C4) in favor of interactions with the B-PALS cluster (C2)" — confidence: high — type: correlational — links: [[claims/mrl-lupus-spleen-shows-differential-follicle]] [[concepts/cluster-neighborhood-enrichment-spatial]]
- `[c08]` MRL spleens develop two distinct trabecular niches with differential CD31/Ly6G expression (p.78–79) "in MRL samples, CellCharter captured the emergence of two distinct trabecular niches ... a CD31+/Ly6G− cluster in proximity to PALS and a CD31−/Ly6G+ cluster within the red pulp" — confidence: medium — type: correlational — links: [[claims/mrl-spleens-develop-two-distinct-trabecular]]
- `[c09]` Hierarchical stable cluster solutions (n=3/8/20) reflect cancer-wide, individual-tumour, and intratumour cancer states in NSCLC (p.79) "CellCharter stable cluster solutions reflected a hierarchy of biological entities: cancer, individual tumors, and intratumor cell states" — confidence: medium — type: methodological — links: [[claims/hierarchical-stable-cluster-solutions-reflect-cancer]] [[foundations/cosmx-spatial-transcriptomics]]
- `[c10]` LUAD tumour cluster C0 (CosMx) expresses a hypoxia + EMT + chemokine state (NDRG1, VEGFA, S100A8/9, CXCL1/2/3) (p.80) "upregulated genes in C0 compared with C12 comprised the hypoxia-inducible gene NDRG1 ... the angiogenic factor VEGFA ... S100A8 and S100A9, and chemokine-encoding genes CXCL1, CXCL2, and CXCL3" — confidence: high — type: mechanistic — links: [[claims/luad-tumor-cluster-c0-expresses-hypoxia]] [[concepts/tan-hypoxia-tumor-niche-luad]] [[foundations/ndrg1]] [[foundations/hif1a]] [[concepts/hypoxia-emt-lineage-plasticity-metastasis]]
- `[c11]` LUAD tumour cluster C12 expresses a proliferative state (MKI67, FGFR1, FGFR2, EZH2) spatially segregated from C0 (p.80) "Upregulated genes in C12 compared with C0 were instead enriched for cell proliferation markers, such as MKI67, and comprised genes encoding for fibroblast growth factor receptors FGFR1 and FGFR2, and for the histone modifier EZH2" — confidence: medium — type: mechanistic — links: [[claims/luad-tumor-cluster-c12-expresses-proliferative]] [[concepts/tan-hypoxia-tumor-niche-luad]]
- `[c12]` Hypoxia signature score in LUAD tumour cells anticorrelates with distance to TANs (p.80) "the response-to-hypoxia signature scores in tumor cells were anticorrelated with the distance between tumor cells and neutrophils that were found in cluster C11" — confidence: high — type: correlational — links: [[claims/hypoxia-signature-tumor-cells-anticorrelates-distance]] [[concepts/tan-hypoxia-tumor-niche-luad]]
- `[c13]` MERFISH LUAD dataset replicates the hypoxic-tumour + neutrophil niche (p.80) "cluster C5 was significantly interacting with a neutrophil-enriched cluster (C14), and exhibited high scores for the response-to-hypoxia gene signature" — confidence: medium — type: correlational — links: [[claims/merfish-luad-dataset-replicates-hypoxic-tumor]] [[foundations/merfish-imaging-spatial]] [[concepts/tan-hypoxia-tumor-niche-luad]]
- `[c14]` IMC LUAD cohort (416 cores) identifies MPO+/HIF1A+ tumour cluster C23 surrounding neutrophil cluster C7 (p.80–81) "cluster C23, which exhibited high expression of myeloperoxidase (MPO) ... and hypoxia-inducible factor HIF1A ... C23 exhibited significant interactions with multiple clusters enriched for neutrophils, most of all cluster C7" — confidence: high — type: correlational — links: [[claims/imc-luad-cohort-identifies-mpo-hif1a]] [[foundations/mpo-myeloperoxidase]] [[foundations/hif1a]] [[concepts/tan-hypoxia-tumor-niche-luad]]
- `[c15]` Response-to-hypoxia signature correlates with TAN but not NAN signature across 9 LUAD cohorts (p.81) "In multiple independent LUAD cohorts, the response-to-hypoxia signature was highly correlated with TAN infiltration but showed no correlation with NAN" — confidence: high — type: correlational — links: [[claims/response-hypoxia-signature-correlates-tan-nan]] [[concepts/tan-hypoxia-tumor-niche-luad]]
- `[c16]` Response-to-hypoxia and TAN signatures associate with worse LUAD prognosis; NAN does not (p.81) "multivariate Cox regression analysis found a significant association with worse prognosis for response-to-hypoxia and TAN signatures, but not for NAN" — confidence: high — type: correlational — links: [[claims/response-hypoxia-tan-signatures-associate-worse]] [[concepts/tan-hypoxia-tumor-niche-luad]]
- `[c17]` Authors propose a positive-feedback loop between tumour hypoxia, chemokine-driven neutrophil recruitment, and EMT in LUAD (p.81–82) "Our results hence suggest a positive feedback between these interacting cells promoting cancer cell state transition" — confidence: low — type: mechanistic — links: [[claims/authors-propose-tumor-hypoxia-neutrophil-emt]] [[concepts/tan-hypoxia-tumor-niche-luad]] [[concepts/hypoxia-emt-lineage-plasticity-metastasis]]
- `[c18]` Cell-type admixing vs segregation distinguishes patients with similar TME composition (p.79) "the same proportions of the same immune cell populations can exhibit spatial admixing or spatial segregation in different patients" — confidence: medium — type: correlational — links: [[claims/cell-type-admixing-versus-segregation-distinguishes]]
- `[c19]` CellCharter's analytical cluster NE is more scalable than permutation-based tests (p.75) "CellCharter introduces an analytical approach to compute symmetric and asymmetric cluster NE, which is more efficient than currently available permutation-based methods" — confidence: medium — type: methodological — links: [[claims/analytical-cluster-neighborhood-enrichment-scales-beyond]] [[concepts/cluster-neighborhood-enrichment-spatial]]
- `[c20]` Tumour-enriched spatial clusters are patient-private while TME-enriched clusters are shared across patients (p.79) "Tumor-enriched clusters were almost invariably patient-specific but shared between independent samples derived from the same patient. Although TME-enriched clusters were often shared among patients" — confidence: medium — type: correlational — links: [[claims/tumor-enriched-clusters-patient-private-while]]

## Discussion captured

### Authors' interpretation

- The authors interpret the lung-cancer niche as evidence that spatial organisation distinguishes coexisting cancer cell states (hypoxic-EMT vs proliferative) within the same tumour. They argue this is invisible to non-spatial single-cell omics, and that the spatial coupling between hypoxic tumour cells and TANs reveals a "biological communication unit" — a tumour-microenvironment niche with prognostic value.
- They emphasise the modular, scverse-compatible design as enabling future integration of histology / hematoxylin & eosin features and digital-pathology pipelines.

### Comparisons with prior literature (made by authors)

- Compares against Squidpy (Palla et al. 2022, Nat. Methods) ref. 46 — the permutation-based NE baseline.
- Cites Sorin et al. 2023 *Nature* (ref. 24) for TAN signature, IMC LUAD dataset, and prognostic links between TAN infiltration and tumour invasion.
- Cites Goltsev et al. 2018 *Cell* (ref. 5) for the CODEX mouse-spleen dataset.
- Cites Maynard et al. 2021 (DLPFC Visium, ref. 47) for the benchmark dataset.
- Cites Zhang et al. 2023 *Nature* (ref. 22) for the multiome spatial epigenome-transcriptome dataset.
- Compares against STAGATE (Dong & Zhang 2022, ref. 32), BayesSpace (Zhao 2021, ref. 28), DR-SC (Liu 2022, ref. 29), SEDR (Fu 2021, ref. 31), SOTIP (Yuan 2022, ref. 36), UTAG (Kim 2022, ref. 34), SpaGCN (Hu 2021, ref. 30), SpatialPCA (Shang & Zhou 2022, ref. 35), SPACE-GM (Wu 2022, ref. 33).
- Cites Tavernari et al. 2021 *Cancer Discov.* (ref. 11) as part of the LUAD survival meta-analysis.

### Mechanistic hypotheses proposed

- "Our results hence suggest a positive feedback between these interacting cells promoting cancer cell state transition." (Discussion, p.82) — hypothesised feedback among tumour hypoxia, HIF1α-driven chemokine release, TAN recruitment, and EMT.

### Caveats and self-criticism

- Authors note that spatially resolved cohorts are still limited in size and number of markers, restricting generalisability of the niche claim to larger cohorts and other tumour types.
- Acknowledge that anticipating which spatial technologies will dominate is uncertain — design decisions for CellCharter aim at being technology-agnostic but the field is fast-moving.

### Future directions suggested

- Integration with hematoxylin-and-eosin / histology features through deep neural networks pre-trained on large pathology corpora.
- Application to additional spatial multiome platforms (epigenetic features, copy-number, chromatin accessibility, multimodal profiles).
- Use of CellCharter-defined niches as prognostic markers in digital pathology / clinical decision-making.
- Functional and prognostic exploration of cell-type admixing as a distinct feature from cell-type composition.

## Limitations

- Method-side: analytical NE inherits null-model assumptions; cluster-shape descriptors require robust boundary estimates; multimodal VAEs require per-modality engineering.
- Biology-side: TAN-hypoxia niche validation rests on 5 CosMx + 2 MERFISH patients plus IMC TMA — no genetic / pharmacological perturbation.
- Survival analyses are bulk-transcriptomic — cannot directly measure niche colocalisation in the survival cohorts.
- LUSC is represented by one sample; the niche's generalisation beyond LUAD is not established.

## Open questions

### Open questions raised by authors

- How will CellCharter perform on multimodal spatial datasets at the cohort level?
- Could spatial niches predict immunotherapy response, and what is the prognostic value of cell-type admixing vs composition?

### Open questions identified during ingest

- Therapeutic targetability of the TAN-hypoxia niche (HIF1α inhibition with PX-478 / belzutifan, CXCR1/2 antagonism).
- Whether the hierarchical n=3/8/20 stable solutions generalise to other tumour cohorts.
- Robustness of analytical-NE false-positive rate vs permutation-NE.

## My take

CellCharter is a strong methodological contribution that gives a scalable, technology-agnostic, scverse-compatible alternative to STAGATE / BayesSpace for joint multi-sample spatial clustering. The most decision-relevant biology output for this wiki is the TAN + hypoxia + EMT spatial niche in LUAD — a recurrent observation across CosMx, MERFISH, IMC, and 9 bulk-transcriptomic LUAD cohorts — which provides a high-confidence linkage between local tumour hypoxia and the neutrophil-driven inflammatory state that anchors poor prognosis. Useful both as a methods anchor for the spatial-niche detection topic and as a biology anchor for hypoxia → EMT / immune-recruitment crosstalk in LUAD.

## Related

- [[concepts/tan-hypoxia-tumor-niche-luad]]
- [[concepts/cluster-neighborhood-enrichment-spatial]]
- [[concepts/cluster-shape-analysis-spatial]]
- [[concepts/spatial-domain-detection-from-svg]]
- [[concepts/hypoxia-emt-lineage-plasticity-metastasis]]
- [[concepts/tam-recruitment-hypoxic-niche-chemokines]]
- [[foundations/cellcharter-framework]]
- [[foundations/fowlkes-mallows-index]]
- [[foundations/10x-visium-spatial-transcriptomics]]
- [[foundations/cosmx-spatial-transcriptomics]]
- [[foundations/merfish-imaging-spatial]]
- [[foundations/codex-multiplexed-imaging]]
- [[foundations/hif1a]]
- [[foundations/ndrg1]]
- [[foundations/mpo-myeloperoxidase]]
- [[foundations/atac-seq]]
- [[papers/systematic-benchmarking-computational-methods-identify-spatially]]
- [[papers/molecular-landmarks-tumor-hypoxia-across-cancer]]
- [[papers/hypoxia-driven-crosstalk-between-tumor-tumor]]

- [[papers/single-cell-spatial-transcriptomic-analysis-human]] — Restrepo et al. (*Nat Genet* 2026): MERFISH+Visium organ-wide human skin atlas with ten multicellular neighborhoods
