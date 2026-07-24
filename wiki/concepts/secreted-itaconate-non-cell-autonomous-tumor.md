---
title: "Secreted itaconate as a non-cell-autonomous tumor suppressor"
slug: secreted-itaconate-non-cell-autonomous-tumor
type: concept
aliases:
  - paracrine itaconate anti-tumor
  - extracellular itaconate tumor suppression
tags:
  - itaconate
  - macrophage
  - paracrine-signaling
  - tumor-microenvironment
  - lung-cancer
maturity: emerging
key_papers:
  - irg1-itaconate-rewires-macrophage-lung-tumor
first_introduced: "2026"
date_updated: 2026-07-24
related_concepts:
  - irg1-itaconate-g6pd-pentose-phosphate-pathway
  - tumor-associated-macrophage-immunosuppression
  - succinate-itaconate-metabolic-set-point
---

## Definition

The proposition that itaconate produced inside macrophages is exported (via ABCG2) into the tumor microenvironment and acts directly on neighboring cancer cells to suppress their proliferation — a non-cell-autonomous, paracrine metabolic effect — rather than acting only through macrophage-intrinsic immunomodulation.

## Intuition

Cancer epithelial cells do not make itaconate (they lack IRG1). Traditionally itaconate was thought to influence tumors indirectly by tuning macrophage phenotype. This concept says the metabolite itself crosses the intercellular space: macrophage-exported itaconate enters adjacent tumor cells, inhibits their G6PD, and limits their growth. Local macrophage-rich niches can reach effective concentrations despite low bulk extracellular itaconate.

## Formal notation

IRG1⁺ macrophage → itaconate synthesis → ABCG2-mediated export → extracellular itaconate → uptake by adjacent tumor cell → G6PD inhibition → ↓ proliferation. Evidence: ABCG2 knockdown attenuates the anti-proliferative activity of pro-inflammatory macrophage conditioned media; exogenous itaconate suppresses tumor-cell proliferation directly.

## Variants

- Autocrine (macrophage-intrinsic G6PD/PPP control) vs paracrine (export to tumor cells).
- Endogenous secreted itaconate vs pharmacologic 4-octyl itaconate delivery.

## Comparison

Contrasts with the cell-autonomous view of intracellular itaconate action in immune cells; complements the [[concepts/irg1-itaconate-g6pd-pentose-phosphate-pathway]] axis by specifying how the effector metabolite reaches tumor cells. Related to broader TAM-tumor crosstalk in [[concepts/tumor-associated-macrophage-immunosuppression]].

## When to use

When modeling metabolite-level crosstalk in the TME, or when interpreting why itaconate exporter expression (ABCG2) carries prognostic value in tumors.

## Known limitations

- Extracellular itaconate concentrations are generally low; local niche concentrations are inferred, not directly measured in situ.
- Itaconate import mechanism into tumor cells remains undefined.

## Open problems

- Transporters governing itaconate import into recipient cells.
- Whether OXGR1 receptor signaling contributes alongside direct intracellular G6PD inhibition.

## Key papers

- [[papers/irg1-itaconate-rewires-macrophage-lung-tumor]] — demonstrates ABCG2-dependent paracrine anti-tumor itaconate action.

## My understanding

This is the conceptual pivot that lets a macrophage metabolite have a direct tumor-cell-intrinsic effect, and it is what makes ABCG2 (the exporter) a prognostic axis in its own right.
