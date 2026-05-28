---
title: "A pairwise cytokine code explains the organism-wide response to sepsis"
slug: pairwise-cytokine-code-explains-organism-wide
arxiv: ""
doi: "10.1038/s41590-023-01722-8"
pmid: "38191855"
venue: "Nature Immunology"
year: 2024
authors:
  - Michihiro Takahama
  - Ashwini Patil
  - Gabriella Richey
  - Denis Cipurko
  - Katherine Johnson
  - Peter Carbonetto
  - Madison Plaster
  - Surya Pandey
  - Katerina Cheronis
  - Tatsuki Ueda
  - Adam Gruenbaum
  - Tadafumi Kawamoto
  - Matthew Stephens
  - Nicolas Chevrier
first_author: "Michihiro Takahama"
corresponding_author: "Nicolas Chevrier"

source_type: pdf
s2_id: "7d64969bb283b69896ee6d9383f590bd907bde63"
date_added: 2026-05-22
ingested_date: 2026-05-22
ingest_version: 1
last_reviewed:

importance: 4
tier: TIER_1
tags:
  - sepsis
  - cytokines
  - TNF
  - IL-18
  - IFN-gamma
  - IL-1-beta
  - organism-wide
  - multi-tissue
  - topic-model
  - spatial-transcriptomics
  - immunology
keywords:
  - sepsis
  - endotoxemia
  - cecal ligation puncture
  - pairwise cytokine
  - cytokine storm
  - cytokine hierarchy
  - TNF
  - IL-18
  - IFN-gamma
  - IL-1beta
  - whole-tissue RNA-seq
  - topic modeling
  - grade of membership
  - whole-mouse spatial transcriptomics
  - cell-type abundance scoring
domain: immunology

tissue:
  - bone_marrow
  - blood
  - liver
  - lung
  - kidney
  - heart
  - colon
  - spleen
  - thymus
  - skin
  - multi
condition:
  - inflam_precancer
disease_specific:
  - sepsis
  - endotoxemia
  - polymicrobial-sepsis
species:
  - mouse
hypoxia_relevant: false
contains_immune_cells: true
contains_myeloid: true

techniques:
  - bulk_RNA-seq
  - PME-seq
  - spatial_visium
  - whole_mouse_spatial_transcriptomics
  - flow_cytometry
  - immunohistochemistry
  - TUNEL
  - cytokine-neutralization
  - genetic-knockout
n_samples:
n_cells_total:
integration_method: ""

key_cell_types:
  - hepatocyte
  - kidney_proximal_tubule_epithelial
  - colon_neuron
  - splenic_marginal_zone_B_cell
  - splenic_follicular_B_cell
  - bone_marrow_erythroid
  - neutrophil
  - macrophage
  - endothelial_cell
  - thymocyte
  - T_cell
  - NK_cell
  - dendritic_cell
key_markers:
  - TNF
  - IL-18
  - IFN-gamma
  - IL-1-beta
  - IL-6
  - IL-10
  - S100a8
  - Cr2
  - Serpina1c
  - Eci3
  - Nrn1
  - Bach2
  - Cd274
  - Ctla4
  - Cd86
  - Spp1
  - Crp
  - Calca
  - Ly6G
  - Adgre1
  - Marco
key_pathways:
  - TNF/TNFR1
  - IL-18/IL-18R MyD88-NF-kB
  - IFN-gamma JAK/STAT
  - IL-1R/MyD88
  - MAPK
  - IRF
  - NF-kB inflammation

projects:
  - thesis
priority: reference
read_status: read

hypoxiaverse_status:
exclusion_reason:
data_availability: "GSE236546 / Supplementary Tables 1–6"

code_url: ""
cited_by: []
---

## Problem

Sepsis remains a leading global cause of ICU mortality with no organ-specific targeted therapies, in part because the molecular and cellular response to sepsis across organs has never been mapped at organism scale. The literature implicates many cytokines (TNF, IL-1β, IL-6, IL-10, IL-18, IFN-γ) and many cell-type changes (lymphopenia, neutrophil surge, endothelial activation, hepatic acute phase), but no unifying framework connects which cytokines drive which cellular and tissue effects across the whole body, and decades of single-cytokine clinical trials have failed.

## Key idea

The chaotic blood-cytokine storm of sepsis can be decoded into a small, low-dimensional message: three TNF-anchored cytokine pairs — TNF+IL-18, TNF+IFN-γ and TNF+IL-1β — collectively suffice to recapitulate most of the organism-wide molecular, cellular, physiological and fitness response to bacterial and viral sepsis. The hierarchy is TNF-centered, the interactions are non-additive (synergistic / antagonistic), and the same module is also necessary (cytokine genetic deletion + anti-TNF reverses 32–63% of CLP DEGs).

## Method

- Mouse models: sublethal and lethal LPS endotoxemia + severity-graded CLP polymicrobial sepsis + vaccinia virus Western Reserve viral sepsis.
- Organism-wide bulk transcriptomics: PME-seq whole-tissue RNA-seq on 13 tissues (BM, brain, colon, heart, iLN, kidney, liver, lung, PBMC, SI, skin, spleen, thymus) at 6 timepoints (0.25, 0.5, 1, 2, 3, 5 d).
- Cytokine perturbation screen: 6 single + 15 pair recombinant cytokine injections (TNF, IL-1β, IL-6, IL-10, IL-18, IFN-γ) profiled by bulk RNA-seq in 9 organs at 12 h.
- Statistical/computational pipeline: limma DE (FDR<0.01–0.1, |log2FC|>2), grade-of-membership topic models (fastTopics, k=16), linear modeling for synergy/antagonism classification, cell-type abundance scoring from a 195-cell-type × 9-organ specificity reference.
- Functional perturbations: anti-TNF, anti-IL-18, anti-IFN-γ, anti-IL-1β neutralizing antibodies; Tnf-/-, Il18-/-, Ifng-/-, Il1b-/- genetic deletions; survival and rectal body temperature read-outs.
- Validation: custom large-format whole-mouse spatial transcriptomics on 17 tissues + 10x Visium for kidney; Ly6G / F4/80 IHC; flow cytometry for splenic B cell subsets; TUNEL for hepatocyte apoptosis.

## Results

- LPS endotoxemia produces 10,003 DEGs across 13 tissues, with nonlymphoid organs returning to baseline by 5 d while lymphoid organs do not.
- LPS and CLP DEG profiles overlap 29.5%–68% across 8 tissues at 0.25–1 d; CLP severity scales DEG count and LPS overlap.
- Grade-of-membership (k=16) topic modeling separates baseline tissue identity topics (k4 SI, k7 lung, k15 heart) from sepsis-induced topics (k1 PBMC granulocyte, k6 liver acute phase, k9 organism-wide ISG, k13 splenic/lung neutrophil).
- Of 6 single + 15 paired cytokine conditions, only three pairs (TNF+IL-18, TNF+IFN-γ, TNF+IL-1β) substantially overlap LPS-induced DEGs (TNF+IL-18: 14.9%–56.8%) and produce the largest DEG counts (7,083 / 4,071 / 2,452 vs 382 ± 298 for the other 12 pairs).
- TNF+IL-18 covers 45.7% (118/258) of curated sepsis biomarker genes; TNF+IFN-γ 43.8%, TNF+IL-1β 32.6%, the other 12 pairs only 8.1%±7.3%.
- The three pairs collectively recapitulate viral sepsis (vaccinia WR) tissue effects as well as LPS/CLP bacterial sepsis effects.
- Pairs produce synergistic + antagonistic gene programs not predictable from singles; liver is highest in non-additivity (TNF+IL-18: 10.2% synergistic / 30.3% antagonistic), BM lowest.
- Liver/kidney TNF-pair programs are largely shared across the three pairs; heart/spleen/LNs programs are largely pair-specific.
- Anti-TNF + Il18-/-/Ifng-/-/Il1b-/- counteracts 31.9%–63.3% of CLP-induced DEGs; anti-TNF or anti-IL-1β alone give 100% survival in lethal LPS, while anti-IL-18 / anti-IFN-γ give partial survival.
- Cell-type abundance scoring of 195 cell types across 9 organs links cytokine pairs to: splenic B cell loss (TNF+IL-18), BM erythroid depletion (TNF+IL-1β), endothelial expansion in heart/kidney/liver, hepatocyte and colon-neuron loss, kidney proximal tubule loss, whole-body neutrophil accumulation.
- Whole-mouse spatial transcriptomics validates 7/7 computational predictions (hepatocyte, kidney epithelia, colon neuron, splenic B cells, BM erythroid, neutrophils, macrophages).
- The three pairs together explain ~52% (178/342) of LPS-induced cell-type changes at day 0.5; the remaining ~48% requires additional factors.

## All claims (exhaustive)

- `[c1]` Three TNF-anchored cytokine pairs (TNF+IL-18, TNF+IFN-γ, TNF+IL-1β) recapitulate the organism-wide transcriptional response to sepsis (p.226, 230) "the pairwise effects of tumor necrosis factor plus interleukin (IL)-18, interferon-gamma or IL-1β suffice to mirror the impact of sepsis across tissues." — confidence: high — type: mechanistic — links: [[concepts/pairwise-cytokine-code-sepsis]] [[foundations/tnf-tumor-necrosis-factor]] [[foundations/il-18-cytokine]] [[foundations/ifn-gamma-cytokine]] [[foundations/il-1-beta-cytokine]] [[claims/pairwise-cytokine-code-recapitulates-sepsis]]
- `[c2]` TNF+IL-18 is the most impactful cytokine pair, producing 7,083 DEGs across organs versus 382 ± 298 for non-TNF pairs (p.230) "TNF plus IL-18, IFN-γ or IL-1β regulated the most genes across all organs with 7,083, 4,071 or 2,452 genes, respectively, compared to the average number of DEGs, 382 ± 298 s.d., for the other 12 pairs tested." — confidence: high — type: quantitative — links: [[foundations/tnf-tumor-necrosis-factor]] [[foundations/il-18-cytokine]] [[claims/tnf-il18-most-impactful-cytokine-pair]]
- `[c3]` Nonlymphoid tissues return to transcriptional steady state within 5 d of LPS while lymphoid tissues do not (p.227) "nonlymphoid tissues returned to their transcriptional steady state within 5 d of LPS injection, whereas lymphoid tissues did not, which is reminiscent of the reported link between sepsis and long-term immune defects." — confidence: high — type: correlational — links: [[concepts/lymphoid-nonlymphoid-recovery-asymmetry-sepsis]] [[claims/lymphoid-tissue-delayed-recovery-sepsis]]
- `[c4]` LPS and CLP sepsis produce overlapping organ transcriptomes (29.5%–68% DEG overlap), with severity scaling DEG count (p.228–229) "high degree of similarity between the tissue expression profiles of LPS and CLP at 0.25 d, 0.5 d and 1 d after sepsis, ranging from 29.5% in heart to 68% in thymus upon severe CLP sepsis at 0.5 d." — confidence: high — type: correlational — links: [[foundations/lps-toll-like-receptor-signaling]] [[foundations/cecal-ligation-puncture-clp]] [[claims/lps-clp-tissue-transcriptome-overlap]]
- `[c5]` The four-cytokine module (TNF, IL-18, IFN-γ, IL-1β) is sufficient to phenocopy sepsis at molecular, cellular, physiological and fitness levels (p.230–232) "Taken together, the similarities in tissue transcriptional states between sepsis and the three key cytokine pairs reflected similarities in physiological effects, including tissue injury, body temperature and survival." — confidence: high — type: mechanistic — links: [[concepts/pairwise-cytokine-code-sepsis]] [[concepts/tnf-centered-cytokine-hierarchy]] [[claims/four-cytokine-module-sufficient-sepsis]]
- `[c6]` Anti-TNF or anti-IL-1β prophylaxis yields 100% survival of lethal LPS and preserves body temperature; anti-IL-18 / anti-IFN-γ only partial (p.232) "blocking TNF or IL-1β led to 100% survival in mice challenged with a lethal dose of LPS, whereas blocking IL-18 or IFN-γ led to partial survival." — confidence: high — type: pharmacological — links: [[foundations/tnf-tumor-necrosis-factor]] [[concepts/tnf-centered-cytokine-hierarchy]] [[claims/anti-tnf-prevents-lethal-lps]]
- `[c7]` Cytokine pairs produce synergistic / antagonistic gene regulation across tissues with liver highest in non-additivity (p.230) "liver displayed some of the highest proportions of synergistic and antagonistic genes across all three cytokine pairs: 10.2% and 30.3% for TNF + IL-18, 6.8% and 15.9% for TNF + IFN-γ and 2.7% and 8.7% for TNF + IL-1β, respectively, whereas bone marrow displayed the lowest." — confidence: high — type: mechanistic — links: [[concepts/cytokine-pair-synergy-antagonism-tissue]] [[claims/cytokine-pair-synergy-antagonism-gene-regulation]]
- `[c8]` Cytokine pair programs are mostly shared in liver/kidney but mostly pair-specific in heart/spleen/LNs (p.230) "these three cytokine pairs regulated genes showing both shared and pair-specific patterns of expression, as in liver and kidney (mostly shared), and heart, spleen and LNs (mostly pair-specific)." — confidence: medium — type: correlational — links: [[concepts/cytokine-pair-synergy-antagonism-tissue]] [[claims/shared-vs-pair-specific-cytokine-tissue-programs]]
- `[c9]` LPS sepsis drives whole-body neutrophil accumulation across 17 tissues, validated by S100a8 spatial transcriptomics and lung Ly6G IHC (p.235–236) "We found neutrophil accumulation in all 17 tissues profiled by whole-mouse sections and in the vasculature, as indicated by the upregulation of S100a8 transcripts." — confidence: high — type: methodological — links: [[concepts/cell-type-abundance-from-bulk-tissue-rnaseq]] [[claims/organism-wide-neutrophil-accumulation-lps]]
- `[c10]` TNF+IL-18 is sufficient to deplete splenic marginal-zone and follicular B cells (validated by spatial + flow) (p.236) "TNF plus IL-18 combined to deplete B cell subsets including follicular and, even more so, marginal zone B cells, by spatial transcriptomics and flow cytometric analysis." — confidence: high — type: mechanistic — links: [[claims/tnf-il18-splenic-b-cell-depletion]] [[foundations/tnf-tumor-necrosis-factor]] [[foundations/il-18-cytokine]]
- `[c11]` TNF+IL-1β depletes BM erythroid lineage cells, providing a mechanistic basis for sepsis anemia (p.236) "we confirmed that TNF plus IL-1β are sufficient to decrease the abundance of cell types from the erythroid lineage which help to explain anemia, a well-described phenomenon in sepsis." — confidence: medium — type: mechanistic — links: [[foundations/tnf-tumor-necrosis-factor]] [[foundations/il-1-beta-cytokine]] [[claims/tnf-il1beta-erythroid-depletion]]
- `[c12]` LPS and TNF-anchored cytokine pairs increase endothelial cell-type abundance in heart, kidney and liver (p.234–236) "LPS and cytokine pairs led to an increase in abundance of endothelial cell types associated with the heart, kidney and liver, which is corroborated by recent work, and our results identify the cytokine factors driving this effect on the endothelium across tissues." — confidence: medium — type: correlational — links: [[claims/cytokine-pair-endothelial-increase]]
- `[c13]` LPS and cytokine pairs downregulate hepatocytes, validated by Serpina1c spatial transcriptomics + TUNEL (p.234–235) "marker genes for hepatocytes, kidney epithelia and colon neurons were downregulated by LPS sepsis... hepatocytes were negatively impacted by LPS and cytokine pairs using TUNEL staining." — confidence: high — type: methodological — links: [[claims/hepatocyte-downregulation-sepsis]]
- `[c14]` Cell-type abundance scoring from bulk tissue RNA-seq using specificity-ranked gene sets recovers 195-cell-type shifts across 9 organs and validates 7/7 in spatial transcriptomics (p.232–234) "we computed a cell-type specificity score for each gene expressed in 195 cell types across 9 organs. Resulting gene-centric specificity scores were used to define ranked gene sets for each cell type." — confidence: high — type: methodological — links: [[concepts/cell-type-abundance-from-bulk-tissue-rnaseq]] [[claims/cell-type-abundance-score-bulk-rnaseq-methodology]]
- `[c15]` Grade-of-membership topic modeling (k=16) on whole-tissue RNA-seq separates baseline tissue identity from sepsis-driven cross-tissue processes (p.228) "We analyzed the LPS time-series data using grade of membership models to examine the impact of sepsis on intra-tissue and cross-tissue states... topic k9 reflected organism-wide changes in interferon-stimulated genes." — confidence: high — type: methodological — links: [[foundations/fasttopics-grade-of-membership]] [[claims/topic-modeling-sepsis-tissue-processes]]
- `[c16]` The three cytokine pairs collectively explain ~52% (178/342) of LPS-induced cell-type changes; the rest is not cytokine-encoded (p.237) "our data linked one of the three cytokine pairs or more with 52% (178/342 at day 0.5) of the target cell types tested in at least one organ type and impacted with LPS, the other half of the cellular effects of LPS on tissues remained unexplained by the three cytokine pairs used here." — confidence: medium — type: quantitative — links: [[claims/cytokine-pairs-explain-half-lps-cellular-effects]]
- `[c17]` TNF+IL-18 regulates 45.7% (118/258) of curated sepsis biomarker genes, TNF+IFN-γ 43.8%, TNF+IL-1β 32.6%, vs 8.1%±7.3% for the other 12 pairs (p.230) "encompassed a high proportion of sepsis biomarker genes, 45.7% (118/258), 43.8% (113/258) or 32.6% (84/258), respectively, compared to the other 12 cytokine pairs tested (8.1% ± 7.3% s.d.)." — confidence: high — type: quantitative — links: [[claims/tnf-il18-sepsis-biomarker-coverage]]
- `[c18]` Whole-mouse large-format spatial transcriptomics validates 7/7 computational cytokine-pair → cell-type predictions (p.234–236) "all seven associations between cytokines and cell types selected for further study were validated by experiments, encompassing hepatocytes, kidney epithelia, colon neuronal cells, splenic B cells, bone marrow erythroid cells and whole-body neutrophils and macrophages." — confidence: high — type: methodological — links: [[claims/spatial-transcriptomics-cytokine-cell-type-validation]]
- `[c19]` Combined anti-TNF + cytokine genetic deletion counteracts 31.9%–63.3% of CLP-induced gene changes (p.231) "pairwise cytokine perturbations counteracted most of the gene expression changes due to CLP sepsis, with total overlaps in DEGs ranging from 31.9% (2,267/7,106 genes) for anti-TNF + Il1b−/−, 45.6% (3,242/7,106 genes) for anti-TNF + Il18−/−, to 63.3% (4,497/7,106 genes) for anti-TNF + Ifng−/−." — confidence: high — type: pharmacological — links: [[claims/tnf-blockade-reverses-clp-tissue-transcriptome]]

## Discussion captured

### Authors' interpretation

The authors interpret their findings as a "decoding" of the cytokine cacophony in sepsis into a low-dimensional, hierarchical message. TNF sits at the apex of the network because (i) every cytokine pair that suffices to mimic sepsis contains TNF, (ii) anti-TNF alone protects against lethal LPS, and (iii) TNF kinetics in mouse and human peak in blood within 2 h. They argue the pairwise rather than single-cytokine logic explains decades of mixed in-vitro / in-vivo cytokine interaction data and the historical failure of single-cytokine clinical trials in sepsis. They draw a parallel to the broader cytokine hierarchy defining human chronic inflammatory diseases, where anti-TNF therapy has the widest cross-disease efficacy.

### Comparisons with prior literature (made by authors)

- Built on prior organism-wide profiling from the same lab — vaccination across tissues (Kadoki 2017 Cell) and PME-seq (Pandey 2020 Nat Protoc) — extending the methodology to perturbation by sepsis and cytokines.
- Connects to four decades of in-vitro work on TNF synergy/antagonism with IFN-γ and IL-1β (refs 33-37), and prior in-vivo work showing TNF+IFN-γ or IL-1β worsen sepsis outcome (refs 38-44).
- Anemia and erythroid depletion in sepsis previously linked to Bach2 (Kato 2018, ref 21) — this paper assigns the upstream cytokine driver (TNF+IL-1β).
- Splenic B cell loss observed previously in CLP (ref 28); causal cytokine factor (TNF+IL-18) is established here for the first time.
- Endothelial expansion in sepsis recently described; this paper identifies the responsible cytokine pairs.
- TNF as central anti-inflammatory drug target across psoriasis / IBD / RA / AS / juvenile arthritis is referenced (ref 58) to contextualise the apex role.

### Mechanistic hypotheses proposed

- "The cytokines of this module also influence each other's production, which further supports the hierarchy uncovered by our pairwise cytokine screening data."
- Direct vs indirect cytokine pair effects through downstream secondary cytokines and non-cytokine diffusibles (hypothesized).
- MAPK, NF-κB, IRF, JAK/STAT pathway rewiring as the molecular substrate of pairwise synergy/antagonism (proposed for future testing).
- TNF apex role partly explained by ubiquitous TNF-receptor expression.

### Caveats and self-criticism

- The three pairs explain ~52% of LPS-induced cell-type changes; the other ~48% requires additional cytokine or non-cytokine factors (complement, coagulation), explicitly acknowledged.
- Direct vs indirect cytokine pair effects on each cell type are not separated.
- Late-phase tissue recovery during CLP with antibiotic treatment (closer to human ICU practice) is not assessed.
- All results are in mouse; human translation untested.

### Future directions suggested

- Identify the non-cytokine factors filling the unexplained 48% (complement, coagulation, DAMPs).
- Map direct vs indirect pair effects per cell type.
- Profile recovery dynamics under antibiotic-treated CLP.
- Investigate the molecular pathway rewiring (MAPK / NF-κB / IRF / JAK-STAT) underlying synergy/antagonism.
- Test the pairwise code in other cytokine storm syndromes (COVID-19, CRS, MAS, HLH).
- Identify tissue-protective factors safeguarding nonlymphoid tissues (e.g., IL-10 for microglia, GDF15 for heart).

## Limitations

- Mouse-only; no human sepsis cohort data.
- Single sublethal LPS dose and single cytokine i.v. dose; dose-response and route effects not exhaustively mapped.
- Cytokine pair screen is exhaustive at the pair level but does not test triplets/quartets.
- Bulk-tissue resolution; cell-type abundance scoring is inferred from a single reference atlas and validated only for the 7 selected cases.
- TNF neutralization alone in CLP produced minimal DEG significance at the threshold tested — a power-vs-effect ambiguity acknowledged in the text.
- Survival/temperature read-outs are 5/group cohorts.

## Open questions

### Open questions raised by authors

- What fills the unexplained ~48% of LPS cellular effects beyond the three cytokine pairs?
- Are the direct cellular targets of each cytokine pair separable from indirect ones?
- What molecular pathway rewiring (MAPK / NF-κB / IRF / JAK-STAT) underlies the synergy and antagonism?
- Why is TNF the apex node — receptor ubiquity, kinetics or signalling crosstalk?
- Does the pairwise code generalise to non-sepsis cytokine storms in human disease?

### Open questions identified during ingest

- How transferable is the cell-type-abundance scoring method to atlases with different cell-type granularity?
- Could a "pairwise code" exist for chronic inflammatory diseases (RA, psoriasis, IBD) where anti-TNF works but other monotherapies do not?
- What does combining anti-TNF with cytokine knockout in human cytokine storm syndromes (CRS) look like, given that TNF half-life and kinetics in humans differ?
- How does the pairwise code intersect with the broader [[concepts/cytokine-cell-type-specific-response-pleiotropy]] insight from the Immune Dictionary (Cui & Hacohen 2024)?
- Is the lymphoid-nonlymphoid recovery asymmetry preserved across mouse strains and ages?

## My take

This is a landmark paper for systems-level thinking about cytokine biology in sepsis: it operationalises "the cytokine storm" into a measurable, perturbation-tractable code, and provides a TNF-apex explanation for both why anti-TNF has the widest cross-disease efficacy in chronic inflammation and why single-cytokine sepsis trials fail. The combination of organism-wide bulk profiling (PME-seq, 13 tissues × 6 timepoints), exhaustive pairwise cytokine perturbation (6 singles + 15 pairs × 9 organs), and whole-mouse spatial transcriptomics validation defines a new bar for cytokine network biology — directly relevant to any future "pairwise code" studies in other inflammatory conditions and complementary to the cell-type-specific cytokine pleiotropy framework from the Immune Dictionary. The 52% unexplained cellular effects is the honest limitation and the most actionable follow-up.

## Related

- [[concepts/pairwise-cytokine-code-sepsis]]
- [[concepts/tnf-centered-cytokine-hierarchy]]
- [[concepts/cytokine-pair-synergy-antagonism-tissue]]
- [[concepts/lymphoid-nonlymphoid-recovery-asymmetry-sepsis]]
- [[concepts/cell-type-abundance-from-bulk-tissue-rnaseq]]
- [[concepts/organism-wide-multi-tissue-perturbation-profiling]]
- [[concepts/cytokine-cell-type-specific-response-pleiotropy]]
- [[concepts/cytokine-mediated-immune-cell-cell-interactome]]
- [[concepts/tissue-context-dependence-immune-signaling]]
- [[foundations/tnf-tumor-necrosis-factor]]
- [[foundations/il-18-cytokine]]
- [[foundations/il-1-beta-cytokine]]
- [[foundations/ifn-gamma-cytokine]]
- [[foundations/il-6-cytokine]]
- [[foundations/il-10-cytokine]]
- [[foundations/lps-toll-like-receptor-signaling]]
- [[foundations/cecal-ligation-puncture-clp]]
- [[foundations/fasttopics-grade-of-membership]]
- [[foundations/limma-differential-expression]]
- [[foundations/pme-seq-whole-tissue-rna-seq]]
- [[people/nicolas-chevrier]]
- [[people/michihiro-takahama]]
- [[people/matthew-stephens]]
- [[papers/single-cell-cytokine-dictionary-human-peripheral]] — complementary cytokine-perturbation axis: single-cytokine in vitro human PBMC single-cell (vs pairwise in vivo organism-wide bulk); together they span the single-vs-pairwise and human-vs-mouse cytokine-perturbation literature.
