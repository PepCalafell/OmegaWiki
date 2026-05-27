---
title: "Muscle glucose hypermetabolism in cachexia — PC/PDH-driven TCA flux acceleration"
aliases:
  - "cachectic muscle hypermetabolism"
  - "PC-PDH TCA rewiring in cachexia"
tags:
  - muscle
  - cachexia
  - 13C-glucose
  - pyruvate-carboxylase
  - PDH
  - TCA-cycle
  - INCA-flux
  - anaplerosis
  - glutamine
maturity: emerging
key_papers:
  - multi-omics-profiling-cachexia-targeted-tissues
first_introduced: "Morigny et al. 2026 (Nat Metab)"
date_updated: 2026-05-27
related_concepts:
  - methionine-cycle-myotube-atrophy-hypermetabolism
  - one-carbon-metabolism-cachexia-tissue-overarching
---

## Definition

The concept that skeletal (GC, soleus) and cardiac muscle of cachectic tumour-bearing mice exhibit accelerated glucose-derived TCA cycle flux despite stable or reduced unlabelled metabolite pools, driven by simultaneous pyruvate-carboxylase (PC) and pyruvate-dehydrogenase (PDH) activity and complemented by glutamine anaplerosis — a state of nutrient-availability-dependent energy hyperconsumption that is detectable already in the pre-cachectic phase.

## Intuition

Cachectic muscle is *hungrier than it looks*. Basal (unlabelled) TCA intermediates appear stable or decreased, but as soon as glucose is supplied (i.p. 13C6-glucose 1 h before tissue collection), label incorporation into citrate/succinate/fumarate/malate jumps — including higher isotopologues (M+3, M+4) that require multi-turn or anaplerotic entry. So the deficit is not "the cycle is broken" but "the cycle is overdriven when fuel is available, hence wasting fuel without fixing the energy deficit elsewhere."

## Formal notation

- In vivo tracer: i.p. [13C6]-glucose, tissue collection 1 h later under 6-h fasting baseline.
- Readouts in Cax vs Ctrl/Non-cax mice (n = 4/group):
  - GC, soleus, heart: ↑ M+2/M+3/M+4 isotopologues of citrate, succinate, fumarate, malate.
  - Total unlabelled pool: stable or ↓.
- Mechanistic interpretation:
  - M+3 succinate/fumarate/malate from [13C6]-glucose requires pyruvate carboxylase (PC) — confirmed by [1-13C]-pyruvate tracing in C2C12 showing M+1 TCA label.
  - PC and PDH co-active in cachectic muscle.
- INCA 2.3 flux modelling (normalised to citrate synthase V12):
  - ↑ V9 (PC), ↑ V10 (PDH), ↑ V18 (2-OGDH).
  - Trends ↑ V19-21 (SDH, FH, MDH).
  - ↑ V16-V17 (glutamine anaplerosis).
  - ↓ V11 (β-oxidation/ketogenic-AA-derived acetyl-CoA).
- Early-event signature: Pre-cax mice (no weight loss) already trend toward the same flux pattern.
- Cell-line corroboration: L-methionine treatment of C2C12 reproduces glucose hyperconsumption + TCA label enrichment.

## Variants

- C26 model (this paper's primary): documented across GC, soleus, heart.
- Panc02 / 8025 PDAC models: 13C-glucose enrichment scales with cachexia severity in GC muscle.
- Humanised SW480 model: cardiac + skeletal muscle TCA label enrichment matches C26 pattern.
- C2C12 in vitro: methionine-driven hypermetabolism in absence of tumour.

## Comparison

- Vs canonical "muscle protein catabolism / proteolysis" cachexia model: this concept reframes wasting partially as an *energy-leak* phenomenon, complementary to (not replacing) ubiquitin-proteasome / autophagy-mediated proteolysis.
- Vs Warburg-like tumour glycolysis: tumour and host muscle compete for glucose, but the directionality (muscle consuming more glucose into TCA) diverges from classical tumour lactate-producing aerobic glycolysis.
- Vs HIF/hypoxia-driven PDH inhibition (PDK1 → PDH-OFF → lactate accumulation [[claims/hif-1alpha-pdk1-blocks-pyruvate-tca-lactate-accumulation]]): cachectic muscle does the opposite — PDH is active and TCA is overdriven. Mechanistically distinct from a hypoxia state.

## When to use

- When interpreting indirect calorimetry / resting energy expenditure data from cachectic patients — provides a tissue-level mechanism for elevated REE in pre-cachexia.
- When considering metabolic interventions (PC inhibition, ketogenic / glucose-restriction diets, glutamine antagonism) for cachexia therapy.
- When designing isotope-tracing studies in human cachexia: the protocol (i.p. or oral 13C-glucose + multi-tissue MS) is a template.

## Known limitations

- "Hypermetabolism" is detected only upon glucose challenge — the basal flux state in fasted cachectic muscle is not clearly hypermetabolic.
- INCA flux normalisation to citrate synthase activity (V12) — already elevated in Cax muscle — means *absolute* fluxes are larger than reported relative changes.
- No measurement of mitochondrial respiration capacity (Seahorse OCR/ECAR) in primary cachectic muscle fibres to corroborate flux modelling.
- Cell-type contribution unresolved — single-cell or fibre-type-resolved analysis missing.

## Open problems

- Is PC the right pharmacological handle for blocking cachectic-muscle energy leak (PC inhibition could compromise gluconeogenesis systemically)?
- Does glutamine anaplerosis blockade (CB-839 / telaglenastat) rescue muscle mass in cachexia models?
- How does the methionine-cycle activation mechanistically couple to PC/PDH flux acceleration (allosteric effects of SAM/SAH on glycolytic enzymes? methylation of metabolic-gene promoters?)?
- Pre-cachexia detection by 13C-glucose breath test or muscle-MRS in patients — translational potential.

## Key papers

- [[papers/multi-omics-profiling-cachexia-targeted-tissues]] — Establishes PC/PDH-driven TCA rewiring with INCA flux modelling.

## My understanding

This is the most novel mechanistic finding of the paper, even if the one-carbon framing dominates the abstract. The reframing of muscle wasting as partly an energy-leak phenomenon driven by simultaneous PC + PDH + glutamine anaplerosis is mechanistically rich — it suggests that interventions targeting metabolic flux (rather than proteolysis machinery) could be productive. Pairing with [[concepts/methionine-cycle-myotube-atrophy-hypermetabolism]] makes the methionine ↔ hypermetabolism coupling a load-bearing concept for the cachexia branch of the wiki.
