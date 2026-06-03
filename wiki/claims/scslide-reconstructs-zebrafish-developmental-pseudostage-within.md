---
title: "scSLIDE reconstructs zebrafish developmental pseudostage within and across timepoints"
slug: scslide-reconstructs-zebrafish-developmental-pseudostage-within
status: supported
confidence: 0.8
tags: [zebrafish, development, pseudostage, fast-muscle, outlier-detection]
domain: developmental biology
source_papers:
  - reconstructing-developmental-disease-progression-sample-level
evidence:
  - source: reconstructing-developmental-disease-progression-sample-level
    type: supports
    strength: moderate
    detail: "On ZSCAPE (~528k cells, 1,025 embryos, 18 timepoints), scSLIDE clustered embryos by stage more sharply than cell-type proportions, flagged temperature-outlier embryos without metadata, and revealed within-timepoint pseudostage (e.g. fast-muscle markers ttn.1/ttn.2/mylpfa/mylpfb elevated in 'late' 22hpf embryos)."
conditions: "ZSCAPE zebrafish embryogenesis atlas (sci-RNA-seq3 + sci-Plex)."
date_proposed: 2026-06-03
date_updated: 2026-06-03
---

## Statement

Applied to the ZSCAPE zebrafish embryogenesis atlas, scSLIDE clusters embryos by developmental stage more sharply than cell-type-proportion clustering, detects outlier embryos (raised at a different temperature) without being told, and reconstructs a continuous "pseudostage" that captures developmental heterogeneity both across and within nominal timepoints.

## Evidence summary

Figure 5 of [[reconstructing-developmental-disease-progression-sample-level]]: pseudostage ordering revealed gradual changes in fast-muscle abundance and in maturation markers (ttn.1, ttn.2, mylpfa, mylpfb) already rising in a subset of "late" 22-hour embryos.

## Conditions and scope

Vertebrate development; unsupervised scSLIDE sufficed because temporal phenotype is strong.

## Counter-evidence

None reported.

## Linked ideas

Developmental analogue of [[continuous-disease-progression-modeling]]; data generated via [[sci-rna-seq3]] and [[sci-plex-chemical-transcriptomics]].

## Open questions

Can pseudostage resolve branch points where lineages diverge within a timepoint?
