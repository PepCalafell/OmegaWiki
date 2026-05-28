---
title: "VHL–MCCC2 binding inhibits leucine catabolism under hypoxia"
aliases:
  - "VHL-MCCC2 interaction"
  - "VHL inhibition of leucine catabolism"
  - "mitochondrial VHL MCCC2 axis"
tags:
  - hypoxia
  - VHL
  - MCCC2
  - leucine
  - BCAA-metabolism
maturity: emerging
key_papers:
  - mitochondrial-vhl-rewires-cell-metabolism-hypoxia
first_introduced: "Li et al. 2026 Cell Metabolism"
date_updated: 2026-05-28
related_concepts:
  - mitochondrial-vhl-noncanonical-hypoxia-function
  - leucine-allosteric-gdh-glutaminolysis-activation
  - prmt5-mccc2-arginine-methylation-oxygen-switch
---

## Definition

Inside hypoxic mitochondria, VHL binds MCCC2 (the β subunit of the leucine-degrading enzyme MCCC) and disrupts MCCC1–MCCC2 holoenzyme assembly, thereby inhibiting the rate-limiting carboxylation step of leucine catabolism. The result is leucine accumulation, which serves as the upstream cause of downstream metabolic rewiring.

## Intuition

VHL acts as a wedge that pries apart the MCCC complex. With the leucine-breakdown machine jammed, leucine piles up. The phenotype of VHL is reproduced simply by depleting MCCC2 — confirming MCCC2 inhibition is the operative mechanism.

## Formal notation

- VHL recognizes a tri-residue motif (184–186) of VHL for MCCC2 binding; VHL Y185 is critical.
- VHL binds MCCC2 region 269–300; docking suggests an H-bond between phospho-VHL Y185 and MCCC2 R292.
- VHL WT (not import-dead VHL M2) reduces MCCC1–MCCC2 affinity under hypoxia.
- MCCC2 depletion phenocopies VHL WT growth promotion in hypoxia (not normoxia).

## Variants

- VHL Y185F: import-competent but MCCC2-binding-deficient → loss of metabolic phenotype.
- MCCC2 R292Q: cannot bind VHL → recovers MCCC complex.
- Type 2B VHL mutants: enhanced VHL–MCCC2 association, stronger MCCC disruption.

## Comparison

- Versus SIRT4–MCCC1 regulation: SIRT4 loss disrupts MCCC via MCCC1 acylation; here VHL disrupts MCCC via direct MCCC2 binding under hypoxia.
- Versus canonical VHL substrate recognition: no hydroxyproline degron — MCCC2 lacks the hydroxylated prolines VHL classically reads.

## When to use

Invoke when explaining how hypoxic cells suppress leucine oxidation, or how VHL status changes BCAA flux independently of HIF.

## Known limitations

- Direct structural confirmation of the VHL–MCCC2 interface is modeled, not solved.
- Mostly cell-line evidence plus knock-in mouse.

## Open problems

- Whether VHL similarly regulates other carboxylases/mitochondrial enzymes.
- Quantitative contribution of MCCC inhibition vs other hypoxic metabolic changes.

## Key papers

- [[papers/mitochondrial-vhl-rewires-cell-metabolism-hypoxia]] — Li et al. 2026.

## My understanding

The MCCC2-depletion phenocopy is the strongest piece of evidence here: it converts a correlation (VHL binds MCCC2) into causation (inhibiting MCCC2 is sufficient). Links [[foundations/mccc2-3-methylcrotonyl-coa-carboxylase]], [[foundations/leucine-bcaa]], [[foundations/vhl-von-hippel-lindau]].
