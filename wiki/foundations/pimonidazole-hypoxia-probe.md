---
title: "Pimonidazole — exogenous hypoxia marker probe"
slug: "pimonidazole-hypoxia-probe"
domain: "tumor hypoxia / histology"
status: mainstream
aliases:
  - "pimonidazole"
  - "Hypoxyprobe"
  - "pimonidazole hydrochloride"
first_introduced: "1980s"
date_updated: 2026-07-23
source_url: "https://hypoxyprobe.com/"
---

## Definition

Pimonidazole is a 2-nitroimidazole compound that is reductively activated and forms stable covalent adducts with thiol groups only in cells at oxygen tensions below ~10 mmHg (~1.3% O2). Adducts are detected with an anti-pimonidazole antibody by flow cytometry or immunofluorescence, marking which individual cells experienced hypoxia in vivo.

## Intuition

Unlike a transcriptomic hypoxia signature, which is an indirect readout, pimonidazole physically tags hypoxic cells at the time of injection. Injecting it ~60 min before euthanasia and then co-staining lets one ask, cell by cell, "was this macrophage sitting in a hypoxic niche?" — the assay that showed angiogenic TAMs, but not MHC-II+ TAMs, are pimonidazole-positive.

## Formal notation

Not applicable — an antibody-detected chemical adduct, quantified as mean fluorescence intensity or percent-positive cells.

## Key variants

- EF5 and CCI-103F — related 2-nitroimidazole immunochemical probes.
- [[fmiso-hypoxia-pet-tracer]] — the PET-imaging nitroimidazole analogue for non-invasive whole-tumor hypoxia mapping.

## Known limitations

- Requires in vivo administration before sampling; not usable on archival fixed tissue that was never exposed.
- Binary-ish threshold near ~1% O2; grades severe hypoxia poorly.
- Perfusion-dependent delivery can under-label poorly vascularised necrotic cores.

## Open problems

- Quantitative calibration of adduct level to absolute pO2 across tissues.
- Multiplexing with intracellular phenotypic markers while preserving surface epitopes for live-cell sorting.

## Relevance to active research

Pimonidazole staining is the standard single-cell hypoxia readout linking spatial oxygen tension to macrophage phenotype; it provided the direct evidence that angiogenic (CX3CR1−MHC-II−) TAMs occupy hypoxic niches whereas MHC-II+ TAMs reside in normoxic regions.
