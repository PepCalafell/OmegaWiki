---
title: "AHR-HIF crosstalk through shared ARNT — hypoxia-driven competition that titrates AHR transcriptional activity"
aliases:
  - AHR-HIF ARNT competition
  - AHR HIF1α competition
  - AHR HIF2α competition
  - ARNT competition hypoxia
  - bHLH-PAS partner competition
  - hypoxia modulation of AHR
  - AHR under hypoxia
  - AHR EPAS1 competition
  - cobalt chloride AHR
  - DMOG AHR
tags:
  - AHR
  - HIF1A
  - HIF2A
  - ARNT
  - hypoxia
  - tumor-microenvironment
  - bHLH-PAS
  - transcription-factor-competition
maturity: stable
key_papers:
  - complex-biology-aryl-hydrocarbon-receptor-activation
  - aryl-hydrocarbon-receptor-rehabilitated-target-therapeutic
first_introduced: ""
date_updated: 2026-05-26
related_concepts:
  - ahr-context-specificity-pleiotropy
  - ahr-arnt-paralogs-and-isoforms
  - ahr-canonical-signalling-pathway
---

## Definition

AHR, HIF1α, and HIF2α (EPAS1) all heterodimerise with the shared partner ARNT/HIF1β. Under hypoxia, HIFα stabilisation depletes the free ARNT pool, reducing AHR-XRE transcription. The competition is bidirectional in principle: hypoxia mimetics (CoCl₂, DMOG) modulate ARNT abundance and AHR activity in a cell-line-specific way.

## Intuition

In the hypoxic tumour core, even ligand-bound AHR cannot transcribe its targets if ARNT is sequestered by HIF1α/HIF2α. AHR phenotypes should therefore differ between tumour core (hypoxic, HIF-dominant) and periphery (normoxic, AHR-dominant).

## Formal notation

[ARNT-AHR]_active ∝ [ARNT_free] × [AHR-ligand], where [ARNT_free] = [ARNT_total] − ([ARNT-HIF1α] + [ARNT-HIF2α] + [ARNT-AHRR] + [ARNT2-AHR]).

## Variants

- HIF1α-dominant hypoxia vs HIF2α-dominant pseudohypoxia (VHL-loss) — both consume ARNT but via different transcriptional programs.
- ARNT2-dominant tissues (kidney/CNS) may relieve this competition somewhat ([[concepts/ahr-arnt-paralogs-and-isoforms]]).

## Comparison

- Versus AHRR competition: AHRR also competes for ARNT and adds chromatin co-repressor recruitment.
- Versus PHD-driven HIFα stabilisation logic: this is downstream — once HIFα is stable, it titrates ARNT.

## When to use

- Direct relevance to my thesis hypoxia work: predicting spatial AHR phenotypes from oxygen gradients.
- When interpreting why AHR-driven phenotypes fail to manifest in deeply hypoxic tumour regions despite high Kyn/AHR activation in adjacent normoxic regions.

## Known limitations

- Quantitative model of ARNT competition is missing.
- ARNT-replenishment dynamics under acute vs chronic hypoxia not mapped.

## Open problems

- Spatial transcriptomics integrating hypoxia signatures with AHR-target expression to test the competition model in human tumours.
- ARNT over-expression as a rescue strategy in hypoxic tumours where AHR-driven anti-cancer functions might be desirable.

## Key papers

- [[papers/complex-biology-aryl-hydrocarbon-receptor-activation]] — Opitz et al. 2023.
- [[papers/aryl-hydrocarbon-receptor-rehabilitated-target-therapeutic]] — Polonio/Quintana 2025.

## My understanding

A direct intersection of AHR biology and my hypoxia work. The competition logic predicts cleanly testable spatial patterns in tumour scRNA-seq + spatial atlases — likely a useful integrative analysis to add to the hypoxia/skin work.
