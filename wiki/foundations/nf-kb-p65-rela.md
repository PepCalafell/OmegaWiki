---
title: "NF-κB / p65 (RELA)"
slug: nf-kb-p65-rela
domain: "molecular-biology / inflammation"
status: mainstream
aliases:
  - "NF-kB"
  - "NF-κB"
  - "p65"
  - "RELA"
  - "v-rel avian reticuloendotheliosis viral oncogene homolog A"
  - "transcription factor p65"
  - "canonical NF-κB"
  - "RelA / p65 subunit"
first_introduced: "Sen & Baltimore 1986"
date_updated: 2026-05-08
source_url: "https://www.uniprot.org/uniprot/Q04206"
---

## Definition

NF-κB is a family of dimeric transcription factors central to inflammation, immunity, cell proliferation, and apoptosis. The canonical pathway is mediated by p65 (RELA)/p50 (NFKB1) heterodimers. Stimulation by TLR ligands (LPS), TNF-α, IL-1β, or other inflammatory cues triggers IKK-mediated phosphorylation and degradation of IκBα, releasing the p65/p50 dimer to translocate to the nucleus and activate genes containing κB binding motifs (5′-GGGRNYYYCC-3′).

## Intuition

NF-κB is the master inflammatory transcription factor — almost any pathogen-associated or damage-associated stimulus eventually feeds into NF-κB activation. p65 is the canonical transactivator subunit; nuclear p65 is a near-universal marker of inflammatory activation.

## Formal notation

- Subunits: RELA (p65), RELB, REL (c-Rel), NFKB1 (p50/p105), NFKB2 (p52/p100)
- Canonical dimer: p65/p50
- Activation: IKKβ → P-IκBα → IκBα ubiquitination + degradation → p65/p50 nuclear import
- DNA binding motif: 5′-GGGRNYYYCC-3′ (κB site)

## Key variants

- Canonical pathway: p65/p50, fast TLR/TNF-α/IL-1β response
- Non-canonical pathway: RelB/p52, slower, lymphotoxin-β / CD40 / BAFF response

## Known limitations

- Canonical motif is degenerate; many predicted κB sites are not functional.
- Crosstalk with HIF1α, AP-1, IRF, STAT pathways complicates target attribution.

## Open problems

- Target-gene specificity across cell types and stimulus combinations.
- Mechanism by which NF-κB engages epigenetic remodeling machinery (CBP/p300, SWI/SNF, TET).

## Relevance to active research

In [[papers/nf-kb-tet2-promote-macrophage-reprogramming]], p65 is the primary driver of hypoxia-specific cluster-C2 DNA demethylation: BAY11-7082 inhibition restores normoxic methylation levels at C2 CpGs, while HIF1α inhibition does not. p65 binding peaks (P1 ChIP-seq cluster) maximize in mMAC1 and overlap ~15% with HIF1α H2-cluster peaks. The paper proposes a non-physical cooperative mechanism between p65 and HIF1α. In [[papers/hypoxia-driven-crosstalk-between-tumor-tumor]] (Bai 2022 review), the *dimer composition* of NF-κB (p65-p50 heterodimer vs p50-p50 homodimer) is argued to determine TAM polarization direction: LPS-driven p50-p50 homodimers favor M2 reprogramming, Bufalin-driven p65-p50 heterodimers favor M1 transition. NF-κB is also central to multiple hypoxic TAM mechanisms reviewed in Bai 2022: TLR4/TRIF/NF-κB-driven IL-1β/M2 from necrotic debris; CCL8 → CCR2-NF-κB TAM infiltration; tumor IL-10/NF-κB → M2; CCL15-CCR1-NF-κB gefitinib resistance; ROS-NF-κB-driven Galectin-3 expression in hypoxic TAMs.
