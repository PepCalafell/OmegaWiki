---
title: "Cross-platform spatial meta-community"
aliases: ["spatial meta-community", "consensus spatial community across platforms"]
tags: [spatial-omics, niche, community-analysis, methods]
maturity: emerging
key_papers:
  - integrating-12-spatial-single-cell-technologies
first_introduced: "2025"
date_updated: 2026-06-03
related_concepts: [spatial-multiomics-orthogonal-validation, differential-stromal-interactions-skin-cancer]
---

## Definition

A spatial tissue community (recurrent neighbourhood of co-located cell types) defined by consolidating per-platform community calls into a shared neighbourhood matrix, then grouping communities with similar cell-type composition across platforms into a single "meta-community." This yields communities that consistently appear across Visium, CosMx, and Xenium rather than artefacts of one platform.

## Intuition

Each spatial platform clusters neighbourhoods on its own, producing platform-specific communities that are hard to compare. By matching communities with similar composition across platforms (e.g. Visium_2 ≈ Xenium_2 ≈ Xenium_7 ≈ CosMx_6), one obtains robust, biologically meaningful communities and can compare their abundance across conditions.

## Formal notation

Cells/spots → neighbourhood composition vectors → per-platform communities → cross-platform matching by composition similarity → meta-community membership.

## Variants

- Transcriptomics-only meta-communities (Visium/CosMx/Xenium)
- Cross-modality community matching (Xenium/CODEX/glycomics)

## Comparison

Generalises single-sample neighbourhood/niche analysis (e.g. cluster neighbourhood enrichment) to a cross-platform consensus; related to but distinct from batch-effect-correction approaches, since it matches composition rather than embedding spots into one latent space.

## When to use

When community/niche findings must be reproducible across platforms and compared between conditions (e.g. melanoma vs cSCC/BCC abundance of a melanocyte-enriched community).

## Known limitations

- Requires comparable cell-type annotations across platforms
- Matching threshold choice affects meta-community boundaries
- Panel differences limit composition comparability

## Open problems

- Statistical calibration of cross-platform community matching
- Extending to >3 platforms and modalities jointly

## Key papers

- [[integrating-12-spatial-single-cell-technologies]] — identifies a melanocyte-enriched meta-community (Visium_2, Xenium_2/7, CosMx_6) more abundant in melanoma, with collagen-CD44 signalling and Treg/fibroblast co-occurrence.

## My understanding

A practical answer to "is this niche real or a platform quirk?" — consensus across platforms is the test, and it enables cross-condition community comparison.
