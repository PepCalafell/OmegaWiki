---
title: "Strongest batch-effect contributors in single-cell genomics integration are inter-species, single-nucleus-vs-single-cell and spatial location"
slug: strongest-batch-effects-species-nuclei
status: supported
confidence: 0.75
tags:
  - batch-effects
  - data-integration
  - benchmarking
  - species
domain: single-cell-methods
source_papers:
  - benchmarking-atlas-level-data-integration-single
evidence:
  - source: "[[papers/benchmarking-atlas-level-data-integration-single]]"
    type: supports
    strength: medium
    detail: "Qualitative ranking of batch-effect strength (Fig. 5b): inter-species > nuclei-vs-cell > inter-tissue / spatial location / inter-platform > inter-patient > replicate. The strongest contributors are also the most ambiguously biological — species, modality, and spatial location can be regarded as either batch or biology."
conditions: "Ranking is qualitative, derived from integration difficulty across the 13 scIB tasks. Strength ordering is task-aggregate; on specific tasks a weaker contributor may dominate (e.g. protocol effect dominating donor effect in some single-tissue tasks)."
date_proposed: 2026-05-22
date_updated: 2026-05-22
---

## Statement

A qualitative ranking of batch-effect contributors by integration difficulty, derived from the 13 scIB tasks, places inter-species and single-nucleus-vs-single-cell modality at the top, followed by inter-tissue / spatial location / inter-platform, then inter-patient, with technical replicates the weakest. The strongest contributors are also the most ambiguous because species, modality and spatial location can be interpreted as either batch effect or genuine biological signal.

## Evidence summary

Quote (p.43): "The most challenging batch effects across the integration tasks were due to species, sampling locations and single-nucleus versus single-cell data. These batch effect contributors can also be interpreted as biological signals rather than technical noise."

Fig. 5b in the paper depicts the relative strength as a schematic ranking.

## Conditions and scope

- Ranking is qualitative; not a quantitative effect-size table.
- Task-dependent: in single-tissue tasks, protocol effects may dominate donor effects.
- For HCA-scale integration involving multiple species or single-nuclei + single-cell data, expect integration to struggle most on these axes.

## Counter-evidence

- (none — schematic finding)

## Linked ideas

(none yet)

## Open questions

- Can a quantitative meta-analysis across HCA datasets reproduce this ranking?
- For TAM/macrophage atlases that mix mouse + human (relevant to thesis), this claim predicts species will be the dominant axis — confirmed in MoMac-VERSE?
