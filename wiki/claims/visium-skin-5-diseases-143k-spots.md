---
title: "Visium ST integration spans 143k spots from 81 samples / 63 donors across normal skin and 5 skin diseases (AD, SCC, HS, BCC, PP)"
slug: visium-skin-5-diseases-143k-spots
status: supported
confidence: 0.9
tags: [skin, Visium, atopic-dermatitis, psoriasis, hidradenitis-suppurativa, SCC, BCC, methodological]
domain: methods / dermatology
source_papers:
  - single-cell-spatial-transcriptomic-analysis-human
evidence:
  - source: single-cell-spatial-transcriptomic-analysis-human
    type: supports
    strength: strong
    detail: "Quote (Fig. 6, p.10): 'Integration of Visium ST n = 63 donors, 5 skin diseases, k = 142,515 spots'."
conditions: "Public Visium ST datasets harmonised onto neighborhood label set."
date_proposed: 2026-05-27
date_updated: 2026-05-27
---

## Statement

The disease-mapping arm of the atlas integrates ~143k Visium ST spots (142,515) from 81 samples across 63 donors, covering normal skin plus atopic dermatitis, squamous-cell carcinoma, hidradenitis suppurativa, basal-cell carcinoma and psoriasis.

## Evidence summary

[[papers/single-cell-spatial-transcriptomic-analysis-human]] Fig. 6a.

## Conditions and scope

Public data integration; healthy MERFISH atlas used as reference for neighborhood prediction.

## Counter-evidence

None within paper.

## Linked ideas

## Open questions

- How does neighborhood mapping accuracy degrade with Visium spot resolution vs MERFISH single-cell ground truth?
