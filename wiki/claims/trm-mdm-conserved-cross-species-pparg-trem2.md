---
title: "TRM (PPARG/MARCO) and MDM (TREM2/SPP1/APOE) NSCLC signatures are conserved across human and mouse"
slug: trm-mdm-conserved-cross-species-pparg-trem2
status: supported
confidence: 0.85
tags:
  - cross-species
  - signature-conservation
  - NSCLC
  - TRM
  - MDM
  - PPARG
  - TREM2
domain: "immunology / oncology / genomics"
source_papers:
  - tissue-resident-macrophages-provide-pro-tumorigenic
evidence:
  - source: tissue-resident-macrophages-provide-pro-tumorigenic
    type: supports
    strength: strong
    detail: "Cross-species comparison (Fig. 1c): genes upregulated above log2 fold-change 1.1 in homologous cell types in each species, log-transformed and z-scaled. Mouse and human group I clusters share PPARG, MARCO, SIGLEC1, STMN1 (cell-cycle), TUBA1B (suggesting self-renewal). Mouse and human group II clusters share APOE, TREM2, SPP1, GPNMB (lipid metabolism), CCR2, CD14 (monocyte-identity). Mouse group III ↔ human CD14⁺ monocytes; mouse group IV ↔ human CD16⁺ monocytes."
conditions: "Cross-species transcriptional comparison; intraspecies log2 fold-change > 1.1; z-scaled visualisation; mouse KP NSCLC and human NSCLC scRNA-seq (35 patients, Mount Sinai cohort)."
date_proposed: 2026-05-06
date_updated: 2026-05-06
---

## Statement

Despite broad cross-species transcriptional divergence in macrophage subtypes, the four conserved myeloid groups in NSCLC share defining marker modules between mouse and human: group I (PPARG, MARCO, SIGLEC1, STMN1, TUBA1B — alveolar TRM), group II (APOE, TREM2, SPP1, GPNMB, CCR2, CD14 — monocyte-derived TAM), and groups III/IV (CD14⁺ and CD16⁺ monocytes). This conservation supports the cross-species translatability of mouse lineage-tracing findings to human NSCLC.

## Evidence summary

- Intraspecies log2 fold-change > 1.1 cell-type-defining genes
- Z-scaled cross-species visualisation (Fig. 1c)
- Independent validation against an inDrop NSCLC dataset (Zilionis 2019, GSE127465) and against bulk RNA-seq of purified human alveolar macrophages (Leach 2020, Cell Reports 33, 108337)

## Conditions and scope

- Mouse KP orthotopic NSCLC + human NSCLC scRNA-seq (35-patient Mount Sinai cohort)
- Cross-validated via two independent public datasets
- Conservation defined at the group-level signature, not single-gene

## Counter-evidence

- Many other genes diverge between species; only the conserved gene module is the basis for cross-species inference
- Conservation does not prove functional equivalence; the human group I cluster may not have identical EMT-niche function

## Linked ideas

(none yet)

## Open questions

- Whether functional assays (Treg licensing, EMT induction) replicate in human alveolar macrophage + NSCLC organoid systems
- Single-cell-resolution mapping of mouse fate-mapping data onto human NSCLC scRNA-seq
- Whether intra-group heterogeneity is similarly conserved across species
