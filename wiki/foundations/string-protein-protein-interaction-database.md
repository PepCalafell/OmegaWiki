---
title: "STRING — protein-protein interaction database"
slug: string-protein-protein-interaction-database
domain: "methods / network biology / functional genomics"
status: mainstream
aliases:
  - STRING
  - STRINGdb
  - STRING database
  - Search Tool for the Retrieval of Interacting Genes/Proteins
first_introduced: "Szklarczyk et al., STRING (Nucleic Acids Research, ongoing since 2000)"
date_updated: 2026-06-10
source_url: "https://string-db.org"
---

## Definition

STRING is a database and web resource of known and predicted protein-protein interactions, aggregating evidence from experiments, curated databases, co-expression, text mining, and genomic context. Each interaction carries a combined confidence score (0-1); a typical cutoff of 0.4 retains medium-confidence edges.

## Intuition

Given a gene list, STRING returns a network whose edges represent functional/physical association evidence, letting you ask whether a set of differentially expressed genes is more interconnected than chance — a proxy for coherent pathway involvement.

## Key variants

- Web interface, REST API, and the `STRINGdb` R/Bioconductor package for programmatic mapping of genes to STRING proteins and subnetwork extraction.

## Known limitations

- Text-mining and co-expression channels introduce indirect or literature-biased edges; combined scores are not direct physical-binding evidence.
- Network connectivity is confounded by study bias toward well-characterized proteins.

## Open problems

- Disentangling causal from merely correlated associations within aggregated evidence channels.

## Relevance to active research

Used to test functional segregation/cohesion of DEG signatures (e.g. normalized-cut analysis of disease-specific gene modules) and for pathway-level interpretation of single-cell findings across the corpus.
