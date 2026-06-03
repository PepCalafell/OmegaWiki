---
title: "stLearn SCTP — spatially-constrained ligand-receptor inference"
slug: stlearn-sctp-spatial-lr
domain: spatial omics methods
status: mainstream
aliases: ["stLearn", "SCTP", "spatially-constrained two-level permutation", "stLearn cell-cell interaction"]
first_introduced: "2023"
date_updated: 2026-06-03
source_url: "https://github.com/BiomedicalMachineLearning/stLearn"
---

## Definition

stLearn is a spatial transcriptomics analysis toolkit; its SCTP (Spatially-Constrained Two-level Permutation) test predicts ligand-receptor (L-R) cell-cell interactions while requiring that the interacting cells/spots are spatial neighbours (Pham et al., 2023). It scores L-R co-expression between neighbouring spots/cells and assesses significance via a two-level permutation that controls for both expression level and spatial arrangement.

## Intuition

scRNA-seq dissociates tissue and loses spatial context, so it can predict interactions between cell types that never physically touch (false positives). By constraining inference to spatial neighbours, SCTP removes such artefacts (e.g. XCL1-XCR1 predicted by scRNA-seq but not co-localised) and recovers genuine interactions that single-cell analysis missed (e.g. WNT5A-ROR1).

## Formal notation

For an L-R pair (l,r) and neighbouring spots (i,j): interaction score from co-expression of l in i and r in neighbour j; significance via two-level permutation over expression and spatial labels.

## Key variants

- Spot-level (Visium) vs single-cell (CosMx, Xenium) SCTP
- Integration with downstream MMCCI for multi-sample consistency

## Known limitations

- Neighbourhood definition affects results
- Limited to genes present on the platform panel
- Co-expression proximity is an inference, not direct interaction proof

## Open problems

- Optimal neighbourhood radius across platforms
- Distinguishing autocrine/juxtacrine/paracrine signalling

## Relevance to active research

Provides spatially-informed L-R predictions that, after MMCCI integration, yield high-confidence cancer-type-specific interactomes; the spatial constraint materially improves accuracy/specificity over dissociated scRNA-seq.
