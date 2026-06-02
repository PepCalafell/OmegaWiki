---
title: "GITIII predicts the central receiver cell's state from neighbouring sender cells via node, distance, and edge embeddings"
slug: gitiii-predicts-central-cell-state-neighbouring
status: supported
confidence: 0.7
tags:
  - cell-cell-interaction
  - spatial-transcriptomics
  - graph-transformer
domain: "spatial transcriptomics / methods"
source_papers:
  - identifying-spatial-single-cell-level-interactions
evidence:
  - source: identifying-spatial-single-cell-level-interactions
    type: supports
    strength: moderate
    detail: "Commentary describes GITIII's embedding module producing a node embedding (with masking of same-type neighbour cell-state to prevent perfect prediction), a distance embedding modelling signalling decay, and an edge embedding capturing neighbouring ligand influence and spatial proximity."
conditions: "Architecture as described in the News & Views; details secondary to primary paper."
date_proposed: 2026-06-02
date_updated: 2026-06-02
---

## Statement

GITIII models CCIs by learning to predict the gene-expression state of a central (receiver) cell from the spatial organization, ligand expression, types, and states of its neighbouring (sender) cells, using three embeddings: a node embedding (masking the cell-state expression of same-type neighbours to prevent perfect prediction), a distance embedding (modelling signalling decay with distance), and an edge embedding (capturing the influence of neighbouring ligands and spatial proximity).

## Evidence summary

Described in [[papers/identifying-spatial-single-cell-level-interactions]] (p.146): "The first module generates three distinct embeddings: a node embedding that integrates cell state and type while masking the cell-state expression of neighbouring sender cells of the same type as the central cell to prevent perfect prediction; a distance embedding encoding spatial dependence to model different signalling decay patterns; and an edge embedding that captures the influence of neighbouring ligands and spatial proximity." See [[foundations/gitiii-graph-transformer-cci-method]].

## Conditions and scope

Describes the model architecture; faithful to the commentary's account of the primary paper.

## Counter-evidence

None recorded.

## Linked ideas

None yet.

## Open questions

- Sensitivity of the distance-embedding decay model to neighbourhood radius and platform.
</content>
