---
title: "A 15-gene mRNA signature robustly classifies tumour hypoxia status across cancer types"
slug: 15-gene-hypoxia-signature-robust-pancancer-classification
status: supported
confidence: 0.9
tags:
  - hypoxia
  - mRNA-signature
  - pancancer
  - TCGA
  - methodology
domain: "oncology / cancer-genomics / hypoxia-quantification"
source_papers:
  - characterization-hypoxia-associated-molecular-features-aid
evidence:
  - source: characterization-hypoxia-associated-molecular-features-aid
    type: supports
    strength: strong
    detail: "In ten independent datasets, cells under hypoxic conditions showed significantly higher 15-gene hypoxia scores than normoxic controls; the score correlated strongly with the Winter and Hu signatures (Fig. 1l). Quote (p.432): 'These results demonstrate the robustness of the 15-gene signature to define hypoxia status in different cancer types.' Protein-level validation (CPTAC) confirmed enrichment in hypoxia score-high BRCA (NES=1.92, FDR<0.001) and OV (NES=2.15, FDR<0.001)."
conditions: "15-gene signature: ACOT7, ADM, ALDOA, CDKN3, ENO1, LDHA, MIF, MRPS17, NDRG1, P4HA1, PGAM1, SLC2A1, TPI1, TUBB6, VEGFA. Hypoxia score computed by GSVA; status assigned by unsupervised hierarchical clustering into high/intermediate/low groups per cancer type. Relative (within-cancer-type) signature, not an absolute O2 readout."
date_proposed: 2026-06-02
date_updated: 2026-06-02
---

## Statement

A compact 15-gene mRNA expression signature reliably separates hypoxic from normoxic samples and ranks tumour hypoxia status across diverse cancer types. Its scores are concordant with independent hypoxia signatures (Winter, Hu) and validated at the protein level by CPTAC mass spectrometry, supporting its use as the classification backbone for pan-cancer hypoxia analyses.

## Evidence summary

- [[papers/characterization-hypoxia-associated-molecular-features-aid]] — ten validation datasets, cross-signature correlation, CPTAC protein-level enrichment.
- The 15-gene signature was shown to be the best performer in a prior comprehensive robustness assessment (Fox et al. 2014, *BMC Bioinformatics*).

## Conditions and scope

- Relative signature: classifies samples *within* a cancer type; absolute hypoxia status is not measured.
- KIRC and COAD samples with VHL mutation ≥5% were excluded to avoid pseudohypoxia confounding.

## Counter-evidence

- Bulk-tissue signature; does not resolve intratumoral hypoxia heterogeneity or stromal/immune contributions.

## Linked ideas

(none yet)

## Open questions

- How well does a relative within-cancer signature transfer to single-cell or spatial resolution?
