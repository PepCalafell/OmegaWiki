---
title: "NF-κB-mediated DNA demethylation in hypoxia"
aliases:
  - "p65-driven hypoxic demethylation"
  - "NF-κB override of hypoxic TET inhibition"
  - "NF-κB-dependent TET-mediated demethylation"
  - "RELA-driven focal hypomethylation"
  - "hypoxia-specific inflammatory demethylation"
  - "p65-tethered TET demethylation at NF-κB enhancers"
  - "stimulus-induced focal demethylation under low O2"
tags:
  - DNA-methylation
  - NF-kB
  - TET
  - hypoxia
  - epigenetics
maturity: emerging
key_papers:
  - nf-kb-tet2-promote-macrophage-reprogramming
first_introduced: "Calafell-Segura/de la Calle-Fabregat 2024"
date_updated: 2026-05-05
related_concepts:
  - cluster-c2-hypoxia-hypomethylation-signature
  - mmac1-hypoxic-inflammatory-macrophage
  - hif1a-nf-kb-cooperative-chromatin-binding
---

## Definition

A focal, locus-restricted active DNA demethylation event driven by p65/RELA binding that proceeds *despite* the global hypoxic suppression of TET activity. Demonstrated in human MACs at cluster C2 (403 CpGs), where NF-κB binding overrides oxygen-dependent TET inhibition and enables α-KG/Fe²⁺-dependent oxidation of 5mC to 5hmC at proinflammatory enhancers.

## Intuition

TET enzymes need O₂ as a cofactor — under 1% O₂, bulk TET-driven demethylation slows down (cluster C1 effect). But NF-κB binding in hypoxic-LPS-activated MACs *recruits or licenses* TET activity at a small focal set of enhancers (cluster C2), so a tiny island of demethylation persists in an otherwise methylation-frozen genome. The mechanism is locally permissive, not globally restorative.

## Formal notation

- Genome-wide TET activity ↓ under hypoxia (cluster C1: bulk MAC-differentiation demethylation blunted)
- Locus-restricted TET activity ↑ under hypoxia + NF-κB activation (cluster C2: 403 CpGs, hypomethylated only in mMAC1)
- p65 inhibition (BAY11-7082) → C2 methylation restored to mMAC21 levels (rescue)
- HIF1α inhibition (PX-478) → no effect on C2 methylation (specificity)
- TET inhibition (4-octyl itaconate) → C2 methylation increased + gene expression decreased (necessity)

## Variants

- Possibly applicable to other inflammatory ligands (P3C, polyI:C, TNF-α, IL-1β all yielded the same hypoxia-amplified expression).
- Cell-type generality unproven — currently established in monocyte-derived M-CSF MACs.

## Comparison

vs Thienpont-2016 (Nature) global hypoxic hypermethylation: that study described bulk hypermethylation; this concept extends the picture by showing that NF-κB carves out a focal exception.
vs trained-immunity epigenetic remodeling: thematically related but mechanistically distinct (trained immunity centers on H3K4me1/H3K27ac persistence; this concept is centered on stimulus-specific TET-DNA demethylation).

## When to use

When analyzing methylation dynamics in stimulated immune cells under low oxygen. The concept predicts a class of "hypoxia-rescued" demethylated CpGs that should appear specifically at NF-κB-bound enhancers in any TLR/cytokine-activated myeloid system in hypoxia.

## Known limitations

- TET isoform specificity not resolved; the inferred "TET2" attribution comes from chemical inhibition (4-octyl itaconate) which is not isoform-specific.
- Time-resolved methylome + transcriptome to nail down ordering (NF-κB binding → TET recruitment → demethylation → expression) not yet performed.
- Whether p65 physically recruits TET2, or whether p65 just stabilizes chromatin in a TET-accessible state, is unknown.

## Open problems

- Mechanism of TET licensing by p65: direct recruitment vs cofactor competition vs chromatin opening.
- Whether the same override exists for AP-1 / IRF1 / STAT2 binding in other epigenetic contexts.
- Generalizability to GM-CSF MACs, dendritic cells, and tissue MACs.

## Key papers

- [[papers/nf-kb-tet2-promote-macrophage-reprogramming]] — defines and pharmacologically validates the concept

## My understanding

This is the load-bearing mechanistic concept of the paper: it reconciles the contradictory hypoxia-immunology literature by saying *both* hypoxic suppression *and* hypoxic boosting can be true simultaneously, depending on whether NF-κB is engaged at a given locus. Important for any HypoxiaVERSE-scope hypothesis about stimulus-specific epigenetic plasticity in low-O₂ tissues.
