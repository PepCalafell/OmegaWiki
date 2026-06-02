---
title: "Kinase activity footprint inference from phosphoproteomics"
aliases:
  - kinase activity footprinting
  - kinase footprint inference
  - upstream kinase activity inference
tags:
  - phosphoproteomics
  - kinase
  - signaling
  - methods
maturity: active
key_papers:
  - delineation-signaling-routes-underlie-differences-macrophage
first_introduced: "Concept matured with motif atlases (Johnson et al. 2023) and enrichment tools (KEA3, NetPhorest)"
date_updated: 2026-06-02
related_concepts:
  - macrophage-activation-core-regulatory-hubs
  - pak2-pkc-alpha-regulators-immunosuppressive-macrophages
---

## Definition

A family of analytical strategies that infer the activity of upstream protein kinases from the pattern of phosphorylation changes (the "footprint") observed in a phosphoproteomics dataset, rather than from direct measurement of the kinases themselves. Approaches combine motif-based prediction (which kinase prefers the sequence around a site), curated kinase–substrate annotations, and enrichment statistics over sets of regulated phosphosites.

## Intuition

Most active kinases are present at low abundance and are themselves poorly captured by phosphoproteomics. But their activity leaves a trace: the substrates they phosphorylate. By asking "which kinases would produce the set of phosphosites that went up in condition X," one can nominate active kinases even when the kinase peptide was never measured. This converts a sparse, noisy phosphoproteome into testable hypotheses about signaling flow.

## Formal notation

- Input: differentially regulated phosphosites per condition (with FC, p-values, localization probability)
- Motif scoring: per-kinase position-specific matrices over the ±n residues around the site ([[foundations/kinase-library-phosphosite-atlas]])
- Family-level probabilistic prediction ([[foundations/netphorest-kinase-prediction]])
- Set enrichment over substrate/interaction/co-expression libraries ([[foundations/kea3-kinase-enrichment-analysis]])
- Significance via Fisher's exact test with BH multiple-testing correction

## Variants

- Motif-based (Kinase Library) — individual-kinase resolution from sequence
- Family-based probabilistic (NetPhorest) — kinase-family posterior probabilities
- Enrichment-based (KEA3) — multi-library ranking of upstream kinases
- Curated knowledge-based (PhosphoSitePlus, SIGNOR, OmniPath) — observed edges only

## Comparison

vs transcriptomics/proteomics, which report abundance but cannot reveal directionality of signaling: footprinting reads signaling *state* and flow. vs direct kinase-activity assays (antibody panels), which cover only a handful of kinases: footprinting is unbiased across the kinome but indirect and prediction-dependent.

## When to use

- Interpreting MS phosphoproteomics where many active kinases are unmeasured
- Nominating candidate regulators of a cell state for follow-up perturbation
- Building kinase–kinase / kinase–TF signaling networks per condition

## Known limitations

- Predicts capability, not whether a kinase is expressed/active in the sample
- Closely related kinases share motifs, limiting individual resolution
- High phosphoproteome missingness and literature bias toward well-studied kinases

## Open problems

- Integrating motif predictions with abundance to filter inactive kinases
- Reconciling disagreements among motif-, family-, and enrichment-based predictions

## Key papers

- [[papers/delineation-signaling-routes-underlie-differences-macrophage]] — applies Kinase Library, KEA3, and NetPhorest to primary human macrophage phosphoproteomes to recover known M1 kinases (JNK, p38) and nominate novel immunosuppressive-state kinases (PAK2, PKCα, LRRK2, IRAK1/4, CAMKK2, GAK).

## My understanding

The central methodological move of this corpus's macrophage-signaling work: because the most interesting kinases are invisible to direct measurement, footprinting is what makes phosphoproteomics actionable for finding reprogramming targets. Its predictions are hypotheses, not proof — best paired with activation-loop phosphosite evidence and downstream perturbation.
