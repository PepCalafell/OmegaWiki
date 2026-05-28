---
title: "Microbiome–host protein meta-interactome (HuMMI)"
aliases:
  - HuMMI
  - human microbiome meta-interactome
tags:
  - microbiome
  - host-pathogen
  - interactome
  - hummi
maturity: emerging
key_papers:
  - effector-host-interactome-map-links-type
first_introduced: "2026"
date_updated: 2026-05-28
related_concepts:
  - commensal-t3ss-host-directed-secretion
  - effector-convergence-host-hub-proteins
---

## Definition

HuMMI is the first systematic, experimentally verified protein–protein interaction map
between commensal bacterial T3SS effectors and human proteins, built by multi-assay
(Y2H + orthogonal validation) screening of a cloned human-microbiome effector ORFeome
against the human ORFeome.

## Intuition

A "wiring diagram" connecting which bacterial effectors physically touch which human
proteins, enabling systems-level inference of effector function via host-network context.

## Formal notation

HuMMI = HuMMIMAIN ∪ HuMMIRPT ∪ HuMMIHOM; final map = 1,255 unique verified interactions
between 286 effectors and 426 human proteins. Sampling sensitivity of the main screen
≈ 32%.

## Variants

HuMMIMAIN (main screen, 1,067 interactions), HuMMIRPT (repeat screens, saturation
estimate), HuMMIHOM (homolog-profiling, 181 non-redundant).

## Comparison

Analogous in spirit to plant effector–host interactome maps and to [[huri-human-reference-interactome]],
but for cross-kingdom commensal effector–human interactions.

## When to use

As the resource underlying convergence, interface, disease-module and functional
analyses of commensal effectors.

## Known limitations

Y2H sensitivity (~13–17.5%); sampling sensitivity ~32%; prokaryotic proteins harder to
test in some assays.

## Open problems

Scaling to more strains/effectors; capturing modification- and context-dependent
interactions.

## Key papers

- [[effector-host-interactome-map-links-type]] — defines and validates HuMMI.

## My understanding

HuMMI is the central deliverable of the paper — the dataset from which every downstream
biological claim is derived.
