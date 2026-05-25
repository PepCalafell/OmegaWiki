---
title: "The pan-cancer proteome atlas, a mass spectrometry-based landscape for discovering tumor biology, biomarkers, and therapeutic targets"
slug: pan-cancer-proteome-atlas-mass-spectrometry
arxiv: ""
doi: "10.1016/j.ccell.2025.05.003"
pmid: "40446800"
venue: "Cancer Cell"
year: 2025
authors:
  - Jaco C. Knol
  - Mengge Lyu
  - Franziska Böttger
  - Madalena Nunes Monteiro
  - Thang V. Pham
  - Frank Rolfs
  - Andrea Vallés-Martí
  - Tim Schelfhorst
  - Richard R. de Goeij-de Haas
  - Irene V. Bijnsdorp
  - Shuaiyao Wang
  - Fangfei Zhang
  - Jun A
  - Bart A. Westerman
  - Barbara Sitek
  - Janne Lehtiö
  - Jan Koster
  - Jan N. M. IJzermans
  - Hanneke W. M. van Laarhoven
  - Maarten F. Bijlsma
  - Jan Paul Medema
  - Alex A. Henneman
  - Sander R. Piersma
  - Ruud H. Brakenhoff
  - Jacqueline Cloos
  - Valentina Cordo'
  - Daphne de Jong
  - Geert Kazemier
  - Danijela Koppers-Lalic
  - Mariette Labots
  - Tessa Y. S. Le Large
  - John W. M. Martens
  - Jules P. P. Meijerink
  - Xiaolu Zhan
  - Tiannan Guo
  - Connie R. Jimenez
first_author: "Jaco C. Knol"
corresponding_author: "Tiannan Guo; Connie R. Jimenez"

source_type: pdf
s2_id: "be21de01a71656e539e54d063362a48f1825117b"
date_added: 2026-05-25
ingested_date: 2026-05-25
ingest_version: 1
last_reviewed:

importance: 4
tier: TIER_1
tags: [pan-cancer, proteomics, dia-ms, tpcpa, biomarkers, drug-targets, cms, immune-subtypes, cup-classifier, protac, wgcna]
keywords: [pan-cancer proteome, DIA-MS, TPCPA, WGCNA, ESTIMATE, ssGSEA, Tamborero, CMS, immune consensus cluster, cancer of unknown primary, E3 ligase, PROTAC, SDC1, HSP90, GFPT1, HERC5, RNF5]
domain: oncology

tissue: [blood, bone_marrow, lung, colon, stomach, liver, pancreas, kidney, ovary, bladder, prostate, breast, brain, skin, head_and_neck, esophagus, multi]
condition: [cancer]
disease_specific: [colorectal_cancer, B_ALL, T_ALL, AML, DLBCL, melanoma, ovarian_cancer, pancreatic_cancer, kidney_cancer, breast_cancer]
species: [human]
hypoxia_relevant: true
contains_immune_cells: true
contains_myeloid: true

techniques: [DIA-MS, LC-MS, single-shot_proteomics, bulk_RNA-seq]
n_samples: 999
n_cells_total:
integration_method: ""

key_cell_types: [bulk_tumour_tissue, CD8_T, T_helper, Treg, macrophage, neutrophil, eosinophil, mast_cell, B_cell, NK_CD56bright, NK_CD56dim]
key_markers: [SDC1, HERC5, RNF5, GFPT1, GFPT2, HSP90AA1, HSP90AB1, LRPPRC, PINK1, PMPCB, DOCK2, PTPN6, CTNNB1, BCL7A, IKZF1, SEPTIN6, PTPRC, PAX5, PASK, PTPRK, EGFR, ERBB3, IL16, ARHGAP25]
key_pathways: [Wnt_signaling, hexosamine_biosynthesis, O-GlcNAcylation, antigen_presentation, MTORC1, ROS_pathway, p53_pathway, hypoxia, EMT, mitochondrial_translation, peroxisome_metabolism, ubiquitin_proteasome]

projects: [thesis]
priority: reference
read_status: skimmed

hypoxiaverse_status:
exclusion_reason:
data_availability: "Interactive TPCPA portal at http://r2platform.com/TPCPA; raw DIA-MS data deposited via repository links in the paper."

code_url: ""
cited_by: []
---

## Problem
Most cancer proteomics studies to date have focused on single cancer types using TMT-multiplexed workflows that cap the number of cross-cohort sample groups that can be balanced in a single experiment. Genomic and transcriptomic atlases (TCGA, ICGC) do not directly measure protein-level abundance — the layer where most therapies act. A unified, high-throughput pan-cancer protein atlas is missing, leaving open the question of how cross-cancer protein signatures relate to tissue identity, prognostic biology, and therapeutic targeting.

## Key idea
Use single-shot data-independent acquisition mass spectrometry (DIA-MS) to generate a uniform pan-cancer proteome dataset across 22 cancer types and 999 primary tumours, then mine it with unsupervised clustering (UMAP, hierarchical), hallmark and immune ssGSEA, WGCNA co-expression, supervised pan-cancer DE, and a 75-feature multi-cancer classifier — to surface pan-cancer biology, candidate biomarkers, candidate therapeutic targets (including PROTAC-handle E3 ligases), CRC consensus molecular subtype protein markers with immune-cluster refinement, and a cancers-of-unknown-primary (CUP) classifier.

## Method
- **Cohort**: 1,236 DIA raw files → 1,172 QC-pass → 999 primary cancer samples spanning 22 cancer types (18 solid + 4 liquid); 11,250 protein groups identified, 9,670 quantified after filtering (≥5 samples / cancer type, ≥30% data presence). FF and FFPE inputs across two laboratories (Amsterdam UMC, Westlake).
- **Acquisition**: single-shot LC-[[foundations/dia-ms-data-independent-acquisition]] without sample multiplexing.
- **Unsupervised analysis**: UMAP and hierarchical clustering on the 20% most variable proteins; HeLa cell-line QC samples for cross-batch anchoring.
- **Enrichment**: [[foundations/ssgsea-single-sample-gsea]] of MSigDB cancer hallmarks; [[foundations/estimate-stromal-immune-score]] for stromal and immune scoring; [[foundations/tamborero-immune-signatures]] for immune-cell-subset inference.
- **Network**: [[foundations/wgcna-weighted-gene-coexpression]] on protein expression → 13 modules; module hubs = top 5 proteins by eigenprotein correlation.
- **Deconvolution comparison**: [[foundations/cibersortx-deconvolution]] (CIBERSORT) and EPIC tested on bulk proteome — performed poorly relative to Tamborero ssGSEA.
- **Supervised pan-cancer DE**: blood vs solid; each cancer type vs the rest within its solid/non-solid class.
- **CUP classifier**: 75 features (top 25 per cancer of 17 solid types), multi-class model with feature-score thresholding; validated on CPTAC kidney, independent DIA breast ([[foundations/cptac-clinical-proteomic-tumor-atlas]]), and on 28 metastatic ovarian + 32 metastatic CRC cohorts.
- **CRC analysis**: 195 CRC samples assigned to [[foundations/cms-classifier-crc]] subtypes from matched RNA; protein-level CMS DE; Tamborero-ssGSEA-based hierarchical clustering → immune consensus clusters CC1/CC2 (CC3 NKI-specific) and recurrence-free survival analysis on AMC stage-2 and EMC stage-1/2 cohorts. Cross-validation at RNA level on independent material via [[foundations/tcga-the-cancer-genome-atlas]] and the TPCPA portal.
- **E3 ligase analysis**: pan-cancer DE on detected E3 ubiquitin ligases for PROTAC-handle nomination.
- **Data portal**: TPCPA released through the R2 Genomics platform (http://r2platform.com/TPCPA).

## Results
1. DIA-MS achieves ~5,000–6,000 proteins per sample across ~4 orders of magnitude of abundance, including 7 HUPO HPP "missing proteins" (USP17L10 with 4 peptides).
2. UMAP + hierarchical clustering separate samples primarily by cancer type, with blood, liver and prostate cancers co-clustering across laboratories; HeLa QC samples form an isolated cluster (Fig. 1C–D, Fig. S1F).
3. Hallmark ssGSEA rediscovers known biology (androgen / prostate; bile acid / liver; EMT / pancreatic; MYC, E2F, G2M, DNA repair / liquid cancers; immune signaling / DLBCL) (Fig. 2A–B).
4. E3 ligase DE highlights HERC5 (esophageal) and RNF5 (liver) as tumour-type-enriched candidates for PROTAC selectivity (Fig. 2C).
5. WGCNA resolves 13 modules: module 5 colon (GFPT1/2, CTNNB1 hubs; nucleotide-sugar biology), module 6 stress (HSP90AA1/AB1, PMPCB, LRPPRC, PINK1 hubs; mitochondrial import / mitophagy), module 10 squamous (esophagus / head-and-neck / cervical; keratin biology), module 11 antigen-presentation (DLBCL), module 12 blood (DOCK2, ARHGAP25, PTPN6, IL16 hubs) (Fig. 3A–C).
6. ESTIMATE on bulk proteome ranks blood > melanoma high for immune score and prostate / glioma / ovary low; pancreatic cancer ranks highest for stromal score (Fig. 4A).
7. EPIC and CIBERSORT fail on bulk proteome for solid tumours (data not shown); Tamborero ssGSEA is preferred.
8. Pan-cancer blood vs solid DE recovers expected biology: blood cancers — lymphocyte/leukocyte activation, antigen processing/presentation, phagocytosis; solid cancers — adhesion, cytoskeleton, migration. Top blood markers BCL7A, IKZF1, SEPTIN6, DOCK2, PTPRC, PAX5, PASK; top solid markers PTPRK, SDC1, EGFR, ERBB3 (Fig. S5A–F).
9. 75-protein cancer-type classifier: AUC 0.998 on CPTAC kidney, AUC 0.992 on DIA breast, AUC 1.0 on 28 metastatic ovarian, AUC 0.98 on 32 metastatic CRC (Fig. 6D–E).
10. CRC analysis: protein-level hallmark refinement of CMS subtypes — CMS1 + MTORC1 (new); CMS2 + mitochondrial respiration + translation (new at protein level); CMS3 + peroxisome / protein-secretion (new); CMS4 + ROS / p53 / UV / hypoxia (new) (Fig. 7A).
11. CMS-enriched proteins largely validate at RNA level on external CRC cohorts (TPCPA "CRC CMS prot/mRNA" portal); 79 CMS markers diverge between protein and RNA layers.
12. Immune CC clustering of 195 CRC samples yields CC1 (CD8/Th-high, Treg-low, innate-low; CMS2/3-enriched) and CC2 (CD8/Th-low, Treg/macrophage/neutrophil/mast-high; CMS1/4-enriched). In AMC stage-2 RFS, immune CC predicts RFS more significantly than CMS, with CC1 longer RFS than CC2 (Fig. 8A–D). RNA-level analysis on independent material from the same tumours corroborates the protein-level signal (Fig. 8E).
13. CMS4 has the worst RFS and the characteristic "inflamed phenotype": high macrophages / mast / eosinophils / Tregs, low CD8 / Th (Fig. S8C; Table S8D).

## All claims (exhaustive)
- `[c01]` TPCPA quantifies 9,670 proteins from 999 primary tumors across 22 cancer types (p.1, Summary) "TPCPA includes 9,670 proteins derived from 999 primary tumors representing 22 cancer types" — confidence: high — type: quantitative — links: [[concepts/pan-cancer-proteome-atlas-tpcpa]] [[claims/tpcpa-9670-proteins-999-samples-22-cancers]]
- `[c02]` Unsupervised TPCPA clustering separates samples by cancer type independent of batch and laboratory (p.3) "these unsupervised analyses indicate that cancer type clustering reflects molecular differences between the 22 cancer types in TPCPA, rather than data acquisition batch effects" — confidence: high — type: methodological — links: [[concepts/pan-cancer-proteome-atlas-tpcpa]] [[foundations/dia-ms-data-independent-acquisition]] [[claims/tpcpa-cancer-type-clustering-batch-independent]]
- `[c03]` WGCNA on TPCPA yields 13 protein co-expression modules (p.2) "Weighted gene co-expression analysis identifies 13 modules with known and potential oncogenic drivers as hub proteins" — confidence: high — type: methodological — links: [[concepts/wgcna-protein-coexpression-cancer-hubs]] [[foundations/wgcna-weighted-gene-coexpression]] [[claims/wgcna-13-modules-pan-cancer-proteome]]
- `[c04]` GFPT1 and GFPT2 are hub proteins of colon module 5, linking N/O-glycosylation to β-catenin biology (p.4) "GFPT1/GFAT1 and GFPT2/GFAT2 (glutamine-fructose-6-phosphate transaminases) being among the five hub proteins ... the GFAT1/hexosamine biosynthetic pathway/O-GlcNAcylation axis regulates β-catenin activity to promote pancreatic cancer aggressiveness" — confidence: medium — type: mechanistic — links: [[concepts/wgcna-protein-coexpression-cancer-hubs]] [[foundations/gfpt1-gfat1-glutamine-fructose-aminotransferase]] [[foundations/ctnnb1-beta-catenin]] [[claims/gfpt1-gfpt2-hub-colon-module5-hexosamine]]
- `[c05]` HSP90AA1, HSP90AB1, PMPCB, LRPPRC and PINK1 are module 6 hub proteins connecting stress response to mitochondrial protein import and mitophagy (p.4) "Both Hsp90alpha and PMPCB are involved in mitochondrial protein import and influence levels of the mitophagy-inducing kinase PINK1, and LRPPRC ... impacts ... mitochondrial biology and mitophagy" — confidence: medium — type: mechanistic — links: [[concepts/wgcna-protein-coexpression-cancer-hubs]] [[foundations/hsp90-aip-chaperone-complex]] [[claims/hsp90-pink1-lrpprc-hub-module6-stress-mitophagy]]
- `[c06]` ESTIMATE applied to bulk proteome assigns highest immune scores to blood and melanoma and lowest to prostate, brain, ovary (p.5) "non-solid (blood) cancer types ... had the highest immune scores. Of the solid cancers, skin cancer (melanoma) had one of the highest scores, while prostate cancer, brain cancer (high-grade glioma), and ovarian cancer were found at the other extreme" — confidence: high — type: correlational — links: [[foundations/estimate-stromal-immune-score]] [[claims/estimate-immune-score-cold-hot-tumors-tpcpa]]
- `[c07]` Pancreatic cancer has the highest ESTIMATE stromal score in TPCPA (p.5) "the known stromal character of the tumor microenvironment of pancreatic cancer was reflected in the highest stromal score" — confidence: high — type: correlational — links: [[foundations/estimate-stromal-immune-score]] [[claims/pancreatic-cancer-highest-stromal-score]]
- `[c08]` EPIC and CIBERSORT perform poorly on bulk proteome; Tamborero ssGSEA preferred for CRC immune subtyping (p.7) "deconvolution approaches using EPIC and CIBERSORT did not result in meaningful results (data not shown), suggesting that they may be less suitable to quantify infiltration of immune cell populations in solid tumors using bulk protein expression data" — confidence: medium — type: methodological — links: [[foundations/tamborero-immune-signatures]] [[foundations/cibersortx-deconvolution]] [[claims/cibersort-epic-fail-bulk-proteome-tamborero-preferred]]
- `[c09]` HERC5 is highly expressed in esophageal cancer and RNF5 in liver cancer, nominating tumour-selective PROTAC E3 handles (p.3) "we identify E3-ubiquitin ligases highly expressed in specific tumor types, including HERC5 (esophageal cancer) and RNF5 (liver cancer)" — confidence: high — type: correlational — links: [[concepts/e3-ligase-protac-tumor-selectivity]] [[foundations/herc5-e3-ligase]] [[foundations/rnf5-e3-ligase]] [[claims/herc5-rnf5-tumor-enriched-e3-ligases]]
- `[c10]` Blood-vs-solid pan-cancer DE recovers expected immune and adhesion biology (p.9) "Unsurprisingly, pan-cancer features of blood cancers included immune-associated functions ... while solid cancers were characterized by terms such as cell adhesion, cytoskeletal/cell junction organization and cell migration" — confidence: high — type: correlational — links: [[claims/blood-vs-solid-pan-cancer-de-recapitulates-biology]]
- `[c11]` Top blood-cancer-enriched proteins include BCL7A, IKZF1, SEPTIN6, DOCK2, PTPRC, PAX5 and PASK (p.9) "several of the top 25 blood cancer-enriched proteins, i.e., BCL7A, IKZF1, SEPTIN6, DOCK2, PTPRC, and PAX5, are known cancer genes, while PASK is a protein kinase implicated in a link between cellular energy metabolism and differentiation competence" — confidence: high — type: correlational — links: [[claims/bcl7a-ikzf1-dock2-pax5-blood-cancer-markers]]
- `[c12]` SDC1 emerges as a top solid-cancer-unique marker and known indatuximab ravtansine target (p.9) "Top ranked proteins (unique in solid cancers) included the cancer gene PTPRK and the indatuximab ravtansine target SDC1, which is detectable on the cell surface and in plasma" — confidence: high — type: correlational — links: [[foundations/sdc1-syndecan-1]] [[claims/sdc1-top-solid-cancer-marker-adc-target]]
- `[c13]` 75-feature cancer-type classifier achieves AUC 0.998 on CPTAC renal and AUC 0.992 on independent DIA breast data (p.10) "Predictions using our model achieved an AUC of 0.998 for the CPTAC kidney cancer dataset, and an AUC of 0.992 for the breast cancer dataset" — confidence: high — type: methodological — links: [[concepts/cup-cancer-type-classifier-proteome]] [[foundations/cptac-clinical-proteomic-tumor-atlas]] [[claims/tpcpa-classifier-75-features-cptac-validation]]
- `[c14]` Classifier reaches AUC 1.0 on metastatic ovarian and AUC 0.98 on metastatic CRC cohorts (p.10) "classification of metastatic ovarian and colorectal cancers yielded an AUC of 1 and 0.98, respectively" — confidence: high — type: methodological — links: [[concepts/cup-cancer-type-classifier-proteome]] [[claims/tpcpa-classifier-metastatic-ovarian-crc-validation]]
- `[c15]` CRC CMS1 shows new proteome-level MTORC1 enrichment (p.11) "we found enrichment of the MTORC1 pathway for CMS1" — confidence: medium — type: correlational — links: [[concepts/proteomic-cms-markers-colorectal-cancer]] [[foundations/cms-classifier-crc]] [[claims/crc-cms1-mtorc1-enrichment-new]]
- `[c16]` CRC CMS3 shows new proteome-level peroxisome and protein-secretion enrichment (p.11) "peroxisome and protein secretion terms for CMS3" — confidence: medium — type: correlational — links: [[concepts/proteomic-cms-markers-colorectal-cancer]] [[foundations/cms-classifier-crc]] [[claims/crc-cms3-peroxisome-secretion-enrichment]]
- `[c17]` CRC CMS4 shows new proteome-level ROS, p53, UV-response and hypoxia hallmark enrichment (p.11) "ROS pathway, p53 pathway, UV response, and hypoxia terms for CMS4" — confidence: high — type: correlational — links: [[concepts/proteomic-cms-markers-colorectal-cancer]] [[foundations/cms-classifier-crc]] [[claims/crc-cms4-ros-p53-hypoxia-hallmarks]]
- `[c18]` CRC CMS2 shows new proteome-level mitochondrial respiration and translation enrichment not detected at RNA level (p.11) "Top 200 CMS2 proteins largely revealed biology related to mitochondrial gene expression and translation, and small molecule metabolism. Interestingly, transcriptomic studies did not find metabolism-related pathways as differential in CMS2" — confidence: medium — type: correlational — links: [[concepts/proteomic-cms-markers-colorectal-cancer]] [[foundations/cms-classifier-crc]] [[claims/crc-cms2-mitochondrial-respiration-enrichment]]
- `[c19]` CRC immune CC1 vs CC2 differ by activated CD8+ T, Th and Treg infiltration (p.12) "Immune CC1 was characterized by significantly increased infiltration with activated CD8 + T cells and T helper (Th) cells, lower infiltration with regulatory T cells, and lower levels of innate immunity subsets, such as macrophages, neutrophils, and mast cells" — confidence: high — type: correlational — links: [[concepts/immune-consensus-cluster-crc-prognostic]] [[foundations/tamborero-immune-signatures]] [[claims/crc-immune-cc1-cc2-cd8-treg-distinction]]
- `[c20]` Immune CC predicts RFS in stage-2 CRC more significantly than CMS subtype (p.12) "immune CC could predict survival more significantly than CMS subtype, with immune CC1 (CMS2/3-enriched) showing longer RFS than immune CC2 (CMS1/4-enriched)" — confidence: high — type: correlational — links: [[concepts/immune-consensus-cluster-crc-prognostic]] [[claims/immune-cc-predicts-rfs-better-than-cms-crc]]
- `[c21]` CMS4 has worst RFS and low CD8/Th with high Treg/macrophages/eosinophils (p.13) "CMS4, which had the worst RFS ... was significantly depleted in Th cells and also had the lowest level of CD8 + T cells ... CMS4 was significantly enriched in eosinophils, macrophages, mast cells, and regulatory T cells" — confidence: high — type: correlational — links: [[concepts/proteomic-cms-markers-colorectal-cancer]] [[claims/crc-cms4-worst-rfs-low-cd8-high-treg]]
- `[c22]` Most CMS-enriched proteins validate at RNA level on external CRC cohorts (p.11) "most top 200 CMS subtype-enriched proteins validate well at the RNA level in external datasets" — confidence: high — type: methodological — links: [[concepts/proteomic-cms-markers-colorectal-cancer]] [[claims/cms-protein-markers-validate-rna-external]]
- `[c23]` Single-shot DIA-MS quantifies 5,000–6,000 proteins per sample with ~4 orders of magnitude dynamic range (p.3) "Most samples yielded 5,000–6,000 identified proteins, with abundance spanning ∼4 orders of magnitude" — confidence: high — type: quantitative — links: [[foundations/dia-ms-data-independent-acquisition]] [[claims/tpcpa-5000-6000-proteins-per-sample]]

## Discussion captured

### Authors' interpretation
The authors interpret TPCPA as a comprehensive proteome-level complement to TCGA-style genomic atlases, demonstrating that bulk DIA-MS on primary tumours yields cancer-type-dominant signal across cohorts. They emphasise three deliverables: (i) module-driven hub-protein nomination as drug targets beyond known cancer-gene lists, (ii) CRC immune consensus clusters as a prognostic axis orthogonal to and stronger than CMS, and (iii) a deployable cancer-type classifier with strong AUC on metastatic samples as a CUP solution.

### Comparisons with prior literature (made by authors)
- Cancer-type-specific TMT proteomics studies (refs 9–11) — TPCPA covers more cancer types under one workflow.
- CPTAC kidney (ref 78) and an independent DIA breast cancer dataset (ref 79) — used as external classifier validation.
- Tamborero immune signatures (Tamborero et al.) — adopted as the preferred immune-subset method on bulk proteome.
- ESTIMATE (Yoshihara et al., ref 68) — applied to bulk proteome successfully.
- Guinney CMS classifier — leveraged for CRC subtype assignment from matched RNA; immune CC refines its prognostic capacity.
- HSP90 inhibition literature (refs 49–50) and GFAT1/HBP / β-catenin / pancreatic cancer (refs 44–46) — cited as functional context for module hub nominations.
- "Inflamed phenotype" CMS4 immune biology (refs 86–88) — proteome data corroborates.

### Mechanistic hypotheses proposed
- "These [E3 ubiquitin] ligases highly expressed in specific tumor types ... may provide [PROTAC] selectivity" (Summary + p.3).
- WGCNA module hubs (GFPT1, HSP90, PINK1, DOCK2, PTPN6, LRPPRC) act as connectors between metabolism, stress / mitochondrial homeostasis, and oncogenic signalling and constitute new drug-target candidates (p.4).
- "Immune subset analysis using protein signatures will be a more robust approach for confident subtype determination" than IHC of individual markers (p.14).
- CMS4 worst-RFS phenotype is driven by an innate-immune-rich, Treg-high, CD8/Th-low TME (p.13).

### Caveats and self-criticism
- "Since we used all samples, including test samples, for feature selection, there may have been some overfitting in test set classification" (p.10).
- The TPCPA dataset encompasses diverse tissues, processing methods and laboratories — batch effects may arise even though HeLa QC clustering supports cross-lab comparability (p.14).
- The 32 metastatic CRC validation cohort is unpublished Jimenez-lab data — partial cohort independence only.
- Tamborero gene-set coverage on proteome varies (33–81% per subset).
- Immune CC validation rests on AMC stage-2 RFS plus EMC stage-1/2 — no truly external validation cohort.

### Future directions suggested
- Extend TPCPA to post-translational modifications, metabolites and spatial proteomics via laser-capture microdissection (p.14).
- Robust real-time clinical proteome measurements of tumour resections and biopsies.
- Independent validation of immune CC prognostic value via IHC or independent MS cohorts (p.14).
- Functional validation of module hub proteins (GFPT1, HSP90, PINK1, LRPPRC, DOCK2, PTPN6) as drug targets.

## Limitations
- 999 samples with imbalanced per-cancer cohort sizes (smallest 8 skin/melanoma; largest 195 CRC).
- Bulk tissue only — no cell-type resolution; tissue-of-origin contribution to clustering is substantial.
- Per-sample depth of 5,000–6,000 proteins is below fractionated TMT workflows.
- FF + FFPE mixed inputs may interact with cohort effects in specific cancer types.
- EPIC and CIBERSORT failure reported only as "data not shown" — not directly benchmarked.
- 75-feature classifier feature selection used the test split; classifier external evaluation includes only two non-TPCPA primary cohorts and two small metastatic cohorts.
- Immune CC RFS analysis lacks multivariable adjustment for stage / MSI / KRAS / BRAF.

## Open questions

### Open questions raised by authors
- Will inclusion of PTMs, metabolites and spatial layers extend mechanistic understanding of pan-cancer biology?
- Does immune CC robustly predict CRC patient survival beyond AMC / EMC?
- Are module hub proteins functionally tractable as cross-cancer drug targets?

### Open questions identified during ingest
- Can a HERC5- or RNF5-recruiting PROTAC achieve tumour-selective degradation of a canonical oncoprotein in esophageal or liver cancer models?
- Does GFPT1 inhibition phenocopy β-catenin inhibition in colon cancer organoids?
- How robust is the 75-feature classifier to non-DIA (TMT or DDA) input?
- Which of the 79 RNA-discordant CMS proteins are post-transcriptionally regulated vs derived from infiltrating cell populations?
- Does CMS4 hypoxia signature predict response to hypoxia-activated prodrugs (evofosfamide, tarloxotinib)?
- Does immune CC retain prognostic power after multivariable adjustment for stage / MSI / KRAS / BRAF?

## My take
TPCPA is the first pan-cancer DIA-MS atlas at this scale and quality, and its design choices (single-shot, no TMT, R2 data portal) are correct for a community-reference dataset. The standout findings are (i) the immune CC axis that out-predicts CMS for RFS in stage-2 CRC — a candidate clinical biomarker if multivariably and externally validated; (ii) the WGCNA hub-protein nominations (GFPT1, HSP90 module, DOCK2/PTPN6) as cross-cancer drug-target shortlist; and (iii) the CUP classifier, which is the most translatable output. The PROTAC E3 ligase framing is speculative — expression enrichment is necessary but far from sufficient — yet it correctly orients pan-cancer atlases toward PROTAC chemistry. For thesis context, the CMS4 hypoxia hallmark enrichment and the per-cancer ESTIMATE stromal/immune profile are useful priors when reasoning about hypoxia-relevant cohorts.

## Related
- [[foundations/dia-ms-data-independent-acquisition]] — acquisition method
- [[foundations/wgcna-weighted-gene-coexpression]] — co-expression module discovery
- [[foundations/estimate-stromal-immune-score]] — stromal/immune scoring
- [[foundations/ssgsea-single-sample-gsea]] — sample-level enrichment
- [[foundations/tamborero-immune-signatures]] — immune-subset signatures
- [[foundations/cms-classifier-crc]] — CRC subtype taxonomy
- [[foundations/cptac-clinical-proteomic-tumor-atlas]] — external proteome reference
- [[foundations/tcga-the-cancer-genome-atlas]] — external RNA reference
- [[foundations/cibersortx-deconvolution]] — deconvolution baseline
- [[foundations/hsp90-aip-chaperone-complex]] — module 6 chaperone hubs
- [[foundations/gfpt1-gfat1-glutamine-fructose-aminotransferase]] — module 5 metabolic hub
- [[foundations/ctnnb1-beta-catenin]] — Wnt effector connected to GFPT1/HBP
- [[foundations/sdc1-syndecan-1]] — translatable ADC target
- [[foundations/herc5-e3-ligase]] — tumour-selective PROTAC E3
- [[foundations/rnf5-e3-ligase]] — tumour-selective PROTAC E3
- [[concepts/pan-cancer-proteome-atlas-tpcpa]]
- [[concepts/dia-ms-pan-cancer-proteomics-approach]]
- [[concepts/wgcna-protein-coexpression-cancer-hubs]]
- [[concepts/proteomic-cms-markers-colorectal-cancer]]
- [[concepts/immune-consensus-cluster-crc-prognostic]]
- [[concepts/cup-cancer-type-classifier-proteome]]
- [[concepts/e3-ligase-protac-tumor-selectivity]]
- [[people/jaco-c-knol]]
- [[people/tiannan-guo]]
- [[people/connie-r-jimenez]]
