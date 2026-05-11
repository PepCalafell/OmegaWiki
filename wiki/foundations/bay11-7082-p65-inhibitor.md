---
title: "BAY11-7082 — NF-κB / IκB kinase α (IKKα) covalent inhibitor"
slug: bay11-7082-p65-inhibitor
domain: "pharmacology"
status: mainstream
aliases:
  - "BAY11-7082"
  - "BAY 11-7082"
  - "BAY-11-7082"
  - "(E)-3-(4-Methylphenylsulfonyl)-2-propenenitrile"
  - "IκBα phosphorylation inhibitor"
  - "p65 inhibitor"
  - "NF-κB inhibitor BAY"
  - "IKKα inhibitor BAY11"
first_introduced: "Pierce et al. 1997 (J Biol Chem)"
date_updated: 2026-05-11
source_url: "https://pubchem.ncbi.nlm.nih.gov/compound/5353431"
---

## Definition

BAY11-7082 is a small-molecule covalent inhibitor of IκBα phosphorylation that blocks canonical NF-κB activation by preventing IκBα proteasomal degradation and consequent p65 (RELA) nuclear translocation. It is widely used as a tool compound to silence canonical NF-κB signaling in vitro.

## Intuition

If IκBα cannot be phosphorylated, p65 stays sequestered in the cytoplasm. BAY11-7082 covalently modifies cysteine residues on IKKα and IκBα, locking the inhibitory complex in place. It is more potent on the canonical p65/p50 axis than on the non-canonical RelB/p52 axis.

## Formal notation

- Chemical formula: C₁₀H₉NO₂S, MW ~ 207.25 Da
- Covalent target: cysteine residues on IKKα and IκBα (Michael acceptor sulfone)
- Typical in vitro doses: 1-25 μM (3-24 h)
- IC₅₀ for IκBα phosphorylation: ~10 μM (cell-context-dependent)

## Key variants

- BAY11-7085 (related sulfone, similar mechanism)
- Other p65/NF-κB tool inhibitors: TPCA-1 (IKK2-selective), IKK-16, JSH-23 (nuclear translocation inhibitor)

## Known limitations

- BAY11-7082 has well-documented off-target effects: glutathionylation, GSDMD inhibition, ROS modulation, ubiquitin C-terminal hydrolase inhibition.
- Cysteine-modifying mechanism makes selectivity poor at higher doses.
- Cell death is often confounding at >25 μM.

## Open problems

- Cleaner selective p65 / RELA chemical-genetic tools (proximity-induced KO, dTAG).
- In vivo PK / safety remains a limit for therapeutic translation.

## Relevance to active research

Used in Calafell-Segura et al. 2024 ([[papers/nf-kb-tet2-promote-macrophage-reprogramming]]) to demonstrate that p65 inhibition — but not HIF1α inhibition (PX-478) — blocks hypoxia-specific C2 DNA demethylation in mMAC1. Establishes p65 as the necessary driver of NF-κB-mediated DNA demethylation under hypoxia.
