---
# === Identification ===
title: "Cancer-Associated Cachexia: Bridging Clinical Findings with Mechanistic Insights in Human Studies"
slug: cancer-associated-cachexia-bridging-clinical-findings
arxiv: ""
doi: "10.1158/2159-8290.CD-25-0293"
pmid: ""
venue: "Cancer Discovery"
year: 2025
authors:
  - "Kexin Koh"
  - "Rachel Scott"
  - "Elizabeth M. Cespedes Feliciano"
  - "Tobias Janowitz"
  - "Marcus D. Goncalves"
  - "Eileen P. White"
  - "Barry J.A. Laird"
  - "Kerstin Haase"
  - "Mariam Jamal-Hanjani"
first_author: "Kexin Koh"
corresponding_author: "Mariam Jamal-Hanjani"

# === Source & metadata ===
source_type: pdf
s2_id: ""
date_added: 2026-05-27
ingested_date: 2026-05-27
ingest_version: 1
last_reviewed: null

# === Classification ===
importance: 4
tier: TIER_1
tags:
  - cancer-cachexia
  - human-studies
  - clinical-phenotyping
  - body-composition
  - CT-L3-imaging
  - sarcopenia
  - TRACERx
  - central-melanocortin-system
  - cancer-anorexia
  - cori-cycle
  - hypermetabolism
  - PTHrP
  - GDF-15
  - WAT-browning
  - UCP1
  - lipolysis
  - HSL
  - ATGL
  - ubiquitin-proteasome-MURF1-Atrogin1
  - muscle-protein-synthesis
  - patient-reported-outcomes
  - FAACT
  - PG-SGA
  - chemotherapy-induced-cachexia
  - immunotherapy-cachexia
  - PET-isotope-tracing
  - review
keywords:
  - CAC clinical phenotyping
  - body composition CT subtypes (SAT/VAT/SKM)
  - Fearon and Evans diagnostic criteria
  - TRACERx NSCLC cachexia thresholds
  - latent trajectories of body composition loss
  - pre-CAC phase precedes pancreatic cancer diagnosis
  - sex dimorphism in muscle loss
  - FOLFIRINOX vs GEM/NAB differential body-compartment loss
  - hypothalamic fMRI in cancer anorexia
  - melanocortin POMC AgRP MC4R in CAC
  - tumor-driven Cori cycle and hypermetabolism
  - PTHrP-driven WAT browning conflicting in humans
  - PET ML model for CAC detection
  - HSL ATGL catecholamine-stimulated lipolysis
  - UPS MURF1 Atrogin-1 conflicting human evidence
  - postprandial anabolic resistance in CAC muscle
domain: "oncology / metabolism / cachexia / clinical review"

# === Biomedical domain ===
tissue:
  - skeletal_muscle
  - adipose_SAT
  - adipose_VAT
  - liver
  - brain_hypothalamus
  - blood
  - multi
condition:
  - cancer
disease_specific:
  - cancer_cachexia
  - sarcopenia
  - NSCLC_cachexia
  - pancreatic_cancer_cachexia
  - colorectal_cancer_cachexia
species:
  - human
hypoxia_relevant: false
contains_immune_cells: false
contains_myeloid: false

# === Technique ===
techniques:
  - CT_L3_body_composition_segmentation
  - MRI_body_composition
  - DEXA
  - bioimpedance_BIA
  - hypothalamic_fMRI
  - PET_FDG_imaging
  - in_vivo_13C_glucose_tracing
  - in_vivo_heavy_isotope_tracing
  - immunoassay_PTHrP
  - HGS_handgrip_strength
  - 6MWT
  - FAACT_PRO
  - PG-SGA
  - ECOG_performance_status
  - latent_trajectory_modelling
  - machine_learning_PET_segmentation
n_samples: null
n_cells_total: null
integration_method: ""

# === Biology captured ===
key_cell_types:
  - skeletal_muscle_fibre
  - adipocyte_SAT
  - adipocyte_VAT
  - hepatocyte
  - POMC_neuron_ARC
  - AgRP_NPY_neuron_ARC
key_markers:
  - IL6
  - TNF
  - IL1
  - GDF-15
  - PTHrP
  - UCP1
  - HSL_LIPE
  - ATGL_PNPLA2
  - MURF1_TRIM63
  - Atrogin-1_FBXO32
  - Beclin-1
  - MAP1LC3B
  - caspase-8
  - caspase-9
  - mTOR
  - IGF-1
  - leptin
  - ghrelin
  - alpha-MSH
  - MC4R
  - AgRP
  - POMC
  - activin-A
  - CRP
  - albumin
key_pathways:
  - central_melanocortin_appetite_regulation
  - HPA_axis_glucocorticoid_signaling
  - cori_cycle_lactate_glucose_recycling
  - hepatic_gluconeogenesis
  - adipose_lipolysis_HSL_ATGL
  - WAT_browning_UCP1
  - ubiquitin_proteasome_proteolysis
  - autophagy_lysosomal_proteolysis
  - mTOR_protein_synthesis
  - IL6_inflammatory_signaling

# === User project membership ===
projects:
  - thesis
priority: context
read_status: read

# === HypoxiaVERSE-specific ===
hypoxiaverse_status: excluded
exclusion_reason: "Clinical review of cancer-associated cachexia in human studies; not hypoxia-focused. Useful as the canonical human-evidence reference for CAC mechanisms, phenotyping and treatment interactions — companion to [[papers/multi-omics-profiling-cachexia-targeted-tissues]]."
data_availability: "Review — no primary data; cites cohorts including TRACERx (NCT01888601) and NCT06431476/NCT06073431."

# === Cross-references ===
code_url: ""
cited_by: []
---

## Problem

Cancer-associated cachexia (CAC) is a chronic wasting syndrome affecting 15-80% of patients with cancer depending on tumour site, strongly predicts mortality, and has no globally approved effective therapy. Despite >150 years of clinical recognition, definitions remain inconsistent, animal-model mechanisms have translated poorly, and CAC clinical heterogeneity (sarcopenic obesity, isolated body-compartment loss, anorexia-only phenotypes) is not captured by weight-loss-centric criteria. The field needs a synthesis of HUMAN evidence — clinical phenotyping, mechanism, and therapeutic options — to bridge the bench-to-bedside gap and guide trial stratification and intervention design.

## Key idea

A comprehensive review of human evidence in CAC organized around three axes: (i) **clinical phenotyping** via imaging-derived body composition (CT-L3 SAT/VAT/SKM segmentation), patient-reported outcomes (FAACT, PG-SGA), and functional assessments (HGS, 6MWT, ECOG); (ii) **mechanistic insight from human studies** spanning anorexia (central melanocortin system mapped by hypothalamic fMRI), tumour-driven host metabolic rewiring (Cori cycle, hypermetabolism, PET-isotope tracing of glucose/lactate fluxes), adipose tissue wasting (lipolysis via HSL/ATGL/catecholamines, contested WAT browning), and muscle wasting (UPS via MURF1/Atrogin-1, autophagy, blunted postprandial protein synthesis); (iii) **bidirectional interaction with anticancer therapy** (treatment-induced cachexia in NSCLC/PDAC/CRC; pretreatment SKM affects toxicity and survival). The review emphasizes that animal models exaggerate CAC features (Lewis lung, C26 IL-6 >600 pg/mL) and that distinct clinical subtypes — adipose-tissue-loss-only vs adipose+SKM-loss — may need bespoke therapeutic strategies.

## Method

This is a narrative review (not primary data). The authors synthesize:

- Diagnostic-criteria comparison across Fearon, Evans, SCRINIO, Zhou, Argilés (CASCO) and Silva (mGPS) frameworks.
- Imaging-based body composition methodology (CT-L3 segmentation, MRI, DEXA, BIA) and automated AI segmentation.
- Cross-sectional and longitudinal cohort findings, including the prospective TRACERx-NSCLC body-composition arm (Al-Sawaf, Goncalves et al.), Jin et al. liver-cancer trajectory analysis, Klassen et al. PDAC chemotherapy-by-sex analysis, and Sun et al. multi-tissue metabolomics.
- Human-evidence mechanistic studies: hypothalamic fMRI in lung CAC (Molfino et al.) and colorectal CAC (Simoes et al.); in vivo [13C]-glucose / [13C]-lactate tracing in NSCLC tumours (Hensley et al., Faubert et al.); PET-derived ML model for CAC detection.
- In-tissue molecular evidence from adipose (lipolysis enzymes, adipocyte morphology) and skeletal muscle (UPS markers, autophagy markers, myofibrillar protein synthesis rates).
- Clinical trials registry references (NCT06431476, NCT06073431) for ongoing deep-phenotyping initiatives.

## Results

### 1. Diagnostic and staging criteria of CAC are non-unified
- Fearon criterion is most widely used (weight loss thresholds + low BMI + sarcopenia); Evans adds biochemistry (CRP, IL-6, Hb, albumin).
- Staging tools span CASCO (LBM + metabolic/inflammatory + PROs + function), Zhou score (5 components incl. ECOG), and Silva mGPS (CRP + albumin only).
- None incorporate adipose tissue loss thresholds despite prognostic relevance in lung and pancreatic cancers — a critical gap.

### 2. CT-L3 body-composition phenotyping enables CAC subtypes
- CT discriminates SAT, VAT, SKM, intermuscular adipose; L3-vertebra single-slice strongly correlates with whole-body measures.
- AI segmentation now scales to multi-vertebral analysis; major implementation challenges remain in reference values (mostly White Non-Hispanic), thresholds, and image-acquisition variability (slice thickness alters SKM area 1%, VAT area 3%).
- TRACERx-NSCLC defined CAC as ≥1 of: >10% SKM loss, >20% SAT loss, >20% VAT loss, or grade-4 BMI-adjusted weight loss.

### 3. Clinical CAC subtypes by body-compartment loss
- Pancreatic-cancer cohort (Klassen): "adipose-tissue-loss only" and "adipose + SKM loss" subtypes coexist with a no-loss group, independent of tumour response, sarcopenia or obesity. Both worse survival.
- TRACERx patients with isolated SKM loss (>10% vs <10%) had distinct primary-tumour gene-expression profiles, suggesting biological subtypes.
- Sun et al. metabolomics: more metabolite elevations in SAT/VAT/liver, more reductions in SKM — divergent organ-level pathway alterations.

### 4. Treatment-induced cachexia and pretreatment body composition shape outcomes
- Chemotherapy, immunotherapy and radiotherapy can induce/exacerbate weight + SKM loss (nasopharyngeal, head/neck, renal, CRC, ovarian, melanoma).
- FOLFIRINOX → greater SKM loss in males; GEM/NAB → greater adipose-tissue loss in both sexes (advanced PDAC).
- Low pretreatment BMI/SKM (or sarcopenia) → higher treatment toxicity and worse survival; some chemotherapies (cytotoxics) distribute in LBM, so body-surface-area dosing under-corrects for low SKM.

### 5. Anorexia and central melanocortin system in human CAC
- Anorexia prevalence: 26% (advanced breast) - 40% (advanced gastric/CRC); FAACT-ACS is a stronger survival predictor than 6-month weight loss in metastatic esophagogastric cancer.
- Hypothalamic fMRI differentiates lung-cancer patients with vs without anorexia after oral nutritional supplementation; CRC-CAC patients show structural and functional CNS changes (Simoes et al.), suggesting neuroinflammation.
- Mechanistic framework: POMC/α-MSH (anorexigenic, ARC + NTS) vs NPY/AgRP (orexigenic, ARC); MC3R/MC4R balance modulated by IL-6, TNF-α, GDF-15, leptin, ghrelin.

### 6. Tumour-driven host metabolic rewiring
- Negative energy balance: reduced intake (up to ~50% of REE in severe), malabsorption, and hypermetabolism (REE elevation).
- Tumour rewires host metabolism toward energetically expensive futile cycles: Cori cycle (hepatic gluconeogenesis from tumour-derived lactate); increased fat oxidation and proteolysis.
- PTHrP detected in NSCLC blood (immunoassay) → ↓LBM, ↑REE, implicated in WAT browning via UCP1 induction in primary brown/white adipocyte cultures.
- In-vivo isotope tracing (Faubert, Hensley): NSCLC tumours utilize lactate to fuel TCA — lactate is not just waste. NSCLC tumours exhibit higher glucose oxidation than adjacent normal tissue.
- Lieffers et al.: increased liver weight (incl. metastases) ↔ increased REE in advanced CRC.
- Mitamura: PET tumour glucose uptake ↔ energy expenditure and weight loss in esophageal cancer; subsequent NSCLC studies confirmed; ML model on PET/CT detects CAC at diagnosis (NSCLC, n=cohort retrospective) with 81% accuracy — top features: spleen, pancreas, liver, adipose uptake.

### 7. Adipose-tissue wasting: lipolysis dominates over impaired anabolism
- Adipocytes smaller (not fewer) in GI-CAC SAT vs weight-stable — consistent with lipolysis-driven loss.
- Plasma glycerol and FFAs elevated. Catecholamine + natriuretic-peptide stimulation of HSL is stronger in CAC.
- Mouse-model ATGL primacy not strongly supported in humans yet.
- WAT browning evidence in humans is conflicting: Petruzzelli et al. showed UCP1 in WAT of 7/8 CAC patients; but a 14,134-patient cohort showed BAT prevalence LOWER (not higher) in CAC, no survival association; PDAC VAT showed no UCP1 differential. To date NO conclusive evidence WAT browning drives human CAC REE elevation.

### 8. Muscle wasting: conflicting UPS/autophagy evidence + impaired anabolism
- MURF1, Atrogin-1, ubiquitinated proteins, proteasome activity: ELEVATED in some CAC cohorts (Khal, Bossola), UNCHANGED in others (Stephens) — definition and cohort heterogeneity drives discrepancy.
- Autophagy markers Beclin-1, MAP1LC3B: elevated in some studies, unchanged in others; flux not directly measured.
- Apoptosis (caspase-8/9) elevated in advanced GI-CAC (~15% weight loss) but not in <10% weight-loss gastric cohort — late-stage feature.
- MacDonald et al.: myofibrillar protein synthesis HIGHER in GI-CAC vs controls, but synthesis < breakdown → net catabolism.
- Postprandial protein synthesis is BLUNTED in CRC/PDAC-CAC vs healthy controls — anabolic resistance, supporting nutrition-alone failures.

## All claims (exhaustive)

- `[c1]` CAC prevalence varies dramatically by cancer type — 15-30% in blood/breast/prostate vs 40-80% in lung/gastric/pancreatic (p.1544) "Higher incidence is observed in lung cancer, gastric cancer, and pancreatic cancer, ranging from 40\% in lung to as high as 80\% in pancreatic cancer" — confidence: high — type: correlational — links: [[concepts/cac-clinical-phenotyping-body-composition]] [[foundations/cancer-cachexia]] [[claims/cac-prevalence-varies-by-cancer-type]]
- `[c2]` Pancreatic-cancer CAC has at least two body-composition subtypes — "adipose-tissue-loss only" and "adipose + SKM loss" — independent of tumour response, sarcopenia or obesity; both have worse survival (p.1547) "two CAC phenotypes were identified – 'adipose tissue loss only' and 'adipose and SKM tissue loss' – alongside a group of patients with no tissue loss, independent of tumor response, sarcopenia, or obesity" — confidence: high — type: correlational — links: [[concepts/cac-clinical-subtypes-body-composition]] [[claims/cac-subtypes-by-body-composition-pancreatic]]
- `[c3]` TRACERx-NSCLC defines CAC thresholds as ≥1 of >10% SKM loss, >20% SAT loss, >20% VAT loss, or grade-4 BMI-adjusted weight loss, and shows isolated SKM-loss subtype has distinct primary-tumour gene expression (p.1547) "Body composition analyses between diagnosis and first relapse after primary surgery identified thresholds for defining CAC as at least one of the following criteria: >10\% SKM loss, >20\% SAT loss, >20\% VAT loss, or grade 4 BMI-adjusted weight loss" — confidence: high — type: methodological — links: [[concepts/ct-l3-body-composition-phenotyping]] [[foundations/tracerx-nsclc-cohort]] [[claims/tracerx-nsclc-cac-thresholds]]
- `[c4]` Jin et al. liver-cancer latent-trajectory analysis (n=2,138 measurements) identifies stable vs sharp-falling SKM and adipose trajectories; sharp-falling = CAC with worse survival (p.1547) "two distinct trajectories for SKM and total adipose tissue area were defined, stable and sharp-falling, using 2,138 body composition measurements" — confidence: high — type: methodological — links: [[concepts/ct-l3-body-composition-phenotyping]] [[claims/longitudinal-trajectories-cac-liver-cancer]]
- `[c5]` Body-composition loss precedes clinical pancreatic-cancer diagnosis (pre-CAC phase) — SKM/VAT/SAT loss detectable before diagnosis (p.1547) "the loss of SKM, VAT, and SAT has been shown to precede clinical diagnosis of pancreatic cancer, suggesting the existence of a pre-CAC phase that can be detected with body composition change" — confidence: medium — type: correlational — links: [[concepts/cac-clinical-subtypes-body-composition]] [[claims/body-composition-loss-precedes-pancreatic-cancer-diagnosis]]
- `[c6]` CAC shows sex dimorphism — loss of muscle mass observed in males but not females across various advanced cancer types (p.1544) "There may also be sexual dimorphism underlying CAC as the loss of muscle mass in males but not in females has been observed in various advanced cancer types" — confidence: medium — type: correlational — links: [[concepts/cac-clinical-subtypes-body-composition]] [[claims/sex-dimorphism-skm-loss-cac]]
- `[c7]` Reduced handgrip strength is associated with poor survival in CAC across European and Chinese populations and slow gait in elderly Indian populations (p.1548) "Reduced HGS has been associated with poor survival in patients with CAC in European-based and Chinese populations and slow walking speed in elderly Indian population" — confidence: high — type: correlational — links: [[concepts/cac-clinical-phenotyping-body-composition]] [[claims/hgs-predicts-cac-survival]]
- `[c8]` FOLFIRINOX is associated with greater SKM loss in males whereas GEM/NAB is associated with greater adipose-tissue loss in both sexes in advanced PDAC (p.1549) "FOLFIRINOX (folinic acid, 5-fluorouracil, irinotecan, and oxaliplatin) was associated with greater SKM loss in males whereas GEM/NAB (gemcitabine and nab-paclitaxel) was associated with greater adipose tissue loss in both sexes" — confidence: high — type: pharmacological — links: [[concepts/treatment-induced-cachexia]] [[claims/folfirinox-vs-gemnab-differential-loss]]
- `[c9]` Pretreatment weight loss is associated with poor tumour response and severe dose-limiting toxicity in breast and gastrointestinal cancers (p.1549) "previous studies have shown that weight loss prior to chemotherapy is associated with poor tumor response and severe dose-limiting toxicity in patients with breast and gastrointestinal cancers" — confidence: high — type: correlational — links: [[concepts/treatment-induced-cachexia]] [[claims/pretreatment-weight-loss-poor-tumour-response]]
- `[c10]` Hypothalamic fMRI differentiates lung-cancer patients with vs without anorexia after oral nutritional supplementation, demonstrating CNS involvement in human CAC anorexia (p.1550) "in 13 patients with lung cancer, hypothalamic activity has been shown to differ between patients with and without anorexia (but without weight loss) after oral nutritional supplementation, indicating the role of the CNS in the development of cancer-associated anorexia" — confidence: medium — type: methodological — links: [[concepts/central-melanocortin-system-cancer-anorexia]] [[foundations/fmri-functional-mri-method]] [[claims/hypothalamic-fmri-distinguishes-cac-anorexia]]
- `[c11]` Patients with NSCLC who have detectable circulating PTHrP exhibit lower LBM and higher REE, with PTHrP inducing UCP1 in primary brown/white adipocyte cultures (p.1551) "patients with NSCLC who had detectable blood PTHrP levels measured by immunoassay exhibited lower LBM and higher REE" — confidence: medium — type: correlational — links: [[foundations/pthrp-parathyroid-hormone-related-protein]] [[foundations/ucp1]] [[claims/pthrp-detection-nsclc-lower-lbm-higher-ree]]
- `[c12]` The Cori cycle is rewired by tumour to recycle lactate→glucose via hepatic gluconeogenesis, an energetically expensive futile cycle contributing to host hypermetabolism in CAC (p.1551) "Cancer may elevate metabolic demands by rewiring host metabolism to favor energetically expensive futile cycles such as the Cori cycle, in which ATP is consumed to recycle glucose from lactate in the liver, which is subsequently utilized by the tumor" — confidence: medium — type: mechanistic — links: [[concepts/cori-cycle-tumor-host-metabolism]] [[claims/cori-cycle-tumor-host-futile-cycle]]
- `[c13]` Lactate is utilized by NSCLC tumours to fuel the TCA cycle, contradicting the assumption that lactate is solely a Cori-cycle waste product (p.1551) "in recent years, lactate has been shown to be utilized by tumors to fuel the TCA cycle in patients with NSCLC" — confidence: medium — type: mechanistic — links: [[concepts/cori-cycle-tumor-host-metabolism]] [[claims/lactate-fuels-nsclc-tca]]
- `[c14]` NSCLC tumours exhibit higher glucose oxidation than adjacent normal tissue, demonstrated by in vivo heavy-isotope tracing (p.1551) "in patients with NSCLC, tumors exhibited higher glucose oxidation than adjacent normal tissues" — confidence: medium — type: methodological — links: [[concepts/cori-cycle-tumor-host-metabolism]] [[claims/nsclc-tumour-higher-glucose-oxidation-than-adjacent]]
- `[c15]` A machine-learning model trained on retrospective whole-body PET/CT in lung-cancer patients identifies CAC at diagnosis with 81% accuracy, with spleen, pancreas, liver and adipose uptake emerging as the most predictive features (p.1551) "a machine-learning model built on a retrospective cohort of patients with lung cancer was able to identify CAC at diagnosis with 81\% accuracy, with uptake values from spleen, pancreas, liver, and adipose tissue emerging as the most predictive features" — confidence: medium — type: quantitative — links: [[concepts/cori-cycle-tumor-host-metabolism]] [[claims/pet-ml-model-detects-cac-nsclc-81-accuracy]]
- `[c16]` In gastrointestinal CAC, abdominal SAT adipocytes are smaller in size (not fewer in number) compared with weight-stable patients, consistent with lipolysis-driven adipose wasting (p.1551) "In patients with gastrointestinal CAC, the size, as opposed to number, of adipocytes from abdominal SAT has been shown to be smaller than that of weight-stable patients" — confidence: high — type: mechanistic — links: [[concepts/adipose-lipolysis-cancer-cachexia]] [[claims/cac-sat-adipocyte-size-reduced]]
- `[c17]` The lipolytic effect of catecholamines and natriuretic peptides on hormone-sensitive lipase (HSL) is stronger in CAC patients than in weight-stable patients (p.1552) "The lipolytic effects of catecholamines and natriuretic peptides on HSL have been shown to be stronger in patients with CAC" — confidence: medium — type: mechanistic — links: [[concepts/adipose-lipolysis-cancer-cachexia]] [[foundations/hsl-hormone-sensitive-lipase]] [[claims/catecholamine-lipolysis-stronger-in-cac]]
- `[c18]` Evidence for WAT browning driving human CAC is conflicting: Petruzzelli et al. found UCP1 in 7/8 CAC patients' WAT, but a 14,134-patient cohort showed BAT prevalence LOWER (not higher) in CAC with no survival association, and PDAC VAT shows no UCP1 differential (p.1552) "a retrospective study in a cohort of 14,134 patients with various cancer types demonstrated a higher prevalence of brown adipose tissue (BAT) in patients without CAC compared with patients with CAC at diagnosis" — confidence: medium — type: correlational — links: [[concepts/adipose-lipolysis-cancer-cachexia]] [[foundations/ucp1]] [[claims/wat-browning-human-cac-evidence-conflicting]]
- `[c19]` UPS markers MURF1 and Atrogin-1, ubiquitinated proteins and proteasome activity are reported as elevated in some human CAC cohorts and unchanged in others, with cohort definitions (weight-loss cutoffs) driving the discrepancy (p.1552) "the expression of UPS markers such as muscle RING finger–containing protein 1 and Atrogin-1, ubiquitinated proteins, and proteasome proteolytic activity have been shown to be either elevated or unchanged in patients with gastrointestinal and lung CAC" — confidence: medium — type: methodological — links: [[concepts/muscle-wasting-ups-autophagy-cac]] [[foundations/murf1-trim63]] [[foundations/atrogin1-fbxo32]] [[claims/ups-markers-conflicting-evidence-cac]]
- `[c20]` In GI-CAC, myofibrillar protein synthesis rate is HIGHER than in weight-stable patients or healthy controls, but lower than the rate of muscle protein breakdown — yielding net catabolism (MacDonald et al.) (p.1552) "muscle myofibrillar protein synthesis was higher in patients with gastrointestinal CAC compared with weight-stable patients or healthy controls, the rate of muscle protein synthesis was lower than the rate of muscle protein breakdown, resulting in net catabolism" — confidence: medium — type: quantitative — links: [[concepts/muscle-wasting-ups-autophagy-cac]] [[claims/muscle-protein-synthesis-lower-than-breakdown-cac]]
- `[c21]` Postprandial muscle protein synthesis is blunted in CRC/PDAC-CAC vs healthy controls, indicating anabolic resistance to feeding and rationalizing nutrition-alone treatment failures (p.1552) "muscle protein synthesis is blunted in response to feeding among patients with colorectal and pancreatic CAC, in contrast to healthy controls for whom muscle protein synthesis is stimulated in the postprandial state" — confidence: high — type: mechanistic — links: [[concepts/muscle-wasting-ups-autophagy-cac]] [[claims/postprandial-protein-synthesis-blunted-cac]]

## Discussion captured

### Authors' interpretation
The authors argue that animal-model-derived mechanisms have NOT translated to humans, and that CAC heterogeneity in patients (subtypes by body-compartment loss, sex dimorphism, treatment-modality dependence) reflects underlying biological subtypes that current diagnostic criteria mask. They position deep clinical phenotyping (via TRACERx-style cohorts, multi-omics, in vivo isotope tracing, hypothalamic fMRI) as the way forward — not a single unifying definition but a SPECTRUM of CAC subtypes each potentially needing bespoke intervention. They explicitly call for unified body-composition reference values across ethnicities and standardization of CT-acquisition parameters.

### Comparisons with prior literature (made by authors)
- Argue Lewis-lung and C26 mouse models (IL-6 >600 pg/mL, tumours >5% BW) DO NOT recapitulate human CAC inflammatory or tumour-burden scale (refs. 26-29).
- Compare Fearon (ref. 3, most widely used) vs Evans (ref. 2) vs CASCO (Argilés, ref. 41) vs Silva mGPS (ref. 40) — emphasize lack of unification.
- Acknowledge Petruzzelli et al. (ref. 184) finding of UCP1 in human WAT but cite the contradicting 14,134-patient cohort (ref. 186) and PDAC VAT UCP1-no-change study (ref. 187) to argue browning evidence is NOT settled in humans.
- Contrast Khal (ref. 196 — UPS elevated, severe CAC cutoff 11%) vs Stephens (ref. 200 — UPS unchanged, 5% cutoff) — attribute discrepancy to definition heterogeneity.
- Cite Faubert / Hensley NSCLC isotope tracing (refs. 165, 166) as reframing lactate from waste to TCA fuel.

### Mechanistic hypotheses proposed
- "Perhaps the best approach is to perform deep phenotyping of CAC manifestation in patients to define subtypes representing the spectrum of conditions rather than trying to define it as a single condition (NCT06073431)" (p.1545).
- Tumour-driven Cori-cycle rewiring contributes more to host hypermetabolism than the Warburg effect inside the tumour itself (p.1551).
- WAT browning in human CAC, if it occurs, is likely a minor contributor to REE elevation — most evidence is methodologically conflicting (p.1552).
- Anabolic resistance to feeding (blunted postprandial protein synthesis) explains the failure of nutrition-alone CAC interventions (p.1552).

### Caveats and self-criticism
- Acknowledge that CT-derived reference values are primarily from "White non-Hispanic outpatients and study participants of the Framingham Heart Study" — limiting global applicability.
- Concede that "human evidence for [REE elevation] is limited, and additional data are urgently needed to quantify the changes in energy balance in humans with cancer" (p.1550).
- Note that Beclin-1 and MAP1LC3B are POOR indicators of autophagy flux — calls into question many existing studies (p.1552).
- Highlight cohort/definition heterogeneity as a recurring source of conflict in the field.

### Future directions suggested
- Develop multiethnic CT-based reference values; standardize CT-acquisition parameters and segmentation precision testing.
- Use longitudinal trajectory modelling (Jin et al. approach) and TRACERx-style prospective cohorts to define CAC subtypes prospectively.
- Apply hypothalamic fMRI more broadly to map central CAC mechanisms in humans.
- Use in vivo heavy-isotope tracing and dynamic PET/MRI to characterize tumour-host metabolic flux at the patient level.
- Develop CAC-subtype-specific therapeutics (e.g., anabolic-resistance-targeting nutrition + exercise + drug combinations).

## Limitations

- Review is NARRATIVE not systematic — no PRISMA inclusion criteria or reproducible search.
- Heavily weighted toward GI-cancer and lung-cancer cohorts; sparse on breast, prostate, hematological cancers.
- Mechanistic evidence in humans is overwhelmingly cross-sectional or post hoc — few longitudinal causal experiments.
- Therapeutic-trial review (in the original paper, beyond this ingest's text) is acknowledged to be uneven across stages of CAC.
- Author conflict-of-interest disclosures not assessed here.

## Open questions

### Open questions raised by authors
- Is CAC a single condition or a spectrum of subtypes each with distinct mediators? (p.1545)
- Do specific cancer types or treatments require bespoke CAC interventions? (p.1547-1549)
- Does WAT browning meaningfully contribute to human CAC REE elevation, or is it a minor/artefactual finding? (p.1552)
- What is the relative contribution of UPS vs autophagy vs apoptosis vs anabolic resistance to net muscle loss across CAC stages? (p.1552)
- Are NSCLC tumour-uptake patterns (high glucose oxidation, lactate fueling TCA) a CAUSE of host hypermetabolism or just a correlate? (p.1551)
- Why does sex dimorphism manifest in muscle loss but not always in adipose loss?

### Open questions identified during ingest
- The interaction between immunotherapy (checkpoint inhibitors) and CAC is mentioned but underexplored — is ICI-induced cachexia mechanistically distinct from chemotherapy-induced cachexia?
- Are the body-composition subtypes (adipose-only vs adipose+SKM) genetically/transcriptomically stratifiable in ways that predict response to ghrelin-receptor agonism (anamorelin) vs anti-IL-6/IL-6R vs anti-GDF-15 therapies?
- How do the CT-based subtypes map onto the multi-tissue metabolic signatures identified in [[papers/multi-omics-profiling-cachexia-targeted-tissues]] (one-carbon metabolism, IL-6/NNMT axis)?

## My take

This is the canonical 2025 human-evidence review of cancer cachexia — explicit foil to the mouse-model-dominated literature and a useful counterpart to the Morigny et al. multi-omics resource [[papers/multi-omics-profiling-cachexia-targeted-tissues]]. Two contributions stand out: (1) the explicit framing of CAC as a SPECTRUM of body-composition subtypes that may need bespoke therapies rather than a single condition; and (2) the careful debunking of WAT-browning-as-human-CAC-driver — large-cohort BAT evidence contradicts the Petruzzelli paradigm. For the thesis, this paper anchors the "human-evidence" pillar that complements [[papers/multi-omics-profiling-cachexia-targeted-tissues]] (multi-tissue molecular mechanism) and provides the CT-L3 phenotyping vocabulary needed to map molecular subtypes onto clinical phenotypes. It should be revisited when looking at CAC-trial outcome design (FAACT vs HGS vs PET-ML) and when considering whether candidate interventions can address anabolic resistance (the most therapeutically actionable insight here).

## Related

- [[papers/multi-omics-profiling-cachexia-targeted-tissues]] — Morigny et al. 2026 *Nat Metab* — companion multi-omics mechanistic resource defining one-carbon metabolism as the tissue-overarching CAC pathway and IL-6/NNMT as a central driver. This review provides the human clinical-phenotyping and mechanistic context that Morigny et al.'s mouse-centric multi-omics complements.
- [[foundations/cancer-cachexia]] — foundational concept page anchoring this paper.
- [[foundations/sarcopenia-clinical-syndrome]] — clinical readout overlapping with CAC.
