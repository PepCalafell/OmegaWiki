---
title: "KDM6A and KDM5A histone demethylases are direct oxygen sensors regulating cell fate independent of HIF"
slug: kdm6a-kdm5a-direct-oxygen-sensors
status: supported
confidence: 0.85
tags:
  - KDM6A
  - KDM5A
  - histone-demethylase
  - oxygen-sensor
  - chromatin
  - epigenetics
  - hypoxia
  - HIF-independent
  - H3K27me3
  - H3K4me3
domain: "molecular-biology / chromatin / hypoxia"
source_papers:
  - hypoxia-driven-crosstalk-between-tumor-tumor
evidence:
  - source: hypoxia-driven-crosstalk-between-tumor-tumor
    type: supports
    strength: strong
    detail: "Bai 2022 (DOI 10.1186/s12943-022-01645-2, p.4) synthesizes the 2019 Chakraborty Science discovery: KDM6A and KDM5A are JmjC-domain α-KG-dependent dioxygenases that require Fe(II), 2-OG, and O₂ for catalysis. Their KM for O₂ is in the physiological pO₂ range, so they lose activity under hypoxia. Hypoxic inactivation of KDM6A → persistent H3K27me3 → blocked cellular differentiation; KDM5A → persistent H3K4me3 → altered transcriptional readiness. Mechanism is independent of the HIF / PHD / VHL / FIH axis."
conditions: "Demonstrated in Drosophila, mouse, and human cell lines for cell-fate / differentiation systems. Cancer-cell evidence is more limited but accumulating. The KDM-axis O₂ sensor is parallel to (not redundant with) the HIF-axis sensor — they may act on different timescales (HIF fast, KDM slower / chromatin-level)."
date_proposed: 2026-05-08
date_updated: 2026-05-08
---

## Statement

Beyond the canonical HIF-PHD-VHL axis, certain JmjC-domain α-ketoglutarate-dependent histone demethylases — exemplified by KDM6A (H3K27me3 demethylase) and KDM5A (H3K4me3 demethylase) — directly sense cellular oxygen. Their catalytic activity requires O₂ at concentrations in the physiological pO₂ range, so under hypoxia they lose activity, and the chromatin marks they would have removed (H3K27me3 / H3K4me3) accumulate, altering gene expression and cell-fate decisions independently of the HIF transcription factor. The KDM oxygen-sensing layer expands the cellular hypoxia response from a transcriptional-only model to a transcriptional-plus-epigenetic model.

## Evidence summary

- [[papers/hypoxia-driven-crosstalk-between-tumor-tumor]] — Bai 2022 *Molecular Cancer* review section "Oxygen sensing mechanisms" foregrounds KDM6A/KDM5A as direct O₂ sensors, citing Chakraborty 2019 *Science* and Gallipoli & Huntly 2019 *Science* perspective.
- Primary discovery: Chakraborty et al. 2019 *Science* 363:6432, 1217-1222 "Histone demethylase KDM6A directly senses oxygen to control chromatin and cell fate."
- Companion: Batie et al. 2019 *Science* 363:6432, 1222-1226 "Hypoxia induces rapid changes to histone methylation and reprograms chromatin."
- Perspective: Gallipoli & Huntly 2019 *Science* 363:6432, 1148-1149 "Histone modifiers are oxygen sensors."

## Conditions and scope

- Demonstrated in cell-fate / differentiation contexts (T-cell differentiation, ES cell differentiation).
- KMs for O₂ vary across the JmjC family; not all demethylases will be substrate-limited at the same pO₂.
- The KDM-axis output (chromatin-level changes) is slower than the HIF-axis output (transcriptional changes within hours).
- KDM-specific inhibitors (GSK-J4 for KDM6A) can pharmacologically mimic hypoxic inactivation in normoxia, providing tool compounds for dissecting the axis.

## Counter-evidence

- Some JmjC demethylases are themselves HIF target genes (KDM3A, KDM4B, KDM6B), creating cross-talk and partially confounding clean "HIF-independent" interpretation.
- Quantitative dominance: in many hypoxic transcriptomic responses, HIF target genes account for the bulk of variance; KDM-axis-specific effects need careful experimental isolation.
- Long-term replication and cancer-specific validation are still accumulating since 2019.

## Linked ideas

(none yet)

## Open questions

- A complete map of which JmjC demethylases are O₂-substrate-limited at physiological tumor hypoxia (pO₂ < 10 mmHg) — KMs vary across the family.
- Whether KDM oxygen sensing dominates or merely modulates the HIF transcriptional response in hypoxic cancer cells in vivo.
- Therapeutic exploitation: KDM inhibitors as hypoxia-mimetic compounds, or KDM activators as anti-hypoxia compounds.
- Cross-talk with the metabolic state: 2-OG and succinate are competing co-substrates / inhibitors of KDMs.
- In hypoxic macrophages: does KDM6A inactivation drive the H3K27me3 program in parallel with TET2-mediated DNA demethylation, creating an unusual chromatin state with high accessibility plus retained polycomb mark?
