---
title: "Novae: a graph-based foundation model for spatial transcriptomics data"
slug: novae-graph-based-foundation-model-spatial
arxiv: ""
doi: "10.1038/s41592-025-02899-6"
pmid: ""
venue: "Nature Methods"
year: 2025
authors:
  - "Quentin Blampey"
  - "Hakim Benkirane"
  - "Nadège Bercovici"
  - "Kevin Mulder"
  - "Grégoire Gessain"
  - "Florent Ginhoux"
  - "Fabrice André"
  - "Paul-Henry Cournède"
first_author: "Quentin Blampey"
corresponding_author: "Quentin Blampey; Paul-Henry Cournède"

source_type: pdf
s2_id: ""
date_added: 2026-05-26
ingested_date: 2026-05-26
ingest_version: 1
last_reviewed:

importance: 4
tier: TIER_1
tags:
  - spatial-transcriptomics
  - foundation-model
  - graph-neural-network
  - self-supervised-learning
  - batch-effect-correction
  - multimodal
  - methods
keywords:
  - Novae
  - graph attention network
  - SwAV
  - optimal transport
  - prototypes
  - zero-shot inference
  - hierarchical spatial domains
  - panel-invariant embedding
  - H&E + spatial transcriptomics fusion
  - Hugging Face Hub
domain: "methods / spatial-transcriptomics / oncology"

tissue:
  - colon
  - breast
  - lung
  - liver
  - uterine
  - tonsil
  - prostate
  - ovarian
  - lymph_node
  - skin
  - brain
  - pancreas
  - bone_marrow
  - kidney
  - mouse_brain
  - mouse_femur
  - mouse_colon
  - whole_mouse
condition:
  - cancer
  - healthy
  - Alzheimer-like
species:
  - human
  - mouse
hypoxia_relevant: false
contains_immune_cells: true
contains_myeloid: true

techniques:
  - Xenium_spatial_transcriptomics
  - MERSCOPE_spatial_transcriptomics
  - CosMx_spatial_transcriptomics
  - CosMx_protein_assay
  - HE_imaging
  - graph_attention_network
  - SwAV_self_supervised
  - optimal_transport_sinkhorn
n_samples: "78 slides (pretraining), ~30M cells"
n_cells_total: "~30,000,000 (pretraining); benchmarks: 2 (breast) + 5 (colon) + 5 (synthetic) + 2 (mouse brain split) + 2 (Xenium lung) + 8 (HNSCC CosMx) + 2 (lymph node) + 6 (mouse brain longitudinal)"
integration_method: "Novae native batch correction (relaxed OT over shared prototypes)"

key_cell_types:
  - central memory CD4+ T cell (TCM)
  - plasma B cell
  - regulatory T cell (FOXP3+)
  - macrophage
  - multinucleated giant cell (MGC)
  - MGC-mononuclear phagocyte (MGC-MNP)
  - CD8+ T cell
  - endothelial cell
  - stromal cell
  - adipocyte
  - inflammatory monocyte
  - mature B cell (CD79+CR2+ germinal center)
key_markers:
  - FN1
  - COL1A1
  - TAPBP
  - PGR
  - CDH1
  - PTPRC
  - CD52
  - CD3E
  - FOXP3
  - CD4
  - CD8
  - CXCL12
  - CR2
  - CD79A
  - Neurod6
  - Trbc2
  - Slc17a7
key_pathways:
  - brain aging
  - hypoxia
  - lymphocyte chemotaxis (CXCL12)
  - tertiary lymphoid structure formation
  - tumour-associated macrophage immunosuppression

projects:
  - thesis
  - methods
priority: secondary
read_status: deep_read

hypoxiaverse_status: excluded
exclusion_reason: "Methods paper; hypoxia is not a central biological focus."
data_availability: "Pretrained model on Hugging Face Hub (MICS-Lab/novae). Code: https://github.com/MICS-Lab/novae. HNSCC CosMx proteomics dataset publicly released with this paper."

code_url: "https://github.com/MICS-Lab/novae"
cited_by: []
---

## Problem

Spatial transcriptomics across multiple slides, panels, and platforms (Xenium, MERSCOPE, CosMx) is hindered by (1) reliance on shared gene panels, (2) strong inter-slide batch effects, (3) dependence on external batch-correction (Harmony) and clustering (Leiden/mclust) tools, which become the runtime bottleneck on million-cell datasets, and (4) per-study retraining that prevents cross-cohort comparison. Existing spatial-clustering methods (STAGATE, GraphST, SpaceFlow, SEDR, NicheCompass) cannot be reused as a pretrained model across new tissues, panels, and platforms.

## Key idea

Novae is a graph-based foundation model for spatial transcriptomics. It uses a GATv2 graph-attention encoder that operates on local subgraphs of the cell-proximity graph; embeddings are projected onto a shared set of learnable prototypes; an optimal-transport-based swapped-assignment objective (adapted from SwAV) trains the model self-supervised and natively corrects batch effects across slides. Relaxed equipartition allows prototypes to remain unused per slide, preventing over-correction. The pretrained model — released on Hugging Face — supports zero-shot inference, fine-tuning, nested-hierarchical-resolution assignment without re-clustering, downstream SVG / pathway / trajectory analyses, and multimodal H&E integration via CONCH patch embeddings.

## Method

- Pretraining: 78 slides, ~30M cells, 18 tissues, three imaging-based platforms (Xenium, MERSCOPE, CosMx). Single A100 (40 GB), lazy on-the-fly subgraph sampling.
- Architecture: per-cell GATv2 graph-attention encoder over local subgraphs; panel-invariant cell-embedding layer; learnable prototype matrix; Sinkhorn-Knopp OT swapped assignment; swapped cross-entropy loss.
- Hierarchical domains: prototypes regrouped into user-chosen resolution via a vectorial mapping — no re-clustering required.
- Batch correction: relaxed-equipartition OT per mini-batch (mini-batch = one biological slide).
- Multimodal: optional CONCH H&E patch embedding fused via MLP with the graph embedding.
- Distribution: pretrained weights on Hugging Face Hub (`MICS-Lab/novae`); compatible with scverse / AnnData / SpatialData / Sopa.

## Results

- Benchmarks across breast (Xenium + MERSCOPE), colon (5 slides, 3 panels), and a 5-slide / 7-domain synthetic dataset: Novae beats STAGATE / GraphST / SpaceFlow / SEDR / Scanpy / NicheCompass on FIDE (continuity) and JSD (cross-slide homogeneity) in zero-shot and fine-tuning modes.
- Runtime: orders of magnitude faster than competitors at 6M cells (Fig. 3h); the Harmony + Leiden/mclust downstream is the dominant cost for competitors. Novae's batch correction + assignment runs in seconds.
- Robustness: stable spatial-domain assignments under 10x default vs Baysor segmentation (Fig. 4e); robust to node-shuffle / edge-length perturbations except at domain interfaces and stromal/sparse regions (Fig. 4f); performance drops sharply at ~60% degradation (Supp. Fig. 17).
- Multimodal: Novae + CONCH H&E achieves the highest FIDE on a Xenium 5k human-lung slide and resolves bronchus (D2032) and parenchyma (D2027) domains merged by Novae alone (Fig. 5d-e).
- HNSCC CosMx protein-assay: domain D492 colocalises TCM CD4+ T cells, plasma B cells, macrophages and overlaps H&E-annotated TLSs (Fig. 5a,c); D497 (FOXP3+ Treg + stromal) is significantly reduced in MGC+ patients (P=0.0028, Fig. 5b); macrophages are spatially further from D495 in MGC+ patients (P=0.0010).
- Lymph-node case study: reactive vs nondiseased PAGA graphs show germinal-center D500 going from 1 to 5 connected neighbours, and D500/D501 proportion inversion (Fig. 6a-d).
- Mouse brain longitudinal (6 slides, control vs TgCRND8 at 2.5/5.7/13.4/17.9 months): brain-aging pathway enriched in D494 (Neurod6-high) and D481 in 17.9-month TgCRND8 (Fig. 6f); SVG analysis recovers Neurod6 / Slc17a7 / Trbc2 (Fig. 6g).

## All claims (exhaustive)

- `[c01]` Novae is pretrained on ~30M cells / 18 tissues / 78 slides / 3 platforms and distributed on Hugging Face Hub (p.2540) "We trained Novae on a large dataset comprising 78 slides, representing nearly 30 million cells across 18 tissues and three different subcellular resolution technologies" — confidence: high — type: methodological — links: [[claims/novae-trained-30m-cells-18-tissues-foundation-model]] [[concepts/graph-based-foundation-model-spatial-transcriptomics]] [[foundations/huggingface-hub]] [[foundations/xenium-in-situ-spatial-transcriptomics]] [[foundations/merscope-vizgen]] [[foundations/cosmx-spatial-transcriptomics]]
- `[c02]` Novae performs zero-shot spatial-domain inference across new tissues, panels, and platforms (p.2542-2543) "Novae's design allows it to seamlessly integrate data from different platforms and gene panels without compromising performance" — confidence: high — type: methodological — links: [[claims/novae-zero-shot-cross-panel-cross-tissue-inference]] [[concepts/zero-shot-spatial-domain-inference]] [[concepts/graph-based-foundation-model-spatial-transcriptomics]]
- `[c03]` Novae natively corrects batch effects via shared prototypes and a relaxed optimal-transport swapped-assignment objective (p.2543) "Novae's batch-effect correction uses optimal transport to align spatial domains across slides; however, as different slides may contain spatial domains in varying proportions ... we relaxed the alignment objective by allowing a subset of prototypes to remain unused within each slide" — confidence: high — type: methodological — links: [[claims/novae-native-batch-correction-via-relaxed-ot-prototypes]] [[concepts/native-batch-effect-correction-via-prototypes]] [[foundations/optimal-transport-sinkhorn]] [[foundations/swav-self-supervised-framework]]
- `[c04]` Novae produces nested hierarchical spatial domains via prototype regrouping, switching resolution without re-clustering (p.2541) "it provides a nested organization of spatial domains for different resolutions" — confidence: medium — type: methodological — links: [[claims/novae-nested-hierarchical-spatial-domains-no-reclustering]] [[concepts/nested-hierarchical-spatial-domains]]
- `[c05]` Novae outperforms STAGATE/GraphST/SpaceFlow/SEDR/Scanpy on FIDE and JSD for multi-panel breast spatial transcriptomics (p.2542, Fig. 3b) "Figure 3b presents the results of this benchmark, highlighting a notable improvement in performance by Novae, even in the zero-shot case" — confidence: high — type: methodological — links: [[claims/novae-outperforms-stagate-graphst-spaceflow-sedr-breast]] [[concepts/fide-jsd-spatial-domain-metrics]] [[foundations/stagate-graph-attention-autoencoder]] [[foundations/graphst-spatial]] [[foundations/spaceflow-spatial]] [[foundations/sedr-spatial]]
- `[c06]` Novae outperforms STAGATE/GraphST/SpaceFlow/SEDR/Scanpy on FIDE and JSD for multi-panel colon spatial transcriptomics (p.2542, Fig. 3d) "again showing a superior performance by Novae in both zero-shot and fine-tuning modes" — confidence: medium — type: methodological — links: [[claims/novae-outperforms-stagate-graphst-spaceflow-sedr-colon]] [[concepts/fide-jsd-spatial-domain-metrics]]
- `[c07]` Novae achieves the highest ARI and FIDE on a 5-slide / 7-domain synthetic spatial transcriptomics benchmark (p.2543, Fig. 3f-g) "Novae outperformed the other methods, demonstrating higher ARI and FIDE scores with notably low s.d. in ARI" — confidence: high — type: methodological — links: [[claims/novae-best-ari-fide-synthetic-dataset]] [[foundations/nichecompass-spatial]]
- `[c08]` Novae is orders of magnitude faster than competitors on million-cell datasets by avoiding external Harmony/Leiden/mclust (p.2543) "using Harmony and Leiden can be slow, especially on large datasets of millions of cells. Indeed, this can take up to several days on 6 million cells, whereas Novae can perform these two operations in several seconds" — confidence: high — type: methodological — links: [[claims/novae-runtime-orders-magnitude-faster-large-datasets]] [[foundations/harmony-integration]] [[foundations/leiden-clustering]] [[foundations/mclust-r]] [[foundations/scanpy]]
- `[c09]` Novae's lazy subgraph loading bounds GPU VRAM to model + mini-batch size, independent of dataset size (p.2545) "the maximum video-random-access-memory (VRAM) required by a GPU is the model size (128 MB for our current model on Hugging Face) and one mini-batch of graphs that is generated on the fly (between 2 MB and 20 MB depending on hyperparameters)" — confidence: high — type: methodological — links: [[claims/novae-lazy-loading-gpu-vram-bounded-not-dataset-size]] [[concepts/subgraph-local-microenvironment-encoding]]
- `[c10]` Novae spatial-domain assignments are robust to cell segmentation method (10x default vs Baysor) (p.2545, Fig. 4e) "demonstrating that Novae consistently identifies the same spatial domains despite methodological differences in the segmentation" — confidence: medium — type: methodological — links: [[claims/novae-robust-to-segmentation-baysor-vs-10x]] [[foundations/baysor-segmentation]]
- `[c11]` Novae outputs are robust to input-graph perturbations (node shuffle, edge-length drop) with errors concentrated at domain interfaces and stromal/sparse regions (p.2545, Fig. 4f) "we observe that node shuffling primarily affects domain interfaces, while edge-length reduction impacts mostly stromal and sparse regions" — confidence: medium — type: methodological — links: [[claims/novae-robust-to-node-shuffle-edge-length-perturbation]]
- `[c12]` Novae's relaxed-OT batch correction simultaneously avoids over- and under-correction in the missing-domain benchmark (p.2545, Fig. 4b,d) "Novae achieves both a high FIDE score (indicating domain continuity) and a low post-split JSD (indicating that Novae is not overcorrecting)" — confidence: high — type: methodological — links: [[claims/novae-relaxed-ot-avoids-over-and-under-correction]] [[concepts/fide-jsd-spatial-domain-metrics]] [[concepts/batch-removal-vs-bioconservation-tradeoff]]
- `[c13]` Novae recovers similar spatial-domain distributions across lymphoid tissues (tonsil/lymph node) and across cross-tissue cancer-related domains (p.2542, Fig. 2) "the lymph node and tonsil exhibited similar spatial domain distributions, with some domains also observed in other tissues such as breast and lung" — confidence: medium — type: correlational — links: [[claims/novae-recovers-similar-spatial-domains-tonsil-lymph-node]]
- `[c14]` Novae + CONCH multimodal fusion achieves the highest FIDE on a human-lung Xenium 5k slide and resolves bronchus / parenchyma domains (p.2546, Fig. 5d-e) "the fused Novae + CONCH model achieves the highest FIDE score, indicating improved performance through multimodal integration ... the combination of Novae and CONCH enables the separation of domains D2032 and D2027, whereas Novae alone merges them" — confidence: high — type: methodological — links: [[claims/novae-multimodal-conch-he-fusion-best-fide-lung]] [[concepts/multimodal-he-spatial-transcriptomics-fusion]] [[foundations/conch-pathology-foundation-model]]
- `[c15]` In CosMx HNSCC, Novae domain D492 colocalises TCM CD4+ T cells, plasma B cells and macrophages, overlapping H&E-annotated TLSs in MGC+ patients (p.2546) "domain D492 (enriched in B cells, plasma cells and macrophages) closely overlaps with lymphoid aggregates, which compose, among others, tertiary lymphoid structures (TLSs)" — confidence: medium — type: correlational — links: [[claims/novae-d492-tls-tcm-plasma-b-cells-mgc-hnscc]]
- `[c16]` FOXP3+ Treg-enriched stromal-like Novae domain D497 is significantly reduced in MGC-positive HNSCC patients (P=0.0028) (p.2546, Fig. 5b) "Novae identified a significant reduction in domain D497 in patients who were MGC-positive ... a region characterized by a stromal-like environment enriched in FOXP3 T cells (regulatory T (Treg) cells)" — confidence: high — type: quantitative — links: [[claims/novae-d497-foxp3-treg-stromal-niche-reduced-mgc]]
- `[c17]` Reactive lymph node shows reorganisation of germinal-center domain D500 connectivity (5 vs 1) and D500/D501 proportion inversion (p.2547, Fig. 6a-d) "the D500 domain in the germinal center ... is connected only to the D501 domain on the nondiseased slide, contrary to the reactive one, which is highly connected to five domains" — confidence: medium — type: correlational — links: [[claims/novae-d500-d501-germinal-center-rewiring-reactive-lymph-node]] [[foundations/paga-trajectory]]
- `[c18]` In TgCRND8 Alzheimer-like mouse brain, brain-aging pathway is enriched in Novae spatial domains D494 (Neurod6-high) and D481 (p.2548, Fig. 6f) "the 17.9-month-old TgCRND8 mouse, which exhibits Alzheimer's-like pathology, shows higher brain aging, particularly in specific spatial domains such as D494 and D481" — confidence: medium — type: correlational — links: [[claims/novae-d494-d481-aging-pathway-enriched-tgcrnd8-alzheimer]]
- `[c19]` Novae spatial-domain grouping identifies Neurod6, Slc17a7, and Trbc2 as top spatially variable genes in 2.5-month control mouse brain (p.2548, Fig. 6g) "In Fig. 6g, we demonstrate this for the 2.5-month control mouse, showing the three most SVGs identified by Novae" — confidence: medium — type: methodological — links: [[claims/novae-svg-detection-mouse-brain-neurod6-trbc2-slc17a7]] [[concepts/spatially-variable-gene-detection]]
- `[c20]` Novae's performance drops sharply at ~60% slide degradation (cell + gene-expression loss) (p.2548, Supp. Fig. 17) "the degradation benchmark revealed a performance drop when approximately 60% of cells and gene expression were lost" — confidence: medium — type: quantitative — links: [[claims/novae-degradation-benchmark-performance-drop-at-60-percent-cells-lost]]

## Discussion captured

### Authors' interpretation

- Authors interpret Novae as the first general-purpose foundation model for spatial transcriptomics: a single pretrained graph encoder that (a) operates across panels / tissues / platforms, (b) integrates batch-effect correction inside the model rather than as a post hoc Harmony step, and (c) is faster than competitors despite being a larger model — because Harmony + Leiden/mclust are the actual bottleneck.
- They frame the prototype-based design as enabling cross-cohort spatial comparisons that are otherwise inaccessible, with implications for biomarker discovery (e.g., MGC-stratified HNSCC immune niches).

### Comparisons with prior literature (made by authors)

- Compares against STAGATE (Dong & Zhang 2022), GraphST (Long et al. 2023), SpaceFlow (Ren et al. 2022), SEDR (Xu et al. 2024), NicheCompass (Birk et al. 2025), Scanpy (Wolf et al. 2018) as the spatial-clustering baselines.
- Builds on SwAV (Caron et al. 2020), GATv2 (Brody et al. 2022), optimal transport (Cuturi 2013; Peyré & Cuturi 2019).
- Cites Bommasani et al. 2021 (foundation models) and Hao et al. 2024 (scFoundation) for the foundation-model framing.
- Cites Gessain et al. 2024 Cancer Discov. (ref 35) for the HNSCC MGC biology underlying the CosMx Protein Assays case study.
- Cites Janesick et al. 2023 (Xenium), Chen et al. 2015 (MERFISH), He et al. 2022 (CosMx) for platforms.
- Cites Blampey et al. 2024 (Sopa), Marconato et al. 2025 (SpatialData), Virshup et al. 2023/2024 (scverse / AnnData) for the upstream ecosystem.
- Cites Lu et al. (CONCH) ref 42 for the H&E pathology foundation model.
- Cites Petukhov et al. 2022 (Baysor) for the alternative segmentation pipeline.
- Cites André et al. 2024 Nature (ref 26) for the tumour-naming reform motivating cross-tissue domain analysis.

### Mechanistic hypotheses proposed

- Cancer-related spatial domains shared across breast and lung tumour slides may reflect a tissue-agnostic tumour microenvironment state (e.g., hypoxic / immunosuppressive niches) — partially supported by D503 expansion in breast Xenium suggesting clonal cancer expansion within immune-excluded D485 stroma.
- D492 in HNSCC may represent a coordinated TCM-CD4+ + plasma-B + macrophage response anchored by TLSs, linking favourable prognosis in MGC+ patients to TLS-driven adaptive immunity.

### Caveats and self-criticism

- Pretrained Novae weights rely exclusively on spatial transcriptomics — the absence of large-scale paired multimodal datasets (ST + proteomics + H&E) prevents true multimodal pretraining.
- ~60% cell/gene-expression loss in the degradation benchmark causes a performance drop.
- Cell-centroid input limits representation of axonal / dendritic / non-blob structures.
- Synthetic-data benchmark excludes zero-shot Novae and NicheCompass.

### Future directions suggested

- Mixture-of-experts to unify spot-resolution (Visium) and single-cell-resolution data within a single foundation model.
- Expanding training-corpus tissues, panels, and modalities to improve generalisability and robustness to missing data domains.
- Joint multimodal pretraining once paired ST + proteomics + H&E corpora become available.
- Updating the input graph to accommodate emerging segmentations of complex structures (axons, dense epithelium).

## Limitations

- Pretrained weights exclude NGS-based platforms (Visium) and spatial proteomics; only imaging-based ST in pretraining.
- ~60% degradation breaking point in the robustness benchmark.
- Benchmark fairness — comparators must intersect gene panels, which structurally disadvantages them.
- Lymph node / HNSCC / Alzheimer mouse case studies use small cohorts; observations are descriptive.
- Cell-centroid input — cannot represent complex extended structures (axons).
- Multimodal H&E experiments are restricted to one slide.

## Open questions

### Open questions raised by authors

- How to extend the foundation model to NGS-based platforms (Visium) and to genuine multimodal pretraining?
- Can mixture-of-experts unify spot and single-cell resolutions?
- How to update the input graph for complex tissue structures (axons, sparse epithelium)?

### Open questions identified during ingest

- Calibration of FIDE/JSD across tissue density extremes.
- Out-of-distribution generalisation to unseen tissues / panels / proteomics modalities.
- Whether prototypes can be safely shared across modalities (transcriptomics + proteomics + H&E).
- Therapeutic relevance of D497 reduction and D492 TLS niche in larger HNSCC cohorts.

## My take

Novae is a strong methodological contribution — the first credible foundation-model entry for spatial transcriptomics, with a clean technical story (SwAV adapted to GATv2 over local subgraphs, with relaxed OT for native batch correction). The most decision-relevant outputs for this wiki are (1) the foundation-model framing for spatial omics, which sits alongside scFoundation/scGPT on the scRNA-seq side and creates space for ΩmegaWiki entries on cross-platform / cross-panel pretraining and (2) the HNSCC MGC-stratified Treg/D497 result, which connects to wider TME-immune-niche literature already in the wiki ([[concepts/immune-rich-vs-immune-poor-niches-nsclc]], [[concepts/cxcl13-cxcr5-tls-recruitment]]). Practical caveat: benchmarks against comparators forced into panel intersection structurally favour Novae — the more interesting comparison would be against alternative methods retrofitted with panel-invariant front-ends.

## Related

- [[concepts/graph-based-foundation-model-spatial-transcriptomics]]
- [[concepts/zero-shot-spatial-domain-inference]]
- [[concepts/native-batch-effect-correction-via-prototypes]]
- [[concepts/nested-hierarchical-spatial-domains]]
- [[concepts/subgraph-local-microenvironment-encoding]]
- [[concepts/multimodal-he-spatial-transcriptomics-fusion]]
- [[concepts/fide-jsd-spatial-domain-metrics]]
- [[concepts/spatial-domain-detection-from-svg]]
- [[concepts/spatially-variable-gene-detection]]
- [[concepts/batch-removal-vs-bioconservation-tradeoff]]
- [[concepts/atlas-level-data-integration]]
- [[foundations/swav-self-supervised-framework]]
- [[foundations/graph-attention-network-gatv2]]
- [[foundations/optimal-transport-sinkhorn]]
- [[foundations/xenium-in-situ-spatial-transcriptomics]]
- [[foundations/merscope-vizgen]]
- [[foundations/cosmx-spatial-transcriptomics]]
- [[foundations/10x-visium-spatial-transcriptomics]]
- [[foundations/scanpy]]
- [[foundations/leiden-clustering]]
- [[foundations/mclust-r]]
- [[foundations/harmony-integration]]
- [[foundations/stagate-graph-attention-autoencoder]]
- [[foundations/graphst-spatial]]
- [[foundations/spaceflow-spatial]]
- [[foundations/sedr-spatial]]
- [[foundations/nichecompass-spatial]]
- [[foundations/baysor-segmentation]]
- [[foundations/conch-pathology-foundation-model]]
- [[foundations/paga-trajectory]]
- [[foundations/sopa-pipeline]]
- [[foundations/spatialdata-framework]]
- [[foundations/huggingface-hub]]
- [[foundations/cellcharter-framework]]
- [[papers/cellcharter-reveals-spatial-cell-niches-associated]]
- [[papers/systematic-benchmarking-computational-methods-identify-spatially]]
- [[papers/identifying-spatial-single-cell-level-interactions]] — News & Views on GITIII; graph-based deep learning on spatial-transcriptomics neighbourhoods (similar method family).
