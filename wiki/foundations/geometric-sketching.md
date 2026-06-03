---
title: "Geometric Sketching"
slug: geometric-sketching
domain: single-cell genomics
status: mainstream
aliases:
  - geometric sketch
  - geosketch
first_introduced: "2019"
date_updated: 2026-06-03
source_url: ""
---

## Definition

Geometric sketching is a subsampling method that selects a small, representative subset ("sketch") of cells from a large single-cell dataset by covering the geometry of the expression manifold evenly, rather than sampling in proportion to cell-type abundance.

## Intuition

Uniform random sampling over-represents abundant cell types and can miss rare ones. Geometric sketching instead tiles the data space so that both common and rare states are captured, preserving the structure of the manifold with far fewer cells.

## Formal notation

The data space is partitioned into roughly equal-volume regions and one (or few) cells are drawn per occupied region, yielding a sketch whose density is approximately uniform over the manifold's support.

## Key variants

- Plate/grid-based covering vs nearest-neighbor-graph covering.

## Known limitations

- Sketch quality depends on the embedding used to define geometry.
- Even coverage can under-weight biologically important but geometrically small regions if region size is misset.

## Open problems

- Optimal region granularity as a function of dataset size and heterogeneity.

## Relevance to active research

scSLIDE uses geometric sketching to select ~5,000 "landmark cells" that span abundant and rare cellular states, ensuring sample-density estimation is anchored on a representative set of reference points.
