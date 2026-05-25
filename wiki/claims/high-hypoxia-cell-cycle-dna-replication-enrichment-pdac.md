---
title: "High hypoxia group in TCGA-PAAD is enriched for cell-cycle, DNA replication, E2F, G2M, and protein-processing pathways by GSEA"
slug: high-hypoxia-cell-cycle-dna-replication-enrichment-pdac
status: supported
confidence: 0.65
tags: [hypoxia,PDAC,GSEA,cell-cycle,DNA-replication,E2F,G2M,proliferation]
domain: oncology-hypoxia
source_papers:
  - development-hypoxia-responsive-macrophage-prognostic-model
evidence:
  - source: development-hypoxia-responsive-macrophage-prognostic-model
    type: supports
    strength: medium
    detail: "Quote (p.9, Results): 'the high hypoxia group exhibited significant enrichment in several critical pathways, including biosynthesis of amino acids, cell cycle, DNA replication, nucleocytoplasmic transport, nucleotide metabolism, protein processing in the endoplasmic reticulum, ribosome, E2F targets, G2M checkpoint, hypoxia and mitotic spindle (Fig 5A and 5B)'. GSEA via clusterProfiler with MSigDB Hallmark / KEGG sets; NES |> 1|, FDR < 0.25, p < 0.05."
conditions: "Bulk TCGA-PAAD; ranking by hypoxia score; clusterProfiler default settings."
date_proposed: 2026-05-25
date_updated: 2026-05-25
---

## Statement

GSEA on TCGA-PAAD ranked by 13-gene hypoxia score reveals that high-hypoxia tumours are enriched for proliferative pathways (cell cycle, DNA replication, E2F targets, G2M checkpoint, mitotic spindle), translation/protein processing (ribosome, protein processing in ER), and nucleotide / amino-acid metabolism — alongside the canonical Hallmark Hypoxia signature itself.

## Evidence summary

Reported in [[papers/development-hypoxia-responsive-macrophage-prognostic-model]] (Ge et al., *PLoS One* 2025, Fig 5A–B). Consistent with literature linking hypoxia to a proliferative, replication-stressed state in aggressive tumours.

## Conditions and scope

- Single cohort, single ranking criterion; FDR threshold of 0.25 is lenient.
- The hypoxia score is partially derived from macrophage genes (LYZ, PLAU), so enrichment may partially reflect myeloid infiltration rather than tumour-cell-intrinsic proliferation.

## Counter-evidence

None within paper scope.

## Linked ideas

## Open questions

- Is the proliferation signature driven by tumour cells or by infiltrating immune cells?
- Does the high-hypoxia G2M-checkpoint enrichment translate to differential sensitivity to CDK4/6 or WEE1 inhibitors?
