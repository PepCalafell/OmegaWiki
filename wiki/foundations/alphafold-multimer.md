---
title: "AlphaFold-Multimer"
slug: alphafold-multimer
domain: methods
status: mainstream
aliases:
  - AlphaFold-Multimer
  - AlphaFold Multimer
first_introduced: ""
date_updated: 2026-05-28
source_url: ""
---

## Definition

AlphaFold-Multimer is a deep-learning method that predicts the three-dimensional
structure of protein complexes, extending the AlphaFold monomer model to multi-chain
assemblies and enabling in silico modelling of protein–protein interfaces.

## Intuition

Given the sequences of two (or more) interacting proteins, it predicts how they fold
together and which residues form the binding interface, with per-residue and
inter-chain confidence estimates (e.g. PAE).

## Formal notation

Interface contacts can be thresholded by predicted aligned error (PAE); shared-contact
overlap is quantified by a Jaccard index (JI) to classify interfaces as same
(JI ≥ 0.6), overlapping (0.1 < JI < 0.6) or distinct (JI ≤ 0.1).

## Key variants

AlphaFold2/3 monomer prediction; FoldSeek for structural similarity search over
predicted structures.

## Known limitations

Often misses interactions mediated by short linear motifs (SLiMs) in disordered
regions; confident multimer predictions obtained for only a fraction of pairs
(~10% in the commensal effector–host setting).

## Relevance to active research

Used to model effector–host interfaces and infer shared vs distinct binding modes,
complementing orthogonal SLiM-domain inference (mimicINT) and experimental holdup assays.
