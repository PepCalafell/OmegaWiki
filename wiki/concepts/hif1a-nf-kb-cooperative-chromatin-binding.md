---
title: "HIF1α/NF-κB cooperative chromatin binding"
aliases:
  - "HIF1a-p65 co-binding"
  - "HIF1A-RELA chromatin cooperation"
  - "HIF1α and p65 cobound peaks"
  - "non-physical HIF/NF-κB cooperation"
  - "cooperative TF binding without complex formation"
  - "indirect HIF-NF-κB transcriptional cooperation"
  - "HIF1α/p65 enhancer co-occupancy"
tags:
  - transcription-factor
  - chromatin
  - hypoxia
  - inflammation
  - HIF1a
  - NF-kB
maturity: emerging
key_papers:
  - nf-kb-tet2-promote-macrophage-reprogramming
first_introduced: "Calafell-Segura/de la Calle-Fabregat 2024"
date_updated: 2026-05-05
related_concepts:
  - mmac1-hypoxic-inflammatory-macrophage
  - nf-kb-mediated-dna-demethylation-hypoxia
---

## Definition

A pattern of co-occupancy at the same enhancer/promoter regions by HIF1α and p65 (RELA) in hypoxic LPS-activated MACs (mMAC1), without strong correlation of binding intensities (Pearson r=0.13, P=2.5×10⁻⁴). Cobound peaks are enriched in HIF + NF-κB + AP-1 + IRF + ETS motifs and predominantly regulate LPS-signaling genes — distinct from HIF1α-only peaks (glycolysis) or p65-only peaks (immune differentiation/adhesion).

## Intuition

Both TFs land on the same regulatory regions but their binding strengths don't track each other linearly — suggesting the cooperation is grammatical (motif co-occurrence) rather than physical (complex). HIF1α typically arrives first (higher binding in iMAC1 already), and p65 stacks on after LPS, with maximum cobinding in mMAC1. The two factors together control a distinct functional axis from either alone.

## Formal notation

- HIF1α peaks: H1 (hypoxia-induced), H2 (LPS-induced), H3 (both).
- p65 peaks: P1 (single cluster, max in mMAC1).
- ~15% of HIF1α H2 peaks overlap p65 peaks in mMAC1.
- HIF1α-centered analysis at cobound peaks: HIF1α motif dominant, p65 motif present but weaker.
- p65-centered analysis at cobound peaks: HIF1α and p65 motifs roughly equal.
- Pearson correlation of binding intensities at cobound peaks: r=0.13, P=2.5×10⁻⁴ (statistically significant but mechanistically weak).
- Functional separation by GO: HIF1α-only → glycolysis; p65-only → immune adhesion/differentiation; cobound → LPS signaling.

## Variants

- Hypoxia-only cobinding (no LPS): rare, mostly H1-cluster.
- LPS-only cobinding (no hypoxia): dominated by p65 with little HIF1α.
- Hypoxia + LPS cobinding: maximal, defines mMAC1 program.

## Comparison

vs canonical NF-κB/IRF/STAT cobinding at IFN-stimulated response elements: similar grammar of motif co-occurrence, different upstream signal.
vs reported HIF1α/STAT3 or HIF1α/AP-1 cooperation in tumors: shares the "TF stacking under hypoxia" pattern but with a distinct functional output (T-cell-attracting MAC vs angiogenic/stem-like phenotypes).

## When to use

When dissecting transcriptional logic at hypoxic-inflammatory enhancers, especially in immune cells where both HIF1α and NF-κB are stabilized. Useful as a search pattern for ChIP-seq cobinding analyses in any hypoxia + activation experimental design.

## Known limitations

- The non-physical-cooperation conclusion rests on a single linear correlation analysis (r=0.13). Higher-order non-linear coordination (e.g., switch-like dependency) is not formally excluded.
- Co-IP / proximity-ligation experiments would directly test physical interaction; the paper does not perform them.
- The motif analyses depend on HOMER's motif library and may miss non-canonical NF-κB/HIF binding modes.

## Open problems

- Order of TF arrival in time: ChIP-seq is steady-state; live single-cell or sequential ChIP would reveal whether HIF1α primes or merely co-occupies.
- Whether the ~15% cobinding is enriched at C2-demethylated CpGs specifically or at other regulatory elements.
- Whether other hypoxic TFs (HIF2α, EPAS1) participate in this cobinding pattern.

## Key papers

- [[papers/nf-kb-tet2-promote-macrophage-reprogramming]] — defines the cooperation and demonstrates functional separation by binding pattern

## My understanding

The "non-physical cooperation" concept is the paper's most provocative TF-biology claim. It predicts that pharmacologically targeting either TF will only partially break the cooperative output (consistent with PX-478 only partially reducing some target genes). For HypoxiaVERSE, this is a useful template for thinking about how multiple stress-responsive TFs assemble local regulatory grammars without forming dedicated complexes.
