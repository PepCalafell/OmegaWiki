---
title: "RETICLE — real-time search-assisted MS acquisition for scp-MS"
slug: reticle-realtime-search-acquisition
domain: "methods / mass spectrometry"
status: mainstream
aliases:
  - RETICLE
  - real-time search acquisition
  - RTS-assisted scp-MS
  - real-time search Orbitrap
  - MS3 RTS scp-MS
  - real-time peptide search
  - RETICLE Schoof
  - intelligent data acquisition MS
first_introduced: "Furtwängler & Schoof et al. (RETICLE method); cited as ref 28 of the Furtwängler 2025 *Science* paper"
date_updated: 2026-05-26
source_url: ""
---

## Definition

RETICLE is a real-time search-assisted data acquisition method for single-cell proteomics by mass spectrometry. During an LC-MS/MS run, RETICLE performs a real-time peptide database search on each MS2 spectrum and decides on-the-fly whether to elevate the precursor to MS3 / SPS-MS3 acquisition for reporter-ion quantification. The result is higher quantification accuracy and more single-cell-relevant precursors selected per unit instrument time.

## Intuition

Standard data-dependent acquisition (DDA) wastes instrument time on uninformative MS2 events. By identifying candidate peptide-spectrum matches in real time, RETICLE redirects scan time to peptides most likely to yield reliable quantification in the single-cell channels.

## Formal notation

Workflow per MS scan:
1. MS1 survey scan.
2. Trigger MS2 on top-N precursors.
3. RETICLE real-time DB search on each MS2.
4. If PSM passes a confidence threshold, trigger MS3 / SPS-MS3 with TMT reporter-ion quantification.
5. Repeat over the LC gradient.

## Key variants

- SPS-MS3 (synchronous precursor selection) for reporter-ion quantification.
- Alternative: Orbitrap RTS plus FAIMS for ion-mobility separation.

## Known limitations

- Real-time search introduces instrument software / hardware dependencies (Orbitrap Eclipse / Tribrid with RTS firmware).
- Throughput gain depends on the proteome complexity and gradient length.

## Open problems

- Open-source RTS implementations to broaden adoption beyond Thermo Tribrid hardware.

## Relevance to active research

- Used as the acquisition method for the scp-MS dataset in [[papers/mapping-early-human-blood-cell-differentiation]].
