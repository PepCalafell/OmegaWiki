---
title: "Proximity Ligation Assay (PLA)"
slug: proximal-ligation-assay
domain: molecular imaging
status: mainstream
aliases: ["PLA", "Proximity Ligation Assay", "Duolink", "in situ PLA"]
first_introduced: "2006"
date_updated: 2026-06-03
source_url: "https://en.wikipedia.org/wiki/Proximity_ligation_assay"
---

## Definition

The Proximity Ligation Assay (PLA) detects two proteins that are in close physical proximity (typically within ~20–40 nm) in situ. Two primary antibodies against the candidate partners are bound by secondary antibodies conjugated to complementary oligonucleotides (PLA probes). When the two probes are close enough, the oligos can be ligated into a circle, rolling-circle amplified, and detected as a discrete fluorescent spot — each spot marking one proximity/interaction event.

## Intuition

Co-localisation by ordinary immunofluorescence only proves two proteins are in the same region. PLA raises the bar: a signal appears *only* when the two epitopes are within ligation distance, providing much stronger evidence of a direct or near-direct protein–protein interaction at defined subcellular locations (e.g. the cell membrane).

## Formal notation

Not applicable. Readout is a count of fluorescent puncta per cell/area, each ≈ one proximity event.

## Key variants

- Fluorescence PLA (Duolink)
- Brightfield PLA
- Multiplexed PLA for several pairs

## Known limitations

- Requires validated antibody pairs for the two partners
- Proximity (≤~20–40 nm) is necessary but not absolute proof of direct binding
- Sensitive to fixation and epitope accessibility; throughput is limited

## Open problems

- Scaling PLA to many ligand–receptor pairs in parallel
- Quantitative calibration of puncta counts to interaction strength

## Relevance to active research

Used to validate ligand–receptor / protein–protein interactions nominated by spatial transcriptomics (e.g. CD44–FGF2, CD44–MMP9, CD44–FN1), bridging computational interaction predictions and direct molecular evidence.
