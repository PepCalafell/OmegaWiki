---
title: "Tumour and microenvironment crosstalk in NSCLC progression and response to therapy"
slug: tumour-microenvironment-crosstalk-nsclc-progression-response
arxiv: ""
doi: "10.1038/s41571-025-01021-1"
pmid: "40379986"
venue: "Nature Reviews Clinical Oncology"
year: 2025
authors:
  - Zahraa Rahal
  - Roy El Darzi
  - Seyed Javad Moghaddam
  - Tina Cascone
  - Humam Kadara
first_author: "Zahraa Rahal"
corresponding_author: "Humam Kadara"

source_type: pdf
s2_id: "fa127b0f5770090a8adbb0a8f57e9544abf86e78"
date_added: 2026-05-22
ingested_date: 2026-05-22
ingest_version: 1
last_reviewed:

importance: 4
tier: TIER_1
tags:
  - nsclc
  - tumour-microenvironment
  - immunotherapy
  - spatial-niches
  - tls
  - cafs
  - tams
  - hypoxia
  - sex-differences
  - ageing
  - obesity
  - microbiome
  - health-disparities
  - review
keywords:
  - non-small-cell lung cancer
  - tumour microenvironment
  - immune checkpoint inhibitors
  - spatial transcriptomics
  - tertiary lymphoid structures
  - cancer-associated fibroblasts
  - tumour-associated macrophages
  - CXCL9
  - SPP1
  - TREM2
  - hypoxia
  - tobacco smoke
  - aryl hydrocarbon receptor
domain: oncology

tissue:
  - lung
condition:
  - cancer
disease_specific:
  - nsclc
  - luad
  - lung-squamous-cell-carcinoma
species:
  - human
  - mouse
hypoxia_relevant: true
contains_immune_cells: true
contains_myeloid: true

techniques:
  - spatial_transcriptomics
  - scRNA-seq_10x
  - multiplex_imaging
  - bulk_RNA-seq
  - immunohistochemistry
n_samples:
n_cells_total:
integration_method: ""

key_cell_types:
  - CD8_T_effector
  - CD8_T_exhausted
  - Treg
  - TH1
  - TH2
  - TH17
  - B_cell
  - plasma_cell
  - TAM_CXCL9
  - TAM_SPP1
  - TAM_TREM2
  - TAM_COL1A1
  - cDC1
  - cDC2
  - plasmacytoid_DC
  - NK_cell
  - MDSC
  - TAN
  - myofibroblastic_CAF
  - hypoxic_CAF
  - inflammatory_CAF
  - desmoplastic_CAF
  - pericyte
  - endothelial_cell
key_markers:
  - PD-L1
  - PD-1
  - CTLA4
  - CXCL9
  - CXCL10
  - CXCL11
  - CXCL13
  - SPP1
  - TREM2
  - COL1A1
  - COL11A1
  - GREM1
  - TCF7
  - HAVCR2
  - LAMP3
  - CCR7
  - NOTCH3
  - HIF1A
  - TGFB1
  - SMAD3
  - STAT3
  - NF-kB
  - IL-6
  - IL-1A
  - IL-4
  - VEGF
  - IDO1
  - CD55
  - CD59
  - C5a
  - KRAS
  - EGFR
  - AHR
key_pathways:
  - PD-1/PD-L1 axis
  - CTLA4 checkpoint
  - CXCR3 chemokine signalling
  - TGFβ-Smad3
  - HIF1α hypoxia signalling
  - NOTCH3 stromal signalling
  - AHR-mTOR
  - IL-4-STAT6 myelopoiesis
  - complement (CD55/CD59/C5a)
  - JAK-STAT
  - NF-κB inflammation

projects:
  - thesis
  - hypoxia
priority: core
read_status: read

hypoxiaverse_status:
exclusion_reason:
data_availability: ""

code_url: ""
cited_by: []
---

## Problem

Non-small-cell lung cancer (NSCLC) remains the leading cause of cancer mortality despite immune checkpoint inhibitors (ICIs) and targeted therapies; the majority of patients fail to achieve durable benefit. Why responses differ so widely is not fully understood, but the tumour microenvironment (TME) — its spatial heterogeneity, stromal/immune crosstalk, and modulation by patient-level factors (smoking, sex, age, obesity, microbiome, ancestry, socioeconomic status) — is now recognized as a primary determinant of progression, metastasis, and therapy response.

## Key idea

The NSCLC TME is best understood as a spatially organised ecosystem of "immune-rich" and "immune-poor" niches whose composition, crosstalk, and patient-specific modifiers jointly explain resistance and inform combination strategies. The Review argues for moving beyond a tumour-centric, binary "hot vs cold" view toward a holistic, topographical model that integrates spatial transcriptomics, niche-level signalling (CXCL9–SPP1, COL11A1–SPP1, NOTCH3, CXCL13–CXCR5, TGFβ–Smad3, AHR–mTOR), and patient-level determinants to guide therapeutic sequencing and biomarker development.

## Method

Narrative review. The authors synthesise NSCLC TME literature with emphasis on:
- Recent spatial transcriptomic and high-resolution imaging studies of NSCLC biopsies (pretreatment and post-treatment, including chemo–ICI combinations).
- scRNA-seq atlases of NSCLC immune and stromal compartments.
- Mouse models (KP LUAD, urothelial carcinoma, melanoma, breast cancer) for mechanistic claims.
- Clinical trial data and meta-analyses for sex, age, and obesity effects on ICI efficacy.
- Microbiome and metabolomic studies linking systemic factors to TME composition.

## Results

- Immune-rich niches are defined by dense T/B-cell, NK, DC, CXCL9⁺ TAM infiltrates and TLS formation; their presence correlates with ICI response.
- Immune-poor niches are characterised by dense ECM (myofibroblastic and desmoplastic CAFs), hypoxia, MDSC/TAN/Treg dominance, and COL11A1⁺GREM1⁺ CAFs paired with SPP1⁺ TAMs adjacent to cancer cells, predicting poor ICI outcomes.
- A pretreatment "stem-immunity hub" enriched for TCF7⁺PD1⁺CD8⁺ T cells, CCR7⁺LAMP3⁺ DCs, CCL19⁺ CAFs, and CXCL10⁺ TAMs predicts response to PD-(L)1 blockade.
- Macrophage phenotype dichotomy: CXCL9⁺ TAMs support antitumour immunity, while SPP1⁺, COL1A1⁺ and TREM2⁺ TAMs (latter enriched in hypoxic/lipid-rich niches) promote immune exclusion and exhaustion; the CXCL9:SPP1 ratio is a candidate ICI biomarker.
- Late, T-cell-exhaustion-marked TLS correlate with complete response to chemo–ICI combinations; hypoxia impairs TLS maturation in non-responders.
- Sex effects: androgen signalling drives male CD8⁺ exhaustion and reduced ICI efficacy; oestrogen polarizes TAMs immunosuppressively (rescuable by fulvestrant); KRAS-mutant LUAD shows sex-dimorphic response to STAT3 loss (IL-6/CXCL1 in males, oestrogen-mediated in females).
- Ageing produces a PD-L2/TIM3-high, TAM-enriched, IL-1α-driven immunosuppressive TME with naïve-like CD8 phenotypes and reduced ICI benefit; methylmalonic acid drives TGFβ/SOX4-mediated EMT and metastasis.
- Obesity paradox: leptin/IL-6-driven T-cell exhaustion paradoxically sensitises tumours to PD-1 blockade; metformin synergises with ICIs by reducing Treg activity.
- Microbiota: Akkermansia / Ruminococcus / Bifidobacterium enhance ICI response; Alistipes promotes immunosuppression.
- Health disparities: Black patients more often present with immunologically cold TMEs; KRAS G12C and EGFR mutation prevalence differs by ancestry, affecting both TME composition and treatment selection.
- Complement axis: CD55/CD59 upregulation blunts CD8 cytotoxicity; combining anti-CD55/CD59 with anti-PD-1 was synergistic in mouse lung cancer.
- IL-4–dependent bone-marrow myelopoiesis fuels immunosuppression; dupilumab plus anti-PD-(L)1 (n=6 first-in-human) reduced circulating immunosuppressive monocytes and increased CD8 infiltration.

## All claims (exhaustive)

- `[c1]` NSCLC TME is organised into immune-rich and immune-poor spatial niches that jointly determine therapy response (p.464–466) "Conceptually, the NSCLC TME can be classified into two principal types of spatial niches defined by immune cell density and activity: immune rich and immune poor." — confidence: high — type: mechanistic — links: [[concepts/immune-rich-vs-immune-poor-niches-nsclc]] [[claims/nsclc-tme-spatial-dichotomy-immune-rich-poor]]
- `[c2]` A low CXCL9:SPP1 macrophage ratio predicts poor response to ICIs and worse prognosis across multiple solid tumours including NSCLC (p.467–468) "with a low CXCL9:SPP1 ratio linked with resistance to ICIs and poor prognosis across several solid tumour types including NSCLC." — confidence: high — type: correlational — links: [[concepts/cxcl9-spp1-tam-ratio-ici-biomarker]] [[concepts/ifng-mac-cxcl9-tam-ici-responder]] [[foundations/spp1-secreted-phosphoprotein-1]] [[claims/cxcl9-spp1-tam-ratio-ici-response-nsclc]]
- `[c3]` A COL11A1⁺GREM1⁺ CAF / SPP1⁺ TAM axis adjacent to cancer cells physically obstructs CTL infiltration, increasing tumour burden and worsening chemo–ICI outcomes (p.468–469) "Spatial transcriptomic analyses... revealed an enrichment in COL11A1+GREM1+ CAFs and SPP1+ TAMs adjacent to cancer cells, and their increased abundance correlated with a higher tumour burden and poor treatment outcomes. The COL11A1–SPP1 axis has been hypothesized to physically obstruct infiltration of CTLs." — confidence: high — type: mechanistic — links: [[concepts/col11a1-spp1-fibrotic-axis-cd8-exclusion-nsclc]] [[foundations/cancer-associated-fibroblast]] [[claims/col11a1-spp1-fibrotic-axis-cd8-exclusion-nsclc]]
- `[c4]` A pretreatment "stem-immunity hub" — TCF7⁺PD1⁺CD8⁺ T cells with CCR7⁺LAMP3⁺ DCs, CCL19⁺ CAFs and CXCL10⁺ TAMs — predicts ICI response in NSCLC (p.466) "researchers identified a distinct niche referred to as the stem-immunity hub, which is enriched in stem-like TCF7+PD1+CD8+ T cells, activated CCR7+LAMP3+ DCs, CCL19+ CAFs and CXCL10+ TAMs preferentially engaging TCF7−CD8+ T cells." — confidence: high — type: correlational — links: [[concepts/stem-immunity-hub-nsclc-ici-response]] [[claims/stem-immunity-hub-tcf7-pd1-nsclc]]
- `[c5]` Late-stage TLS marked by T-cell exhaustion genes (IFNG, HAVCR2) characterise complete responders to chemo–ICI, whereas activated TLS with germinal-centre signatures coexisting with hypoxia mark non-responders (p.466–467) "Complete responders to chemotherapy–ICI combinations frequently exhibited late TLS characterized by T cell exhaustion markers (such as IFNG or HAVCR2)... By contrast, nonresponders frequently had activated TLS with robust germinal centre signatures yet concomitant hypoxia, which can inhibit the maturation of these structures." — confidence: high — type: correlational — links: [[concepts/tertiary-lymphoid-structure]] [[concepts/tls-maturation-stage-nsclc-ici-response]] [[claims/tls-late-stage-better-ici-response-nsclc]]
- `[c6]` Anti-PD-1 + anti-CTLA4 + chemotherapy combinations activate CXCL13–CXCR5 chemokine signalling, facilitating lymphocyte recruitment and TLS maturation in NSCLC (p.468) "analysis of NSCLCs from patients who received combinations comprising of the anti-PD-1 nivolumab, the anti-CTLA4 antibody ipilimumab and standard-of-care chemotherapy revealed activation of chemokine signalling pathways, such as the CXCL13–CXCR5 axis, thereby facilitating lymphocyte recruitment and TLS maturation." — confidence: high — type: mechanistic — links: [[concepts/cxcl13-cxcr5-tls-recruitment]] [[foundations/cxcl13-chemokine]] [[claims/cxcl13-cxcr5-tls-maturation-nsclc]]
- `[c7]` TREM2⁺ TAMs, enriched in lipid-rich and hypoxic niches, suppress NK activity and expand exhausted CD8⁺ T cells, fostering immunologically cold NSCLC TMEs (p.468) "TREM2+ macrophages, more abundant in lipid-rich and hypoxic niches, sustain an immunosuppressive phenotype by curbing NK cell activity and expanding exhausted CD8+ T cell populations and fostering an immunologically cold TME." — confidence: high — type: mechanistic — links: [[foundations/trem2-receptor]] [[concepts/trem2-tumor-associated-macrophage]] [[claims/trem2-tam-nk-suppression-cd8-exhaustion-hypoxic-niche]]
- `[c8]` NOTCH3-dependent signalling between CAFs, pericytes and endothelial cells drives tumour invasion, collagen production and a TGFβ-related poor-prognosis signature in NSCLC (p.469–470) "Interactions between CAFs, pericytes and endothelial cells, driven by activation of NOTCH signalling (and particularly NOTCH3)... NOTCH3-dependent signalling promotes tumour invasion, collagen production and expression of a TGFβ-related signature associated with a poor prognosis in patients with NSCLC." — confidence: medium — type: mechanistic — links: [[concepts/notch3-stromal-tumour-invasion]] [[foundations/notch3-receptor]] [[claims/notch3-stromal-tumour-invasion-tgfb-nsclc]]
- `[c9]` Treg depletion in a mouse LUAD model reprograms fibroblast, endothelial and TAM transcriptional states and enhances VEGF signalling, increasing vascularization and immunomodulation (p.470) "In a mouse model of LUAD, depletion of Treg cells resulted in reprogramming of the TME, altering the expression profiles of fibroblasts, endothelial cells and TAMs, and enhancing VEGF signalling. This reprogramming led to increased vascularization and immunomodulation of innate and adaptive immune cells." — confidence: high — type: mechanistic — links: [[concepts/treg-tme-stromal-tam-reprogramming-vegf]] [[foundations/kp-nsclc-mouse-model]] [[foundations/vegf]] [[claims/luad-treg-depletion-tme-reprogramming-vegf]]
- `[c10]` Persistent tobacco smoking upregulates PD-L1 via aryl hydrocarbon receptor–mTOR signalling, reinforcing immune evasion in smoking-related NSCLC (p.470) "Persistent tobacco smoking drives inflammation, further upregulating PDL1 through activation of aryl hydrocarbon receptor–mTOR signalling, reinforcing immune evasion." — confidence: high — type: mechanistic — links: [[concepts/tobacco-smoke-ahr-mtor-pdl1-immune-evasion]] [[foundations/pd-l1-cd274]] [[claims/tobacco-ahr-mtor-pdl1-immune-evasion-nsclc]]
- `[c11]` EGFR-mutant LUAD, particularly in smokers, has a lower TMB, reduced immune infiltration, and fibroblast-enriched niches conferring resistance to both ICIs and EGFR TKIs (p.470) "In EGFR-mutant LUAD, tobacco smoking further modifies the TME, shifting it towards immune exclusion and stromal activation. Unlike other smoking-driven NSCLCs, these tumours have a lower TMB, reduced immune cell infiltration and abundance of fibroblast-enriched niches, leading to enhanced resistance to both ICIs and EGFR TKIs." — confidence: high — type: correlational — links: [[foundations/egfr-mutation-luad]] [[concepts/egfr-mutant-luad-immune-excluded-tme]] [[claims/egfr-mutant-luad-immune-excluded-stromal-rich-tme]]
- `[c12]` STAT3 knockout in a KRAS-mutant LUAD mouse model produces sex-dimorphic outcomes: enhanced antitumour immunity in females (oestrogen-dependent, reversed by tamoxifen) versus tumour-promoting NF-κB/CXCL1-driven neutrophil response and IL-6 induction in males (p.471–472) "Female mice had enhanced antitumour immune responses and a reduced tumour burden, whereas males showed increased tumour growth owing to a tumour-promoting immune phenotype characterized by activation of NF-κB signalling, a CXCL1-mediated neutrophil response and IL-6 induction." — confidence: high — type: mechanistic — links: [[foundations/stat3-tf]] [[foundations/nf-kb-p65-rela]] [[concepts/kras-stat3-sex-dimorphic-luad]] [[claims/kras-stat3-ko-sex-dimorphic-tumour-progression-il6-neutrophil]]
- `[c13]` In treatment-naïve NSCLC and mouse urothelial cancer, androgen signalling expands progenitor exhausted CD8⁺ T cells and reduces ICI efficacy in males relative to females (p.471) "androgen signalling was associated with an increased presence of progenitor exhausted CD8+ T cells, leading to inferior control over tumour growth in males compared with females... exhausted CD8+ tumour-infiltrating lymphocytes (TILs) were more prevalent in males, correlating with decreased efficacy of ICIs." — confidence: high — type: correlational — links: [[concepts/androgen-signaling-cd8-exhaustion-ici]] [[claims/androgen-cd8-exhaustion-male-ici-bias]]
- `[c14]` In a mouse melanoma model, oestrogen signalling polarizes TAMs to an immunosuppressive phenotype causing CD8⁺ T-cell exhaustion and ICI resistance, reversed by the selective oestrogen receptor degrader fulvestrant (p.471) "oestrogen signalling led to TAM polarization towards an immunosuppressive phenotype, leading to CD8+ T cell dysfunction and exhaustion. This phenotype was associated with resistance to ICIs, which could be overcome by combining ICIs with the selective oestrogen receptor degrader fulvestrant." — confidence: high — type: pharmacological — links: [[concepts/oestrogen-tam-immunosuppression]] [[foundations/fulvestrant-er-degrader]] [[claims/oestrogen-tam-immunosuppression-fulvestrant-resensitization]]
- `[c15]` LUAD biopsies from patients >70 years old show increased PD-L2, TIM3, immunosuppressive TAMs and fewer TANs, correlating with reduced T-cell function and lower overall survival in early-stage but not advanced disease (p.472) "LUAD biopsy samples from older patients show increased expression of immunosuppressive proteins, such as PD-L2 and TIM3, and higher levels of immunosuppressive TAMs and fewer TANs... This TME correlates with reduced T cell function and overall immunity, leading to decreased overall survival in older patients with early stage disease, but not in those with advanced-stage disease." — confidence: high — type: correlational — links: [[concepts/ageing-nsclc-tme-immunosuppression]] [[claims/ageing-nsclc-tme-immunosuppression-pdl2-tim3-il1a]]
- `[c16]` Elevated methylmalonic acid in aged NSCLC promotes EMT (↑fibronectin, ↑vimentin, ↓E-cadherin), activates TGFβ signalling and SOX4, and enhances metastatic potential (p.472–473) "In a mouse model of NSCLC, elevated levels of methylmalonic acid promoted cancer aggressiveness and metastatic potential by inducing the expression of epithelial-to-mesenchymal transition markers such as fibronectin and vimentin, and reducing that of E-cadherin. Methylmalonic acid also enhanced activation of TGFβ signalling and expression of SOX4, both associated with poor prognosis and tumour progression." — confidence: high — type: mechanistic — links: [[concepts/methylmalonic-acid-aged-emt-metastasis]] [[foundations/methylmalonic-acid]] [[foundations/tgfb1-cytokine]] [[claims/methylmalonic-acid-tgfb-sox4-emt-aged-nsclc-metastasis]]
- `[c17]` Obesity in NSCLC paradoxically improves PFS and OS under PD-1 blockade because leptin- and IL-6-driven T-cell exhaustion upregulates PD-1, creating dependency on the targeted axis (p.473) "Leptin signalling, which contributes to T cell exhaustion and increased PD-1 expression, seems to have a key role. Consequently, PD-1 blockade in patients with obesity has been shown to reverse T cell dysfunction, leading to improved PFS and overall survival compared with those without obesity." — confidence: high — type: correlational — links: [[concepts/obesity-paradox-tam-pd1-glycolysis]] [[concepts/obesity-leptin-pd1-ici-paradox-nsclc]] [[claims/obesity-ici-paradox-leptin-pd1-nsclc]]
- `[c18]` Metformin enhances ICI efficacy by reprogramming the TME — reducing Treg activity and improving Teff function — in preclinical models and patients with obesity (p.473) "metformin enhanced the efficacy of ICIs by reprogramming the immune TME, reducing activity of Treg cells and improving Teff cell function." — confidence: medium — type: pharmacological — links: [[foundations/metformin]] [[concepts/metformin-ici-synergy-treg-teff]] [[claims/metformin-treg-teff-ici-synergy]]
- `[c19]` Gut microbiota composition modulates ICI efficacy in NSCLC: Akkermansia, Ruminococcus and Bifidobacterium enhance antitumour immunity, while Alistipes-driven dysbiosis (via IL-6) promotes immunosuppression and resistance (p.473) "Imbalances in microbial populations and the presence of pro-inflammatory bacteria, such as members of the Alistipes genus, can foster immunosuppression... certain bacterial genera, such as Akkermansia, Ruminococcus and Bifidobacterium, have been associated with enhanced antitumour immunity and improved responses to anti-PD-(L)1 antibodies." — confidence: medium — type: correlational — links: [[concepts/gut-microbiota-ici-response-nsclc]] [[foundations/akkermansia-muciniphila]] [[claims/gut-microbiota-akkermansia-alistipes-ici-modulation]]
- `[c20]` Upregulation of complement regulators CD55 and CD59 in the TME suppresses CD8 cytotoxicity and enables immune evasion; combining anti-CD55/CD59 with anti-PD-1 was synergistic in a mouse lung cancer model (p.471) "Inactivation of the complement cascade within the TME, which is mediated by upregulation of complement regulatory proteins CD55 and CD59, decreases CD8+ T cell cytotoxicity and facilitates tumour immune evasion. In a mouse model of lung cancer, combining antibodies targeting CD55 or CD59 with those targeting PD-1 had a synergistic antitumour effect." — confidence: high — type: pharmacological — links: [[concepts/complement-cd55-cd59-tumour-evasion]] [[claims/cd55-cd59-complement-evasion-cd8-cytotoxicity-nsclc]]
- `[c21]` IL-4 signalling in bone-marrow myeloid progenitors generates immunosuppressive myeloid cells in NSCLC; first-in-human dupilumab (anti-IL-4Rα) plus anti-PD-(L)1 in 6 patients reduced circulating immunosuppressive monocytes and increased CD8⁺ infiltration (p.470–471) "Elevated activation of IL-4-dependent signalling in bone marrow myeloid progenitors leads to the generation of immunosuppressive myeloid cells, contributing to a poor prognosis in patients with NSCLC. In a first-in-human trial involving 6 patients with NSCLC, addition of the anti-IL-4Rα antibody dupilumab to anti-PD-(L)1 antibodies showed preliminary efficacy, and analysis of paired biopsy samples showed evidence of reduced circulating immunosuppressive monocytes and enhanced infiltration of CD8+ T cells." — confidence: medium — type: pharmacological — links: [[concepts/il4-myeloid-immunosuppression-nsclc]] [[foundations/dupilumab-anti-il4ra]] [[claims/il4-myeloid-immunosuppression-dupilumab-anti-pdl1-nsclc]]

## Discussion captured

### Authors' interpretation

The authors frame NSCLC progression and ICI resistance as fundamentally a spatial-architectural phenomenon: niche-level cellular composition and stromal geometry (ECM density, vascular abnormality, hypoxia gradients) — not merely tumour-cell-intrinsic biology — dictate whether immunity is permitted or excluded. They emphasize that "immune desertification" is an *active* exclusionary process driven by stromal configuration rather than passive absence. Patient-level modifiers (sex, age, obesity, microbiome, ancestry, smoking) are treated as systemic inputs that reshape the TME and must be integrated into precision-oncology decisions.

### Comparisons with prior literature (made by authors)

- Spatial-transcriptomics-defined CXCL9⁺/SPP1⁺ TAM dichotomy in NSCLC builds on pan-cancer TAM atlases and is connected to ICI biomarker work — see [[papers/pd-l1-expressing-tumor-associated-macrophages]] and [[papers/tissue-resident-macrophages-provide-pro-tumorigenic]].
- TLS biology in NSCLC echoes earlier work on TLS as ICI biomarkers in melanoma/sarcoma and B-cell–driven humoral immunity in solid tumours.
- Hypoxia-driven immune evasion claims are consistent with broader literature on hypoxia immunosuppression — see [[papers/hypoxia-driven-crosstalk-between-tumor-tumor]] and [[papers/hypoxic-microenvironment-cancer-molecular-mechanisms-therapeutic]].
- Obesity paradox and metformin–ICI synergy follow earlier preclinical and retrospective clinical observations.

### Mechanistic hypotheses proposed

- "The COL11A1–SPP1 axis has been hypothesized to physically obstruct infiltration of CTLs, thereby undermining effective antitumour immunity" (p.469).
- AHR–mTOR signalling as the mechanistic link between persistent smoking and immune-evasive PD-L1 upregulation (p.470).
- Functional iron insufficiency via NUPR1–LCN2 axis may suppress alveolar stem-cell renewal and explain reduced NSCLC incidence in >80-year-olds (p.472).
- Re-educating CAFs (rather than depleting them) as a strategy to overcome therapeutic resistance.

### Caveats and self-criticism

- Whether immune-desert niches are intrinsically irreversible or can be reprogrammed is "remains to be determined" (p.469).
- CAF heterogeneity makes selective targeting of protumorigenic subtypes without harming tumour-suppressive ones an unresolved challenge.
- Microbiome influences on TME are "highly context-dependent, varying across patients based on host immunity, tumour biology and broader microenvironmental factors."
- Ethnicity correlations with TME composition do not always translate to ICI outcome differences once performance status, BMI and PD-L1 are controlled.

### Future directions suggested

- Predictive spatial atlases that map architecture × niche composition × functional state for patient stratification.
- Combination of TME-remodelling agents (anti-TGFβ, anti-VEGF, anti-CAF antifibrotics like pirfenidone) with ICIs.
- Microbiome-targeted interventions (probiotics, FMT, prebiotics) as ICI adjuvants and non-invasive biomarkers.
- Sex- and age-stratified trial design; integration of androgen/oestrogen modulators with ICIs.
- Selective re-education of protumorigenic CAFs.

## Limitations

- Narrative review without systematic search criteria; weighting of evidence reflects author selection.
- Many mechanistic claims rely on mouse models (KP LUAD, urothelial, melanoma, breast) that may not fully recapitulate human NSCLC TME.
- Spatial-transcriptomics studies cited are typically small cohorts; reproducibility and platform-dependence (Visium, CosMx, MERFISH) not fully addressed.
- Clinical claims (e.g., dupilumab + anti-PD-(L)1) rest on very small first-in-human cohorts (n=6).
- Sex/age/ancestry stratifications often derived from retrospective subgroup analyses with confounders.

## Open questions

### Open questions raised by authors

- Are NSCLC immune-desert niches reprogrammable into immune-responsive ones, or are they irreversibly committed?
- Can protumorigenic CAF subtypes be selectively targeted while sparing tumour-suppressive CAFs?
- What mechanisms drive the paradoxical decrease in NSCLC incidence above age 80 (e.g., NUPR1–LCN2 / alveolar stem-cell senescence)?
- Are microbiome-based biomarkers (and FMT-style interventions) ready for prospective ICI trials in NSCLC?
- How should treatment sequencing (neoadjuvant ICI → surgery → adjuvant) be optimized given TME-remodelling effects of each modality?

### Open questions identified during ingest

- Could combining anti-CD55/CD59 with anti-PD-1 (mouse synergy) translate to NSCLC patients, and which TME archetype would benefit?
- Is the CXCL9:SPP1 ratio sufficient as a standalone biomarker, or must it be combined with spatial context (e.g., distance-to-tumour-nest) to predict ICI response robustly?
- How does the AHR–mTOR–PD-L1 axis intersect with [[concepts/ahr-tam-immunosuppression-tumour]] and AHR-targeted therapy strategies elsewhere in the wiki?
- Does the obesity paradox extend to anti-TIGIT or LAG3 combination regimens, or is it PD-1-axis-specific?

## My take

This is the most up-to-date, integrative reference on NSCLC TME for the thesis: it unifies spatial transcriptomic claims, CAF/TAM/Treg heterogeneity, and patient-level modifiers in a way that maps cleanly to hypoxia + immunosuppression themes already developed in this wiki. The CXCL9–SPP1 axis, COL11A1–SPP1 stromal axis, and TREM2⁺ TAM hypoxic-niche claims are particularly important — they extend the macrophage-state framework from pan-cancer atlases (e.g. [[papers/pd-l1-expressing-tumor-associated-macrophages]], [[papers/tissue-resident-macrophages-provide-pro-tumorigenic]]) into a lung-specific, spatially resolved context. The AHR–mTOR–PD-L1 link in smokers is a new mechanistic bridge between the wiki's existing AHR work and immune evasion. Caveat: the strongest mechanistic claims rest on mouse models, and clinical translation of patient-level modifiers (sex/age/obesity/microbiome) remains stratified by retrospective evidence.

## Related

- [[concepts/tertiary-lymphoid-structure]]
- [[foundations/cancer-associated-fibroblast]]
- [[concepts/hypoxia-immune-evasion-clonal-selection]]
- [[concepts/obesity-paradox-tam-pd1-glycolysis]]
- [[concepts/ecm-mac-collagen-producing-tam]]
- [[concepts/pan-cancer-tam-atlas-23-clusters]]
- [[concepts/ifng-mac-cxcl9-tam-ici-responder]]
- [[concepts/ahr-tam-immunosuppression-tumour]]
- [[foundations/pd-l1-cd274]]
- [[foundations/trem2-receptor]]
- [[foundations/hif1a]]
- [[foundations/stat3-tf]]
- [[foundations/nf-kb-p65-rela]]
- [[foundations/tgfb1-cytokine]]
- [[foundations/vegf]]
- [[foundations/metformin]]
- [[foundations/kp-nsclc-mouse-model]]
- [[papers/hypoxia-driven-crosstalk-between-tumor-tumor]]
- [[papers/hypoxic-microenvironment-cancer-molecular-mechanisms-therapeutic]]
- [[papers/pd-l1-expressing-tumor-associated-macrophages]]
- [[papers/tissue-resident-macrophages-provide-pro-tumorigenic]]
- [[papers/tumor-induced-metabolic-immunosuppression-mechanisms-therapeutic]]
- [[papers/molecular-landmarks-tumor-hypoxia-across-cancer]]
- [[papers/cellcharter-reveals-spatial-cell-niches-associated]]
