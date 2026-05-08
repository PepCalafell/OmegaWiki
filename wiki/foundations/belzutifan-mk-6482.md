---
title: "Belzutifan (MK-6482, Welireg) — first FDA-approved HIF-2α small-molecule inhibitor"
slug: belzutifan-mk-6482
domain: "oncology / drug-discovery / hypoxia-therapeutics"
status: mainstream
aliases:
  - "Belzutifan"
  - "MK-6482"
  - "Welireg"
  - "PT2977"
  - "HIF-2α inhibitor Belzutifan"
  - "first FDA-approved HIF inhibitor"
  - "VHL disease drug Belzutifan"
  - "Merck HIF-2α antagonist"
  - "PAS-B-pocket HIF-2α inhibitor"
  - "ccRCC HIF inhibitor"
first_introduced: "Wehn et al. 2018 J Med Chem (PT2977/MK-6482 medicinal chemistry); Jonasch et al. 2021 NEJM (phase 2 VHL trial); FDA approval 13 Aug 2021"
date_updated: 2026-05-08
source_url: "https://www.fda.gov/drugs/resources-information-approved-drugs/fda-approves-belzutifan-cancers-associated-von-hippel-lindau-disease"
---

## Definition

Belzutifan (Merck trade name Welireg; development codes MK-6482 / PT2977) is a small-molecule allosteric inhibitor of HIF-2α (EPAS1), binding the PAS-B internal hydrophilic pocket and disrupting HIF-2α / ARNT (HIF-1β) heterodimerization. It is the first HIF inhibitor to receive FDA approval (13 August 2021), indicated for adult patients with Von Hippel-Lindau (VHL) disease who require therapy for VHL-disease-associated renal cell carcinoma (RCC), CNS hemangioblastoma, or pancreatic neuroendocrine tumors (pNET) and do not require immediate surgery. Belzutifan is selective for HIF-2α over HIF-1α — both isoforms share PAS-B sequence identity but the PAS-B pocket is uniquely druggable in HIF-2α — so off-target HIF-1α-axis effects are minimal.

## Intuition

VHL-disease patients carry a germline VHL mutation, lose the second VHL allele somatically in tumors, and end up with constitutively stabilized HIF-2α driving multi-organ tumorigenesis. Until 2021, the only treatments were surgical or local-ablation; systemic options were limited. Belzutifan provides the first systemic option that targets the actual molecular cause: it locks HIF-2α in a dimerization-incompetent conformation, blocking transcription of HIF-2α target genes (VEGF, EPO, GLUT1 etc.) that drive tumor growth. The drug is oral, daily-dosed, and reasonably well-tolerated, with anemia as the dominant on-target side effect (HIF-2α drives erythropoiesis).

## Formal notation

Drug properties:
- IUPAC: 3-[(1S,2S,3R)-2,3-difluoro-1-hydroxy-7-methylsulfonyl-2,3-dihydro-1H-inden-4-yl]oxy-5-fluorobenzonitrile
- Molecular formula: C₁₇H₁₂F₃NO₄S; MW 383.3 g/mol.
- Route: oral.
- Approved dose: 120 mg once daily.

Mechanism:
- Binds the HIF-2α PAS-B internal hydrophilic cavity (~290 Å³).
- Allosterically prevents HIF-2α / ARNT dimerization.
- HIF-2α HRE-binding lost → target gene transcription suppressed.
- Selective for HIF-2α over HIF-1α despite their PAS-B sequence similarity.

Indications:
- VHL-disease-associated RCC, CNS hemangioblastoma, pNET (FDA approved 2021).
- Sporadic ccRCC (post-checkpoint / TKI failure; clinical investigation).
- Pacak-Zhuang syndrome (somatic-mosaic activating EPAS1 mutation; per Bai 2022, candidate).
- Pheochromocytoma / paraganglioma (NCT04924075 phase II).

Combination trials (per Bai 2022):
- Belzutifan + pembrolizumab (NCT04976634)
- Belzutifan + Lenvatinib (NCT05239728)
- Belzutifan + cabozantinib (NCT03634540, NCT04736706)
- NCT05030506, NCT04626518, NCT04586231, NCT04626479

Pivotal evidence:
- Jonasch et al. NEJM 2021: open-label phase 2 in VHL-RCC (n=61); ORR 49%, durable responses, manageable safety.

## Key variants

- *Belzutifan vs PT2385*: PT2385 was the first-in-class clinical candidate; Belzutifan (PT2977) has improved PK and is the FDA-approved successor.
- *Belzutifan vs DFF332 / NKT2152*: similar mechanism (PAS-B pocket); next-generation candidates in early-phase trials.

## Known limitations

- HIF-2α-selective: tumors driven by HIF-1α are not addressed.
- Anemia is the dominant adverse event (≥hemoglobin <10 g/dL in ~75% of trial patients) — must be managed.
- Hypoxia (decreased O₂ saturation) and fatigue are common.
- Real-world durability beyond 2-3 years in VHL patients (lifelong therapy) is being established.
- Sporadic ccRCC results have been variable; predictive biomarkers beyond VHL mutation are needed.
- Pulmonary hypertension and metabolic effects observed in HIF-2α-loss-of-function animal models — clinical relevance debated.

## Open problems

- Predictive biomarker for response in sporadic ccRCC and other tumors beyond VHL status alone.
- Optimal combination partner: pembrolizumab vs Lenvatinib vs cabozantinib (head-to-head trials needed).
- Long-term safety in young VHL patients on lifelong therapy.
- Resistance mechanisms (HIF-1α bypass, NRF2 upregulation, etc.) and second-line strategies.

## Relevance to active research

Belzutifan is the proof-of-concept that the HIF axis is clinically tractable. In [[papers/hypoxia-driven-crosstalk-between-tumor-tumor]] (Bai 2022), it anchors the section on HIF-2α small-molecule inhibitors as the first FDA-approved HIF inhibitor and the platform for future combinations with checkpoint blockade and TKIs. For my hypoxia-NF-κB-macrophage work, Belzutifan is a useful counterfactual: it tells us what happens when HIF-2α function is blocked in tumor cells, but does NOT block HIF-1α (the dominant α-isoform in macrophages) — so its TAM-side effects are limited to HIF-2α-dependent TAM features (e.g. Spint1 secretion).
