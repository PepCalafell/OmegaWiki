---
title: "Heuristic DESeq2 power-analysis p-values are broadly concordant with full PyDESeq2"
slug: heuristic-deseq2-power-analysis-values-concordant
status: weakly_supported
confidence: 0.65
tags: [validation, deseq2, pydeseq2, power-analysis, dispersion]
domain: "statistics / methods"
source_papers:
  - depower-approximate-power-analysis-deseq2
evidence:
  - source: depower-approximate-power-analysis-deseq2
    type: supports
    strength: moderate
    detail: "Fig 1c-d on GSE254223 ground-squirrel liver miRNA data (8 animals/group): heuristic p-values broadly consistent with PyDESeq2 0.4.8; deviations overwhelmingly from the ad hoc dispersion — using true PyDESeq2 dispersion gives near-identical p-values."
conditions: "Single small qualitative benchmark dataset; 'forward' estimation comparison only."
date_proposed: 2026-06-03
date_updated: 2026-06-03
---

## Statement

The heuristic procedure's intermediate statistics and nominal p-values are broadly consistent with a full PyDESeq2 analysis; the deviations are overwhelmingly explained by the ad hoc dispersion estimate, since substituting the true PyDESeq2 dispersion (while keeping the rest of the procedure) yields p-values nearly identical to the full workflow.

## Evidence summary

Qualitative validation on mitochondrial-microRNA counts from thirteen-lined ground squirrel liver (Robichaud et al., GSE254223; summer TSL vs. torpid TTL, 8 animals/group) against PyDESeq2 0.4.8 (Figure 1b–d).

## Conditions and scope

A single small, qualitative benchmark; not a systematic accuracy evaluation across datasets or designs.

## Counter-evidence

Individual genes lie outside the dispersion band; the dispersion heuristic is the explicit weak link.

## Linked ideas

- [[concepts/heuristic-dispersion-band-mean-expression]]
- [[claims/deseq2-mean-dispersion-curve-approximated-heuristic]]

## Open questions

- How well does concordance hold across larger, more heterogeneous datasets and unbalanced designs?
