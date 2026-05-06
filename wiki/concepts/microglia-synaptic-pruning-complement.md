---
title: "Microglia synaptic pruning via complement and BDNF"
aliases:
  - "synaptic pruning"
  - "microglia synaptic pruning"
  - "C1Q complement synapse elimination"
  - "developmental synaptic pruning"
  - "microglia BDNF synapse formation"
  - "complement-mediated synapse refinement"
  - "microglia neuron homeostasis"
  - "microglia learning-dependent synaptogenesis"
tags:
  - microglia
  - neuroscience
  - synapse
  - complement
  - BDNF
  - immunology
  - development
maturity: stable
key_papers:
  - physiology-diseases-tissue-resident-macrophages
first_introduced: "Stevens 2007 Cell (complement); Paolicelli 2011 Science; Parkhurst 2013 Cell (BDNF); reviewed in Lazarov & Geissmann 2023"
date_updated: 2026-05-06
related_concepts:
  - macrophage-ontogeny-resident-vs-monocyte-derived
  - efferocytosis-anti-inflammatory-clearance
  - trem2-microglia-dementia-axis
---

## Definition

Microglia — the yolk-sac-derived tissue-resident macrophages of the central nervous system — actively shape neural circuits by *pruning* synapses during development and adult plasticity. Pruning uses the classical complement cascade (C1Q-tagged synapses are recognized and engulfed) and is paired with the production of trophic factors, primarily BDNF, that support learning-dependent synapse formation. Loss of microglial pruning causes circuit-level connectivity defects; loss of microglial BDNF impairs motor-learning synaptogenesis and modulates neuropathic pain.

## Intuition

The CNS uses macrophages — microglia — to perform *structural editing* of the wiring diagram. C1Q deposits on weak or unused synapses; microglia engulf them. In parallel, microglia secrete BDNF (and other neurotrophins NGF, neurotropin-3, TGFβ, IGF1) that promote synapse strengthening. Pruning is not random — it is activity-dependent, and visual experience modulates microglia–synapse interactions.

## Formal notation

- **Tagging signals**: C1Q deposits on synapses → activates classical complement → C3 fragments mark synapses for engulfment
- **Microglial recognition**: complement receptor CR3 (CD11b/CD18) + scavenger receptors
- **Engulfment**: phagocytic uptake via TIM4/TAM-shared machinery (overlaps with [[concepts/efferocytosis-anti-inflammatory-clearance]])
- **Trophic balance**: BDNF, NGF, neurotropin-3, TGFβ, IGF1 secreted by microglia in steady state
- **Behavioural readouts**: motor learning, neuropathic pain, layer V cortical neuron survival, dopaminergic outgrowth

## Variants

- *Developmental pruning* (highest activity P10–P30 in mouse) — sets up adult connectivity.
- *Adult pruning* — ongoing low-rate refinement; perturbed in neurodegeneration.
- *Disease-associated microglia (DAM)* — TREM2-driven state in neurodegeneration; aberrant synaptic uptake hypothesized as Alzheimer mechanism.

## Comparison

vs efferocytosis (apoptotic cell clearance): synaptic pruning targets *living-but-weak* synapses, not apoptotic neurons. Mechanism overlaps (complement, engulfment) but substrate is structural, not corpse-like.
vs astrocyte synapse-elimination: astrocytes also prune synapses (MEGF10, MERTK pathways) and the two cell types collaborate; microglia are more dynamic and complement-dependent.

## When to use

- Interpreting circuit-level phenotypes in conditional microglia/C1Q knockouts.
- Distinguishing developmental from neurodegenerative synaptic loss.
- Evaluating complement-blocker therapies (e.g. C1Q antibodies in Alzheimer's trials).

## Known limitations

- Complement is not the only pruning mechanism — phosphatidylserine-flipped synapses can be engulfed via PtdSer-recognition pathways.
- "Pruning" measurements often rely on engulfed-material visualization, which conflates active engulfment with passive uptake.
- Mouse-to-human translation: human microglia have distinct transcriptomic states; pruning mechanisms may differ.

## Open problems

- Whether activity-dependent C1Q deposition is upstream or downstream of synaptic weakness.
- The molecular logic of microglial decisions about which synapse to prune.
- How disease-associated microglia (TREM2-driven DAM state) lose vs gain pruning capacity in Alzheimer's.

## Key papers

- [[papers/physiology-diseases-tissue-resident-macrophages]] — Lazarov & Geissmann 2023 *Nature* — review section "Microglia in neuron homeostasis and diseases" covers complement-dependent pruning, microglial BDNF and motor learning, and links to ALSP, paediatric leukoencephalopathy, Alzheimer's, and Nasu-Hakola

## My understanding

The complement-pruning model is one of the cleanest "macrophage as ancillary tissue cell" examples — microglia provide a tissue-specific service (circuit refinement) using a phagocytic toolkit re-purposed from immune defence. For my work, microglia are not directly relevant, but the conceptual template — *resident macrophage uses generic phagocytic + cytokine output to do tissue-specific job* — generalizes to any macrophage-tissue pairing, including hypoxic-tumour macrophages whose "tissue-specific job" is poorly characterized.
