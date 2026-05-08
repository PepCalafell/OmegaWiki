---
title: "PT2385 — first-in-class clinical HIF-2α small-molecule antagonist"
slug: pt2385-hif2a-inhibitor
domain: "oncology / drug-discovery / hypoxia-therapeutics"
status: mainstream
aliases:
  - "PT2385"
  - "first-in-class HIF-2α antagonist"
  - "PT-2385"
  - "Peloton HIF-2α inhibitor"
  - "ccRCC HIF-2α inhibitor PT2385"
  - "recurrent GBM HIF inhibitor"
  - "PT2385 sorafenib combination"
first_introduced: "Chen et al. 2016 Nature (PT2385 discovery and ccRCC efficacy); Courtney et al. 2017 Clin Cancer Res (phase 1)"
date_updated: 2026-05-08
source_url: "https://clinicaltrials.gov/ct2/show/NCT02293980"
---

## Definition

PT2385 is a small-molecule allosteric antagonist of HIF-2α (EPAS1), binding the PAS-B internal pocket and blocking HIF-2α / ARNT (HIF-1β) heterodimerization. It was the first HIF-2α antagonist to enter clinical trials and the precursor of the clinically approved Belzutifan (PT2977 / MK-6482). PT2385 is selective for HIF-2α over HIF-1α and has been tested in clear cell renal cell carcinoma (ccRCC) and recurrent glioblastoma multiforme (GBM) in phase 1-2 trials. It can mitigate the adverse effects of sorafenib (TKI) by blocking HIF-2α, increasing androgen receptor (AR), and suppressing downstream pSTAT3 / pAKT / pERK pathways.

## Intuition

PT2385 was the proof-of-concept that the HIF-2α PAS-B pocket — a protein-protein interaction interface — is druggable with a small molecule. Despite the high sequence identity between HIF-1α and HIF-2α PAS-B domains, PT2385 is highly selective for HIF-2α/ARNT dissociation with no measurable activity against HIF-1. The clinical success of PT2385 in ccRCC translated into the chemically improved Belzutifan, which became the FDA-approved member of the class.

## Formal notation

Mechanism:
- PAS-B pocket allosteric inhibitor.
- Binds HIF-2α → conformational change → blocks ARNT dimerization → no HRE binding → target gene transcription suppressed.

Trial program (per Bai 2022 and ClinicalTrials.gov):
- NCT02293980 — phase 1 in advanced ccRCC.
- NCT03108066 — phase 2 in VHL-disease-associated ccRCC.
- NCT04989959 — phase 1 in renal cell carcinoma.
- NCT03216499 — phase 2 in recurrent glioblastoma.

Combination directions:
- PT2385 + sorafenib: PT2385 reduces sorafenib adverse effects via AR upregulation and pSTAT3/pAKT/pERK suppression.

## Key variants

- *PT2385 vs Belzutifan (PT2977 / MK-6482)*: same mechanism; Belzutifan has improved PK and became the FDA-approved successor.
- *Other PAS-B HIF-2α inhibitors*: DFF332 (NCT04895748), NKT2152 (NCT05119335), all in phase I.

## Known limitations

- HIF-2α-selective: tumors driven by HIF-1α are not addressed.
- Anemia is a class side effect (HIF-2α drives EPO).
- Clinical durability variable; resistance mechanisms emerging.
- Largely superseded by Belzutifan in clinical use.

## Open problems

- Whether PT2385 has a niche in HIF-2α-driven non-ccRCC tumors (recurrent GBM trial outcome will inform).
- Mechanistic basis for PT2385's effect on AR / pSTAT3 / pAKT / pERK in the context of sorafenib combination — direct off-target or downstream of HIF-2α blockade?
- Predictive biomarker beyond VHL mutation.

## Relevance to active research

PT2385 is the clinical proof-of-concept paper for HIF-2α inhibition. In [[papers/hypoxia-driven-crosstalk-between-tumor-tumor]] (Bai 2022), it is highlighted as the first-in-class drug that opened the path to Belzutifan. For my hypoxia-NF-κB work, PT2385 (like Belzutifan) is a useful tool compound for selectively blocking HIF-2α function in cell-culture or animal models without affecting HIF-1α-dominant macrophage hypoxic responses.
