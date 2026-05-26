---
title: "Tissue-specific TAM function — context-dependent paradigm"
aliases:
  - "context-dependent TAM function"
  - "organ-specific TAM"
  - "TAM tissue-context dependence"
tags:
  - TAM
  - tissue-specific
  - macrophage
  - tumor-microenvironment
  - paradigm
  - functional-reversal
maturity: emerging
key_papers:
  - trem2-macrophages-associated-enhanced-response-pd
  - nf-kb-tet2-promote-macrophage-reprogramming
first_introduced: "Recurring observation; sharply formalised by Hamon et al. 2025 for TREM2 mac (HCC vs NSCLC)"
date_updated: 2026-05-26
related_concepts:
  - trem2-tumor-associated-macrophage
  - folr2-tissue-resident-macrophage
  - hepatic-trem2-protective-tam-program
  - mmac1-hypoxic-inflammatory-macrophage
---

## Definition

The principle that a TAM transcriptional state with a conserved core gene program can produce opposite immunological output (immunosuppressive vs protective / immunostimulatory) in different tissue contexts, mediated by tissue-specific genes layered on top of the core. Established for TREM2 macs (HCC protective vs NSCLC immunosuppressive; Hamon 2025) and FOLR2 macs (HCC non-responder-associated vs breast-cancer favourable).

## Intuition

The same "cluster name" in a pan-cancer scRNA-seq atlas does not guarantee the same biology. TAM functional output is partly transcriptional core + partly tissue-context overlay. For ICB-response biomarkers, this means signatures must be validated tissue-by-tissue, and translation strategies (e.g., anti-TREM2 antibodies) must be reasoned about per organ context.

## Formal notation

- Core program (conserved across tissues): pan-cancer transcriptional signature
- Tissue-specific overlay: organ-derived homeostatic cues + chronic-inflammation context
- Net functional output = core × overlay × activation context

## Variants

- TREM2 TAM: HCC protective (MT1G/H, CALR layer) vs NSCLC immunosuppressive (CCL20/S100A10/SPP1 layer)
- FOLR2 TAM: HCC non-responder-associated vs breast cancer T-cell-infiltration-favourable
- Hypoxic activation context: mMAC1/IL4I1 program inverts the "hypoxia = immunosuppression" expectation in BLCA/OC ([[concepts/mmac1-hypoxic-inflammatory-macrophage]]) — another instance of context-dependence

## Comparison

vs pan-cancer TAM universalism: opposite framing.
vs cell-state plasticity: distinct; here the state is *stable* but the context modulates output.

## When to use

When designing predictive biomarkers, when generalising preclinical TAM-targeting therapies, or when comparing scRNA-seq atlases across tumor types.

## Known limitations

- Tissue-context overlay is poorly characterised mechanistically.
- Most evidence is correlational; functional dissection of the tissue-layer genes is sparse.

## Open problems

- Which tissue-derived signals (hepatocyte vs alveolar epithelium vs mammary epithelium) program the overlay?
- Can the overlay be reprogrammed therapeutically to flip the functional output?

## Key papers

- [[papers/trem2-macrophages-associated-enhanced-response-pd]] — flagship example: TREM2 mac protective in HCC vs immunosuppressive in NSCLC, with 209-vs-89 tissue-specific genes
- [[papers/nf-kb-tet2-promote-macrophage-reprogramming]] — complementary example at the activation-context axis (hypoxia × LPS reprograms TAM functional output in BLCA/OC)
