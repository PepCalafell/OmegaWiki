---
title: "Coordinated multi-tissue host response in cancer cachexia — multi-omics integration framing"
aliases:
  - "multi-tissue coordinated metabolome cachexia"
  - "spatio-temporal multi-omics cachexia framework"
tags:
  - multi-omics
  - metabolomics
  - transcriptomics
  - isotope-tracing
  - cachexia
  - multi-tissue
  - integration
maturity: emerging
key_papers:
  - multi-omics-profiling-cachexia-targeted-tissues
first_introduced: "Morigny et al. 2026 (Nat Metab)"
date_updated: 2026-05-27
related_concepts:
  - one-carbon-metabolism-cachexia-tissue-overarching
  - muscle-glucose-hypermetabolism-cachexia-tca-rewiring
---

## Definition

The methodological + conceptual framing that *coordinated host responses* in cachexia can be detected only by integrating polar metabolomics, bulk transcriptomics and in vivo isotope tracing across multiple tissues (plasma, liver, eWAT, iWAT, heart, GC muscle, soleus, tumour) at three temporal stages (control, pre-cachectic, cachectic) — and that no single tissue or single -omics layer would have revealed the tissue-overarching one-carbon axis.

## Intuition

Cachexia is a multi-organ syndrome but previous studies sampled only one or two tissues + one -omics layer. The conceptual contribution is that *coordination* is a feature only visible at the level of integrated data — individual hits (e.g., NNMT in Mizuno et al., sarcosine in earlier metabolomics) had been described, but the realisation that all host tissues + tumour reorganise the *same* pathway in parallel required multi-tissue + multi-omics + pseudo-time + pathway-integration analysis.

## Formal notation

- Tissues sampled (C26 model): plasma, liver, eWAT, iWAT, heart, GC muscle, soleus, tumour.
- Time points: Ctrl, Non-cax, Pre-cax, Cax (n = 4 per group).
- Data layers:
  - Polar metabolomics: LIMeX pipeline; ~200-300 metabolites/tissue retained.
  - Bulk RNA-seq: 5 tissues; ~340 commonly altered genes across Cax tissues.
  - 13C6-glucose tracing: 1 h post i.p. injection; isotopologue distributions of TCA intermediates per tissue.
  - INCA 2.3 flux modelling: GC muscle.
- Integration tools:
  - VSClust pseudo-time clustering (8 metabolite-trajectory clusters).
  - IPA combined-omics pathway analysis (Cax vs Ctrl, Cax vs Non-cax).
  - KEGG pathway enrichment of commonly altered metabolites in ≥2 cachexia target tissues.
  - Upstream regulator analysis (IPA) nominating LPS/IL6/TGFB1.
- Conservation testing: 5 additional mouse models (Panc02, 8025, ApcMin, LLC, KPP) + humanised SW480 + patient liver/muscle cohort.

## Variants

- Single-tissue analysis (prior literature): captures individual hits but misses coordination.
- Multi-tissue metabolomics only (refs 10-17): captures the metabolite layer but not the transcription-driver layer.
- Single-cell or spatial transcriptomics (future extension): would refine cell-type contribution.

## Comparison

- Vs the Atlas-of-circadian-metabolism / multi-tissue metabolomics atlases (refs 18-19): similar tissue breadth but normal-physiology vs disease focus.
- Vs the COVID-19 multi-omics serum-organ studies: comparable analytical strategy.

## When to use

- When designing future cachexia studies — this paper sets a methodological floor: ≥6 tissues, ≥3 time points, metabolomics + RNA-seq + isotope tracing.
- When interpreting single-tissue cachexia results: ask which findings replicate in this paper's multi-tissue resource.
- When teaching multi-omics integration: the pseudo-time + IPA upstream regulator workflow is a model example.

## Known limitations

- Only male mice in this paper's primary C26 cohort.
- Bulk -omics; cell-type contribution unresolved.
- 13C-glucose tracing only at 1 h post-injection — temporal resolution of flux dynamics limited.
- INCA modelling has parametric assumptions (steady-state, normalisation to citrate synthase).

## Open problems

- Whether a single-cell version of this design would reveal cell-type-specific drivers within muscle, liver and adipose.
- Whether longitudinal patient sampling could reproduce the pseudo-time signature.
- Whether the WebApp (https://m3cav.metabolomics.fgu.cas.cz/) becomes a community standard for cachexia metabolomics queries.

## Key papers

- [[papers/multi-omics-profiling-cachexia-targeted-tissues]] — The reference dataset and methodology.

## My understanding

This concept is the framing scaffold for the cachexia-as-multi-organ-syndrome view — its principal value to the wiki is as a methodological template. Future cachexia ingests should reference this paper as the high-water-mark resource; gaps (sex, single-cell, longitudinal patient sampling) are the natural axes for follow-up work.
