---
title: "MissionBio is the hardest scRNA-seq platform for all evaluated agents"
slug: missionbio-hardest-scrna-seq-platform-all
status: supported
confidence: 0.85
tags:
  - benchmark
  - platform
  - missionbio
domain: methods
source_papers:
  - scbench-evaluating-ai-agents-single-cell
evidence:
  - source: scbench-evaluating-ai-agents-single-cell
    type: supports
    strength: strong
    detail: "MissionBio is hardest for all 8 models (cross-model mean 26.4%); it inverts rankings (Grok-4 beats GPT-5.2; Sonnet 4.5 beats GPT-5.2 by 11 pp). Tapestri's non-standard DNA+protein data structures and rare tooling drive the collapse."
conditions: "MissionBio Tapestri targeted DNA+protein panel; hematopoietic/CCUS samples."
date_proposed: 2026-06-12
date_updated: 2026-06-12
---

## Statement

MissionBio (Tapestri) is the hardest platform in scBench for all eight models,
with a cross-model mean accuracy of 26.4%, and it inverts the overall model
ranking because most competitors collapse while Anthropic models hold up.

## Evidence summary

Grok-4 (sixth overall) beats GPT-5.2 (third overall) on MissionBio; Sonnet 4.5
surpasses GPT-5.2 by 11 pp. Attributed to non-standard data structures and
less-common tooling, underrepresented in public documentation.

## Conditions and scope

Tapestri is a targeted DNA+protein platform included to stress-test
generalization beyond transcriptomic workflows.

## Counter-evidence

None within the paper.

## Linked ideas

## Open questions

Whether assay-specific tooling would rescue performance on Tapestri-style data.
