---
title: "SIRPα–CD47 'don't-eat-me' axis"
aliases:
  - "SIRPα CD47 axis"
  - "don't-eat-me signal"
  - "CD47 macrophage checkpoint"
  - "SHPS-1"
  - "SIRPa-CD47 immunotherapy"
  - "macrophage checkpoint inhibition"
  - "calreticulin eat-me signal"
  - "anti-CD47 antibody therapy"
  - "magrolimab CD47"
  - "SIRPα ITIM signaling"
tags:
  - macrophage
  - phagocytosis
  - cancer-immunotherapy
  - immune-checkpoint
  - SIRPa
  - CD47
  - immunology
maturity: active
key_papers:
  - physiology-diseases-tissue-resident-macrophages
first_introduced: "Oldenborg 2000 Science (CD47 don't-eat-me); Jaiswal 2009 Cell (CD47 in cancer); reviewed in Lazarov & Geissmann 2023"
date_updated: 2026-05-06
related_concepts:
  - efferocytosis-anti-inflammatory-clearance
  - tumor-associated-macrophage-immunosuppression
---

## Definition

The SIRPα–CD47 axis is the principal "don't-eat-me" signaling pathway that protects healthy cells from macrophage phagocytosis. Macrophage SIRPα (signal regulatory protein α; also known as SHPS-1) carries an ITIM cytoplasmic motif that, when engaged by CD47 on a target cell, recruits SHP-1/SHP-2 phosphatases and inhibits the phagocytic synapse. Tumour cells exploit this pathway by overexpressing CD47, thereby evading macrophage destruction. Therapeutic targeting of SIRPα or CD47 (anti-CD47 antibodies, SIRPα fusions) releases this brake and is in clinical trials across multiple cancer types.

## Intuition

Macrophages need a way to distinguish "me" from "not-me" — both for limiting auto-immunity and for tolerating self-tissue at homeostasis. CD47 is the universal "self" marker; its engagement of SIRPα on macrophages says "do not phagocytose this cell." Apoptotic cells lose surface CD47 (in addition to flipping PtdSer), shifting the balance toward engulfment. Tumour cells *upregulate* CD47 to mimic healthy self and avoid macrophage attack. Drugs that block this interaction (anti-CD47 antibodies like magrolimab; SIRPα-Fc fusions) are macrophage-checkpoint inhibitors, complementary to T-cell-checkpoint inhibitors (anti-PD-1/PD-L1).

## Formal notation

- **CD47**: 5-pass membrane glycoprotein on virtually all cells; the ligand for SIRPα
- **SIRPα (CD172a, SHPS-1)**: ITIM-bearing receptor on macrophages, neutrophils, dendritic cells
- **Signaling**: SIRPα ITIM phosphorylation → SHP-1 / SHP-2 recruitment → dephosphorylation of phagocytosis-promoting kinases → inhibition of engulfment
- **Counter-signals (eat-me)**: PtdSer (apoptotic cells), calreticulin (stressed cells), antibody-Fc (opsonized cells)
- **Tumour exploitation**: CD47 overexpression in AML, NHL, solid tumours
- **Therapeutics**:
  - Anti-CD47 antibodies: magrolimab (Hu5F9-G4), TTI-621
  - SIRPα-Fc fusions: TTI-621
  - Anti-SIRPα antibodies: also in development
  - Combination with rituximab, anti-PD-1 in trials

## Variants

- *Tumour-cell CD47 upregulation* — the canonical cancer escape mechanism.
- *RBC CD47 protection* — RBCs use CD47 to avoid Kupffer/splenic phagocytosis in steady state; CD47 declines on senescent RBCs to enable clearance.
- *HSC / progenitor CD47* — HSCs upregulate CD47 to survive bone-marrow phagocyte surveillance.
- *Pathogen-derived CD47 mimicry* — some viruses and bacteria express CD47-like molecules to evade phagocytosis.

## Comparison

vs PD-1/PD-L1 axis: PD-1/PD-L1 is the *T-cell-checkpoint* axis; SIRPα-CD47 is the *macrophage-checkpoint* axis. Both protect healthy self and are exploited by tumours. The two are complementary in cancer immunotherapy.
vs efferocytosis: efferocytosis is the active *uptake* programme triggered by eat-me signals; SIRPα-CD47 is the *suppression* programme that prevents uptake of healthy cells. They operate in dynamic tension at the cell surface.

## When to use

- Predicting which tumour types will respond to anti-CD47 therapy (high CD47 + macrophage-rich infiltrate + intact phagocytic machinery).
- Interpreting on-target toxicity of anti-CD47 drugs (anaemia from RBC clearance — managed with priming-dose strategies).
- Designing combinations with opsonizing antibodies (anti-CD20 rituximab + anti-CD47 in B-NHL).

## Known limitations

- On-target anaemia is dose-limiting; engineering of low-affinity-to-RBC variants is active.
- Tumour CD47 overexpression is heterogeneous; not all tumours are vulnerable.
- TAM phagocytic capacity varies by macrophage state; immunosuppressive TAMs may not phagocytose even when CD47 is blocked.
- Magrolimab clinical trials in AML and MDS were halted in 2024 for lack of efficacy / safety concerns — efficacy in liquid tumours remains uncertain.

## Open problems

- Why magrolimab failed in AML/MDS despite strong preclinical signal.
- The role of ADCP (antibody-dependent cellular phagocytosis) augmentation as the primary mechanism of anti-CD47 antibodies.
- Whether anti-SIRPα (rather than anti-CD47) circumvents the on-target anaemia.

## Key papers

- [[papers/physiology-diseases-tissue-resident-macrophages]] — Lazarov & Geissmann 2023 *Nature* — review highlights SIRPα-CD47 as the principal macrophage-checkpoint and a "promising strategy for cancer treatment"

## My understanding

For my hypoxia-NF-κB work this is a *contextual* axis — hypoxic tumours have abundant macrophages and CD47 is hypoxia-regulated (HIF1α is reported to upregulate CD47 in some contexts). Whether hypoxia drives SIRPα-CD47-axis-mediated phagocytosis evasion is an interesting cross-cutting hypothesis. The clinical relevance is high; the mechanism in solid hypoxic tumours could differ from liquid tumours, which may explain heterogeneous trial outcomes.
