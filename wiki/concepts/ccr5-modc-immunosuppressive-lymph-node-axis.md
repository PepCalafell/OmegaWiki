---
title: "CCR5-dependent moDC immunosuppressive draining-lymph-node axis"
aliases:
  - CCR5 moDC axis
  - moDC immunosuppression draining lymph node
  - Ly6C moDC CCR5 migration
tags:
  - monocyte-derived-dc
  - chemokine
  - immunosuppression
  - cancer-vaccine
  - lung-cancer
maturity: emerging
key_papers:
  - chemokine-defined-macrophage-niches-establish-spatial
first_introduced: "2026"
date_updated: 2026-06-02
related_concepts:
  - chemokine-defined-interstitial-macrophage-division-of-labor
  - im-derived-ccl2-recmac-recruitment-loop
  - tumor-associated-macrophage-immunosuppression
---

## Definition

A protumor circuit in which Ly6C⁺ recruited macrophages differentiate into monocyte-derived dendritic cells (moDCs) that migrate to tumor-draining lymph nodes via CCR5–CCL5 signaling (rather than the CCR7 route used by classical DCs) and act as immunosuppressive antigen-presenting cells, inducing antigen-specific regulatory T cells and limiting cytotoxic T cell responses.

## Intuition

Migratory DCs in the lymph-node T cell zone produce CCL5; CCR5⁺ moDCs follow this gradient into the node. Because conventional DCs use CCR7, selectively removing CCR5 (genetically or pharmacologically) suppresses the moDC arm while leaving protective DC cross-priming intact — converting a suppressive node into a productive one.

## Formal notation

Ly6C⁺ recMac → moDC (CCR5⁺) → [CCL5 from migratory DCs] → draining LN → antigen-specific Treg induction → blunted CD8 antitumor response.

## Variants

- Genetic isolation via competitive Ccr2⁻ᐟ⁻:Ccr5⁻ᐟ⁻ (80:20) vs Ccr2⁻ᐟ⁻:WT mixed bone-marrow chimeras (preserves normal DC representation).
- Pharmacological, windowed disruption via transient [[maraviroc]] during vaccination.

## Comparison

Downstream continuation of the [[im-derived-ccl2-recmac-recruitment-loop]]: IM-derived CCL2 recruits recMacs, whose moDC progeny then suppress in the lymph node. Contrasts with CCR7-dependent conventional DC priming.

## When to use

When designing cancer vaccines / immunotherapies that must avoid monocyte-derived antigen presentation while preserving DC cross-priming.

## Known limitations

- Mouse models; recMac/moDC suppressive identity is context-dependent (inflammatory monocytes can be immunostimulatory in infection).
- Prolonged systemic CCR5 blockade in patients hits many CCR5⁺ populations, unlike the transient windowed approach here.

## Open problems

- Translating transient, monocyte-selective CCR5 blockade to human vaccination schedules.
- Markers to distinguish suppressive vs stimulatory monocyte-derived APCs in tissue.

## Key papers

- [[chemokine-defined-macrophage-niches-establish-spatial]]

## My understanding

The suppressive arm of the division of labor extends beyond the tumor into the draining lymph node; the therapeutic insight is timing — a brief CCR5 block during priming flips the balance toward protective DC immunity.
