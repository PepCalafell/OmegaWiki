---
title: "TMTpro isobaric multiplexing for single-cell proteomics"
slug: tmtpro-isobaric-multiplexing
domain: "methods / mass spectrometry"
status: mainstream
aliases:
  - TMTpro
  - TMTpro 16-plex
  - TMT isobaric labeling
  - tandem mass tag
  - TMT 11-plex
  - isobaric labeling MS
  - reporter-ion quantification
  - TMTpro 18-plex
  - TMTpro carrier channel
  - peptide carrier scp-MS
first_introduced: "Thompson et al. 2003 *Anal Chem* (TMT 6-plex); TMTpro 16-plex extension by Li et al. 2020"
date_updated: 2026-05-26
source_url: "https://www.thermofisher.com/order/catalog/product/A44520"
---

## Definition

TMTpro (tandem mass tag, "pro" generation) is an isobaric chemical labeling reagent for peptide quantitation by mass spectrometry. Up to 16 (or 18) samples are labeled with chemically identical but isotopically distinct tags; samples are then pooled and analyzed in a single LC-MS/MS run. Quantification comes from low-mass reporter ions released upon HCD fragmentation. In scp-MS, one channel is typically used as a "peptide carrier" (a 200-500× larger amount of bulk peptide) to boost ion statistics for the single-cell channels.

## Intuition

Single cells produce too little peptide for reliable MS detection on their own. Pooling 14 single cells plus a peptide carrier into one MS run multiplies throughput while keeping each single cell's quantification independent via the reporter-ion intensity. The cost is reporter-ion interference (co-isolation) and carrier-channel bias if poorly designed.

## Formal notation

For one MS set in [[papers/mapping-early-human-blood-cell-differentiation]]: 14 single cells (TMTpro-127 to TMTpro-135) + 1 carrier well containing 200-cell equivalent (TMTpro-126), labeled at 13 mM TMTpro for cells and 6 mM for the carrier (paper reports specific concentrations differently — see methods).

## Key variants

- TMTpro 16-plex (default in scp-MS workflows).
- TMTpro 18-plex (most recent extension).
- TMT 11-plex (earlier generation, lower throughput).
- iTRAQ 4-plex / 8-plex (alternative isobaric reagent family).

## Known limitations

- Reporter-ion co-isolation distorts quantification at low signal-to-noise.
- Carrier-channel bias if carrier is too large (>500×) or too dissimilar to single cells.
- Cost per sample is non-trivial relative to label-free or DIA approaches.

## Open problems

- Optimal carrier size and composition for various scp-MS workflows.
- Label-free / plexDIA alternatives that avoid TMT cost and reporter-ion interference.

## Relevance to active research

- Foundational reagent for [[papers/mapping-early-human-blood-cell-differentiation]] scp-MS workflow.
