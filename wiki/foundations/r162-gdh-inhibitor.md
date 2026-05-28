---
title: "R162 — glutamate dehydrogenase (GDH) inhibitor"
slug: r162-gdh-inhibitor
domain: "pharmacology / metabolism tool compound"
status: mainstream
aliases:
  - R162
  - "GDH inhibitor R162"
  - "purpurin-related GDH inhibitor"
first_introduced: "Jin et al. 2015 Cancer Cell (R162 as GDH inhibitor in tumor metabolism)"
date_updated: 2026-05-28
source_url: "https://pubchem.ncbi.nlm.nih.gov/compound/R162"
---

## Definition

R162 is a small-molecule inhibitor of glutamate dehydrogenase (GDH/GLUD1) used as a metabolic tool compound. By blocking GDH it suppresses glutaminolysis (the conversion of glutamate to α-ketoglutarate), limiting anaplerotic and anabolic use of glutamine carbon and nitrogen. It is used experimentally to test the dependence of a phenotype on GDH-driven glutamine breakdown.

## Intuition

R162 closes the GDH valve, so even if leucine tries to activate GDH, the flux from glutamine into the TCA cycle is blocked. This makes it the counter-reagent to leucine/α-KIC supplementation in pathway-dissection experiments.

## Formal notation

- Target: GDH (GLUD1); inhibits oxidative deamination of glutamate.
- Used in vivo in [[papers/mitochondrial-vhl-rewires-cell-metabolism-hypoxia]] at 20 mg/kg/day.

## Key variants

- Related GDH inhibitors: EGCG (epigallocatechin gallate), bithionol.

## Known limitations

- Limited potency/selectivity typical of metabolic-enzyme tool inhibitors.
- In vivo pharmacokinetics not fully characterized.

## Open problems

- Whether GDH inhibition can be therapeutically leveraged in hypoxic/ischemic disease.

## Relevance to active research

In [[papers/mitochondrial-vhl-rewires-cell-metabolism-hypoxia]], R162 blocked the increased glutaminolysis caused by BCAT-IN-2 and abrogated the protective effect of leucine-driven metabolic rewiring in renal ischemia-reperfusion, confirming GDH as the downstream effector. See [[concepts/leucine-allosteric-gdh-glutaminolysis-activation]] and [[foundations/glud1-glutamate-dehydrogenase]].
