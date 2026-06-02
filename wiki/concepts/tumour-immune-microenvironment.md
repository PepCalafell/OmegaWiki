---
title: "Tumour immune microenvironment (immune TME)"
aliases:
  - tumour immune microenvironment
  - immune TME
  - TIME
  - tumour microenvironment immune compartment
  - TME immune cells
  - intratumoural immune compartment
  - immune component of TME
  - cancer immune microenvironment
  - tumour-infiltrating immune cells
  - tumour immune contexture
tags: [oncology, immunology, tumour-microenvironment]
maturity: stable
key_papers:
  - cancer-organoids-modelling-complexity-tumour-immune
  - tumor-induced-metabolic-immunosuppression-mechanisms-therapeutic
  - regulation-immunity-inflammation-hypoxia-immunological-niches
first_introduced: ""
date_updated: 2026-05-22
related_concepts: [hot-cold-tumour-immune-classification, immune-checkpoint-blockade, tertiary-lymphoid-structure, tumour-infiltrating-lymphocyte]
---

## Definition

The tumour immune microenvironment is the spatially organized assembly of lymphoid and myeloid immune cells, cancer-associated fibroblasts, vasculature and extracellular matrix that surrounds and infiltrates malignantly transformed cells. Its composition vitally regulates cancer progression, response to therapy and patient outcome.

## Intuition

Tumours occupy a spectrum from "hot" (acute-inflammation-like) to "cold" (chronic-inflammation-like). Hot infiltrates (CD8+, TH1, NK, ILC2, eosinophils, M1 macrophages, CX3CR1hi monocytes, DC1, TLSs) typically correlate with favourable prognosis and ICB sensitivity, whereas cold infiltrates (M2 macrophages, MDSCs, TH2, Treg, exhausted CD8, Breg, CCR2hi monocytes, mregDC) are pro-tumorigenic and ICB-resistant.

## Variants

- **Hot/inflamed TME** — dense CD8 + DC1 + TLS infiltration; strong neoantigen burden in MMR-deficient tumours.
- **Cold/immune-excluded TME** — immunosuppressive myeloid dominance.
- **Cold/immune-desert TME** — minimal immune infiltration.

## Known limitations of current models

- Conventional epithelial-only PDOs lack the immune TME entirely.
- Reconstituted PDOs disrupt native immune-stromal spatial organization.
- Most multiplexed imaging methods (CODEX, MIBI) sample fixed tissue and lose live interactions.

## Open problems

- Causal mechanisms switching cold to hot TMEs.
- Role of hypoxic niches in shaping immune exclusion (see [[hypoxia-immune-evasion-clonal-selection]]).
- Spatial-transcriptomic mapping of TLS formation across tumour types.

## Key papers

- [[cancer-organoids-modelling-complexity-tumour-immune]]

## My understanding

The immune TME is the dominant explanatory variable for both spontaneous tumour control and ICB response, but is poorly captured by epithelial-only models. Native immune organoids (ALI, PDOTS) and multiplexed spatial methods (CODEX, MIBI) provide the most faithful current readouts.
