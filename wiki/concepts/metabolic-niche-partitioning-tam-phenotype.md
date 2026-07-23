---
title: "Metabolic-niche partitioning of TAM phenotypes"
aliases:
  - "metabolic niche partitioning of TAMs"
  - "niche-specific metabolic determination of TAM phenotype"
tags:
  - TAM
  - tumor-hypoxia
  - spatial-metabolomics
  - fatty-acid-oxidation
  - glycolysis
  - tumor-microenvironment
maturity: emerging
key_papers:
  - functional-genetic-screens-reveal-key-pathways
first_introduced: "2025"
date_updated: 2026-07-23
related_concepts:
  - angiogenic-mhc-ii-tam-mutual-exclusivity
  - lgp-factor-tam-polarization-axis
  - anatomical-niche-predicts-macrophage-function
  - tam-recruitment-hypoxic-niche-chemokines
---

## Definition

The mutually exclusive TAM phenotypes are spatially organised by local metabolism: angiogenic TAMs occupy hypoxic, glycolytic, lactic-acid/PGE2-rich niches, whereas MHC-II+ TAMs occupy normoxic niches marked by active fatty-acid oxidation (FAO). Spatial exclusivity of the two niches mirrors the cellular mutual exclusivity.

## Intuition

Where a macrophage sits determines what it becomes. The tumor's metabolic geography — hypoxia and lactate/prostaglandin in one region, oxygen and fatty-acid fuel in another — supplies exactly the LGP-factor combinations that push local macrophages toward angiogenic or MHC-II fates.

## Formal notation

Operationalised by pimonidazole-positivity of angiogenic (not MHC-II) TAMs, spatial cross-correlation between metabolite abundance and TAM signatures, and cluster co-occurrence scores showing MHC-II-high niches segregate from glycolysis-high niches.

## Variants

- Direct hypoxia evidence: pimonidazole labels only CX3CR1−MHC-II− angiogenic TAMs across 4T1/LLC/MC38.
- Human evidence: paired spatial transcriptomics + AFADESI-MSI metabolomics in NSCLC; FAO intermediates ↔ MHC-II niches, lactate/prostaglandins ↔ angiogenic niches.

## Comparison

Extends [[anatomical-niche-predicts-macrophage-function]] and [[tam-recruitment-hypoxic-niche-chemokines]] by supplying the *metabolite-level* cause (via the [[lgp-factor-tam-polarization-axis]]) rather than only the anatomical correlation.

## When to use

Use when interpreting spatial data where TAM phenotype tracks tissue architecture, or when arguing that normalising tumor metabolism (reducing hypoxia/lactate) would shift TAM composition.

## Known limitations

- GM-CSF could not be detected by current spatial platforms, so its niche localisation is inferred, not measured.
- Spatial metabolomics resolution (~100 µm) is coarser than single cells.

## Open problems

- Higher-resolution (MERFISH-scale) validation of the niche boundaries.
- Whether relieving hypoxia in vivo re-partitions TAM phenotypes as the model predicts.

## Key papers

- [[functional-genetic-screens-reveal-key-pathways]] — provides the pimonidazole, immunofluorescence, and paired spatial multiomics evidence for metabolic-niche partitioning.

## My understanding

This concept is the spatial closure of the LGP model: it shows the factors that drive polarization in vitro are physically enriched exactly where the corresponding TAM phenotype is found in vivo.
