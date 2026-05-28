---
title: "SRC-mediated VHL Y185 phosphorylation enables the mitochondrial VHL–MCCC2 interaction"
aliases:
  - "SRC-VHL Y185 phosphorylation"
  - "VHL Y185 phospho-switch"
  - "SRC-VHL-MCCC2 axis"
tags:
  - hypoxia
  - SRC
  - VHL
  - phosphorylation
  - post-translational-modification
maturity: emerging
key_papers:
  - mitochondrial-vhl-rewires-cell-metabolism-hypoxia
first_introduced: "Li et al. 2026 Cell Metabolism"
date_updated: 2026-05-28
related_concepts:
  - vhl-mccc2-leucine-catabolism-inhibition
  - prmt5-mccc2-arginine-methylation-oxygen-switch
---

## Definition

Under hypoxia, the proto-oncogene tyrosine kinase SRC phosphorylates VHL at tyrosine 185 (Y185). This phospho-mark is required for VHL to bind MCCC2 in the mitochondria; phospho-Y185 is proposed to form a hydrogen bond with MCCC2 R292. SRC expression/activity is itself hypoxia-induced (HIF-1/HIF-2-driven), making Y185 phosphorylation an oxygen-responsive switch.

## Intuition

VHL needs a "phospho-key" (pY185) to dock onto MCCC2. SRC cuts that key only under hypoxia. Without SRC (or with the non-phosphorylatable Y185F mutant), VHL still reaches the mitochondria but cannot grip MCCC2, so leucine breakdown proceeds and the metabolic rewiring collapses.

## Formal notation

- SRC directly phosphorylates VHL Y185 (in vitro kinase assays; blocked by SRC inhibitor eCF506).
- VHL Y185F: phospho-dead, MCCC2-binding-deficient, but TOM22 affinity and HIF functions intact.
- VHL Y185E: phosphomimetic; mitochondrially imported but does not bind MCCC2 unless MCCC2 R292 methylation is removed → reveals dual-PTM requirement.
- SRC hypoxia-induction mediated by both HIF-1 and HIF-2; SRC promoter carries HREs.
- SRC depletion compromises VHL-driven metabolic rewiring and hypoxic proliferation.

## Variants

- SRC also phosphorylates PRMT5 (Y283), inhibiting PRMT5 — a parallel arm of the same switch.
- Among hypoxia-induced tyrosine kinases (SRC, MET, INSR), only SRC phosphorylates VHL.

## Comparison

- Versus canonical VHL regulation: canonical VHL function depends on substrate hydroxylation, not on VHL phosphorylation; this is a new VHL PTM layer.
- Versus MCCC2 methylation arm: SRC-pVHL is the "enabling" PTM on VHL; PRMT5-MCCC2 methylation is the "blocking" PTM on the partner — both must be resolved for binding.

## When to use

Invoke when explaining how oxygen tension is transduced into the VHL–MCCC2 interaction, or when considering SRC inhibition (eCF506) effects on hypoxic metabolism.

## Known limitations

- pY185–R292 H-bond is from docking models, not a solved complex.
- SRC has many substrates; phenotype partly inferred from inhibitor/knockdown.

## Open problems

- Full set of hypoxia-responsive VHL PTMs.
- Whether targeting SRC-pVHL is selective enough for therapy.

## Key papers

- [[papers/mitochondrial-vhl-rewires-cell-metabolism-hypoxia]] — Li et al. 2026.

## My understanding

This converts VHL from a static adaptor into a signal-integrating node: SRC reads oxygen status and licenses VHL's mitochondrial job. The dual-PTM logic (enable VHL + de-block MCCC2) is what makes the switch sharp. Links [[foundations/src-kinase]], [[foundations/ecf506-src-inhibitor]], [[foundations/vhl-von-hippel-lindau]].
