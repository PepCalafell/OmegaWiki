---
title: "ERK1/2 — MAPK1 / MAPK3 (extracellular signal-regulated kinases)"
slug: mapk1-3-erk1-2-kinases
domain: kinase / signalling
status: mainstream
aliases:
  - "ERK1/2"
  - "ERK1"
  - "ERK2"
  - "p44/42 MAPK"
  - "MAPK1"
  - "MAPK3"
  - "p-ERK"
  - "phospho-ERK"
  - "Mapk1"
  - "Mapk3"
  - "extracellular signal-regulated kinase"
  - "Ras-Raf-MEK-ERK cascade"
first_introduced: "Boulton 1991; Cobb & Goldsmith reviews"
date_updated: 2026-05-26
source_url: ""
---

## Definition

ERK1 (MAPK3, p44) and ERK2 (MAPK1, p42) are the terminal kinases of the Ras-Raf-MEK-ERK MAP kinase cascade, broadly activated by growth factors, cytokines, and adhesion / receptor engagement. Active phospho-ERK1/2 (Thr202/Tyr204) translocates to the nucleus and phosphorylates ETS-family TFs (Elk-1), RSK kinases, and direct gene targets. In macrophages, AC binding via CD36 activates ERK transiently; sustained activation requires removal of DUSP4 negative feedback for productive downstream gene induction.

## Intuition

ERK is the canonical proliferation/differentiation signal but its duration determines whether downstream programs activate. Transient ERK = no Ptgs2 induction; sustained ERK (after DNMT3A-mediated DUSP4 repression in efferocytosing macrophages) → Ptgs2-PGE2-TGFβ1 induction.

## Formal notation

- Cascade: RTK / GPCR → Ras → Raf → MEK1/2 → ERK1/2
- Activating phosphorylation: Thr202/Tyr204 (TEY motif)
- Pharmacology: MEK inhibitor U0126; trametinib (clinical), selumetinib
- Knockdown: siMapk1 + siMapk3 (combinatorial required due to isoform redundancy)
- Substrates: Elk-1, p90RSK, MNK, MSK, MAP kinase phosphatases (DUSP1/4)
- Negative feedback: DUSP1, DUSP4, DUSP6 phosphatases dephosphorylate ERK

## Variants

- ERK1 vs ERK2: largely redundant; ERK2 dominant in most tissues
- Scaffolds: KSR, paxillin, β-arrestins

## Known limitations

- Pan-MEK inhibitors block both ERK1 and ERK2 — isoform-specific dissection requires genetic KO
- Cytoplasmic vs nuclear ERK functions differ; phospho-Ab specificity variable

## Open problems

- Quantitative duration thresholds for distinct gene programs (transient ERK induces IEGs; sustained ERK induces second-wave genes like Ptgs2)
- Which scaffolds dictate efferocytosis-specific ERK output

## Relevance to active research

Central to [[papers/macrophages-use-apoptotic-cell-derived-methionine]] (Ampomah 2022 *Nat Metab*): U0126 or siMapk1+siMapk3 blocks AC-induced Ptgs2/Tgfb1; CD36 silencing reduces AC-induced p-ERK; DNMT3A-KO macrophages have blunted sustained p-ERK due to failure to repress DUSP4. The pathway makes ERK duration — not magnitude — the rate-limiting variable for downstream resolution gene induction.
