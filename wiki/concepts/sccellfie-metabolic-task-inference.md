---
title: "scCellFie — single-cell & spatial metabolic-task inference"
aliases:
  - scCellFie
tags:
  - single-cell
  - spatial-transcriptomics
  - metabolism
  - metabolic-task
  - GPR-rules
  - cell-cell-communication
  - endometrium
maturity: emerging
key_papers:
  - atlas-scale-metabolic-activities-inferred-single
first_introduced: "2025-05 (bioRxiv preprint)"
date_updated: 2026-05-27
related_concepts:
  - warburg-effect-hif1a-glycolytic-reprogramming
  - tryptophan-ido1-kynurenine-immunosuppression
---

## Definition

**scCellFie** is a Python framework that infers the activity of metabolic tasks (sets of reactions converting specific substrates into target products) from single-cell and spatial transcriptomics data. It extends the bulk-resolution CellFie method ([[metabolic-task-cellfie]]) to single-cell scale by combining gene-expression thresholding, GPR (gene–protein–reaction) rule evaluation, and task-level aggregation built on top of [[genome-scale-metabolic-model]] reconstructions (Human1, Mouse1).

## Intuition

Other tools either run pathway-enrichment (interpretable, blind to enzymes), flux-balance analysis (mechanistic, not scalable), or deep-learning regressors (scalable, opaque). scCellFie occupies the gap: per-reaction activity uses min-over-subunits / max-over-isoenzymes from GPR rules — capturing enzyme bottlenecks — and per-task scores aggregate reactions, yielding biochemically interpretable scores at single-cell or spatial-spot resolution that scale to ~30M cells.

## Formal notation

Three steps: (1) gene expression → gene scores via precomputed CELLxGENE-derived thresholds; (2) gene scores → reaction activities via GPR rules (AND = min across complex subunits, OR = max across isoenzymes); (3) reaction activities → task scores via weighted aggregation, with weights downweighting reactions shared across tasks. Optional KNN smoothing $X' = (1-\alpha) X + \alpha (S X)$ addresses sparsity.

## Variants

- **scCellFie-human** — 218 tasks built on Human1.
- **scCellFie-mouse** — 203 tasks built on Mouse1.
- **scCellFie-hormones** — newly added sex-hormone biosynthesis tasks (testosterone, progesterone, estradiol, etc.).
- **scCellFie spatial** — Moran's I spatial autocorrelation + neighborhood-based metabolite-mediated CCC on [[10x-visium-spatial-transcriptomics]].

## Comparison

- vs. **CellFie**: scCellFie scales to single cells/spots, adds smoothing, CCC, GAM-based temporal analysis.
- vs. **Compass** (FBA-based): scCellFie is far faster; gives task-level rather than per-reaction flux estimates.
- vs. **scFEA** (deep-learning fluxes): scCellFie is interpretable via GPR rules; scFEA is harder to audit.
- vs. **gene-set enrichment** (e.g. AUCell on KEGG): scCellFie respects enzyme stoichiometry and complex/isoenzyme logic.

## When to use

When you need interpretable metabolic readouts across millions of cells or spatial spots, want to test specific hypotheses about substrate-to-product conversions, or want to couple metabolic-task activity with cell-cell communication (metabolite ligand → receptor).

## Known limitations

Quality bounded by GEM annotations and curated task list; transcript abundance is an imperfect proxy for enzyme activity (post-translational regulation, kinetics, metabolite levels not modeled); thresholds tied to reference atlas may misclassify out-of-distribution tissues; metabolite-CCC depends on metabolite–receptor interaction databases that remain incomplete.

## Open problems

Automated task expansion; uncertainty estimates on per-cell task scores; benchmarks against paired metabolomics at true single-cell resolution; coupling with metabolic-flux measurements.

## Key papers

- [[atlas-scale-metabolic-activities-inferred-single]] — original scCellFie preprint with CELLxGENE atlas, endometrium, endometriosis, and endometrial-carcinoma applications.

## My understanding

scCellFie is the first method to deliver atlas-scale, biochemically interpretable metabolic readouts at single-cell and spatial resolution. For endometrial biology it nominates concrete, testable metabolic hypotheses (kynurenine–AHR in epithelial inflammation control; MVA in malignant cells; local androgen→estrogen conversion in EEC). Strongest immediate value: hypothesis generation atop existing scRNA-seq/Visium datasets; weakest link: lack of orthogonal metabolomic validation in this paper.
