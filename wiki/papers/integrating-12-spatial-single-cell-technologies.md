---
# === Identification ===
title: "Integrating 12 Spatial and Single Cell Technologies to Characterise Tumour Neighbourhoods and Cellular Interactions in three Skin Cancer Types"
slug: integrating-12-spatial-single-cell-technologies
arxiv: ""
doi: "10.1101/2025.07.25.666708"
pmid: "40766555"
venue: "bioRxiv"
year: 2025
authors: ["P. Prakrithi", "Laura F. Grice", "Feng Zhang", "Levi Hockey", "Samuel X. Tan", "Xiao Tan", "Zherui Xiong", "Onkar Mulay", "Andrew Causer", "Andrew Newman", "Duy Pham", "Guiyan Ni", "Kelvin Tuong", "Xinnan Jin", "Eunju Kim", "Minh Tran", "Hani Vu", "Nicholas M. Muller", "Emily E. Killingbeck", "Mark T. Gregory", "Siok Min Teoh", "Tuan Vo", "Min Zhang", "Maria Teresa Landi", "Kevin M. Brown", "Mark M. Iles", "Zachary Reitz", "Katharina Devitt", "Liuliu Pan", "Arutha Kulasinghe", "Yung-Ching Kao", "Michael Leon", "Sarah R. Murphy", "Hiromi Sato", "Jazmina Gonzalez Cruz", "Snehlata Kumari", "Hung N. Luu", "Sarah E. Warren", "Chris McMillan", "Joakim Henricson", "Chris Anderson", "David Muller", "Arun Everest-Dass", "Blake O'Brien", "Mathias Seviiri", "Matthew H. Law", "H. Peter Soyer", "Ian Frazer", "Youngmi Kim", "Mitchell S. Stark", "Kiarash Khosrotehrani", "Quan Nguyen"]
first_author: "P. Prakrithi"
corresponding_author: "Quan Nguyen"

# === Source & metadata ===
source_type: pdf
s2_id: "87a9509055032cdb5b434f194c71651a4b05c7db"
date_added: 2026-06-03
ingested_date: 2026-06-03
ingest_version: 1
last_reviewed:

# === Classification ===
importance: 4
tier: TIER_1
tags: [spatial-omics, multiomics, skin-cancer, single-cell, cell-cell-interaction, atlas, melanoma, cscc, bcc]
keywords: [spatial transcriptomics, ligand-receptor, tumour microenvironment, CD44, IL34-CSF1R, gsMAP, melanoma, keratinocyte cancer]
domain: oncology

# === Biomedical domain ===
tissue: [skin]
condition: [cancer, healthy]
disease_specific: [cutaneous_squamous_cell_carcinoma, basal_cell_carcinoma, melanoma]
species: [human]
hypoxia_relevant: false
contains_immune_cells: true
contains_myeloid: true

# === Technique ===
techniques: [scRNA-seq_10x, snRNA-seq, spatial_visium, Xenium, CosMx, GeoMx, CODEX, MALDI-MSI, RNAScope, PLA, Opal_Polaris]
n_samples: 24
n_cells_total: 200000
integration_method: "Harmony"

# === Biology captured ===
key_cell_types: [keratinocyte, melanocyte, fibroblast, T_cell, regulatory_T_cell, macrophage, dendritic_cell, endothelial_cell, NK_cell]
key_markers: [SOX2, CXCL9, CXCL10, CCL5, LAMP3, UBE2C, CD44, FGF2, IL34, CSF1R, SPP1, MLANA, TYR, MITF, MX2, PTCH1]
key_pathways: [collagen-integrin signaling, FGF-FGFR signaling, IL-17 pathway, WNT5A-FZD, Hedgehog, tyrosine metabolism, pyrimidine metabolism]

# === User project membership ===
projects: [thesis, skin]
priority: core
read_status: read

# === HypoxiaVERSE-specific ===
hypoxiaverse_status:
exclusion_reason:
data_availability: "Interactive resource at https://skincanceratlas.com (skInteractive)"

# === Cross-references ===
code_url: ""
cited_by: []
---

## Problem

The three major skin cancers — cutaneous squamous cell carcinoma (cSCC), basal cell carcinoma (BCC), and melanoma — together account for >70% of all cancers (European-ancestry populations) yet are rarely compared at single-cell and spatial resolution. Their microenvironments, the cellular interactions driving differential initiation/progression, and why most keratinocyte cancers are less invasive than melanoma remain poorly characterised. No prior data provided matched healthy/cSCC/BCC single-cell references, a benign-to-invasive melanoma continuum, or multimodal (RNA/protein/metabolite) spatial maps of these cancers.

## Key idea

Apply 12 complementary single-cell and spatial technologies to the same skin cancer samples to build *orthogonally-validated* cell signatures, spatial maps, and interactomes for cSCC, BCC, and melanoma — and integrate the result with population-scale genetics. Cross-validation across platforms that differ in resolution, sensitivity, and analyte class yields high-confidence findings and doubles as a practical guide to spatial-multiomics experimental design ([[concepts/spatial-multiomics-orthogonal-validation]]).

## Method

- **Cohort**: 24 donors — cSCC (n=7), BCC (n=4), melanoma (n=7, incl. n=3 snRNA-seq), non-cancer (n=3) plus 5 non-sun-exposed healthy skin samples. Up to 12 assays per biopsy.
- **Single-cell**: 10x Chromium scRNA-seq ([[scrna-seq-10x-chromium]]) of matched healthy/cSCC; FLEX snRNA-seq ([[snrna-seq-single-nucleus]]) of benign→dysplastic→invasive melanocytic lesions; Harmony integration ([[harmony-integration]]).
- **Spatial transcriptomics**: Visium ([[10x-visium-spatial-transcriptomics]]), Xenium ([[xenium-in-situ-spatial-transcriptomics]]), CosMx ([[cosmx-spatial-transcriptomics]]).
- **Spatial protein/metabolite**: GeoMx WTA/CTA + IO protein ([[geomx-digital-spatial-profiling]]), CODEX ([[codex-multiplexed-imaging]]), MALDI-MSI glycomics ([[maldi-msi-spatial-glycomics]]).
- **Malignant-cell calling**: consensus CNV inference ([[infercnv-cnv-scrna]]) + cancer module scores ([[addmodulescore-seurat]]) + spatial mapping.
- **Interactions**: CellChat ([[cellchat-cell-cell-communication]]) on scRNA-seq; spatially-constrained SCTP via stLearn ([[stlearn-sctp-spatial-lr]]); multi-platform integration via MMCCI ([[mmcci-multiplatform-cci]]) ([[concepts/spatially-constrained-ligand-receptor-inference]]).
- **Validation**: RNAScope/STRISH ([[rnascope-single-molecule-fish]]), Opal Polaris multiplex IHC ([[opal-polaris-multiplex-ihc]]), Proximity Ligation Assay ([[proximal-ligation-assay]]); prognosis via TCGA ([[tcga-the-cancer-genome-atlas]]).
- **Genetics**: gsMAP ([[gsmap-spatial-heritability]]) mapping cSCC/BCC/melanoma GWAS heritability onto spatial cell types/domains ([[concepts/spatial-gwas-heritability-cell-type-mapping]]).

## Results

A matched-condition cSCC atlas (45,909 cells; 19 immune subtypes) and a benign-to-invasive snRNA-seq melanoma reference were built and cross-validated against spatial data. A six-gene KC-cancer signature (SOX2, LAMP3, CXCL10, CXCL9, CCL5, UBE2C) was reproduced across four platforms. Cross-platform spatial integration defined a melanocyte-enriched meta-community ([[concepts/cross-platform-spatial-meta-community]]) with collagen-CD44 signalling and enriched tyrosine/pyrimidine metabolism. MMCCI yielded cancer-type-specific interactomes (16 BCC, 17 cSCC, 37 melanoma LR pairs), with melanoma dominated by collagen-integrin and FGF-CD44 ([[concepts/cd44-ecm-axis-melanoma-invasion]]) and differential fibroblast wiring across subtypes ([[concepts/differential-stromal-interactions-skin-cancer]]). IL34-CSF1R and CD44 interactions were experimentally validated (RNAScope/PLA), and gsMAP localised skin-cancer heritability to melanocytes, dysplastic/cornified keratinocytes, and fibroblasts.

## All claims (exhaustive)

- `[c01]` Matched healthy/cancer cSCC scRNA-seq atlas of 45,909 cells, 19 immune subtypes (p.4) "A total of 45,909 skin cells passed quality control... further identified 19 immune cell (sub)types" — confidence: high — type: methodological — links: [[claims/cscc-atlas-matched-healthy-cancer-45909-cells]] [[scrna-seq-10x-chromium]]
- `[c02]` Cancer KCs called by combined CNV polyploidy + module score; 745 cells, 82.6% dysplastic (p.5) "a cell was considered a cancer KC cell if the cell had abnormal polyploidy based on CNV analysis... and had high cancer module scores... we identified a total of 745 KC cancer cells" — confidence: high — type: methodological — links: [[claims/cancer-kc-identification-cnv-module-score]] [[infercnv-cnv-scrna]] [[addmodulescore-seurat]]
- `[c03]` snRNA-seq melanoma reference spans benign naevus → dysplastic → invasive; 10,747 nuclei, 118 melanoma cells (p.5) "From 10,747 single nuclei... we integrated CNV analysis, module scores, and spatial mapping of melanocytes to identify 118 melanoma cells" — confidence: high — type: methodological — links: [[claims/snrnaseq-melanoma-reference-benign-to-invasive]] [[snrna-seq-single-nucleus]]
- `[c04]` Between-lineage transcriptomic variation exceeds within-lineage (3257 vs 176 / 68 DE genes) (p.6) "3257 genes higher in cSCC than in melanomas... 176 genes upregulated in cancer KCs vs healthy KCs and 68 upregulated genes in melanoma cells compared to melanocytes" — confidence: medium — type: quantitative — links: [[claims/cancer-lineage-variation-exceeds-intralineage]]
- `[c05]` Six cross-platform-validated KC cancer markers: SOX2, LAMP3, CXCL10, CXCL9, CCL5, UBE2C (p.6) "we identified six consistently upregulated genes in KC cancer cells: SOX2, LAMP3 (CD208), CXCL10, CXCL9, CCL5, and UBE2C" — confidence: high — type: quantitative — links: [[claims/six-validated-kc-cancer-markers-multiplatform]] [[concepts/spatial-multiomics-orthogonal-validation]]
- `[c06]` SOX2 specifically marks KC cancer cells, absent in normal epithelium (p.6-7) "The transcription factor SOX2, absent in normal epithelial cells, is essential for cancer-initiating cells in cSCC" — confidence: medium — type: mechanistic — links: [[claims/sox2-marks-kc-cancer-cells]]
- `[c07]` KC cancer cells upregulate ECM-remodeling (MMPs/SERPINs) and IL-17 pathway genes (p.6) "extracellular matrix remodeling pathways... MMP1, MMP3, MMP10, MMP12, MMP13, SERPINB3... alongside IL-17 pathway components" — confidence: medium — type: correlational — links: [[claims/kc-cancer-ecm-remodeling-il17-signature]]
- `[c08]` Melanoma upregulates immune-evasion genes (CTLA4, CD274/PD-L1) vs melanocytes; CST6 down (p.7) "Genes associated with immune evasion, including CTLA4, CD274 (PD-L1)... CST6... a known suppressor of melanoma proliferation" — confidence: medium — type: correlational — links: [[claims/melanoma-immune-evasion-signature-vs-melanocytes]]
- `[c09]` Melanoma shows higher spatial cell-type heterogeneity than cSCC (Rao's Q) (p.8) "We detected a significant increase in cell type heterogeneity score in the melanoma samples compared to in cSCC cancer" — confidence: medium — type: quantitative — links: [[claims/melanoma-higher-spatial-heterogeneity-than-cscc]]
- `[c10]` Reproducible melanocyte-enriched meta-community (Visium_2, Xenium_2/7, CosMx_6), melanoma-enriched (p.9) "we identified a meta-community comprising Visium_2, Xenium_2, Xenium_7, and CosMX_6, all enriched for melanocytes" — confidence: high — type: methodological — links: [[claims/cross-platform-melanocyte-meta-community]] [[concepts/cross-platform-spatial-meta-community]]
- `[c11]` Melanoma community: collagen-CD44 signalling + enriched tyrosine and pyrimidine metabolism (p.9) "interactions were highly enriched for collagen signaling, especially between collagens and CD44... Tyrosine metabolism was enriched... Pyrimidine metabolism upregulated" — confidence: medium — type: mechanistic — links: [[claims/melanoma-community-collagen-cd44-tyrosine-pyrimidine]] [[maldi-msi-spatial-glycomics]] [[cd44-receptor]]
- `[c12]` Treg and fibroblasts co-localize with melanocytes in melanoma communities (p.9) "Treg and Fibroblasts have a high co-occurrence probability with melanocytes" — confidence: medium — type: correlational — links: [[claims/treg-fibroblast-colocalize-melanocytes-melanoma]] [[codex-multiplexed-imaging]]
- `[c13]` Spatial constraint removes scRNA-seq false-positive LR (XCL1-XCR1) and recovers missed ones (WNT5A-ROR1) (p.10) "interactions that were predicted by scRNAseq but no colocalization was observed, suggesting possible false detection (e.g., XCL1-XCR1)" — confidence: high — type: methodological — links: [[claims/spatial-constraint-reduces-false-lr-interactions]] [[stlearn-sctp-spatial-lr]] [[concepts/spatially-constrained-ligand-receptor-inference]]
- `[c14]` Melanoma dominated by collagen-integrin (15/37) and FGF-CD44/FGFR (6/37) LR pairs (p.10-11) "37 in melanoma... making 15 out of all the 37 LR pairs... collagen interactions... Fibroblast Growth Factor, with six out of 37 interactions" — confidence: high — type: quantitative — links: [[claims/melanoma-collagen-integrin-fgf-cd44-interactions]] [[mmcci-multiplatform-cci]] [[concepts/cd44-ecm-axis-melanoma-invasion]]
- `[c15]` cSCC enriched for SPP1-integrin/CD44; BCC for WNT (WNT5A-FZD) and angiogenesis (p.10-11) "For cSCC, strong enrichment of Osteopontin (SPP1)... For BCC... WNT5A-FZD7 and WNT5A-FZD8... appeared to be more active in BCC" — confidence: medium — type: correlational — links: [[claims/cscc-spp1-integrin-bcc-wnt-angiogenesis-interactions]] [[spp1-secreted-phosphoprotein-1]] [[mapk1-3-erk1-2-kinases]]
- `[c16]` Fibroblast-T-cell interactions stronger in cSCC/BCC; fibroblast-melanocyte stronger in melanoma (p.11) "stronger fibroblast to T cells interaction in cSCC and BCC compared to in melanoma, whereas the fibroblast to melanocyte interaction was higher in melanoma" — confidence: medium — type: correlational — links: [[claims/differential-fibroblast-interactions-skin-cancers]] [[cancer-associated-fibroblast]] [[concepts/differential-stromal-interactions-skin-cancer]]
- `[c17]` IL34-CSF1R elevated in melanoma, RNAScope/STRISH-validated, antigen-presentation/lipid linked (p.12) "We found co-localisation of IL34 and CSF1R by RNAScope analysis... enrichment of the antigen processing pathway and lipid metabolism" — confidence: high — type: methodological — links: [[claims/il34-csf1r-elevated-melanoma-validated]] [[csf1r-receptor]] [[rnascope-single-molecule-fish]]
- `[c18]` CD44 dominant melanoma receptor; CD44-MMP9/FN1/FGF2 PLA-validated; CD44-FGF2 candidate target; TCGA prognostic (p.12) "focusing on CD44, a dominant receptor found with distinctively more common interactions in melanoma... we validated CD44-MMP9, CD44-FN1, and CD44-FGF2 interactions" — confidence: medium — type: pharmacological — links: [[claims/cd44-fgf2-melanoma-therapeutic-target-pla-validated]] [[cd44-receptor]] [[proximal-ligation-assay]] [[tcga-the-cancer-genome-atlas]]
- `[c19]` gsMAP maps skin-cancer GWAS heritability: melanoma→melanocytes/KC-diff; cSCC/BCC→KC-dysplastic/hair/cornified; fibroblast across all (p.13-14) "top association for melanoma included melanocytes and KC differentiating. Fibroblast consistently displayed a strong association signal" — confidence: high — type: methodological — links: [[claims/gsmap-skin-cancer-heritability-cell-type-mapping]] [[gsmap-spatial-heritability]] [[concepts/spatial-gwas-heritability-cell-type-mapping]]
- `[c20]` First spatial multiomics atlas of cSCC/BCC/melanoma integrating 12 technologies; public resource (p.1/14) "we integrated 12 complementary spatial single-cell technologies to construct orthogonally-validated cell signatures, spatial maps, and interactomes for cSCC, BCC, and melanoma" — confidence: high — type: methodological — links: [[claims/first-spatial-multiomics-skin-cancer-atlas-resource]] [[concepts/spatial-multiomics-orthogonal-validation]]

## Discussion captured

### Authors' interpretation

The authors argue that cross-validation across 12 orthogonal technologies (complementary in resolution, sensitivity, throughput, and analyte class) yields high-confidence biology unattainable by any single platform, and that the work provides a general guideline for spatial multiomics experimental design beyond skin cancer. They interpret the dominance and differential wiring of fibroblast interactions as a candidate explanation for the differing metastatic potential of the three cancers, and frame dysplastic melanocytes "shedding" regulatory keratinocyte interactions as a route to uncontrolled proliferation.

### Comparisons with prior literature (made by authors)

- Foundational single-cell atlases of BCC (Guerrero-Juarez 2022; Yerly 2022; Huang 2023; Ganier 2024), cSCC (Ji 2020; Yan 2021; Zou 2023) and melanoma (Tirosh 2016; Jerby-Arnon 2018; Karras 2022; Pozniak 2024) are cited as characterising each cancer individually but never comparing them.
- PTCH1 defective in 70-85% of BCC but not cSCC (Boukamp 2005; Bonilla 2016) is cited to argue loss of PTCH1 signalling predisposes toward BCC over cSCC.
- Fibroblast roles in skin cancer initiation/progression (Flach 2011; Kim 2013; Ayuso 2021; Wang 2012/2016; Werner 2007; Van Hove 2022) are cited to contextualise the differential fibroblast interactome.
- gsMAP method from Song et al., 2024; GWAS from Seviiri 2022 (cSCC/BCC) and Landi 2020 (melanoma).

### Mechanistic hypotheses proposed

- "loss of PTCH1 signalling may predispose a cell towards initiating BCC over cSCC" (p.16).
- Some melanoma risk loci "may be mediated by cis-regulation in keratinocytes, which are involved in tightly controlling melanocyte proliferation and invasion" (p.17).
- CD44 acts as an MMP9 docking receptor localising protease to the cell surface to degrade collagen and enhance invasion (p.12).

### Caveats and self-criticism

- Sample size is small (24 patients total); new findings from this cohort "would require future validation to external cohorts" (p.18).
- Heterogeneity assessment "would require bigger sample cohorts" (p.8).
- RNA-based interaction approaches "remain as an inference test, but not a direct proof of protein-protein interactions" (p.17); Opal Polaris co-localisation "lacks the resolution to find exact interactions" (addressed by PLA at 20 nm).
- CODEX could not map keratinocyte cell types due to lack of protein markers (p.8).

### Future directions suggested

- Validate additional ligand-receptor pairs where antibodies are available (p.13).
- Use the resource to interpret pathways where DNA mutations are known but single-cell/spatial manifestation is not (MAPK in melanoma, Hedgehog in BCC, NOTCH/p53 in cSCC) (p.18).
- Deeper study of cancer-associated fibroblasts and EMT-fibroblasts in BCC/cSCC progression (p.15).

## Limitations

- Small cohort (24 donors; as few as 2-4 patients per cancer type for some spatial comparisons).
- Many key interactions are computational inferences; only a few (CD44-MMP9/FN1/FGF2, IL34-CSF1R) are experimentally validated.
- Partially overlapping gene/protein panels across platforms complicate direct cross-platform comparison; CODEX lacks KC markers; glycomics cell typing is coarse.
- Melanoma single-cell numbers are very low (118 cells), limiting DE power.
- bioRxiv preprint, not peer-reviewed (CC-BY-ND), as of this ingest.

## Open questions

### Open questions raised by authors

- Which factors differentiate progressor from non-progressor actinic-keratosis/naevus lesions?
- Why are most cSCCs and BCCs less invasive than melanoma, and does differential fibroblast wiring explain it?
- Can risk loci be mechanistically attributed to keratinocyte cis-regulation of melanocytes?

### Open questions identified during ingest

- Do the cross-platform-validated markers (SOX2, CXCL9/10, CCL5, LAMP3, UBE2C) hold as KC-cancer-intrinsic in larger cohorts, controlling for immune infiltrate?
- Is CD44-FGF2 a tractable therapeutic target in functional melanoma models, beyond proximity validation?
- Does the melanoma spatial heterogeneity difference associate with clinical outcome?

## My take

A landmark resource paper: ambitious 12-technology integration, a genuinely novel benign-to-invasive melanoma reference, and a clean computation→validation arc for CD44 and IL34-CSF1R. Directly relevant to the user's skin/thesis work — both as a spatial-multiomics methods template and as a source of skin-cancer TME biology. The headline limitation is cohort size; the GWAS integration partly offsets this for generalisability. The methodological concepts (orthogonal cross-platform validation, spatially-constrained LR inference, cross-platform meta-communities, spatial heritability mapping) are reusable well beyond skin.

## Related

Concepts: [[concepts/spatial-multiomics-orthogonal-validation]], [[concepts/spatially-constrained-ligand-receptor-inference]], [[concepts/cross-platform-spatial-meta-community]], [[concepts/spatial-gwas-heritability-cell-type-mapping]], [[concepts/differential-stromal-interactions-skin-cancer]], [[concepts/cd44-ecm-axis-melanoma-invasion]]

Foundations (methods): [[10x-visium-spatial-transcriptomics]], [[xenium-in-situ-spatial-transcriptomics]], [[cosmx-spatial-transcriptomics]], [[geomx-digital-spatial-profiling]], [[codex-multiplexed-imaging]], [[maldi-msi-spatial-glycomics]], [[scrna-seq-10x-chromium]], [[snrna-seq-single-nucleus]], [[harmony-integration]], [[infercnv-cnv-scrna]], [[addmodulescore-seurat]], [[cellchat-cell-cell-communication]], [[stlearn-sctp-spatial-lr]], [[mmcci-multiplatform-cci]], [[gsmap-spatial-heritability]], [[rnascope-single-molecule-fish]], [[opal-polaris-multiplex-ihc]], [[proximal-ligation-assay]], [[tcga-the-cancer-genome-atlas]]

Foundations (biology): [[cd44-receptor]], [[csf1r-receptor]], [[spp1-secreted-phosphoprotein-1]], [[cancer-associated-fibroblast]], [[mapk1-3-erk1-2-kinases]]

People: [[people/quan-nguyen]], [[people/p-prakrithi]], [[people/laura-f-grice]], [[people/feng-zhang-qimr]], [[people/ian-frazer]]
