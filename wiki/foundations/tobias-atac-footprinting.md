---
title: "TOBIAS — transcription factor footprinting on ATAC-seq"
slug: tobias-atac-footprinting
domain: methods
status: mainstream
aliases: ["TOBIAS", "TOBIAS footprinting", "TF footprinting ATAC-seq", "ATACorrect", "BINDetect", "FootprintScores", "TOBIAS BINDetect", "differential TF footprinting", "TF footprint TOBIAS"]
first_introduced: "2020"
date_updated: 2026-05-22
source_url: "https://doi.org/10.1038/s41467-020-18035-1"
---

## Definition

ATAC-seq-based transcription factor footprinting toolkit (Bentsen et al. 2020). Three core steps: `ATACorrect` removes Tn5 cleavage bias; `FootprintScores` quantifies per-base footprint depth; `BINDetect` calls condition-specific differential TF binding by combining footprint scores with motif scanning against a PFM database (e.g. JASPAR2022). Outputs per-TF activity scores that can be aggregated across samples.

## Relevance to active research

- Standard tool for inferring differential TF activity from bulk or pseudobulk ATAC-seq across genotypes / conditions, when ChIP-seq is impractical.
- Used in [[jak-stat-signaling-maintains-homeostasis-cells]] (Fortelny et al. 2024) to identify mutant-specific TF activity shifts (RUNX2 in Stat5-hyp T cells, EOMES and FOS::JUN in Stat5-KO T cells, GATA1::TAL1 in Stat5-KO macrophages, NFKB2 in Stat6-KO macrophages, ZBED1 depletion in Stat4-KO T cells) — complementary to HOMER motif enrichment and LOLA region-set enrichment.
- Footprint inference is motif-based: a footprint "call" implies sequence-motif occupancy, not necessarily direct binding of any one TF that shares the motif family.
