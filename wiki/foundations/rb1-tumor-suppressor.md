---
title: "RB1 (retinoblastoma 1) tumor suppressor"
slug: rb1-tumor-suppressor
domain: oncology
status: mainstream
aliases:
  - RB1
  - retinoblastoma protein
  - pRb
  - Rb
  - retinoblastoma tumor suppressor
  - RB pocket protein
  - p105-Rb
first_introduced: "1986 (RB1 cloned, Friend et al.)"
date_updated: 2026-05-26
source_url: "https://www.ncbi.nlm.nih.gov/gene/5925"
---

## Definition

RB1 encodes the retinoblastoma protein (pRb), a pocket protein and master G1/S checkpoint regulator. Hypophosphorylated pRb binds and inhibits E2F transcription factors, blocking transcription of S-phase entry genes; CDK4/6-cyclin D phosphorylation of pRb releases E2F, enabling G1→S transition.

## Intuition

pRb is the "brake" on the cell cycle's G1/S gate. Its loss (mutation, deletion, or HPV E7-mediated degradation) accelerates cell-cycle entry and biases tumours toward G1/S accumulation of cycling cells (consistent with the 3CA pan-cancer finding that RB1 mutation associates with G1/S phase bias).

## Key variants and contexts

- **Familial retinoblastoma** — germline RB1 inactivation.
- **Small cell lung cancer** — nearly universal RB1 loss.
- **HPV+ tumours** — pRb is functionally degraded by HPV E7 even without mutation (see [[foundations/hpv-oncoprotein-e6-e7]]).
- **CDK4/6 inhibitors** (palbociclib, ribociclib, abemaciclib) require intact RB1 to work — RB1-deficient tumours are resistant.
- **Triple-negative breast cancer, prostate neuroendocrine** — frequent RB1 loss.

## Known limitations

- "RB1 wild-type" by sequencing can still be functionally inactivated by upstream loss (e.g. CDKN2A deletion → CDK4/6 hyperactivation → pRb hyperphosphorylation).
- HPV E7 inactivation is post-translational, not visible from genomic data.

## Open problems

- Selecting CDK4/6 inhibitors based on pRb functional status rather than RB1 mutation alone.
- RB1-loss-driven lineage plasticity (neuroendocrine differentiation).

## Relevance to active research

In pan-cancer scRNA-seq, RB1 mutation correlates with G1/S phase bias of cycling malignant cells ([[curated-cancer-cell-atlas-provides-comprehensive]]). The interaction with HPV E7 explains the opposite phase bias of HPV+ vs HPV− HNSCC.
