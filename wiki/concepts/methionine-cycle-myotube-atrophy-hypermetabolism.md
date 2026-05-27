---
title: "Methionine-cycle drives myotube atrophy and glucose hypermetabolism (in vitro causality)"
aliases:
  - "L-methionine induces myotube atrophy"
  - "methionine cycle atrophy hypermetabolism axis"
tags:
  - methionine
  - myotube
  - atrophy
  - hypermetabolism
  - C2C12
  - FIDAS-5
  - cachexia
maturity: emerging
key_papers:
  - multi-omics-profiling-cachexia-targeted-tissues
first_introduced: "Morigny et al. 2026 (Nat Metab)"
date_updated: 2026-05-27
related_concepts:
  - one-carbon-metabolism-cachexia-tissue-overarching
  - muscle-glucose-hypermetabolism-cachexia-tca-rewiring
  - fidas-5-methionine-blockade-rescues-cachexia
  - il6-driven-cachexia-one-carbon-reprogramming
---

## Definition

The concept that pharmacological activation of the methionine cycle (excess extracellular L-methionine, 20-100 μM) in cultured C2C12 myotubes is sufficient to recapitulate two core cachexia features simultaneously: (i) dose-dependent myotube atrophy and (ii) elevated glucose consumption / 13C6-glucose-traced TCA hypermetabolism — and that MAT inhibition (FIDAS-5) produces the opposite phenotype.

## Intuition

This is the in-vitro causal link that makes the broader cachexia → one-carbon story mechanistic rather than correlative. If excess methionine — the entry substrate of the cycle — by itself, in a muscle cell, drives both shrinkage and energy-wasting glucose burn, then one-carbon activation is *upstream* of (or coupled to) atrophy mechanics rather than a passive byproduct. FIDAS-5 reversal of IL6-induced atrophy makes the methionine cycle a *druggable* node downstream of inflammation.

## Formal notation

- Cell system: differentiated C2C12 myotubes (5-day differentiation in 2% FBS DMEM); ImageJ-based diameter quantification across 40-60 myotubes/well.
- L-methionine doses: 0, 20, 100 μM (48 h), in dialysed-serum methionine-poor base medium.
- Direct readouts:
  - One-carbon metabolites (SAM, SAH, MNAM, DMG): dose-dependent ↑.
  - Myotube diameter: dose-dependent ↓.
  - Glucose consumption: ↑.
  - 13C6-glucose label in TCA cycle (M+2, M+3, M+4 isotopologues): ↑.
- FIDAS-5 (MAT inhibitor; 2-5 μM, 48 h): ↓ one-carbon metabolites; myotube hypertrophy; ↓ glucose consumption — opposite phenotype.
- IL6 epistasis: recombinant IL6 (100 ng/mL) → induces methionine cycle + atrophy + hypermetabolism; FIDAS-5 rescues each readout → methionine cycle is downstream of IL6 in C2C12.
- Cell-type specificity: 3T3-L1 adipocytes do not show lipolysis or glucose-consumption phenotype on L-methionine — effect is muscle-cell specific.

## Variants

- Acute (24 h) vs sustained (48 h) treatment: only 48 h fully shows atrophy (consistent with cycle activation requirements).
- C2C12 vs primary myotubes (untested) — generalisation pending.
- L-methionine vs direct SAM supplementation (untested in this paper) — would test whether methionine entry per se is rate-limiting.

## Comparison

- Vs classical cachexia myotube models (dexamethasone, conditioned media from C26 cells, IL6/TNF): methionine is a metabolite stimulus that bypasses cytokine-receptor signalling — a different entry point into the same phenotypic state.
- Vs methionine-restricted-diet lifespan biology (Sanderson, Ducker reviews): the in vitro phenotype is consistent with methionine excess as a stress signal rather than a benign nutrient.

## When to use

- When designing in vitro screens for cachexia-rescue compounds — C2C12 + L-methionine (or + IL6) is a tractable atrophy readout.
- When considering dietary methionine restriction as a cachexia intervention — provides the cellular mechanism to interpret organ-level effects.
- When interpreting muscle-fibre metabolic states in transcriptomic data: high methionine-cycle gene expression should be flagged as potentially atrophy-promoting.

## Known limitations

- Dose range (20-100 μM) is supra-physiological for plasma but plausible for intramuscular concentrations during one-carbon cycle activation; physiological dosing range underspecified.
- Atrophy is morphological (diameter); no proteasomal/autophagic flux measurements (LC3, polyubiquitin) — molecular atrophy biomarkers missing.
- C2C12 is an immortalised mouse cell line — primary human muscle (or iPSC-derived myotubes) needed to translate.
- FIDAS-5 selectivity at 2-5 μM is acceptable but not perfect; off-targets in adjacent SAM-dependent reactions possible.

## Open problems

- Which downstream methylation reactions in myotubes mediate the atrophy phenotype (DNA / RNA / histone / specific protein methylation)?
- Is the glucose hypermetabolism phenotype a direct PC/PDH allosteric effect of methionine-cycle intermediates (e.g., SAM-dependent histone marks regulating glycolytic gene expression) or downstream of mitochondrial-dysfunction stress?
- Does dietary methionine restriction in tumour-bearing mice phenocopy FIDAS-5 in vitro at the muscle level?
- Does the methionine ↔ glucose-hyperconsumption coupling generalise to human myotubes?

## Key papers

- [[papers/multi-omics-profiling-cachexia-targeted-tissues]] — In vitro causality in C2C12 (Fig. 5, Ext Fig. 6).

## My understanding

This concept is the most translatable handle of the paper. In vivo FIDAS-5 testing (the most obvious follow-up) was not performed in this paper but is the natural next experiment. If a systemic MAT inhibitor or methionine-restricted diet preserves muscle mass and survival in C26 (or PDAC) mice, the cachexia field gets a new therapeutic axis that pairs naturally with IL6 blockade.
