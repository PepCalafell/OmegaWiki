---
title: "mimicINT (SLiM–domain interaction inference)"
slug: mimicint-slim-domain-inference
domain: methods
status: mainstream
aliases:
  - mimicINT
  - mimicint
first_introduced: ""
date_updated: 2026-05-28
source_url: ""
---

## Definition

mimicINT is a computational workflow that infers protein–protein interactions
mediated by short linear motifs (SLiMs) by matching candidate interaction pairs to
known SLiM–domain interaction templates (e.g. from the ELM resource).

## Intuition

Many interactions are mediated by a short motif in a disordered region binding a
globular domain pocket. mimicINT scans one partner for SLiMs and the other for the
cognate domain, proposing motif–domain interfaces that structure predictors often miss.

## Formal notation

Candidate interfaces are filtered by stringency criteria and tested for enrichment
against randomized networks (e.g. permutation P values).

## Key variants

ELM-template-based SLiM detection; complementary to AlphaFold-Multimer for globular
interfaces.

## Known limitations

Motif matches are predictions requiring experimental validation; template coverage
limits novel-motif discovery.

## Relevance to active research

Used to identify SLiM–domain interfaces (notably PDZ–PBM) among commensal effector–host
interactions that AlphaFold-Multimer could not capture.
