---
title: "MAGeCK — Model-based Analysis of Genome-wide CRISPR-Cas9 Knockout"
slug: "mageck-crispr-screen-analysis"
domain: "genomics / functional genetics"
status: mainstream
aliases:
  - "MAGeCK"
  - "Model-based Analysis of Genome-wide CRISPR-Cas9 Knockout"
  - "MAGeCK count"
  - "MAGeCK test"
first_introduced: "2014"
date_updated: 2026-07-23
source_url: "https://doi.org/10.1186/s13059-014-0554-4"
---

## Definition

MAGeCK is a computational pipeline for identifying positively and negatively selected genes from pooled CRISPR-Cas9 knockout screens. It maps sequencing reads to an sgRNA library (`count`), then ranks genes by the enrichment or depletion of their sgRNAs between conditions (`test`), producing per-sgRNA and per-gene FDR and log2 fold-change statistics.

## Intuition

In a pooled screen, each cell carries one sgRNA; a phenotype-based sort (e.g. sorting ARG1-negative macrophages) enriches or depletes the guides targeting genes required for that phenotype. MAGeCK aggregates the several guides per gene using a modified robust rank aggregation, so a gene called a hit must have consistent signal across multiple independent guides, controlling false positives from single off-target guides.

## Formal notation

Per-gene significance is computed by negative-binomial modelling of sgRNA read counts, followed by rank-based aggregation (RRA) of sgRNA-level p-values into a gene-level score. Normalisation can use total counts, median, or (as in TAM screens) a designated set of control/non-targeting sgRNAs via `--norm-method control` and `--control-sgrna`.

## Key variants

- MAGeCK-RRA (robust rank aggregation) — the classic enrichment test.
- MAGeCK-MLE (maximum-likelihood) — models multiple conditions jointly with a design matrix.
- MAGeCK-VISPR / MAGeCKFlute — downstream visualisation and QC.

## Known limitations

- Low guide coverage or shallow sequencing inflates noise, especially for depletion (dropout) hits.
- Assumes guides for a gene behave concordantly; variable guide efficiency weakens weak hits.
- Phenotype-sort screens inherit the noise of the FACS gate used to define the selected population.

## Open problems

- Calibrating FDR under strong selection bottlenecks (e.g. primary macrophage screens with limited cell numbers).
- Integrating single-cell readouts (CROP-seq) with bulk count-based statistics.

## Relevance to active research

MAGeCK is the standard analysis layer for CRISPR-screen–based discovery of macrophage-polarisation regulators; the TAM-polarization screen used it (`v0.5.9.2`) to call `Hif1a`, `Ptger4`, `Csf2ra`, `Adar`, `Spi1`, and SWI/SNF components as regulators of the angiogenic phenotype.
