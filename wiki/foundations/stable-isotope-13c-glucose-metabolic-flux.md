---
title: "Stable-isotope ¹³C-glucose metabolic flux tracing"
slug: stable-isotope-13c-glucose-metabolic-flux
domain: "metabolomics / isotope tracing"
status: mainstream
aliases:
  - 13C-glucose tracing
  - stable isotope tracing
  - metabolic flux analysis
  - isotopologue tracing
  - 1,2-13C2 glucose tracing
first_introduced: ""
date_updated: 2026-07-24
source_url: "https://doi.org/10.1038/s41598-018-36293-4"
---

## Definition

Stable-isotope ¹³C-glucose tracing feeds cells glucose labeled at defined carbon positions (e.g. [1,2-¹³C₂]-glucose) and measures the resulting mass-isotopologue distributions (M+0, M+1, M+2, …) of downstream metabolites by LC-MS. Because oxidative and non-oxidative routes of glucose catabolism transfer labeled carbons differently, the isotopologue pattern reports the relative flux through competing pathways such as the oxidative pentose phosphate pathway versus glycolysis.

## Intuition

Concentrations tell you how much of a metabolite is present; tracing tells you where its carbons came from. Labeling glucose lets you watch which road the glucose carbon takes — losing its labeled carbon as CO₂ through the oxidative PPP (yielding M+1 pentoses) versus staying in glycolysis (yielding M+2 species).

## Formal notation

With [1,2-¹³C₂]-glucose, oxidative-PPP flux produces M+1 ribose-5-phosphate/ribulose-5-phosphate (one carbon lost as CO₂), whereas glycolytic routing yields M+2 lactate and triose phosphates. Ratios such as lactate M+2/M+1 discriminate PPP shunting from glycolysis. Raw isotopologues are corrected for natural isotope abundance before interpretation.

## Key variants

- [1,2-¹³C₂]-glucose (oxidative vs non-oxidative PPP discrimination).
- Uniformly labeled [U-¹³C₆]-glucose (global flux).
- ¹³C-glutamine / other substrate tracers for orthogonal pathways.

## Known limitations

- Requires isotopologue correction and steady-state or well-defined labeling kinetics.
- Compartmentation and metabolite pool sizes complicate absolute flux inference.
- Short labeling windows capture fast fluxes but miss slow turnover.

## Open problems

- Reconciling tracing-derived relative fluxes with absolute quantitative flux maps.
- Cell-type-resolved tracing in heterogeneous tissue.

## Relevance to active research

¹³C-glucose tracing provided the direct evidence that 4-octyl itaconate reduces oxidative PPP flux (decreased M+1 pentose phosphates) without enhancing glycolysis, pinning the metabolic effect on the oxidative branch downstream of G6PD ([[papers/irg1-itaconate-rewires-macrophage-lung-tumor]]).
