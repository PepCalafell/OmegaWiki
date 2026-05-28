---
title: "Short linear motif–domain interfaces are enriched among commensal effector–host interactions"
slug: slim-domain-interfaces-enriched-in-hummi
status: supported
confidence: 0.75
tags: [hummi, slim, mimicint, interfaces]
domain: genomics
source_papers:
  - effector-host-interactome-map-links-type
evidence:
  - source: effector-host-interactome-map-links-type
    type: supports
    strength: moderate
    detail: "mimicINT identified 54 SLiM–domain interfaces in HuMMIMAIN; 51 pass ≥1 stringency criterion (P=0.0137, n=10,000) and 22 pass two criteria (P=0.0005). AlphaFold-Multimer gave confident predictions for only 123 pairs (10%)."
conditions: "Template-based SLiM-domain inference (ELM); permutation testing."
date_proposed: 2026-05-28
date_updated: 2026-05-28
---

## Statement

A significant fraction of commensal effector–host interactions are mediated by short
linear motifs binding host domains — interactions that globular structure prediction
tends to miss.

## Evidence summary

[[effector-host-interactome-map-links-type]] (p.447): mimicINT found 54 SLiM-domain
interfaces; 51 pass ≥1 stringency (P=0.0137), 22 pass two (P=0.0005). AlphaFold-Multimer
modelled only ~10% of pairs.

## Conditions and scope

Predictions require validation; template coverage limits discovery.

## Counter-evidence

No host-substrate-motif engagement by effector enzymatic domains found (only one
LxVP/Efe_1–VAC14 example).

## Linked ideas

Defines [[slim-pdz-effector-host-interface]]. Uses [[mimicint-slim-domain-inference]],
[[alphafold-multimer]].

## Open questions

Extent of functional mimicry without sequence similarity.
