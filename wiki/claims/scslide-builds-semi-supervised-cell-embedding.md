---
title: "scSLIDE builds a semi-supervised cell embedding by WNN-combining unsupervised and PLS embeddings"
slug: scslide-builds-semi-supervised-cell-embedding
status: supported
confidence: 0.9
tags: [scSLIDE, WNN, PLS, embedding, semi-supervised]
domain: single-cell genomics
source_papers:
  - reconstructing-developmental-disease-progression-sample-level
evidence:
  - source: reconstructing-developmental-disease-progression-sample-level
    type: supports
    strength: strong
    detail: "Method: a type-focused unsupervised embedding and a PLS-based state-focused embedding are combined with weighted nearest neighbor (WNN) into a single semi-supervised space that retains cell-type resolution while prioritizing phenotype-linked variation."
conditions: "Requires sample-level metadata (e.g. disease status) for the PLS component."
date_proposed: 2026-06-03
date_updated: 2026-06-03
---

## Statement

scSLIDE's cell-level embedding is semi-supervised: it merges an unsupervised "type" embedding with a supervised PLS "state" embedding via the weighted-nearest-neighbor (WNN) framework, retaining high-resolution cell-type structure while emphasizing phenotype-associated signal.

## Evidence summary

Described in [[reconstructing-developmental-disease-progression-sample-level]]. The authors draw an analogy to RNA/protein multimodal integration: supervised and unsupervised views are complementary modalities unified by WNN.

## Conditions and scope

The PLS view needs informative phenotype labels; when temporal phenotype is strong (zebrafish) supervision is unnecessary.

## Counter-evidence

For zebrafish embryogenesis an unsupervised variant recovered nearly the same trajectory, showing supervision is not always required.

## Linked ideas

Uses [[wnn-weighted-nearest-neighbor-integration]] and [[partial-least-squares-pls]].

## Open questions

Could supervised deep-learning embeddings replace PLS for richer phenotype integration at scale?
