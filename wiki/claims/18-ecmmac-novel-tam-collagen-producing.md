---
title: "Cluster 18_ECMMac is a previously-undescribed TAM subset characterized by COL1A1/COL1A2/COL3A1 production, likely on a TAM→fibroblast differentiation path"
slug: 18-ecmmac-novel-tam-collagen-producing
status: supported
confidence: 0.85
tags: [TAM,18_ECMMac,collagen,ECM,macrophage-fibroblast-differentiation]
domain: immuno-oncology
source_papers:
  - using-pan-cancer-atlas-investigate-tumour
evidence:
  - source: using-pan-cancer-atlas-investigate-tumour
    type: supports
    strength: strong
    detail: "Quote (p.8): 'One cluster identified here that is absent from other TAM analyses is 18_ECMMac. These macrophages showed high levels of increased collagen production compared to other TAM subsets in the atlas. This cluster most likely represents an avenue towards fibroblast differentiation'."
conditions: "23-cluster Seurat RPCA atlas; 18_ECMMac defined by COL1A1/COL1A2/COL3A1 + CD68; absent in Mulder 2021 MoMac-VERSE and Cheng 2021 myeloid atlas at comparable resolution; CosMx spatial co-expression in lung tumour tissue."
date_proposed: 2026-05-13
date_updated: 2026-05-13
---

## Statement

18_ECMMac is a TAM subset newly resolved by the Coulton 2024 pan-cancer atlas, defined by high expression of collagen genes (COL1A1, COL1A2, COL3A1) and likely representing an intermediate cell state on a TAM-to-myofibroblast differentiation trajectory. It is absent from comparable pan-cancer myeloid/MNP atlases (Mulder 2021, Cheng 2021).

## Evidence summary

Reported and characterized in [[papers/using-pan-cancer-atlas-investigate-tumour]] (Coulton et al., *Nat Commun* 2024); spatial validation via CosMx FFPE NSCLC (Fig. 4d).

## Conditions and scope

Human pan-cancer TAMs at 23-cluster Louvain resolution; enriched in ccRCC (28.2%), HGSOC (15.4%), CRC (14.9%); absent in oral cancer (Luoma 2022 projection).

## Counter-evidence

The collagen signature overlaps with fibroblasts — bulk-RNAseq attribution to TAMs vs fibroblasts is not unambiguous. CosMx CD68+/COL+ co-expression mitigates but does not eliminate this confound.

## Linked ideas

## Open questions

- Is 18_ECMMac a transient or terminal state?
- Why is it absent in oral cancer?
- Does it share ontogenetic origin (monocyte-derived vs tissue-resident) across cancer types?
