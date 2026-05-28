---
title: "Polyamine–hypusine–eIF5A axis as a cell-intrinsic regulator of macrophage tissue residency"
aliases:
  - "polyamine–hypusine axis in macrophages"
  - "DHPS–eIF5A residency axis"
tags:
  - macrophage
  - immunometabolism
  - polyamine
  - hypusine
  - tissue-residency
  - translation
maturity: emerging
key_papers:
  - transition-monocyte-tissue-resident-macrophage-requires
first_introduced: "Carrizo et al., Nature 2026"
date_updated: 2026-05-28
related_concepts:
  - macrophage-ontogeny-resident-vs-monocyte-derived
  - tissue-specific-metabolic-programming-macrophages
---

## Definition

A cell-intrinsic, tissue-agnostic regulatory node in which the polyamine spermidine fuels [[foundations/deoxyhypusine-synthase-dhps]]-mediated hypusination of [[foundations/eif5a-hypusine]], and hypusinated eIF5A in turn enables efficient translation of cell-adhesion and signalling proteins required for monocytes to differentiate into mature tissue-resident macrophages (RTMs) and for mature RTMs to persist.

## Intuition

Whereas tissue-specific factors (GM-CSFR for alveolar, GATA-6 for peritoneal macrophages) instruct *where*-specific identity, the polyamine–hypusine axis acts *across* tissues to license the residency transition itself. Removing DHPS does not block initial macrophage development (CSF1R-driven) but prevents cells from "taking up residence" — they remain immature monocyte-derived macrophages, fail to self-maintain, and are continually replaced by futile monocytic influx.

## Formal notation

spermidine → DHPS → deoxyhypusine-eIF5A → DOHH → hypusine-eIF5A → translation of adhesion/signalling mRNAs (e.g. Il1rl1/ST2, Tnik, Cdh1, L1cam) → RTM differentiation + persistence.

## Variants

- Steady-state residency vs damage-induced replenishment.
- Tissue-specific dependence of individual downstream targets (e.g. ST2 more relevant in peritoneum).

## Comparison

- Distinct from [[concepts/macrophage-ontogeny-resident-vs-monocyte-derived]], which concerns developmental origin rather than the translational mechanism gating the transition.
- Complements metabolic-instruction views in [[concepts/tissue-specific-metabolic-programming-macrophages]] and prior work linking hypusine to macrophage alternative activation and mitochondrial respiration.

## When to use

Invoke when reasoning about cell-intrinsic, metabolism-linked control of macrophage tissue residency, or when interpreting polyamine/hypusine perturbations in myeloid cells.

## Known limitations

- The precise hypusine-dependent transcript set in vivo is not fully resolved.
- Transcriptional vs translational contributions to protein deficits are entangled.
- Possible eIF5A-independent DHPS effects (e.g. on RIPK1) are not excluded.

## Open problems

- How tissue polyamine availability tunes the axis in health, age and disease.
- Whether the axis can be therapeutically modulated to reshape resident-macrophage pools.

## Key papers

- [[papers/transition-monocyte-tissue-resident-macrophage-requires]] — defines the axis as a tissue-agnostic requirement for the monocyte-to-RTM transition.

## My understanding

This reframes resident-macrophage differentiation as partly a *translational* decision: a metabolite (spermidine) gates which adhesion/signalling proteins get made, and that gate determines tissue occupancy. It is an attractive bridge between immunometabolism and macrophage ontogeny.
