---
title: "KEA3 — Kinase Enrichment Analysis version 3"
slug: kea3-kinase-enrichment-analysis
domain: methods
status: mainstream
aliases:
  - KEA3
  - Kinase Enrichment Analysis 3
first_introduced: "Kuleshov et al. 2021 Nucleic Acids Research"
date_updated: 2026-06-02
source_url: "https://www.maayanlab.cloud/kea3/"
---

## Definition

KEA3 (Kinase Enrichment Analysis 3) is a web tool that infers upstream kinases responsible for an input set of differentially phosphorylated or differentially expressed proteins by enrichment against assembled libraries of kinase–substrate interactions, kinase–protein interactions, and kinase co-expression/co-regulation.

## Intuition

KEA3 leverages multiple evidence types — not just curated kinase–substrate edges but also interaction and co-expression trends — so that even kinases with few annotated substrates can be ranked as likely regulators of an observed phosphoprotein set.

## Formal notation

- Input: gene/protein list (e.g. upregulated phosphoproteins per phenotype)
- Background libraries: kinase–substrate, kinase–PPI, co-expression
- Output: ranked upstream kinases by enrichment across libraries

## Key variants

- KEA / KEA2 predecessors; integrated within the Enrichr/MaayanLab toolset
- Complementary to motif-based prediction (Kinase Library) and NetPhorest

## Known limitations

- Enrichment depends on library completeness and is biased toward well-studied kinases
- Set-based input loses quantitative phosphosite-level information

## Open problems

- Reconciling enrichment-based and motif-based kinase predictions
- Reducing literature bias toward heavily annotated kinases

## Relevance to active research

Applied to upregulated phosphoproteins per macrophage phenotype to predict upstream kinases; its predictions included JAK and MAPK kinases for M1 and PKACα/PAK2 for the M2 states, corroborating the motif-based footprinting.
