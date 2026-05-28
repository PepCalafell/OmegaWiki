---
title: "Sequence-independence of effector–host interaction profiles"
aliases:
  - sequence-independent interaction profiles
tags:
  - microbiome
  - host-pathogen
  - effector
  - protein-interaction
maturity: emerging
key_papers:
  - effector-host-interactome-map-links-type
first_introduced: "2026"
date_updated: 2026-05-28
related_concepts:
  - microbiome-host-meta-interactome-hummi
---

## Definition

The finding that an effector's host interaction profile is largely independent of its
overall sequence similarity to other effectors: sequence similarity sets only an upper
bound on interaction similarity, while structurally/sequence-dissimilar effectors can
share host targets.

## Intuition

Even effectors >90% identical can have interaction profiles ranging from identical to
complementary; conversely, unrelated effectors can hit the same host proteins. So you
cannot reliably transfer interaction annotations by sequence homology.

## Formal notation

Within homology clusters (≥90% identity), Jaccard interaction-profile similarity spans
the full range; clustering by interaction profile recovers overlap outside sequence
homology clusters.

## Variants

Globular-interface determinants (AlphaFold) vs short-linear-motif determinants
(mimicINT/SLiM); same vs distinct interfaces on shared targets.

## Comparison

Challenges homology-based functional inference common in interactomics.

## When to use

When cautioning against propagating effector function by sequence similarity alone.

## Known limitations

Based on the subset of systematically profiled homolog clusters.

## Open problems

What structural/motif features actually determine interaction profiles?

## Key papers

- [[effector-host-interactome-map-links-type]]

## My understanding

A methodological warning with broad implications for effector annotation pipelines.
