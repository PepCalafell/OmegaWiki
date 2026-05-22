---
title: "TF community analysis reveals state-specific pathway rewiring: TGFβ/adhesion in TRM vs proteasome/apoptosis in TEXterm"
slug: tf-community-rewiring-trm-vs-texterm
status: supported
confidence: 0.8
tags: [tf-community, network-rewiring, trm, exhaustion, mechanistic]
domain: immunology
source_papers:
  - atlas-guided-discovery-transcription-factors-cell
evidence:
  - source: atlas-guided-discovery-transcription-factors-cell
    type: supports
    strength: strong
    detail: "Fig. 2d–h: Leiden community detection on TF–TF association networks; TRM community-3 → TGFβ response and cell adhesion; TEXterm community-3 → intrinsic apoptosis; TRM-c1 → RNA metabolism vs TEXterm-c1 → catabolism, proteolysis, autophagy."
conditions: "TF–TF association built from regulatee adjacency matrix per state."
date_proposed: 2026-05-22
date_updated: 2026-05-22
---

## Statement

Leiden community detection over Taiji TF–TF association networks shows that the **same TFs** form distinct partnerships in TRM vs TEXterm cells, with TRM communities enriched for TGFβ response, cell adhesion, and RNA metabolism, while TEXterm communities are enriched for protein catabolism, ubiquitin-proteasome, autophagy, and intrinsic apoptosis.
