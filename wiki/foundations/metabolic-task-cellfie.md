---
title: "Metabolic task (CellFie / scCellFie)"
slug: metabolic-task-cellfie
domain: "systems biology / metabolism"
status: mainstream
aliases:
  - metabolic task
  - CellFie
  - CellFie task
  - metabolic task inference
first_introduced: "2020"
date_updated: 2026-05-27
source_url: "https://github.com/LewisLabUCSD/CellFie"
---

## Definition

A **metabolic task** is a discrete biochemical function defined as a module of reactions converting a specific substrate metabolite into a target product (e.g. "ATP generation from glucose", "synthesis of estradiol from androstenedione"). The CellFie framework (Richelle et al. 2021) introduced the formal definition and inferred task activity from bulk transcriptomics via [[genome-scale-metabolic-model]] gene–protein–reaction (GPR) rules; [[sccellfie-metabolic-task-inference]] extended this to single-cell and spatial resolution.

## Intuition

Pathway-based metabolic inference treats genes as bags of overlapping sets. A task instead asks: given the enzymes required for *this specific transformation*, do we see coordinated expression — accounting for protein complexes (AND across subunits) and isoenzymes (OR across alternatives)? This yields biochemically interpretable activity scores rather than gene-set enrichment scores.

## Formal notation

Reaction activity = aggregation over GPR with min (AND, complex) and max (OR, isoenzyme). Task score = weighted aggregation of constituent reaction activities, with weights adjusting for reactions shared across multiple tasks.

## Key variants

- **CellFie** (bulk transcriptomics, Richelle 2021).
- **scCellFie** ([[atlas-scale-metabolic-activities-inferred-single]]) — single-cell and spatial, scalable to ~30M cells, integrates with [[scanpy]].
- **Hormone-biosynthesis tasks** (new in scCellFie) — seven sex-hormone biosynthesis tasks built from Human1/Mouse1.

## Known limitations

Coverage limited to manually curated tasks (218 human / 203 mouse in scCellFie); transcript-to-activity mapping ignores post-translational regulation, enzyme kinetics, and metabolite concentrations.

## Open problems

Automated task discovery from GEMs; uncertainty quantification on task scores; integration with metabolomics ground truth at single-cell resolution.

## Relevance to active research

Backbone of interpretable, scalable metabolic inference from transcriptomics — used in [[atlas-scale-metabolic-activities-inferred-single]] to build a CELLxGENE-scale metabolic atlas and to interrogate endometrial physiology, endometriosis, and endometrial carcinoma.
