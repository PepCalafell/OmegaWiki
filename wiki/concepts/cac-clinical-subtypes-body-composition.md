---
title: "Clinical CAC subtypes defined by body-composition loss patterns"
aliases:
  - "CAC body-composition subtypes"
  - "adipose-tissue-loss only CAC"
  - "adipose + SKM loss CAC"
tags:
  - cachexia
  - oncology
  - body-composition
  - clinical-phenotyping
maturity: emerging
key_papers:
  - cancer-associated-cachexia-bridging-clinical-findings
  - multi-omics-profiling-cachexia-targeted-tissues
first_introduced: "Klassen et al. (PDAC); TRACERx-NSCLC body-composition arm"
date_updated: 2026-05-27
related_concepts: []
---

## Definition

A framework for stratifying cancer-associated cachexia (CAC) patients by the PATTERN of body-compartment loss observed on serial CT imaging — specifically the relative loss of skeletal muscle (SKM), subcutaneous adipose tissue (SAT) and visceral adipose tissue (VAT) — rather than by total weight loss alone. Operationally, two reproducible subtypes have been described in advanced PDAC: "adipose-tissue-loss only" and "adipose + SKM loss". TRACERx-NSCLC extends this to isolated SKM-loss vs combined-loss phenotypes, each with distinct primary-tumour gene-expression profiles.

## Intuition

Weight loss is a downstream summary statistic that COLLAPSES distinct biological processes: lipolysis-driven adipose loss can occur without muscle loss (early CAC, sarcopenic obesity), and muscle loss can occur with stable weight (when fat gain masks SKM atrophy). Stratifying by which COMPARTMENT is lost reveals subgroups that probably correspond to different driver biology (e.g., catecholamine/HSL-dominated lipolysis vs UPS-dominated proteolysis vs blunted-anabolism) and therefore may respond to different interventions.

## Formal notation

- TRACERx-NSCLC CAC = any of: SKM loss > 10%, SAT loss > 20%, VAT loss > 20%, grade-4 BMI-adjusted weight loss.
- Klassen PDAC subtypes: {no-loss, adipose-only-loss, adipose + SKM loss}.
- Latent-trajectory (Jin et al. liver cancer): stable vs sharp-falling SKM; stable vs sharp-falling total adipose tissue → 4 combinatorial trajectories.

## Variants

- Sarcopenic obesity (high fat mass + low SKM).
- Isolated SKM loss (predominantly males in advanced cancer).
- Isolated adipose loss (predominantly observed in some PDAC chemotherapy-treated cohorts).
- Pre-CAC phase: detectable body-compartment loss before clinical diagnosis (notably PDAC).

## Comparison

Versus Fearon consensus criteria: Fearon collapses heterogeneity into a single weight-loss threshold and ignores body-compartment differentiation. Versus single-marker biochemistry (mGPS, CRP+albumin): captures structural-tissue change directly. Versus DEXA/BIA: CT discriminates SAT/VAT/SKM whereas DEXA gives whole-body lean vs fat only.

## When to use

When stratifying CAC patients for trial enrollment or for mechanistic studies where the goal is to map molecular drivers to a phenotype. Especially useful when serial CT scans are already available as part of standard oncology care (cost-neutral).

## Known limitations

- Single-slice L3 imaging may miss compartment-specific changes outside the abdomen.
- Cross-sectional reference values do not capture intra-person change; longitudinal trajectory modelling is needed.
- Acquisition parameters (slice thickness, IV contrast, tube current) introduce measurement variability not yet standardized.
- Reference values are biased toward White non-Hispanic populations.

## Open problems

- Do body-composition subtypes correspond to molecular subtypes defined by [[papers/multi-omics-profiling-cachexia-targeted-tissues]] (one-carbon/IL-6 axis)?
- Are subtypes stable over time within a patient, or do they progress (e.g., adipose-only → combined)?
- Do subtypes predict differential response to anti-IL-6, anti-GDF-15, ghrelin-receptor agonism, or anabolic-resistance-targeted nutrition?

## Key papers

- [[papers/cancer-associated-cachexia-bridging-clinical-findings]] — the canonical 2025 review formalizing this framework.
- [[papers/multi-omics-profiling-cachexia-targeted-tissues]] — molecular pillar that may map onto these clinical subtypes.

## My understanding

The most useful clinical-research contribution from the 2025 Cancer Discovery review. Treating CAC as a SPECTRUM rather than a binary diagnosis is what unblocks trial design, since the field has been comparing apples to oranges across cohorts with incompatible definitions.
