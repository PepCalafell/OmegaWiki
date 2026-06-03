---
title: "Kinobeads chemoproteomic selectivity profiling (and CATDS score)"
slug: kinobeads-chemoproteomic-selectivity-profiling
domain: "chemoproteomics / drug profiling / methods"
status: mainstream
aliases:
  - "kinobeads"
  - "CATDS"
  - "concentration and target-dependent score"
  - "kinobeads competition assay"
first_introduced: "Bantscheff et al. 2007 *Nat Biotechnol*; Klaeger et al. 2017 *Science* (kinobeads + CATDS)"
date_updated: 2026-06-03
source_url: "https://doi.org/10.1126/science.aan4368"
---

## Definition

Kinobeads are immobilized broad-spectrum ATP-competitive ligands (kinase-inhibitor-coated beads) used to pull endogenous kinases out of cell lysates. By measuring, via quantitative mass spectrometry, how much a free kinase inhibitor competitively displaces each captured kinase across a concentration range, kinobeads assays yield EC50/Kd-like binding affinities for many kinases simultaneously. The CATDS (concentration- and target-dependent selectivity) score derived from these data expresses, at a given inhibitor concentration, the reduction in binding of one target kinase divided by the total reduction across all targets — ranging 0 (no selectivity) to 1 (single-target selectivity).

## Intuition

Kinobeads measure binding to endogenously expressed kinases (not recombinant domains) and integrate both intrinsic inhibitor affinity and target affinity for ATP. CATDS turns the multi-target binding curves into a single interpretable selectivity number per kinase.

## Formal notation

- Output per inhibitor: dose-resolved binding (apparent EC50/Kd) for each captured kinase.
- CATDS_target = Δbinding(target) / Σ Δbinding(all targets), at a chosen concentration; ∈ [0, 1].
- Reference dataset: Klaeger et al. 2017 profiled 243 clinical kinase inhibitors against ~253/518 human kinases.

## Key variants

- Multiplexed kinobeads (mixture of several immobilized broad inhibitors to widen kinome coverage).
- Biotin-labeled probe chemoproteomics on lysates (Patricelli et al. 2011) — conceptually similar.

## Known limitations

- Only a partial fraction of the kinome is capturable (~253/518 in Klaeger et al.); low-abundance kinases evade detection.
- Pure in-vitro binding assay on lysates: predicts binding, not necessarily cellular functional consequence.
- Reliance on a single reference dataset can propagate measurement bias.
- Captures ATP-binding non-kinase enzymes too (e.g., NQO2, TOP2B, ACOX3).

## Open problems

- Bridging in-vitro binding selectivity to in-cell functional effect remains unsolved.
- Extending coverage to the undruggable/undetectable kinome fraction.

## Relevance to active research

[[papers/integrative-epigenome-based-strategy-unbiased-functional]] selects its 58 CKIs and their working concentrations from Klaeger et al. kinobeads/CATDS data, then shows that kinobeads target assignment outperforms clinical labels for predicting epigenomic similarity yet still fails to explain the full spectrum of cellular effects — motivating an orthogonal epigenome-based functional readout.
