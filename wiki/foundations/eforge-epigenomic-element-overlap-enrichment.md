---
title: "eFORGE"
slug: eforge-epigenomic-element-overlap-enrichment
domain: methods
status: mainstream
aliases: ["eFORGE", "eFORGE v2.0", "experimentally derived Functional element Overlap analysis of ReGions from EWAS"]
first_introduced: "2016"
date_updated: 2026-06-12
source_url: "https://eforge.altiusinstitute.org/"
---

## Definition

eFORGE (experimentally derived Functional element Overlap analysis of ReGions from EWAS) tests whether a set of EWAS-derived CpG sites is enriched for overlap with cell-type-specific regulatory features such as DNase I hypersensitive sites and chromatin states.

## Intuition

Given a list of significant CpGs, eFORGE asks which tissues/cell types and chromatin states (active vs inactive transcription) the sites preferentially mark, helping interpret the functional and cellular context of methylation changes.

## Formal notation

Compares the query CpG set against matched background sets across reference epigenomes (e.g. Roadmap/ENCODE), reporting enrichment significance per cell type and chromatin state.

## Key variants

eFORGE v1 vs v2.0 (expanded reference data and chromatin-state analysis).

## Known limitations

Limited to features in reference panels; interpretation depends on background matching.

## Open problems

Resolving cell-type signal in mixed-tissue (whole blood) EWAS.

## Relevance to active research

Used to show BCG-demethylated CpGs are enriched in active transcription states and to annotate chromatin context of short- vs long-term methylation changes.
