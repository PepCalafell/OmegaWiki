---
title: "Epigenome-based functional profiling of kinase inhibitors"
aliases:
  - "epigenome-based CKI profiling"
  - "H3K27ac-based kinase inhibitor profiling"
tags:
  - kinase-inhibitors
  - epigenomics
  - H3K27ac
  - drug-profiling
  - macrophages
  - methods
maturity: emerging
key_papers:
  - integrative-epigenome-based-strategy-unbiased-functional
first_introduced: "Gualdrini et al. 2024 *Molecular Systems Biology*"
date_updated: 2026-06-03
related_concepts:
  - polypharmacology-clinical-kinase-inhibitors
  - h3k27ac-functional-readout-signaling-perturbation
  - discordance-between-vitro-kinase-inhibitor-selectivity
---

## Definition

An experimental–analytical strategy that profiles the functional cellular effects of clinical kinase inhibitors (CKIs) by reading out signal-induced changes in a dynamic chromatin modification (H3K27ac) genome-wide, rather than by measuring in-vitro target binding or transcriptome changes. Inhibitor-induced H3K27ac perturbations across thousands of cis-regulatory elements are deconvolved (via Multiple Factor Analysis) into per-CRE perturbation likelihoods, and inter-inhibitor similarity is computed from the overlap and kinetics of those perturbations.

## Intuition

Kinases relay signals to transcription factors that deposit/remove histone acetylation at enhancers. So the pattern of H3K27ac change a drug induces is an indirect but high-content fingerprint of which signaling pathways (and downstream TFs) the drug actually perturbs in living cells — a functional readout, not a binding readout.

## Formal notation

- Setting: primary mouse BMDMs, stimuli LPS (TLR4) or IL-4 (IL-4R), timepoints 0/0.5/1/2/4 h.
- Readout: ~600 H3K27ac ChIP-seq datasets across 58 CKIs + DMSO.
- Deconvolution: MFA → per-CRE perturbation likelihood; KNN network of CKIs.

## Variants

- Transcriptome-based profiling (RNA-seq) — lower granularity comparator.
- Phosphoproteomics / kinobeads — orthogonal binding/activity readouts.

## Comparison

Versus binding assays (kinobeads): captures cellular functional consequence, not just affinity. Versus RNA-seq: more variables (CREs ≫ genes), excludes RNA-stability/post-transcriptional confounders, and gives higher-resolution inhibitor separation.

## When to use

Best applied to compounds already advanced in the preclinical pipeline to compare on- vs off-target effects within a related compound series in a dynamic, stimulus-driven cellular system — not as a primary high-throughput library screen.

## Known limitations

- Cannot directly assign specific inhibited kinases to specific TFs/H3K27ac changes (only correlative).
- Restricted to the signaling contexts and CKI panel assayed.
- Indirect: infers signaling via downstream chromatin, not direct kinase activity.

## Open problems

- Integrating multiple cell types/contexts and clinical efficacy/toxicity data to predict clinical outcomes.
- Disentangling combinatorial on-/off-target contributions to a measured H3K27ac signature.

## Key papers

- [[papers/integrative-epigenome-based-strategy-unbiased-functional]] — introduces the strategy.

## My understanding

A genuinely novel reframing: treat the epigenome as a polypharmacology "sensor". Highly relevant to macrophage/inflammation epigenetics work — the same H3K27ac/TF-occupancy logic used here for drug profiling is the substrate of enhancer-level signaling analysis.
