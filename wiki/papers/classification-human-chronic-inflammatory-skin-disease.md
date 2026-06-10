---
# === Identification ===
title: "Classification of human chronic inflammatory skin disease based on single-cell immune profiling"
slug: classification-human-chronic-inflammatory-skin-disease
arxiv: ""
doi: "10.1126/sciimmunol.abl9165"
pmid: "35427179"
venue: "Science Immunology"
year: 2022
authors: ["Yale Liu", "Hao Wang", "Mark Taylor", "Christopher Cook", "Alejandra Martínez-Berdeja", "Jeffrey P. North", "Paymann Harirchian", "Ashley A. Hailer", "Zijun Zhao", "Ruby Ghadially", "Roberto R. Ricardo-Gonzalez", "Roy C. Grekin", "Theodora M. Mauro", "Esther Kim", "Jaehyuk Choi", "Elizabeth Purdom", "Raymond J. Cho", "Jeffrey B. Cheng"]
first_author: "Yale Liu"
corresponding_author: "Raymond J. Cho; Jeffrey B. Cheng"

# === Source & metadata ===
source_type: pdf
s2_id: "af222fcea0e4154e2e86cb2b48eff7941750ba8e"
date_added: 2026-06-10
ingested_date: 2026-06-10
ingest_version: 1
last_reviewed:

# === Classification ===
importance: 4
tier: TIER_1
tags: [immunology, skin, scrna-seq, cite-seq, atopic-dermatitis, psoriasis, trm, classification, dupilumab]
keywords: [inflammatory skin disease, single-cell RNA-seq, resident memory T cells, TH2/TH17, molecular endotyping, RashX]
domain: immunology

# === Biomedical domain ===
tissue: [skin]
condition: [autoimmune]
disease_specific: [atopic_dermatitis, psoriasis_vulgaris, lichen_planus, bullous_pemphigoid]
species: [human]
hypoxia_relevant: false
contains_immune_cells: true
contains_myeloid: true

# === Technique ===
techniques: [scRNA-seq_10x, CITE-seq]
n_samples: 31
n_cells_total: 158037
integration_method: "Harmony"

# === Biology captured ===
key_cell_types: [Trm1, Trm2, Trm3, eTreg, cmTreg, CTLac, CTLex, ILC2, NK, Langerhans cells, macrophages, moDC, DC, monocytes, mast cells, B cells, plasma cells]
key_markers: [ITGAE/CD103, CD69, CXCR6, FOXP3, IL17F, CXCL13, GNLY, CTLA4, PDCD1, LAG3, GZMB, TWIST1, IL17RB, KMT2A, NEAT1]
key_pathways: [TH2 signaling, TH17/IL-17 signaling, T cell exhaustion, Treg regulation]

# === User project membership ===
projects: [skin, thesis]
priority: context
read_status: not_read

# === HypoxiaVERSE-specific ===
hypoxiaverse_status:
exclusion_reason:
data_availability: ""

# === Cross-references ===
code_url: "https://rashX.ucsf.edu"
cited_by: []
---

## Problem

Inflammatory conditions are the largest class of chronic skin disease, but the molecular dysregulation underlying many individual cases is unclear. Atopic dermatitis (AD, TH2-skewed) and psoriasis vulgaris (PV, TH1/TH17-skewed) are prototypical, yet 20-50% of patients fail a given targeted biologic and many adult rashes are clinically/histopathologically indeterminate. Bulk profiling conflates cell types and yields poorly reproducible disease signatures, leaving no reliable patient-level molecular classification or objective basis for therapy selection.

## Key idea

By restricting analysis to cutaneous CD45+ immune cells and using high analytic resolution (41 immune cell classes), scRNA-seq + CITE-seq can localize disease-discriminating transcriptional abnormalities to a specific population — skin-resident memory T cells (Trm1) — and build TH2/TH17 gene signatures that classify rash type at the patient level, including for clinically ambiguous cases, with results that track therapeutic response. The approach is packaged as a public web portal (RashX).

## Method

Flow-sorted live CD45+ cells from 31 skin samples (8 PV, 7 AD, 2 LP, 1 BP, 6 CIR, 7 HC) were profiled by 10x Chromium 3' scRNA-seq with CITE-seq protein epitopes. After Cell Ranger alignment (GRCh38, or GRCh38+mm10 for murine spike-in), QC, scDblFinder doublet removal, HVG selection, and Harmony batch integration, Seurat Louvain clustering (clustree-guided) plus iterative subclustering yielded 41 immune classes. Compositional shifts were tested with a weighted Gaussian linear model; differential expression used MAST with an 80%-of-samples heterogeneity filter (|avg_log2FC| > 0.425, adj P < 0.001). Disease-specific Trm1 gene sets were scored with AddModuleScore and analyzed in qgraph coexpression and STRING PPI networks (normalized-cut permutation test). Samples were placed on a TH2/TH17 hyperdimensional plane and classified by Canberra distance to AD/PV centroids (Mann-Whitney).

## Results

Inflammation drove a relative lymphoid increase and myeloid decrease, with 27/41 clusters significantly altered: exhausted CD8+ T cells (CTLex +80.4%), all three Treg classes (2.19-3.13×), and Trm classes (Trm1 +71.4%, Trm2 +108.7%) expanded, with active proliferation of cycling counterparts. Trm1 harbored the most disease-discriminating DEGs; AD/PV signatures localized specifically to CD69+CD103+ Trm cells. PV-specific genes (IL17F, CXCL13, GNLY, CTLA4) concentrated in Trm1/Trm3; AD-specific genes (TWIST1, IL17RB, KMT2A, NEAT1) in Trm, ILC, and effector CTLs. The two signature modules segregated discretely in coexpression and STRING networks (P = 0.001) and accurately classified an external validation cohort. Molecular stratification of indeterminate rashes (CIRs) tracked dupilumab response, and BP/LP segregated with AD/PV respectively. RashX deploys the framework publicly.

## All claims (exhaustive)

- `[c01]` A 31-sample CD45+ scRNA-seq/CITE-seq dataset yielded 158,037 cells (p.2) "We obtained transcriptomic data from 158,037 single cells after quality control filtering" — confidence: high — type: quantitative — links: [[claims/31-patient-cd45-scrna-seq-dataset]] [[foundations/scrna-seq-10x-chromium]] [[foundations/cite-seq-citeseq]]
- `[c02]` Iterative subclustering defined 41 cutaneous immune cell classes (p.2) "this classification generated 41 final clusters" — confidence: high — type: methodological — links: [[claims/41-cutaneous-immune-cell-classes-defined]] [[foundations/louvain-community-detection-clustering]] [[foundations/clustree-clustering-resolution-selection]]
- `[c03]` Exhausted CD8+ T cells (CTLex) increase 80.4% in chronic inflammatory skin disease (p.3) "CTLex class up 80.4%, from 4.5 to 8.2%" — confidence: high — type: quantitative — links: [[claims/exhausted-cd8-cells-increase-chronic-inflammatory]] [[foundations/pd-1-receptor-pdcd1]] [[concepts/treg-trm-expansion-cd8-exhaustion-chronic]]
- `[c04]` All three Treg classes expand 2.19-3.13 fold in rashes (p.3) "a substantial expansion of all three Treg classes (2.19- to 3.13-fold)" — confidence: high — type: quantitative — links: [[claims/all-three-treg-classes-expand-rash]] [[foundations/foxp3-tf]] [[concepts/treg-trm-expansion-cd8-exhaustion-chronic]]
- `[c05]` Resident memory T cell classes (Trm1, Trm2) increase in rashes (p.3) "Trm1 up 71.4% from 6.3 to 10.7% and Trm2 up 108.7% from 4.3 to 9.0%" — confidence: high — type: quantitative — links: [[claims/resident-memory-cell-classes-increase-rash]] [[foundations/itgae-cd103-integrin-trm-marker]] [[concepts/tissue-resident-memory-cd8-t-cell-trm]]
- `[c06]` Mitotically active immune clusters expand, indicating local proliferation (p.3) "Mitotically active cell clusters were markedly expanded in rashes, revealing active proliferation of Trm, Treg, ILC/NK, and CD8+ T cell populations" — confidence: high — type: mechanistic — links: [[claims/mitotically-active-immune-clusters-expand-lesional]] [[concepts/treg-trm-expansion-cd8-exhaustion-chronic]]
- `[c07]` Inflammation shifts skin immune composition toward lymphoid and away from myeloid (p.3) "inflammation was accompanied by relative increases in multiple lymphoid cell classes and proportionate decreases in myeloid populations" — confidence: high — type: correlational — links: [[claims/inflammation-shifts-skin-immune-composition-toward]] [[concepts/treg-trm-expansion-cd8-exhaustion-chronic]]
- `[c08]` Exhausted CD8+ and NK cells are more elevated in PV than AD (p.4) "CTLex and NK cells were more elevated in PV than in AD (in PV versus HC samples, up by 74.6 and 99.4%, respectively)" — confidence: high — type: correlational — links: [[claims/exhausted-cd8-nk-cells-more-elevated]] [[concepts/treg-trm-expansion-cd8-exhaustion-chronic]]
- `[c09]` Trm1 harbors the most disease-discriminating DEGs (p.4) "Trm1 had a disproportionately large number of DEGs in the three comparisons (e.g., in the PV versus HC comparison, 514 DEGs for Trm1 cells)" — confidence: high — type: quantitative — links: [[claims/trm1-harbors-most-disease-discriminating-degs]] [[foundations/mast-hurdle-model-single-cell-differential]] [[concepts/trm1-th2-th17-molecular-classification-inflammatory]]
- `[c10]` AD/PV disease-specific signatures localize to CD69+CD103+ Trm cells (p.8) "both our AD and PV disease-specific transcriptional signatures were only found in CD69+ CD103+-resident memory T cells" — confidence: high — type: mechanistic — links: [[claims/ad-pv-transcriptional-signatures-localize-cd69]] [[foundations/itgae-cd103-integrin-trm-marker]] [[concepts/trm1-th2-th17-molecular-classification-inflammatory]]
- `[c11]` PV-specific upregulated genes (IL17F, CXCL13, GNLY, CTLA4) concentrate in Trm1/Trm3 (p.4) "PV-specific up-regulated genes were heavily concentrated in skin-resident memory classes Trm1 and Trm3 ... include granulysin GNLY and CTLA4" — confidence: high — type: correlational — links: [[claims/pv-specific-upregulated-genes-concentrate-resident]] [[foundations/il-17a-il17f-cytokines]] [[foundations/cxcl13-chemokine]]
- `[c12]` AD-specific upregulated genes (TWIST1, IL17RB, KMT2A, NEAT1) localize to Trm, ILC, effector CTLs (p.5) "Skin-resident memory classes also prominently expressed AD-specific up-regulated DEGs, including the known TH1-inhibiting transcriptional regulator TWIST1, IL17RB ... MLL1 (KMT2A) ... the lncRNA NEAT1" — confidence: high — type: correlational — links: [[claims/ad-specific-upregulated-genes-localize-trm]] [[concepts/trm1-th2-th17-molecular-classification-inflammatory]]
- `[c13]` AD/PV-specific Trm1 genes segregate discretely in coexpression and STRING networks (p.5) "These two groups showed significantly smaller linkages between the two groups than in multiple permutation tests ... (P = 0.001)" — confidence: high — type: methodological — links: [[claims/ad-pv-specific-trm1-genes-segregate]] [[foundations/string-protein-protein-interaction-database]] [[foundations/qgraph-network-visualization]]
- `[c14]` Trm1 DEG signatures classify rash type in an external validation dataset (p.6) "our disease-specific DEGs accurately identified the two rash types in the Reynolds et al. dataset" — confidence: high — type: methodological — links: [[claims/trm1-deg-signatures-classify-rash-type]] [[foundations/addmodulescore-seurat]] [[concepts/trm1-th2-th17-molecular-classification-inflammatory]]
- `[c15]` Molecular rash stratification matched dupilumab clinical response (p.6) "CIR-A and CIR-B, the dupilumab-responsive cases, segregated more closely with AD ... The lone dupilumab failure, CIR-E, segregated with PV" — confidence: medium — type: pharmacological — links: [[claims/molecular-rash-stratification-matches-dupilumab-clinical]] [[foundations/dupilumab-anti-il4ra]] [[concepts/molecular-stratification-indeterminate-rash-predicts-dupilumab]]
- `[c16]` BP segregates with AD and LP with PV by the Trm1 signature (p.6) "we saw the BP sample segregate more closely with AD and the LP samples with PV" — confidence: medium — type: correlational — links: [[claims/bullous-pemphigoid-segregates-ad-lichen-planus]] [[concepts/trm1-th2-th17-molecular-classification-inflammatory]]
- `[c17]` Exhausted CD8+ T cells are a shared end state, not a disease-discriminating force (p.8) "these cells harbored relatively few distinguishing abnormalities between disease classes, suggestive of a shared end state rather than a causative force" — confidence: medium — type: mechanistic — links: [[claims/exhausted-cd8-cells-shared-end-state]] [[concepts/cd8-t-cell-exhaustion-texterm]]
- `[c18]` The RashX portal classifies external rash scRNA-seq within the TH2/TH17 framework (p.8) "Example web portal outputs showed that these samples segregated closely to their parent class" — confidence: high — type: methodological — links: [[claims/rashx-portal-classifies-external-rash-scrna]] [[concepts/rashx-rash-classification-web-portal]]

## Discussion captured

### Authors' interpretation

The authors interpret proliferation-driven Treg/Trm expansion plus universal cytotoxic exhaustion as a shared architecture of chronic skin inflammation, on which disease-specific TH2/TH17 transcriptional programs are superimposed within Trm cells. They argue that prior bulk studies failed to reproducibly distinguish AD and PV because cell-type conflation obscured the Trm-restricted signal, and that Tregs proliferate to control inflammation but are qualitatively unable to do so.

### Comparisons with prior literature (made by authors)

- They validate against and compare to Reynolds et al. (ref 12) skin scRNA-seq atlas (external AD/PV cohort).
- Consistency with prior AD scRNA-seq (type 2/22 T cells, inflammatory DCs, Trm; refs 11, 12, 14, 15) and PV TH17/Tc17, CXCL13+ Tc17 findings (refs 9, 12).
- BP's type-2 inflammation and dupilumab responsiveness (ref 73); LP TH1/TH17 activity and IL17-antagonist response (refs 74, 75).
- Trm functional importance: psoriatic skin grafting onto mice (refs 69, 70), Trm in arthritis flares (ref 71), pulmonary Trm fibrosis after influenza (ref 72).

### Mechanistic hypotheses proposed

- "Tregs usually proliferate in rashes in an attempt to control pathogenic skin inflammation but ... one or more qualitative factors prevented successful regulation" (p.8).
- Cytotoxic exhaustion is "a shared end state rather than a causative force" (p.8).
- KMT2A (MLL1) and NEAT1 are flagged as candidate epigenetic/lncRNA maintainers of the TH2 memory program (p.5).

### Caveats and self-criticism

- Covariates (age, anatomic location) may add variability given the relatively small cohort.
- Unbiased CD45+ profiling leaves APC populations with too few cells to detect their unique abnormalities.
- CIR therapeutic-response inference rests on a very small test set.

### Future directions suggested

- Larger cohorts to detect complementary signatures in other subpopulations and validate T-cell discoveries.
- Integrate scRNA-seq with TCR clonality assessment.
- Larger unbiased therapeutic trials using the precision-medicine stratification; growth of a worldwide inflammatory-skin scRNA-seq resource.

## Limitations

- Small per-disease sample sizes (notably 1 BP, 2 LP); compositional estimates are relative, not absolute.
- MAST treats cells as independent samples, inflating significance; mitigated but not eliminated by the 80% heterogeneity filter.
- APC clusters underpowered (often <100 cells/sample).
- Classification validated on a small external cohort; portal accuracy not benchmarked at scale.

## Open questions

### Open questions raised by authors

- Can complementary disease signatures be recovered in non-Trm populations with deeper sampling?
- Will molecular class predict drug response in larger prospective trials?
- How does TCR clonality refine the inflammatory-dysregulation picture?

### Open questions identified during ingest

- Do the AD/PV Trm modules map onto distinct druggable pathway hubs (via the STRING modules)?
- Is the TH2/TH17 two-axis model adequate for dermatoses outside the AD-PV-BP-LP spectrum?
- Are Trm cells causal drivers or faithful reporters of disease-specific programs?

## My take

A clean demonstration that cell-type-restricted single-cell signatures can recover patient-level disease class where bulk profiling and even histopathology fail, with a genuine translational artifact (RashX). For thesis/skin work it is a strong reference template for molecular endotyping: the compositional shifts are a useful shared-inflammation null model, and the Trm1-restricted signature is the discriminating signal. The clinical-prediction claims are proof-of-principle scale and should be treated as hypotheses.

## Related

### Concepts introduced
- [[concepts/trm1-th2-th17-molecular-classification-inflammatory]]
- [[concepts/treg-trm-expansion-cd8-exhaustion-chronic]]
- [[concepts/rashx-rash-classification-web-portal]]
- [[concepts/molecular-stratification-indeterminate-rash-predicts-dupilumab]]

### Concepts used
- [[concepts/tissue-resident-memory-cd8-t-cell-trm]]
- [[concepts/cd8-t-cell-exhaustion-texterm]]

### Foundations
- [[foundations/scrna-seq-10x-chromium]] · [[foundations/cite-seq-citeseq]] · [[foundations/cell-ranger-10x-alignment]] · [[foundations/harmony-integration]] · [[foundations/seurat-v3-integration]] · [[foundations/louvain-community-detection-clustering]] · [[foundations/clustree-clustering-resolution-selection]] · [[foundations/scdblfinder-doublet-detection]] · [[foundations/hvg-selection-scrna]] · [[foundations/mast-hurdle-model-single-cell-differential]] · [[foundations/addmodulescore-seurat]] · [[foundations/umap-dimensionality-reduction]] · [[foundations/string-protein-protein-interaction-database]] · [[foundations/qgraph-network-visualization]]
- [[foundations/atopic-dermatitis]] · [[foundations/psoriasis-disease]] · [[foundations/itgae-cd103-integrin-trm-marker]] · [[foundations/foxp3-tf]] · [[foundations/il-17a-il17f-cytokines]] · [[foundations/cxcl13-chemokine]] · [[foundations/pd-1-receptor-pdcd1]] · [[foundations/gzmb-granzyme]] · [[foundations/dupilumab-anti-il4ra]]

### People
- [[people/yale-liu]] · [[people/raymond-cho]] · [[people/jeffrey-cheng]] · [[people/elizabeth-purdom]]
