---
# === Identification ===
title: "Pseudodynamics+: Reconstructing Population Dynamics from Time-Resolved Single Cell Landscapes with Physics Informed Neural Networks"
slug: pseudodynamics-reconstructing-population-dynamics-time-resolved
arxiv: ""
doi: "10.64898/2025.11.30.691399"
pmid: ""
venue: "bioRxiv"
year: 2025
authors:
  - Weizhong Zheng
  - Melania Barile
  - Nicola K. Wilson
  - Yuanhua Huang
  - Fabian J. Theis
  - Berthold Göttgens
first_author: "Weizhong Zheng"
corresponding_author: "Berthold Göttgens"

# === Source & metadata ===
source_type: pdf
s2_id: "95b49b6e2ad6909ad317a3e9626159780f51cfea"
date_added: 2026-06-03
ingested_date: 2026-06-03
ingest_version: 1
last_reviewed:

# === Classification ===
importance: 4
tier: TIER_1
tags:
  - single-cell
  - trajectory-inference
  - population-dynamics
  - physics-informed-neural-network
  - neural-ode
  - haematopoiesis
  - thymocyte-development
  - cell-flux
  - lineage-tracing
  - megakaryocyte
  - methods
keywords:
  - pseudodynamics
  - PINN
  - advection-reaction-diffusion PDE
  - continuous density transport
  - LARRY barcoding
  - diffusion map
  - growth differentiation diffusion rates
domain: "methods / single-cell genomics / haematopoiesis"

# === Biomedical domain ===
tissue: [bone_marrow, multi]
condition: [healthy]
disease_specific: []
species: [mouse]
hypoxia_relevant: false
contains_immune_cells: true
contains_myeloid: true

# === Technique ===
techniques: [scRNA-seq_10x, lineage_tracing]
n_samples:
n_cells_total: 48000
integration_method: ""

# === Biology captured ===
key_cell_types:
  - haematopoietic stem cell (HSC)
  - megakaryocyte-erythroid progenitor (MEP)
  - megakaryocyte progenitor
  - erythroid progenitor
  - neutrophil progenitor
  - vWF+ MK-biased HSC
  - thymocyte (DN/DP)
  - non-canonical lymphoid (NCL) cell
key_markers:
  - Vwf
  - Pf4
  - Gata1
  - Klf1
  - Cebpa
  - Cebpe
  - Nupr1
  - Mecom
key_pathways:
  - haematopoietic differentiation
  - T-cell maturation / beta-selection
  - megakaryocyte lineage commitment

# === User project membership ===
projects: [methods]
priority: reference
read_status: not_read

# === HypoxiaVERSE-specific ===
hypoxiaverse_status:
exclusion_reason:
data_availability: "Reuses published datasets: Kernfeld et al. 2018 (thymus), Weinreb et al. 2020 (LARRY), Kucinski et al. 2024 (in vivo persistent-labelling haematopoiesis)"

# === Cross-references ===
code_url: "https://github.com/Gottgens-lab/pseudodynamics_plus"
cited_by: []
---

## Problem

Time-series single-cell sequencing resolves developmental landscapes at deep molecular resolution, but turning these snapshots into tissue-scale dynamics is hard for two reasons. First, sequencing is destructive, so trajectory information connecting transiting cell states is lost. Second, captured cells do not reflect actual cell numbers in the tissue, especially in rapidly growing systems — so snapshots lose information about expansion/contraction of the whole population. Crucially, existing trajectory methods (optimal transport, generative/flow-matching models, dynamic OT) neglect total population size, which can lead to misinterpreting changes in proliferation or death as changes in cellular migration. The original `pseudodynamics-v1` (Fischer et al. 2019) integrated population size with single-cell omics but reduced gene expression to a 1D pseudotime axis, making it unable to resolve complex multi-branch landscapes (cells at identical pseudotime across divergent trajectories are indistinguishable).

## Key idea

`pseudodynamics+` is a physics-informed neural network (PINN) framework that solves the governing advection-reaction-diffusion PDE for single-cell density on complex, branching, high-dimensional landscapes **without** pseudotime discretization. By jointly modelling single-cell density `u(s,t)` (whose integral over state space equals the measured total population size `Nt`) and parameterizing three behaviour functions — net proliferation `g(s,t)`, drift/differentiation velocity `v(s,t)`, and diffusion `D(s,t)` — with neural networks, it estimates time- and state-resolved dynamic parameters at single-cell resolution. This bridges single-cell genomics with population-scale cell-flux modelling.

## Method

- **Governing PDE** (advection-reaction-diffusion): `∂u/∂t = g(s,t)u − ∇s(v(s,t)u) + ∇s(D(s,t)∇s u)` — growth, drift, diffusion terms. `s` is a `d`-dimensional cell-state vector (diffusion-map coordinates); `u(s,t)` is an unnormalized density scaled so `Nt = ∫ u(s,t) ds`.
- **PINN surrogate network** `uθ(s,t)` approximates the density and supplies first/second-order spatial derivatives via autograd; three **behaviour MLPs** (`gw`, `vw`, `Dw`) parameterize the dynamic rates. The inverse problem is solving for the behaviour-network parameters.
- **Losses** (Eq. 8): forward density loss `Lθ`, PDE residual loss `Lr`, NeuralODE simulation loss `Lsim` (integrating the RHS of the PDE between observed timepoints), plus regularizers — diffusion penalty `LD`, velocity-direction cosine loss `Lv` (aligns `v` with local data geometry / RNA velocity or kNN), and growth-matching loss `Lgrowth`. `λgrowth = 0` encodes an **open system** allowing outflux to unobserved states.
- **Density estimation**: diffusion-map (palantir) coordinates + scipy Gaussian KDE per timepoint, rescaled to the observed `Nt`.
- **Defaults**: `λD=1, λv=0.01, λgrowth=0`; Adam lr 3e-4; Dopri5 NeuralODE solver, tol 1e-4 (Rk4 fixed-step fallback on underflow).
- **Downstream**: timepoint imputation; deterministic/stochastic trajectory simulation via the velocity field; a **drift-association gene test** (DE within the steepest-differentiation-rate pseudotime window + trajectory correlation); and **continuous density transport (CDT)**, which combines `v`, `g`, `D` to quantify stepwise density redistribution from a cell to its progenies.

## Results

- **Density-estimation benchmark** (megakaryocyte differentiation, Kucinski 2024): diffusion-map + Gaussian KDE best matched the pseudotime ground truth; TIGON's GMM estimator had high correlation but failed to recover Day-3 stem accumulation / Day-7 progenitor transition.
- **Synthetic 5D data**: accurately recovered the increasing growth-rate trend; differentiation rate recovered at average Pearson **0.81**.
- **Thymocyte maturation** (Kernfeld 2018, ~48k cells, E12.5–E19.5): recovered rapid thymocyte expansion; identified **three** proliferative bursts (progenitor, Phase 2, DP) vs only two for v1; the DP wave is validated by high G2M fraction in DP cells. Open-system soft boundary let DP cells keep differentiating downstream (v1 forced zero-drift at the boundary).
- **LARRY benchmark** (Weinreb 2020): fate-prediction accuracy comparable to SOTA flow-matching (OT-CFM, SF2M) and better than dynamic-OT methods (TrajectoryNet, MIOFlow, TIGON); Wasserstein-2 trajectory accuracy competitive with flow-matching (surpassed by PRESCIENT and MIOFlow on W2). Dynamic-OT methods underperformed at fate prediction.
- **In vivo persistent-labelling haematopoiesis** (Kucinski 2024, tdTomato, 3–269 days): **time-dependent** parameters needed (static-rate models fail over 9 months); training KLD 0.136, held-out timepoint (Day 49, 161) imputation KLD **0.097**. Megakaryocyte/erythroid lineages show coupled growth+differentiation; neutrophil lineage decoupled. Drift-association test recovered canonical regulators (Pf4/Gata1 Mk, Klf1/Gata1 Ery, Cebpa/Cebpe Neu).
- **Temporal lineage shift**: relative differentiation rates stabilize after Day 76; the system shifts from early megakaryocyte-biased to balanced homeostatic output. vWF+ MK-biased HSCs enriched Day 3–12 then decline; early-phase vWF+ HSCs score higher in an alternative-MK / vWF+ P-HSC signature (max p=0.00735, Mann–Whitney U). Time-independent models wrongly assign high growth to HSCs (incompatible with known quiescence).
- **CDT of MEPs**: transient Mk bias (Day 12–27) giving way to balanced Ery–Mk output from Day 49; early MEPs score higher in a low-output signature, late MEPs in a multi-lineage signature.

## All claims (exhaustive)

- `[c01]` pseudodynamics+ solves the single-cell advection-reaction-diffusion PDE on high-dimensional branching landscapes without pseudotime discretization, using a PINN surrogate plus three behaviour networks (p.2-4, "a physics-informed neural network architecture that solves the governing partial differential equation (PDE) system without discretization, enabling joint estimation of time- and state-resolved parameters") — confidence: high — type: methodological — links: [[concepts/population-aware-single-cell-flux-modeling]] [[foundations/physics-informed-neural-network]] [[foundations/neural-ordinary-differential-equation]] [[claims/pseudodynamics-solves-single-cell-advection-reaction]]
- `[c02]` Single-cell snapshot trajectories confound cell flux with changes in overall population size, so proliferation/death changes can be misread as migration (p.1, "the observed trajectories are confounded by changes in overall population size. This ambiguity can lead to misinterpreting changes in proliferation or death rates as changes in cellular migration") — confidence: high — type: mechanistic — links: [[concepts/population-size-confounds-snapshot-trajectory-flux]] [[claims/single-cell-snapshot-trajectories-confound-cell]]
- `[c03]` Diffusion-map coordinates coupled with traditional Gaussian KDE best recapitulate the pseudotime-based density ground truth, outperforming TIGON GMM, Mellon, Denmarf and hashing-KDE for capturing developmental stages (p.5, "we selected diffusion map coordinates coupled with traditional Gaussian KDE, as this combination yielded cell densities that best captured the distinct developmental stages") — confidence: high — type: methodological — links: [[foundations/diffusion-map-embedding]] [[foundations/gaussian-kernel-density-estimation]] [[claims/diffusion-map-coordinates-gaussian-kde-best]]
- `[c04]` On synthetic five-dimensional time-series data with known ground truth, pseudodynamics+ recovered the differentiation rate at an average Pearson correlation of 0.81 (p.6, "achieving an average Pearson correlation of 0.81") — confidence: high — type: quantitative — links: [[claims/pseudodynamics-recovers-synthetic-differentiation-rate-pearson]]
- `[c05]` pseudodynamics+ identified three waves of proliferative bursts during thymocyte maturation (progenitor, Phase 2, DP), whereas pseudodynamics-v1 suggested only the first two (p.6-7, "Pseudodynamics+ also identified three waves of proliferative bursts... In contrast, pseudodynamics-v1 only suggested the first two waves") — confidence: high — type: correlational — links: [[concepts/time-dependent-flux-parameters-long-timecourse]] [[claims/pseudodynamics-identifies-three-proliferative-bursts-during]]
- `[c06]` The third (DP-cell) proliferative wave predicted by pseudodynamics+ is validated by a high G2M proportion of cycling DP cells in scRNA-seq cell-cycle scoring (p.7, "cell cycle phase prediction based on scRNA-seq analysis showed a high G2M proportion of cycling DP cells... thus validating the third wave of proliferative burst") — confidence: high — type: correlational — links: [[claims/dp-thymocyte-proliferative-wave-validated-high]]
- `[c07]` pseudodynamics+ uses an open-system assumption with a soft boundary (a penalty on mass outflow) rather than v1's closed system with enforced zero drift at the last bin, allowing DP cells to keep differentiating to unobserved downstream states (p.15-16, "our method only builds a soft boundary by applying a loss term that penalises the mass flowing out of the system... a soft boundary coupled with the open system assumption is intuitively more suitable") — confidence: high — type: methodological — links: [[concepts/population-aware-single-cell-flux-modeling]] [[claims/open-system-soft-boundary-assumption-allows]]
- `[c08]` On LARRY-barcoded in vitro haematopoiesis, pseudodynamics+ achieves cell-fate prediction accuracy comparable to the latest flow-matching models (OT-CFM, SF2M) and outperforms most existing methods (p.7-8, "pseudodynamics+ outperformed most existing methods and achieved comparable accuracy with the latest flow-matching models") — confidence: high — type: methodological — links: [[foundations/flow-matching-generative-modeling]] [[foundations/larry-lineage-barcoding]] [[claims/pseudodynamics-matches-flow-matching-fate-prediction]]
- `[c09]` Dynamic optimal-transport-based methods underperformed at cell-fate prediction, possibly because their primary goal is reconstructing density changes rather than predicting cell state (p.7, "dynamic optimal transport-based methods underperformed, possibly due to their primary goal of reconstructing density changes rather than predicting cell state") — confidence: medium — type: correlational — links: [[foundations/optimal-transport-sinkhorn]] [[claims/dynamic-optimal-transport-methods-underperform-cell]]
- `[c10]` Modelling 9-month in vivo haematopoiesis required extending static-rate models to time-sensitive dynamic parameters; fixed-parameter models do not fit the data well (p.8-9 & p.16, "the static-rate setting adapted by previous studies needed to be extended to incorporate the modelling of time-sensitive dynamic parameters, which provided a good fit") — confidence: high — type: methodological — links: [[concepts/time-dependent-flux-parameters-long-timecourse]] [[claims/time-dependent-flux-parameters-required-fit]]
- `[c11]` pseudodynamics+ accurately imputed cell-type density for two held-out timepoints (Day 49 and 161) with average KLD 0.097 (training KLD 0.136) (p.9-10, "average KLD = 0.136 for seen training timepoints... average KLD = 0.097") — confidence: high — type: quantitative — links: [[claims/pseudodynamics-imputes-held-out-haematopoiesis-timepoints]]
- `[c12]` The megakaryocyte and erythroid lineages exhibit coupled growth and differentiation rates, whereas the neutrophil lineage shows a decoupled growth/differentiation pattern (p.10-11, "The Megakaryocyte and Erythroid lineage exhibited coupled growth and differentiation rates... the Neutrophil lineage demonstrated a decoupled differentiation and growth rate pattern") — confidence: medium — type: mechanistic — links: [[claims/megakaryocyte-erythroid-lineages-show-coupled-growth]]
- `[c13]` The drift-association test recovered canonical lineage regulators across all three lineages: Pf4/Gata1 (Mk), Klf1/Gata1 (Ery), Cebpe/Cebpa (Neu) (p.10-11, "This approach recovered canonical lineage regulators across all three lineages... Pf4 and Gata1 for Megakaryocytes... Klf1 and Gata1 for Erythocytes... Cebpe and Cebpa for Neutrophils") — confidence: high — type: methodological — links: [[concepts/drift-association-gene-discovery-test]] [[foundations/platelet-factor-pf4]] [[claims/drift-association-test-recovers-canonical-haematopoietic]]
- `[c14]` Over the time course the system shifts from quick megakaryocyte-biased haematopoiesis to slow balanced homeostatic haematopoiesis, with relative differentiation rates stabilizing after Day 76 (p.11-12, "the transition from quick megakaryocytic biased haematopoiesis to slow homeostatic haematopoiesis over time... relative differentiation rates remained stable after Day 76") — confidence: medium — type: mechanistic — links: [[concepts/megakaryocyte-biased-balanced-haematopoiesis-temporal-shift]] [[claims/haematopoiesis-shifts-early-megakaryocyte-biased-balanced]]
- `[c15]` A vWF+ megakaryocyte-restricted HSC subgroup is enriched from Day 3 to Day 12 and declines over time, scoring higher in an alternative-MK / vWF+ P-HSC signature during the early phase (max p=0.00735, Mann–Whitney U) (p.11, "a recently identified HSC subgroup restricted to produce megakaryocyte (vWF+ HSCs) was detected from Day 3 to Day 12... significantly higher expression in our early-phase vWF+ HSCs (max p-value = 0.00735)") — confidence: medium — type: correlational — links: [[concepts/vwf-hsc-fast-megakaryocyte-differentiation-pathway]] [[foundations/von-willebrand-factor-vwf]] [[claims/vwf-megakaryocyte-biased-hscs-enriched-early]]
- `[c16]` Continuous density transport (CDT) combines the learned velocity, growth and diffusion to quantify stepwise redistribution of a cell's density among its progenies along the differentiation trajectory, yielding a per-cell transport map (p.11-12, "continuous density transport (CDT), allowing us to quantify how a cellular density redistribute stepwise among its progenies along the differentiation trajectory") — confidence: high — type: methodological — links: [[concepts/continuous-density-transport]] [[claims/continuous-density-transport-quantifies-stepwise-progeny]]
- `[c17]` CDT of MEPs reveals a transient megakaryocyte bias between Day 12 and Day 27 that gives way to balanced erythrocyte–megakaryocyte output from Day 49 onwards (p.13, "Between Day 12 and Day 27, MEPs acquired a transient megakaryocyte bias, which subsequently gave way to a balanced erythrocyte–megakaryocyte output from Day 49 onwards") — confidence: medium — type: correlational — links: [[concepts/continuous-density-transport]] [[claims/meps-show-transient-megakaryocyte-bias-giving]]
- `[c18]` Time-independent models incorrectly assign high growth rates to HSCs (incompatible with their known quiescence and low cell-cycle scores), whereas the time-dependent pseudodynamics+ predicts HSCs divide rarely (p.11, "pseudodynamics+ predicts that HSCs divide rarely, whereas time-independent model assigned high growth rates to HSCs... incompatible with their known quiescence") — confidence: high — type: correlational — links: [[concepts/time-dependent-flux-parameters-long-timecourse]] [[claims/time-independent-models-wrongly-assign-high]]

## Discussion captured

### Authors' interpretation

The authors frame pseudodynamics+ as a "step-change" in capturing population dynamics for complex multi-lineage landscapes at single-cell resolution, arguing that joining single-cell genomics with population-scale flux modelling yields insight neither approach gives alone. They stress that population-scale flux dynamics are what is perturbed in disease and what must be rectified to treat it, positioning the method as a route to therapeutic intervention. The drift-association test is presented as a novel gene-programme discovery method leveraging previously unused population/tissue-scale parameters.

### Comparisons with prior literature (made by authors)

- vs **pseudodynamics-v1** (Fischer et al. 2019): v1 uses a 1D pseudotime coordinate with an enforced closed system (zero drift at the last bin); pseudodynamics+ uses multi-dimensional diffusion-map space and a soft open boundary. The high DP growth rate disagrees with v1 but matches cell-cycle phase.
- Early MK-biased proliferation aligns with Upadhaya et al. 2018 (MK progenitors outpace other progenitors first week post-tamoxifen) and Kucinski et al. 2024 (>50% expansion of MEP/MkP-like progenitors).
- vWF+ MK-biased fast HSC pathway: Sanjuan-Pla et al. 2013, Haas et al. 2015, Carrelha et al. 2018/2024.
- Fast-engrafting MK/Ery-biased vs slow myeloid/lymphoid HSC clones (HSC transplant study; Laurenti & Göttgens 2018).
- Low-output vs multi-lineage HSC signatures from Rodriguez-Fraticelli et al. 2020.

### Mechanistic hypotheses proposed

- Early faster MK differentiation reflects HSC heterogeneity at homeostasis: a small subset of rapidly differentiating MK-biased (vWF+) HSCs dominates early output, followed by delayed contribution from slower unbiased HSCs — a temporal shift of HSC subtypes propagating downstream to progenitors.
- Large early variation in dynamic parameters may stem from (i) tamoxifen perturbation (suggested to inhibit JAK-STAT signalling; Sánchez-Aguilera 2014) and/or (ii) HSC-pool kinetic heterogeneity.

### Caveats and self-criticism

- The optimal strength of the soft-boundary constraint can only be determined retrospectively.
- Using diffusion-map coordinates (not gene expression) as input means there is no explicit mapping from gene expression to dynamic rates, so per-gene contributions to flux cannot be directly quantified; gradient-based attribution is noise-sensitive.
- Drift-associated genes represent associations that may or may not have regulatory causality.
- Disentangling tamoxifen effects from genuine HSC heterogeneity will require new experimental approaches.

### Future directions suggested

- Beyond haematopoiesis, a generalizable approach for any dynamic system where both state transitions and population flux matter (regenerative biology, disease progression, therapeutic intervention).
- Reversible dimensionality reduction to link gene expression to dynamic rates (noting current attribution limitations).

## Limitations

- Input is diffusion-map coordinates, not raw gene expression — limits direct gene-level interpretability of inferred rates.
- Density estimation is hard in high dimensions; the method depends on a good low-dimensional manifold and KDE quality.
- Soft-boundary strength and several `λ` hyperparameters require tuning; the open-system choice is dataset-dependent.
- Validation is on three previously published datasets (mouse only); no new wet-lab perturbation validates the inferred parameters.
- It is a bioRxiv preprint (not peer reviewed; 0 citations at ingest).

## Open questions

### Open questions raised by authors

- How to separate tamoxifen-induced perturbation from intrinsic HSC kinetic heterogeneity in the early time window.
- How to recover per-gene contributions to flux parameters given the diffusion-map input.
- Whether drift-associated genes are causal regulators or mere correlates.

### Open questions identified during ingest

- How robust are the inferred time-dependent rates to the choice of density estimator and diffusion-map dimensionality?
- Does the open-system assumption generalize to systems with strong influx (not just outflux)?
- How does CDT compare quantitatively to optimal-transport coupling maps on the same data?

## My take

A genuinely novel methods contribution: solving the population-aware single-cell flux PDE on branching landscapes with a PINN, avoiding the pseudotime bottleneck of pseudodynamics-v1, and adding time-dependent rates that matter over long in vivo time courses. The Göttgens × Theis pairing is strong, the benchmarks are honest (it ties, not dominates, flow-matching on LARRY), and CDT plus the MK→balanced HSC-output shift is a nice biological payoff. Main caveat is interpretability (diffusion-map input) and that all validation is computational on reused mouse datasets. Relevant to the wiki as a population-dynamics counterpart to RNA-velocity / CellRank-style fate mapping.

## Related

- [[concepts/population-aware-single-cell-flux-modeling]]
- [[concepts/continuous-density-transport]]
- [[concepts/population-size-confounds-snapshot-trajectory-flux]]
- [[concepts/drift-association-gene-discovery-test]]
- [[concepts/time-dependent-flux-parameters-long-timecourse]]
- [[concepts/megakaryocyte-biased-balanced-haematopoiesis-temporal-shift]]
- [[concepts/vwf-hsc-fast-megakaryocyte-differentiation-pathway]]
- [[foundations/physics-informed-neural-network]]
- [[foundations/neural-ordinary-differential-equation]]
- [[foundations/diffusion-map-embedding]]
- [[foundations/larry-lineage-barcoding]]
- [[foundations/gaussian-kernel-density-estimation]]
- [[foundations/waddington-ot]]
- [[foundations/moscot-multi-omic-optimal-transport]]
- [[foundations/prescient-population-dynamics-model]]
- [[foundations/tigon-dynamic-unbalanced-optimal-transport]]
- [[foundations/von-willebrand-factor-vwf]]
- [[foundations/platelet-factor-pf4]]
- [[foundations/optimal-transport-sinkhorn]]
- [[foundations/flow-matching-generative-modeling]]
- [[foundations/cellrank-fate-mapping]]
- [[foundations/palantir-pseudotime-fate]]
- [[foundations/pseudotime-trajectory-inference]]
- [[foundations/rna-velocity]]
- [[foundations/scanpy]]
- [[foundations/scrna-seq-10x-chromium]]
- [[foundations/cre-loxp-recombinase-system]]
- [[papers/cellrank-consistent-data-view-agnostic-fate]] — builds_on: uses CellRank's velocity kernel for MEP fate probabilities
- [[people/fabian-theis]]
- [[people/weizhong-zheng]]
- [[people/berthold-gottgens]]
