---
title: "GISTIC 2.0 — Genomic Identification of Significant Targets in Cancer"
slug: gistic2-copy-number
domain: "methods / genomics"
status: mainstream
aliases:
  - "GISTIC"
  - "GISTIC 2.0"
  - "GISTIC2"
  - "Genomic Identification of Significant Targets in Cancer"
  - "CNA caller GISTIC"
  - "broad and focal CNA analysis"
first_introduced: "Mermel et al. 2011 Genome Biology (GISTIC 2.0)"
date_updated: 2026-05-25
source_url: "https://software.broadinstitute.org/cancer/cga/gistic"
---

## Definition

A widely used algorithm and tool from the Broad Institute that identifies genomic regions of significant copy-number amplification or deletion in cancer cohorts, distinguishing focal events from broad arm-level events and assigning gene-level CNA calls based on user-defined thresholds.

## Intuition

GISTIC turns continuous segmented copy-number data (SCNA) into discrete amplification / deletion calls per gene and per cohort, providing per-sample CNA matrices for downstream comparison across groups.

## Formal notation

- Inputs: per-sample segmented copy-number profiles (e.g. from TCGA SNP6 or WES).
- Default thresholds in many TCGA workflows: amplification > +0.2, deletion < -0.2 (gene-level log2 ratios).
- G-score per region weights amplitude × frequency × statistical significance.

## Key variants

- Custom q-value and threshold configurations per cancer-type analysis.
- Broad-vs-focal event partitioning.

## Known limitations

- Thresholds are heuristic; soft "broad" calls in low-purity samples are noisy.
- Tumour purity / ploidy adjustment is critical and frequently under-corrected.

## Open problems

- Subclonal CNA inference from bulk data remains under-developed.

## Relevance to active research

GISTIC 2.0 is the default CNA caller in TCGA cohorts. In [[papers/development-hypoxia-responsive-macrophage-prognostic-model]] it provides the gene-level amplification / deletion calls (thresholds ±0.2) that show enriched CNV gains in the high-hypoxia group.
