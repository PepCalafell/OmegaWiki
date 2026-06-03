---
title: "CETSA — cellular thermal shift assay"
slug: cetsa-cellular-thermal-shift-assay
domain: "biophysics / target engagement / methods"
status: mainstream
aliases:
  - "CETSA"
  - "cellular thermal shift assay"
  - "thermal shift assay"
  - "thermal stabilization assay"
first_introduced: "Martinez Molina et al. 2013 *Science*"
date_updated: 2026-06-03
source_url: "https://doi.org/10.1126/science.1233606"
---

## Definition

CETSA measures drug–target engagement in intact cells or lysates by exploiting ligand-induced thermal stabilization: a bound small molecule typically raises the melting temperature of its target protein. Cells are treated, heated across a temperature gradient, lysed, and the soluble (non-aggregated) fraction of the target is quantified (by Western blot or, in CETSA-MS / thermal proteome profiling, by mass spectrometry) to detect a stability shift relative to vehicle.

## Intuition

If a compound binds a protein in living cells, that protein resists heat-induced unfolding/aggregation at higher temperatures than in untreated cells. The assay thus gives direct, in-situ evidence of cellular target engagement rather than in-vitro binding.

## Formal notation

- Readout: soluble target fraction vs temperature → melt curve; ΔTm or Δ soluble fraction at fixed temperature(s) = stabilization.
- Western-blot CETSA: band intensity normalized to a control protein (e.g., GAPDH) and to the 37 °C reference.

## Key variants

- Thermal proteome profiling (TPP) / MS-CETSA — proteome-wide melt curves.
- ITDR-CETSA — isothermal dose–response variant.

## Known limitations

- Drug–protein interactions in cells can yield complex effects (increased, unchanged, or even reduced thermal stability), complicating interpretation.
- Limited sensitivity for low-abundance targets.
- A negative result does not exclude engagement (some binding events do not shift Tm).

## Open problems

- Quantitative relation between ΔTm and binding affinity/occupancy.
- Detecting engagement for membrane and intrinsically disordered targets.

## Relevance to active research

[[papers/integrative-epigenome-based-strategy-unbiased-functional]] uses Western-blot CETSA in LPS-stimulated macrophages to confirm that Midostaurin stabilizes TBK1 at its EC50 whereas Momelotinib stabilizes TBK1 only at 10×EC50, corroborating kinobeads affinities and the inferred TBK1-mediated suppression of Ifnb1.
