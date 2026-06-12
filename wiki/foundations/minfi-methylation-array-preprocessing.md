---
title: "minfi"
slug: minfi-methylation-array-preprocessing
domain: methods
status: mainstream
aliases: ["minfi", "Minfi"]
first_introduced: "2014"
date_updated: 2026-06-12
source_url: "https://bioconductor.org/packages/minfi/"
---

## Definition

minfi is a Bioconductor R package for reading, quality-controlling, normalizing, and analyzing Illumina Infinium DNA-methylation microarray data (450K and EPIC), starting from raw IDAT files.

## Intuition

It provides an end-to-end pipeline from raw scanner output to normalized beta/M-values, including detection-p filtering and background/dye correction, standardizing array preprocessing.

## Formal notation

Outputs beta values β ∈ [0,1] and M-values log2(β/(1−β)); supports functional, quantile, and stratified-quantile normalization.

## Key variants

Functional normalization (funnorm), Noob, SWAN, stratified quantile normalization.

## Known limitations

Does not itself remove cross-reactive/polymorphic probes (requires external lists); batch correction is separate.

## Open problems

Optimal normalization choice for longitudinal designs.

## Relevance to active research

Used to preprocess the 300BCG EPIC-array methylation data prior to EWAS.
