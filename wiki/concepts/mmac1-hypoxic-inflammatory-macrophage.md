---
title: "mMAC1 (hypoxic inflammatory macrophage)"
aliases:
  - "mMAC1"
  - "hypoxic inflammatory macrophage"
  - "hypoxic activated macrophage"
  - "hypoxic LPS-activated macrophage"
  - "hypoxic M(LPS) macrophage"
  - "1% O2 LPS-stimulated MAC"
  - "hypoxia-activated proinflammatory MAC"
  - "in vivo correlate IL4I1 MAC"
  - "hyperinflammatory hypoxic macrophage"
tags:
  - macrophage
  - hypoxia
  - immune-activation
  - tumor-microenvironment
maturity: emerging
key_papers:
  - nf-kb-tet2-promote-macrophage-reprogramming
first_introduced: "Calafell-Segura/de la Calle-Fabregat 2024"
date_updated: 2026-05-06
related_concepts:
  - cluster-c2-hypoxia-hypomethylation-signature
  - nf-kb-mediated-dna-demethylation-hypoxia
  - hif1a-nf-kb-cooperative-chromatin-binding
  - tumor-associated-macrophage-immunosuppression
  - il4i1-tumor-associated-macrophage
  - momac-verse-mnp-verse-atlas
---

## Definition

A monocyte-derived M-CSF MAC differentiated and LPS-activated under 1% O₂ (hypoxia) that displays an enhanced proinflammatory and antigen-presenting phenotype compared to its normoxic (21% O₂) counterpart (mMAC21). Defined by elevated IL-6/TNF-α secretion, reduced IL-10, higher HLA-DR/CD86/CD80, lower CD14/CD206/CD163, and a focal NF-κB-driven cluster-C2 DNA demethylation signature.

## Intuition

Standard TME framing treats hypoxia as immunosuppressive — but mMAC1 is the counterexample. The hypoxic environment selectively enables NF-κB to override TET inhibition at proinflammatory enhancers, producing a MAC that is both metabolically hypoxic (HIF1α-driven) and immunologically hot (NF-κB/STAT/IRF-driven). In vivo, mMAC1 corresponds to IL4I1 MACs (and, to a lesser extent, IL1B Mo and ISG Mo) found in immune-infiltrated bladder and ovarian carcinomas.

## Formal notation

mMAC1 := monocyte → M-CSF (5d, 1% O₂) → LPS (48h, 1% O₂)
- Cluster-C2 hypomethylation: 403 CpGs, NF-κB-motif-enriched, p65-bound
- Transcriptomic cluster E2 enrichment (P=3.03×10⁻⁴⁴ for C2 ↔ E2)
- DoRothEA: HIF1A + STAT2 + IRF1 + RELA regulons co-active
- In vivo correlates: MoMac-VERSE clusters #15 (IL1B Mo), #6 (IL4I1 Mac), #4 (ISG Mo)

## Variants

- iMAC1: hypoxic but unstimulated — partially differentiated, *lower* p65-bound gene activity (paradoxical "immunosuppressed" intermediate state).
- IL4I1 MAC (in vivo): primary correlate, sorted from ovarian tumors, recapitulates C2 hypomethylation.
- IL1B Mo / ISG Mo: weaker correlates, also enriched but with admixture of normoxic mMAC21 features.

## Comparison

vs mMAC21 (normoxic activated): less suppressive of CD8⁺ T cells, less anti-inflammatory, higher antigen presentation.
vs TREM2 MAC: TREM2 is normoxic-leaning and immunosuppressive; mMAC1 is the opposite.
vs FOLR2 MAC: FOLR2 marks tissue-resident MACs with context-dependent role; mMAC1 is monocyte-derived and inflammatory.

## When to use

When characterizing hypoxia-activated MACs in tumor or chronic-inflammation contexts where DNA methylation is profiled alongside transcriptomics. Useful as a deconvolution target for bulk RNA-seq from immune-hot vs immune-cold tumor samples.

## Known limitations

- Defined from in vitro M-CSF MACs; tissue-resident embryonic MACs may not follow the same wiring.
- "Swap" experiments suggest the activation step (not differentiation) is the critical hypoxic window — operational definition may need refinement for chronic in vivo hypoxia.

## Open problems

- Whether GM-CSF-derived or tissue-resident MACs reproduce the C2 hypomethylation under hypoxia.
- TET-isoform specificity (TET2 vs TET1/3) at C2 loci.
- Whether the mMAC1 → T-cell crosstalk is causally responsible for the BLCA/OC survival benefit.

## Key papers

- [[papers/nf-kb-tet2-promote-macrophage-reprogramming]] — original definition and characterization

## My understanding

mMAC1 is a conceptual unit that ties together a coherent set of observations: epigenetic (C2), transcriptional (E2), TF-regulatory (RELA + HIF1A), in vivo correspondence (IL4I1), and clinical (improved BLCA/OC survival). For the HypoxiaVERSE thesis, mMAC1 is one of the central anchor populations.
