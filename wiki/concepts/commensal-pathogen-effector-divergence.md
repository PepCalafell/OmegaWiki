---
title: "Commensal–pathogen effector repertoire divergence"
aliases:
  - commensal effector divergence
tags:
  - microbiome
  - host-pathogen
  - t3ss
  - effector-evolution
maturity: emerging
key_papers:
  - effector-host-interactome-map-links-type
first_introduced: "2026"
date_updated: 2026-05-28
related_concepts:
  - commensal-t3ss-host-directed-secretion
---

## Definition

The finding that commensal-gut T3SS effector repertoires are largely distinct from
pathogen effectors in both sequence and structure, with commensal-specific domain
content, supporting a model in which commensal T3SS are adapted for cooperative rather
than pathogenic interactions.

## Intuition

If commensal and pathogen effectors had a shared toolkit, they would cluster together;
instead they segregate — commensals follow separate selective trajectories and carry
domains (e.g. c-di-GMP enzymes, PAS sensors) tied to a non-pathogenic lifestyle.

## Formal notation

Only ~0.5% of strain effectors and ~3% of meta-effectors share high sequence similarity
(≥90%/≥90% length) with pathogen effectors; FoldSeek structure clusters are mostly
homogeneous, mixed clusters depleted (empirical P < 0.0001).

## Variants

Sequence-level (jackhmmer/UniRef90) vs structure-level (AlphaFold + FoldSeek)
divergence; domain-content divergence (GGDEF/EAL/PAS enriched in commensals).

## Comparison

Distinct from convergence on shared host targets — divergence is in the effector
proteins themselves, not their host interaction outcomes.

## When to use

When arguing that "commensal" and "pathogen" are not interchangeable effector
categories, or when interpreting effector novelty.

## Known limitations

Pathogen effector reference set is finite; some commensal–pathogen overlap exists at the
host-target level.

## Relevance / Open problems

What functions do commensal-specific domains (c-di-GMP, PAS) serve in interkingdom
signalling?

## Key papers

- [[effector-host-interactome-map-links-type]]

## My understanding

Effector divergence is the structural counterpart to the reframing of T3SS as a
commensal feature.
