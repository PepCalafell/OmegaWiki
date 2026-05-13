---
title: "Hypoxia PET imaging tracers"
aliases:
  - hypoxia tracer
  - FMISO PET
  - 18F-FMISO
  - 18F-HX4
  - 18F-EF5
  - hypoxia imaging
  - non-invasive hypoxia detection
  - 2-nitroimidazole PET tracer
  - hypoxia PET biomarker
  - hypoxia imaging biomarker
tags:
  - hypoxia
  - imaging
  - PET
  - biomarker
  - clinical
maturity: active
key_papers:
  - hypoxic-microenvironment-cancer-molecular-mechanisms-therapeutic
first_introduced: "FMISO 1980s (Rasey); clinical era 2000s"
date_updated: 2026-05-13
related_concepts:
  - tumor-hypoxia-classification-chronic-acute-cyclic
  - tumor-hypoxia-mrna-signature
---

## Definition

Hypoxia PET tracers are radiolabeled 2-nitroimidazole / pentafluorinated nitroimidazole compounds (¹⁸F-FMISO, ¹⁸F-HX4, ¹⁸F-EF5) that are selectively reduced and trapped in hypoxic cells, enabling non-invasive, voxel-resolved quantification of tumor hypoxia by PET. They are the clinical analog of FACS hypoxia probes (EF5, pimonidazole) for in vivo human imaging.

## Intuition

Under normoxia, nitroimidazoles undergo one-electron reduction reversibly. Under hypoxia (<10 mmHg), the radical is further reduced and irreversibly bound to macromolecules, trapping the tracer. PET then maps hypoxia voxel-by-voxel. Clinical use: stratify patients for radiotherapy dose-painting, monitor HAPs, screen for ICB-responsive vs ICB-refractory hypoxic phenotype.

## Variants

- ¹⁸F-FMISO (1-[2-nitro-1H-imidazol-1-yl]-3-fluoro-2-propanol) — most clinically tested
- ¹⁸F-HX4 (3-[¹⁸F]fluoro-2-[4-{(2-nitro-1H-imidazol-1-yl)methyl}-1H-1,2,3-triazol-1-yl]-propan-1-ol) — better pharmacokinetics
- ¹⁸F-EF5 (pentafluorinated analog) — used in HNSCC trials
- ⁶⁴Cu-ATSM (Cu-diacetyl-bis(N4-methylthiosemicarbazone)) — distinct mechanism, faster clearance

## When to use

Cite when discussing in vivo human quantification of hypoxia, biomarker-stratified trials for HAPs / belzutifan / ICB, or rationale for dose-painted radiotherapy.

## Known limitations

- Low tumor-to-background ratio (FMISO ≈ 1.3–1.5) — requires careful threshold calibration.
- Cannot distinguish chronic vs cycling hypoxia.
- Not all hypoxia signatures (mRNA) co-localize with tracer uptake — orthogonal measures.

## Open problems

- Whether tracer-guided dose painting improves outcomes prospectively.
- Combining hypoxia PET with mRNA hypoxia signatures for orthogonal biomarker stratification.
- Detection of pseudohypoxic vs true hypoxic tumors (likely tracer-negative pseudohypoxia).

## Key papers

- [[papers/hypoxic-microenvironment-cancer-molecular-mechanisms-therapeutic]] — review of clinical trial usage of FMISO, HX4, EF5.

## My understanding

Hypoxia PET is the only non-invasive whole-tumor hypoxia measurement clinically validated and FDA-approved — but its therapeutic-decision utility remains underexploited. For thesis work, PET tracers + mRNA signatures + spatial-WGS will become the trifecta for stratifying hypoxic-but-pseudohypoxic vs truly hypoxic tumors.
