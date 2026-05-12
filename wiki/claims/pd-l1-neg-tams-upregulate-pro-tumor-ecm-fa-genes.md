---
title: "PD-L1−/lo TAMs upregulate pro-tumor genes (SPP1, MMP9, SPARC), fatty acid metabolism (FABP4/5, LPL), and ECM organization (FN1, COL1A1/2, COL3A1)"
slug: pd-l1-neg-tams-upregulate-pro-tumor-ecm-fa-genes
status: supported
confidence: 0.9
tags:
  - PD-L1
  - TAM
  - SPP1
  - MMP9
  - FABP4
  - FN1
  - collagen
  - pro-tumor
  - breast-cancer
domain: "immunology / scRNA-seq"
source_papers:
  - pd-l1-expressing-tumor-associated-macrophages
evidence:
  - source: pd-l1-expressing-tumor-associated-macrophages
    type: supports
    strength: strong
    detail: "Wang 2024 Fig. 1G,I, S4D-E: DEG analysis identifies upregulation in PD-L1−/lo TAMs of CD9, CD52, IL1RN, CSTB (anti-inflammatory); SPP1 (osteopontin), MMP9, SPARC (pro-tumor); FABP4, FABP5, LPL (fatty acid metabolism); FN1, COL1A1/2, COL3A1 (ECM organization). Hallmark gene set enrichment shows PD-L1−/lo TAMs are enriched for epithelial-mesenchymal transition (Fig. S2D). Replicated in Pal 2021 TNBC (SPP1, TREM2, IL1RN, CD9, FABP4/5, LPL, FN1)."
conditions: "Untreated primary breast tumors; ER+ and TNBC; cluster-level differential expression."
date_proposed: 2026-05-12
date_updated: 2026-05-12
---

## Statement

PD-L1−/lo TAMs in human breast cancer express anti-inflammatory mediators (IL1RN, CD52, CD9), pro-tumor osteopontin/MMP/SPARC, fatty acid metabolic enzymes (FABP4/5, LPL), and extracellular matrix organizers (FN1, collagens) — collectively a tissue-remodeling, pro-tumor TAM phenotype that aligns with the canonical "TREM2 / SPP1 macrophage" lineage in pan-cancer atlases.

## Evidence summary

- Wang 2024 Fig. 1G (volcano), Fig. 1I (selected genes), Fig. S2D (hallmark enrichment, EMT).
- Replication: Fig. S4D-E in Pal 2021 TNBC.

## Conditions and scope

- Cluster-level differential expression; protein-level validation limited to selected markers (TREM2 / SPP1 via published references).

## Counter-evidence

- None within Wang 2024; cross-validation with TREM2 / SPP1 TAM literature is consistent.

## Linked ideas

- Functional consequence supports [[claims/pd-l1-neg-macs-suppress-cd8-bite-killing]].
- Lineage relationship with [[concepts/trem2-tumor-associated-macrophage]] (Park 2021 and others).

## Open questions

- Whether the PD-L1−/lo signature overlaps with FABP5-driven lipid-laden TAM phenotypes observed in obesity contexts.
- Whether ECM-producing PD-L1− TAMs are pro-fibrotic in vivo.
