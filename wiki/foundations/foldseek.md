---
title: "FoldSeek"
slug: foldseek
domain: methods
status: mainstream
aliases:
  - FoldSeek
  - Foldseek
first_introduced: ""
date_updated: 2026-05-28
source_url: ""
---

## Definition

FoldSeek is a fast structural alignment and clustering tool that searches and compares
protein tertiary structures by encoding 3D structure into a structural alphabet (3Di),
enabling structure-based homology detection at sequence-search speeds.

## Intuition

Two proteins can share a fold despite low sequence identity. FoldSeek finds such
structurally similar proteins by reducing each residue's local geometry to a letter,
then running sequence-style alignment over these structural letters.

## Formal notation

Structure clusters can be tested against random expectation via label-permutation
tests (e.g. empirical P values over n=10,000 permutations) to assess whether
homogeneous or mixed clusters are over/under-represented.

## Key variants

Used over AlphaFold-predicted structures; tunable clustering parameters.

## Known limitations

Depends on quality of input predicted structures; cluster composition can be sensitive
to parameter choice (robustness checks recommended).

## Relevance to active research

Used to show that commensal-effector and pathogen-effector structures form mostly
homogeneous clusters, with mixed clusters depleted — evidence that the two effector
repertoires are structurally distinct.
