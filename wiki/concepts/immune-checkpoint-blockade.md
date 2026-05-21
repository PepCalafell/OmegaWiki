---
title: "Immune-checkpoint blockade (ICB)"
aliases:
  - ICB
  - immune checkpoint inhibitor
  - immune checkpoint inhibitors
  - ICI
  - checkpoint blockade
  - checkpoint inhibitor therapy
  - anti-PD1 therapy
  - anti-PD-L1 therapy
  - anti-CTLA4 therapy
  - PD1 blockade
  - PD-L1 blockade
  - CTLA4 blockade
  - anti-checkpoint antibody
tags: [immunotherapy, oncology, checkpoint]
maturity: stable
key_papers:
  - cancer-organoids-modelling-complexity-tumour-immune
first_introduced: ""
date_updated: 2026-05-21
related_concepts: [tumour-immune-microenvironment, tumour-infiltrating-lymphocyte, hot-cold-tumour-immune-classification]
---

## Definition

Immune-checkpoint blockade is a cancer immunotherapy strategy that uses antibodies (or, increasingly, small molecules) to neutralize inhibitory receptors on T cells (CTLA4, PD1, LAG3, TIM3, TIGIT) or ligands on tumour/myeloid cells (PD-L1, CD47, CD24) that suppress antitumour immunity.

## Intuition

Tumours hijack physiological brakes on T cell activation to evade immune surveillance. ICB removes those brakes, allowing tumour-reactive effector T cells to expand and kill cancer cells. Efficacy correlates broadly with neoantigen burden (e.g. MMR-deficient tumours) and pre-existing CD8 infiltration.

## Variants

- **Single-agent ICB** — anti-CTLA4 (ipilimumab), anti-PD1 (nivolumab, pembrolizumab), anti-PD-L1 (atezolizumab, durvalumab).
- **Combination ICB** — CTLA4 + PD1, LAG3 + PD1.
- **Macrophage checkpoint blockade** — anti-CD47, anti-CD24.
- **Bispecific T cell engagers (BiTEs)** — CD19, CD20, BCMA-targeted.
- **Combination with targeted therapy** — BRAF/MEK + ICB.

## When to use

- Solid tumours with hot/inflamed TME (melanoma, NSCLC, RCC, MMR-deficient CRC, HNSCC).
- Hematological malignancies with checkpoint expression (cHL).
- Increasingly tested in neoadjuvant settings.

## Known limitations

- Response rates vary substantially between histologies and patients.
- Resistance — primary (cold tumours, low neoantigen burden) and acquired (T cell exhaustion, antigen loss).
- Predictive biomarkers (PD-L1 IHC, TMB, gene signatures) have only moderate predictive value.

## Open problems

- Robust per-patient predictors of ICB response.
- Strategies to convert cold tumours to hot.
- Mechanistic drivers of acquired resistance.

## Key papers

- [[cancer-organoids-modelling-complexity-tumour-immune]]

## My understanding

Organoid-based ex vivo ICB testing is one of the most promising routes to functional, per-patient response prediction — provided the platform retains the original tumour's immune TME. Native immune organoids and pooled tumour explants currently lead in correlative evidence.
