---
title: "Direct glioma–microglia co-culture under controlled hypoxia"
aliases: []
tags: [co-culture, model-system, hypoxia, microglia, glioma, BV2, GL261, tumor-microenvironment]
maturity: emerging
key_papers:
  - hypoxic-stress-dysregulates-functions-glioma-associated
first_introduced: "2025"
date_updated: 2026-06-04
related_concepts: [hypoxia-chromatin-remodeling-myeloid-identity-gene, tam-recruitment-hypoxic-niche-chemokines, macrophage-ontogeny-resident-vs-monocyte-derived]
---

## Definition

An in vitro model in which microglia (BV2) or primary BMDM are directly co-cultured with GFP-labeled glioma cells (GL261) and exposed to defined oxygen tensions (e.g. <0.1% O₂ hypoxia vs 21% normoxia), then separated by FACS for genome-wide profiling. Glyoxal fixation immediately post-hypoxia prevents reoxygenation artifacts during sorting. The design isolates and crosses two variables — tumor contact and oxygen level — enabling attribution of transcriptomic/epigenomic changes to hypoxia, glioma contact, or their interaction.

## Intuition

To ask "what does hypoxia do to a microglion that is touching a glioma cell?", you need both partners, controlled oxygen, and clean cell separation. This model provides a 2×2 (±glioma, ±hypoxia) framework with pure sorted populations for RNA-seq/ATAC-seq/CUT&RUN.

## Formal notation

- Conditions: Ctrl_N, Ctrl_H, CC_N, CC_H (control/co-culture × normoxia/hypoxia).
- Key technical features: glyoxal fixation pre-sorting; fixed-cell ATAC-seq; CD45-based FACS isolation of myeloid cells; EGFP-mapping to exclude glioma RNA contamination.

## Variants

- BV2 microglia and primary BMDM as the myeloid partner.
- Extendable to other glioma lines / primary cells.

## Comparison

A reductionist alternative to in vivo GBM models and conditioned-media approaches; trades physiological completeness for controllability and clean attribution of effects.

## When to use

Invoke when designing mechanistic studies of tumor–myeloid crosstalk under hypoxia, or when interpreting findings that require disentangling oxygen from tumor-contact effects.

## Known limitations

- Simplified TME: excludes astrocytes, endothelial cells, T cells, vasculature, and 3D architecture.
- Cell lines (BV2/GL261) may not capture primary/in vivo behavior.

## Open problems

- Adding additional TME cell types while retaining controllability.
- Mapping the relative contributions of direct contact vs secreted factors.

## Key papers

- [[papers/hypoxic-stress-dysregulates-functions-glioma-associated]]

## My understanding

A clean experimental scaffold (the authors call it a robust model system) for hypoxia × tumor-contact dissection — useful as a methodological reference for experiment design in the thesis.
