---
# === Identification ===
title: "O-GlcNAcylation shapes macrophage tissue residency and alternative activation"
slug: glcnacylation-shapes-macrophage-tissue-residency-alternative
arxiv: ""
doi: "10.1038/s41577-026-01278-2"
pmid: ""
venue: "Nature Reviews Immunology"
year: 2026
authors:
  - "Amitava Sinha"
  - "Thomas Weichhart"
first_author: "Amitava Sinha"
corresponding_author: "Thomas Weichhart"

# === Source & metadata ===
source_type: pdf
s2_id: ""
date_added: 2026-06-02
ingested_date: 2026-06-02
ingest_version: 1
last_reviewed: null

# === Classification ===
importance: 2
tier: TIER_3
tags:
  - journal-club
  - preprint-watch
  - commentary
  - macrophage
  - immunometabolism
  - o-glcnac
  - tissue-residency
  - alternative-activation
keywords:
  - O-GlcNAcylation
  - O-GlcNAc transferase (OGT)
  - UDP-GlcNAc
  - alternatively activated macrophages
  - tissue-resident macrophages
  - large cavity macrophages
  - macrophage cell cycle
  - senescence
domain: "immunology / immunometabolism"

# === Biomedical domain ===
tissue:
  - peritoneum
  - lung
  - liver
  - intestine
  - multi
condition:
  - healthy
disease_specific:
  - helminth_infection
species:
  - mouse
hypoxia_relevant: false
contains_immune_cells: true
contains_myeloid: true

# === Technique ===
techniques:
  - flow_cytometry
  - conditional_knockout_mouse
  - macrophage_t_cell_coculture
n_samples: null
n_cells_total: null
integration_method: ""

# === Biology captured ===
key_cell_types:
  - alternatively_activated_macrophage
  - large_cavity_macrophage
  - small_cavity_macrophage
  - converting_cavity_macrophage
  - tissue_resident_macrophage
  - monocyte
key_markers:
  - Ogt
  - O-GlcNAc
  - UDP-GlcNAc
  - TIM4
  - IL-4
key_pathways:
  - O-GlcNAcylation
  - hexosamine_biosynthetic_pathway
  - IL-4_alternative_activation
  - cell_cycle

# === User project membership ===
projects:
  - thesis
priority: reference
read_status: read

# === HypoxiaVERSE-specific ===
hypoxiaverse_status: not_included
exclusion_reason: "One-page Journal Club / Preprint Watch commentary on a non-peer-reviewed preprint (Heieis et al.); not a dataset. Retained as a macrophage-immunometabolism reference (O-GlcNAc control of tissue-resident macrophage maintenance and IL-4 alternative activation)."
data_availability: ""

# === Cross-references ===
code_url: ""
cited_by: []
---

## Problem

Alternatively activated macrophages (AAMs) are induced by type-2 cytokines such as IL-4 during T-helper-2 responses (e.g. to parasites), and IL-4 also drives macrophage local proliferation. The metabolite UDP-GlcNAc is known to be enriched in AAMs, and it is the substrate for O-GlcNAcylation — a reversible Ser/Thr modification, written by O-GlcNAc transferase (OGT), found on many proteins involved in cell-cycle control, metabolism, and nutrient sensing. What had been unclear is whether O-GlcNAcylation is *functionally required* for the AAM programme and for the maintenance of tissue-resident macrophages, or merely a metabolic byproduct.

## Key idea

This is a one-page *Nature Reviews Immunology* **Journal Club / Preprint Watch** commentary (Amitava Sinha & Thomas Weichhart, Preprint Club, Medical University of Vienna) on a non-peer-reviewed bioRxiv preprint — **Heieis, G. A. et al., "O-GlcNAcylation drives macrophage IL-4 responsiveness and tissue residency through metabolic and cell cycle calibration" (bioRxiv 2026, doi:10.64898/2026.01.05.697622)**. The commentary's thesis: O-GlcNAcylation ([[foundations/glcnacylation]], catalysed by [[foundations/ogt-glcnac-transferase]] from [[foundations/udp-glcnac-uridine-diphosphate-acetylglucosamine]]) is a central metabolic regulator of both IL-4-driven alternative activation and macrophage tissue residency — the axis captured as [[concepts/glcnacylation-metabolic-regulator-macrophage-cell-cycle]].

## Method

As summarized by the commentary, Heieis et al. used:
- **Macrophage/myeloid-specific Ogt deletion** (Lyz2ΔOgt, via [[foundations/lysm-cre]]) to remove O-GlcNAcylation in vivo.
- **In vivo helminth challenge** to test IL-4-driven AAM function.
- **Peritoneal cavity macrophage profiling** to track the monocyte → small cavity macrophage (SCM) → converting cavity macrophage (CCM) → large cavity macrophage (LCM) maturation trajectory and TIM4+ ([[foundations/tim-4-timd4]]) mature LCMs.
- **Metabolic, ROS/DNA-damage, senescence, and cell-cycle assays** on LCMs.
- **Macrophage–T-cell co-cultures** with pharmacological OGT inhibition.
- Steady-state and immune-challenge analyses of lung, liver, and intestinal tissue-resident macrophages.

No quantitative values, code, or figures are reproduced in the commentary.

## Results

(All as reported in the commentary's summary of the Heieis et al. preprint.)

- Lyz2ΔOgt mice: decreased O-GlcNAcylation, reduced IL-4-driven AAM markers, defective helminth control.
- Myeloid Ogt deficiency disrupted peritoneal tissue-resident macrophage homeostasis: reduced LCMs, increased monocyte-derived SCMs/CCMs; TIM4+ mature LCMs stayed decreased even during infection resolution.
- O-GlcNAcylation was dynamically regulated along the monocyte–SCM–CCM–LCM transition.
- Ogt-deficient LCMs: increased glucose dependence over mitochondrial respiration, altered lipid metabolism, increased ROS and DNA damage, and a senescence-like phenotype (enlarged size, senescence markers, spontaneous inflammatory cytokine secretion); accumulation in G2/M without productive division.
- Pharmacological OGT inhibition in co-culture increased macrophage co-stimulatory molecules and T cell proliferation.
- Ogt deficiency also affected abundance, proliferation, and activation of resident macrophages in lung, liver, and intestine (steady state and challenge), indicating a broad requirement.

## All claims (exhaustive)

- `[c01]` Macrophage-specific Ogt deletion reduces O-GlcNAcylation, IL-4-driven AAM markers, and helminth control (p.1) "Mice with macrophage-specific genetic deletion of Ogt (Lyz2ΔOgt) had decreased levels of O-GlcNAcylation, reduced canonical IL-4-driven AAM marker expression and defective helminth control in vivo" — confidence: medium — type: mechanistic — links: [[foundations/ogt-glcnac-transferase]] [[foundations/glcnacylation]] [[foundations/il4-cytokine]] [[foundations/lysm-cre]] [[concepts/glcnacylation-metabolic-regulator-macrophage-cell-cycle]] [[claims/macrophage-ogt-deletion-reduces-il-alternative]]
- `[c02]` Myeloid Ogt deficiency disrupts peritoneal tissue-resident macrophage homeostasis, reducing LCMs and increasing SCMs/CCMs, with TIM4+ LCMs persistently low (p.1) "myeloid-specific Ogt deficiency disrupted tissue-resident macrophage homeostasis, leading to reduced large cavity macrophages (LCMs) and increased monocyte-derived small cavity and converting cavity macrophages (SCMs and CCMs, respectively). Even during the resolution of infection, TIM4+ mature LCMs remained decreased in Lyz2ΔOgt mice" — confidence: medium — type: mechanistic — links: [[foundations/large-cavity-macrophage-lcm-peritoneal]] [[foundations/tim-4-timd4]] [[concepts/glcnacylation-metabolic-regulator-macrophage-cell-cycle]] [[claims/myeloid-ogt-deficiency-disrupts-peritoneal-tissue]]
- `[c03]` O-GlcNAcylation is dynamically regulated during the monocyte–SCM–CCM–LCM transition (p.1) "O-GlcNAcylation is dynamically regulated during the monocyte–SCM–CCM–LCM transition" — confidence: medium — type: correlational — links: [[foundations/glcnacylation]] [[foundations/large-cavity-macrophage-lcm-peritoneal]] [[claims/glcnacylation-dynamically-regulated-monocyte-large-cavity]]
- `[c04]` Ogt deficiency rewires LCM metabolism (glucose over mitochondrial respiration, altered lipids), increases ROS/DNA damage, and drives a senescence-like phenotype with G2/M arrest (p.1) "Ogt deficiency altered LCM metabolism, characterized by increased dependence on glucose over mitochondrial respiration, and altered lipid metabolism. Ogt-deficient LCMs had increased production of reactive oxygen species and DNA damage, features consistent with a senescent phenotype ... accumulation of Ogt-deficient LCMs in cycling (G2/M) populations but failure to undergo productive division" — confidence: medium — type: mechanistic — links: [[foundations/large-cavity-macrophage-lcm-peritoneal]] [[concepts/glcnacylation-metabolic-regulator-macrophage-cell-cycle]] [[claims/ogt-deficiency-rewires-macrophage-metabolism-induces]]
- `[c05]` Pharmacological OGT inhibition increases macrophage co-stimulatory molecules and T cell proliferation in co-culture (p.1) "pharmacological inhibition of OGT increased the expression of co-stimulatory molecules on macrophages and resulted in increased T cell proliferation" — confidence: low — type: pharmacological — links: [[foundations/ogt-glcnac-transferase]] [[claims/ogt-inhibition-increases-macrophage-costimulation-cell]]

## Discussion captured

### Authors' interpretation

The commentary authors (Sinha & Weichhart) frame the study as identifying O-GlcNAcylation as "a metabolic regulator of the cell cycle that enables macrophages to acquire and maintain a long-lived tissue-resident state, while enabling IL-4-driven alternative activation." The unifying claim is that one nutrient-coupled modification links AAM identity, productive proliferation, and residency.

### Comparisons with prior literature (made by authors)

- Prior work establishing that **UDP-GlcNAc is enriched in alternatively activated macrophages** — the metabolic premise the preprint builds on.
- Background that O-GlcNAcylation (via OGT) modifies many proteins in cell-cycle control, metabolism, and nutrient sensing.

### Mechanistic hypotheses proposed

- O-GlcNAcylation acts as a cell-cycle "calibration" mechanism: without it, maturing cavity macrophages enter G2/M but cannot complete productive division, defaulting to a senescence-like state instead of self-renewing residency.

### Caveats and self-criticism

- The commentary explicitly flags that the source is a **preprint (not peer-reviewed)**.

### Future directions suggested

- The commentary is descriptive; it does not enumerate formal future directions beyond positioning O-GlcNAcylation as a target of interest in macrophage residency and activation.

## Limitations

- **Secondary source**: this is a one-page Journal Club / Preprint Watch note, not the primary research article; all results are qualitative summaries of Heieis et al.
- The **primary preprint is not peer-reviewed**, so every claim here carries provisional confidence.
- No quantitative data, statistics, code, or figures are available from the commentary.

## Open questions

### Open questions raised by authors

- Implicitly: which O-GlcNAcylated substrate(s) mediate the cell-cycle "calibration" enabling residency and IL-4 responsiveness?

### Open questions identified during ingest

- Does the O-GlcNAc→residency axis operate in tumour-associated macrophages and in hypoxic, glucose-competing niches (the thesis-relevant test)?
- Is the senescence-like G2/M arrest of Ogt-deficient LCMs reversible by restoring O-GlcNAc or relieving ROS/DNA damage?
- How does this metabolic checkpoint relate to other metabolite-gated residency programmes such as the [[concepts/polyamine-hypusine-axis-macrophage-residency]]?
- Would loss of macrophage O-GlcNAcylation enhance antigen-presentation/co-stimulation enough to be exploitable in tumour immunity?

## My take

As a commentary this is a pointer rather than a primary source — its value is folding a striking immunometabolism claim into the wiki's macrophage-residency landscape. The genuinely interesting idea is mechanistic unification: O-GlcNAcylation, downstream of the nutrient-integrating metabolite UDP-GlcNAc, is proposed to gate three things usually studied apart — AAM identity, the ability to divide, and long-term residency — with its loss diverting cells into a senescence-like dead end. For thesis-relevant TAM/hypoxia work this raises a concrete hypothesis: hypoxic niches that throttle glucose-derived UDP-GlcNAc flux might destabilise resident-macrophage programmes via reduced O-GlcNAcylation. But it rests on a non-peer-reviewed preprint relayed through a secondary source — ingesting the primary Heieis et al. preprint would let these claims be upgraded with real data.

## Related

- [[concepts/glcnacylation-metabolic-regulator-macrophage-cell-cycle]] — the central axis this commentary introduces.
- [[concepts/polyamine-hypusine-axis-macrophage-residency]] — analogous metabolite-gated residency programme.
- [[concepts/macrophage-ontogeny-resident-vs-monocyte-derived]] — the monocyte→resident transition this study places a metabolic checkpoint on.
- [[concepts/tissue-specific-metabolic-programming-macrophages]] — broader immunometabolism theme.
- [[foundations/ogt-glcnac-transferase]] / [[foundations/glcnacylation]] / [[foundations/udp-glcnac-uridine-diphosphate-acetylglucosamine]] — the O-GlcNAc machinery.
- [[foundations/large-cavity-macrophage-lcm-peritoneal]] / [[foundations/tim-4-timd4]] / [[foundations/lysm-cre]] / [[foundations/il4-cytokine]] / [[foundations/gfpt1-gfat1-glutamine-fructose-aminotransferase]] / [[foundations/gata6-tf]] — biological entities and tools named.
- [[people/amitava-sinha]] / [[people/thomas-weichhart]] — commentary authors.
