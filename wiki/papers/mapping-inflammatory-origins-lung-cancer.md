---
# === Identification ===
title: "Mapping the inflammatory origins of lung cancer"
slug: mapping-inflammatory-origins-lung-cancer
arxiv: ""
doi: "10.1016/j.ccell.2025.11.005"
pmid: "41386222"
venue: "Cancer Cell"
year: 2026
authors:
  - Nobunari Sasaki
  - Mizuki Homme
  - Shunsuke Kitajima
first_author: "Nobunari Sasaki"
corresponding_author: "Shunsuke Kitajima"

# === Source & metadata ===
source_type: pdf
s2_id: "293e4c76bd7e1debc64c0c893edc3dfe2527aaf3"
date_added: 2026-06-03
ingested_date: 2026-06-03
ingest_version: 1
last_reviewed:

# === Classification ===
importance: 2
tier: TIER_3
tags:
  - luad
  - lung-cancer
  - precancer-interception
  - il1b-il1r1
  - spatial-omics
  - proinflammatory-niche
  - commentary
keywords:
  - lung adenocarcinoma
  - precursor lesions
  - KAC
  - RPII
  - IL-1β
  - canakinumab
  - tumor microenvironment
domain: oncology

# === Biomedical domain ===
tissue: [lung]
condition: [cancer, inflam_precancer]
disease_specific: [LUAD]
species: [human, mouse]
hypoxia_relevant: false
contains_immune_cells: true
contains_myeloid: true

# === Technique ===
techniques: [spatial_visium, snRNA-seq, xenium]
n_samples:
n_cells_total:
integration_method: ""

# === Biology captured ===
key_cell_types:
  - reactive type II pneumocytes (RPII)
  - KRT8-high alveolar intermediate cells (KAC)
  - alveolar type II cells (AT2)
  - macrophages
  - CD8+ cytotoxic T cells
key_markers:
  - KRT8
  - IL1B
  - IL1R1
  - SFTPC
  - CEACAM5
  - MUC5B
  - LAMP3
  - Gprc5a
key_pathways:
  - IL-1β–IL1R1 signaling
  - NF-κB inflammatory signaling

# === User project membership ===
projects: [thesis]
priority: reference
read_status: not_read

# === HypoxiaVERSE-specific ===
hypoxiaverse_status:
exclusion_reason:
data_availability: ""

# === Cross-references ===
code_url: ""
cited_by: []
---

## Problem

The molecular mechanisms by which early cancer precursor cells form within lung adenocarcinoma (LUAD) premalignant lesions — and how their surrounding microenvironment co-develops and drives malignant progression — remain largely unclear. Comprehensive spatial-transcriptomic studies focused on the malignant progression and microenvironmental interactions of *early-phase* tumor precursor cells have been limited, which is a barrier to early detection and interception of LUAD.

## Key idea

This is a *Preview* (commentary) in Cancer Cell discussing **Peng et al. (2025/2026)** [[multimodal-spatial-omics-reveal-co-evolution]]. The commentary frames the central message of that study: multimodal spatial-omics on patient-matched precursor and invasive LUAD lesions reveals that **KRT8-high reactive type II pneumocytes (RPII) — equivalent to KAC alveolar intermediate cells — co-evolve with proinflammatory macrophage niches**, coupled via the **IL-1β–IL1R1 signaling axis**, even before clinically recognizable precursor lesions emerge. The authors of the commentary highlight IL-1β as a validated interception target and situate it against the mixed clinical record of canakinumab in NSCLC.

## Method

The commentary itself performs no new experiments; it summarizes and contextualizes Peng et al. The methods discussed include: Visium spatial transcriptomics (56 samples / 25 patients; 486,519 spots; 5.4 million cells), single-nucleus RNA-seq, Xenium in situ analysis, immunohistochemistry, whole-exome sequencing, copy-number-variation–based clonal-evolution analysis, non-negative matrix factorization (NMF), and *Gprc5a*-deficient + NNK mouse carcinogenesis models with anti-IL-1β / anti-PD-1 antibody interventions.

## Results

The commentary relays the primary study's findings:
- AAH/AIS precursor lesions retain high AT2 marker *SFTPC*; LUAD upregulates dedifferentiation/tumorigenesis genes *KRT8*, *CEACAM5*, *MUC5B*.
- CNV-based clonal evolution falls into three patterns (shared, partial-sharing, no-sharing); the earliest emerging clone often corresponds to RPII.
- NMF + spatial integration places RPII/KAC at an intermediate position between normal AT2 and tumor cells — a "bridging" population preceding clinical precursor lesions.
- RPII/KACs express high *IL1R1*; adjacent macrophages express high *IL1B*, implicating IL-1β–IL1R1 coupling.
- In mouse models, *Il1r1* deletion reduces tumor formation and KRT8⁺/LAMP3⁺ cells; recombinant IL-1β or macrophage co-culture promotes KAC-rich organoid growth.
- Anti-IL-1β monotherapy suppresses tumors more than anti-PD-1; combination is strongest in the interception phase; no effect in the syngeneic established-tumor model — IL-1β inhibition works only in early stages.

## All claims (exhaustive)

- `[c1]` RPII/KAC (KRT8-high alveolar intermediate cells) are the earliest emerging clonal precursors of LUAD, a bridging population between normal AT2 and tumor cells that exists before clinically recognizable precursor lesions (p.248) "the earliest emerging clone in many cases corresponded to reactive type II pneumocytes (RPII)... RPII represents a 'bridging cell population' in the transition from normal alveolar cells to tumor cells, existing even before clinically recognizable precursor lesions emerge" — confidence: medium — type: mechanistic — links: [[concepts/kac-krt8-alveolar-intermediate-cells-luad-progenitors]] [[claims/kac-rpii-earliest-luad-precursor-cells]]
- `[c2]` RPII/KACs express high IL1R1 while adjacent proinflammatory macrophages express high IL1B, coupling the two populations through IL-1β–IL1R1 signaling as a core driver of alveolar epithelial tumorigenesis (p.248) "high IL1R1 expression in RPII/KACs, whereas adjacent proinflammatory niches contained macrophages expressing high levels of IL1B, suggesting an interaction... via the IL-1β-IL1R1 signaling pathway" — confidence: high — type: mechanistic — links: [[concepts/epithelial-proinflammatory-niche-il1b-il1r1-luad-precursor]] [[foundations/il-1-beta-cytokine]] [[foundations/il1r1-receptor]] [[claims/il1b-il1r1-top-ligand-receptor-precursor]]
- `[c3]` Deletion of Il1r1 in mouse lung epithelial cells significantly reduces tumor formation and the KRT8⁺/LAMP3⁺ cell population (p.248) "Deletion of Il1r1 in mouse lung epithelial cells significantly reduced tumor formation and the population of KRT8+/LAMP3+ cells" — confidence: high — type: pharmacological — links: [[foundations/il1r1-receptor]] [[foundations/gprc5a-knockout-luad-mouse-model]] [[claims/il1r1-knockout-reduces-kras-luad-and-krt8-lamp3-cells]]
- `[c4]` Recombinant IL-1β administration or macrophage co-culture promotes growth of KAC-rich organoids (p.248) "administration of recombinant IL-1β or co-culture with macrophages promoted growth of KAC-rich organoids" — confidence: high — type: pharmacological — links: [[foundations/il-1-beta-cytokine]] [[claims/recombinant-il1b-and-im-coculture-increase-krt8-organoid-growth]]
- `[c5]` Anti-IL-1β antibody monotherapy suppresses tumors more strongly than anti-PD-1 in NNK-exposed Gprc5a-deficient mice, with combination treatment most pronounced in the interception phase (p.248) "Anti-IL-1β antibody monotherapy showed stronger tumor suppression than anti-PD-1 antibody, with combination treatment being even more pronounced especially in the interception-phase treatment" — confidence: medium — type: pharmacological — links: [[concepts/il1b-precancer-interception-luad]] [[foundations/canakinumab-anti-il1b]] [[foundations/nnk-tobacco-carcinogen]] [[claims/anti-il1b-anti-pd1-combination-superior-precancerous-interception]]
- `[c6]` IL-1β inhibition is effective only in early/precancerous stages of LUAD: no tumor suppression is seen in the syngeneic established-tumor model (p.248) "tumor suppression in the syngeneic tumor model was not observed, suggesting that IL-1β inhibition is effective only in the early stages of LUAD development" — confidence: medium — type: pharmacological — links: [[concepts/il1b-precancer-interception-luad]] [[claims/anti-il1b-no-effect-syngeneic-established-luad]]

## Discussion captured

### Authors' interpretation

The commentary authors interpret Peng et al.'s results as defining IL-1β–IL1R1 signaling as a "core driver of alveolar epithelial cell tumorigenesis" and frame RPII/KAC–macrophage proinflammatory niches as forming earlier than the clinical definition of precursor lesions. They read combination anti-IL-1β + anti-PD-1 (reduced KAC and macrophage fractions, increased CD8⁺ T-cell infiltration) as evidence that IL-1β blockade drives both tumor suppression and immune activation during the precancerous stage.

### Comparisons with prior literature (made by authors)

- Han et al. 2024, *Nature* 627:656–663 (DOI 10.1038/s41586-024-07113-9) — prior report of KRT8-high alveolar intermediate cells (KACs) acting as LUAD precursors, which RPII histologically resembles.
- Zhu et al. 2025, *Cancer Cell* 43:1125–1140 (DOI 10.1016/j.ccell.2025.04.003) — spatial/multiomics of human and mouse LUAD precursors nominating TIM-3 as a precancer-interception target.
- Canakinumab clinical trials in NSCLC — CANOPY-A (Garon et al. 2024, JCO), CANOPY-2 (Paz-Ares et al. 2024, *Lung Cancer*), CANOPY-1 (Tan et al. 2024, JCO) — cited as having "failed to show the expected benefit."

### Mechanistic hypotheses proposed

- The phase at which IL-1β signaling is suppressed is the critical determinant of clinical efficacy (p.249) "it appears that the phase in which IL-1β signaling is suppressed would be a critical factor in achieving clinical efficacy" — reconciling preclinical success in precancer with the negative late-stage CANOPY trials.

### Caveats and self-criticism

- The authors note that despite the promising preclinical findings, canakinumab trials in established NSCLC have not delivered the expected benefit, implying timing/disease-stage as the unresolved variable.

### Future directions suggested

- Await results of the ongoing Can-Prevent-Lung Trial (NCT04789681, phase 2) testing canakinumab for lung-cancer prevention in patients with high-risk pulmonary nodules.
- Investigate combining anti-IL-1β with ICIs within the precancerous therapeutic time window.

## Limitations

- This is a Preview/commentary, not primary research — all empirical claims derive from Peng et al. and inherit that study's limitations.
- The commentary does not critically scrutinize the primary study's methods or sample sizes; it is largely affirmative.

## Open questions

### Open questions raised by authors

- Will inhibition of IL-1β demonstrate similar efficacy in human LUAD as in the mouse models, particularly when applied at the precancerous window (Can-Prevent-Lung Trial)?
- What is the effect of combining anti-IL-1β with ICIs during the precancerous therapeutic window?

### Open questions identified during ingest

- Can a non-invasive biomarker (e.g., IL1R1-high RPII/KAC signature) prospectively identify the precancer window in which IL-1β blockade is effective?
- Does the stage-dependence of IL-1β efficacy generalize across LUAD oncogenic drivers beyond Kras/Gprc5a contexts?

## My take

A faithful, well-scoped Preview that crystallizes the clinically actionable message of Peng et al.: IL-1β–IL1R1 is a *stage-restricted* interception target, and the negative CANOPY trials likely reflect mistimed (late-stage) intervention rather than a wrong target. For the thesis, its value is as a compact, citable framing of the proinflammatory-niche / KAC-precursor axis and of the precancer-interception window — not as an independent evidence source.

## Related

- [[people/nobunari-sasaki]], [[people/shunsuke-kitajima]] — authors
- [[multimodal-spatial-omics-reveal-co-evolution]] — the primary study this Preview discusses (surveys)
- [[concepts/kac-krt8-alveolar-intermediate-cells-luad-progenitors]]
- [[concepts/epithelial-proinflammatory-niche-il1b-il1r1-luad-precursor]]
- [[concepts/il1b-precancer-interception-luad]]
- [[concepts/spatial-clonal-evolution-patterns-luad-precursor]]
- [[foundations/il-1-beta-cytokine]]
- [[foundations/il1r1-receptor]]
- [[foundations/canakinumab-anti-il1b]]
- [[foundations/nnk-tobacco-carcinogen]]
- [[foundations/gprc5a-knockout-luad-mouse-model]]
- [[foundations/10x-visium-spatial-transcriptomics]]
- [[foundations/xenium-in-situ-spatial-transcriptomics]]
- [[foundations/snrna-seq-single-nucleus]]
- [[foundations/nmf-non-negative-matrix-factorization]]
