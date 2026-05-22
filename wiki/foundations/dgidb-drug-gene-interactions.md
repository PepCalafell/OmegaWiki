---
title: "DGIdb — Drug-Gene Interaction Database"
slug: dgidb-drug-gene-interactions
domain: methods/pharmacogenomics
status: mainstream
aliases:
  - DGIdb
  - drug-gene interaction database
  - DGI database
  - drug-target interaction resource
  - upregulator-downregulator gene drug
  - DGIdb interaction types
first_introduced: "Griffith 2013 Nat Methods"
date_updated: 2026-05-22
source_url: "https://www.dgidb.org"
---

## Definition
DGIdb aggregates curated drug-gene interactions from public sources (DrugBank, ChEMBL, TTD, literature mining) and annotates each interaction with a directional type (inhibitor, activator, agonist, antagonist, ...) so downstream tools can know which gene a drug upregulates or downregulates.

## Intuition
Drug-response data alone tells you whether a cell line dies; to translate that into mechanism you need to know which genes the drug touches and how. DGIdb provides that mapping at scale.

## Key variants
- API access (drug → genes, gene → drugs)
- TSV/JSON bulk downloads
- Interaction-type filtering (e.g. only "inhibitor" relationships)

## Known limitations
- Annotation quality varies by source
- Many small-molecule mechanisms remain unmapped
- Drug aliases / brand names complicate matching

## Open problems
- Integrating off-target interactions consistently
- Quantitative annotation (Kd, IC50) beyond binary directionality

## Relevance to active research
[[papers/spatial-transcriptomics-reveals-distinct-conserved-tumor]] uses DGIdb to identify 140 drugs with annotated up/down gene effects to feed into the Dynamo in-silico perturbation pipeline.
