---
title: "Paneth-progenitor Wnt3 signaling to Lgr5+ stem cells"
aliases:
  - "Paneth progenitor Wnt3 niche"
  - "Paneth-stem Wnt3 axis"
  - "nascent Paneth Wnt3 stem feedback"
tags:
  - intestinal-stem-cell-niche
  - Wnt-signaling
  - crypt-base-niche
  - direct-Paneth-from-stem
maturity: emerging
key_papers:
  - nico-identifies-extrinsic-drivers-cell-state
first_introduced: "Böttcher et al. 2021 (direct Paneth-from-stem differentiation); Agrawal et al. Nat Commun 2024 (NiCo niche covariation)"
date_updated: 2026-05-27
related_concepts: []
---

## Definition

A refined model of the small-intestinal crypt-base stem-cell niche in which nascent Paneth-cell progenitors — recently derived from Lgr5+ stem cells via direct differentiation (Böttcher 2021) — supply the Wnt3 ligand that maintains the parental stem-cell pool. The classical "mature Paneth cell as niche cell" view is augmented: it is the *progenitor* state of the Paneth lineage, not the fully mature secretory cell, that delivers the highest Wnt3 signal to neighboring stem cells.

## Intuition

NiCo (Agrawal 2024) detects significant covariation between stem/TA cell Fa1 (loaded with Olfm4, Lgr5, Hopx) and Paneth cell Fa1 (loaded with progenitor markers, not mature Paneth-cell markers). The correlated ligand-receptor axis is Wnt3 (Paneth Fa1) — Fzd7 (stem/TA Fa1). Mature Paneth cells downregulate Wnt3 — visible as a Wnt3 trajectory that decays as Paneth cells mature. The implication: the self-renewing niche is sustained by a sibling-loop in which freshly born Paneth progenitors immediately re-license stemness in adjacent surviving stem cells.

## When to use

When designing intestinal-organoid niche models, interpreting intestinal-regeneration scRNA-seq data, or reasoning about why partial Paneth-cell ablation does not always abolish stemness (mature Paneth cells are not the main Wnt3 source).

## Known limitations

- The Wnt3 trajectory in NiCo is inferred from a single MERFISH dataset; not orthogonally validated in vivo (no lineage tracing of Wnt3-bright Paneth progenitors).
- The dichotomy between "Paneth progenitor" and "mature Paneth" is continuous; threshold definitions are operational.

## Open problems

- Direct live-imaging of Wnt3 transfer from nascent Paneth progenitors to sister stem cells.
- Whether the same logic operates in colon "deep-crypt secretory cells" — Wnt-like-progenitor feedback to colon stem cells.

## Key papers

- [[papers/nico-identifies-extrinsic-drivers-cell-state]] — NiCo evidence for stem/TA Fa1 — Paneth Fa1 covariation with Wnt3–Fzd7 mediation.

## My understanding

A useful refinement on the textbook niche: it is not the differentiated state that signals to the stem cell, but the just-born sibling progenitor. The logic — "the lineage-committed daughter re-licenses the mother" — is reminiscent of mouse hematopoietic and germline niches and may be a general motif of asymmetric stem-cell maintenance.
