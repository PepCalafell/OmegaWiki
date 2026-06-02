---
title: "MaxQuant — MS-based proteomics quantification software"
slug: maxquant-proteomics
domain: methods
status: mainstream
aliases:
  - MaxQuant
  - Andromeda search engine
first_introduced: "Cox & Mann 2008 Nature Biotechnology"
date_updated: 2026-06-02
source_url: "https://www.maxquant.org/"
---

## Definition

MaxQuant is a widely used software suite for the analysis of high-resolution mass-spectrometry proteomics data. It performs peptide and protein identification (via the integrated Andromeda search engine), label-free quantification (LFQ), match-between-runs, and localization scoring of post-translational modifications such as phosphorylation.

## Intuition

MaxQuant turns raw MS spectra into quantitative protein and phosphosite tables: it matches fragment spectra to a proteome database, infers proteins, and estimates abundances across samples, providing the protein/phosphopeptide matrices that downstream statistics consume.

## Formal notation

- Inputs: raw LC-MS/MS files + proteome FASTA (e.g. UniProt)
- Outputs: proteinGroups.txt, Phospho(STY)Sites.txt, with LFQ intensities
- Phospho-site localization probability (class I sites > 0.75) gauges residue assignment confidence
- FDR thresholds typically 0.01 (peptide) / 0.05 (protein)

## Key variants

- Label-free quantification (LFQ) vs isobaric (TMT) vs SILAC workflows
- DDA-oriented; DIA handled by other tools (e.g. DIA-NN, Spectronaut)

## Known limitations

- Missing values common in label-free phosphoproteomics, requiring imputation
- Protein inference ambiguity for shared peptides; modification-site localization uncertainty

## Open problems

- Robust handling of missingness in phosphoproteomic differential analysis
- Cross-platform reproducibility of label-free quantification

## Relevance to active research

Used (version 2.0.1.0 with Andromeda) to identify and quantify the proteome (5342 proteins) and phosphoproteome (5905 phosphopeptides mapping to 2313 phosphoproteins) of primary human M1/M2a/M2c macrophages, with localization probability >0.75 required for kinase-related analyses.
