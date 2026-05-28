---
title: "IL-32-β myeloid reprogramming to neutrophil-recruiting inflammation"
aliases:
  - IL-32-beta myeloid reprogramming
  - IL-32-beta chemokine switch
  - IL-32 neutrophil-recruiting cascade
maturity: emerging
tags:
  - IL-32
  - myeloid
  - chemokines
  - neutrophil-recruitment
  - inflammation
key_papers:
  - single-cell-cytokine-dictionary-human-peripheral
first_introduced: "2025"
date_updated: 2026-05-28
related_concepts:
  - cytokine-mediated-immune-cell-cell-interactome
  - secondary-cytokine-response-cascade
  - donor-baseline-interferon-signaling-heterogeneity
---

## Definition

A human-specific signaling axis in which IL-32-β reprograms myeloid cells (CD14/CD16 monocytes, cDCs) away from a Th1/antiviral chemokine profile (downregulating CXCL9, CXCL10, CXCL11, IL-18; median log2FC ~ −3.8) toward a neutrophil-recruiting profile (upregulating CXCL1, CXCL2, CXCL3, CXCL5, CXCL8 plus IL-1α/IL-1β; median log2FC ~ +5). IL-32-β is also the only cytokine that strongly upregulates the IL-10 family (IL-10, IL-19, IL-24) in myeloid cells, giving the response a self-regulating character.

## Intuition

IL-32-β flips monocytes from a "call in the T cells / fight viruses" program to an "acute, localized, neutrophil-driven containment" program — while simultaneously arming an IL-10-family brake to self-limit the inflammation. Because IL-32 has no mouse homologue, this axis is invisible in mouse models and is a candidate explanation for human-specific inflammatory biology.

## Variants

- Interferon-group donors: weaker IL-10-family induction but stronger Th1-chemokine downregulation
- DRVI program view: MyeloidRemodel + CytokineProd + Recruitment-2 up, ViralResponse down

## Comparison

Contrasts with interferon/common-γ-chain cytokines that upregulate ELR− CXCL (Th1-attractant) chemokines; IL-32-β does the opposite for myeloid chemokine output. Modulated by donor state (see [[donor-baseline-interferon-signaling-heterogeneity]]).

## When to use

When interpreting human myeloid inflammation where neutrophil-recruiting chemokines and IL-10-family cytokines co-rise; as a candidate axis in SLE (IL-32-β enriched in NK + non-classical monocytes during flare).

## Known limitations

- In vitro, single timepoint, supraphysiological dose
- No receptor identified for IL-32; mechanism partly inferred
- Donor-context dependence limits universality

## Open problems

- IL-32 receptor identity and isoform-specific effects
- In vivo / tissue relevance (tumor myeloid, autoimmune flares)
- Therapeutic targetability of a human-specific node

## Key papers

- [[papers/single-cell-cytokine-dictionary-human-peripheral]]

## My understanding

The headline mechanistic finding of the human Dictionary and a clean example of why a human atlas was needed: a dominant, human-specific myeloid switch absent from the mouse data. Worth tracking for tumor and autoimmune myeloid inflammation.
