---
# === Identification ===
title: "A single-cell and spatial genomics atlas of human skin fibroblasts reveals shared disease-related fibroblast subtypes across tissues"
slug: single-cell-spatial-genomics-atlas-human
arxiv: ""
doi: "10.1038/s41590-025-02267-8"
pmid: "40993240"
venue: "Nature Immunology"
year: 2025
authors:
  - Lloyd Steele
  - Bayanne Olabi
  - Kenny Roberts
  - Pavel Mazin
  - Simon Koplev
  - Catherine Tudor
  - Benjamin Rumney
  - Chloe Admane
  - Treasa Jiang
  - Donovan Correa-Gallegos
  - Krishnaa Chakala
  - Aljes Binkevich
  - Nusayhah Gopee
  - Alexander V. Predeus
  - Martin Prete
  - Elena Winheim
  - Karl Annusver
  - Andreas Forsthuber
  - Laura Francis
  - Stephan Frech
  - Clarisse Gânier
  - Thomas Layton
  - Yingzi Liu
  - Hao Yuan
  - Johann Gudjonsson
  - Beate Lichtenberger
  - Satveer Mahil
  - Jagdeep Nanchahal
  - Edel A. O'Toole
  - Maksim Plikus
  - Yuval Rinkevich
  - Emanuel Rognoni
  - Catherine H. Smith
  - Sarah A. Teichmann
  - Maria Kasper
  - Alasdair Foster
  - Mohammad Lotfollahi
  - Muzlifah Haniffa
first_author: "Lloyd Steele"
corresponding_author: "Muzlifah Haniffa"

# === Source & metadata ===
source_type: pdf
s2_id: "404d455f568f49f71870861ef06d8b1da455cc58"
date_added: 2026-05-28
ingested_date: 2026-05-28
ingest_version: 1
last_reviewed:

# === Classification ===
importance: 4
tier: TIER_1
tags: [skin, fibroblast, myofibroblast, FRC, spatial-transcriptomics, single-cell, atlas, scarring, fibrosis, cross-tissue, immune-niche]
keywords: [skin fibroblast, FRC-like fibroblast, inflammatory myofibroblast, scarring risk, scPoli, cross-tissue fibroblast, lymphoid tissue organizer]
domain: immunology

# === Biomedical domain ===
tissue: [skin, multi]
condition: [healthy, cancer, autoimmune]
disease_specific: [hidradenitis_suppurativa, atopic_dermatitis, systemic_sclerosis, keloid_scar, melanoma, dupuytren_contracture, IBD]
species: [human, mouse]
hypoxia_relevant: true
contains_immune_cells: true
contains_myeloid: true

# === Technique ===
techniques: [scRNA-seq_10x, spatial_visium, spatial_xenium, immunofluorescence]
n_samples: 251
n_cells_total: 2100000
integration_method: scVI

# === Biology captured ===
key_cell_types: [superficial-fibroblast, universal-fibroblast, perivascular-fibroblast, FRC-like-fibroblast, hair-follicle-fibroblast, Schwann-like-fibroblast, inflammatory-myofibroblast, myofibroblast, fascia-like-myofibroblast, neutrophil, monocyte, macrophage, B-cell, T-cell, dendritic-cell]
key_markers: [CCL19, CD74, HLA-DRA, IL33, IL15, PI16, CD34, MFAP5, IL11, MMP1, CXCL8, IL7R, ACTA2, CTHRC1, POSTN, LRRC15, SFRP4, CRABP1, CXCL9, ADAMDEC1, SCN7A, NGFR]
key_pathways: [JAK-STAT, hypoxia, TGFb, Wnt, mechanotransduction]

# === User project membership ===
projects: [skin, thesis]
priority: context
read_status: read

# === HypoxiaVERSE-specific ===
hypoxiaverse_status:
exclusion_reason:
data_availability: "https://cellatlas.io/studies/skin-fibroblast"

# === Cross-references ===
code_url: ""
cited_by: [single-cell-spatial-transcriptomic-analysis-human]
---

## Problem

Fibroblasts shape tissue architecture and immune-cell niches, but their heterogeneity has been hard to classify: they lack unique surface markers and adopt activated phenotypes in culture. Prior skin studies used inconsistent nomenclatures, rarely resolved fibroblasts spatially, and seldom spanned diverse diseases or compared across human tissues. How skin fibroblast composition changes across inflammatory, cancer, and fibrotic disease — and how it relates to other tissues — was unclear.

## Key idea

Build a spatially resolved, disease-aware human skin fibroblast atlas by integrating large-scale scRNA-seq (2.1M cells, 32 datasets, 251 donors) with spatial transcriptomics, then use reference mapping (scPoli) to discover disease-associated states, trajectory analysis to infer myofibroblast origins, and ~5.8M-cell cross-tissue integration to test conservation. The result is a harmonized F1–F8 fibroblast taxonomy in which two immune-related subtypes — F3 FRC-like and F6 inflammatory myofibroblast — are conserved across tissues and organize immune niches.

## Method

- scVI integration of 357,276 high-quality fibroblasts from healthy/nonlesional skin; six major subtypes defined by DE + pathway enrichment.
- Spatial validation with 10x Visium (cell2location deconvolution) and 10x Xenium (5000-plex, single-cell resolution); H&E microenvironment annotation.
- scPoli semi-supervised reference mapping of 190,756 diseased fibroblasts; uncertain cells re-clustered into disease-adapted/disease-specific states.
- Scarring-risk analysis across 23 diseases; random-forest classifier; LRRC15 immunofluorescence validation; PROGENy pathway scoring.
- Trajectory inference (PAGA, scVelo RNA velocity, CellRank2) plus a temporal human wound dataset (58,823 cells).
- Cross-tissue integration of ~5.8M cells (skin, lung, intestine, synovium, endometrium, heart, nasal mucosa); CellChat-style receptor-ligand and NicheCompass niche analysis.
- Developmental analysis integrating adult, prenatal skin, and intestinal fibroblasts; mouse cross-tissue comparison.

## Results

Six healthy skin fibroblast subtypes (F1–F5, with F4/F5 subclusters) occupy distinct microanatomical niches. Disease adds two disease-adapted (F1-like regenerative, F3-like activated FRC) and three disease-specific myofibroblast states (F6, F7, F8). Fibroblast composition distinguishes scarring-risk categories, with F6 inflammatory myofibroblasts uniquely marking scarring risk and acting as a predicted intermediate toward terminal F7 myofibroblasts (supported by a wound time-course). F3 FRC-like and F6 are conserved across human tissues, organizing immune niches: F3 maintains a superficial perivascular immune niche (T–DC interactions), and F6 recruits neutrophils, monocytes and B cells. Adult F3 FRC-like fibroblasts may originate from a prenatal LTo gene program and are enriched in human (vs mouse) skin.

## All claims (exhaustive)

- `[c1]` Healthy human skin contains six major fibroblast subtypes (F1–F5, F4/F5 with subclusters) (p.1808) "In healthy skin, we identified six major fibroblast subtypes based on differential gene expression … and pathway enrichment analysis" — confidence: high — type: methodological — links: [[concepts/harmonized-skin-fibroblast-subtype-atlas-f1]] [[claims/six-major-healthy-skin-fibroblast-subtypes]]
- `[c2]` Atlas integrates 357,276 fibroblasts from 2.1M skin cells, 32 datasets, 251 donors (p.1807) "We re-processed and integrated 2.1 million cells from scRNA-seq data of adult human skin, comprising 32 datasets and 251 donors … 357,276 high-quality fibroblasts were selected" — confidence: high — type: quantitative — links: [[foundations/scvi-deep-generative-model]] [[claims/skin-fibroblast-atlas-integrates-357000-fibroblasts]]
- `[c3]` F1 superficial and F2 universal fibroblasts are uniformly present at different dermal depths (p.1808) "Two of the six fibroblast populations (F1: superficial (papillary) and F2: universal (reticular)) were uniformly present throughout skin at different tissue depths" — confidence: high — type: correlational — links: [[foundations/pi16-peptidase-inhibitor-16]] [[claims/f1-superficial-f2-universal-fibroblasts-uniform]]
- `[c4]` F3 FRC-like fibroblasts localize to the superficial perivascular region near immune cells (p.1808) "F3: fibroblastic reticular cell (FRC)-like fibroblasts were located predominantly in the superficial perivascular region in proximity to immune cells" — confidence: high — type: correlational — links: [[concepts/frc-like-fibroblast-ccl19-immunomodulatory-niche]] [[concepts/perivascular-immune-stromal-niche-skin-salt]] [[claims/f3-frc-like-fibroblasts-localize-superficial]]
- `[c5]` F3 FRC-like fibroblasts transcriptomically resemble lymphoid FRCs (CCL19/CD74/MHC-II/IL33/IL15) (p.1808) "F3: FRC-like fibroblasts transcriptomically resembled FRCs … expressing genes that attract and compartmentalize immune cells (CCL19, CXCL12, CH25H) … and enable antigen presentation (CD74 and MHC-II molecules)" — confidence: high — type: mechanistic — links: [[concepts/frc-like-fibroblast-ccl19-immunomodulatory-niche]] [[foundations/cd74-invariant-chain]] [[foundations/ccl19-chemokine]] [[claims/f3-frc-like-fibroblasts-transcriptomically-resemble]]
- `[c6]` KLF5 TF activity marks F2 universal fibroblasts, consistent with driving the universal PI16+ state (p.1808) "Transcription factor activity inference identified KLF5 in F2: universal fibroblasts … reported to drive the universal Pi16+ state" — confidence: medium — type: mechanistic — links: [[foundations/pi16-peptidase-inhibitor-16]] [[claims/klf5-transcription-factor-activity-marks-f2]]
- `[c7]` F5 Schwann-like fibroblasts are a nerve-associated population (p.1808) "F5: NGFR+ colocalized with Schwann cells, suggesting that they are a nerve-associated population" — confidence: medium — type: correlational — links: [[concepts/harmonized-skin-fibroblast-subtype-atlas-f1]] [[claims/f5-schwann-like-fibroblasts-nerve-associated]]
- `[c8]` scPoli mapped 121,167/190,756 diseased fibroblasts to F1–F5; 69,589 uncertain cells revealed novel states (p.1809) "Out of 190,756 fibroblasts from diseased states, 121,167 diseased cells were confidently assigned existing F1–F5 cell labels … remaining 69,589 fibroblasts … classified as uncertain" — confidence: high — type: methodological — links: [[foundations/scpoli-prototype-reference-mapping]] [[claims/scpoli-reference-mapping-classifies-diseased-fibroblasts]]
- `[c9]` Three disease-specific myofibroblast subtypes (F6, F7, F8) lack a healthy counterpart (p.1809) "'Disease-specific' fibroblasts (F6: inflammatory myofibroblasts, F7: myofibroblasts and F8: fascia-like myofibroblasts) did not have a healthy skin fibroblast counterpart and highly expressed a myofibroblast gene signature" — confidence: high — type: correlational — links: [[concepts/harmonized-skin-fibroblast-subtype-atlas-f1]] [[foundations/lrrc15-leucine-rich-repeat-containing-15]] [[claims/three-disease-specific-myofibroblast-subtypes-f6]]
- `[c10]` F6 inflammatory myofibroblasts co-express an immune program (IL11/IL24, CXCL5/8/13, MMP1) with elevated JAK-STAT and hypoxic signaling (p.1809) "F6: inflammatory myofibroblasts additionally expressed immune-related genes such as interleukins (IL11 and IL24), chemokines (CXCL5, CXCL8, CXCL13 and CCL11) and matrix metalloproteinases … (MMP1). JAK–STAT and hypoxic signaling genes were also elevated" — confidence: high — type: mechanistic — links: [[concepts/inflammatory-myofibroblast-il11-mmp1-intermediate-state]] [[foundations/il11-interleukin-11]] [[foundations/progeny-pathway-activity-inference]] [[claims/f6-inflammatory-myofibroblast-expresses-immune-gene]]
- `[c11]` Fibroblast composition distinguishes clinical scarring-risk categories (p.1810) "We identified distinct fibroblast compositions for each scarring risk category" — confidence: high — type: correlational — links: [[concepts/fibroblast-compositional-signature-scarring-risk]] [[claims/fibroblast-composition-distinguishes-clinical-scarring-risk]]
- `[c12]` F6 inflammatory myofibroblasts are uniquely enriched in scarring-risk disease but sparse in established fibrosis (p.1810) "Diseases with scarring risk were characterized by a uniquely high prevalence of F6: inflammatory myofibroblasts, which was not observed in low scarring risk or established fibrosis" — confidence: high — type: correlational — links: [[concepts/fibroblast-compositional-signature-scarring-risk]] [[concepts/inflammatory-myofibroblast-il11-mmp1-intermediate-state]] [[claims/f6-inflammatory-myofibroblasts-enriched-scarring-risk]]
- `[c13]` A random-forest classifier ranks F6 and F7 as the most important subtypes for predicting scarring risk (p.1810) "we trained a random forest classifier and identified that F6: inflammatory myofibroblasts and F7: myofibroblasts were the most important fibroblast subtypes for predicting scarring risk category" — confidence: high — type: methodological — links: [[concepts/fibroblast-compositional-signature-scarring-risk]] [[claims/random-forest-ranks-f6-f7-myofibroblasts]]
- `[c14]` LRRC15 protein marks myofibroblasts in inflamed scarring-risk skin but not low-risk skin (p.1810) "LRRC15 was evident in inflammation with scarring risk (inflamed hidradenitis suppurativa skin) but not in noninflamed skin or inflamed skin without scarring risk (atopic dermatitis skin)" — confidence: high — type: correlational — links: [[foundations/lrrc15-leucine-rich-repeat-containing-15]] [[claims/lrrc15-protein-validates-myofibroblasts-inflamed-scarring]]
- `[c15]` F7 terminal myofibroblasts arise via two trajectories (F2 direct; F1→F6→F7) (p.1813) "One trajectory arose directly from the F2: universal lineage. A second trajectory originated from F1: superficial fibroblasts, transitioning to F7: myofibroblasts via an intermediate F6: inflammatory myofibroblast state" — confidence: medium — type: mechanistic — links: [[concepts/myofibroblast-differentiation-trajectory-skin]] [[foundations/cellrank-fate-mapping]] [[foundations/scvelo-rna-velocity]] [[claims/f7-terminal-myofibroblasts-arise-two-differentiation]]
- `[c16]` In time-resolved human wounds, F6 predominates by day 7 and F7 by day 30 (p.1813) "By day 7, F6: inflammatory myofibroblasts were the predominant population. By day 30, F7: myofibroblasts had become the predominant population" — confidence: high — type: quantitative — links: [[concepts/myofibroblast-differentiation-trajectory-skin]] [[claims/human-skin-wound-time-course-f6]]
- `[c17]` F2 universal, F3 FRC-like, F6 and F7 fibroblast subtypes are conserved across human tissues (p.1814) "reported cross-tissue populations from previous studies are likely present in human skin, consistent with F2: universal, F3: FRC-like, F6: inflammatory myofibroblast, and F7: myofibroblast subtypes" — confidence: medium — type: correlational — links: [[concepts/cross-tissue-conserved-fibroblast-states]] [[claims/fibroblast-subtypes-conserved-across-multiple-human]]
- `[c18]` F6 inflammatory myofibroblasts are predicted to recruit neutrophils, monocytes/macrophages and B cells via chemokine-receptor axes (p.1816) "Receptor–ligand analysis suggested that F6: inflammatory myofibroblasts recruit and maintain neutrophils (CXCL5/6/8-CXCR2 and CSF3-CSF3R), macrophages/monocytes (CCL5/26-CCR1 and CSF3-CSF3R) and B cells (CXCL13/CXCR5)" — confidence: medium — type: mechanistic — links: [[concepts/inflammatory-myofibroblast-il11-mmp1-intermediate-state]] [[foundations/cellchat-cell-cell-communication]] [[foundations/cxcl8-il8]] [[claims/f6-inflammatory-myofibroblasts-predicted-recruit-neutrophils]]
- `[c19]` F6 inflammatory myofibroblasts are elevated in inflamed IBD tissue and correlate with clinical inflammation severity (p.1816) "F6: inflammatory myofibroblasts were significantly elevated in inflamed tissue, compared to non-inflamed tissue, and their prevalence correlated with clinical inflammation severity scores" — confidence: medium — type: correlational — links: [[concepts/cross-tissue-conserved-fibroblast-states]] [[claims/f6-inflammatory-myofibroblasts-elevated-inflamed-ibd]]
- `[c20]` Adult skin F3 FRC-like fibroblasts may arise from a prenatal LTo program (prenatal skin CCL19+ ≈ intestinal mLTo) (p.1817) "prenatal skin CCL19+ cells and prenatal intestinal mesenchymal LTo cells clustered together … suggesting that prenatal skin CCL19+ cells may give rise to adult skin F3: FRC-like cells in a manner analogous to intestinal LTo cells" — confidence: medium — type: mechanistic — links: [[concepts/frc-like-fibroblast-prenatal-lymphoid-tissue]] [[claims/adult-skin-f3-frc-like-fibroblasts]]
- `[c21]` F3 FRC-like fibroblasts are enriched in human skin but rare/absent in mouse skin (p.1817) "F3: FRC-like fibroblasts were relatively abundant in healthy human skin, the equivalent Ccl19+ fibroblasts were notably rarer in healthy mouse skin … we suggest F3: FRC-like fibroblasts are enriched in human skin and not observed or absent in murine skin" — confidence: medium — type: correlational — links: [[concepts/frc-like-fibroblast-ccl19-immunomodulatory-niche]] [[claims/f3-frc-like-fibroblasts-enriched-human]]

## Discussion captured

### Authors' interpretation

The authors interpret F3 FRC-like fibroblasts as functional analogues of lymphoid T-zone reticular FRCs, located in the superficial perivascular niche and mediating T–DC interactions. They interpret F6 inflammatory myofibroblasts (IL11+MMP1+CXCL8+IL7R+) as an intermediate myofibroblast state observed in early wounds, scarring-risk inflammation and cancer that recruits immune cells (notably neutrophils and monocytes). They argue these two states organize immune niches that drive pathology across multiple tissues.

### Comparisons with prior literature (made by authors)

- Inflammatory myofibroblasts: compared to Gao et al. 2024 (large CAF integration) and IBD reports (refs 78, 80, 81); F6 ≈ iCAF.
- F3 FRC-like: compared to Buechler et al. 2021 (Nature, universal/cross-tissue fibroblasts) and Korsunsky et al. 2022; equivalence to intestinal T-reticular cells (ref 78).
- Universal PI16+ fibroblast and KLF5 driver (refs 4, 50, 52).
- Trajectory consistency with mouse lineage tracing (refs 53, 55, 74).
- F3 enrichment in human vs mouse skin and TLS in hidradenitis suppurativa (refs 83–86).

### Mechanistic hypotheses proposed

- F6 inflammatory myofibroblast is an intermediate differentiation state toward terminal F7 myofibroblasts ("our results point toward F6: inflammatory myofibroblasts as an intermediate differentiation state toward F7: myofibroblasts in human skin", p.1813).
- Adult skin F3 FRC-like fibroblasts arise from a prenatal LTo program analogous to intestinal FRC ontogeny (p.1817).
- F3 FRC-like fibroblasts maintain the superficial perivascular immune niche and mediate T–DC interactions (p.1817–1818).

### Caveats and self-criticism

- "A limitation of our study is that we relied on the uncertainty mechanism incorporated in scPoli to identify disease-associated populations."
- "Our cross-tissue analysis using semi-supervised integration may underestimate tissue-specific differences."
- Trajectory inference methods are limited for predicting multiple cell states converging to a final phenotype, and lineage plasticity is likely.

### Future directions suggested

- Further work validating myofibroblast trajectories in human skin; skin proposed as an accessible exemplar tissue to study human myofibroblast development in vivo via temporal sampling.

## Limitations

- Disease-associated populations depend on scPoli's uncertainty heuristic.
- Spatial/trajectory/receptor-ligand findings are predictive (inference), not functionally validated.
- Semi-supervised cross-tissue integration may underestimate tissue-specific differences; gene panels and cell numbers vary widely across datasets.
- Clinical scarring categories are assigned, and many associations are correlative on snapshot data.

## Open questions

### Open questions raised by authors

- Are F6 inflammatory myofibroblasts obligatory intermediates toward F7, and what controls the transition?
- Do re-activated LTo programs drive tertiary lymphoid structures in human skin disease (e.g. hidradenitis suppurativa)?
- Why is the FRC-like fibroblast uniquely enriched in human skin relative to mouse?

### Open questions identified during ingest

- Could targeting F6 chemokine output (CXCR2/CCR1 axes) modulate scarring or pathological immune infiltration?
- Is the hypoxic-signaling signature in F6 a driver of the inflammatory-myofibroblast state, linking this work to hypoxia-focused stromal biology?

## My take

This is a reference-grade resource: a niche-anchored, disease-spanning fibroblast dictionary whose real punch is the cross-tissue conservation of two immune-interacting fibroblasts (F3 FRC-like, F6 inflammatory myofibroblast). The F6-as-intermediate story is well triangulated (composition + trajectory + wound time-course) even though it stops short of lineage tracing. For skin-stroma and immune-niche work it will be a primary anchor; the hypoxic-signaling angle in F6 is a small but real hook for hypoxia-stroma questions.

## Related

- [[concepts/harmonized-skin-fibroblast-subtype-atlas-f1]]
- [[concepts/frc-like-fibroblast-ccl19-immunomodulatory-niche]]
- [[concepts/inflammatory-myofibroblast-il11-mmp1-intermediate-state]]
- [[concepts/myofibroblast-differentiation-trajectory-skin]]
- [[concepts/cross-tissue-conserved-fibroblast-states]]
- [[concepts/fibroblast-compositional-signature-scarring-risk]]
- [[concepts/frc-like-fibroblast-prenatal-lymphoid-tissue]]
- [[people/lloyd-steele]]
- [[people/muzlifah-haniffa]]
- [[people/sarah-teichmann]]
- [[papers/single-cell-spatial-transcriptomic-analysis-human]] — same problem (human skin spatial fibroblast atlas)
