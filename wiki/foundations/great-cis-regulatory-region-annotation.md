---
title: "GREAT"
slug: great-cis-regulatory-region-annotation
domain: methods
status: mainstream
aliases: ["GREAT", "Genomic Regions Enrichment of Annotations Tool"]
first_introduced: "2010"
date_updated: 2026-06-12
source_url: "http://great.stanford.edu/"
---

## Definition

GREAT (Genomic Regions Enrichment of Annotations Tool) assigns genomic regions (e.g. CpG sites or peaks) to nearby genes using regulatory-domain rules and tests for enrichment of gene ontology and pathway annotations.

## Intuition

Rather than mapping a CpG only to its closest gene, GREAT models cis-regulatory domains so that intergenic regulatory sites are linked to the genes they likely regulate, improving functional interpretation.

## Formal notation

Each gene receives a regulatory domain (basal + extension); region-to-gene association feeds a binomial/hypergeometric enrichment test.

## Key variants

Different regulatory-domain definitions (basal-plus-extension, two-nearest-genes).

## Known limitations

Proximity-based assignment can misattribute distal enhancers; species/genome-build dependent.

## Open problems

Integrating chromatin-contact data for more accurate region-to-gene mapping.

## Relevance to active research

Used to annotate BCG-associated CpG sites to nearby genes for downstream pathway analysis.
