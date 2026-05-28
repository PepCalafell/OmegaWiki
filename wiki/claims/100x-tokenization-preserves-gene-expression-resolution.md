---
title: "100x tokenization preserves gene-expression resolution of 0.01 within a vocabulary of 1024"
slug: 100x-tokenization-preserves-gene-expression-resolution
status: supported
confidence: 0.85
tags: [AlphaCell, tokenization, preprocessing, gene-dosage, methods]
domain: methods / single-cell
source_papers:
  - towards-building-world-model-simulate-perturbation
evidence:
  - source: towards-building-world-model-simulate-perturbation
    type: supports
    strength: strong
    detail: "Quote (p.21): 'Raw UMI counts were first depth-normalized to counts per 10,000 (CP10k) and log(1+x) transformed ... we multiplied the normalized values by 100 and discretized them into integers ... this scaling yields a natural token distribution bounded within a vocabulary size of 1,024. This 100x tokenization strategy preserves expression variations at a resolution of 0.01.'"
conditions: "log(1+CP10k) values x100 then integer-discretized; theoretical max log(1+1e4) ~ 9.21."
date_proposed: 2026-05-28
date_updated: 2026-05-28
---

## Statement

AlphaCell discretizes log(1+CP10k) expression by multiplying by 100 and rounding to integers, giving a vocabulary of 1,024 tokens at a fine resolution of 0.01 — designed to capture subtle gene-dosage shifts in low-abundance transcription factors lost by coarser normalization.

## Evidence summary

Reported in Methods of [[papers/towards-building-world-model-simulate-perturbation]]. Feeds the encoder described in [[claims/alphacell-encoder-mamba-transformer-hybrid-compressing]].

## Conditions and scope

UMI-based assays; vocabulary bound derived from max log(1+1e4) ≈ 9.21.

## Counter-evidence

None; descriptive preprocessing claim.

## Linked ideas

## Open questions

- Does finer (e.g., 1000x) tokenization help or overfit noise?
