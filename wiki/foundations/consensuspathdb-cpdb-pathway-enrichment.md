---
title: "ConsensusPathDB (CPDB)"
slug: consensuspathdb-cpdb-pathway-enrichment
domain: methods
status: mainstream
aliases: ["CPDB", "ConsensusPathDB"]
first_introduced: "2009"
date_updated: 2026-06-12
source_url: "http://cpdb.molgen.mpg.de/"
---

## Definition

ConsensusPathDB (CPDB) is an integrated database and web tool for gene-set/pathway over-representation analysis, combining interaction and pathway information from many primary resources (Reactome, KEGG, etc.).

## Intuition

Given a gene list (e.g. genes mapped to significant CpG sites), CPDB reports which curated pathways are statistically enriched, summarizing the biological themes of the hits.

## Formal notation

Hypergeometric over-representation test of the query gene set against pathway gene sets, with multiple-testing correction.

## Key variants

Over-representation vs network-neighborhood-based enrichment.

## Known limitations

Pathway annotation bias toward well-studied genes; redundancy across source databases.

## Open problems

Harmonizing overlapping pathway definitions across sources.

## Relevance to active research

Used for pathway enrichment of genes mapped to BCG- and trained-immunity-associated CpG sites (e.g. kisspeptin receptor system, mTOR, VEGFA-VEGFR2).
