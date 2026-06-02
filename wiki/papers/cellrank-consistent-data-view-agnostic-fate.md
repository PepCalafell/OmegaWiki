---
# === Identification ===
title: "CellRank: consistent and data view agnostic fate mapping for single-cell genomics"
slug: cellrank-consistent-data-view-agnostic-fate
arxiv: ""
doi: "10.1038/s41596-025-01314-w"
pmid: "41611959"
venue: "Nature Protocols"
year: 2026
authors:
  - Philipp Weiler
  - Fabian J. Theis
first_author: "Philipp Weiler"
corresponding_author: "Fabian J. Theis"

# === Source & metadata ===
source_type: pdf
s2_id: "93d0280661db4f41f512496a138f60f5b5a0f1e3"
date_added: 2026-06-02
ingested_date: 2026-06-02
ingest_version: 1
last_reviewed:

# === Classification ===
importance: 3
tier: TIER_2
tags:
  - trajectory-inference
  - single-cell
  - RNA-velocity
  - pseudotime
  - fate-mapping
  - methods-protocol
keywords:
  - CellRank
  - cellular fate mapping
  - Markov chain
  - GPCCA
  - kernels
  - macrostates
  - lineage drivers
domain: "methods"

# === Biomedical domain ===
tissue: [bone_marrow, multi]
condition: [healthy]
disease_specific: []
species: [human, mouse]
hypoxia_relevant: false
contains_immune_cells: true
contains_myeloid: true

# === Technique ===
techniques: [scRNA-seq_10x]
n_samples:
n_cells_total:
integration_method: ""

# === Biology captured ===
key_cell_types:
  - HSC
  - MEP
  - erythroid
  - monocyte
  - pre-DC
  - cDC
  - pDC
  - CLP
  - HMP
key_markers:
  - ITGA2B
  - VWF
  - CD34
  - PF4
  - HBD
key_pathways: []

# === User project membership ===
projects: [methods]
priority: reference
read_status: not_read

# === HypoxiaVERSE-specific ===
hypoxiaverse_status:
exclusion_reason:
data_availability: "Figshare 10.6084/m9.figshare.c.7752290.v1; code github.com/theislab/cellrank (Zenodo 10.5281/zenodo.10210196)"

# === Cross-references ===
code_url: "https://github.com/theislab/cellrank"
cited_by: []
---

## Problem

Single-cell RNA sequencing is destructive, so cellular differentiation trajectories must be reconstructed computationally from static snapshots. Existing trajectory-inference methods are tied to a single data type (pseudotime, or RNA velocity, or optimal transport) and do not generalize to newly emerging data views, nor do most describe the long-term behavior of individual cells. Integrating orthogonal information typically requires designing bespoke methods, which slows analysis and makes results hard to compare.

## Key idea

CellRank is a **data-view-agnostic** framework for cellular fate mapping. Any source of directional information about cellular change (RNA velocity, pseudotime, stemness, experimental time, lineage tracing) is converted by a *kernel* into a cell–cell transition matrix; the induced Markov chain is analyzed by an *estimator* to infer terminal states and per-cell fate probabilities; *downstream tools* then rank lineage drivers and compare models. CellRank 2 generalizes the original RNA-velocity-only framework to combine complementary views and scale to atlas-sized data.

## Method

Three modular stages (Fig. 1):

1. **Kernels** compute cell–cell transition probabilities from a data view. Five kernels: `VelocityKernel` (RNA velocity), `ConnectivityKernel` (similarity), `PseudotimeKernel` (biases the similarity graph toward increasing pseudotime), `CytoTRACEKernel` (stemness potential), `RealTimeKernel` (OT across experimental time points), plus a `PrecomputedKernel`. Multiple kernels can be combined as a weighted average of their transition matrices.
2. **Estimators** analyze the resulting Markov chain. The default GPCCA estimator coarse-grains the transition matrix via a Schur decomposition into macrostates, from which terminal states (auto or manual) and fate probabilities are derived.
3. **Downstream analysis**: putative lineage drivers (GEX–fate-probability correlation), lineage-weighted generalized additive models of GEX over pseudotime, and the TSI (terminal-state identification) and CBC (cross-boundary correctness) scores for model selection.

The protocol runs four procedures: (1) CytoTRACEKernel and (2) PseudotimeKernel on CD34+ human bone marrow; (3) VelocityKernel (+ kernel combination) on spermatogenesis; (4) RealTimeKernel on time-resolved murine bone marrow.

## Results

- On CD34+ human bone marrow (6,881 cells), GPCCA recovered hematopoietic macrostates and terminal states (Ery, MEP, monocyte, DC subsets); the CytoTRACEKernel reached TSI = 0.85 vs an optimal 1.0.
- The PseudotimeKernel recapitulated known state transitions better than the CytoTRACEKernel on this dataset (positive CBC log-ratios; Welch's t-test).
- Driver ranking recovered ITGA2B/VWF as MEP/megakaryocyte-lineage genes, and flagged a substate biased toward the non-observed megakaryocyte state.
- Reported runtimes are seconds-to-minutes on a laptop (e.g. OT couplings 39 s for Procedure 4), demonstrating scalability.

## All claims (exhaustive)

- `[c01]` CellRank decomposes fate mapping into kernels, estimators and analysis tools (p.2-4) "The CellRank framework naturally divides itself into three parts: kernels … estimators … and analysis tools." — confidence: high — type: methodological — links: [[claims/cellrank-decomposes-trajectory-inference-into-kernels]] [[cellrank-fate-mapping]]
- `[c02]` CellRank 2 generalizes fate mapping to a data-view-agnostic, multiview framework (abstract, p.2) "CellRank 2 generalizes CellRank's trajectory inference framework to multiview single-cell data." — confidence: high — type: methodological — links: [[claims/cellrank-generalizes-fate-mapping-data-view]] [[cellrank-fate-mapping]]
- `[c03]` GPCCA coarse-grains the cell–cell Markov chain into macrostates, terminal states and fate probabilities (p.3-4) "our generalized Perron cluster cluster analysis (GPCCA) estimator coarse grains the transition matrix … defining terminal states and fate probabilities." — confidence: high — type: methodological — links: [[claims/gpcca-estimator-coarse-grains-markov-chain]] [[gpcca-generalized-perron-cluster-cluster-analysis]] [[markov-chain-trajectory-model]]
- `[c04]` Combining multiple kernels improves terminal-state recovery and numerical stability (p.3) "Previous analyses benefited from this step in terms of correctly identifying all terminal states and numerical stability, as one view may regularize another." — confidence: medium — type: methodological — links: [[claims/combining-multiple-kernels-improves-terminal-state]] [[cellrank-fate-mapping]]
- `[c05]` TSI and CBC scores quantify terminal-state recovery and transition fidelity for model selection (p.4, p.25-26) "the terminal state identification (TSI) score … quantifies how faithfully a kernel-derived transition matrix recovers known terminal states … the cross-boundary correctness (CBC) quantifies how accurately the kernel aligns with known state transitions." — confidence: high — type: methodological — links: [[claims/tsi-cbc-scores-quantify-trajectory-inference]] [[cellrank-fate-mapping]]
- `[c06]` CellRank ranks putative lineage drivers by correlating GEX with fate probabilities (p.3-4, Fig.3f,g) "putative lineage drivers [are] genes whose GEX correlates with fate probabilities." — confidence: medium — type: methodological — links: [[claims/cellrank-identifies-putative-lineage-drivers-correlating]] [[cellrank-fate-mapping]]
- `[c07]` On CD34+ human bone marrow the PseudotimeKernel outperformed the CytoTRACEKernel in recapitulating known state transitions (p.7, Fig.2d) "highlighting the PseudotimeKernel outperforming the CytoTRACEKernel on this specific dataset"; CTK TSI = 0.85. — confidence: medium — type: quantitative — links: [[claims/pseudotimekernel-outperformed-cytotracekernel-human-bone-marrow]] [[pseudotime-trajectory-inference]] [[cytotrace-differentiation]]
- `[c08]` CellRank 1 results are compatible with CellRank 2 given unchanged dependencies (p.4) "the two versions will yield the same results as long as the analysis leaves all other Python packages unchanged." — confidence: high — type: methodological — links: [[claims/cellrank-results-compatible-cellrank]] [[cellrank-fate-mapping]]

## Discussion captured

### Authors' interpretation

The authors frame CellRank's value as decoupling fate inference from the source of directional information: by reducing every data view to a cell–cell transition matrix and a Markov chain, the same downstream machinery (GPCCA, fate probabilities, driver ranking, TSI/CBC) applies regardless of modality. They argue this modularity is what lets the framework absorb future data types (and external tools like moscot, moslin, EpiTrace built on top of it).

### Comparisons with prior literature (made by authors)

- **Palantir** (Setty 2019) — also Markov-chain-based, but defines terminal states as extrema of the stationary distribution / diffusion components, whereas CellRank uses GPCCA; CellRank "unifies pseudotime-based fate mapping by decoupling fate inference from pseudotime inference."
- **Slingshot** (Street 2018, BMC Genomics) — minimum-spanning-tree lineages.
- **Velocyto** (La Manno 2018, *Nature*) — first RNA velocity method; **Dynamo** (Qiu 2022, *Cell*) — vector-field/least-action-path drivers from metabolic labeling.
- **Waddington-OT** (Schiebinger 2019) — OT transport maps; CellRank adds intra-time-point information OT neglects.
- Foundational CellRank works cited: Lange et al. *Nat. Methods* 19:159-170 (2022); Weiler et al. *Nat. Methods* 21:1196-1205 (2024); Klein et al. *Nature* 638:1065-1075 (2025); Lange et al. *Genome Biol.* 25 (2024, moslin).

### Mechanistic hypotheses proposed

- A substate of existing clusters in the bone-marrow data is biased toward the non-observed megakaryocyte terminal state (a hypothesis generated by fate-probability analysis, Fig.3d–f).

### Caveats and self-criticism

- CellRank assigns fate probabilities but does not recover the most-probable *path*, limiting analysis of transcriptional convergence / non-tree-like differentiation.
- Driver identification is correlational, not causal.
- Kernel weighting in combinations is global; cell-specific weighting could be better.
- CellRank does not itself handle data sparsity/noise — it depends on upstream tools that produce its inputs.

### Future directions suggested

- Cell-specific kernel weighting; causal driver inference; recovering most-probable paths; calibrated uncertainty on fate probabilities; accommodating further emerging data views.

## Limitations

- Each kernel inherits its data view's limitations: RNA velocity (gene-structure bias, simplistic kinetics), pseudotime (root cell, unidirectionality), real-time (time-point spacing), and the Markov memorylessness assumption misses rare states and delayed effects.
- Absence of ground truth in single-cell data; TSI/CBC require prior knowledge.
- Macrostate decomposition is non-deterministic and the number of macrostates can be ambiguous.

## Open questions

### Open questions raised by authors

- How to weight kernel combinations cell-specifically rather than globally?
- How to infer most-probable paths and causal drivers, not just correlations?

### Open questions identified during ingest

- What predicts, a priori, which kernel performs best on a given dataset?
- How robust is fate inference to upstream dependency version drift (given the v1/v2 compatibility caveat)?

## My take

This is the consolidated, peer-reviewed how-to for the CellRank framework rather than a new method per se — the science (CellRank 1/2, GPCCA, the kernels) lives in the underlying *Nat. Methods*/*Nature* papers. Its value for the vault is as the canonical procedural reference and as a clean map of the trajectory-inference tool landscape (Palantir, Slingshot, Velocyto, Dynamo, Waddington-OT, moscot). Relevant if single-cell developmental/differentiation trajectories ever enter the thesis analysis stack.

## Related

- [[cellrank-fate-mapping]] — the framework this protocol documents (`derived_from`).
- [[rna-velocity]], [[pseudotime-trajectory-inference]], [[gpcca-generalized-perron-cluster-cluster-analysis]], [[markov-chain-trajectory-model]], [[anndata-annotated-data-structure]], [[palantir-pseudotime-fate]] — methods used/compared.
- [[scvelo-rna-velocity]], [[cytotrace-differentiation]], [[optimal-transport-sinkhorn]], [[dynamo-in-silico-perturbation]], [[scvi-deep-generative-model]] — related single-cell methods.
- [[papers/mapping-early-human-blood-cell-differentiation]] — applies the CellRank framework to human hematopoiesis (`similar_method_to`).
- People: [[people/philipp-weiler]], [[people/fabian-theis]].
