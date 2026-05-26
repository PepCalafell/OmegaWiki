---
title: "AHR non-genomic effects — cytoplasmic SRC interaction, STAT1 sequestration, CUL4B-E3 ligase activity, and calcium signalling, independent of XRE transcription"
aliases:
  - AHR non-genomic effects
  - AHR cytoplasmic signalling
  - AHR-SRC axis
  - AHR-STAT1 interaction
  - AHR-CUL4B E3 ligase
  - AHR calcium signalling
  - AHR ESR1 AR PPARG degradation
  - non-transcriptional AHR
  - AHR transcription-independent
  - AHR-EGFR-FAK signalling
  - cytoplasmic AHR functions
tags:
  - AHR
  - non-genomic
  - SRC
  - STAT1
  - CUL4B
  - calcium
  - BRAFi-resistance
  - melanoma
  - ESR1
  - androgen-receptor
  - PPARG
maturity: active
key_papers:
  - complex-biology-aryl-hydrocarbon-receptor-activation
  - aryl-hydrocarbon-receptor-rehabilitated-target-therapeutic
first_introduced: ""
date_updated: 2026-05-26
related_concepts:
  - ahr-non-canonical-signalling
  - ahr-context-specificity-pleiotropy
  - ahr-canonical-signalling-pathway
---

## Definition

Transcription-independent functions of AHR in the cytoplasm, mediated by direct protein-protein interactions and enzymatic activities that do not require nuclear translocation or XRE binding. The four documented arms are: (i) SRC interaction → SRC/EGFR/FAK phosphorylation cascade; (ii) STAT1 sequestration / heterodimerisation repressing STAT signalling; (iii) AHR as the substrate-recognition subunit of a CUL4B-based E3 ubiquitin ligase that degrades ESR1, AR, PPARG; (iv) AHR-dependent intracellular Ca²⁺ elevation (e.g. by pyrene).

## Intuition

A traditional view of AHR as "ligand-activated transcription factor" misses half of its pharmacology. The same ligand can activate canonical AHR transcription *and* trigger SRC kinase / E3 ligase / Ca²⁺ outputs simultaneously — explaining why AHR phenotypes do not always track CYP1A1 expression.

## Formal notation

| Arm | Partner / target | Effect | Therapeutic relevance |
|---|---|---|---|
| Kinase axis | SRC → EGFR, FAK | promotes melanoma BRAFi resistance; supports AR signalling in prostate cancer | combined BRAFi + AHR/SRC inhibition |
| STAT axis | STAT1 cytoplasmic heterodimer | represses STAT homodimer nuclear translocation and IFN signalling | indirect modulation of IFN responses |
| E3 ligase axis | CUL4B + AHR → ESR1, AR, PPARG | ligand-dependent proteasomal degradation of nuclear receptors | breast/prostate cancer endocrine resistance |
| Ca²⁺ axis | AHR-dependent Ca²⁺ rise (pyrene example) | calcium-dependent signalling within minutes | unclear |
| PTM axis | ubiquitination of RAC1 (BaP > FICZ) | ligand-specific PTM signatures | ligand-specific drug discrimination |

## Variants

- Ligand-specific outputs: BaP induces ~5-fold more PTM regulation than FICZ at equivalent canonical induction.
- Pocket-specific outputs: vemurafenib appears to trigger nuclear translocation without canonical XRE engagement — possibly biases output toward non-genomic arms.

## Comparison

- Versus canonical AHR signalling: non-genomic effects can dominate the phenotype in cells with low ARNT availability or repressed nuclear AHR machinery.

## When to use

- When designing AHR-targeted drugs for BRAFi-resistant melanoma, prostate cancer, or endocrine-resistant breast cancer.
- When interpreting AHR phenotypes that fail to correlate with CYP1A1 mRNA.

## Known limitations

- Stoichiometry / kinetics of the four arms vs canonical transcription not quantified.
- The CUL4B-AHR substrate scope beyond ESR1/AR/PPARG is unknown.

## Open problems

- Are there pocket-selective ligands that activate non-genomic outputs without XRE transcription?
- Mechanistic basis for ligand-specific PTM outputs (BaP vs FICZ).

## Key papers

- [[papers/complex-biology-aryl-hydrocarbon-receptor-activation]] — Opitz et al. 2023 §8.
- [[papers/aryl-hydrocarbon-receptor-rehabilitated-target-therapeutic]] — Polonio/Quintana 2025 — therapeutic framing of non-genomic AHR.

## My understanding

The AHR-SRC axis as a BRAFi-resistance vulnerability is the most clinically tractable arm. The CUL4B E3 activity (a "transcription-factor-as-ligase" mode) deserves more attention as an orthogonal therapeutic mechanism.
