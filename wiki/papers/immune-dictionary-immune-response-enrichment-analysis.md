---
# === Identification ===
title: "The Immune Dictionary and Immune Response Enrichment Analysis Web Portal"
slug: immune-dictionary-immune-response-enrichment-analysis
arxiv: ""
doi: ""
pmid: ""
venue: "The Journal of Immunology (AAI Annual Meeting Abstracts; abstract citation ID vkaf283.2735)"
year: 2025
authors:
  - "Nicholas Lai"
  - "Pooja Paresh Savla"
  - "Lawrence Wang"
  - "Brianna S. Yao"
  - "Aileen Ma"
  - "Jorge Perez"
  - "Ang Cui"
first_author: "Nicholas Lai"
corresponding_author: "Ang Cui"

# === Source & metadata ===
source_type: pdf
s2_id: ""
date_added: 2026-06-04
ingested_date: 2026-06-04
ingest_version: 1
last_reviewed:

# === Classification ===
importance: 2
tier: TIER_3
tags:
  - IREA
  - immune-dictionary
  - web-portal
  - cytokine-inference
  - cytokines
  - chemokines
  - perturbational-scRNA-seq
  - computational-immunology
  - software-tool
  - meeting-abstract
keywords:
  - Immune Dictionary
  - IREA web portal
  - cytokine activity inference
  - immune cell polarization
  - 86 cytokines
  - perturbational single-cell RNA-seq
  - chemokines
  - cell-cell network analysis
domain: immunology
# === Biomedical domain ===
tissue:
  - lymph_node
condition:
  - healthy
disease_specific: []
species:
  - mouse
hypoxia_relevant: false
contains_immune_cells: true
contains_myeloid: true

# === Technique ===
techniques:
  - scRNA-seq_10x
  - in_vivo_cytokine_perturbation
  - cytokine_response_enrichment_IREA
  - web_application
n_samples:
n_cells_total:
integration_method: ""

# === Biology captured ===
key_cell_types:
  - B cell
  - CD4+ T cell
  - CD8+ T cell
  - NK cell
  - macrophage
  - dendritic cell
key_markers:
  - cytokines
  - chemokines
key_pathways:
  - cytokine signaling
  - cytokine activity inference
  - cell-cell communication network

# === User project membership ===
projects:
  - thesis
priority: reference
read_status: read

# === HypoxiaVERSE-specific ===
hypoxiaverse_status: candidate
exclusion_reason:
data_availability: "Immune Dictionary / IREA web portal (www.immune-dictionary.org)"

# === Cross-references ===
code_url: "https://github.com/cui-lab/IREA"
cited_by: []
---

## Problem

RNA-seq is ubiquitous in immunology, but software for inferring **cytokine activities** from RNA-seq data has been limited, and the underlying perturbational reference data (the Immune Dictionary) was not easily accessible to bench researchers without bioinformatics support. There was no point-and-click way to ask "which cytokines drive this gene signature?" or to browse how each immune cell type responds to each cytokine.

## Key idea

Deploy the **Immune Dictionary** (single-cell transcriptomic profiles of >17 cell types responding to each of 86 cytokines in mouse lymph nodes in vivo) and its companion software **IREA (Immune Response Enrichment Analysis)** as a single freely-available **web application**. The portal lets researchers (i) interactively visualize cytokine-stimulation responses per immune cell type and (ii) submit a gene list to receive predictions of the key driver cytokines of an immune process within minutes — no local install or coding required.

## Method

- **Web application** hosting the Immune Dictionary perturbational scRNA-seq atlas, optimized for browsing perturbational single-cell data.
- **IREA inference engine** exposed through the browser: gene-list input → enrichment-based cytokine-driver predictions against the Dictionary's per-cell-type response signatures and polarization states.
- **Recent updates**: accelerated graph displays, expanded network analysis, added coverage of immunostimulatory agents such as **chemokines** (beyond the original 86 cytokines), and comprehensive per-function user instructions.
- Conference abstract (AAI 2025); no new wet-lab experiments — the contribution is the portal/software deployment over the previously published atlas.

## Results

- A freely available web portal hosting the Immune Dictionary (>17 cell types × 86 cytokines, mouse lymph node in vivo) and IREA.
- Gene-list-to-driver-cytokine predictions returned "within minutes."
- Interactive exploratory visualization of cytokine-stimulation responses per major immune cell type.
- Portal extended with accelerated graphs, expanded network analysis, chemokine coverage, and user documentation.

## All claims (exhaustive)

- `[c01]` IREA web portal freely hosts the Immune Dictionary atlas + companion software (p.1008) "we created a web application that hosts our Immune Dictionary ... and its companion software, Immune Response Enrichment Analysis (IREA)" — confidence: medium — type: methodological — links: [[foundations/irea-immune-response-enrichment-analysis-software]] [[foundations/immune-dictionary-dataset]] [[claims/irea-web-portal-freely-hosts-immune]]
- `[c02]` Gene list → key driver cytokine predictions within minutes (p.1008) "researchers can easily enter a list of genes involved in an immune process, and the IREA web portal will provide the predictions of key cytokines driving the immune process within minutes" — confidence: medium — type: methodological — links: [[foundations/irea-immune-response-enrichment-analysis-software]] [[concepts/cytokine-mediated-immune-cell-cell-interactome]] [[claims/irea-web-portal-predicts-key-driver]]
- `[c03]` Web app enables exploratory visualization of cytokine response per immune cell type (p.1008) "Our web application allows for exploratory visualization of cytokine stimulation response in each major immune cell type and is optimized for browsing perturbational single-cell RNA-sequencing data" — confidence: medium — type: methodological — links: [[foundations/cytokine-perturbation-scrna-seq-vivo-lymph]] [[concepts/cytokine-cell-type-specific-response-pleiotropy]] [[claims/immune-dictionary-web-application-enables-exploratory]]
- `[c04]` Recent portal updates add accelerated graphs, expanded network analysis, chemokine coverage, user instructions (p.1008) "Recent updates to the web portal include accelerated graph displays, expanded network analysis, additional coverage of immunostimulatory agents such as chemokines, and comprehensive user instructions" — confidence: medium — type: methodological — links: [[foundations/irea-immune-response-enrichment-analysis-software]] [[claims/irea-web-portal-updates-add-accelerated]]
- `[c05]` IREA assesses cytokine activities and immune cell polarization from gene expression data, addressing the limited-tooling gap (p.1008) "software tools for inferring cytokine activities based on RNA-seq data have been limited. To address this gap ... IREA, that allows assessment of cytokine activities and immune cell polarization from gene expression data" — confidence: high — type: methodological — links: [[foundations/irea-immune-response-enrichment-analysis-software]] [[claims/irea-enables-inference-cytokine-activities-cell]]

## Discussion captured

### Authors' interpretation

The authors frame the portal as evidence of "the power of big data in accelerating advancements in immunology and immunotherapies," positioning a freely-available, browser-based inference tool as the way to put a large perturbational atlas into the hands of bench immunologists.

### Comparisons with prior literature (made by authors)

- Builds directly on the original Immune Dictionary / IREA work (Cui, Hacohen et al., *Nature* 2024) — this abstract is its web-portal companion. No other literature is cited in the abstract.

### Mechanistic hypotheses proposed

- None (tool/resource abstract; no new mechanistic claims).

### Caveats and self-criticism

- None explicitly stated in the abstract.

### Future directions suggested

- Implied continued portal development (the abstract emphasizes ongoing updates: faster graphs, expanded networks, broader agent coverage such as chemokines).

## Limitations

- Conference abstract only — no methods detail, benchmarking, or quantitative validation of the portal's predictions.
- Underlying atlas inherits all limitations of the source paper: mouse-only, single tissue (skin-draining lymph node), single 4-h timepoint, single-cytokine perturbations, supraphysiological doses.
- "Within minutes" and "expanded network analysis" are unquantified.
- Chemokine coverage is announced but not enumerated.

## Open questions

### Open questions raised by authors

- None explicitly posed in the abstract.

### Open questions identified during ingest

- How accurate are the portal's gene-list-driven cytokine-driver predictions on independent benchmark datasets?
- Does the added chemokine coverage use the same in vivo lymph-node perturbation design, or imported signatures?
- Can the portal be applied to hypoxic tumour scRNA-seq to infer active cytokine networks (HypoxiaVERSE relevance)?
- Is there a human-Dictionary equivalent in the portal, or only the mouse reference?

## My take

This is a tool/resource abstract, not a new scientific result — its value to the wiki is recording that the Immune Dictionary + IREA are now usable as an interactive web service with chemokine coverage and network-analysis upgrades beyond the 2024 *Nature* release. For my own work, the practical takeaway is that IREA cytokine-driver inference is available without local installation: I can feed TAM/NK gene signatures from hypoxic-vs-normoxic tumour data directly into the portal. The science is entirely inherited from [[papers/dictionary-immune-responses-cytokines-single-cell]]; treat this as the canonical pointer to the deployed tool.

## Related

- [[papers/dictionary-immune-responses-cytokines-single-cell]] — the original *Nature* 2024 atlas paper this abstract deploys as a web portal; this paper builds_on it.
- [[foundations/irea-immune-response-enrichment-analysis-software]], [[foundations/immune-dictionary-dataset]], [[foundations/cytokine-perturbation-scrna-seq-vivo-lymph]] — the software, dataset, and perturbation-design foundations exposed by the portal.
- [[concepts/cytokine-mediated-immune-cell-cell-interactome]], [[concepts/cytokine-cell-type-specific-response-pleiotropy]] — the science the portal makes queryable.
- [[papers/single-cell-cytokine-dictionary-human-peripheral]] — human PBMC counterpart of the Immune Dictionary.
- [[papers/pairwise-cytokine-code-explains-organism-wide]] — complementary in vivo cytokine-perturbation axis.
