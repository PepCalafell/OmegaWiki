---
title: "RiboTag (ribosome-engaged transcript sequencing)"
slug: ribotag-ribosome-profiling
domain: "method / translatomics"
status: mainstream
aliases:
  - "RiboTag"
  - "HA-tagged ribosome immunoprecipitation"
  - "Rpl22-HA"
first_introduced: "Sanz et al., PNAS 2009"
date_updated: 2026-05-28
source_url: ""
---

## Definition

RiboTag is a Cre-dependent mouse system in which the ribosomal protein Rpl22 carries an HA epitope upon recombination, allowing cell-type-specific immunoprecipitation of ribosomes and sequencing of ribosome-associated (translated) transcripts. It reports the translatome of a defined cell population in vivo without cell sorting.

## Intuition

Whereas bulk/scRNA-seq measures transcript abundance, RiboTag measures which transcripts are actually engaged by ribosomes — making it the assay of choice to detect translational control (e.g. transcripts that drop off ribosomes when a translation factor is impaired) rather than transcriptional change.

## Formal notation

n/a

## Key variants

- Combined with myeloid ([[foundations/lysm-cre]]) Cre for macrophage translatomes.
- Input (total) vs HA-pulldown (ribosome-engaged) comparison.

## Known limitations

- Input fraction includes non-target cells when sorting is omitted.
- Cannot distinguish elongation stalling from initiation defects directly.

## Open problems

- n/a

## Relevance to active research

RiboTag in WT vs DHPS-deficient macrophages identified 13 transcripts (including Il1rl1, Tnik, Icos, Cd28) significantly reduced on ribosomes, nominating hypusine-eIF5A-dependent translation targets relevant to tissue residency.
