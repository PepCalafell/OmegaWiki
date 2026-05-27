---
title: "c-Myc compensatory mitochondrial/ribosomal axis in HIF-1α-deficient BMDMs"
aliases:
  - "Myc compensation HIF-1α-loss BMDM"
  - "HIF-1α–Myc antagonism in macrophages"
  - "Myc-driven OXPHOS in Hif1a-/- macrophage"
tags:
  - MYC
  - HIF1A
  - BMDM
  - OXPHOS
  - ribosomal-biogenesis
  - cell-proliferation
  - transcription-factor-antagonism
  - immunometabolism
maturity: emerging
key_papers:
  - hif-regulates-mitochondrial-function-bone-marrow
first_introduced: "Woods et al. 2025 (Sci. Rep.) — DoRothEA + Myc siRNA causal mapping in BMDMs"
date_updated: 2026-05-27
related_concepts:
  - ontogeny-divergent-hif1a-macrophage-metabolism
  - warburg-effect-hif1a-glycolytic-reprogramming
  - hif-dependent-glycolysis-immune-cell-differentiation
---

## Definition

In BMDMs lacking HIF-1α, the c-Myc regulon is derepressed and drives a compensatory shift toward mitochondrial OXPHOS, elevated TCA cycle metabolite levels, increased ETC complex I–IV protein expression, and a transcriptional program of ribosomal biogenesis and proliferation. This Myc-dependence is causally established by siRNA-mediated Myc knockdown in Hif1a⁻/⁻ BMDMs, which normalises basal mitochondrial respiration and ATP production back to control levels.

## Intuition

HIF-1α and c-Myc are mutually antagonistic master regulators of cellular metabolism — HIF-1α drives glycolysis and suppresses growth; c-Myc drives biosynthesis, growth, OXPHOS, and proliferation. When HIF-1α is removed from BMDMs, the c-Myc program is no longer held in check, and the macrophage drifts from a glycolytic, inflammation-poised state to a Myc-dominated, mitochondria-dominated, growth-poised state that is less pro-inflammatory but more proliferative.

## Formal notation

- DoRothEA TF activity (Hif1a⁻/⁻ vs WT BMDM): HIF1A most negative NES; MYC most positive NES.
- Concordant upregulated regulons: E2F1–4, LEF1, GIL2, TFDP1 (all pro-growth).
- Downregulated regulons: FOXO, TCF12, MAF, ONECUT (cell-cycle arrest / glucose-homeostasis).
- Shared c-Myc/HIF-1α target genes — only the glycolytic subset (e.g. *Ldha*) is downregulated in Hif1a⁻/⁻ BMDMs, consistent with HIF-1α being the dominant driver at glycolytic enhancers.
- Causal rescue: Myc siRNA in Hif1a⁻/⁻ BMDMs returns basal OCR and ATP production to WT levels.

## Variants

- Hypoxic context: HIF-1α can displace c-Myc from chromatin and induce cell-cycle arrest (Koshiji 2004; Gordan 2007) — converse of the BMDM observation.
- MCSF-restimulation of BMDMs after starvation also upregulates c-Myc and drives a proliferative, dual glycolytic/mitochondrial phenotype (Daniel 2018, BMDM proliferative state) — same axis, opposite trigger.

## Comparison

This is the inflammatory-macrophage analogue of well-described HIF-1α / c-Myc antagonism in cancer cells (e.g. tumor switch between Warburg metabolism and biosynthetic growth). Distinguished from generic [[concepts/warburg-effect-hif1a-glycolytic-reprogramming]] in that the relevant phenotype is suppression of inflammation rather than tumor survival.

## When to use

When interpreting cytokine-deficient or growth-skewed phenotypes after HIF-1α perturbation in monocyte-derived macrophages; when designing combination therapies that target HIF-1α in inflammatory contexts (a Myc-driven mitochondrial compensation may blunt the desired effect or shift macrophages toward pro-resolution/tissue-repair states).

## Known limitations

- Causal Myc-rescue demonstrated only for basal OCR/ATP — Myc-dependence of the inflammatory-cytokine reduction or ribosomal-biogenesis program was not directly tested.
- DoRothEA infers TF activity from gene-expression footprints — not direct ChIP evidence in Hif1a⁻/⁻ BMDMs.
- Not tested in human MDMs or in vivo.

## Open problems

- Does the Myc-compensation also operate in vivo (e.g. in HIF-1α-deficient infiltrating macrophages in tumors)?
- Is the proliferative shift mechanistically linked to the c-Myc/ribosomal biogenesis observation in tumor-associated macrophages?
- Could PHD-inhibitor therapies (which stabilise rather than ablate HIF-1α) trigger the opposite — Myc suppression and impaired macrophage proliferation in inflammation?

## Key papers

- [[papers/hif-regulates-mitochondrial-function-bone-marrow]] — defining paper.

## My understanding

A clean causal observation worth integrating into the hypoxia / macrophage knowledge map. It also implies that interpreting "HIF-1α inhibitor" data in monocyte-derived macrophages must include a Myc activity readout — otherwise the rebound mitochondrial / proliferative state will be misattributed to other regulators.
