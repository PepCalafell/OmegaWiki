---
# === Identification ===
title: "JAK-STAT signaling maintains homeostasis in T cells and macrophages"
slug: jak-stat-signaling-maintains-homeostasis-cells
arxiv: ""
doi: "10.1038/s41590-024-01804-1"
pmid: ""
venue: "Nature Immunology"
year: 2024
authors: ["Nikolaus Fortelny", "Matthias Farlik", "Victoria Fife", "Anna-Dorothea Gorki", "Caroline Lassnig", "Barbara Maurer", "Katrin Meissl", "Marlies Dolezal", "Laura Boccuni", "Aarathy Ravi Sundar Jose Geetha", "Mojoyinola Joanna Akagha", "Anzhelika Karjalainen", "Stephen Shoebridge", "Asma Farhat", "Ulrike Mann", "Rohit Jain", "Shweta Tikoo", "Nina Zila", "Wolfgang Esser-Skala", "Thomas Krausgruber", "Katarzyna Sitnik", "Thomas Penz", "Anastasiya Hladik", "Tobias Suske", "Sophie Zahalka", "Martin Senekowitsch", "Daniele Barreca", "Florian Halbritter", "Sabine Macho-Maschler", "Wolfgang Weninger", "Heidi A. Neubauer", "Richard Moriggl", "Sylvia Knapp", "Veronika Sexl", "Birgit Strobl", "Thomas Decker", "Mathias Müller", "Christoph Bock"]
first_author: "Nikolaus Fortelny"
corresponding_author: "Matthias Farlik; Christoph Bock"

# === Source & metadata ===
source_type: pdf
s2_id: ""
date_added: 2026-05-22
ingested_date: 2026-05-22
ingest_version: 1
last_reviewed:

# === Classification ===
importance: 5
tier: TIER_1
tags: [jak-stat, homeostasis, interferon, ISGF3, STAT1, STAT2, IRF9, TYK2, STAT5BN642H, chromatin-accessibility, spatial-transcriptomics, immunology, epigenetics]
keywords: [JAK-STAT signaling, baseline/tonic IFN signaling, ISGF3 complex, STAT2-IRF9, STAT5BN642H neomorphic mutation, STAT1 isoforms, TYK2 kinase-independent, ex vivo context deprivation, RNA-seq, ATAC-seq, spatial transcriptomics]
domain: immunology

# === Biomedical domain ===
tissue: [spleen, in_vitro_only]
condition: [healthy]
disease_specific: []
species: [mouse]
hypoxia_relevant: false
contains_immune_cells: true
contains_myeloid: true

# === Technique ===
techniques: [bulk_RNA-seq, ATAC-seq, spatial_visium, RNA-FISH, flow_cytometry]
n_samples: 469
n_cells_total:
integration_method: ""

# === Biology captured ===
key_cell_types: [CD8_T_cell, macrophage, dendritic_cell, NK_cell, B_cell, splenocyte]
key_markers: [STAT1, STAT2, STAT3, STAT4, STAT5A, STAT5B, STAT6, IRF9, TYK2, Oas3, Ifit1, Ifit3, Oasl1, Mx1, Cd8a, Cd33, Cd3e, Cd14, Cd28, Gzmb, Gzmk, Klrg1, Mki67]
key_pathways: [JAK-STAT, type_I_IFN, ISGF3, GAS_ISRE_transcription, Aurora_kinase, cell_cycle, IL-2_signalling, IFN-beta_stimulation]

# === User project membership ===
projects: [thesis]
priority: core
read_status: read

# === HypoxiaVERSE-specific ===
hypoxiaverse_status:
exclusion_reason:
data_availability: "GEO GSE204736; supplementary website http://jakstat.bocklab.org; code Zenodo 10.5281/zenodo.10649062"

# === Cross-references ===
code_url: "https://doi.org/10.5281/zenodo.10649062"
cited_by: []
---

## Problem

JAK-STAT signaling is a canonical inducible pathway: cytokine receptors → JAK kinases → STAT phosphorylation → nuclear transcription of target genes. Yet immune cells must be permanently primed for response without active stimulation, and prior work hinted at low-level STAT1/STAT2 target expression under homeostatic conditions. Whether JAK-STAT signaling actively maintains the **homeostatic** transcriptional/epigenetic state — and which family members do so, in which cell types, under what extrinsic cue — was not systematically known. Knockouts of JAK kinases JAK1/JAK2/JAK3 are perinatally lethal, blocking direct loss-of-function dissection of the pathway in adult immune cells.

## Key idea

Run a comparative multi-omics screen across **12 JAK-STAT mutant mouse models** (knockouts of every STAT, isoform-specific Stat1 mutants, IRF9 KO, TYK2 KO, kinase-dead TYK2-K923E, and oncogenic STAT5BN642H) in **unperturbed/unstimulated** splenic immune cells. Profile transcriptomes (RNA-seq) and chromatin accessibility (ATAC-seq), validate in vivo using [[foundations/10x-visium-spatial-transcriptomics|Visium spatial transcriptomics]] and [[foundations/rnascope-single-molecule-fish|RNAscope single-molecule RNA-FISH]] on perfusion-fixed spleens, then test the **tissue-context hypothesis** by depriving cells of the tissue niche ex vivo ± IFN-β rescue. This isolates **baseline / tonic** JAK-STAT activity as a distinct biological phenomenon from acute-stimulation signaling.

## Method

- **Mouse models**: knockouts of STAT1/2/3/4/5(a/b)/6, IRF9, TYK2; isoform-specific Stat1a-only and Stat1b-only; kinase-dead Tyk2-K923E (Tyk2-inact); oncogenic Stat5b-N642H (Stat5-hyp); Vav-iCre conditional KOs for embryonic-lethal STAT3 and STAT5; matched WT processed in parallel for batch control.
- **Cells profiled**: sort-purified splenic CD8+ T cells, F4/80+ macrophages (main focus); MHCII+CD11c+ DCs, NK1.1+ NK, CD19+ B cells (subset of models).
- **Bulk omics**: Smart-seq2 RNA-seq (n=469 high-quality samples) and ATAC-seq (n=496 samples), STAR alignment to mm10, MACS2 peak calling, limma+variancePartition (dream) linear mixed models with experiment as random intercept.
- **Spatial validation**: 10x Visium FFPE spatial transcriptomics on transcardially formaldehyde-perfused spleens (WT and Stat1-KO); k-means clustering of spatial profiles; quantification of top-15 STAT1-driven genes vs housekeeping genes.
- **Sub-cellular validation**: RNAscope multiplex fluorescent in situ hybridization for Oas3, Ifit3, Cd3e on spleen FFPE.
- **TF inference**: HOMER motif enrichment + LOLA region-set enrichment + TOBIAS ATAC footprinting (JASPAR2022 PFMs).
- **Cell-cell interactions**: CellChat on Tabula Muris/Tabula Sapiens spleen data with ProjecTILs T-cell subtyping.
- **Tissue-context experiments**: 20 h ex vivo culture ± M-CSF ± IFN-β (1.5 h, 20 h) on WT and JAK-STAT mutant cells; matched RNA-seq + ATAC-seq.
- **Module discovery**: UMAP on log2FC matrix across mutants × cell types, walktrap clustering on k-NN graph → 16 gene-regulatory modules (A–P) with gene-set enrichment via tmodCERNO and Fisher's exact test.

## Results

- Every JAK-STAT mutant induced characteristic, cell-type-specific transcriptional changes in unstimulated splenic immune cells. STAT2, STAT3, STAT5 and IRF9 KO had the strongest effects; STAT1 KO had a much smaller effect than expected from its ISGF3 role.
- ISGF3 member KOs (STAT1, STAT2, IRF9) and TYK2 KOs all downregulated core ISGs (Oas3, Ifit1, Ifit3, Oasl1, Mx1) → tonic ISGF3-like activity exists under homeostasis.
- STAT3 and STAT5 KO downregulated a subset of ISGs mainly in macrophages → cooperative ISG regulation under homeostasis.
- No single shared JAK-STAT signature: each family member controls a characteristic, cell-type-specific gene set.
- 16 UMAP-defined gene-regulatory modules organize the JAK-STAT homeostatic landscape; Module P matches the ISG-core gene set and is downregulated in all ISGF3-member and TYK2 KOs.
- IRF9 regulates many target genes independently of STAT1 and STAT2 (e.g. Rdh14, Tprkb, Usb1) — broader function than the ISGF3 complex predicts.
- STAT5BN642H acts as a neomorphic TF: very low Spearman correlation with STAT5-KO (r≈0.07 IL-2 1.5 h, r=0.248 IL-2 20 h) and shifts target genes toward Aurora-kinase, cell-cycle, E2F4, FOXM1 signatures.
- STAT1α and STAT1β isoforms have differential and partially opposing transcriptional effects, with STAT1α showing more similarity to full Stat1-KO.
- TYK2 kinase-dead (Tyk2-inact) vs full Tyk2-KO share many effects but diverge for some genes → kinase-independent TYK2 functions exist (some IL-12-regulated genes).
- Spatial transcriptomics of formaldehyde-perfused WT vs Stat1-KO spleens confirms STAT1-driven ISG expression in white pulp (Cluster 4) with normal tissue architecture preserved.
- RNAscope single-molecule RNA-FISH validates Oas3 and Ifit3 dependency on STAT1 at sub-cellular resolution in white and red pulp.
- ATAC-seq identifies three groups of JAK-STAT mutants: low transcript+epigenome (STAT1/STAT4/STAT6/Tyk2-inact in T cells), high transcript / low epigenome (STAT2, STAT3, IRF9 in both cell types), high epigenome with stronger coupling (STAT5, STAT6 in macrophages, TYK2 in both, STAT5BN642H in T cells).
- STAT5 and STAT6 KO increase chromatin accessibility in macrophages → repressive epigenomic role under homeostasis (consistent with STAT6 repression of M1 polarization).
- STAT5BN642H lost the repressive accessibility role and instead opened T-cell effector loci (granzymes Gzmk/Gzmb, Klrc1/Klre1, Mki67) → mechanism of T-cell hyperproliferation/leukemogenesis.
- TF footprinting (TOBIAS): RUNX2 enriched in STAT5BN642H T cells; EOMES and FOS::JUN in STAT5-KO T cells; GATA1::TAL1 in STAT5-KO macrophages; NFKB2 in STAT6-KO macrophages; ZBED1 motifs depleted in STAT4-KO T cells.
- Ex vivo culture (context deprivation) collapses JAK-STAT and IFN signatures in both T cells and macrophages → baseline activity is **cell-extrinsic** in origin.
- Context-deprivation transcriptional changes mirror those of STAT1/STAT2/IRF9/TYK2 KOs in WT cells; IFN-β stimulation partially rescues these effects (except STAT1β-dependent genes).
- Macrophages additionally lose macrophage-specific identity programs upon context deprivation; neither M-CSF nor IFN-β rescues identity loss → macrophages depend on tissue context for cellular identity, not just for JAK-STAT activity.
- CellChat receptor-ligand inference (Tabula Muris/Sapiens) nominates KLRB1–CLEC2B, SIGLEC1–SPN, LILRB1–HLA-F, HAVCR2/TIM3–LGALS9 as candidate cell-extrinsic triggers of baseline JAK-STAT.
- Interaction-effect modeling (mutant × stimulation) shows STAT2 and IRF9 KO most strongly compromise the IFN-β response — these factors carry the brunt of baseline JAK-STAT-mediated priming.

## All claims (exhaustive)

- `[c01]` Tonic/baseline JAK-STAT signaling exists in unstimulated CD8+ T cells and macrophages from unperturbed mouse spleens (p.848, abstract) — "Baseline JAK-STAT signaling was detected in CD8+ T cells and macrophages of unperturbed mice—but abrogated in the knockouts and in unstimulated immune cells deprived of their normal tissue context" — confidence: high — type: mechanistic — links: [[concepts/tonic-baseline-jak-stat-homeostasis]] [[claims/baseline-jak-stat-homeostasis-cd8-macrophage]]
- `[c02]` 469 RNA-seq + 496 ATAC-seq high-quality profiles across 12 mouse models constitute a baseline JAK-STAT epigenome/transcriptome resource (p.849) — "In total, we obtained 469 high-quality transcriptomes by RNA-seq and 496 high-quality epigenome profiles with the assay for transposase-accessible chromatin using sequencing (ATAC-seq)" — confidence: high — type: methodological — links: [[claims/jak-stat-multiomics-resource-12-mutants]]
- `[c03]` Knockout of STAT2, STAT3, STAT5 and IRF9 produces the largest transcriptional effects on homeostatic immune cells; STAT1 KO is comparatively mild (p.849) — "Knockout of STAT2, STAT3, STAT5 and IRF9 had the strongest transcriptional consequences. Knockout of STAT1 or one of its isoforms had smaller effects, despite its prominent role in the ISGF3 complex" — confidence: high — type: correlational — links: [[claims/stat2-stat3-stat5-irf9-strongest-transcriptional-effects-homeostasis]]
- `[c04]` ISGF3 member KOs (STAT1, STAT2, IRF9) and TYK2 KOs all downregulate core ISGs in homeostatic immune cells (p.849) — "we observed marked downregulation in knockouts of ISGF3 complex members (STAT1, STAT2, IRF9), in TYK2 knockouts and in the kinase-dead TYK2K923E mutant" — confidence: high — type: mechanistic — links: [[concepts/tonic-baseline-jak-stat-homeostasis]] [[foundations/isgf3-complex]] [[claims/core-isg-downregulation-isgf3-tyk2-ko-homeostasis]]
- `[c05]` STAT3 and STAT5 KO cause downregulation of an ISG subset in macrophages, indicating cooperative regulation with ISGF3 members under homeostasis (p.849) — "STAT3 and STAT5 knockouts led to downregulation of a subset of ISGs mainly in macrophages, indicating cooperative regulation of ISGs by STAT3 and STAT5 with ISGF3 members under homeostatic conditions" — confidence: medium — type: mechanistic — links: [[claims/stat3-stat5-cooperate-isgf3-macrophage-isg-regulation]]
- `[c06]` 6,247 differentially expressed genes cluster into 16 gene-regulatory modules (UMAP + walktrap) describing the homeostatic JAK-STAT landscape (p.850) — "we grouped all differentially expressed genes (n = 6,247) into gene-regulatory modules across mutants and cell types ... we clustered differentially expressed genes into 16 gene-regulatory modules" — confidence: high — type: methodological — links: [[claims/jak-stat-16-gene-regulatory-modules-homeostasis]]
- `[c07]` Module P matches the ISG-core gene set and is downregulated in all ISGF3 member KOs and TYK2 KOs (p.850) — "Our analysis identified a gene cluster (module P) that was highly enriched for the previously described 'ISG core' gene set ... This module was strongly downregulated in knockouts of all three ISGF3 members (STAT1, STAT2, IRF9), in TYK2 knockouts and in the kinase-dead TYK2K923E mutant" — confidence: high — type: correlational — links: [[claims/module-p-isg-core-isgf3-tyk2-ko-downregulation]]
- `[c08]` IRF9 regulates target genes independently of STAT1/STAT2/ISGF3 (e.g. Rdh14, Tprkb, Usb1) in homeostatic immune cells (p.851) — "Our analyses demonstrate that IRF9 regulates many of its target genes independent of STAT1, STAT2 and of the canonical ISGF3 complex, possibly by interacting with other transcription factors including members of the STAT family" — confidence: high — type: mechanistic — links: [[concepts/isgf3-independent-irf9-function]] [[foundations/irf9-tf]] [[claims/irf9-isgf3-independent-target-regulation]]
- `[c09]` IRF9 KO transcriptional changes correlate strongly with STAT3 and STAT5 KO macrophage changes, suggesting IRF9 partnership with STAT3/STAT5 under homeostasis (p.851) — "The transcriptional changes observed in IRF9 knockouts showed a high correlation with those found in STAT3 and STAT5 knockout macrophages ... suggesting STAT3 and STAT5 as potential interaction partners of IRF9 in macrophages under homeostatic conditions" — confidence: medium — type: correlational — links: [[concepts/isgf3-independent-irf9-function]] [[claims/irf9-stat3-stat5-partnership-macrophage-correlation]]
- `[c10]` STAT5BN642H is a neomorphic gain-of-function TF: target genes weakly correlate with STAT5-KO and with WT STAT5 IL-2 response (Spearman r≈0.07 at 1.5 h IL-2, r=0.248 at 20 h) (p.852, Fig. 3b) — "STAT5BN642H-mutant T cells also showed little overlap with STAT5 wild type upon IL-2 stimulation (Spearman's r = 0.071 at 1.5 h; Spearman's r = 0.248 at 20 h), suggesting that this oncogenic driver mutation compromises normal STAT5 function and redirects the regulatory activity" — confidence: high — type: quantitative — links: [[concepts/stat5b-n642h-neomorphic-oncogenic-driver]] [[foundations/stat5-tf]] [[claims/stat5bn642h-neomorphic-low-correlation-il2]]
- `[c11]` STAT5BN642H targets are enriched for AURORA kinase, cell-cycle, E2F4 and FOXM1 signatures, linking neomorphic STAT5 to T-cell hyperproliferation (p.852, Fig. 3b) — "Gene set analysis identified enrichment for AURORA kinase signaling ... cell cycle progression and target genes of the transcription factors E2F4 and FOXM1 ... These results suggest a switch of target genes for the STAT5BN642H mutant compared with STAT5 wild type, which likely contributes to its role in T cell proliferation and lymphoma/leukemia development" — confidence: high — type: mechanistic — links: [[concepts/stat5b-n642h-neomorphic-oncogenic-driver]] [[claims/stat5bn642h-aurora-e2f4-foxm1-target-shift]]
- `[c12]` STAT1α and STAT1β isoforms differ in their transcriptional effects, with STAT1α more closely matching the full Stat1-KO phenotype (p.852, Fig. 3c) — "differences between the two STAT1 splicing isoforms ... STAT1 isoform mutants reveal isoform-specific functions and the opposing roles of STAT1 alpha and STAT2" — confidence: medium — type: correlational — links: [[concepts/stat1-isoform-specificity-alpha-beta]] [[foundations/stat1-tf]] [[claims/stat1-alpha-beta-isoform-divergent-effects]]
- `[c13]` TYK2 has kinase-independent regulatory functions: Tyk2-inact (kinase-dead K923E) and full Tyk2-KO share many effects but diverge for a subset of IL-12-regulated genes (p.852, Fig. 3d) — "kinase-independent effects of TYK2 ... A TYK2 kinase-dead mutant reveals kinase-dependent and kinase-independent functions of TYK2" — confidence: high — type: mechanistic — links: [[concepts/kinase-independent-functions-tyk2]] [[foundations/tyk2-kinase]] [[claims/tyk2-kinase-independent-functions]]
- `[c14]` In vivo Visium spatial transcriptomics of formaldehyde-perfused spleens confirms that STAT1-driven ISGs are reduced in Stat1-KO white pulp (Cluster 4) without altering tissue architecture (p.853, Fig. 4a–c) — "We observed significantly higher expression of these putative STAT1 target genes in wild-type compared with STAT1 knockout mice specifically for spatial Cluster 4, which corresponds to white pulp ... the classical ISGs Oas3, Ifit3 and Ifit1 were expressed in wild-type mice but almost completely absent in STAT1 knockouts" — confidence: high — type: methodological — links: [[foundations/10x-visium-spatial-transcriptomics]] [[claims/spatial-transcriptomics-confirms-stat1-baseline-isg-spleen]]
- `[c15]` Single-molecule RNAscope RNA-FISH for Oas3 and Ifit3 confirms loss in Stat1-KO at sub-cellular resolution in both white and red pulp (p.854, Fig. 4d,e) — "Consistent with the spatial transcriptomics data, we observed Oas3 and Ifit3 expression in wild-type mice but not in STAT1 knockout mice, both for the spleen's white pulp ... and the red pulp" — confidence: high — type: methodological — links: [[foundations/rnascope-single-molecule-fish]] [[claims/rnascope-validates-oas3-ifit3-stat1-dependence]]
- `[c16]` JAK-STAT mutants partition into three epigenome–transcriptome coupling groups: low/low low-correlation; high-transcript low-epigenome (STAT2, STAT3, IRF9); strong epigenome with stronger correlation (STAT5/STAT6/TYK2/STAT5BN642H) (p.854, Fig. 5d) — "we identified three groups of JAK-STAT mutants with distinct patterns" — confidence: high — type: correlational — links: [[claims/jak-stat-three-epigenome-transcriptome-coupling-groups]]
- `[c17]` STAT5 and STAT6 KO increase chromatin accessibility in macrophages, indicating a repressive epigenomic role under homeostasis (p.854) — "Knockouts of STAT5 and STAT6 resulted in increased chromatin accessibility specifically in macrophages, indicative of a repressive role of these factors under homeostatic conditions and in line with known STAT6-mediated repression of M1 polarization genes" — confidence: high — type: mechanistic — links: [[claims/stat5-stat6-repressive-chromatin-macrophage-homeostasis]]
- `[c18]` STAT5BN642H abrogates the repressive STAT5 chromatin role and opens T-cell effector loci (Gzmk/Gzmb, Klrc1/Klre1, Mki67), explaining hyperproliferation (p.854) — "The oncogenic STAT5BN642H mutant lost the repressive effect of STAT5 and instead caused T cell-specific increased chromatin accessibility, as well as upregulation of T cell effector genes (granzymes Gzmk, Gzmb), of killer cell lectin-like receptors (Klrc1, Klre1) and of the cell cycle regulator Mki67, which likely contributes to hyperproliferation of STAT5BN642H T cells" — confidence: high — type: mechanistic — links: [[concepts/stat5b-n642h-neomorphic-oncogenic-driver]] [[claims/stat5bn642h-opens-effector-loci-tcell-hyperproliferation]]
- `[c19]` TOBIAS TF-footprinting reveals JAK-STAT mutant-specific TF activity changes: RUNX2 (Stat5-hyp T), EOMES & FOS::JUN (Stat5-KO T), GATA1::TAL1 (Stat5-KO Mac), NFKB2 (Stat6-KO Mac), ZBED1 depleted (Stat4-KO T) (p.854, Fig. 5c) — "We identified enriched binding sites of RUNX2 in STAT5BN642H mutant T cells, EOMES and AP1 heterodimer (FOS/JUN) in STAT5 knockout T cells, GATA1/TAL1 in STAT5 knockout macrophages and NFκB in STAT6 knockout macrophages ... binding sites of ZBED1 ... were enriched in regions with decreased chromatin accessibility in STAT4 knockout T cells" — confidence: high — type: methodological — links: [[foundations/tobias-atac-footprinting]] [[claims/tobias-footprinting-jak-stat-mutant-tf-activity-shifts]]
- `[c20]` Ex vivo culture (tissue-context deprivation) downregulates JAK-STAT and IFN signatures in both T cells and macrophages, mimicking JAK-STAT KO phenotypes (p.854–855, Fig. 6b–d) — "Deprivation of tissue context by ex vivo culture resulted in strong downregulation of genes ... and pathways ... related to JAK-STAT and IFN signaling, both in T cells and in macrophages" — confidence: high — type: mechanistic — links: [[concepts/tissue-context-dependence-immune-signaling]] [[claims/ex-vivo-context-deprivation-collapses-baseline-jak-stat]]
- `[c21]` IFN-β stimulation partially rescues baseline-JAK-STAT loss in context-deprived cells, except for STAT1β-dependent genes (p.855, Fig. 6d) — "Ex vivo stimulation with IFN-β rescued most of these effects, with the exception of STAT1-beta-dependent genes" — confidence: high — type: mechanistic — links: [[concepts/tissue-context-dependence-immune-signaling]] [[concepts/stat1-isoform-specificity-alpha-beta]] [[claims/ifn-beta-partially-rescues-context-deprivation-except-stat1beta]]
- `[c22]` Macrophages additionally lose macrophage-specific identity programs upon context deprivation, not rescued by IFN-β or M-CSF (p.855) — "macrophages depleted of their tissue context not only exhibited widespread loss of JAK-STAT-mediated gene expression, but also a broader downregulation of macrophage-specific gene expression programs ... Neither IFN-β stimulation nor treatment with macrophage growth factor M-CSF was able to rescue this wider loss" — confidence: high — type: mechanistic — links: [[concepts/tissue-context-dependence-immune-signaling]] [[claims/macrophage-identity-tissue-context-dependent-irreversible-ex-vivo]]
- `[c23]` CellChat receptor-ligand inference nominates KLRB1-CLEC2B, SIGLEC1-SPN, LILRB1-HLA-F, HAVCR2/TIM3-LGALS9 as cell-extrinsic candidate triggers of baseline JAK-STAT in spleen (p.855, Fig. 6e–f) — "splenic CD8+ T cells highly expressed the KLRB1 receptor ... Splenic macrophages were characterized by high expression of checkpoint molecule receptors such as SIGLEC1 ... and LILRB1 ... the HAVCR2/TIM3-LGALS9 receptor–ligand pair may mediate macrophage interactions with most types of myeloid immune cells in the spleen" — confidence: medium — type: correlational — links: [[foundations/cellchat-cell-cell-communication]] [[claims/cellchat-receptor-ligand-candidates-baseline-jak-stat-spleen]]
- `[c24]` Spleen architecture is preserved in Stat1-KO mice (T-cell Cd8a and macrophage Cd33 localization unchanged), so baseline-JAK-STAT phenotypes are not secondary to gross structural defects (p.852–853) — "The overall tissue architecture was unaffected by the STAT1 knockout, and the localization of T cells (marked by Cd8a expression) and macrophages (marked by Cd33 expression) was similar between wild-type and knockout mice" — confidence: high — type: correlational — links: [[claims/stat1-ko-preserves-spleen-architecture]]
- `[c25]` STAT2 and IRF9 carry the brunt of homeostatic priming: their KOs most strongly compromise the IFN-β response across interaction-effect signatures (p.857) — "The stimulation-induced restoration of wild-type gene expression was most pronounced for target genes of STAT2 and IRF9, which appear to have key roles in maintaining baseline JAK-STAT signaling in immune cells under homeostatic conditions" — confidence: high — type: mechanistic — links: [[concepts/tonic-baseline-jak-stat-homeostasis]] [[claims/stat2-irf9-keystones-baseline-jak-stat-priming]]

## Discussion captured

### Authors' interpretation

Authors interpret baseline JAK-STAT signaling as an active homeostatic mechanism rather than residual leak: it is broadly cell-type-specific, requires the in vivo tissue context, and tunes both the transcriptome and the chromatin-accessibility landscape ("epigenetic potential") to keep immune cells "poised" for rapid response. STAT2 and IRF9 are framed as the keystones of this poised state, with IRF9 acting well beyond its canonical role in ISGF3 (regulating distinct gene sets, partially via STAT3/STAT5 partnership in macrophages). STAT1 is recast as a chromatin regulator whose epigenome effect exceeds its modest transcriptional footprint. STAT5BN642H is interpreted as a "de novo transcription factor" with cancer-associated target rewiring rather than just a hyperactive STAT5. The authors position the study as the most comprehensive epigenome/transcriptome dissection of a single signaling pathway and a blueprint for similar pathway-level studies.

### Comparisons with prior literature (made by authors)

- Builds on the JAK-STAT-at-30 review (Philips et al. 2022, ref 12) and the foundational JAK-STAT framework (O'Shea/Darnell, refs 10–14, 22–23).
- Cites earlier evidence of low-level constitutive STAT1/STAT2 target expression (Blaszczyk 2016 ref 18; Gough 2012 ref 19 tonic type-I IFN; Platanitis 2019 ref 20 STAT2-IRF9 molecular switch; Taniguchi 2001 ref 21).
- Compares to STAT6-mediated repression of M1 macrophage enhancers (Czimmerer 2018 ref 25) — consistent with the repressive chromatin role this paper observes.
- Cites STAT5BN642H as a known T-cell-neoplasia driver (Pham 2018 ref 48) — extends to neomorphic transcriptional rewiring.
- References Karaghiosoff 2000 (ref 39) and Prchal-Murphy 2012 (ref 40) for TYK2 partial-impairment phenotypes — consistent with kinase-independent functions.

### Mechanistic hypotheses proposed

- "Baseline JAK-STAT activity helps maintain the 'epigenetic potential' of immune cells, by keeping immune cells in a regulatory state that supports rapid activation without previous chromatin remodeling" (p.854).
- IRF9 likely interacts with non-ISGF3 partners (STAT3, STAT5, possibly STAT6) to regulate non-ISG targets under homeostasis (p.851).
- "This oncogenic driver of T cell leukemia/lymphoma should be thought of as a de novo transcription factor with a set of cancer-associated target genes that is qualitatively different from wild-type STAT5B" (p.857) — neomorphic-TF hypothesis for STAT5BN642H.
- Baseline JAK-STAT is triggered by tissue-context cell–cell interactions (candidate pairs from CellChat) rather than cell-intrinsic mechanisms such as DNA-damage accumulation (p.855).

### Caveats and self-criticism

- Authors note the conditional Vav-iCre approach for STAT3 and STAT5 (forced because germline KOs are lethal) may carry hematopoietic-development confounders.
- Sort-purification and ex vivo handling can in principle alter gene expression — the spatial-transcriptomics + RNAscope on perfusion-fixed spleens is included precisely to rule this out.
- Spatial transcriptomics (Visium FFPE) does not provide single-cell resolution; RNAscope is used to complement (p.854).
- "Mutants with many differences in their epigenomes also tended to differ strongly in their transcriptomes, although the association was far from perfect" — non-trivial epigenome–transcriptome decoupling for some mutants (p.854).

### Future directions suggested

- Investigate roles of perturbed baseline JAK-STAT signaling in inborn errors of immunity, inflammatory disorders, and cancer pathophysiology, diagnosis, and treatment (p.857).
- Treat the resource as a blueprint for similar pathway-level studies in immunology and beyond.
- Mechanistic dissection of non-ISGF3 IRF9 complexes and their tissue-context dependencies.
- Map cell-extrinsic ligand identity and source cell types for baseline JAK-STAT triggering.

## Limitations

- All findings in mouse spleen splenocytes; no human validation in this paper.
- Smart-seq2 bulk RNA-seq — no single-cell resolution of intra-population heterogeneity (rescued partially by spatial transcriptomics + RNAscope).
- ATAC-seq accessibility is correlated, not causal, evidence for TF binding; TOBIAS footprinting is motif-based, not chromatin-binding-validated.
- 12 mutant models are deep but still finite; no Jak1/Jak2/Jak3 KO (lethal).
- Tissue-context deprivation experiments use 20 h ex vivo culture as proxy — does not isolate which specific cell–cell interaction is responsible.
- CellChat receptor-ligand inferences are computational hypotheses, not validated experimentally.
- Stat3/Stat5 KO via Vav-iCre may confound hematopoietic development.
- The 16-module decomposition is sensitive to UMAP/walktrap parameters.

## Open questions

### Open questions raised by authors

- What is the role of perturbed baseline JAK-STAT signaling in human disease (inborn errors of immunity, inflammatory disorders, cancer)?
- Which specific cell-extrinsic ligands and source cell types trigger baseline JAK-STAT in the spleen tissue context?
- What non-ISGF3 protein complexes does IRF9 form to regulate ISGF3-independent targets?
- Do other signaling pathways (e.g. NF-κB, MAPK) similarly maintain baseline activity under homeostasis?

### Open questions identified during ingest

- How does baseline JAK-STAT signaling intersect with hypoxia in the spleen and in tumour-infiltrating cells (relevant to thesis)?
- Can context-deprivation phenotypes be partially reversed by reconstituting CellChat-nominated receptor-ligand pairs in vitro (e.g. KLRB1 agonism)?
- Are the IRF9 non-ISGF3 partners cell-type-specific, and do they overlap with STAT3/STAT5 targets in human macrophages?
- Does single-cell ATAC + RNA on perfusion-fixed spleens reproduce the bulk-derived three-group epigenome/transcriptome coupling pattern?
- How does the neomorphic STAT5BN642H chromatin signature relate to TEXterm chromatin landscapes in chronic infection / tumour CD8 cells (cross-link to [[papers/atlas-guided-discovery-transcription-factors-cell]])?

## My take

This is the single most comprehensive in vivo dissection of a cytokine-receptor pathway in unstimulated immune cells to date, and it changes how I read JAK-STAT data: "baseline" is not noise. Two implications for the thesis: (1) any RNA-seq comparison of immune cells **must** preserve tissue context (or explicitly account for ex vivo collapse of JAK-STAT signatures) — macrophages especially lose identity programs in 20 h culture, which is shorter than many in vitro protocols. (2) The STAT2-IRF9 axis as a homeostasis keystone is a novel ingredient for interpreting ISG signatures in TILs and hypoxic tumours — high ISG ≠ active IFN response; could be tonic. The neomorphic STAT5BN642H finding is also a clean precedent for thinking about cancer-driver TFs as **rewired** rather than just hyperactive. Cross-linking to [[papers/atlas-guided-discovery-transcription-factors-cell]] (Chung 2025): the multi-state vs single-state TF framework is directly applicable to homeostatic vs stimulated JAK-STAT modules here.

## Related

- [[concepts/tonic-baseline-jak-stat-homeostasis]]
- [[concepts/tissue-context-dependence-immune-signaling]]
- [[concepts/isgf3-independent-irf9-function]]
- [[concepts/stat5b-n642h-neomorphic-oncogenic-driver]]
- [[concepts/stat1-isoform-specificity-alpha-beta]]
- [[concepts/kinase-independent-functions-tyk2]]
- [[foundations/stat1-tf]]
- [[foundations/stat2-tf]]
- [[foundations/stat3-tf]]
- [[foundations/stat5-tf]]
- [[foundations/stat6-tf]]
- [[foundations/irf9-tf]]
- [[foundations/tyk2-kinase]]
- [[foundations/isgf3-complex]]
- [[foundations/atac-seq]]
- [[foundations/10x-visium-spatial-transcriptomics]]
- [[foundations/rnascope-single-molecule-fish]]
- [[foundations/tobias-atac-footprinting]]
- [[foundations/homer-motif-enrichment-analysis]]
- [[foundations/cellchat-cell-cell-communication]]
- [[foundations/type-interferon-ifna-ifnb]]
- [[people/nikolaus-fortelny]]
- [[people/matthias-farlik]]
- [[people/christoph-bock]]
- [[people/thomas-decker]]
- [[people/mathias-mueller]]
