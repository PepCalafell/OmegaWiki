---
title: "Analytical DESeq2 sample-size estimates should be treated as a lower bound under ideal assumptions"
slug: deseq2-sample-size-estimates-lower-bound
status: supported
confidence: 0.85
tags: [power-analysis, deseq2, assumptions, experimental-design, statistics]
domain: "statistics / methods"
source_papers:
  - depower-approximate-power-analysis-deseq2
evidence:
  - source: depower-approximate-power-analysis-deseq2
    type: supports
    strength: moderate
    detail: "'the results of the sample size analysis should be seen as a lower bound under the ideal-case scenario'; model violations, batches, outliers, and small-sample Wald non-asymptotics raise effective n."
conditions: "Holds whenever the negative-binomial model, balanced depth, and asymptotic Wald assumptions are violated."
date_proposed: 2026-06-03
date_updated: 2026-06-03
---

## Statement

Because the procedure stacks the approximation-specific simplifications (neglected depth variability, heuristic dispersion) on top of the usual DESeq2/Wald assumptions, its sample-size estimates should be read as a lower bound: model violations, additional covariates/batches, outliers, or small-sample breakdown of the Wald asymptotics all imply the effective sample size may need to be higher than predicted.

## Evidence summary

Authors' explicit caveat (Analysis/Discussion); follows from the chain of assumptions underlying the closed form.

## Conditions and scope

General caveat applicable to any use of the method; especially relevant at small n.

## Counter-evidence

None — this is a conservative framing of the method's own limits.

## Linked ideas

- [[concepts/analytical-power-analysis-deseq2-model]]
- [[concepts/heuristic-dispersion-band-mean-expression]]

## Open questions

- Empirical inflation factors to convert the lower bound into a realistic target.
