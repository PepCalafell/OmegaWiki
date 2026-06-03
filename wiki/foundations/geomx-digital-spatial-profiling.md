---
title: "GeoMx Digital Spatial Profiler (DSP)"
slug: geomx-digital-spatial-profiling
domain: spatial omics
status: mainstream
aliases: ["GeoMx", "GeoMx DSP", "Digital Spatial Profiling", "GeoMx WTA", "GeoMx Whole Transcriptome Atlas", "GeoMx CTA"]
first_introduced: "2020"
date_updated: 2026-06-03
source_url: "https://nanostring.com/products/geomx-digital-spatial-profiler/"
---

## Definition

GeoMx Digital Spatial Profiler (NanoString/Bruker Spatial Biology) is a region-of-interest (ROI) based spatial profiling platform. Oligonucleotide-barcoded probes (for RNA or protein antibodies) are hybridised to a tissue section; UV light is then directed at user- or marker-defined ROIs/segments to photo-cleave the barcodes, which are aspirated and counted (nCounter or NGS readout). It supports a Whole Transcriptome Atlas (WTA, ~18k genes / 1820-oncogene CTA panel) and immune-oncology protein panels (e.g. 48 proteins).

## Intuition

Rather than measuring every cell, GeoMx measures *molecular profiles of segmented regions* — e.g. PanCK+ tumour vs CD45+ immune compartments on the same slide. This trades single-cell resolution for high analyte depth (full transcriptome or curated protein panels) within spatially and morphologically defined compartments.

## Formal notation

Not applicable (assay platform). Output is an ROI × analyte count matrix with associated segment masks (e.g. tumour/stroma/immune).

## Key variants

- **GeoMx WTA** — whole-transcriptome RNA readout
- **GeoMx CTA (Cancer Transcriptome Atlas)** — ~1820 oncogenes
- **GeoMx protein (IO panel)** — antibody-barcode protein quantification (~48 IO markers)

## Known limitations

- Not single-cell resolution; ROI-averaged signal requires deconvolution to infer cell-type composition
- Spatial resolution limited by segmentation/ROI size
- Dependent on quality of compartment masks (e.g. PanCK / CD45 gating)

## Open problems

- Robust deconvolution of ROI signal into cell-type proportions
- Cross-platform harmonisation with imaging-based single-cell spatial data (Xenium, CosMx)

## Relevance to active research

Used as an orthogonal protein/transcriptome validation layer in spatial multiomics atlases, confirming cell-type presence and compartment-specific signatures detected by single-cell spatial platforms.
