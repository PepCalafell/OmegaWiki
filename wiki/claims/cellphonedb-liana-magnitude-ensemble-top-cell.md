---
title: "CellPhoneDB and LIANA's magnitude ensemble are the top cell–cell communication performers"
slug: cellphonedb-liana-magnitude-ensemble-top-cell
status: supported
confidence: 0.8
tags:
  - cell-cell-communication
  - benchmarking
  - single-cell
domain: methods / benchmarking / single-cell
source_papers:
  - defining-benchmarking-open-problems-single-cell
evidence:
  - source: papers/defining-benchmarking-open-problems-single-cell
    type: supports
    strength: moderate
    detail: "Ranked by mean overall score across TNBC and mouse-brain subtasks (Fig. 2c)."
conditions: "Open Problems CCC task v1 ranking."
date_proposed: 2026-06-15
date_updated: 2026-06-15
---

## Statement

Across the Open Problems CCC subtasks, the top-performing methods are CellPhoneDB and LIANA's ensemble model of expression-magnitude scoring methods.

## Evidence summary

"the top performers across tasks are CellPhoneDB and LIANA's ensemble model of expression magnitude scoring methods" (p.1038), ranked by the mean of the overall score for each subtask (Fig. 2c). This concretises the magnitude-over-specificity result with named methods.

## Conditions and scope

Ranking from the v1 collated CCC results; relative order may shift as datasets and methods are added to the living task.

## Counter-evidence

A two-dataset ranking is a narrow basis; winners could change with additional tissue contexts.

## Linked ideas

Instantiates [[claims/magnitude-based-cell-cell-communication-scoring]]; methods are [[foundations/cellphonedb-ligand-receptor]] and [[foundations/liana-cell-cell-interaction-inference]].

## Open questions

How robust the CellPhoneDB/LIANA ranking is across more tissues and newer CCC methods.
