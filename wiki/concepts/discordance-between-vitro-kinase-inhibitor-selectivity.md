---
title: "Discordance between in vitro kinase-inhibitor selectivity and cellular effects"
aliases:
  - "binding-vs-function discordance for kinase inhibitors"
  - "kinobeads-clinical annotation discordance"
tags:
  - kinase-inhibitors
  - drug-selectivity
  - kinobeads
  - target-engagement
  - pharmacology
maturity: active
key_papers:
  - integrative-epigenome-based-strategy-unbiased-functional
first_introduced: "Gualdrini et al. 2024 *Molecular Systems Biology*"
date_updated: 2026-06-03
related_concepts:
  - polypharmacology-clinical-kinase-inhibitors
  - epigenome-based-functional-profiling-kinase-inhibitors
---

## Definition

The observation that the targets attributed to a clinical kinase inhibitor by clinical annotations and by in-vitro binding assays (kinobeads) frequently fail to predict the inhibitor's actual functional effects in living cells. Binding affinity is necessary information but insufficient to anticipate the extent and identity of cellular perturbations.

## Intuition

A drug can bind a kinase in a lysate yet not produce the expected cellular consequence — or produce strong cellular effects through targets it was not reported to bind. The three layers (clinical label, in-vitro binding, in-cell function) are only partially aligned.

## Formal notation

- Clinical annotations often discordant with kinobeads-measured targets.
- Kinobeads intra-family CKI distances are smaller than designated-target and random (binding improves on labels)...
- ...yet unrelated-family CKIs can be equally/closer in function, and some strong in-cell effects (e.g., Filgotinib, Tofacitinib STAT1/IFN inhibition) occur without detectable kinobeads JAK binding.

## Variants

- Concordant cases: Midostaurin→TBK1, Momelotinib→TBK1 binding explain interferon effects.
- Discordant cases: Filgotinib/Tofacitinib inhibit IFN signaling with no detected JAK binding.

## Comparison

Reframes drug "selectivity" as layer-dependent: selectivity in a binding assay ≠ functional selectivity in cells.

## When to use

When validating mechanism of action, comparing same-target compounds, or deciding whether binding data justify a functional inference.

## Known limitations

- Kinome coverage of binding assays is partial, so apparent "no binding" may be a detection limit.
- Functional discordance is hard to attribute to a specific unmeasured target.

## Open problems

- Identifying the true cellular mediators behind binding/function discordances.
- Building predictive bridges from binding profiles to cellular phenotype.

## Key papers

- [[papers/integrative-epigenome-based-strategy-unbiased-functional]] — documents both concordant and discordant binding-vs-function cases across 58 CKIs.

## My understanding

The paper's most actionable message for interpreting any kinase-inhibitor experiment: do not assume the labeled target is what is driving the phenotype; functional readouts are required.
