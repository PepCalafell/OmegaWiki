---
title: "Type 2B VHL missense mutations confer mitochondrial gain-of-function in ccRCC"
aliases:
  - "type 2B VHL mitochondrial gain-of-function"
  - "VHL missense mutation mitochondrial metabolism"
  - "VHL mutation subtype metabolic phenotype"
tags:
  - VHL
  - ccRCC
  - kidney-cancer
  - hypoxia
  - clinical-correlation
maturity: emerging
key_papers:
  - mitochondrial-vhl-rewires-cell-metabolism-hypoxia
first_introduced: "Li et al. 2026 Cell Metabolism"
date_updated: 2026-05-28
related_concepts:
  - mitochondrial-vhl-noncanonical-hypoxia-function
  - vhl-mccc2-leucine-catabolism-inhibition
---

## Definition

Clear cell renal cell carcinoma (ccRCC) VHL mutations partition by subtype, and the subtypes differ in mitochondrial (non-canonical) VHL function. Type 1 (frameshift/nonsense) mutations yield absent/truncated VHL that loses both HIF degradation and mitochondrial function. Type 2A missense mutants retain HIF degradation. Type 2B missense mutants (except R167Q) show increased TOM22 affinity, enhanced mitochondrial enrichment, stronger VHL–MCCC2 association, greater leucine-driven glutaminolysis, and faster tumor growth — a mitochondrial gain-of-function that is HIF-independent.

## Intuition

Not all VHL mutations are simple loss-of-function. Some missense mutants (type 2B) actually do the mitochondrial job better — relocating more efficiently and disrupting MCCC harder — which helps hypoxic tumor growth. This reframes certain VHL "mutations" as metabolic gain-of-function for the cancer.

## Formal notation

- Type 1 (frameshift/nonsense): truncated/absent VHL; TCGA-KIRC tumors progress slower.
- Type 2A (Y112H, A149T, T157I): retain HIF degradation, inhibit leucine degradation/promote glutaminolysis like WT.
- Type 2B (Y98N, W117R, R167Q): missense; high ccRCC risk. Y98N/W117R show ↑TOM22 affinity, ↑mito enrichment, ↑VHL-MCCC2, ↑hypoxic growth; R167Q is an exception.
- Y185F co-mutation suppresses tyrosine phosphorylation of type 2B mutants (links to SRC arm).
- Xenografts (A498 ccRCC): type 2B mutants grow faster than type 1/vector with comparable intratumoral hypoxia.
- TCGA-KIRC: SRC/PRMT5/MCCC2 survival correlation stronger in missense-VHL than frameshift/nonsense tumors.

## Variants

- R167Q (type 2B) behaves as an exception (no enhanced mitochondrial gain).
- Type 2A vs 2B distinction maps onto canonical (HIF) vs non-canonical (mitochondrial) retention.

## Comparison

- Versus canonical VHL-loss model of ccRCC: canonical model attributes ccRCC to HIF-2α hyperactivation; this adds a HIF-independent mitochondrial-metabolism axis that distinguishes mutation subtypes.

## When to use

Invoke when interpreting VHL mutation subtype, ccRCC progression differences, or non-HIF mechanisms of VHL-related tumorigenesis.

## Known limitations

- Clinical evidence is correlative (TCGA cohorts, n≈109 per group) plus xenografts; no dedicated patient trial.
- Subtype assignments and exceptions (R167Q) suggest residue-level complexity not fully resolved.

## Open problems

- Whether mutation-subtype-stratified metabolic targeting (SRC/BCAT/GDH) benefits ccRCC patients.
- Mechanistic basis of the R167Q exception.

## Key papers

- [[papers/mitochondrial-vhl-rewires-cell-metabolism-hypoxia]] — Li et al. 2026.

## My understanding

The clinical anchor of the paper: it elevates the mitochondrial-VHL story from cell biology to a tumor-relevant, mutation-subtype-specific axis, and offers a metabolic rationale (SRC-PRMT5-MCCC2) for why missense (2B) ccRCC behaves differently from truncating (type 1). Links [[foundations/vhl-von-hippel-lindau]], [[foundations/tcga-the-cancer-genome-atlas]].
