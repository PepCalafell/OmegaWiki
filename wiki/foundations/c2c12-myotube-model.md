---
title: "C2C12 myotube model"
slug: c2c12-myotube-model
domain: cell biology / muscle biology
status: mainstream
aliases:
  - "C2C12"
  - "C2C12 myoblast / myotube"
  - "ATCC CRL-1772"
first_introduced: "Yaffe & Saxel 1977 (C2 line); Blau 1985 (C2C12 subclone)"
date_updated: 2026-05-27
source_url: ""
---

## Definition

C2C12 is an immortalised mouse myoblast cell line that differentiates into multinucleated myotubes upon serum withdrawal (2% FBS, ~5 days). Differentiated C2C12 myotubes are the workhorse in vitro model for skeletal muscle atrophy/hypertrophy assays, glucose metabolism studies, and cytokine response experiments — including cachexia-mimicking protocols (DEX, IL6, TNF, conditioned media from tumour cells).

## Intuition

C2C12 myotubes provide the simplest, most tractable in vitro readout of muscle atrophy: ImageJ-quantified diameter measurements across 40-60 myotubes/well, paired with metabolic flux (glucose consumption, 13C-glucose tracing) and gene-expression readouts. It is the in vitro counterpart of skeletal muscle in cachexia studies.

## Formal notation

- Origin: mouse skeletal myoblast, ATCC CRL-1772.
- Growth: 10% FBS DMEM (high glucose + pyruvate + L-glutamine).
- Differentiation: 2% FBS DMEM for 5 days; multinucleated long contractile myotubes used for experiments.
- Standard atrophy stimuli: dexamethasone, recombinant TNF, recombinant IL6, conditioned media from C26/LLC cells.

## Key variants

- C2 (parental line) vs C2C12 (Blau subclone, more uniform myotube differentiation).
- L6 rat myoblast as an alternative rodent myotube model.
- Primary mouse satellite-cell-derived myotubes (more physiological but more variable).

## Known limitations

- Immortalised cell line; mouse origin; not equivalent to mature in vivo skeletal muscle fibres.
- Diameter is a morphological proxy; molecular atrophy markers (ubiquitin-proteasome flux, autophagy flux) should be measured in parallel.

## Open problems

- Whether C2C12-derived insights into methionine/one-carbon-driven atrophy translate to human iPSC-derived myotubes or primary human muscle.

## Relevance to active research

Used in [[papers/multi-omics-profiling-cachexia-targeted-tissues]] for the L-methionine dose-response atrophy experiment, FIDAS-5 hypertrophy/hypometabolism experiment, IL6-driven atrophy + FIDAS-5 rescue, and 13C6-glucose / [1-13C]-pyruvate tracing of TCA hypermetabolism — the core in vitro causality engine of the paper.
