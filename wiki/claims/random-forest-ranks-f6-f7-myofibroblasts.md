---
title: "A random-forest classifier ranks F6 and F7 myofibroblasts as the most important fibroblast subtypes for predicting scarring-risk category"
slug: random-forest-ranks-f6-f7-myofibroblasts
status: supported
confidence: 0.75
tags: [skin, myofibroblast, scarring, machine-learning, classifier]
domain: methods
source_papers:
  - single-cell-spatial-genomics-atlas-human
evidence:
  - source: single-cell-spatial-genomics-atlas-human
    type: supports
    strength: moderate
    detail: "Random-forest classifier identified F6 inflammatory myofibroblasts and F7 myofibroblasts as the most important fibroblast subtypes for predicting scarring-risk category (Extended Data Fig. 6b)."
conditions: "Feature-importance from classifier trained on fibroblast composition."
date_proposed: 2026-05-28
date_updated: 2026-05-28
---

## Statement

When predicting clinical scarring-risk category from fibroblast composition, a random-forest classifier ranks F6 and F7 myofibroblasts as the most informative subtypes.

## Evidence summary

Feature-importance ranking (Extended Data Fig. 6b); complemented by LRRC15 protein validation.

## Conditions and scope

Classifier feature importance, not causal.

## Counter-evidence

None.

## Linked ideas

## Open questions

Generalization to unseen diseases/cohorts.
