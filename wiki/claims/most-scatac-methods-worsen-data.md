---
title: "Most scATAC-seq integration outputs (73%) actively degrade data versus the unintegrated baseline"
slug: most-scatac-methods-worsen-data
status: supported
confidence: 0.85
tags:
  - scATAC-seq
  - data-integration
  - benchmarking
  - failure-mode
domain: single-cell-methods
source_papers:
  - benchmarking-atlas-level-data-integration-single
evidence:
  - source: "[[papers/benchmarking-atlas-level-data-integration-single]]"
    type: supports
    strength: strong
    detail: "Only 27% of scATAC-seq integration outputs on peaks feature space beat the best unintegrated baseline, compared to 85% on RNA tasks. Many methods that succeed on scRNA-seq actively introduce artefacts when applied to scATAC-seq."
conditions: "Holds for mouse brain scATAC-seq on peaks feature space; windows / gene-activity follow similar trends. Implies that 'integrate first then analyze' workflows must be evaluated against unintegrated baseline for scATAC."
date_proposed: 2026-05-22
date_updated: 2026-05-22
---

## Statement

For scATAC-seq integration in peak feature space, only 27% of method/preprocessing outputs improve over the best unintegrated baseline — compared to 85% on scRNA-seq. The scATAC field has more methods that hurt than help.

## Evidence summary

Quote (p.46): "only 27% of integration outputs performed better than the best unintegrated result (on peaks, Fig. 4a and Extended Data Figs. 5 and 6) compared to 85% on RNA tasks."

## Conditions and scope

- Tested on mouse brain scATAC-seq (3 datasets).
- "Better than unintegrated baseline" is judged by the 40/60 batch/bio aggregate score.
- For users running scATAC integration: explicitly compare to an unintegrated baseline before adopting any method.

## Counter-evidence

- (none — the finding is a benchmark observation)

## Linked ideas

(none yet)

## Open questions

- Does the 27% generalize to tissues beyond mouse brain?
- Which method+feature combinations are the worst offenders — should they be deprecated?
