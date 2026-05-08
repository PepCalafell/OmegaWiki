---
title: "Sema3A captures TAMs in hypoxic niches via NRP1-followed-by-PlexinA1/A4 stop signaling"
slug: sema3a-nrp1-plexina-stop-signal-tam-hypoxic-niche
status: supported
confidence: 0.7
tags:
  - Sema3A
  - NRP1
  - PlexinA1
  - PlexinA4
  - TAM
  - hypoxic-niche
  - macrophage-recruitment
  - tumor-microenvironment
domain: "oncology / immunology / hypoxia"
source_papers:
  - hypoxia-driven-crosstalk-between-tumor-tumor
evidence:
  - source: hypoxia-driven-crosstalk-between-tumor-tumor
    type: supports
    strength: moderate
    detail: "Bai 2022 review (DOI 10.1186/s12943-022-01645-2, p.11) summarizes the mechanism citing the underlying primary work (Casazza 2013 Cancer Cell): Sema3A is hypoxia-induced in tumor cells; its expression is higher in hypoxic vs normoxic single-cell tumor suspensions; it engages NRP1 on circulating macrophages; once macrophages reach the hypoxic environment, NRP1 is downregulated, and Sema3A captures TAMs locally via NRP1-independent PlexinA1/A4-mediated stop signals; Sema3A-absent tumors show M1-like phenotype TAMs and reduced tumor growth."
conditions: "Demonstrated in Lewis lung carcinoma model. Cervical cancer also shows hypoxia-induced NRP1 upregulation in tumor cells with similar TAM-recruitment effect via a different (NRP1 on tumor) angle. Cross-cancer validation is limited; primary evidence base is Casazza 2013 with Bai 2022 as the synthesizing review."
date_proposed: 2026-05-08
date_updated: 2026-05-08
---

## Statement

Sema3A (Semaphorin 3A), a hypoxia-induced membrane-bound protein on tumor cells, drives circulating macrophages into hypoxic tumor niches via the Sema3A-NRP1 axis. Once macrophages reach the hypoxic core, NRP1 is downregulated; Sema3A then captures the TAMs locally through a NRP1-independent PlexinA1-PlexinA4 stop-signaling mechanism. Sema3A loss yields a more M1-like TAM phenotype and reduced tumor growth, consistent with Sema3A's role in retaining TAMs in the immunosuppressive hypoxic niche.

## Evidence summary

- [[papers/hypoxia-driven-crosstalk-between-tumor-tumor]] — Bai 2022 *Molecular Cancer* review (p.11) synthesizes the Sema3A-NRP1-PlexinA mechanism in the TAM-recruitment-and-retention model.
- Primary mechanism: Casazza et al. 2013 *Cancer Cell* "Impeding macrophage entry into hypoxic tumor areas by Sema3A/Nrp1 signaling blockade inhibits angiogenesis and restores antitumor immunity" — the canonical demonstration in Lewis lung carcinoma model.

## Conditions and scope

- Demonstrated in Lewis lung carcinoma; replicated in cervical cancer with the receptor-side variation (hypoxia-induced NRP1 on tumor cells, not Sema3A on tumor cells).
- The two-step model (NRP1-mediated attraction → NRP1-downregulation → PlexinA1/A4 stop-signal) is mechanistically appealing but rests on a limited primary evidence base.
- Therapeutic interpretation: NRP1 antagonism may release TAMs from hypoxic-niche capture; however, NRP1 also acts in VEGFR2-co-receptor mode, so selectivity is needed.

## Counter-evidence

- The Sema3A-PlexinA stop-signal model is largely from one primary paper (Casazza 2013) plus the Bai 2022 review synthesis; broader replication is limited.
- TAM mobility in vivo is hard to measure; "stop signal" claims are inferred from spatial distribution rather than direct motility imaging.
- Other recruitment-and-retention mechanisms (lactate-driven motility reduction, hypoxia-induced VLA-4 / integrin changes) may co-explain the spatial distribution and have not been disentangled.

## Linked ideas

(none yet)

## Open questions

- Is the Sema3A-NRP1-PlexinA mechanism cancer-type-specific or generalizable across solid tumors?
- What is the role of NRP1 downregulation in hypoxic TAMs — is it stochastic, ligand-dependent, or transcriptionally programmed?
- Therapeutic value of NRP1 antagonism: blocks the Sema3A-mediated stop signal but may also affect VEGF signaling; selectivity strategies needed.
- Which MoMac-VERSE / Casanova-Acebes TAM cluster is the canonical "hypoxic-niche-captured" subset?
