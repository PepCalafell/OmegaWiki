---
title: "LPS / Toll-like receptor signaling"
slug: lps-toll-like-receptor-signaling
domain: "immunology / cell-signaling"
status: mainstream
aliases:
  - "LPS"
  - "lipopolysaccharide"
  - "endotoxin"
  - "TLR4 signaling"
  - "Toll-like receptor signaling"
  - "TLR/MyD88 pathway"
  - "TRIF/TRAM signaling"
  - "PAMP signaling"
  - "TLR4-NF-κB axis"
first_introduced: "Medzhitov & Janeway 1997 (TLR-mammalian)"
date_updated: 2026-05-05
source_url: "https://www.uniprot.org/uniprot/O00206"
---

## Definition

LPS is the major outer-membrane component of Gram-negative bacteria; its lipid A moiety is recognized by the TLR4 receptor on innate immune cells. TLR4 engagement activates two parallel adapter pathways: MyD88-dependent (rapid NF-κB and AP-1 activation, proinflammatory cytokine production) and TRIF-dependent (delayed NF-κB and IRF3 activation, type I interferon response). LPS at 100–200 ng/mL is the canonical reagent for in vitro myeloid activation.

## Intuition

LPS is the textbook activator of innate immunity — drop it on macrophages, monocytes, or dendritic cells and within minutes you get IL-6, TNF-α, IL-1β secretion and a major NF-κB-driven gene expression program. It's the experimental shorthand for "inflammatory stimulus."

## Formal notation

- Receptor: TLR4 (with co-receptors MD-2 and CD14)
- Adapters: MyD88 + TIRAP (membrane); TRIF + TRAM (endosomal)
- Outputs: NF-κB (p65/p50), AP-1 (Fos/Jun), IRF3 (type I IFN)
- Time course: NF-κB target genes peak ~30 min – 2 h post-LPS; IFN response peaks ~4–12 h

## Key variants

- Other PAMPs that engage related TLRs: P3C (TLR2/TLR1), CpG (TLR9), polyI:C (TLR3)
- Cytokine mimics: TNF-α (TNFR1), IL-1β (IL-1R) — converge on NF-κB downstream of distinct receptors

## Known limitations

- LPS purity matters: contaminants can engage TLR2.
- Doses above ~1 μg/mL can drive cytotoxicity / pyroptosis.
- LPS-induced "endotoxin tolerance" is a confounder in chronic-stimulation experiments.

## Open problems

- Hypoxic modulation of LPS responses is exactly what this paper addresses.
- Trained-immunity epigenetic memory after LPS challenge (β-glucan parallels).

## Relevance to active research

[[papers/nf-kb-tet2-promote-macrophage-reprogramming]] uses LPS at 48 h to activate normoxic and hypoxic MACs, demonstrating that NF-κB activation by LPS in hypoxia drives focal C2 demethylation. The "swap" experiment shows the activation step (not differentiation) is the critical hypoxic window for the proinflammatory boost.
