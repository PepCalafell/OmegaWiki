---
title: "Spectrum model of macrophage activation"
aliases:
  - spectrum model of macrophage activation
  - macrophage activation spectrum
  - Xue spectrum model
tags:
  - macrophage
  - immunology
  - transcriptomics
  - activation
maturity: active
key_papers:
  - transcriptome-based-network-analysis-reveals-spectrum
  - transcriptional-regulator-network-human-inflammatory-macrophages
first_introduced: "Xue et al. 2014 Immunity (299-transcriptome resource)"
date_updated: 2026-06-03
related_concepts:
  - m1-m2-polarization-paradigm
  - tpp-chronic-inflammation-macrophage-program
  - macrophage-activation-core-regulatory-hubs
---

## Definition
A model of human macrophage activation in which activation states form a continuous, multidimensional spectrum of at least nine distinct transcriptional programs, rather than the two poles (M1/M2) of the classical polarization paradigm. The model was derived from a resource of 299 human macrophage transcriptomes stimulated with 28 diverse signals and analysed by coregulation networks, SOM clustering, and correlation-coefficient matrices.

## Intuition
Macrophages compute combinations of microenvironmental signals. When only canonical polarizing cytokines (IFN-γ, IL-4) are tested, samples fall on a bipolar axis. Adding stimuli unrelated to M1/M2 — free fatty acids, HDL, glucocorticoids, chronic-inflammation cocktails — pulls samples off that axis, revealing a dense spectrum of states. The M1/M2 axis is thus a low-dimensional projection of a richer space.

## Formal notation
- 299 transcriptomes × 29 conditions; baseline Mb at origin in 3D coregulation space
- 10 major clusters from hierarchically-clustered correlation coefficient matrix (CCM)
- Spectrum reconstructed as sum vectors of CCM clusters in 3D coordinate space (Mb = origin)

## Variants
- Bipolar M1/M2 axis (the special case recovered when only IFN-γ / IL-4 are used)
- Stimulus-tagged M(x) nomenclature (Murray 2014) — a complementary attempt to break the binary
- Single-cell-cluster taxonomies (MoMac-VERSE) — the in-vivo, scRNA-seq successor framing

## Comparison
vs [[m1-m2-polarization-paradigm]]: the spectrum model strictly contains M1/M2 as a 2-point subset and adds ≥7 further programs (e.g. the TPP chronic-inflammation program). vs single-cell taxonomies: the spectrum model is built on bulk in-vitro stimulation under highly standardised conditions, giving cleaner stimulus→program mapping but lacking tissue/ontogeny context.

## When to use
- Interpreting in-vitro macrophage stimulation experiments with non-canonical stimuli
- As the conceptual bridge from the binary M1/M2 ladder to multidimensional single-cell taxonomies
- Mapping in-vivo tissue-macrophage states to defined stimulus programs via module-based GSEA

## Known limitations
- Built from monocyte-derived in-vitro macrophages on a single microarray platform; tissue-resident ontogeny is absent.
- "At least nine" programs is data-set dependent, not a fixed number.
- Bulk transcriptomes average over any cell-to-cell heterogeneity.

## Open problems
- A standard quantitative scoring framework that places any macrophage sample within the spectrum.
- Reconciling the bulk-stimulation spectrum with single-cell in-vivo cluster taxonomies.

## Key papers
- [[papers/transcriptome-based-network-analysis-reveals-spectrum]] — Xue et al. 2014: generated the 299-transcriptome resource and defined the spectrum model extending M1/M2.

## My understanding
This is the foundational bulk-transcriptomic argument that macrophage activation is multidimensional. For thesis framing it is the historical hinge between the M1/M2 paradigm and modern single-cell macrophage taxonomies, and it explicitly identifies the TPP/chronic-inflammation program and a cross-species core signature.
