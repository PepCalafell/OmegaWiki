---
# === Identification ===
title: "Macrophages use apoptotic cell-derived methionine and DNMT3A during efferocytosis to promote tissue resolution"
slug: macrophages-use-apoptotic-cell-derived-methionine
arxiv: ""
doi: "10.1038/s42255-022-00551-7"
pmid: ""
venue: "Nature Metabolism"
year: 2022
authors:
  - "Patrick B. Ampomah"
  - "Bishuang Cai"
  - "Santosh R. Sukka"
  - "Brennan D. Gerlach"
  - "Arif Yurdagul Jr"
  - "Xiaobo Wang"
  - "George Kuriakose"
  - "Lancia N. F. Darville"
  - "Yan Sun"
  - "Simone Sidoli"
  - "John M. Koomen"
  - "Alan R. Tall"
  - "Ira Tabas"
first_author: "Patrick B. Ampomah"
corresponding_author: "Patrick B. Ampomah; Ira Tabas"

# === Source & metadata ===
source_type: pdf
s2_id: ""
date_added: 2026-05-26
ingested_date: 2026-05-26
ingest_version: 1
last_reviewed: null

# === Classification ===
importance: 4
tier: TIER_1
tags:
  - efferocytosis
  - macrophage
  - DNMT3A
  - methionine
  - SAM
  - DNA-methylation
  - DUSP4
  - COX2
  - PGE2
  - TGFβ1
  - ERK
  - CD36
  - CREB1
  - resolution
  - atherosclerosis
  - bone-marrow-transplant
  - isotope-tracing
  - MeDIP
keywords:
  - apoptotic cell methionine
  - DNMT3A efferocytosis
  - DUSP4 repression by methylation
  - PGE2 TGFβ1 resolution axis
  - phagolysosomal degradation Ptgs2 induction
  - 13C-methionine tracing macrophage SAM
  - haematopoietic DNMT3A KO atherosclerosis
  - fibrous cap thinning DNMT3A
  - CHIP DNMT3A coronary artery disease mechanism
  - CD36-ERK-DUSP4 negative feedback
domain: "immunology / epigenetics / cardiovascular"

# === Biomedical domain ===
tissue:
  - bone_marrow
  - blood
  - thymus
  - peritoneum
  - aorta_atherosclerotic_lesion
  - in_vitro_only
condition:
  - healthy
  - atherosclerosis
  - sterile_inflammation
disease_specific:
  - atherosclerosis_advanced
  - thymocyte_apoptosis_DEX
  - zymosan_peritonitis
species:
  - mouse
  - human
hypoxia_relevant: false
contains_immune_cells: true
contains_myeloid: true

# === Technique ===
techniques:
  - qRT-PCR
  - siRNA_knockdown
  - immunoblot_Western
  - flow_cytometry
  - immunofluorescence
  - ELISA
  - LC-MS_MS
  - isotope_tracing_13C_15N_methionine
  - MeDIP-qPCR
  - bone_marrow_transplantation
  - conditional_KO_VavCre
  - atherosclerosis_western_diet_Ldlr
  - dexamethasone_thymus_apoptosis_model
  - zymosan_A_peritonitis_model
n_samples: null
n_cells_total: null
integration_method: ""

# === Biology captured ===
key_cell_types:
  - bone_marrow_derived_macrophage_BMDM
  - human_monocyte_derived_macrophage_HMDM
  - thymic_macrophage
  - peritoneal_exudate_macrophage
  - plaque_macrophage
  - apoptotic_Jurkat_T_cell
key_markers:
  - DNMT3A
  - PTGS2_COX2
  - TGFB1
  - MAT2A
  - DUSP4
  - DUSP1
  - MAPK1_3_ERK
  - CD36
  - MERTK
  - PTGER2_EP2
  - PTGER4_EP4
  - PTGES
  - CREB1
  - p-CREB1
  - Rubicon
  - F4/80
  - Mac2
  - Gr1
  - Ly6G
  - TGFβRI
key_pathways:
  - CD36-ERK-DUSP4-Ptgs2-PGE2-TGFβ1_axis
  - methionine_cycle_MAT2A_SAM
  - DNMT3A_de_novo_DNA_methylation
  - phagolysosomal_AC_degradation_LAP
  - PGE2_EP2_EP4_cAMP_PKA_CREB
  - ERK_MAPK_signalling
  - TGFβ_TGFβRI_SMAD_efferocytosis

# === User project membership ===
projects: []
priority: reference
read_status: deep_read

# === HypoxiaVERSE-specific ===
hypoxiaverse_status: excluded
exclusion_reason: "Mechanistic paper not directly hypoxia-related; mechanism of efferocytosis-driven resolution useful as macrophage-biology context."
data_availability: "Source data deposited with Nat Metab article; isotope-tracing methods detailed in Methods section."

# === Cross-references ===
code_url: ""
cited_by: []
---

## Problem

Efferocytosis — macrophage clearance of apoptotic cells — drives tissue resolution by triggering secretion of pro-resolving lipid mediators (PGE2) and cytokines (TGF-β1). Defective efferocytosis underlies chronic inflammatory diseases including atherosclerosis, autoimmunity, neurodegeneration, and chronic lung disease. The mechanisms linking efferocytosis to TGF-β1 / PGE2 induction remain incompletely defined — particularly the open question of how apoptotic-cell cargo, beyond simple metabolic recycling, signals to drive the macrophage resolution program. Tabas-lab prior work established that AC-derived arginine fuels putrescine-driven engulfment, fatty acids drive IL-10, and cholesterol activates LXR resolution. Whether the AC-derived methyl pool (methionine → SAM) can drive an epigenetic resolution mechanism was unknown.

## Key idea

AC-derived methionine, after phagolysosomal degradation of engulfed apoptotic cells, is converted to S-adenosylmethionine (SAM) by macrophage MAT2A. SAM is consumed by DNMT3A to methylate the CpG-rich Dusp4 promoter, repressing Dusp4 (an ERK1/2 phosphatase). With DUSP4 repressed, the early CD36-driven ERK1/2 activation (otherwise quenched by ERK-DUSP4 negative feedback) is sustained, driving Ptgs2/COX2 induction → PGE2 synthesis → EP2/EP4-mediated p-CREB1 activation → TGF-β1 transcription. TGF-β1 in turn drives autocrine/paracrine efferocytosis amplification and tissue resolution. The pathway is required in vivo in three independent resolution models — DEX-induced thymocyte apoptosis, Zymosan A-induced peritonitis, and advanced atherosclerosis — and is proposed as a candidate mechanism linking DNMT3A clonal-haematopoiesis (CHIP) mutations to elevated coronary artery disease risk.

## Method

In vitro systems: mouse bone marrow-derived macrophages (BMDMs) cultured in L929-CM-supplemented DMEM; human monocyte-derived macrophages (HMDMs) from buffy coats. Apoptotic cells: UV/staurosporine-induced apoptotic human Jurkat T cells (and apoptotic macrophages in cross-validation experiments) labelled with PKH26 dye and/or 13C5,15N-methionine prior to apoptosis induction. Co-culture: 45-min AC incubation + rinsing + 1-6 h chase. Perturbations: siRNA against Rbcn, Ptgs2, Ptges, Ptger2/4, Mat2a, Dnmt3a, Mapk1, Mapk3, Dusp4, Dusp1, Cd36, Creb1, Tgfb1; pharmacological — NS-398 (COX2), PF-9366 (MAT2A), U0126 (MEK), bafilomycin A1 (V-ATPase), LY3200882 (TGFβRI), exogenous SAM and PGE2. Readouts: qRT-PCR (Ptgs2, Tgfb1, Dusp1/4, etc.); immunoblot (DNMT3A, COX2, p-CREB, CREB, β-actin); ELISA (TGF-β1, PGE2); flow cytometry (p-ERK1/2, COX2, LAP-TGFβ1, PKH26 sorting); LC-MS/MS (13C5,15N-SAM, 13C5-mC in macrophage DNA); MeDIP-qPCR at Dusp4 CpG-rich promoter region. In vivo: BMT chimeras — donor Vav1Cre+/− (control) or Dnmt3afl/fl Vav1Cre+/− (H-DNMT3A-KO) BM transplanted into C57BL/6J recipients for DEX-thymus and Zymosan models; into Ldlr-/- recipients for atherosclerosis (12 weeks western-type diet). Mertkfl/fl Lyz2cre and CD36-perturbed cells were used for receptor dissection. Statistics: one-way ANOVA + Fisher's LSD or Student's t-test; biological replicates n=3-8.

## Results

### 1. Phagolysosomal AC degradation is required for Ptgs2/Tgfb1 induction (Fig. 1)
- siRbcn (Rubicon, LAP machinery) or bafilomycin A1 (V-ATPase) blocks AC-induced Ptgs2 and Tgfb1 in BMDMs and HMDMs without affecting AC engulfment.
- siPtgs2 or NS-398 (COX2 inhibitor) blocks AC-induced Tgfb1.
- siPtges (PGE synthase) blocks AC-induced Tgfb1.
- siPtger2 + siPtger4 (EP2 and EP4) blocks both AC- and exogenous PGE2-induced Tgfb1.
- siTgfb1 does not affect AC-induced Ptgs2 — directionality COX2 → PGE2 → TGFβ1.

### 2. AC-derived methionine flows to SAM via MAT2A (Fig. 2)
- PF-9366 or siMat2a blocks AC-induced Ptgs2/Tgfb1/TGF-β1 secretion in BMDM and HMDM.
- Exogenous SAM is sufficient to induce Ptgs2/Tgfb1 and bypasses MAT2A inhibition.
- AC-induced Ptgs2/Tgfb1 is preserved in methionine-free media — AC-derived methionine is sufficient.
- 13C5,15N-methionine-labelled Jurkat ACs → 13C5,15N-SAM is detected by LC-MS/MS only in PKH26+ (AC+) macrophages; bafilomycin abolishes the signal.

### 3. DNMT3A is required for the efferocytosis-Ptgs2/Tgfb1-PGE2-TGF-β1 axis (Fig. 3)
- H-DNMT3A-KO BMDMs and siDNMT3A HMDMs fail to induce Ptgs2/COX2 and Tgfb1; AC uptake unaffected; SAM rescue fails in DNMT3A-null cells.
- AC-induced Ptgs2/COX2 with apoptotic-macrophage source (vs Jurkat) reproduces the DNMT3A requirement.
- Global %5mC in macrophage DNA increases upon AC exposure; partially blocked by MAT2A inhibition and partially by DNMT3A absence.
- 13C5-methylcytosine in macrophage DNA, after 13C-methionine-labelled AC exposure, is detected by LC-MS/MS; combined bafilomycin + PF-9366 markedly blocks the signal.
- PGE2 rescue of Tgfb1 fails in DNMT3A-KO; PGE2-induced p-CREB1 abolished in DNMT3A-KO; siCreb1 blocks both AC- and PGE2-induced Tgfb1.

### 4. CD36-ERK1/2 activation requires DUSP4 repression to sustain Ptgs2/TGFβ1 (Fig. 4)
- U0126 or siMapk1+siMapk3 blocks AC-induced Ptgs2/Tgfb1.
- siCd36 robustly reduces AC-induced p-ERK1/2, COX2, and LAP-TGF-β1 MFI by flow cytometry; MerTK-KO macrophages show only modest decreases — CD36 dominates ERK activation.
- DNMT3A-KO macrophages have a smaller initial p-ERK1/2 increase that diverges further from control over a 2-h chase.
- In siDnmt3a or H-DNMT3A-KO AC-stimulated macrophages, Dusp4 (not Dusp1) is elevated; U0126 also blocks AC-induced Dusp4 (confirming ERK-DUSP4 negative feedback).
- siDusp4 (not siDusp1) rescues Ptgs2/COX2/Tgfb1 in DNMT3A- or MAT2A-deficient macrophages; siDusp4 cannot rescue siMapk1/3 macrophages — DUSP4 acts on ERK.
- MeDIP-qPCR at the Dusp4 CpG-rich promoter: AC-induced 5mC enrichment in WT, absent in DNMT3A-KO.

### 5. The pathway operates in vivo in three resolution models (Fig. 5)
- DEX-thymus model: H-DNMT3A-KO BMT mice have reduced thymic-macrophage p-ERK / COX2 / PGE2 / TGF-β1 and elevated DUSP4 at 18 h post DEX.
- Zymosan A peritonitis: H-DNMT3A-KO mice show reduced exudate-macrophage p-ERK / COX2 / LAP-TGFβ1 and reduced secreted PGE2 / TGFβ1 at 24 h.
- Ldlr-/- atherosclerosis (12 wk WTD): H-DNMT3A-KO BMT mice have reduced lesional-macrophage p-ERK / COX2 / TGF-β1; lesion size and systemic lipids unchanged.

### 6. The pathway is functionally required for efferocytosis and resolution (Fig. 6)
- BMDM CM from control AC-exposed (not DNMT3A-KO) increases recipient-BMDM efferocytosis; blocked by anti-TGFβ1 antibody.
- DEX-thymus: H-DNMT3A-KO increases AC accumulation, cellularity, necrosis; reduces macrophage-associated/free TUNEL+ ratio (impaired efferocytosis).
- Zymosan: H-DNMT3A-KO impairs PMN clearance at 24-48 h; i.p. TGF-β1 (200 ng × 2) rescues PMN counts and macrophage-Gr1 efferocytosis index to control levels — direct TGF-β1 epistasis.
- Atherosclerosis: H-DNMT3A-KO reduces fibrous cap thickness (absolute and as ratio to lesion area) and lesional efferocytosis; lesion size unchanged.

## All claims (exhaustive)

- `[c01]` Phagolysosomal AC degradation (not engulfment alone) is required for AC-induced Ptgs2 and Tgfb1 induction in BMDMs and HMDMs (Fig. 1a-f) "Rubicon silencing suppressed AC-induced increases in both Ptgs2 and Tgfb1... similar results with bafilomycin A1... neither siRbcn nor bafilomycin treatment blocked initial AC engulfment" — confidence: high — type: methodological — links: [[concepts/dnmt3a-dusp4-efferocytosis-resolution-pathway]] [[concepts/efferocytosis-anti-inflammatory-clearance]] [[foundations/bafilomycin-a1-vacuolar-atpase]] [[claims/efferocytosis-phagolysosomal-degradation-required-ptgs2-tgfb1]]
- `[c02]` COX2-derived PGE2 is the obligate intermediate between AC exposure and Tgfb1 induction in macrophages (Fig. 1g-i, ED Fig. 1g-i,l-m) "the AC-induced increase in Tgfb1 mRNA was prevented by Ptgs2 silencing... by the COX2-specific inhibitor NS-398... silencing Ptges blocked AC-induced Tgfb1... silencing Tgfb1 did not affect AC-induced Ptsg2" — confidence: high — type: pharmacological — links: [[foundations/ptgs2-cox2]] [[foundations/pge2-prostaglandin-e2]] [[foundations/tgfb1-cytokine]] [[claims/cox2-pge2-intermediate-tgfb1-efferocytosis]]
- `[c03]` PGE2 receptors EP2 and EP4 mediate the AC- and PGE2-induced Tgfb1 induction in BMDMs (Fig. 1j-k) "silencing two PGE2 receptors, EP2 and EP4, decreased AC-induced Tgfb1, and exogenous PGE2 increased Tgfb1, which was also blocked by silencing EP2/4" — confidence: high — type: pharmacological — links: [[foundations/pge2-prostaglandin-e2]] [[claims/ep2-ep4-receptors-mediate-pge2-tgfb1]]
- `[c04]` MAT2A-catalysed conversion of methionine to SAM is required for AC-induced Ptgs2/Tgfb1; exogenous SAM bypasses MAT2A inhibition (Fig. 2a-f) "MAT2A inhibitor PF-9366 or siMat2a blocked AC-induced increases in Ptgs2 and Tgfb1 mRNA and TGF-β1 secretion... exogenously added SAM was sufficient to induce Ptgs2 and Tgfb1, and... not substantially reduced by PF-9366" — confidence: high — type: pharmacological — links: [[foundations/mat2a-methionine-adenosyltransferase]] [[foundations/s-adenosylmethionine-sam]] [[foundations/pf-9366-mat2a-inhibitor]] [[claims/ac-methionine-mat2a-sam-required-ptgs2-tgfb1]]
- `[c05]` AC-derived methionine is metabolically traced into macrophage SAM by LC-MS/MS using 13C5,15N-methionine-labelled ACs; bafilomycin blocks this transfer (Fig. 2i, ED Fig. 2f-h) "13C5,15N-SAM was found only in AC+ macrophages and, importantly, this was markedly inhibited when phagolysosomal hydrolysis was blocked by bafilomycin" — confidence: high — type: quantitative — links: [[concepts/ac-derived-methionine-sam-macrophage-epigenetics]] [[foundations/s-adenosylmethionine-sam]] [[claims/13c-methionine-from-acs-traced-to-sam-in-macrophages]]
- `[c06]` DNMT3A is required for AC-induced Ptgs2/COX2 and Tgfb1 in BMDMs and HMDMs; SAM rescue also fails in DNMT3A-null macrophages (Fig. 3a-i) "AC-induced increases in Ptgs2, COX2 and Tgfb1 were blocked in BMDMs from Dnmt3afl/fl Vav1Cre+/– mice... DNMT3A silencing blocked AC-induced PTGS2 and TGFβ1 in HMDMs... increases induced by exogenous SAM were also prevented in macrophages lacking DNMT3A" — confidence: high — type: mechanistic — links: [[foundations/dnmt3a-de-novo-dna-methyltransferase]] [[concepts/dnmt3a-dusp4-efferocytosis-resolution-pathway]] [[claims/dnmt3a-required-efferocytosis-ptgs2-tgfb1]]
- `[c07]` Methyl groups from AC-derived methionine are incorporated as 13C-methylcytosine in macrophage genomic DNA, blocked by bafilomycin + MAT2A inhibition (Fig. 3k, ED Fig. 2r) "13CH3-DNA, assayed by LC−MS/MS, was detected in macrophages incubated with 13C5,15N-methionine-labelled ACs versus unlabelled ACs, and this was partially blocked by bafilomycin and markedly blocked by bafilomycin plus the MAT2A inhibitor" — confidence: high — type: quantitative — links: [[concepts/ac-derived-methionine-sam-macrophage-epigenetics]] [[foundations/s-adenosylmethionine-sam]] [[claims/ac-methionine-methyl-groups-traced-to-macrophage-dna]]
- `[c08]` PGE2 → Tgfb1 induction also requires DNMT3A via p-CREB1; siCreb1 phenocopies the block (Fig. 3l-o, ED Fig. 2s) "addition of exogenous PGE2 did not rescue the defect in Tgfb1 mRNA in DNMT3A-KO macrophages... PGE2-induced p-CREB1 was blocked in DNMT3A-KO macrophages... silencing CREB1 blocked the increase in Tgfb1 in macrophages treated with exogenous PGE2 or incubated with ACs" — confidence: medium — type: mechanistic — links: [[foundations/creb1-transcription-factor]] [[foundations/pge2-prostaglandin-e2]] [[claims/pge2-tgfb1-induction-dnmt3a-creb1-dependent]]
- `[c09]` Sustained ERK1/2 activation is required for AC-induced Ptgs2/Tgfb1 in BMDMs and HMDMs (Fig. 4a-d) "inhibition of ERK1/2 by U0126, or silencing of Makp1 and Mapk3, prevented AC-induced increases in Ptgs2 and Tgfb1 and decreased TGF-β1 secretion" — confidence: high — type: pharmacological — links: [[foundations/mapk1-3-erk1-2-kinases]] [[foundations/u0126-mek-erk-inhibitor]] [[claims/erk-activation-required-efferocytosis-cox2-tgfb1]]
- `[c10]` CD36 is the principal AC receptor driving ERK1/2/COX2/TGFβ1 in macrophages; MerTK contributes modestly (Fig. 4e-g, ED Fig. 3e-g) "AC+ MerTK-KO macrophages showed a modest decrease in p-ERK and COX2 MFI, while siCD36-treated versus scrambled RNA-treated AC+ macrophages showed a more robust reduction in p-ERK, COX2 and TGF-β1 MFI" — confidence: high — type: mechanistic — links: [[foundations/cd36-scavenger-receptor]] [[foundations/mertk-tam-receptors]] [[claims/cd36-principal-ac-receptor-driving-erk-cox2-tgfb1]]
- `[c11]` DNMT3A-KO macrophages show smaller initial AC-induced p-ERK1/2 increase that persists for >2 h chase, consistent with failure to repress DUSP4 (Fig. 4h) "DNMT3A-KO macrophages showed a smaller increase in p-ERK1/2 at 45 min, and the difference between KO and control macrophages persisted for the following 2-h chase period" — confidence: high — type: methodological — links: [[foundations/dnmt3a-de-novo-dna-methyltransferase]] [[foundations/mapk1-3-erk1-2-kinases]] [[claims/dusp4-not-dusp1-mediates-erk-negative-feedback-efferocytosis]]
- `[c12]` Dusp4 (not Dusp1) is upregulated in DNMT3A-deficient AC-stimulated macrophages, consistent with DNMT3A-mediated repression of Dusp4 (Fig. 4i-j, ED Fig. 3h) "in siDnmt3a-treated macrophages... there was an increase in Dusp4 but not Dusp1 mRNA... AC-induced Dusp4 was blocked by the ERK inhibitor U0126" — confidence: high — type: methodological — links: [[foundations/dusp4-dual-specificity-phosphatase-4]] [[claims/dusp4-upregulated-in-dnmt3a-deficient-ac-stimulated-macrophages]]
- `[c13]` siDusp4 (not siDusp1) rescues Ptgs2/COX2/Tgfb1 in DNMT3A- or MAT2A-deficient macrophages; cannot rescue siMapk1/3 (Fig. 4k-l, ED Fig. 3i-q) "suppression of Ptgs2, COX2 and Tgfb1 by siDnmt3a or DNMT3A-KO in efferocytosing macrophages was abrogated when Dusp4 was also silenced, but not when Dusp1 was silenced... Dusp4 silencing could not rescue the defect in Tgfb1 expression in siMapk1/3-treated macrophages" — confidence: high — type: mechanistic — links: [[foundations/dusp4-dual-specificity-phosphatase-4]] [[concepts/dnmt3a-dusp4-efferocytosis-resolution-pathway]] [[claims/dusp4-not-dusp1-mediates-erk-negative-feedback-efferocytosis]]
- `[c14]` The CpG-rich Dusp4 promoter is methylated by DNMT3A in AC-stimulated WT (not DNMT3A-KO) macrophages by MeDIP-qPCR (Fig. 4m) "using methylated DNA immunoprecipitation, we found that the CpG-rich promoter region of the Dusp4 gene was methylated in response to ACs in wild-type, but not DNMT3A-deficient macrophages" — confidence: high — type: methodological — links: [[foundations/medip-methylated-dna-immunoprecipitation]] [[foundations/dusp4-dual-specificity-phosphatase-4]] [[claims/dusp4-promoter-methylated-ac-stimulated-wt-not-dnmt3a-ko]]
- `[c15]` AC-induced macrophage global %5mC increases; partially MAT2A- and DNMT3A-dependent (Fig. 3j) "ACs increased the percentage of 5-methylcytosine (mC) in macrophage DNA, which was partially dampened by MAT2A inhibition or DNMT3A absence" — confidence: medium — type: quantitative — links: [[foundations/dnmt3a-de-novo-dna-methyltransferase]] [[claims/global-5mc-increase-efferocytosis-mat2a-dnmt3a-dependent]]
- `[c16]` H-DNMT3A-KO mice (DEX-thymus model) show reduced thymic-macrophage p-ERK/COX2/PGE2/TGFβ1 and elevated DUSP4 (Fig. 5a-d) "DEX increased thymic macrophage p-ERK, COX2, PGE2 and TGF-β1 in the control mice, whereas these responses were suppressed in the H-DNMT3A-KO mice... thymi of H-DNMT3A-KO mice had higher DUSP4 expression" — confidence: high — type: methodological — links: [[concepts/dnmt3a-dusp4-efferocytosis-resolution-pathway]] [[claims/h-dnmt3a-ko-reduces-thymic-cox2-pge2-tgfb1-dusp4-up]]
- `[c17]` H-DNMT3A-KO impairs continual thymic efferocytosis and resolution: increased AC accumulation, cellularity, necrosis; reduced macrophage-TUNEL+ ratio (Fig. 6b-e) "thymi of the H-DNMT3A-KO cohort showed a greater increase in ACs and cellularity and a smaller decrease in thymus weight after DEX... ratio of macrophage-associated to free TUNEL+ thymocytes was lower" — confidence: high — type: methodological — links: [[concepts/efferocytosis-anti-inflammatory-clearance]] [[claims/h-dnmt3a-ko-impairs-thymic-efferocytosis-and-resolution]]
- `[c18]` H-DNMT3A-KO impairs Zymosan A peritonitis resolution at 24-48 h with reduced exudate-macrophage p-ERK/COX2/LAP-TGFβ1 and reduced PGE2/TGFβ1 (Fig. 5e-g, Fig. 6f, ED Fig. 4c-d) "after 24 h, but not 12 h, exudate macrophages from the H-DNMT3A-KO mice had decreases in phospho-ERK, COX2 and LAP-TGF-β1 and also in secreted PGE2 and TGF-β1" — confidence: high — type: methodological — links: [[concepts/dnmt3a-dusp4-efferocytosis-resolution-pathway]] [[claims/h-dnmt3a-ko-impairs-zymosan-peritonitis-resolution]]
- `[c19]` i.p. TGF-β1 rescues PMN resolution and macrophage-Gr1 efferocytosis index in H-DNMT3A-KO Zymosan mice (Fig. 6g-h) "treatment of H-DNMT3A-KO mice with TGF-β1 15 and 20 h after Zymosan lowered the number of PMNs to the level seen in the control cohort... TGF-β1 treatment in H-DNMT3A cohort increased the percentage of efferocytosing macrophages" — confidence: high — type: pharmacological — links: [[foundations/tgfb1-cytokine]] [[claims/exogenous-tgfb1-rescues-dnmt3a-ko-zymosan-resolution]]
- `[c20]` H-DNMT3A-KO in 12-wk WTD Ldlr-/- atherosclerosis reduces lesional-macrophage p-ERK/COX2/TGFβ1 without changing lesion size or systemic lipids (Fig. 5h-j, ED Fig. 4e-m) "lesional macrophages of H-DNMT3A-KO mice had decreases in p-ERK, COX2 and TGF-β1... lesion size was not affected by H-DNMT3A-KO" — confidence: high — type: methodological — links: [[concepts/dnmt3a-dusp4-efferocytosis-resolution-pathway]] [[claims/h-dnmt3a-ko-reduces-lesional-macrophage-p-erk-cox2-tgfb1-atherosclerosis]]
- `[c21]` H-DNMT3A-KO atherosclerosis causes fibrous cap thinning and impaired lesional efferocytosis — features of plaque instability (Fig. 6i-k) "H-DNMT3A-KO resulted in marked decreases in cap thickness when compared with lesions from control mice... lesional efferocytosis was impaired in the lesions of H-DNMT3A-KO versus control mice" — confidence: high — type: methodological — links: [[concepts/dnmt3a-dusp4-efferocytosis-resolution-pathway]] [[claims/h-dnmt3a-ko-fibrous-cap-thinning-impaired-lesional-efferocytosis]]
- `[c22]` Conditioned media from AC-exposed control (not DNMT3A-KO) macrophages enhances recipient-macrophage efferocytosis in an anti-TGFβ1-blockable manner (Fig. 6a) "incubation of macrophages with conditioned media from AC-exposed control macrophages, but not AC-exposed DNMT3A-KO macrophages, increased efferocytosis, and the increase seen with control-macrophage CM was blocked by an anti-TGF-β1 antibody" — confidence: high — type: methodological — links: [[foundations/tgfb1-cytokine]] [[claims/conditioned-media-from-control-not-dnmt3a-ko-macs-enhances-efferocytosis-via-tgfb1]]
- `[c23]` Exogenous TGF-β1 enhances macrophage efferocytosis; blocked by TGFβRI inhibitor LY3200882 (ED Fig. 5a) "incubation of macrophages with TGF-β1 in vitro enhances efferocytosis, which was blocked by inhibiting transforming growth factor beta receptor I-mediated SMAD phosphorylation with LY3200882" — confidence: medium — type: pharmacological — links: [[foundations/tgfb1-cytokine]] [[claims/exogenous-tgfb1-enhances-efferocytosis-via-tgfbri-smad]]
- `[c24]` AC-induced Ptgs2/Tgfb1 in BMDMs occurs in methionine-free media — AC-derived methionine is sufficient (Fig. 2g-h) "AC-induced increases in Ptgs2 and Tgfb1 were not dependent on methionine in the media" — confidence: high — type: methodological — links: [[concepts/ac-derived-methionine-sam-macrophage-epigenetics]] [[claims/ac-induced-ptgs2-tgfb1-independent-of-extracellular-methionine]]

## Discussion captured

### Authors' interpretation

The authors interpret efferocytosis as a two-step macrophage-resolution program: an early surface-receptor signal (CD36 → ERK), and a delayed metabolic-epigenetic signal (AC-methionine → SAM → DNMT3A → Dusp4 methylation). The delayed step is what commits the macrophage to the COX2-PGE2-TGFβ1 resolution program; without it, the early ERK signal is quenched by DUSP4 negative feedback. They emphasise that this is a genuinely new mechanism distinct from prior AC-cargo-driven resolution pathways (arginine, fatty acid, cholesterol) because it operates through *DNA methylation* rather than transcription factor activation. The findings are framed as a candidate mechanism linking DNMT3A clonal-haematopoiesis (CHIP) mutations to coronary artery disease — a known epidemiological association without a clear mechanism — by predicting that partial DNMT3A loss-of-function in plaque macrophages would impair the resolution program documented here.

### Comparisons with prior literature (made by authors)

- **Yurdagul, Doran, Cai et al. (Tabas-lab prior work, refs 6-8)** — established that AC-derived arginine, fatty acids, and cholesterol drive distinct resolution programs in macrophages. This paper extends to methionine as the *epigenetic* arm.
- **Tabas / Bornfeldt 2016 (ref 9)** — established efferocytosis-PGE2-TGFβ1 as a resolution axis; this paper provides mechanistic underpinnings.
- **Rőszer 2015 / DNMT3A biology (ref 28)** — DNMT3A is the postnatal de novo methyltransferase in mature cells.
- **CHIP-CAD epidemiology (ref 49)** — Jaiswal 2017 NEJM linking DNMT3A loss-of-function to CAD; authors propose their pathway as candidate mechanism.
- **AC-driven mesenchymal stem cell therapy (refs 51-54)** — apoptotic cell infusion in clinical trials (GVHD); authors suggest their mechanism may be exploited therapeutically.

### Mechanistic hypotheses proposed

- Two-step efferocytosis signalling: AC-binding (ERK pulse, insufficient) + AC-degradation (methionine→SAM→DNMT3A→Dusp4 repression) → sustained ERK → COX2/PGE2/TGFβ1.
- DNMT3A acts at a *second* site downstream of PGE2 to enable p-CREB1 — mechanism unresolved.
- AC-methionine may be rate-limiting for specific DNA methylation events because endogenous SAM is depleted by other macrophage methyltransferase reactions.

### Caveats and self-criticism

- Direct causal link Dusp4-promoter-methylation → Dusp4 repression inferred from MeDIP enrichment + DNMT3A KO, not from targeted promoter demethylation.
- "Future studies are needed to show that AC-derived methionine per se is the source of methyl groups on the Dusp4 promoter and that methylation of this promoter is directly responsible for AC-induced repression of Dusp4 expression."
- Pharmacological inhibitors (PF-9366, bafilomycin, U0126) all have potential off-targets at sustained or high doses.

### Future directions suggested

- Genome-wide methylation analysis (WGBS / ATAC-seq) in control vs DNMT3A-KO ± AC macrophages.
- Whether histone methyltransferases also use AC-derived SAM.
- Whether prolonged ERK activation in DNMT3A-deficient macrophages affects gene programs beyond Ptgs2.
- Whether CHIP-associated DNMT3A R882H phenocopies homozygous KO.
- Therapeutic exploitation: AC infusion therapies (mesenchymal stem cells) likely engage this pathway.

## Limitations

- Direct causal link between Dusp4-promoter methylation and Dusp4 repression is inferred, not demonstrated by targeted demethylation (e.g., dCas9-TET).
- AC-methionine as the *specific* methyl source on the Dusp4 promoter is inferred from bulk 13C-mC tracking, not site-specific.
- No genome-wide methylation (WGBS) or chromatin accessibility (ATAC-seq) data to identify other DNMT3A-dependent efferocytosis-induced sites.
- Conditional Vav1Cre KO targets all haematopoietic lineages, not strictly macrophage; LysMCre or CD68Cre would be cleaner.
- TET-family demethylase contribution to the steady-state Dusp4 methylation balance is unaddressed.
- The DNMT3A-dependent step downstream of PGE2 (enabling p-CREB1) is mechanistically unresolved.
- Only Jurkat (or apoptotic macrophage) AC source tested — tissue-relevant ACs (apoptotic neutrophils, thymocytes) used only in vivo.
- Pharmacological inhibitors (PF-9366, bafilomycin, U0126) all have off-target liabilities; orthogonal validation by genetic perturbation strengthens but does not eliminate the concern.

## Open questions

### Open questions raised by authors

- What other gene promoters are DNMT3A-methylated during efferocytosis (genome-wide map needed)?
- Does AC-methionine specifically route to the Dusp4 promoter or genome-wide?
- Does prolonged ERK activation in DNMT3A-deficient cells affect other gene programs beyond Ptgs2?
- Are histone methyltransferases also fed by AC-methionine?
- Is DNMT3A enzymatic activity itself stimulated by efferocytosis (beyond substrate provision)?
- Does CHIP-associated DNMT3A R882H phenocopy homozygous KO?

### Open questions identified during ingest

- Whether the pathway operates in tissue-resident macrophages (Kupffer, microglia, RPE) or only MoDM.
- Whether dietary methionine restriction in atherosclerotic mice phenocopies haematopoietic DNMT3A loss.
- Whether the iMAC1 paradox from hypoxic-macrophage work (NF-κB-targets *down* in unstimulated hypoxic MACs) has any parallel here — i.e., does hypoxia + AC exposure interact with the DNMT3A-Dusp4 axis?
- Whether dCas9-TET2 targeted demethylation of the Dusp4 promoter would phenocopy DNMT3A KO at the Dusp4 locus.
- Whether the pathway is preserved or rewired in tumour-associated macrophages eating apoptotic tumour cells.

## My take

Strong, multi-modal mechanism paper from a top efferocytosis lab. The two key conceptual contributions:
1. **Epigenetic AC-cargo signalling**: macrophages don't just metabolise AC content — they use AC-derived methionine specifically as a DNA-methylation substrate. The isotope tracing (13C-methionine → 13C-SAM → 13C-mC) is the cleanest line of evidence and establishes the metabolic route definitively.
2. **Two-step efferocytosis signalling**: the CD36-ERK transient pulse + delayed methionine-DNMT3A-Dusp4-sustained-ERK loop is a structurally novel signalling architecture (sensor + commit-step), distinct from other receptor-only or cargo-only resolution programs.

The DNMT3A-CHIP-CAD link is speculative but very plausible — CHIP carriers with partial DNMT3A loss may have weakened plaque resolution exactly through impaired efferocytosis-driven TGF-β1, leading to thinner fibrous caps and unstable plaques. This is a high-value testable hypothesis.

The unresolved DNMT3A-dependent step in PGE2 → p-CREB1 is the most interesting loose end. The authors flag it but do not pursue. Candidate mechanisms include DNMT3A-mediated repression of a phosphatase acting on CREB1, methylation of an EP2/4-downstream regulator, or a non-catalytic scaffolding role for DNMT3A.

Methodologically, the integration of isotope tracing + conditional KO + chemical genetics + three orthogonal in vivo resolution models + functional rescue (TGF-β1 ip) is exemplary.

For a HypoxiaVERSE / macrophage thesis, this paper is an important methodological reference for efferocytosis biology and a useful cross-link if any project examines macrophage DNA-methylation dynamics under cargo loading or hypoxic plaque conditions. The mechanism is hypoxia-independent in this paper, but interaction effects are worth exploring (e.g., does NF-κB-driven TET demethylation in hypoxic macrophages [[concepts/nf-kb-mediated-dna-demethylation-hypoxia]] oppose the DNMT3A methylation event here?).

## Related

- [[concepts/efferocytosis-anti-inflammatory-clearance]] — broad efferocytosis concept; this paper provides one of the canonical mechanistic underpinnings of the anti-inflammatory output (PGE2 + TGF-β1)
- [[concepts/dnmt3a-dusp4-efferocytosis-resolution-pathway]] — the central pathway defined by this paper
- [[concepts/ac-derived-methionine-sam-macrophage-epigenetics]] — the broader principle that AC cargo metabolites fuel macrophage epigenetic states
- [[foundations/dnmt3a-de-novo-dna-methyltransferase]] — central enzyme
- [[foundations/ptgs2-cox2]] — central enzyme
- [[foundations/pge2-prostaglandin-e2]] — central mediator
- [[foundations/mat2a-methionine-adenosyltransferase]] — central enzyme
- [[foundations/s-adenosylmethionine-sam]] — central metabolite
- [[foundations/dusp4-dual-specificity-phosphatase-4]] — the regulated phosphatase
- [[foundations/cd36-scavenger-receptor]] — central receptor
- [[foundations/mertk-tam-receptors]] — secondary receptor
- [[foundations/creb1-transcription-factor]] — downstream TF
- [[foundations/mapk1-3-erk1-2-kinases]] — central kinase axis
- [[foundations/tgfb1-cytokine]] — central output
- [[foundations/pf-9366-mat2a-inhibitor]] — MAT2A tool inhibitor
- [[foundations/u0126-mek-erk-inhibitor]] — MEK tool inhibitor
- [[foundations/bafilomycin-a1-vacuolar-atpase]] — phagolysosomal tool inhibitor
- [[foundations/medip-methylated-dna-immunoprecipitation]] — DNA methylation enrichment method
- [[papers/metabolism-tissue-macrophages-homeostasis-pathology]] — Wculek 2022 *Cell Mol Immunol* — broader macrophage immunometabolism context for AC-cargo-driven programs
