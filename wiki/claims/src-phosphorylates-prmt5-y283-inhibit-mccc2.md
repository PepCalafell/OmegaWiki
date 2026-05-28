---
title: "SRC phosphorylates PRMT5 Y283 to inhibit MCCC2 R292 dimethylation under hypoxia"
slug: src-phosphorylates-prmt5-y283-inhibit-mccc2
status: supported
confidence: 0.75
tags: [hypoxia,SRC,PRMT5,Y283,MCCC2,methylation,mechanistic]
domain: metabolism
source_papers:
  - mitochondrial-vhl-rewires-cell-metabolism-hypoxia
evidence:
  - source: mitochondrial-vhl-rewires-cell-metabolism-hypoxia
    type: supports
    strength: moderate
    detail: "Quote (p.183-184): 'SRC overexpression established the VHL-MCCC2 interaction in normoxia after HIF1A depletion by targeting Y283 instead of other reported phospho-sites on PRMT5... SRC inhibited MCCC2 R292 dimethylation only under hypoxia. The non-phosphorylatable PRMT5 Y283F mutation or SRC depletion restored the MCCC complex assembly.' (Fig. 6N, S8D-M)."
conditions: "HEK293; PRMT5 Y283F mutant; shSRC; tyrosine phosphorylation represses PRMT5 activity (prior literature)."
date_proposed: 2026-05-28
date_updated: 2026-05-28
---

## Statement

SRC phosphorylates PRMT5 at Y283 to repress PRMT5 activity, lowering MCCC2 R292 dimethylation under hypoxia — the second SRC-controlled arm (alongside VHL Y185) that converges to license the VHL–MCCC2 interaction.

## Evidence summary

Reported in [[papers/mitochondrial-vhl-rewires-cell-metabolism-hypoxia]] (Fig. 6N, S8D–M). PRMT5 Y283F mutant, SRC overexpression/depletion.

## Conditions and scope

Links the SRC and PRMT5 arms via a single upstream kinase; PRMT5 levels are constant across O₂, regulated by PTM.

## Counter-evidence

None within scope.

## Linked ideas

Supports [[concepts/prmt5-mccc2-arginine-methylation-oxygen-switch]] and [[concepts/src-vhl-y185-phosphorylation-mitochondrial-axis]].

## Open questions

- How oxygen tension and SRC jointly tune PRMT5 in vivo.
