---
title: "scSLIDE recovers the time-since-onset axis without being given that metadata"
slug: scslide-recovers-time-since-onset-axis
status: supported
confidence: 0.8
tags: [COVID-19, scSLIDE, unsupervised-discovery]
domain: immunology
source_papers:
  - reconstructing-developmental-disease-progression-sample-level
evidence:
  - source: reconstructing-developmental-disease-progression-sample-level
    type: supports
    strength: moderate
    detail: "DC2 correlated strongly with time since onset although TSO was never supplied to the scSLIDE workflow, demonstrating discovery of an unprovided axis of variation."
conditions: "Only disease state and severity metadata were given to the PLS step; TSO emerged de novo."
date_proposed: 2026-06-03
date_updated: 2026-06-03
---

## Statement

scSLIDE identified a time-since-onset (TSO) axis of sample variation even though TSO information was never provided to the model, showing the semi-supervised embedding retains the ability to discover unprovided sources of variation.

## Evidence summary

Figure 2e and text of [[reconstructing-developmental-disease-progression-sample-level]]: DC2 position correlated with TSO despite only disease state and severity being supplied to the PLS embedding.

## Conditions and scope

A demonstration of the framework's design goal that supervision should not eliminate novel-axis discovery.

## Counter-evidence

None within the paper.

## Linked ideas

Supports the design rationale behind [[scslide-builds-semi-supervised-cell-embedding]].

## Open questions

Under what supervision strength does novel-axis discovery degrade?
