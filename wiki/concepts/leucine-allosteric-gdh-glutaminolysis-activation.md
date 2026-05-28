---
title: "Leucine accumulation allosterically activates GDH to drive glutaminolysis in hypoxia"
aliases:
  - "leucine-GDH glutaminolysis axis"
  - "leucine allosteric GDH activation"
  - "leucine-driven glutaminolysis"
tags:
  - hypoxia
  - leucine
  - GDH
  - glutaminolysis
  - lipogenesis
  - nucleotide-synthesis
maturity: emerging
key_papers:
  - mitochondrial-vhl-rewires-cell-metabolism-hypoxia
first_introduced: "Li et al. 2026 Cell Metabolism (in the mitochondrial VHL context)"
date_updated: 2026-05-28
related_concepts:
  - vhl-mccc2-leucine-catabolism-inhibition
  - mitochondrial-vhl-noncanonical-hypoxia-function
---

## Definition

Mitochondrial leucine that accumulates when leucine catabolism is blocked allosterically activates glutamate dehydrogenase (GDH/GLUD1), accelerating glutaminolysis. The enhanced glutamine breakdown supplies carbon (reductive lipogenesis → palmitate/stearate) and nitrogen (nucleotide synthesis) needed for hypoxic cell proliferation. Leucine thus links BCAA status to glutamine metabolism, substituting leucine-derived acetyl-CoA with a larger glutamine-derived supply.

## Intuition

Rather than burning leucine for a small amount of acetyl-CoA (which would raise cytotoxic ROS under hypoxia), the cell hoards leucine and uses it as a signal that turns up glutaminolysis — a more productive source of lipids and nucleotides. The leucine-insensitive GDH mutant (R204M) breaks this link, proving the allostery is required.

## Formal notation

- Leucine (1–10 μM, physiological) dose-dependently raises GDH activity; isoleucine/valine do not.
- GDH R204M (human; ≈ bovine R207M): leucine-unresponsive, basal activity intact.
- R204M reconstitution abolishes VHL-promoted reductive glutaminolysis and growth in hypoxia.
- Glutamine deprivation removes VHL/MCCC2-driven growth advantage; citrate + nucleosides rescue VHL-deficient cells.
- mTOR is NOT the relevant leucine output here: hypoxia represses mTOR; leucine repletion fails to activate mTOR.

## Variants

- Reductive (hypoxic) vs oxidative (normoxic) glutaminolysis: GDH WT and R204M both support oxidative glutaminolysis in normoxia, but R204M fails the leucine-dependent reductive route in hypoxia.

## Comparison

- Versus mTOR leucine sensing (sestrin2): the canonical leucine→mTOR axis is suppressed in hypoxia; the leucine→GDH axis dominates.
- Versus direct glutaminase regulation: this axis acts at GDH (glutamate→α-KG), downstream of glutaminase.

## When to use

Invoke when explaining anaplerosis and reductive carboxylation in hypoxic/tumor cells, or when BCAA levels modulate glutamine dependence.

## Known limitations

- Compartment-specific leucine measurement is technically demanding.
- Generality across cell types with different glutamine dependence is untested.

## Open problems

- Quantitative split of glutamine carbon between lipids and nucleotides under this regime.
- Whether the leucine→GDH axis is druggable for hypoxia-related disease.

## Key papers

- [[papers/mitochondrial-vhl-rewires-cell-metabolism-hypoxia]] — Li et al. 2026.

## My understanding

The cleanest mechanistic link in the paper: a single point mutant (GDH R204M) that keeps basal activity but loses leucine sensing severs the whole downstream phenotype. Connects [[foundations/leucine-bcaa]], [[foundations/glud1-glutamate-dehydrogenase]], [[foundations/bcat-branched-chain-aminotransferase]], and the warburg/glutamine literature ([[concepts/warburg-effect-hif1a-glycolytic-reprogramming]]).
