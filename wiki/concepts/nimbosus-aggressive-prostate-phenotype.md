---
title: "Nimbosus — aggressive cellular phenotype in localized prostate cancer"
aliases:
  - "nimbosus"
  - "nimbus aggressive phenotype"
  - "stormy clouds prostate phenotype"
  - "hypoxia-PTEN-IDC-CA constellation"
  - "hypoxic IDC-CA PTEN-deleted phenotype"
  - "aggressive PCa molecular constellation"
  - "Bhandari nimbosus"
  - "Chua nimbosus"
  - "PCa aggressive phenotype constellation"
tags:
  - prostate-cancer
  - hypoxia
  - PTEN
  - TP53
  - IDC-CA
  - chromothripsis
  - telomere
  - aggressive-phenotype
  - prognostic
maturity: emerging
key_papers:
  - molecular-landmarks-tumor-hypoxia-across-cancer
first_introduced: "Chua, van der Kwast, Bristow et al. 2017 Eur Urol; consolidated by Bhandari et al. 2019 Nat Genet"
date_updated: 2026-05-06
related_concepts: []
---

## Definition

Nimbosus (Latin: "gathering of stormy clouds") is the name proposed for a constellation of co-occurring molecular and pathological features in localized prostate cancer that together define an aggressive cellular phenotype. The defining features are: (1) elevated tumor hypoxia, (2) allelic loss of PTEN, (3) mutant TP53, (4) chromothripsis, (5) shorter telomeres, and (6) intraductal/cribriform carcinoma (IDC-CA) histopathology. Subjects whose tumors carry the full constellation (hypoxia + IDC-CA + PTEN deletion) have hazard ratio 11.10 (95% CI 3.02–47.27, P=3.15×10⁻⁵) for poor 5-year biochemical relapse-free outcome — substantially worse than any single component.

## Intuition

The nimbosus framing reframes prostate cancer aggressiveness from "a list of independent risk factors" to "a *coherent* molecular state shaped by hypoxia-driven evolutionary selection." Hypoxia exerts the early selective pressure (99% of hypoxia-associated CNAs in trunk timing); surviving subclones are those that escape apoptosis (mutant TP53), tolerate replication stress (PTEN loss → AKT hyperactivation), and maintain telomeres (TERT induction). When this state is reached, all six features tend to co-occur — like multiple weather features that together signal a storm system rather than independent variables.

## Formal notation

- Pillars (each independently prognostic, jointly multiplicatively prognostic):
  - Hypoxia: continuous, mRNA Buffa signature (or ensemble)
  - PTEN: allelic loss / deep deletion
  - TP53: missense/nonsense SNV
  - Chromothripsis: structural-variant call
  - Telomere length: TelSeq-estimated
  - IDC-CA: pathologist-assessed, includes intraductal carcinoma and cribriform architecture
- Joint hazard model: hypoxia × IDC-CA × PTEN-loss vs all others, HR=11.10 (P=3.15×10⁻⁵)

## Variants

- Original concept introduced by Chua, van der Kwast, Bristow et al. (2017) Eur Urol focused on intraductal/cribriform carcinoma
- Extended by Bhandari et al. (2019) [[papers/molecular-landmarks-tumor-hypoxia-across-cancer]] to include hypoxia, PTEN, TP53, chromothripsis, telomeres
- Polyclonal vs monoclonal architecture: nimbosus features more pronounced in polyclonal tumors

## Comparison

| Risk-stratification approach | Components | HR for biochemical relapse |
|---|---|---|
| Gleason score alone | histology | ~2–3 (advanced grades) |
| CAPRA score | clinical + biopsy | ~2–4 |
| Nimbosus (hypoxia + IDC-CA + PTEN loss) | molecular + histology | ~11 |

## When to use

- Risk-stratification of localized PCa post-prostatectomy
- Selection of high-risk subjects for hypoxia-targeting therapy trials
- Mechanistic studies on hypoxia-driven tumor evolution
- Hypothesis generation for molecular-pathology integration

## Known limitations

- Defined empirically from CPC-GENE / TCGA cohorts; prospective trial validation pending
- "Nimbosus" is a clinicomolecular *correlate*, not a mechanistic category — directly testing whether the constellation is causally connected requires longitudinal patient-derived models
- IDC-CA call quality depends on pathologist training; not universally available
- TP53 status in localized PCa is often subclonal and missed by bulk WGS

## Open problems

- Does treating hypoxia (e.g., evofosfamide) prevent nimbosus emergence?
- Are there tumor types beyond PCa where an analogous "constellation" exists?
- Does the immune microenvironment modulate nimbosus emergence (cf. [[papers/nf-kb-tet2-promote-macrophage-reprogramming]] hypoxic-MAC infiltration)?
- Can a single molecular biomarker capture the full nimbosus state?

## Key papers

- [[papers/molecular-landmarks-tumor-hypoxia-across-cancer]] — full nimbosus consolidation across CPC-GENE + TCGA, HR=11.10

## My understanding

Nimbosus is the cleanest statement to date that aggressive localized PCa has a *recurrent molecular grammar*, not just a list of independent risk factors. For HypoxiaVERSE, this provides the clinical anchor: hypoxia is not an incidental feature of bad PCa, it is one of the early shaping forces. The next question worth pursuing is whether the immune microenvironment of nimbosus tumors is also stereotyped — and if so, whether hypoxic-macrophage signatures (mMAC1, IL4I1) co-occur with nimbosus.
