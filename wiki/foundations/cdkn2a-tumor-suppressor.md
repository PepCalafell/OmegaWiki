---
title: "CDKN2A (Cyclin-Dependent Kinase Inhibitor 2A; p16INK4a / p14ARF)"
slug: cdkn2a-tumor-suppressor
domain: "molecular-biology / oncology / cell-cycle"
status: mainstream
aliases:
  - "CDKN2A"
  - "p16"
  - "p16INK4a"
  - "p14ARF"
  - "INK4a/ARF"
  - "MTS1"
  - "tumor suppressor at chromosome 9p21.3"
  - "9p21 deletion"
  - "INK4a-ARF locus"
first_introduced: "Serrano, Hannon, Beach 1993 Nature (p16); Quelle et al. 1995 Cell (p14ARF)"
date_updated: 2026-05-06
source_url: "https://www.uniprot.org/uniprot/P42771"
---

## Definition

CDKN2A is a complex tumor-suppressor locus on chromosome 9p21.3 that encodes two functionally distinct proteins via alternative reading frames: p16INK4a (an inhibitor of CDK4/6 → preserves Rb-mediated G1 arrest) and p14ARF (an inhibitor of MDM2 → stabilizes p53). Loss of CDKN2A — most often via homozygous deletion of the 9p21 locus — simultaneously disables both the Rb and p53 tumor-suppressor arms.

## Intuition

CDKN2A loss is a "two-for-one" hit: deleting one locus knocks out both Rb-pathway brake (via p16) and p53-pathway brake (via p14ARF). It is among the most common deletions in human cancer, especially in glioblastoma, melanoma, lymphoma, mesothelioma, and renal clear cell carcinoma. Co-occurrence with hypoxia in renal clear cell carcinoma (KIRC) reflects the pressure to simultaneously escape replicative arrest and apoptosis under metabolic stress.

## Formal notation

- Encoded by CDKN2A (chr9p21.3 in human)
- Two transcripts via alternative first exons:
  - p16INK4a (16 kDa, 156 aa): four ankyrin repeats; binds CDK4/CDK6 catalytic cleft → blocks CCND association
  - p14ARF (14 kDa in human, p19ARF in mouse): binds MDM2 → blocks MDM2 ubiquitination of p53
- Frequent loss via: homozygous deletion (most common), promoter hypermethylation, rare point mutations

## Key variants

- Germline CDKN2A mutations → familial atypical multiple-mole melanoma (FAMMM) syndrome
- Co-deletion with neighboring CDKN2B (p15INK4b) common, since 9p21 deletions span 1–4 Mb

## Known limitations

- Methylation-based silencing is harder to detect than deletion; some "neutral" copy-number calls are functionally null via methylation.
- CDKN2A status is rarely reported separately from p16/p14ARF readouts in clinical studies.

## Open problems

- Whether CDKN2A loss is a *consequence* of hypoxia-driven selection or an independent oncogenic event is unclear; the strong KIRC-specific hypoxia-CDKN2A association in [[papers/molecular-landmarks-tumor-hypoxia-across-cancer]] (Bonferroni p=1.40×10⁻⁹) may reflect VHL-loss / pseudohypoxia in clear-cell biology.

## Relevance to active research

In [[papers/molecular-landmarks-tumor-hypoxia-across-cancer]], CDKN2A loss is the strongest tumor-suppressor co-occurrence with hypoxia in KIRC (Bonferroni p=1.40×10⁻⁹), pancancer-relevant alongside MYC gain.
