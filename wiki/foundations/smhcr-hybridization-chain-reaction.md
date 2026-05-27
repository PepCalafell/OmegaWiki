---
title: "smHCR — single-molecule Hybridization Chain Reaction"
slug: smhcr-hybridization-chain-reaction
domain: "spatial-transcriptomics / validation / RNA-FISH"
status: mainstream
aliases:
  - "smHCR"
  - "single-molecule HCR"
  - "HCR RNA-FISH"
  - "HCR v3"
first_introduced: "Dirks & Pierce PNAS 2004; smHCR Choi et al. Development 2018"
date_updated: 2026-05-27
source_url: "https://www.molecularinstruments.com/hcr-rnafish-technology"
---

## Definition

smHCR uses pairs of DNA initiator probes that bind adjacent mRNA targets and trigger a hairpin polymerization cascade, producing a localized fluorescent amplicon at each mRNA molecule. Achieves single-molecule sensitivity for multiplexed RNA detection in fixed tissue.

## Intuition

Higher sensitivity than commercial spatial transcriptomics panels for arbitrarily chosen genes; used to validate transcripts that are missing from a fixed MERSCOPE/MERFISH panel. NiCo uses smHCR to validate the predicted Tgfb1 (Kupffer) — Dcn (stellate) covariation in mouse liver because neither gene was in the original MERSCOPE 347-gene panel.

## Known limitations

- Multiplexing limited to a handful of genes per round.
- Throughput limited compared to high-plex MERFISH / Xenium.

## Relevance to active research

Gold-standard orthogonal validation assay for spatial transcriptomics predictions that rely on inferred genes outside the original panel.
