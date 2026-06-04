---
# === Identification ===
title: "Hypoxic stress dysregulates functions of glioma-associated myeloid cells through epigenomic and transcriptional programs"
slug: "hypoxic-stress-dysregulates-functions-glioma-associated"
arxiv: ""
doi: "10.1016/j.celrep.2025.116222"
pmid: ""
venue: "Cell Reports"
year: 2025
authors: ["Monika Dzwigonska", "Patrycja Rosa", "Szymon Lipiec", "Tomasz Obrebski", "Gabriela Smyk", "Beata Kaza", "Salwador Cyranowski", "Aleksandra Ellert-Miklaszewska", "Agata Kominek", "Anna R. Malik", "Katarzyna Piwocka", "Jakub Mieczkowski", "Bozena Kaminska", "Katarzyna B. Leszczynska"]
first_author: "Monika Dzwigonska"
corresponding_author: "Katarzyna B. Leszczynska"

# === Source & metadata ===
source_type: pdf
s2_id: ""
date_added: 2026-06-04
ingested_date: 2026-06-04
ingest_version: 1
last_reviewed:

# === Classification ===
importance: 4
tier: TIER_1
tags: [hypoxia, glioma, glioblastoma, glioma-associated-macrophages, microglia, myeloid-cells, epigenomics, chromatin-accessibility, ATAC-seq, H3K27ac, HDAC, lipid-droplets, tumor-microenvironment, galectin-3, P2RY12, TMEM119]
keywords: [GAMs, hypoxia, LGALS3, P2RY12, TMEM119, GPNMB, ATAC-seq, CUT&RUN, H3K27ac, panobinostat, lipid-droplets, HIF, SPI1, IRF8, AP1, ATF3, co-culture, GL261, BV2]
domain: "oncology / immunology / epigenetics"

# === Biomedical domain ===
tissue: [brain, in_vitro_only]
condition: [cancer]
disease_specific: [glioblastoma]
species: [mouse, human]
hypoxia_relevant: true
contains_immune_cells: true
contains_myeloid: true

# === Technique ===
techniques: [bulk_RNA-seq, ATAC-seq, CUT&RUN, scRNA-seq_10x, qPCR, immunoblot, immunofluorescence, CODEX, flow_cytometry, BODIPY_lipid_staining, Matrigel_invasion_assay]
n_samples:
n_cells_total:
integration_method: ""

# === Biology captured ===
key_cell_types: [microglia, glioma-associated-macrophages, monocyte-derived-macrophages, BV2_microglia, RAW264.7_macrophages, BMDM, GL261_glioma]
key_markers: [LGALS3, P2RY12, TMEM119, GPNMB, GLUT1, VEGFA, PLIN2, PLIN3, HILPDA, SOAT1, OLFML3]
key_pathways: [HIF_signaling, chromatin_accessibility_remodeling, H3K27ac_acetylation, HDAC_activity, lipid_storage_metabolism, SPI1-IRF8_microglial_identity, AP1-ATF3_signaling]

# === User project membership ===
projects: [thesis, hypoxia]
priority: core
read_status: read

# === HypoxiaVERSE-specific ===
hypoxiaverse_status:
exclusion_reason:
data_availability: "GEO: GSE300330 (RNA-seq, ATAC-seq, CUT&RUN)"

# === Cross-references ===
code_url: ""
cited_by: []
---

## Problem

Hypoxia is a defining histopathological feature of glioblastoma (GBM), associated with aggressiveness and therapy resistance. Glioma-associated microglia/macrophages (GAMs) dominate the GBM microenvironment and acquire immunosuppressive, tumor-supportive states. Single-cell studies classify GAMs (Mg-GAMs vs Mo/Mφ-GAMs and functional subtypes) using marker genes, but many of those markers are environmentally labile. Whether — and how — hypoxia itself reprograms GAM identity and function, and whether it confounds marker-based GAM classification, was poorly defined.

## Key idea

Hypoxia is a strong intratumoral, epigenomic regulator of myeloid cell identity and function. It dysregulates the very markers used to distinguish GAM subtypes (up: LGALS3; down: P2RY12, TMEM119) regardless of cell lineage, reshapes chromatin accessibility at myeloid identity-gene promoters, and drives a lipid-laden phenotype through loss of histone H3K27 acetylation — which is reversible with an HDAC inhibitor (panobinostat).

## Method

- **Cells/models**: mouse BV2 microglia, RAW264.7 and primary BMDM macrophages, GL261-GFP glioma; direct microglia–glioma co-culture (CC) under controlled oxygen (<0.1% O₂ hypoxia vs 21% normoxia), 2×2 design (±glioma, ±hypoxia), FACS isolation of CD45⁺ myeloid cells; glyoxal fixation to prevent reoxygenation artifacts.
- **Genomics**: bulk RNA-seq (BV2, BMDM, GL261), fixed-cell ATAC-seq, CUT&RUN for H3K27ac; HOMER/FIMO TF-motif analysis; HIF metagene (Lombardi et al.); GAM-cluster marker sets and a combined "hypoxia score" from Wang and Antunes scRNA-seq datasets (GSE163120).
- **In vivo/clinical**: public mouse and human GBM scRNA-seq; IvyGAP anatomic regional expression; CODEX multiplex imaging of an 80-sample human GBM TMA.
- **Functional/pharmacological**: qPCR, western blot, immunofluorescence (H3K27me3/H3K9me3), Matrigel invasion assay, phagocytosis assay, BODIPY lipid-droplet quantitation, pan-HDAC inhibitor panobinostat (10 nM), CoCl₂ hypoxia mimetic.

## Results

Hypoxia upregulates LGALS3 and downregulates P2RY12/TMEM119 in all tested myeloid cells and reproduces this with CoCl₂; the pattern holds in vivo (mouse/human GBM scRNA-seq hypoxia-score correlations, IvyGAP perinecrotic regions, and CODEX on human GBM). In co-culture, hypoxia dominates the microglial transcriptome (thousands of DEGs) while glioma contact dominates chromatin accessibility; combined exposure remodels promoters most. Hypoxia broadly shifts GAM subtype programs (IFN/ribosomal down; phagocytic/chemotactic up; lipid-storage up) and increases BMDM phagocytosis and glioma invasion. RNA and ATAC changes are only ~24% concordant. Mechanistically, the P2ry12 promoter loses accessibility at an SPI1/IRF8 peak while the Lgals3 promoter gains an AP1/ATF3 peak. Hypoxia raises repressive H3K27me3/H3K9me3 and globally lowers H3K27ac; lipid-storage genes and lipid droplets increase; panobinostat restores H3K27ac, rescues TMEM119, blocks LGALS3 induction, and reduces lipid droplets.

## All claims (exhaustive)

- `[c1]` Hypoxia upregulates Lgals3 (galectin-3) in microglia and macrophages (p.3) "In all three cell types, hypoxic conditions (<0.1% O2) induced upregulation of Lgals3 at the mRNA and protein levels, along with known hypoxia-induced genes vascular endothelial growth factor A (Vegfa) and glucose transporter protein type 1 (Glut1)" — confidence: high — type: mechanistic — links: [[claims/hypoxia-upregulates-lgals3-microglia-macrophages]] [[concepts/hypoxia-confounds-gam-subtype-marker-classification]] [[foundations/galectin-3]] [[foundations/hif1a]] [[foundations/vegf]] [[foundations/bv2-microglial-cell-line]] [[foundations/bone-marrow-derived-macrophage-bmdm]]
- `[c2]` Hypoxia downregulates microglial markers P2ry12 and Tmem119 across myeloid cells (p.3) "the expression of microglial markers Tmem119 and P2ry12 was significantly downregulated ... was detected in RAW 264.7 and BMDM cells, and was suppressed by hypoxia" — confidence: high — type: mechanistic — links: [[claims/hypoxia-downregulates-microglial-markers-p2ry12-tmem119]] [[concepts/hypoxia-confounds-gam-subtype-marker-classification]] [[foundations/p2ry12-purinergic-receptor-microglial-marker]] [[foundations/tmem119-transmembrane-protein-119-microglial-marker]]
- `[c3]` CoCl2 hypoxia mimetic reproduces hypoxic dysregulation of Lgals3/P2ry12/Tmem119 (p.3) "Both the mild hypoxia and CoCl2 increased Lgals3 expression at both mRNA and protein levels ... both mild hypoxia and CoCl2 decreased their expression" — confidence: medium — type: pharmacological — links: [[claims/cocl2-hypoxia-mimetic-reproduces-hypoxic-dysregulation]] [[foundations/hif1a]] [[foundations/phd-prolyl-hydroxylases]] [[foundations/galectin-3]]
- `[c4]` Hypoxia score positively correlates with Lgals3 and negatively with P2ry12/Tmem119 in GBM TAMs (p.5) "a statistically significant positive correlation between the hypoxia score and Lgals3 and a negative correlation with Tmem119 and P2ry12 in TAMs, especially in Mg-TAMs" — confidence: medium — type: correlational — links: [[claims/hypoxia-score-positively-correlates-lgals3-negatively]] [[concepts/gam-hypoxia-score-transcriptomic-signature]] [[concepts/hypoxia-confounds-gam-subtype-marker-classification]] [[foundations/scrna-seq-10x-chromium]] [[foundations/galectin-3]]
- `[c5]` LGALS3 highest and TMEM119/P2RY12 lowest in hypoxic perinecrotic GBM regions (p.5) "LGALS3 expression was highest in the perinecrotic and pseudopalisading regions (CTpnz and CTpcan), similar to classic hypoxia markers SLC2A1 or VEGFA ... TMEM119 and P2RY12 expression was lowest in these hypoxic areas" — confidence: medium — type: correlational — links: [[claims/lgals3-highest-tmem119-p2ry12-lowest-hypoxic]] [[concepts/hypoxia-confounds-gam-subtype-marker-classification]] [[foundations/ivygap-ivy-glioblastoma-atlas-project]] [[foundations/galectin-3]] [[foundations/vegf]]
- `[c6]` Hypoxia is the dominant driver of the microglial transcriptome over glioma contact (p.5) "Hypoxia imposed stronger sample separation (along PC1) compared to the CC effect (along PC2) ... 2605 upregulated and 1942 downregulated genes (CC_H versus CC_N)" — confidence: high — type: quantitative — links: [[claims/hypoxia-dominant-driver-microglial-transcriptome-over]] [[concepts/direct-glioma-microglia-co-culture-under]] [[foundations/bv2-microglial-cell-line]] [[foundations/gl261-mouse-glioma-cell-line]]
- `[c7]` Hypoxia and glioma co-culture upregulate axon development pathways in microglia (p.5) "hypoxia also upregulated genes from axon development, axon guidance, or tissue morphogenesis pathways in BV2 cells" — confidence: medium — type: correlational — links: [[claims/hypoxia-glioma-co-culture-upregulate-axon]] [[concepts/direct-glioma-microglia-co-culture-under]] [[foundations/bv2-microglial-cell-line]]
- `[c8]` Hypoxia represses ribosome biogenesis and RNA processing genes in microglia (p.5) "downregulated genes under hypoxia in BV2 CCs were associated with pathways previously reported as repressed by hypoxia, including ribosomal biogenesis, RNA processing, or DNA replication" — confidence: high — type: correlational — links: [[claims/hypoxia-represses-ribosome-biogenesis-rna-processing]] [[foundations/bv2-microglial-cell-line]]
- `[c9]` Hypoxia represses IFN/transitory/ribosomal GAM markers and induces phagocytic/chemotactic markers (p.6) "Markers of IFN, transitory and ribo-GAMs were predominantly downregulated, while phagocytic and chemotactic GAM genes were upregulated by hypoxia" — confidence: high — type: mechanistic — links: [[claims/hypoxia-represses-ifn-ribosomal-gam-markers]] [[concepts/hypoxia-confounds-gam-subtype-marker-classification]] [[foundations/bone-marrow-derived-macrophage-bmdm]]
- `[c10]` Hypoxia increases phagocytosis in bone marrow-derived macrophages (p.6) "We confirmed increased phagocytosis in BMDMs upon hypoxia and lipopolysaccharide (LPS) stimulation, supporting the functional relevance of the observed transcriptomic changes" — confidence: high — type: mechanistic — links: [[claims/hypoxia-increases-phagocytosis-bone-marrow-derived]] [[foundations/bone-marrow-derived-macrophage-bmdm]] [[foundations/lps-toll-like-receptor-signaling]]
- `[c11]` Promoters of hypoxia-induced myeloid genes are enriched for HIF/RUNX/NF-κB/AP1 motifs (p.6) "hypoxia-upregulated genes also showed enrichment for MYC associated factor X (MAX), runt-related transcription factor (RUNX), nuclear factor κB (NF-κB), activator protein-1 (AP1)" — confidence: medium — type: methodological — links: [[claims/promoters-hypoxia-induced-myeloid-genes-enriched]] [[concepts/hypoxia-chromatin-remodeling-myeloid-identity-gene]] [[foundations/hif1a]] [[foundations/hif2a]] [[foundations/nf-kb-p65-rela]] [[foundations/fos-transcription-factor]] [[foundations/homer-motif-enrichment-analysis]]
- `[c12]` Microglia under hypoxia enhance glioma cell migration and invasion (p.6) "The most efficient transmigration occurred when glioma cells were exposed to both hypoxia and microglia" — confidence: medium — type: mechanistic — links: [[claims/microglia-under-hypoxia-enhance-glioma-cell]] [[foundations/gl261-mouse-glioma-cell-line]] [[foundations/bv2-microglial-cell-line]]
- `[c13]` Hypoxia globally increases repressive H3K27me3 and H3K9me3 in microglia and glioma (p.6) "Hypoxia globally increased histone 3 (H3) lysine 27 trimethylation (H3K27me3) or H3 lysine 9 trimethylation (H3K9me3) marks in both glioma and BV2 cells" — confidence: high — type: mechanistic — links: [[claims/hypoxia-globally-increases-repressive-h3k27me3-h3k9me3]] [[foundations/h3k27me3-histone-trimethylation-mark]] [[foundations/bv2-microglial-cell-line]]
- `[c14]` Glioma co-culture remodels microglial chromatin accessibility more than hypoxia alone (p.8) "CC with glioma cells had a stronger effect on BV2 chromatin accessibility (PC1 axis) than hypoxia (PC2 axis)" — confidence: high — type: quantitative — links: [[claims/glioma-co-culture-remodels-microglial-chromatin]] [[concepts/hypoxia-chromatin-remodeling-myeloid-identity-gene]] [[concepts/direct-glioma-microglia-co-culture-under]] [[foundations/atac-seq]] [[foundations/bv2-microglial-cell-line]]
- `[c15]` Hypoxia alone reduces promoter accessibility while glioma+hypoxia increases promoter openness (p.10) "hypoxia alone reduces promoter accessibility, whereas the combined glioma presence and hypoxia increase promoter openness in hypoxic BV2 cells" — confidence: high — type: mechanistic — links: [[claims/hypoxia-alone-reduces-promoter-accessibility-while]] [[concepts/hypoxia-chromatin-remodeling-myeloid-identity-gene]] [[foundations/atac-seq]]
- `[c16]` HIF-inducible genes gain accessibility at genic, not promoter-only, peaks under hypoxia (p.10) "non-promoter peaks were particularly induced in HIF-target genes ... HIF-1A and HIF-2A enrichment only in genic but absent from promoter-only regions" — confidence: medium — type: mechanistic — links: [[claims/hif-inducible-genes-gain-accessibility-genic]] [[concepts/hypoxia-chromatin-remodeling-myeloid-identity-gene]] [[foundations/hif1a]] [[foundations/hif2a]] [[foundations/atac-seq]]
- `[c17]` RNA and ATAC-seq changes are only partially concordant in hypoxic microglia (p.10) "The Spearman and Pearson correlation coefficients (0.24) for ATAC-seq peaks and gene expression indicated a partial but significant correlation" — confidence: high — type: quantitative — links: [[claims/rna-atac-seq-changes-only-partially]] [[concepts/hypoxia-chromatin-remodeling-myeloid-identity-gene]] [[foundations/atac-seq]]
- `[c18]` P2ry12 promoter loses accessibility at a SPI1/IRF8 motif peak under hypoxic co-culture (p.12) "the ATAC-seq peak at the P2ry12 ... promoter was nearly lost in BV2 cells co-cultured with glioma under hypoxia. This peak contained motifs for Spi-1 ... (SPI1, encoding PU.1) and interferon regulatory factor 8 (IRF8)" — confidence: high — type: mechanistic — links: [[claims/p2ry12-promoter-loses-accessibility-spi1-irf8]] [[concepts/hypoxia-chromatin-remodeling-myeloid-identity-gene]] [[foundations/p2ry12-purinergic-receptor-microglial-marker]] [[foundations/spi1-pu1-master-tf]] [[foundations/irf8-interferon-regulatory-factor]]
- `[c19]` Spi1 expression decreases under hypoxia, contributing to P2ry12 downregulation (p.12) "Spi1 expression decreased in hypoxia in our RNA-seq data, potentially contributing to the downregulation of P2ry12" — confidence: medium — type: mechanistic — links: [[claims/spi1-expression-decreases-under-hypoxia-contributing]] [[foundations/spi1-pu1-master-tf]] [[foundations/p2ry12-purinergic-receptor-microglial-marker]]
- `[c20]` Lgals3 promoter gains accessibility at an AP1/ATF3 motif region under hypoxia (p.12) "At the Lgals3 promoter, the upregulated accessible chromatin region was enriched in binding motifs for AP1 and ATF3 motifs, both linked to tumor-supportive macrophage functions, including lipid metabolism" — confidence: high — type: mechanistic — links: [[claims/lgals3-promoter-gains-accessibility-ap1-atf3]] [[concepts/hypoxia-chromatin-remodeling-myeloid-identity-gene]] [[foundations/galectin-3]] [[foundations/fos-transcription-factor]] [[foundations/atf3-activating-transcription-factor]]
- `[c21]` Hypoxia upregulates lipid storage genes (Plin2, Plin3, Hilpda, Soat1) in GAMs (p.12) "Lipid storage-related genes were upregulated in both cell types (Lgals3, perilipin 2 [Plin2], Plin3, hypoxia inducible lipid droplet associated (Hilpda), and sterol O-acyltransferase 1 [Soat1])" — confidence: high — type: mechanistic — links: [[claims/hypoxia-upregulates-lipid-storage-genes-plin2]] [[concepts/hdac-h3k27ac-control-lipid-droplet-accumulation]] [[foundations/plin2-perilipin]] [[foundations/hilpda-hypoxia-inducible-lipid-droplet-associated]] [[foundations/galectin-3]]
- `[c22]` Hypoxia increases lipid droplet accumulation in GAMs (p.14) "lipid droplet (LD) levels in BV2 and BMDM monocultures using boron-dipyrromethene (BODIPY) staining and found them significantly increased under hypoxia" — confidence: high — type: mechanistic — links: [[claims/hypoxia-increases-lipid-droplet-accumulation-gams]] [[concepts/hdac-h3k27ac-control-lipid-droplet-accumulation]] [[foundations/bv2-microglial-cell-line]] [[foundations/bone-marrow-derived-macrophage-bmdm]]
- `[c23]` Hypoxia causes global loss of H3K27ac in microglia (p.14) "a global loss of histone acetylation ... H3 lysine 27 acetylation (H3K27ac) in BV2 cells and found it to be globally decreased in hypoxia" — confidence: high — type: mechanistic — links: [[claims/hypoxia-causes-global-loss-h3k27ac-microglia]] [[concepts/hdac-h3k27ac-control-lipid-droplet-accumulation]] [[foundations/h3k27ac-histone-acetylation-mark]] [[foundations/hdac-histone-deacetylase]] [[foundations/cut-run-cleavage-under-targets-release]]
- `[c24]` Pan-HDAC inhibitor panobinostat restores Tmem119 and blocks hypoxia-induced Lgals3 (p.14) "panobinostat, rescued expression of the hypoxia-repressed microglial marker Tmem119. Conversely, panobinostat impaired hypoxia-induced upregulation of Lgals3 mRNA and protein" — confidence: high — type: pharmacological — links: [[claims/pan-hdac-inhibitor-panobinostat-restores-tmem119]] [[concepts/hdac-h3k27ac-control-lipid-droplet-accumulation]] [[foundations/panobinostat-pan-hdac-inhibitor]] [[foundations/hdac-histone-deacetylase]] [[foundations/tmem119-transmembrane-protein-119-microglial-marker]] [[foundations/galectin-3]]
- `[c25]` Panobinostat reduces hypoxia-induced lipid droplet formation in GAMs (p.14) "Consistent with gene expression data, panobinostat impaired LD formation in hypoxia" — confidence: high — type: pharmacological — links: [[claims/panobinostat-reduces-hypoxia-induced-lipid-droplet]] [[concepts/hdac-h3k27ac-control-lipid-droplet-accumulation]] [[foundations/panobinostat-pan-hdac-inhibitor]]
- `[c26]` TMEM119 down and GPNMB up in GAMs within hypoxic human GBM regions (p.14) "predominant TMEM119 downregulation in GAMs within hypoxic areas (39 of 43 hypoxic cores) ... GPNMB ... specifically upregulated in GAMs present in hypoxic areas (32 of 43 hypoxic cores)" — confidence: medium — type: correlational — links: [[claims/tmem119-downregulated-gpnmb-upregulated-gams-within]] [[concepts/hypoxia-confounds-gam-subtype-marker-classification]] [[foundations/codex-multiplexed-imaging]] [[foundations/tmem119-transmembrane-protein-119-microglial-marker]] [[foundations/gpnmb-protein]] [[foundations/galectin-3]]

## Discussion captured

### Authors' interpretation

The authors interpret hypoxia as a master regulator of myeloid identity in GBM: tumor-hypoxia-driven chromatin reprogramming acts as a "master regulator" of identity-defining changes, upregulating tumor-supportive genes while downregulating homeostatic/neuroprotective genes and canonical microglial markers. They emphasize that most rapid gene-expression changes are likely driven by immediate TF activity (HIF-1α/2α, NF-κB, RUNX1, AP1), while chromatin reprogramming "fine-tunes" key myeloid genes (P2ry12/Olfml3 down; Lgals3/Gpnmb up). They stress that hypoxia confounds the markers used to distinguish tumor-infiltrating microglia from peripheral monocytes/macrophages, which may help resolve conflicting literature.

### Comparisons with prior literature (made by authors)

- Lipid-laden TAMs in hypoxic niches using myelin lipids to fuel glioma (Kloosterman et al. 2024, Cell; ref 11).
- GAM scRNA-seq subtype definitions (Ochocka et al. 2021 Nat Commun ref 6; Antunes et al. 2021 Nat Neurosci ref 7; Wang et al. 2024 Cancer Cell ref 5; Sankowski et al. 2024 ref 8).
- IRF8/SPI1 as microglial identity regulators (refs 48–50); SMAD2/3 TGFβ axis driving immunosuppression (refs 44, 46); GPNMB immunosuppression in glioma (Yalcin et al. 2024 ref 45).
- Hypoxia/HDAC links to histone acetylation loss (ref 54); hypoxia chromatin remodeling (Batie/Rocha, Chakraborty/KDM6A, Thienpont/TET; refs 33–37); their own DDX5/chromatin-accessibility work (Leszczynska et al. 2023 ref 30).
- HIF metagene from Lombardi et al. 2022 (ref 25).

### Mechanistic hypotheses proposed

- Glioma interaction and oxygen loss synergistically reduce chromatin accessibility at the P2ry12 promoter (PU.1/IRF8 sites) (p.14).
- AP1/ATF3 at the opened Lgals3 promoter, and TGFβ/SMAD at the Gpnmb promoter, drive the respective inductions (p.12).
- Hypoxia-induced HDAC activity lowers H3K27ac, promoting lipid storage; restoring acetylation reverses it (p.14).
- Non-concordant accessibility changes may reflect delayed expression effects or altered 3D chromatin structure (p.15).

### Caveats and self-criticism

The in vitro direct co-culture is simplified and excludes other TME components (astrocytes, endothelial cells, T cells, vasculature, 3D architecture). The proposed GAM hypoxia score "requires further development and validation across additional single-cell GAM datasets." Bulk regional (IvyGAP) signal may partly reflect cell-composition shifts rather than per-cell reprogramming. LGALS3 upregulation in hypoxic human GBM is not myeloid-restricted, limiting its use as a clean GAM marker.

### Future directions suggested

- Deeper epigenomic studies capturing chromatin conformation under hypoxia.
- Therapeutic targeting of hypoxia-induced epigenomic/transcriptomic alterations in GAMs (HDAC inhibition; LGALS3 in highly hypoxic tumors).
- Dissecting the glioma-contact × hypoxia co-regulation of the P2ry12 promoter.

## Limitations

- Simplified two-cell in vitro co-culture; lacks the full TME and 3D context.
- Cell-line–centric (BV2, GL261, RAW264.7), with primary BMDM and human-tissue validation but no in vivo perturbation.
- Pan-HDAC inhibition (panobinostat) is non-specific; the responsible HDAC isoform and direct target loci are unidentified.
- RNA–ATAC concordance is partial (~0.24), so chromatin remodeling explains only part of the transcriptional response.
- GAM hypoxia score derived from two GBM datasets; not yet broadly validated.

## Open questions

### Open questions raised by authors

- How do glioma contact and hypoxia synergize to close the P2ry12 promoter?
- What is the functional significance of accessibility changes that do not affect nearby gene expression (3D structure? timing?)?
- Can targeting hypoxia-induced epigenomic alterations (HDAC, LGALS3) therapeutically benefit hypoxic GBM?

### Open questions identified during ingest

- Which HDAC isoform mediates the hypoxic H3K27ac loss and lipid phenotype?
- Is the marker dysregulation HIF-dependent in microglia (genetic HIF1α/HIF2α tests)?
- Does a myeloid-specific hypoxia score generalize beyond glioma to other solid tumors (HypoxiaVERSE relevance)?
- Is GPNMB a more hypoxia-robust myeloid marker than LGALS3 in human tumors?

## My take

The strongest, most thesis-relevant contributions are (1) the demonstration that hypoxia confounds marker-based GAM classification — a methodological warning for any single-cell/spatial myeloid map of hypoxic tumors — and (2) the epigenomic mechanism: hypoxia closes the PU.1/IRF8-controlled P2ry12 promoter and opens the AP1/ATF3-controlled Lgals3 promoter, with a separable HDAC/H3K27ac axis controlling a reversible lipid-droplet phenotype. The HDAC-inhibitor reversal makes the hypoxic myeloid phenotype epigenetically targetable. The reductionist co-culture and pan-HDAC non-specificity temper causal claims, but the in vivo/CODEX validation gives it real footing. Directly applicable to hypoxia + macrophage epigenetics work.

## Related

- [[concepts/hypoxia-confounds-gam-subtype-marker-classification]]
- [[concepts/hypoxia-chromatin-remodeling-myeloid-identity-gene]]
- [[concepts/hdac-h3k27ac-control-lipid-droplet-accumulation]]
- [[concepts/direct-glioma-microglia-co-culture-under]]
- [[concepts/gam-hypoxia-score-transcriptomic-signature]]
- [[people/monika-dzwigonska]]
- [[people/bozena-kaminska]]
- [[people/katarzyna-leszczynska]]
