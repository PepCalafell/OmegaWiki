---
# === Identification ===
title: "Cross-tissue single-cell landscape of human monocytes and macrophages in health and disease"
slug: cross-tissue-single-cell-landscape-human
arxiv: ""
doi: "10.1016/j.immuni.2021.07.007"
pmid: "34331874"
venue: "Immunity"
year: 2021
authors:
  - "Kevin Mulder"
  - "Amit Ashok Patel"
  - "Wan Ting Kong"
  - "Cécile Piot"
  - "Evelyn Halitzki"
  - "Garett Dunsmore"
  - "Shabnam Khalilnezhad"
  - "Sergio Erdal Irac"
  - "Agathe Dubuisson"
  - "Marion Chevrier"
  - "Xiao Meng Zhang"
  - "John Kit Chung Tam"
  - "Tony Kiat Hon Lim"
  - "Regina Men Men Wong"
  - "Rhea Pai"
  - "Ahmed Ibrahim Samir Khalil"
  - "Pierce Kah Hoe Chow"
  - "Suny Z. Wu"
  - "Ghamdan Al-Eryani"
  - "Daniel Roden"
  - "Alexander Swarbrick"
  - "Jerry Kok Yen Chan"
  - "Salvatore Albani"
  - "Lisa Derosa"
  - "Laurence Zitvogel"
  - "Ankur Sharma"
  - "Jinmiao Chen"
  - "Aymeric Silvin"
  - "Antonio Bertoletti"
  - "Camille Blériot"
  - "Charles-Antoine Dutertre"
  - "Florent Ginhoux"
first_author: "Kevin Mulder"
corresponding_author: "Charles-Antoine Dutertre; Florent Ginhoux"

# === Source & metadata ===
source_type: pdf
s2_id: "b733115a1777f22f0a24635c0b8437b061ce5257"
date_added: 2026-05-06
ingested_date: 2026-05-06
ingest_version: 1
last_reviewed: null

# === Classification ===
importance: 5
tier: TIER_1
tags:
  - macrophage
  - monocyte
  - dendritic-cell
  - mononuclear-phagocyte
  - single-cell
  - scRNA-seq
  - atlas
  - cross-tissue
  - tumor-microenvironment
  - immunology
  - cancer
  - immunosuppression
  - reference-mapping
keywords:
  - MNP-VERSE
  - MoMac-VERSE
  - IL4I1 macrophage
  - TREM2 macrophage
  - HES1 macrophage
  - FOLR2 macrophage
  - mregDC
  - Phenograph clusters
  - Seurat V3 integration
  - SCENIC
  - NicheNet
  - Azimuth
  - tryptophan / AHR / IDO1
  - tumor periphery
domain: "immunology / single-cell / oncology"

# === Biomedical domain ===
tissue:
  - spleen
  - lung
  - liver
  - skin
  - blood
  - lymph_node
  - kidney
  - tonsil
  - colon
  - stomach
  - breast
  - pancreas
  - multi
condition:
  - healthy
  - cancer
  - autoimmune
  - inflam_precancer
disease_specific:
  - lupus_nephritis
  - cirrhosis
  - colitis
  - rheumatoid_arthritis
  - COVID-19
  - HCC
  - LUAD
  - colorectal_cancer
  - breast_cancer
  - gastric_cancer
  - pancreatic_cancer
species:
  - human
  - mouse
hypoxia_relevant: false
contains_immune_cells: true
contains_myeloid: true

# === Technique ===
techniques:
  - scRNA-seq_10x
  - scRNA-seq_SMARTseq2
  - CITE-seq
  - flow_cytometry
  - mass_cytometry
  - lineage_tracing_Ms4a3
  - bulk_RNA-seq
  - SCENIC
  - NicheNet
  - Azimuth
  - Seurat_V3_integration
  - Phenograph_clustering
  - Ingenuity_Pathway_Analysis
n_samples: 41
n_cells_total: 178651
integration_method: "Seurat V3 anchor integration (CCA + reciprocal PCA)"

# === Biology captured ===
key_cell_types:
  - classical_monocyte_cMo
  - CD16_non-classical_monocyte
  - intermediate_monocyte
  - alveolar_macrophage
  - TREM2_macrophage
  - IL4I1_macrophage
  - HES1_macrophage
  - FOLR2_macrophage
  - FTL_macrophage
  - C1Qhi_macrophage
  - IL1B_monocyte
  - ISG_monocyte
  - cDC1
  - cDC2
  - DC3
  - mregDC
  - pre-DC
  - proliferating_macrophage
  - regulatory_T_cell
  - cytotoxic_CD8_T_cell
key_markers:
  - CD14
  - CD16
  - CD88
  - CD11b
  - CD206
  - HLA-DR
  - HLA-DP
  - HLA-DQ
  - CD68
  - C1QA
  - C1QB
  - TREM2
  - APOE
  - SPP1
  - GPNMB
  - FOLR2
  - LYVE1
  - MERTK
  - HBEGF
  - IL4I1
  - IDO1
  - PD-L1
  - PD-L2
  - CD40
  - CD80
  - CD86
  - CCR7
  - CD9
  - HES1
  - FTL
  - CXCL9
  - CXCL10
  - CXCL11
  - IL1B
  - NFKBIA
  - C5AR1
  - HLA-DRB1
  - ISG15
  - IFIT1
  - IFIT2
  - IFIT3
  - S100A8
  - S100A9
  - S100A12
  - CADM1
  - CLEC9A
  - XCR1
  - FCER1A
  - CD1C
  - CD1E
  - CD123
  - CD169
  - CD5
  - FcεRIα
  - CD141
  - CD274
  - PDCD1LG2
  - CD38
key_pathways:
  - tryptophan-AHR-IDO1
  - IFNG/STAT1
  - IFNA/STAT2
  - NF-kB
  - PD-L1/PD-1
  - CD40-CD40L
  - antigen-presentation
  - phagocytosis-MERTK
  - lipid-metabolism
  - CXCR3-chemokine

# === User project membership ===
projects:
  - thesis
  - hypoxia
priority: core
read_status: read

# === HypoxiaVERSE-specific ===
hypoxiaverse_status: included
exclusion_reason: null
data_availability: "https://gustaveroussy.github.io/FG-Lab/ — interactive MoMac-VERSE / MNP-VERSE atlas; constituent dataset accessions in original publications"

# === Cross-references ===
code_url: "https://gustaveroussy.github.io/FG-Lab/"
cited_by:
  - nf-kb-tet2-promote-macrophage-reprogramming
  - pd-l1-expressing-tumor-associated-macrophages
---

## Problem

Mononuclear phagocytes (MNPs) — monocytes, macrophages, and dendritic cells — are central to immune defence, homeostasis, and immunoregulation, yet decades of scRNA-seq studies in different tissues have used incompatible nomenclature. Each study defines its own cell-type vocabulary (e.g. "TREM2 TAM in liver", "LAM in adipose", "mregDC in lung tumours"), making it impossible to ask cleanly whether the same population is present across tissues or diseases. There is no consensus annotation tool, no shared coordinate system, and no easy way to project new query datasets onto a stable reference. The mononuclear phagocyte system therefore lacks a unified single-cell atlas analogous to the Tabula Muris / Sapiens for whole organisms.

## Key idea

Integrate 178,651 human MNPs from 41 published scRNA-seq datasets across 13 tissues using Seurat V3 anchors to build the **MNP-VERSE** (full MNP compartment) and **MoMac-VERSE** (monocytes + macrophages only) — two consensus single-cell reference atlases that (i) define conserved Phenograph clusters with stable gene-expression and TF-regulon signatures, (ii) recover the major MNP populations validated at protein level by indexed-SMARTseq2 and CITE-seq, (iii) accept new query datasets via Azimuth for de novo annotation, and (iv) reveal pan-cancer, pan-inflammation MNP states — most notably the IL4I1⁺PD-L1⁺IDO1⁺ macrophage that accumulates in the tumour periphery and exerts T-cell-driven immunosuppression through tryptophan catabolism (AHR pathway).

## Method

- 41 datasets × 13 tissues × 178,651 MNPs collected; integration first within tissue, then across tissues using Seurat V3 anchoring (CCA / reciprocal PCA).
- In-house indexed-SMARTseq2 scRNA-seq of 1830 cells from 5 tissues (spleen, lung, liver, skin, tonsil) used to validate major MNP subsets at protein level via simultaneously indexed surface markers (CD88, CD16, CD14, CD11b, CD206, CD123, CD5, CD169, CD1c, FcεRIα, CD141).
- "Transformed matrix" (transf.matrix) constructed for downstream analysis using genes common to all integrated datasets (excluding 6 datasets too sparse to contribute).
- Phenograph clustering on the integrated/transformed embedding identified 18 clusters in MoMac-VERSE; differentially expressed transformed genes (DEtGs) per cluster.
- M1/M2 signature scoring per cluster from Martinez et al. 2006 gene sets.
- SCENIC (single-cell regulatory network inference) on three datasets (colon Zhang, liver Sharma, lung Kim) to identify differentially expressed regulons (DERs).
- Pathway analysis (Ingenuity Pathway Analysis) on cluster DEtGs vs healthy and inflammation/cancer comparisons.
- Validation by Azimuth re-projection of three new query datasets: rheumatoid arthritis synovial tissues (Kuo 2019), COVID-19 PBMCs (Silvin 2020), COVID-19 BAL (Liao 2020).
- Mouse liver scRNA-seq with Ms4a3cre-RosatdTomato lineage tracing to assign monocyte vs embryonic origin to MoMac-VERSE clusters.
- LYVE1⁻ conserved monocyte signature mean overlay to identify long-term-resident vs monocyte-derived populations.
- NicheNet on liver-cancer scRNA-seq (Sharma 2020) to predict ligand-target relationships between T-cell subsets and IL4I1_Mac / ISG_Mo.
- CITE-seq breast cancer dataset (S.Z.W., unpublished) for protein-level validation of IL4I1_Mac surface markers (PD-L1, PD-L2, MHC-II, CD80, CD86).
- Multiparametric flow cytometry on healthy human lung CD88⁺ Mo/Mac and on lung adenocarcinoma (LUAD; n=3 patients) and HCC patient samples to validate IL4I1_Mac, TREM2_Mac, HES1_Mac/FOLR2_Mac at the protein level and in normal-adjacent / periphery / core tumour zones.

## Results

- 18 conserved Phenograph clusters in MoMac-VERSE with stable DEtGs, validated at protein level on indexed-SMARTseq2 and CITE-seq.
- The "Macs" supercluster comprises HES1_Mac (#2), TREM2_Mac (#3), ISG_Mo (#4), IL4I1_Mac (#6), IL1B_Mo (#15), C1Qhi_Mac (#16), FTL_Mac (#17), and an alveolar Mac sub-population (#16 in lung).
- M1/M2 scoring: clusters #2, #6, #15, #16 enriched in M1 genes; clusters #3, #17 enriched in M2 genes; majority co-express both, breaking the binary axis. IL-12B is restricted to mregDC, not macrophages, undermining a canonical M1 marker for human MNPs.
- SCENIC: NFKB1/NFKB2 regulons confirm IL1B_Mo (#15) inflammatory status; STAT1, STAT2, ETV7, IRF1, IRF7 are common upstream regulators of ISG_Mo (#4) and IL4I1_Mac (#6).
- Cancer vs healthy: Macs in tumours up-regulate lipid-metabolism and inflammation pathways; Mos up-regulate cytokine-stimulation pathways. Shared up-regulation of T-cell-interaction pathways across both.
- Inflammation vs healthy: T-helper-1 / T-helper-2 activation, AhR activation, complement, and oxidative phosphorylation programmes shared between Mos and Macs.
- Disease-specific accumulations: liver cirrhosis → CD16⁺ Mo (#1); lupus nephritis → MNP/T cell doublets (#9), monocyte-derived DC genotype (#7); colitis → S100A8/A9/A12 cMo (#8); pan-cancer → TREM2_Mac (#3), IL4I1_Mac (#6), proliferating_Mac (#10) in all 6 cancer types; lung cancer also shows HES1_Mac (#2) accumulation; liver cancer is unique in C1Qhi_Mac (#16) accumulation.
- Azimuth validation: rheumatoid arthritis populations HBEGF⁺/MERTK⁺/IFN-STAT (Kuo 2019) map to HES1_Mac (#2), TREM2_Mac (#3), IL4I1_Mac (#6) respectively; COVID-19 BAL severe disease maps to IL4I1_Mac (#6) with strong CXCL10 + ISG signature; COVID-19 PBMC maps to HLA-DRB1^hi (mild) and NFKBIA^hi/C5AR1^hi (severe) clusters.
- Origin: Ms4a3-Cre fate-mapping in mouse liver — TREM2⁺Spp1⁺ Macs are predominantly monocyte-derived; HES1⁺/FOLR2⁺ Macs are predominantly non-monocyte-origin; murine Il4i1-like Macs are dTomato⁺ (monocyte-derived).
- Tumour zonation (liver and colon): ISG_Mo (#4), IL4I1_Mac (#6) accumulate preferentially in tumour periphery vs core; CD40LG⁺ CD4⁺ T cells and IFNG⁺ CD69⁺ CD8⁺ T cells co-localise in periphery (one-way ANOVA p<10⁻⁴).
- IL4I1_Mac membrane proteome (CITE-seq breast cancer): significantly higher PD-L1 (CD274), PD-L2 (PDCD1LG2), MHC-II, CD80, CD86 vs other Mo/Mac (p<0.0001 each).
- Flow cytometry on healthy human lung detects PD-L1^hi PD-L2^hi HLA-DP^hi HLA-DQ^hi CD40^hi CD86^hi IL4I1_Mac population.
- LUAD flow cytometry (n=3): IL4I1_Mac (CD9⁺TREM2⁻PD-L1^hi), TREM2_Mac (CD9⁺TREM2⁺), and FOLR2_Mac all accumulate in tumour vs normal adjacent.
- HCC flow cytometry: IL4I1_Mac highest CD38 and HLA-DP expression, accumulates in tumour periphery, absent from normal adjacent.
- NicheNet: IFNG (top from CD8⁺ T cells) and CD40LG (top from CD4⁺ T cells) are the most predictive ligands for IL4I1_Mac and ISG_Mo programmes.
- Mechanistic model (Fig. 6H): activated CD8⁺ IFNγ⁺ and CD4⁺ CD40L⁺ T cells in the tumour periphery reprogram IFN-primed monocytes (ISG_Mo, #4) into IL4I1_Mac (#6) via CD40 + IFNGR signalling; IL4I1_Mac then suppress T cells through PD-L1/PD-L2 and via tryptophan catabolism / AHR activation (citing Sadik et al. 2020), and recruit FOXP3⁺ Tregs through CXCR3-ligand chemokines (CXCL9/10/11).

## All claims (exhaustive)

- `[c01]` The MNP-VERSE integrates 178,651 human MNPs from 41 datasets across 13 tissues (p.1884) "we integrated 178,651 MNPs from 13 tissues across 41 datasets to generate a MNP single-cell RNA compendium (MNP-VERSE)" — confidence: high — type: methodological — links: [[concepts/momac-verse-mnp-verse-atlas]] [[claims/momac-verse-conserved-mnp-signatures-cross-tissue]]
- `[c02]` In-house indexed-SMARTseq2 of 1830 cells from 5 tissues validates major MNP populations at protein level (p.1884) "in-house-indexed-SMARTseq2 scRNA-seq data of 1,830 cells from 5 different tissues ... allowed us to broadly identify the major MNP populations based on surface protein expression" — confidence: high — type: methodological
- `[c03]` Phenograph clustering of MoMac-VERSE yields 18 conserved clusters with cluster-specific DEtGs (p.1884–1888) "calculated the differentially expressed 'transformed' genes (DEtGs) for all Phenograph clusters using the transf.matrix" — confidence: high — type: methodological — links: [[concepts/momac-verse-mnp-verse-atlas]]
- `[c04]` M1/M2 dichotomy fails to embrace the diversity of human MAC populations across tissues (p.1888–1898) "in vitro M1 Macs may not recapitulate the primary M1-like Macs ... we evidenced an array of specialized cell subsets ... the M1/M2 classification ... does not embrace macrophage diversity" — confidence: high — type: challenges — links: [[concepts/m1-m2-polarization-paradigm]]
- `[c05]` NFKB1/NFKB2 regulons define IL1B_Mo (cluster #15) inflammatory status (p.1888) "the regulon analysis could also be used to refine subpopulation functions, as exemplified by the nuclear factor κB subunit 1 (NFKB1) and NFKB2 DER of IL1B Mo #15, which confirms their classification as inflammatory Mo" — confidence: high — type: methodological — links: [[foundations/scenic-tf-regulon-inference]]
- `[c06]` STAT1, STAT2, ETV7, IRF1, IRF7 are common upstream TFs regulating ISG_Mo (#4) and IL4I1_Mac (#6) (p.1892) "we identified common key transcription factors ... STAT1, STAT2, ETS variant transcription factor 7 (ETV7), IFN regulatory factor 7 (IRF7), and IRF7 could be involved in the regulation of indoleamine 2,3-dioxygenase 1 (IDO1) and IL4I1 genes" — confidence: high — type: methodological — links: [[foundations/scenic-tf-regulon-inference]]
- `[c07]` Azimuth-mapped RA synovial populations (Kuo 2019: HBEGF⁺, MERTK⁺, IFN/STAT) map onto HES1_Mac (#2), TREM2_Mac (#3), IL4I1_Mac (#6) (p.1888) "populations identified in the study of Kuo et al. (2019) in osteoarthritis and rheumatoid arthritis patients corresponded to HES1_Mac (#2), TREM2_Mac (#3), and IL4I1_Mac (#6) of the MoMac-VERSE" — confidence: high — type: methodological — links: [[foundations/azimuth-reference-mapping]]
- `[c08]` BAL Macs from severe COVID-19 (Liao 2020) map mostly to IL4I1_Mac (#6), with strong CXCL10 + ISG signature (p.1888) "the BAL Macs from severe COVID-19 patients mapped mostly to IL4I1_Mac (#6), which were in association with stronger C-X-C motif chemokine ligand 10 (CXCL10) gene expression and IFN-stimulated gene (ISG) expression" — confidence: high — type: methodological
- `[c09]` Liver cirrhosis is associated with accumulation of CD16⁺ Mo (cluster #1) compared to healthy liver (p.1890) "Liver cirrhosis was associated with an accumulation of CD16+ Mo (#1) when compared to healthy liver" — confidence: high — type: correlational
- `[c10]` In lupus nephritis, monocyte-derived DC genotype (#7) and MNP/T cell doublets (#9) accumulate in inflamed kidney (p.1890) "in the kidneys of patients with lupus nephritis, cells with a monocyte-derived DC genotype (#7) and MNP/T cell doublets (#9) were increased" — confidence: high — type: correlational
- `[c11]` Classical S100A8/A9/A12^hi Mo accumulate in inflamed colons of colitis patients (p.1890) "classical S100A8/A9/A12hi Mo accumulated in the inflamed colons of patients presenting with colitis" — confidence: high — type: correlational
- `[c12]` TREM2_Mac (#3), IL4I1_Mac (#6), and proliferating_Mac (#10) accumulate in all 6 included cancer types (p.1892) "TREM2_Mac (#3), IL4I1_Mac (#6), and proliferating_Mac (#10) were accumulated in all of the tumors from the 6 cancer types ... included" — confidence: high — type: correlational — links: [[concepts/trem2-tumor-associated-macrophage]] [[concepts/il4i1-tumor-associated-macrophage]] [[claims/trem2-tam-pancancer-accumulation-momac-verse]]
- `[c13]` Liver tumours uniquely accumulate C1Qhi_Mac (#16); IL1B Mo (#15) does not accumulate (p.1892) "Liver tumors exhibited increased HES1_Mac (#2) and C1Qhi_Mac (#16) ... whereas IL1B Mo #15 were not accumulating" — confidence: high — type: correlational
- `[c14]` HES1_Mac (#2) populations are mostly of non-monocytic origin (p.1893) "Hes1+Folr2+ Macs were mostly of non-monocytic origin" — confidence: high — type: mechanistic — links: [[concepts/macrophage-ontogeny-resident-vs-monocyte-derived]]
- `[c15]` TREM2_Mac (#3) is predominantly monocyte-derived per Ms4a3-Cre fate-mapping (p.1893) "Trem2+Spp1+ Macs were monocyte derived" — confidence: high — type: mechanistic — links: [[concepts/macrophage-ontogeny-resident-vs-monocyte-derived]] [[concepts/trem2-tumor-associated-macrophage]]
- `[c16]` Mouse Il4i1-like Macs are dTomato⁺ — monocyte-derived (p.1893) "Mouse Il4i1+-like Macs were all dTomato+ and thus derived from Mo" — confidence: high — type: mechanistic — links: [[concepts/il4i1-tumor-associated-macrophage]]
- `[c17]` ISG_Mo (#4) and IL4I1_Mac (#6) share a similar gene expression profile suggesting a precursor-product relationship (p.1888, 1892) "ISG_Mo (#4) and IL4I1_Mac (#6) shared a similar gene expression profile ... suggestive of a close relationship ... a potential differentiation path between the ISG_Mo (#4) to the IL4I1_Mac (#6)" — confidence: medium — type: mechanistic
- `[c18]` CD40LG-expressing CD4⁺ T cells and IFNG-expressing CD69⁺ CD8⁺ T cells are most abundant in tumour periphery (p.1894–1896) "These observations suggest a potential interaction of CD40L-expressing CD4+ T cells and IFN-γ–producing CD69+-activated CD8+ T cells with ISG_Mo #4, contributing to the reprogramming into immunosuppressive IDO1+/IL4I1_Mac" — confidence: high — type: correlational — links: [[claims/il4i1-tam-induced-by-ifng-cd40l-from-tcells]]
- `[c19]` NicheNet on liver cancer predicts IFNG and CD40LG as the top stimulators of ISG_Mo (#4) and IL4I1_Mac (#6) (p.1894) "We confirmed that IFNG was the top predicted stimulator of ISG_Mo (#4) and IL4I1_Mac (#6), but not of the other T cell subsets. Importantly, CD40LG was also one of the top predicted stimulators of ISG_Mo (#4) and IL4I1_Mac (#6)" — confidence: high — type: methodological — links: [[foundations/nichenet-ligand-target-inference]] [[claims/il4i1-tam-induced-by-ifng-cd40l-from-tcells]]
- `[c20]` IL4I1_Macs degrade tryptophan via AHR pathway, consistent with Sadik et al. 2020 (p.1884, 1892, 1898) "IL-4I1+ Macs could contribute to tryptophan degradation through the IL-4I1-induced activation of the aryl hydrocarbon receptor (AHR), leading to an accumulation of regulatory T (Treg) cells, thereby establishing an immunosuppressive environment" — confidence: high — type: mechanistic — links: [[concepts/il4i1-tumor-associated-macrophage]] [[foundations/ahr-ido1-tryptophan-axis]] [[claims/il4i1-tam-degrade-tryptophan-via-ahr-immunosuppression]]
- `[c21]` IL4I1_Macs express PD-L1, PD-L2, MHC-II, CD80, CD86 at protein level — significantly higher than other Mo/Mac (p<0.0001 each) (p.1895) "Multiparametric spectral flow cytometry, quantifying protein markers validated through RNA/protein expression from the integrated CITE-seq/scRNA-seq breast cancer dataset, revealed that at the protein level, IL4I1_Mac (#6) significantly expressed more PD-L1, PD-L2, MHC class II, CD80, and CD86 proteins" — confidence: high — type: quantitative — links: [[concepts/il4i1-tumor-associated-macrophage]]
- `[c22]` CXCL9, CXCL10, CXCL11 are top DEtGs of IL4I1_Mac (#6) — predicted to recruit Tregs via CXCR3 (p.1894) "CXCL9, CXCL10, and CXCL11 were among the top DEtGs of IL4I1_Mac (#6) ... CXCR3, the receptor for these 3 chemokines, was strongly expressed by Tregs within the tumor periphery and core" — confidence: high — type: mechanistic
- `[c23]` In healthy human lung, IL4I1_Mac corresponds to PD-L1^hi-PD-L2^hi HLA-DP^hi-HLA-DQ^hi CD40^hi CD86^hi cells (p.1895) "within monocyte/macrophages, a minor population of PD-L1hiPD-L2hiHLA-DPhiHLA-DQhiCD40hiCD86hi cells that corresponded to the IL4I1_Mac (#6)" — confidence: high — type: correlational
- `[c24]` In LUAD, IL4I1_Mac (#6) and TREM2_Mac (#3) increased in tumours of all 3 patients; HES1/FOLR2_Mac increased in 2/3 (p.1896) "While IL4I1_Mac (#6) and TREM2_Mac (#3) all increased in tumors for all 3 patients, HES1/FOLR2_Mac (#2) only increased in the tumors of 2 out of the 3 patients" — confidence: high — type: correlational
- `[c25]` In HCC, IL4I1_Mac is retrieved mostly in the tumour periphery and absent from normal adjacent (p.1896) "Within Macs, PD-L1lo/–HLA-DQlo/– IL4I1_Mac (#6) was gated. Next, among PD-L1lo/–HLA-DQlo/– cells, gating of TREM2+FOLR2lo/– TREM2_Mac (#3) and TREM2lo/– FOLR2+ HES1/FOLR2_Mac (#2)" / Fig. 7K — confidence: high — type: correlational
- `[c26]` HES1_Mac (#2) and FTL_Mac (#17) are tissue-resident-leaning, sharing LYVE1⁺ signature with human fetal-liver Macs (p.1893) "LYVE1+ cells strongly overlap with fetal liver Macs included in the MoMac-VERSE ... most of the macrophage populations that were increased in cancer corresponded to the putative monocyte-derived Macs ... apart from liver tumors, where the 'long-term resident'-like HES1_Mac (#2) accumulated" — confidence: medium — type: mechanistic — links: [[concepts/macrophage-ontogeny-resident-vs-monocyte-derived]]
- `[c27]` IL4I1_Mac shows highest CD38 and HLA-DP expression among tested populations in human lung Mo/Mac (Fig. 7I) (p.1896) "IL4I1_Mac had the highest expression of CD38 and HLA-DP, confirming our findings from the MoMac-VERSE at the protein level" — confidence: high — type: quantitative

## Discussion captured

### Authors' interpretation

- The MNP-VERSE / MoMac-VERSE provides the first cross-tissue, cross-disease single-cell atlas of human mononuclear phagocytes, unifying nomenclature across studies and establishing a reference-mapping platform for de novo annotation of new datasets.
- The pan-cancer immunosuppressive macrophage axis is bipartite: TREM2_Mac (#3) lipid-driven and IL4I1_Mac (#6) IFN/T-cell-driven, accumulating in different but overlapping tumour zones.
- IL4I1_Mac is a feedback-suppressive node induced by infiltrating T cells via IFNγ + CD40L; it represents a metabolic immune checkpoint (tryptophan / AHR pathway) on top of the surface PD-L1/PD-L2 axis.
- M1/M2 dichotomy under-describes human MAC diversity, especially in cancer; the field needs a state + ontogeny taxonomy that the MoMac-VERSE clusters provide.
- HES1_Mac and FTL_Mac are likely embryonic-origin / long-term-resident; TREM2_Mac, IL4I1_Mac, proliferating_Mac, C1Qhi_Mac are likely monocyte-derived.
- COVID-19 BAL Macs map onto IL4I1_Mac and ISG_Mo, suggesting that IL4I1 macs are not tumour-specific but appear in any IFN-rich severe-inflammatory context.

### Comparisons with prior literature (made by authors)

- Mulder et al. cite Hao et al. 2021 (Azimuth, *Cell*) as the reference-mapping algorithm enabling de novo MoMac-VERSE annotation.
- They cite Stuart, Butler et al. 2019 (Seurat V3, *Cell*) as the integration backbone.
- They cite Aibar et al. 2017 (SCENIC, *Nat Methods*) for TF regulon inference.
- They cite Browaeys et al. 2020 (NicheNet, *Nat Methods*) for ligand-target inference.
- They cite Katzenelenbogen et al. 2020 *Cell*, Molgora et al. 2020 *Cell*, and Zhou et al. 2020 for prior murine TREM2 TAM characterisation, and validate cross-species similarity to MoMac-VERSE TREM2_Mac.
- They cite Maier et al. 2020 *Nature* (mregDC) as a related immunoregulatory MNP state on the DC side; IL4I1_Mac is its macrophage counterpart.
- They cite Sadik et al. 2020 *Cell* for IL4I1 acting as a more potent AHR activator than IDO1, providing the mechanistic basis for tryptophan-degradation-mediated immunosuppression.
- They cite Munn et al. 1999 *J Exp Med* for the original demonstration that IDO1-expressing monocyte-derived Macs can suppress T-cell proliferation.
- They cite Zhao et al. 2012 for IFN-γ-dependent IDO1 induction in monocyte-derived Macs by activated CD69⁺ CD8⁺ T cells, supporting the proposed mechanism.
- They cite Dutertre et al. 2019 *Immunity* for the human DC2/DC3 distinction integrated into the MNP-VERSE cluster definitions.
- They cite Liu et al. 2019 *Cell* for the Ms4a3-Cre fate-mapping mouse model used to assign monocyte vs embryonic origin.
- They cite Chakarov et al. 2019 *Science* for the LYVE1⁺ tissue-resident interstitial macrophage signature used to discriminate long-term-resident vs monocyte-derived MoMac-VERSE clusters.
- They cite Silvin et al. 2020 *Cell* and Liao et al. 2020 *Nat Med* for COVID-19 monocyte/macrophage findings recapitulated by MoMac-VERSE projection.
- They cite Bian et al. 2020 *Nature* for human embryonic Mac development used to establish the iron-metabolism / fetal-liver signature of HES1/FTL macs.

### Mechanistic hypotheses proposed

- "Activated CD8⁺ T cells produce IFN-γ that programs ISG_Mo (#4) into IL4I1_Mac (#6); CD40L-expressing CD4⁺ T cells provide a second signal" (Fig. 6H); the resulting IL4I1_Mac suppress T-cell proliferation through PD-L1, PD-L2, and tryptophan/AHR catabolism, and recruit FOXP3⁺ Tregs through CXCR3-ligand chemokines.
- The cancer-type-specific imprinting of MoMac populations (HES1_Mac in liver only; C1Qhi_Mac in liver tumours only; HES1/FOLR2_Mac in lung) suggests tumour-context-dependent recruitment vs reprogramming of tissue-resident vs monocyte-derived macrophages.
- TREM2_Mac may share monocyte ontogeny with IL4I1_Mac but follow a lipid/MERTK-driven differentiation path independent of the IFN/T-cell axis.

### Caveats and self-criticism

- "The transformed matrix is made in such a way that only genes common to all of the included datasets were taken; consequently, some genes were lost in this process but those included are conserved across studies" (p.1898) — explicit acknowledgement that transformed-matrix integration loses gene resolution.
- "Since we only included scRNA-seq datasets that were available at the time when these VERSES were generated, the MNP- and MoMac-VERSES could continuously be improved by mapping more recent and upcoming datasets through reintegration or using Azimuth" — acknowledged as a static snapshot of public data at submission time.
- "We were also limited by the number of datasets that had separately sequenced normal adjacent tissue, periphery, and tumor core. Consequently, our findings on the accumulation of IL4I1_Mac and their IFN-primed Mo (cluster #4) within the tumor periphery were limited to the liver and colon. Therefore, further validation is required for other tumors" (p.1898) — periphery-vs-core IL4I1 zonation generalisation is not fully supported.
- The IL4I1_Mac → T-cell suppression is established at the protein-marker and pathway level but not directly demonstrated by isolated IL4I1_Mac suppression assays in matched human tumour tissue.

### Future directions suggested

- Continuous updating of the atlas with newer multi-omic and spatial datasets via Azimuth-mapped reintegration.
- Validation of IL4I1_Mac periphery-zonation in additional tumour types beyond liver and colon.
- Therapeutic exploration: targeting IL4I1_Mac (anti-IL4I1, AHR antagonists, anti-CD40L blockade in cancer settings), TREM2_Mac (anti-TREM2 antibodies), and the IFN-driven monocyte-Macrophage axis.
- Translation to predict response to immunotherapy: the MoMac-VERSE platform is positioned as a way to score patient samples and stratify by IL4I1_Mac / TREM2_Mac frequencies.

## Limitations

- Transformed-matrix integration sacrifices gene resolution to maximise dataset overlap; rare or dataset-specific genes may be lost.
- 13 tissues studied — brain microglia, bone marrow, female reproductive tract, and several other tissues are not represented.
- Periphery vs tumour-core annotations available only for liver and colon cancers; periphery zonation of IL4I1_Mac in lung/breast/stomach/pancreas remains to be validated.
- Mouse Ms4a3-Cre ontogeny mapping is direct only for liver; assignment of MoMac-VERSE clusters to monocyte vs embryonic origin in other tissues is inferred from gene-signature similarity.
- IL4I1_Mac immunosuppressive function is inferred from gene programme + protein markers + spatial co-localisation + Sadik 2020 prior work, not from direct in-vitro suppression assays on FACS-isolated IL4I1_Mac from human tumour tissue.
- Cross-disease validation limited to RA and COVID-19; many other inflammatory conditions remain unmapped.

## Open questions

### Open questions raised by authors

- What are the precise ligand-receptor pathways by which IL4I1_Macs dampen antitumour T-cell responses, and how do they vary across tumour types? "The precise pathways involved are still unclear and deserve further investigation to fully decipher the T cell/TAM relationship" (p.1897, citing Gordon et al. 2017).
- Are the monocyte-derived TAMs (TREM2, IL4I1, proliferating, C1Qhi) the appropriate therapeutic targets, given that they are monocyte-derived and therefore replenishable? Targeting recruitment vs differentiation are distinct strategies.
- Is the M1/M2 Mills et al. 2000 paradigm refinable into a state + ontogeny taxonomy that captures the full diversity revealed by MoMac-VERSE?
- Can the MoMac-VERSE platform predict patient response to immunotherapy by quantifying cluster frequencies in pre-treatment samples?

### Open questions identified during ingest

- Direct in-vitro T-cell suppression assays on FACS-isolated IL4I1_Mac to confirm causal immunosuppression beyond gene-programme inference.
- Anti-IFNγ or anti-CD40L perturbation in mouse tumour models to test the proposed T-cell → IL4I1_Mac induction loop.
- Spatial-transcriptomic validation of periphery-vs-core localisation across additional tumour types.
- Whether IL4I1_Mac is induced by chronic IFN signalling in non-tumour autoimmune contexts (lupus, RA flares, severe COVID-19), and whether the same mechanistic loop applies.
- Quantitative comparison of the murine TREM2 TAM vs human TREM2_Mac transcriptional programme: is the cross-species "TREM2 TAM" a single conserved state or a convergence of distinct programmes?
- Relationship of IL4I1_Mac to Calafell 2024 mMAC1 hypoxic state: is mMAC1 a hypoxic/in-vitro proxy of IL4I1_Mac, an upstream precursor, or a distinct differentiation path that converges on similar surface markers?

## My take

This is a foundational atlas paper — the Tabula Sapiens-equivalent for human mononuclear phagocytes. The two principal contributions are (i) the consensus MoMac-VERSE / MNP-VERSE clusters with stable cross-tissue gene signatures, and (ii) the mechanistic characterisation of IL4I1⁺ TAMs as a T-cell-induced immunosuppressive node distinct from TREM2⁺ TAMs. For HypoxiaVERSE and the Calafell 2024 line of work, this paper provides the in vivo coordinate system on which mMAC1 / hypoxic-MAC signatures are projected; the IL4I1_Mac is the central anchor population. The strongest result is the multi-modal validation pipeline (transcriptomic clusters → SCENIC TF regulons → CITE-seq protein → flow cytometry → cross-species fate-mapping) that together establish IL4I1_Mac as a real tissue cell state, not just a gene-expression cluster. The weakest points are (a) the absence of a direct functional T-cell suppression assay on isolated IL4I1_Macs from human tumour tissue, and (b) the periphery-vs-core zonation conclusion being limited to liver and colon. This paper is a top-priority anchor for any thesis chapter on TAM heterogeneity, MNP atlases, or IFN-driven myeloid reprogramming.

## Related

- Concepts: [[concepts/momac-verse-mnp-verse-atlas]], [[concepts/il4i1-tumor-associated-macrophage]], [[concepts/trem2-tumor-associated-macrophage]], [[concepts/mononuclear-phagocyte-system]], [[concepts/macrophage-ontogeny-resident-vs-monocyte-derived]], [[concepts/m1-m2-polarization-paradigm]], [[concepts/tumor-associated-macrophage-immunosuppression]], [[concepts/mmac1-hypoxic-inflammatory-macrophage]]
- Foundations (methods): [[foundations/seurat-v3-integration]], [[foundations/scenic-tf-regulon-inference]], [[foundations/nichenet-ligand-target-inference]], [[foundations/azimuth-reference-mapping]]
- Foundations (biological): [[foundations/trem2-receptor]], [[foundations/ahr-ido1-tryptophan-axis]]
- Claims: [[claims/momac-verse-conserved-mnp-signatures-cross-tissue]], [[claims/trem2-tam-pancancer-accumulation-momac-verse]], [[claims/il4i1-tam-induced-by-ifng-cd40l-from-tcells]], [[claims/il4i1-tam-degrade-tryptophan-via-ahr-immunosuppression]], [[claims/il4i1-macrophages-vivo-correlates-mmac1]], [[claims/trem2-macrophages-associate-poor-cancer-prognosis]]
- People: [[people/kevin-mulder]], [[people/charles-antoine-dutertre]], [[people/camille-bleriot]], [[people/florent-ginhoux]]

- [[papers/dictionary-immune-responses-cytokines-single-cell]] — Cui & Hacohen et al. 2024 *Nature* Immune Dictionary + IREA: cytokine perturbational atlas; complementary cytokine-activity inference framework.
