---
title: "[13C6]-glucose tracer"
slug: 13c6-glucose-tracer
domain: mass spectrometry / metabolic flux
status: mainstream
aliases:
  - "13C6-glucose"
  - "[U-13C]-glucose"
  - "U-13C6-D-glucose"
  - "uniformly-labelled 13C glucose"
first_introduced: "Stable-isotope tracer methodology; widely deployed for metabolic flux analysis"
date_updated: 2026-05-27
source_url: ""
---

## Definition

[13C6]-glucose (uniformly 13C-labelled D-glucose) is a stable-isotope-labelled glucose tracer where all six carbons are 13C. It enters glycolysis as M+6 glucose, generates M+3 pyruvate, and labels downstream metabolites — providing isotopologue distributions that report on glycolytic, pentose-phosphate, anaplerotic (PC), oxidative (PDH), and one-carbon flux.

## Intuition

By measuring not just total metabolite levels but the mass-isotopologue distribution (M+0, M+1, ..., M+n), 13C6-glucose tracing distinguishes direct glycolytic flux (M+3 → M+2 acetyl-CoA → M+2 citrate via PDH) from anaplerotic flux (M+3 pyruvate → M+3 OAA via PC → M+3 citrate). Higher isotopologues (M+4, M+5) accumulate through TCA cycle multi-turn or refeed of labelled OAA. The ratio of M+2 vs M+3 in TCA intermediates is diagnostic of PDH vs PC flux balance.

## Formal notation

- Mass shift: +6 Da from 12C6 baseline.
- Typical in vivo dosing: ~0.5-2 g/kg i.p. in mice; 1 h tissue collection window for short-term flux.
- Typical in vitro dosing: 1-5 mM in DMEM (with or without 12C glucose washout).
- Isotopologue correction: IsoCor (Millard et al.) for natural-13C correction.

## Key variants

- [1,2-13C2]-glucose: distinguishes pentose-phosphate from glycolysis.
- [1-13C]-glucose: lower-cost label for entry into PPP / glycolysis distinction.
- [U-13C5]-glutamine: complementary tracer for glutamine anaplerosis.
- [1-13C]-pyruvate: tests PC vs PDH balance directly (used in C2C12 in [[papers/multi-omics-profiling-cachexia-targeted-tissues]]).

## Known limitations

- 1 h tracer time captures only fast-turnover pools; slow pools (storage carbohydrates, large protein pools) underestimated.
- In vivo enrichment depends on plasma glucose dynamics and competing endogenous unlabelled glucose pools.
- Tissue heterogeneity (cell-type-specific flux) averaged out in bulk MS.

## Open problems

- Whether breath-13CO2 measurements can serve as a non-invasive flux readout in patients.
- Pre-cachexia detection via plasma TCA-isotopologue patterns.

## Relevance to active research

Central tracer in [[papers/multi-omics-profiling-cachexia-targeted-tissues]]: i.p. 13C6-glucose 1 h before tissue collection across all eight tissues revealed elevated TCA-cycle label incorporation (especially higher isotopologues M+3, M+4) in cachectic GC muscle, soleus and heart — establishing muscle glucose hypermetabolism. Combined with [1-13C]-pyruvate tracing in C2C12 to confirm PC activity.
