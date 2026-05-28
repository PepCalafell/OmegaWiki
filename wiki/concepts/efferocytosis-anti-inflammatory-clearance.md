---
title: "Efferocytosis — apoptotic cell clearance with anti-inflammatory output"
aliases:
  - "efferocytosis"
  - "apoptotic cell clearance"
  - "PtdSer recognition"
  - "TIM4 efferocytosis"
  - "MERTK efferocytosis"
  - "TAM receptor signaling"
  - "MFGE8 GAS6 protein S bridging"
  - "anti-inflammatory phagocytosis"
  - "find-me eat-me signaling"
  - "engulfment of dying cells"
tags:
  - macrophage
  - phagocytosis
  - apoptotic-clearance
  - tissue-homeostasis
  - immunology
maturity: stable
key_papers:
  - physiology-diseases-tissue-resident-macrophages
  - metabolism-tissue-macrophages-homeostasis-pathology
  - macrophages-use-apoptotic-cell-derived-methionine
  - transition-monocyte-tissue-resident-macrophage-requires
first_introduced: "deCathelineau & Henson 2003 (term efferocytosis); reviewed in Lazarov & Geissmann 2023"
date_updated: 2026-05-06
related_concepts:
  - macrophage-ontogeny-resident-vs-monocyte-derived
  - sirpa-cd47-don-t-eat-me-axis
---

## Definition

Efferocytosis is the recognition, engulfment, and lysosomal degradation of apoptotic cells by phagocytes — primarily macrophages — accompanied by an anti-inflammatory cytokine output (TGFβ, IL-10, PGE2) and active suppression of pro-inflammatory cytokine production (TNF, IL-1β, IL-6). The process recycles ~10¹¹ apoptotic cells per day in mammalian tissues without triggering inflammation, and its failure causes prolonged collateral tissue damage, autoimmunity, and chronic inflammation.

## Intuition

Apoptotic cells display "eat-me" signals — primarily phosphatidylserine (PtdSer) flipped from inner to outer leaflet — that macrophages recognize directly (TIM4) or via soluble bridging molecules (MFGE8, GAS6, protein S, complement C1Q) that link PtdSer to receptors on the phagocyte (TAM family TYRO3/AXL/MERTK; integrins αVβ3/αVβ5; complement receptors). Engagement triggers engulfment + lysosomal digestion + a *programmed* switch to anti-inflammatory output, distinguishing efferocytosis from inflammatory phagocytosis of pathogens.

## Formal notation

- **Eat-me signals**: PtdSer (universal), calreticulin (in stress)
- **Direct receptors**: TIM4 (PtdSer-binding immunoglobulin-domain), Stabilin-2, BAI1
- **Bridging-ligand receptors** (TAM family + integrins):
  - MERTK (with GAS6 / protein S bridging)
  - TYRO3 (with GAS6 / protein S)
  - AXL (with GAS6)
  - Integrin αVβ3 (with MFGE8)
- **Complement-bridged**: C1Q binds dying cells; complement receptors recognize C1Q-tagged corpses
- **Output cytokines (programmed anti-inflammatory)**: TGFβ, IL-10, PGE2
- **Suppressed cytokines**: TNF, IL-1β, IL-6, type-I IFNs

## Variants

- *Tissue-resident efferocytosis* — TRMs continuously clear physiological apoptosis (e.g. Kupffer cells clear senescent erythrocytes; tingible-body macrophages in germinal centers clear apoptotic B cells).
- *Monocyte-derived efferocytosis* — recruited macrophages clear bulk debris during injury and infection.
- *Calreticulin-driven cell-of-stress engulfment* — programmed cell removal of unfit but not yet apoptotic cells (overlaps with cancer SIRPα-CD47 axis).

## Comparison

vs phagocytosis of pathogens: pathogen phagocytosis (via PRRs/PAMPs) is *pro-inflammatory* and drives TNF/IL-1/IFN. Efferocytosis is *anti-inflammatory*. The same macrophage can do both, with the receptor engaged dictating the cytokine outcome.
vs SIRPα-CD47 axis: SIRPα-CD47 protects *living, healthy* cells from any phagocytosis (a "don't-eat-me" signal). Efferocytosis is the opposite — actively recognizing cells that have lost CD47-like protection and gained PtdSer.

## When to use

- Diagnosing accumulation of apoptotic debris in tissues with autoimmune phenotypes (lupus, glomerulonephritis).
- Designing therapies for cancer (target SIRPα-CD47 to release efferocytic restraint on tumour cells) or for autoimmunity (boost efferocytosis to clear immunogenic debris).
- Interpreting why MERTK/MFGE8/TIM4/C1Q knockouts develop SLE-like phenotypes.

## Known limitations

- Receptor redundancy makes single-knockout phenotypes incomplete.
- The respective contributions of TRMs vs monocyte-derived macrophages to physiological vs pathological efferocytosis are unclear.
- TAM-family signaling overlaps with platelet biology (GAS6/protein S also act on platelets); macrophage-restricted KOs are needed.

## Open problems

- Quantitative thresholds — how much defective efferocytosis triggers autoimmunity?
- Whether efferocytosis-engaged macrophages acquire a long-term anti-inflammatory programme or merely a transient state.
- Reconciling efferocytosis with tumour immune evasion — TAMs that efferocytose may be selectively immunosuppressive in cancer.

## Key papers

- [[papers/physiology-diseases-tissue-resident-macrophages]] — Lazarov & Geissmann 2023 *Nature* — review section "Phagocytosis and nutrient recycling" covers TIM4/TAM/bridging-ligand efferocytosis machinery and the anti-inflammatory output programme
- [[papers/macrophages-use-apoptotic-cell-derived-methionine]] — Ampomah 2022 *Nat Metab* — mechanism of efferocytosis-driven COX2/PGE2/TGFβ1 resolution via AC-methionine → SAM → DNMT3A → Dusp4 promoter methylation → sustained ERK

## My understanding

For my hypoxia-NF-κB work: hypoxia-driven NF-κB activation in macrophages would be expected to *bias against* the anti-inflammatory efferocytic output programme (since NF-κB drives pro-inflammatory cytokines that efferocytosis normally suppresses). Whether hypoxic mMAC1 macrophages have impaired efferocytosis is a testable hypothesis worth flagging — if true, it would explain part of the chronic-inflammation phenotype in hypoxic tissues.
