---
title: "Skin inflammation shifts immune composition toward lymphoid and away from myeloid cells"
slug: inflammation-shifts-skin-immune-composition-toward
status: supported
confidence: 0.8
tags: [skin, immune-composition, scrna-seq, immunology, correlational]
domain: immunology / single-cell
source_papers:
  - classification-human-chronic-inflammatory-skin-disease
evidence:
  - source: classification-human-chronic-inflammatory-skin-disease
    type: supports
    strength: moderate
    detail: "Quote (p.3): 'inflammation was accompanied by relative increases in multiple lymphoid cell classes and proportionate decreases in myeloid populations.' 27 of 41 clusters significantly altered."
conditions: "Relative CD45+ proportions; weighted Gaussian linear model, adj P < 0.05."
date_proposed: 2026-06-10
date_updated: 2026-06-10
---

## Statement

Chronic skin inflammation is accompanied by a relative compositional shift toward lymphoid cell classes and a proportionate decrease in myeloid populations, with 27 of 41 immune clusters showing statistically significant frequency alterations between rash and healthy skin.

## Evidence summary

Reported in Results of [[papers/classification-human-chronic-inflammatory-skin-disease]] using [[foundations/mast-hurdle-model-single-cell-differential]] downstream context. Supports [[concepts/treg-trm-expansion-cd8-exhaustion-chronic]].

## Conditions and scope

Relative (proportional) composition of sorted CD45+ cells; absolute numbers not measured.

## Counter-evidence

Compositional shifts are relative and can be distorted by the most abundant populations.

## Linked ideas

## Open questions

- Does the myeloid decrease reflect true loss or dilution by lymphoid expansion?
