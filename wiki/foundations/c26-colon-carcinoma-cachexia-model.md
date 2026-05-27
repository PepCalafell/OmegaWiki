---
title: "C26 colon carcinoma mouse model of cancer cachexia"
slug: c26-colon-carcinoma-cachexia-model
domain: oncology / cachexia models
status: mainstream
aliases:
  - "C26 cachexia model"
  - "Colon 26 cachexia"
  - "C-26 adenocarcinoma cachexia"
first_introduced: "Tanaka et al. 1990 Cancer Res (Colon 26 cachexia paper)"
date_updated: 2026-05-27
source_url: ""
---

## Definition

The C26 model is a subcutaneous (or intramuscular) implantation of the Colon 26 (C26) murine colon adenocarcinoma cell line into syngeneic BALB/c mice, producing a reproducible cachexia syndrome (~10% body-weight loss, muscle atrophy, adipose loss, systemic inflammation including high IL6) over 2-3 weeks. It is the most widely used mouse model of cancer cachexia.

## Intuition

C26 is to cachexia what Lewis lung carcinoma (LLC) is to metastasis: a workhorse model that produces uniform, fast-onset, IL6-driven cachexia ideal for mechanistic studies. The non-cachexia-inducing NC26 line (also used in [[papers/multi-omics-profiling-cachexia-targeted-tissues]]) is a critical negative control distinguishing tumour-presence effects from cachexia-specific effects.

## Formal notation

- Host strain: BALB/c (immunocompetent, syngeneic).
- Inoculum: typically 5×10⁵ – 1×10⁶ C26 cells s.c.
- Cachexia onset: ~10-14 days; cachexia (≥10% BW loss) by ~21 days.
- Tumour cytokine: high IL6 secretion (CRISPR Il6 KO abolishes cachexia despite tumour growth).
- Pre-cax stage: capturable around 7-10 days (before weight loss).

## Key variants

- C26 vs C26-IL6-KO (used by Morigny et al.) — clean genetic dissociation of IL6 from tumour mass.
- C26 vs NC26 — NC26 grows comparably but does not induce cachexia.
- Female vs male C26: most studies use male; female data sparse.

## Known limitations

- Fast-onset cachexia atypical of indolent human disease.
- BALB/c-specific immune background; results may not generalise across strains.
- Most studies have used males — sex differences underexplored.

## Open problems

- Detailed time-resolved transcriptome / metabolome dynamics through pre-cax → cax transition (only partially covered by [[papers/multi-omics-profiling-cachexia-targeted-tissues]]).
- Long-term survival endpoint comparisons across interventions.

## Relevance to active research

Primary model used in [[papers/multi-omics-profiling-cachexia-targeted-tissues]] for multi-tissue metabolomics + transcriptomics + 13C6-glucose tracing across Ctrl / Non-cax (NC26) / Pre-cax / Cax stages. Findings extended to five additional mouse models (Panc02, 8025, ApcMin, LLC, KPP) and a humanised SW480 model.
