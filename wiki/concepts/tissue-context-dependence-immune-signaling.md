---
title: "Tissue context dependence of baseline immune-cell signaling"
aliases:
  - "tissue context dependence"
  - "ex vivo loss of immune signaling"
  - "context deprivation phenotype"
  - "niche-dependent immune cell identity"
  - "cell-extrinsic triggers of baseline signaling"
  - "in vivo tissue niche signaling"
  - "macrophage identity tissue dependence"
  - "ex vivo culture collapses cytokine signaling"
  - "tissue context-dependent JAK-STAT"
  - "homeostatic immune cell programming by niche"
  - "cell isolation artefact baseline signaling"
tags: [immunology, niche, macrophage-identity, jak-stat, ex-vivo, tissue-context]
maturity: active
key_papers:
  - jak-stat-signaling-maintains-homeostasis-cells
first_introduced: "2024"
date_updated: 2026-05-22
related_concepts: [tonic-baseline-jak-stat-homeostasis, isgf3-independent-irf9-function]
---

## Definition

The principle that the baseline transcriptional and chromatin state of unstimulated immune cells in vivo is **actively** maintained by cell-extrinsic signals from their tissue microenvironment, such that **removing the tissue context** (e.g. short-term ex vivo culture) causes rapid collapse of signaling pathways — JAK-STAT and IFN signatures in T cells and macrophages — and, in macrophages specifically, loss of cellular identity programs that are not rescued by single-ligand stimulation.

## Intuition

Tissue-resident immune cells are not "asleep waiting for a stimulus" — they are continuously listening to a chorus of niche signals. Pull them out of the tissue and the chorus stops; signaling collapses within hours. Type-I IFN can replace part of the chorus but not all of it, and macrophages additionally lose identity, suggesting tissue context maintains macrophage state through multiple parallel cues.

## Variants

- **T-cell context deprivation**: JAK-STAT/IFN signatures collapse; IFN-β stimulation largely restores them.
- **Macrophage context deprivation**: JAK-STAT/IFN collapses plus macrophage-identity collapse; neither M-CSF nor IFN-β rescues identity.
- **Sampling-handling artefacts (avoided)**: ex vivo handling can mimic context deprivation — using in situ formaldehyde perfusion + Visium / RNAscope rules this out.

## When to use

- Designing in vitro / ex vivo immune-cell experiments: predict and account for rapid collapse of baseline JAK-STAT/IFN signatures within hours.
- Interpreting bulk RNA-seq of sorted vs in-tissue immune cells — large ISG differences may reflect context loss, not real biology.
- Validating in vivo findings with tissue-preserved methods (perfusion fixation, spatial transcriptomics, in situ hybridization).

## Known limitations

- The specific cell-extrinsic ligand(s) and source cell(s) are not yet identified.
- Only spleen has been mapped; other tissues are untested.
- 20 h ex vivo timepoint is chosen — earlier timepoints (mins–hours) may already show collapse.

## Open problems

- Identify the source-cell + ligand pairs that maintain baseline JAK-STAT in each tissue.
- Determine whether reconstituting a single CellChat-nominated pair can rescue context-deprivation phenotypes.
- Quantify how much of the literature's "macrophage transcriptome" reflects ex vivo context loss.

## Key papers

- [[jak-stat-signaling-maintains-homeostasis-cells]] — Fortelny et al. 2024: ex vivo culture collapses JAK-STAT/IFN signatures in spleen T cells and macrophages; partial rescue by IFN-β; macrophage-identity loss is rescue-resistant.
