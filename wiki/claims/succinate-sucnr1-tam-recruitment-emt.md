---
title: "Tumor-derived succinate engages SUCNR1 on TAMs and tumor cells to drive macrophage recruitment, M2 polarization, and EMT via PI3K-HIF-1α"
slug: succinate-sucnr1-tam-recruitment-emt
status: supported
confidence: 0.75
tags:
  - succinate
  - SUCNR1
  - GPR91
  - TAM
  - oncometabolite
  - macrophage-recruitment
  - M2-polarization
  - EMT
  - HIF-1α
  - PI3K
domain: "oncology / metabolism / immunology"
source_papers:
  - hypoxia-driven-crosstalk-between-tumor-tumor
evidence:
  - source: hypoxia-driven-crosstalk-between-tumor-tumor
    type: supports
    strength: strong
    detail: "Bai 2022 review (DOI 10.1186/s12943-022-01645-2, p.13) summarizes the lung-cancer mechanism: tumor-released succinate engages SUCNR1 on TAMs → PI3K-HIF-1α → TAM recruitment, migration, M2-skewed polarization. M2 TAMs secrete IL-6 → cancer cell migration. Tumor-derived succinate also activates SUCNR1 on tumor cells → PI3K/HIF-1α → cancer cell migration and EMT. Mechanism citation: Wu et al. 2020 Cell Metabolism 31, 267-283 'Succinate-induced neuronal mitochondrial fission and hexokinase II malfunction in ischemic stroke' (extended for lung cancer in subsequent work)."
conditions: "Primary mechanistic evidence in lung cancer (Wu 2020). SDH-deficient paragangliomas / GIST may experience constitutive intracellular succinate accumulation that complicates extracellular SUCNR1 signaling; intracellular vs extracellular routing has different outputs (Tannahill 2013 → IL-1β vs Wu 2020 → M2). Cross-cancer-type validation is limited."
date_proposed: 2026-05-08
date_updated: 2026-05-08
---

## Statement

Tumor-derived extracellular succinate, a TCA-cycle intermediate that accumulates in hypoxic / Warburg-shifted tumor cells, acts as a signaling ligand for the GPCR SUCNR1 (GPR91) on both TAMs and tumor cells. On TAMs, SUCNR1 → PI3K → HIF-1α drives macrophage recruitment, migration, and M2-skewed polarization with IL-6 secretion that promotes cancer cell migration. On tumor cells, the same SUCNR1 → PI3K/HIF-1α axis directly drives migration and EMT. The axis is distinct from the lactate-driven TAM polarization mechanism (which uses HIF-1α and PKA-CREB) and constitutes a parallel oncometabolite-receptor signaling channel that amplifies HIF-1α already stabilized by tumor hypoxia.

## Evidence summary

- [[papers/hypoxia-driven-crosstalk-between-tumor-tumor]] — Bai 2022 *Molecular Cancer* review (p.13) synthesizes the SUCNR1-TAM mechanism in the broader oncometabolite section.
- Primary mechanism: Wu et al. 2020 *Cell Metabolism* (extended for lung cancer-TAM by subsequent work cited in Bai 2022 as [109]).
- Companion: Tannahill et al. 2013 *Nature* on intracellular succinate accumulation driving HIF-1α and IL-1β in inflammatory macrophages — distinct routing but same convergence on HIF-1α.

## Conditions and scope

- Lung cancer is the primary cancer-type evidence.
- SUCNR1 is expressed on multiple cell types (macrophages, dendritic cells, kidney epithelium, retinal cells, platelets, tumor cells); the macrophage and tumor-cell roles are foregrounded here.
- Intracellular vs extracellular succinate routing produces different outputs: intracellular succinate (Tannahill 2013) → IL-1β in inflammatory macrophages; extracellular tumor-derived succinate (Wu 2020) → M2-like polarization in TAMs.
- SDH-deficient paragangliomas / IDH-mutant gliomas have constitutive succinate / 2-HG / fumarate accumulation that may chronically engage similar pathways.

## Counter-evidence

- The Wu 2020 lung-cancer mechanism is the dominant cited evidence; cross-cancer-type validation is limited.
- SUCNR1 antagonists are not yet clinically validated, so loss-of-function in vivo evidence is from genetic models in mice.
- Distinguishing intracellular vs extracellular succinate effects in vivo is technically hard.
- SUCNR1 pharmacology (Gαi vs Gαq coupling) is cell-type-dependent; quantitative downstream attribution is incomplete.

## Linked ideas

(none yet)

## Open questions

- A unified pharmacological model of SUCNR1 antagonism in TAM and tumor cell — does the same antagonist hit both?
- Whether SUCNR1 signaling in TAM converges with the lactate-GPCR axis at common downstream nodes (HIF-1α, mTOR).
- Cross-cancer-type generalization beyond lung cancer.
- Therapeutic exploitation: SUCNR1 antagonist + HIF inhibitor + checkpoint blockade combinations.
