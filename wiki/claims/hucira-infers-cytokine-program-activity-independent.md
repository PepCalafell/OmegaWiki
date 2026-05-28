---
title: "huCIRA infers cytokine and program activity from independent transcriptomic datasets"
slug: hucira-infers-cytokine-program-activity-independent
status: supported
confidence: 0.85
tags: [huCIRA,enrichment,gseapy,cytokine-inference,CIP]
domain: immunology
source_papers:
  - single-cell-cytokine-dictionary-human-peripheral
evidence:
  - source: single-cell-cytokine-dictionary-human-peripheral
    type: supports
    strength: strong
    detail: "Quote (p.23): 'we developed huCIRA (short for human Cytokine Immune Response Analysis), an open-source, easy-to-use Python tool that interfaces gseapy and supports the use of these gene sets in enrichment analyses and differential cell-cell communication inference'."
conditions: "In vitro human PBMC (12 healthy donors), 24 h cytokine stimulation, Parse Biosciences split-pool scRNA-seq."
date_proposed: 2026-05-28
date_updated: 2026-05-28
---

## Statement

huCIRA is an open-source Python tool (interfacing gseapy) that scores cytokine and CIP activity, and differential cell-cell communication, in any user-supplied human transcriptomic dataset by enrichment against the Human Cytokine Dictionary gene sets.

## Evidence summary

Reported in [[papers/single-cell-cytokine-dictionary-human-peripheral]] (Oesinghaus, Seelig, Theis et al., bioRxiv 2025). Type: methodological.

## Conditions and scope

In vitro human PBMC (12 healthy donors), 24 h cytokine stimulation, Parse Biosciences split-pool scRNA-seq.

## Counter-evidence

None within the paper's scope.

## Linked ideas

## Open questions
