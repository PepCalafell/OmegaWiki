---
title: "LGP-factor axis — lactic acid + GM-CSF + PGE2 combinatorial TAM polarization"
aliases:
  - "LGP factors"
  - "LGP axis"
  - "lactic acid GM-CSF PGE2 axis"
tags:
  - TAM
  - macrophage-polarization
  - lactic-acid
  - PGE2
  - GM-CSF
  - tumor-microenvironment
  - combinatorial-signaling
maturity: emerging
key_papers:
  - functional-genetic-screens-reveal-key-pathways
first_introduced: "2025"
date_updated: 2026-07-23
related_concepts:
  - lactate-driven-tam-m2-polarization
  - angiogenic-mhc-ii-tam-mutual-exclusivity
  - m1-m2-polarization-paradigm
---

## Definition

The LGP-factor axis is a combinatorial model in which three tumor-derived factors — **L**actic acid, **G**M-CSF, and **P**GE2 — jointly and antagonistically instruct tumor-associated-macrophage (TAM) polarization. Lactic acid and PGE2 (LP) cooperatively induce the angiogenic/glycolytic program while suppressing MHC-II; GM-CSF drives the MHC-II-high antigen-presenting program. None of the three alone is sufficient for the full angiogenic phenotype — all three together are necessary and sufficient to reproduce the tumor-educated macrophage state.

## Intuition

Rather than a single master cytokine, TAM identity is set by the *ratio and combination* of metabolic and cytokine cues in the local niche. Lactic acid and PGE2 pull macrophages toward angiogenic/immunosuppressive; GM-CSF pulls toward MHC-II/antigen-presenting. Because LP and GM-CSF antagonise each other at the chromatin level, the two fates become mutually exclusive.

## Formal notation

Not applicable — a combinatorial signalling model. Operationalised as ARG1 induction and angiogenic/MHC-II signature scores under single vs. combinational treatment of L (25 mmol/L lactate), G (2 ng/mL GM-CSF), and P (100 nmol/L PGE2).

## Variants

- Tumor-intrinsic version: Ldha/Cox2 double-knockout in tumor cells removes L and P, shifting TAMs toward MHC-II in vivo.
- Receptor-level version: Ptger4/Ptger2 (PGE2), Hcar1/Mct1/Mct4 (lactate), and Csf2ra (GM-CSF) transduce the factors.

## Comparison

Extends the classical single-factor lactate model ([[lactate-driven-tam-m2-polarization]]) by showing lactate is necessary but not sufficient, and integrates GM-CSF as the antagonistic MHC-II driver. Supersedes the coarse [[m1-m2-polarization-paradigm]] for TAMs.

## When to use

Invoke when reasoning about why a given TAM subset dominates a tumor region, or when designing tumor-intrinsic (enzyme KO) vs. macrophage-intrinsic (receptor KO) strategies to redirect polarization.

## Known limitations

- Single-receptor knockouts only modestly shift the MHC-II/angiogenic ratio because lactate and PGE2 each signal through multiple redundant receptors.
- Other cues (hypoxia directly, TNFα, succinate) also modulate the phenotype and are not captured by the three-factor core.

## Open problems

- Quantitative dose-combination mapping of L/G/P to phenotype fractions.
- Whether the axis generalises beyond the tumor models tested to human TAMs in situ.

## Key papers

- [[functional-genetic-screens-reveal-key-pathways]] — defines the LGP axis via ex vivo CRISPR screens, RNA-seq/ATAC-seq combinatorial dissection, and in vivo CROP-seq.

## My understanding

The strength of the model is that it is anchored in both loss-of-function genetics (screens, KOs) and gain-of-function reconstitution (recombinant L+G+P recapitulates TCM). The antagonism at the chromatin level (LP closes GM-CSF-induced ETS sites) is what makes "mutually exclusive" a mechanistic statement rather than a correlational one.
