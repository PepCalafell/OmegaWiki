---
title: "PROGENy (pathway responsive genes for activity inference)"
slug: progeny-pathway-activity-inference
domain: methods
status: mainstream
aliases:
  - PROGENy
first_introduced: "Schubert et al., Nature Communications 2018"
date_updated: 2026-05-28
source_url: "https://doi.org/10.1038/s41467-017-02391-6"
---

## Definition

PROGENy infers the activity of signaling pathways from gene expression by scoring a curated set of pathway-responsive genes (downstream transcriptional footprints) rather than pathway-member genes themselves. It returns per-cell or per-group scores for pathways such as TGFβ, Hypoxia, JAK-STAT, NFκB, TNFα, MAPK, PI3K, p53, and others.

## Intuition

The transcriptional footprint of a pathway (genes whose expression changes when the pathway is active) is a more robust readout of pathway activity than expression of the pathway's own genes, which are often post-translationally regulated.

## Formal notation

Linear model: pathway activity = weighted sum of responsive-gene expression, with weights learned from a large perturbation compendium.

## Key variants

decoupleR implementation; species-specific weight matrices (human/mouse).

## Known limitations

Limited to the ~14 pathways with curated footprints; scores are relative, not absolute; footprints derived largely from cell-line perturbations may not transfer to all primary cell contexts.

## Open problems

Expanding the pathway catalog; context-specific footprints for tissue-resident cells.

## Relevance to active research

Used to show JAK-STAT and hypoxic signaling elevated in F6 inflammatory myofibroblasts, and TGFβ enriched in F7/F8 myofibroblasts of human skin.
