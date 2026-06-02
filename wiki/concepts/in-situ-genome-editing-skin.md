---
title: "In situ genome editing of skin"
aliases:
  - "in situ skin genome editing"
  - "topical in vivo genome correction"
  - "in situ base editing of skin"
tags:
  - genome-editing
  - skin
  - gene-therapy
  - genodermatosis
  - base-editing
maturity: emerging
key_papers:
  - editing-skin-place-vivo-genome-correction
first_introduced: "2026"
date_updated: 2026-06-02
related_concepts: []
---

## Definition

In situ genome editing of skin is the correction of a disease-causing mutation directly within a patient's skin in place — without removing cells, editing them ex vivo, and grafting them back. It couples a precision genome editor (delivered as mRNA cargo) with a delivery route that reaches the regenerative basal keratinocyte (skin stem cell) compartment, so the correction is durable as the epidermis renews.

## Intuition

Skin is a paradoxical target: accessible, self-renewing, and dispensable in small areas (attractive for local therapy), yet it evolved specifically to exclude macromolecules and hides its stem cells beneath a formidable barrier (hard to reach non-invasively). In situ editing succeeds only when both halves are solved together — a single-nucleotide-precise editor *and* a delivery system that physically reaches and transfects the stem-cell compartment. Editing differentiated cells alone gives transient benefit; editing basal stem cells gives a potentially curative one.

## Variants

- **Ex vivo gene-corrected grafts** — edit keratinocytes in culture, expand, graft back (prior standard; invasive, limited scalability)
- **Gene augmentation in situ** (e.g. Vyjuvek/beremagene geperpavec, HSV-1 delivering collagen VII) — adds a functional gene copy topically but does not correct the underlying mutation
- **In situ genome correction** (this concept) — corrects the pathogenic mutation in place, here via topical mRNA-LNP base editor

## Comparison

Versus gene augmentation: in situ correction fixes the endogenous allele under native regulation rather than overlaying an exogenous copy, addressing durability and physiological-regulation concerns. Versus ex vivo grafting: in situ correction is non-invasive and targets the resident stem cells directly, but must overcome the skin barrier and currently covers only small surface areas.

## When to use

For monogenic genodermatoses with a defined, correctable point mutation and a quantifiable functional readout (e.g. *TGM1*/TG1 activity in ARCI). The modular framework — barrier modulation + LNP delivery + precision editor — is, in principle, adaptable across many single-gene skin diseases.

## Key papers

- [[papers/editing-skin-place-vivo-genome-correction]]

## Open problems

- Confirming durability of correction at time points beyond 48 h
- Competitive dynamics of corrected vs uncorrected skin stem cells
- Scaling from focal application to whole-body surface area
- Moving from immortalised human cells / 3D models to primary patient cells and clinical settings

## My understanding

The conceptual leap here is targeting the *stem-cell compartment in place*. Transient correction of differentiated keratinocytes is washed out by epidermal turnover; reaching basal keratinocytes is what makes "editing the skin in place" potentially durable. The delivery innovation ([[concepts/laser-microablation-transdermal-lnp-delivery]]) is what makes the stem-cell compartment reachable, and the precision editor ([[concepts/bystander-free-precision-base-editing]]) is what makes correction at a conserved splice site safe.
