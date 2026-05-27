---
title: "Kupffer–stellate Tgfb1–Decorin homeostatic feedback loop"
aliases:
  - "Kupffer-stellate Tgfb1-Dcn feedback"
  - "stellate cell Decorin feedback loop"
  - "hepatic Tgfb1-Dcn homeostatic loop"
tags:
  - liver
  - macrophage-fibroblast-crosstalk
  - TGFbeta-signaling
  - fibrosis
  - hepatic-homeostasis
maturity: emerging
key_papers:
  - nico-identifies-extrinsic-drivers-cell-state
first_introduced: "Agrawal et al. Nat Commun 2024 (NiCo)"
date_updated: 2026-05-27
related_concepts: []
---

## Definition

A predicted homeostatic negative-feedback loop in the healthy mouse liver in which Kupffer-cell-derived Tgfb1 induces decorin (Dcn) expression in co-localized hepatic stellate cells; secreted Dcn then sequesters the same Tgfβ ligand at the ECM, dampening pro-fibrogenic signaling and preventing premature stellate activation under low-level pathogen or immune-activation stimuli.

## Intuition

Resting Kupffer cells continuously sense gut-derived pathogens and low-grade innate-immune cues, secreting Tgfb1 as part of their homeostatic anti-inflammatory program. Neighboring stellate cells, instead of activating into fibrogenic myofibroblasts, respond by upregulating Dcn — a decoy proteoglycan that captures and inactivates ambient Tgfβ. The result is a self-limiting loop that gates stellate activation: only when chronic injury overwhelms the Dcn-mediated buffer does Tgfβ signaling surpass the activation threshold, triggering collagen production and progression to fibrosis.

## Formal notation

Predicted by NiCo's ridge-regression covariation module: log10P = −3.08 for stellate Fa2 ↔ Kupffer Fa1 (supported by 7,781 co-localized pairs out of 11,881 stellate / 38,932 Kupffer cells in MERSCOPE liver). Inferred ligand-receptor pair: Tgfb1 (KC) — Tgfbr3 (HSC). Validation: smHCR Pearson r=0.59 for Tgfb1–Dcn in co-localized pairs (vs r=0.24 for Clec4f–Dcn baseline); qPCR shows Dcn co-administration significantly dampens TGFβ-induced Col1a1 (P<0.01) and Pdgfrb (P<0.04) in cultured HSCs.

## When to use

When reasoning about mechanisms of stellate-cell quiescence in normal liver, or when interpreting why low-grade chronic inflammation (e.g. early MASH) crosses the activation threshold.

## Known limitations

- In vivo causal manipulation (Dcn KO, KC-specific Tgfb1 KO with stellate readout) not yet performed.
- Tgfbr3 is a "type III TGFβ receptor" with complex signaling roles; the mediator identity is suggestive, not proven.
- Loop derived from a single MERSCOPE liver slice; cross-cohort and human-liver replication needed.

## Open problems

- Threshold modeling of the Tgfb1–Dcn buffer: at what Tgfβ flux does the loop break?
- Whether the same Tgfb1–Dcn loop modulates MASH/NASH progression in vivo.
- Whether analogous Tgfβ–proteoglycan buffers operate in other macrophage–fibroblast pairs (alveolar Mac ↔ lung fibroblast; microglia ↔ brain pericyte).

## Key papers

- [[papers/nico-identifies-extrinsic-drivers-cell-state]] — NiCo prediction + smHCR + qPCR validation.

## My understanding

A clean mechanistic example of how a homeostatic macrophage cytokine output is held in check by a fibroblast-produced decoy. The framing generalizes: for any pro-fibrotic / pro-inflammatory cytokine, look for a niche-paired proteoglycan or soluble decoy receptor in co-localized stromal partners.
