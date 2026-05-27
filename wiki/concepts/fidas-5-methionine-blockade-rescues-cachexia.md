---
title: "FIDAS-5 methionine-cycle blockade rescues cachexia features in C2C12 myotubes"
aliases:
  - "FIDAS-5 MAT inhibition cachexia"
  - "methionine cycle pharmacological blockade muscle"
tags:
  - FIDAS-5
  - MAT-inhibitor
  - methionine-cycle
  - cachexia
  - therapeutic
  - C2C12
maturity: emerging
key_papers:
  - multi-omics-profiling-cachexia-targeted-tissues
first_introduced: "Morigny et al. 2026 (Nat Metab); FIDAS-5 itself: original MAT-inhibitor chemistry"
date_updated: 2026-05-27
related_concepts:
  - methionine-cycle-myotube-atrophy-hypermetabolism
  - il6-driven-cachexia-one-carbon-reprogramming
  - one-carbon-metabolism-cachexia-tissue-overarching
---

## Definition

The concept that pharmacological inhibition of methionine adenosyltransferase (MAT) with FIDAS-5 in C2C12 myotubes simultaneously (i) lowers one-carbon-pathway metabolite levels, (ii) drives myotube hypertrophy (opposite of cachectic atrophy), (iii) reduces glucose consumption, and (iv) rescues each of these readouts when IL6 is the upstream trigger — making the methionine cycle a candidate druggable node downstream of IL6 in cachexia.

## Intuition

FIDAS-5 is the *mechanistic mirror image* of L-methionine treatment: same axis, opposite direction. The fact that the same inhibitor rescues IL6-driven phenotypes means the methionine cycle sits downstream of IL6, and MAT activity is rate-limiting for the cachexia phenotype in muscle cells. This is the most translatable pharmacological handle in the paper.

## Formal notation

- Compound: FIDAS-5 (allosteric MAT2A inhibitor lineage; commercial MCE HY-136144).
- Doses tested: 2 μM, 5 μM (48 h), with matched DMSO vehicle.
- Readouts in C2C12 myotubes:
  - One-carbon metabolites: ↓ dose-dependently.
  - Myotube diameter: ↑ (hypertrophy).
  - Glucose consumption: ↓.
- IL6 epistasis experiment:
  - 100 ng/mL recombinant IL6 alone → ↑ one-carbon, atrophy, hypermetabolism.
  - IL6 + FIDAS-5 → each readout reversed toward control.

## Variants

- In vivo FIDAS-5 in tumour-bearing mice: not tested in this paper — the most important missing experiment.
- Dietary methionine restriction as an alternative pathway-level intervention: discussed; not tested here.
- NNMT inhibitors as a downstream alternative: untested.

## Comparison

- Vs PF-9366 (another MAT2A inhibitor used in [[concepts/ac-derived-methionine-sam-macrophage-epigenetics]] / macrophage efferocytosis biology): same enzyme target, different cellular context.
- Vs anti-IL6 / anti-IL6R therapies: FIDAS-5 acts downstream of IL6 — could be combined or used as backup when IL6 blockade is contraindicated.

## When to use

- When prioritising druggable nodes in the one-carbon-cachexia axis: MAT inhibition is the clearest causal handle in this paper.
- When designing cachexia-rescue screens that already use the methionine-treated C2C12 model.

## Known limitations

- Only C2C12 myotubes — no primary muscle, no in vivo data.
- MAT2A inhibition is not selective over all SAM-utilising reactions; pleiotropic effects (DNA methylation, histone methylation, polyamine synthesis) expected at higher doses.
- Hypertrophy at baseline may reflect non-physiological methionine restriction in the dialysed-serum medium — caution interpreting absolute diameter changes.

## Open problems

- Does systemic FIDAS-5 (or another MAT inhibitor) preserve muscle mass and survival in C26 / PDAC mice in vivo?
- Does combining FIDAS-5 with anti-IL6R (tocilizumab) outperform either alone?
- Are MTAP-deleted cachexia-associated tumours selectively sensitive to MAT2A inhibition (synthetic-lethality literature suggests yes)?
- Toxicity profile of sustained systemic MAT inhibition in lean tissue (intestine, immune cells).

## Key papers

- [[papers/multi-omics-profiling-cachexia-targeted-tissues]] — Provides the in vitro double-rescue evidence.

## My understanding

The natural follow-up experiment for the wiki to flag: an in vivo FIDAS-5 study in C26-bearing mice with body-weight, lean-mass, grip-strength, and tumour-size endpoints. This single experiment would convert the concept from "in vitro mechanistic" to "preclinical therapeutic candidate."
