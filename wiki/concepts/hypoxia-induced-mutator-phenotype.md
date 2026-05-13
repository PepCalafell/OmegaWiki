---
title: "Hypoxia-induced mutator phenotype"
aliases:
  - hypoxia mutator phenotype
  - cycling hypoxia mutator
  - hypoxia error-prone polymerase induction
  - translesion synthesis under hypoxia
  - REV1 hypoxia
  - low-fidelity DNA polymerase induction
  - hypoxia-driven point mutations
  - hypoxia APOBEC mutagenesis
  - hypoxia ROS-ATM-MRE11 mutagenic axis
  - hypoxia-elevated SNV burden
  - hypoxia frameshift insertions
  - hypoxic clonal mutator selection
tags:
  - hypoxia
  - mutational-signatures
  - genomic-instability
maturity: stable
key_papers:
  - tumour-hypoxia-driving-genomic-instability-tumour
  - hypoxic-microenvironment-cancer-molecular-mechanisms-therapeutic
first_introduced: "2003"
date_updated: 2026-05-13
related_concepts:
  - hypoxia-inhibits-dna-repair-pathways-hr
  - hypoxia-genomic-instability-pga
---

## Definition

Hypoxia produces a heritable elevation of point-mutation rate (a "mutator phenotype") via three converging mechanisms: (1) HIF1-dependent induction of low-fidelity translesion-synthesis polymerases that bypass lesions during replication; (2) ROS-driven ATM–MRE11 degradation of nascent DNA at stalled forks under HR-deficient conditions, forcing error-prone repair; (3) APOBEC editing of exposed ssDNA at stalled forks during cycling hypoxia.

## Intuition

Cycling hypoxia (anoxia-reoxygenation) is more mutagenic per cycle than chronic hypoxia, because ROS bursts plus ssDNA exposure activate the ATM–MRE11 axis and feed APOBEC. Cancer cell lines passaged 20 generations at 1% O2 acquire elevated TMB and frameshift insertions.

## Variants

- Translesion synthesis–driven SNV gain (HIF1-dependent)
- APOBEC-driven kataegis (cycling hypoxia)
- MRE11-mediated fork-degradation mutagenesis (chronic hypoxia + HR deficit)

## When to use

Use to explain elevated TMB / SBS6 / SBS2 / SBS13 in hypoxic tumours without classical DDR mutations, or to motivate hypoxia-modulated therapy responses.

## Known limitations

Mutator phenotype is partially reversible upon reoxygenation; mechanistic contributions of each axis quantitatively unresolved.

## Open problems

- Quantifying per-cycle mutation gain in cycling vs chronic hypoxia in vivo
- Whether the mutator phenotype is the dominant driver of clonal selection or whether secondary epigenetic plasticity dominates

## Key papers

- [[papers/tumour-hypoxia-driving-genomic-instability-tumour]]

## My understanding

Pairs directly with [[concepts/hypoxia-inhibits-dna-repair-pathways-hr]] — repair suppression alone is insufficient; cells must also acquire and survive mutations, which requires the polymerase and ROS–MRE11 axes. This is the "engine" behind hypoxic clonal evolution.
