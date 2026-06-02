---
title: "mcRigor-optimized partition better reveals temporal immune-cell trajectories and corrects gene temporal patterns"
slug: mcrigor-optimized-partition-reveals-temporal-immune
status: supported
confidence: 0.75
tags: [single-cell, metacell, mcRigor, trajectory, Zman-seq, tumor-immunity]
domain: single-cell-methods
source_papers:
  - mcrigor-statistical-method-enhance-rigor-metacell
evidence:
  - source: mcrigor-statistical-method-enhance-rigor-metacell
    type: supports
    strength: moderate
    detail: "On Zman-seq intratumoral T/NK cells, mcRigor's optimal partition (SEACells γ=43, DubRate 0.056 vs 0.222 original) gave larger cTET separation of NK transitional stages (0.718 vs 0.538), higher stage correlation (Spearman 0.967 vs 0.954), recovered more time-correlated genes (260 vs 135), and corrected Lag3/Clspn temporal patterns to biologically plausible trends."
conditions: "2431 intratumoral T/NK cells, mouse glioblastoma, time-stamped Zman-seq; improvements held when isolating mcRigor's contribution (MetaCell+mcRigor vs MetaCell)."
date_proposed: 2026-06-02
date_updated: 2026-06-02
---

## Statement

Optimizing the metacell partition with mcRigor sharpens temporal immune-cell trajectories and corrects spurious gene temporal patterns relative to the original published partition.

## Evidence summary

On Zman-seq data (2431 intratumoral T/NK cells, mouse glioblastoma), mcRigor selected SEACells γ = 43 (DubRate 0.056 vs the original 0.222). The optimized partition gave greater cTET separation between earliest- and latest-stage NK metacells (0.718 vs 0.538), stronger stage correlation (Spearman 0.967 vs 0.954), more time-correlated genes (260 vs 135), and corrected Lag3 and Clspn to biologically plausible upregulation trends. A direct MetaCell+mcRigor vs MetaCell-alone comparison confirmed the gains are attributable to mcRigor.

## Conditions and scope

Despite finer granularity (γ = 43 vs 66), the optimized partition still resolved sparsity and recovered all key temporally dynamic gene modules.

## Counter-evidence

None reported.

## Linked ideas

(none yet)

## Open questions

Applicability to other temporal / trajectory technologies and tissues.
