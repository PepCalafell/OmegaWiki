---
title: "Epigenetic potential"
aliases:
  - unrealized epigenetic potential
  - epigenetic potential
tags:
  - epigenetics
  - chromatin-accessibility
  - macrophage
  - gene-regulation
maturity: emerging
key_papers:
  - integrated-time-series-analysis-high-content
first_introduced: "Traxler et al. 2025 Cell Systems (operationalized from prior open-chromatin priming concepts)"
date_updated: 2026-06-04
related_concepts:
  - open-chromatin-predefined-macrophage-activation-tr
  - relative-transcriptional-abundance
---

## Definition
Epigenetic potential is the presence of promoter-associated open chromatin in excess of a gene's current transcriptional activity — i.e., chromatin accessibility higher than expected given the gene's observed expression. It marks genes that are "loaded" for rapid transcriptional upregulation but not yet actively transcribed (unrealized potential).

## Intuition
Open chromatin acts as a pre-set launchpad. A gene with high epigenetic potential can be switched on quickly upon stimulation without first remodeling its chromatin, whereas genes lacking such potential upregulate more slowly because they must first open their promoters.

## Formal notation
For a gene g, quantify expression E(g) (RNA-seq) and promoter accessibility A(g) (ATAC-seq) on normalized, batch-corrected scales. A gene is "divergent" toward epigenetic potential when A(g) ≫ expected(A | E) — accessibility exceeds the level predicted from expression among genes of similar profile. The complementary deviation is [[relative-transcriptional-abundance]].

## Variants
- Realized vs unrealized potential: potential present at baseline that is (or is not) converted into transcription upon stimulation.
- Build-up of potential: genes (e.g. cell-cycle/DNA-replication clusters) that decrease transcription while retaining accessibility, banking potential for later reactivation.

## Comparison
Distinct from the [[open-chromatin-predefined-macrophage-activation-tr]] concept (Schmidt/Schultze), which describes constitutively accessible promoters of the macrophage TR network; epigenetic potential is a continuous, per-gene quantitative divergence metric between accessibility and expression.

## When to use
When integrating paired chromatin-accessibility and expression time series to explain why some genes respond faster than others, or to nominate poised regulatory programs.

## Known limitations
Defined on promoter accessibility only (enhancers not directly captured); relative metric depends on the reference gene population.

## Open problems
Which regulators establish, maintain, and realize epigenetic potential, and whether it generalizes beyond macrophages.

## Key papers
- [[papers/integrated-time-series-analysis-high-content]] — defines and quantifies epigenetic potential across six macrophage immune stimuli.

## My understanding
A clean, measurable formalization of "poised chromatin" that complements rather than replaces transcription-only readouts; pairs naturally with relative transcriptional abundance as two opposite divergence directions.
