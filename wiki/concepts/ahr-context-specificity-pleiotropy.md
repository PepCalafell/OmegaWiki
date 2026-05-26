---
title: "AHR context specificity — eleven layers explain divergent / opposite phenotypes of the same receptor"
aliases:
  - AHR context specificity
  - AHR pleiotropy
  - AHR layered context model
  - AHR context-dependent biology
  - AHR cell-type-specific output
  - AHR ligand-cell-type-context paradigm
  - context-dependent AHR signalling
  - AHR tumour suppressor vs tumour promoter
  - AHR Treg vs Th17 paradox
  - AHR divergence framework
  - eleven-layer AHR model
tags:
  - AHR
  - context-specificity
  - layered-regulation
  - tumour-suppression
  - tumour-promotion
  - immune-modulation
maturity: emerging
key_papers:
  - complex-biology-aryl-hydrocarbon-receptor-activation
  - aryl-hydrocarbon-receptor-rehabilitated-target-therapeutic
first_introduced: "2023 (Opitz et al. Biochem Pharmacol review systematises the framework)"
date_updated: 2026-05-26
related_concepts:
  - ahr-canonical-signalling-pathway
  - ahr-non-canonical-signalling
  - ahr-ligand-pharmacology-sahrm
  - ahr-posttranslational-modifications-landscape
  - ahr-epigenetic-regulation-of-target-genes
  - ahr-arnt-paralogs-and-isoforms
  - ahr-non-genomic-cytoplasmic-effects
  - ahr-hif-arnt-competition
  - ahr-cyp1a1-negative-feedback-clearance
---

## Definition

A framework that explains AHR's divergent — sometimes opposite — phenotypes (tumour promotion vs tumour suppression; Treg vs Th17; inflammation vs immunosuppression) as the combined output of eleven *additive layers of regulation* operating on the same receptor in different cells/contexts.

## Intuition

A single transcription factor cannot, in itself, produce opposite phenotypes. AHR appears to violate this because the field has under-counted the variables that modulate its output. Once each layer is recognised — and especially once two or more interact (e.g. ligand identity × kinase repertoire × ARNT2 dominance) — the divergence becomes predictable rather than paradoxical.

## Formal notation

Net AHR output ≈ f(L, [AHR], [ARNT/ARNT2/iso], [AHRR], TFcrosstalk, sig_crosstalk, NG, PTM, EP_AHR, EP_targets, LDE), where:

| Layer | Variable | Examples |
|---|---|---|
| 1 | Ligand identity (L) | TCDD, FICZ, Kyn, KynA, indirubin, vemurafenib, dietary indoles |
| 2 | AHR expression | tissue-graded; induced by Trp deprivation via NRF2 / mTORC1 |
| 3 | ARNT / ARNT2 / iso ratio | ARNT2 antagonises; iso1/iso3 ratio in lymphoid malignancies |
| 4 | AHR degradation | TIPARP ADP-ribosylation; UCHL3 stabilisation |
| 5 | AHRR | tissue-restricted to barrier immune cells; cancer-silenced |
| 6 | TF crosstalk | KLF6, RB1, E2F1, RELA/B, ESR1, HIF1α/HIF2α |
| 7 | sig_crosstalk | EGFR, STAT, TLR, NF-κB |
| 8 | NG (non-genomic) | SRC, STAT1, CUL4B-E3 ligase, Ca²⁺ |
| 9 | PTM | phosphorylation, SUMOylation, ubiquitination |
| 10 | EP_AHR | AHR promoter methylation / histones / miRNAs |
| 11 | EP_targets | CYP1A1/CYP1B1 enhancer methylation; HK2 demethylation; H1K34 carbamylation |
| 12 | LDE | CYP1A1/B1 ligand-degrading negative feedback |

## Variants

- **Five-source model (Polonio/Quintana 2025)**: AHR-ligand pharmacology + AHRR feedback + CYP1A1 clearance + Treg/Th17 polarisation focus. More compact, more therapy-oriented than the Opitz model.
- **Three-layer model (simplified)**: ligand × cell type × time. Insufficient for explaining BRAFi-resistance or lymphoid-malignancy phenotypes.

## Comparison

- Versus [[concepts/cytokine-cell-type-specific-response-pleiotropy]]: cytokine pleiotropy is mostly receptor-cell-type-driven; AHR pleiotropy adds ligand-occupancy mode (primary vs secondary pocket), PTM landscape, and ARNT competition as orthogonal axes.

## When to use

- When trying to predict whether a candidate AHR drug will produce tumour-promoting or tumour-suppressive effects in a specific cancer.
- When designing patient-stratification biomarkers for AHR-pathway therapeutics.
- When integrating multi-omics (methylation × scRNA-seq × ligand profiling) to forecast AHR phenotypes.

## Known limitations

- The framework is qualitative; no quantitative integration of the eleven layers is published.
- Most evidence per layer is cell-line-specific; in-vivo and human-tissue validation is uneven.
- Layer interactions (e.g. ligand × PTM × ARNT-iso) are largely unmapped.

## Open problems

- A quantitative scoring system that integrates the layers into a predicted AHR phenotype.
- Single-cell atlases that resolve all layers simultaneously.
- Pocket-selective AHR ligands as a tool to test the model.

## Key papers

- [[papers/complex-biology-aryl-hydrocarbon-receptor-activation]] — Opitz et al. 2023 Biochem Pharmacol, the systematic eleven-layer framing.
- [[papers/aryl-hydrocarbon-receptor-rehabilitated-target-therapeutic]] — Polonio/Quintana 2025 NRDD, complementary therapeutic framing.

## My understanding

Useful as a *checklist* when reading any AHR study: identify which layer the study tests, which layers it controls, which it ignores. The single biggest missing piece is a quantitative integrative model — currently a human reader must do the integration cognitively. Likely a candidate for a future ML/multi-omics modelling project using existing scRNA-seq + methylation atlases.
