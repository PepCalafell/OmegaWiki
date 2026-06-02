---
title: "FOS / NCOR2 / PPARγ transcriptional hub of immunosuppressive macrophages"
aliases:
  - FOS NCOR2 PPARγ M2a hub
tags:
  - macrophage
  - transcription-factor
  - immunosuppression
  - network
  - TAM
maturity: emerging
key_papers:
  - delineation-signaling-routes-underlie-differences-macrophage
first_introduced: "Totu, Bossart et al. 2025 NAR Molecular Medicine"
date_updated: 2026-06-02
related_concepts:
  - pak2-pkc-alpha-regulators-immunosuppressive-macrophages
  - tumor-associated-macrophage-immunosuppression
  - macrophage-activation-core-regulatory-hubs
---

## Definition

The finding that, when proteomic, phosphoproteomic, and transcriptomic data from human macrophages are integrated into a single interaction network, the transcription regulators FOS, NCOR2, and PPARγ emerge as central nodes (high current-flow betweenness centrality) of the immunosuppressive M2a state — a transcriptional counterpart to the kinase hubs (PAK2, PKCα) of the same state.

## Intuition

Multi-omics network integration asks not just "which molecules change" but "which molecules connect the most other changing molecules." For M2a macrophages the answer at the transcription-factor level is FOS, NCOR2, and PPARγ — TFs with documented anti-inflammatory / protumoral roles — mirroring how STAT1/STAT3/RELA/JUN anchor the M1 network.

## Formal notation

- M2a TF hubs: FOS ([[foundations/fos-transcription-factor]]), NCOR2 ([[foundations/ncor2-nuclear-receptor-corepressor]]), PPARγ ([[foundations/pparg-tf]])
- Additional M2a-associated TFs with upregulated phosphosites: MAFB ([[foundations/mafb-transcription-factor]]), HSF1 ([[foundations/hsf1-heat-shock-factor]])
- Contrast — M1 TF hubs: STAT1, STAT3, RELA, JUN, NFKB2, NCOR1
- Centrality metric: current-flow betweenness in the integrated multi-omics network

## Variants

- TF hub set is state-specific (M1 vs M2a vs M2c)
- Hub identity depends on the interaction-database background and centrality metric used

## Comparison

vs single-omics TF inference (e.g. TRRUST/DoRothEA on transcriptomes alone): network integration adds phospho- and proteomic evidence, so hubs reflect signaling state, not just mRNA. vs the M1 hub set (STAT/RELA/JUN): FOS/NCOR2/PPARγ define the opposing immunosuppressive pole.

## When to use

- Interpreting which transcription programs anchor immunosuppressive macrophage states
- Prioritizing TFs for perturbation in TAM repolarization studies

## Known limitations

- Centrality is sensitive to interaction-database completeness and literature bias
- Hubs are correlative network features, not validated drivers
- Derived from in vitro polarized macrophages

## Open problems

- Causal validation that FOS/NCOR2/PPARγ drive (rather than mark) M2a programs
- How these TF hubs connect to the PAK2/PKCα kinase hubs mechanistically

## Key papers

- [[papers/delineation-signaling-routes-underlie-differences-macrophage]] — identifies FOS, NCOR2, and PPARγ as central transcription regulators of the immunosuppressive M2a macrophage network via multi-omics integration.

## My understanding

The transcription-factor face of the same immunosuppressive-macrophage story whose kinase face is PAK2/PKCα. Useful as a curated short-list of M2a TF hubs to test against the vault's TAM-immunosuppression and macrophage-core-regulatory-hub concepts.
