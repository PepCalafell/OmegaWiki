---
title: "Sequencing platform affects agent scRNA-seq accuracy as much as model choice"
slug: sequencing-platform-affects-agent-scrna-seq
status: supported
confidence: 0.85
tags:
  - benchmark
  - platform
  - scrna-seq
domain: methods
source_papers:
  - scbench-evaluating-ai-agents-single-cell
evidence:
  - source: scbench-evaluating-ai-agents-single-cell
    type: supports
    strength: strong
    detail: "Cross-model mean accuracy ranges 59.1% (CSGenetics) to 26.4% (MissionBio) — a 32.7 pp gap exceeding the 23.6 pp best-worst model spread. Gemini drops 42 pp between platforms; Opus 4.5 loses 39 pp."
conditions: "Six platforms (Chromium, BD Rhapsody, CSGenetics, Illumina, MissionBio, ParseBio)."
date_proposed: 2026-06-12
date_updated: 2026-06-12
---

## Statement

The sequencing platform of the data affects agent analysis accuracy as much as,
or more than, the choice of model: the 32.7 pp cross-platform gap in cross-model
mean accuracy exceeds the 23.6 pp spread between the best and worst models.

## Evidence summary

Every model shows large platform swings, attributed to uneven training-data
representation (Chromium/Illumina well-documented; MissionBio/ParseBio less so).

## Conditions and scope

scBench's six platforms; attribution to training data is inferential.

## Counter-evidence

None within the paper.

## Linked ideas

## Open questions

Whether platform-aware tooling closes the gap.
