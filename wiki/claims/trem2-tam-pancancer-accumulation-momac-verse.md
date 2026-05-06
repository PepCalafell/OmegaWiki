---
title: "TREM2⁺ TAMs accumulate across all six human cancer types in the MoMac-VERSE"
slug: trem2-tam-pancancer-accumulation-momac-verse
status: supported
confidence: 0.85
tags:
  - TREM2
  - TAM
  - cancer
  - pan-cancer
  - macrophage
  - tumor-microenvironment
domain: "oncology / immunology"
source_papers:
  - cross-tissue-single-cell-landscape-human
evidence:
  - source: cross-tissue-single-cell-landscape-human
    type: supports
    strength: strong
    detail: "MoMac-VERSE cluster #3 (TREM2_Mac) is significantly increased in tumour vs matched healthy/normal-adjacent tissue across all 6 cancer scRNA-seq datasets included in the study (lung Kim, colon Zhang10X, colon Lee, liver Zheng10X, liver Sharma, breast Azizi, stomach Irac, pancreas Peng); paired t-test p<0.0001 (Fig. 4N). Cross-species validation: TREM2_Mac shares signature with murine Trem2 TAMs (Katzenelenbogen 2020; Molgora 2020). Mouse Ms4a3-Cre fate-mapping: TREM2_Mac is predominantly monocyte-derived."
conditions: "Pan-cancer scRNA-seq across 6 tumour types with paired healthy / normal-adjacent samples; cluster identity assigned via MoMac-VERSE Phenograph."
date_proposed: 2026-05-06
date_updated: 2026-05-06
---

## Statement

TREM2⁺ TAMs (MoMac-VERSE cluster #3) are significantly enriched in human tumours of liver, lung, colon, breast, stomach, and pancreas compared with matched healthy or normal-adjacent tissue. They are predominantly monocyte-derived and show conserved transcriptional programmes across cancer types and across species.

## Evidence summary

- Paired t-test across 6 cancer datasets: TREM2_Mac frequency higher in tumour vs healthy (p<0.0001).
- Cluster #3 DEtGs include TREM2, APOE, GPNMB, SPP1, FABP5, MARCO, lipid-handling and phagocytic-maturation genes.
- Cross-species: shares signature with murine Trem2 TAMs in colon (Katzenelenbogen 2020) and breast/sarcoma (Molgora 2020).
- Mouse Ms4a3cre-RosatdTomato lineage tracing on liver scRNA-seq: TREM2⁺Spp1⁺ Macs are predominantly monocyte-derived.
- Flow-cytometry validation on lung adenocarcinoma (3 patients) confirms TREM2 marker accumulation in tumour, corroborating the scRNA-seq frequency.

## Conditions and scope

- Established for 6 epithelial-origin solid tumours; not directly tested in haematological malignancies or paediatric tumours.
- Frequency calculation is on MNP fraction (Mo/Mac); absolute density per tumour mass is not reported.

## Counter-evidence

- Some recent reports describe context-dependent TREM2 functions (lipid clearance, tissue repair) that complicate the universally-pro-tumour reading.
- Bulk-deconvolution-derived TREM2 signatures may conflate TREM2_Mac with related lipid-associated populations (LAM, DAM).

## Linked ideas

(none yet)

## Open questions

- Whether TREM2 TAM accumulation is causal vs reactive in tumour growth.
- Tumour-specific sub-states of TREM2_Mac (e.g. TREM2⁺C1Q⁺ vs TREM2⁺Spp1⁺ axes).
- Therapeutic response to anti-TREM2 antibodies in solid tumours.
