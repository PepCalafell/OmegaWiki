---
title: "ISGF3-independent transcriptional functions of IRF9"
aliases:
  - "ISGF3-independent IRF9"
  - "non-canonical IRF9 function"
  - "IRF9 STAT1-independent regulation"
  - "IRF9 beyond ISGF3"
  - "IRF9 alternative complexes"
  - "IRF9 STAT2-IRF9 dimer"
  - "IRF9 non-ISG targets"
  - "IRF9 STAT3 STAT5 partnership"
  - "IRF9 macrophage-specific regulation"
  - "STAT2-IRF9 ISGF3-independent axis"
tags: [immunology, irf9, jak-stat, transcription-factor, isgf3, non-canonical-signaling]
maturity: active
key_papers:
  - jak-stat-signaling-maintains-homeostasis-cells
first_introduced: "2019"
date_updated: 2026-05-22
related_concepts: [tonic-baseline-jak-stat-homeostasis]
---

## Definition

The set of IRF9-dependent transcriptional regulatory activities in immune cells that do **not** require formation of the canonical ISGF3 complex (STAT1-STAT2-IRF9 heterotrimer binding ISRE elements). Under homeostatic conditions, IRF9 regulates target genes (e.g. Rdh14, Tprkb, Usb1) that are not classical ISGs and overlap partially with STAT3- and STAT5-regulated genes in macrophages, suggesting IRF9 forms alternative complexes with non-STAT1/2 partners.

## Intuition

ISGF3 is the canonical IRF9 complex, but knocking out IRF9 produces transcriptional changes that look only weakly correlated with knocking out STAT1 or STAT2. The extra IRF9-only signature implies IRF9 has a second life as a partner of other TFs — likely STAT3/STAT5 in macrophages, possibly STAT6 — generating non-ISG regulatory output.

## Variants

- **STAT2-IRF9 dimer (without STAT1)**: documented in prior work (Platanitis 2019), candidate for some baseline targets.
- **IRF9-STAT3 / IRF9-STAT5 partnership**: inferred from high correlation between IRF9 KO and STAT3/STAT5 KO transcriptomes in macrophages.
- **IRF9 solo / unknown partner**: a residual set of IRF9-only effects with no clear correlate.

## When to use

- Reading IRF9 KO phenotypes that don't match STAT1/STAT2 phenotypes.
- Interpreting macrophage-specific IRF9 effects that overlap with STAT3/STAT5 signatures.
- Designing experiments that disambiguate ISGF3-driven vs IRF9-alternative-complex transcription.

## Known limitations

- Direct biochemical evidence of alternative IRF9 complexes is sparse — most evidence is correlative (KO transcriptomes).
- Cell-type specificity is documented but not mechanistic.
- The non-ISG IRF9 targets (Rdh14, Tprkb, Usb1) are diverse and may not share a single regulatory partner.

## Open problems

- IP-MS / proximity-labeling to identify IRF9 partners under homeostasis.
- Test whether STAT3 or STAT5 KO abolishes the IRF9-only target subset.
- Determine if ISGF3-independent IRF9 has analogous roles in human macrophages and TILs.

## Key papers

- [[jak-stat-signaling-maintains-homeostasis-cells]] — Fortelny et al. 2024: identifies IRF9 targets independent of ISGF3 and points to STAT3/STAT5 as candidate macrophage partners.
