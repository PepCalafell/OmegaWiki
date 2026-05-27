---
title: "Organ-wide MERFISH+scRNA-seq+Visium integrated atlas of normal adult human skin"
aliases:
  - organ-wide human skin atlas
  - human skin spatial atlas
  - 15-site MERFISH skin resource
tags:
  - skin
  - atlas
  - MERFISH
  - spatial-transcriptomics
  - Visium
  - scRNA-seq
  - resource
maturity: emerging
key_papers:
  - single-cell-spatial-transcriptomic-analysis-human
first_introduced: "Restrepo et al. Nature Genetics 2026"
date_updated: 2026-05-27
related_concepts:
  - "[[concepts/skin-multicellular-spatial-neighborhoods]]"
  - "[[concepts/perivascular-immune-stromal-niche-skin-salt]]"
---

## Definition

An integrated tri-modality resource of normal human skin covering: (i) MERFISH on 114 samples / 22 donors / 15 anatomic sites yielding ~1.2 million cells, (ii) an integrated scRNA-seq reference of ~286k cells from 14 published studies (93 samples, 85 donors) used to derive a 45-cell-type label set, and (iii) Visium spatial transcriptomics on 143k spots from 81 samples / 63 donors spanning normal + five skin diseases.

## Intuition

A reference atlas plays the role of a coordinate system: any future skin spatial / single-cell study can map its cells onto the 45-cell-type labels and ten-neighborhood scheme to compare across sites, ages and diseases without reinventing annotation.

## Variants

- MERFISH (Vizgen MERSCOPE) panel-based, 500-gene catalog.
- Integrated scRNA-seq is whole-transcriptome but lacks spatial coordinates.

## Comparison

- Largest human skin single-cell spatial dataset to date; complements lymph-node, gut and lung organ-wide atlases.

## When to use

As the default skin reference for label transfer (Azimuth-style), neighborhood mapping, and for benchmarking new spatial methods on a non-tumour tissue.

## Known limitations

- Limited demographic representativeness (22 MERFISH donors).
- Healthy-only MERFISH cohort; disease data come from integrated Visium of public datasets.

## Open problems

- Inclusion of paediatric / pigmented / non-Western skin cohorts.
- Linking gene-level transcriptomic data with proteomic / epigenomic atlas layers.

## Key papers

- [[papers/single-cell-spatial-transcriptomic-analysis-human]]

## My understanding

This is the new default reference resource for skin spatial omics — comparable in role to the Tabula Sapiens for whole-body scRNA-seq but skin-focused and explicitly spatial.
