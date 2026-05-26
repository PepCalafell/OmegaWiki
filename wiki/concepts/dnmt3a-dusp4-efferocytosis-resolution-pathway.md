---
title: "DNMT3A–DUSP4 efferocytosis-resolution pathway"
aliases:
  - "DNMT3A efferocytosis pathway"
  - "AC-methionine-SAM-DNMT3A-Dusp4 axis"
  - "efferocytosis-induced Dusp4 methylation"
  - "AC-derived methionine DNMT3A resolution"
  - "DNMT3A-COX2-TGFβ1 axis"
  - "epigenetic resolution program macrophage"
  - "methionine-SAM-DNMT3A pathway"
  - "AC-degradation-induced ERK sustainment pathway"
  - "phagolysosomal methionine DNA methylation macrophage"
  - "Ampomah pathway"
tags:
  - macrophage
  - efferocytosis
  - DNA-methylation
  - DNMT3A
  - Dusp4
  - COX2
  - PGE2
  - TGFβ1
  - resolution
  - atherosclerosis
maturity: emerging
key_papers:
  - macrophages-use-apoptotic-cell-derived-methionine
first_introduced: "Ampomah 2022 Nat Metab"
date_updated: 2026-05-26
related_concepts:
  - efferocytosis-anti-inflammatory-clearance
  - ac-derived-methionine-sam-macrophage-epigenetics
---

## Definition

A two-step efferocytosis signalling pathway by which macrophages couple apoptotic-cell (AC) recognition + AC phagolysosomal degradation to sustained ERK1/2 activation and COX2-PGE2-TGFβ1 induction. Step 1: AC binding to CD36 (and modestly MERTK) activates ERK1/2 transiently, but ERK-DUSP4 negative feedback limits the response. Step 2: phagolysosomal AC degradation releases methionine; methionine is converted to SAM by MAT2A; SAM is used by DNMT3A to methylate the CpG-rich Dusp4 promoter, repressing Dusp4. With DUSP4 down, p-ERK is sustained, driving Ptgs2/COX2 induction → PGE2 secretion → EP2/EP4-mediated p-CREB1 → autocrine/paracrine TGF-β1 production. The TGF-β1 output feeds forward by enhancing continual efferocytosis and promoting tissue resolution (cap thickening in plaques, debris clearance in DEX-thymus and zymosan peritonitis).

## Intuition

Efferocytosis triggers two distinct waves of signalling: a transient surface-receptor signal (CD36 → ERK) and a delayed metabolic-epigenetic signal (AC-methionine → SAM → DNMT3A → Dusp4 silencing). The macrophage only commits to the resolution program once both waves arrive — a built-in safety check ensuring that mere AC binding (without actual ingestion / digestion) does not trigger the resolution cascade. The "second wave" is uniquely epigenetic: methyl groups from the corpse you just ate end up writing on your own DNA.

## Formal notation

Two-step cascade:
1. AC binding → CD36 / MerTK → ERK1/2 transient activation → Ptgs2 (insufficient alone)
2. AC engulfment → phagolysosomal degradation → AC-methionine release → MAT2A → SAM → DNMT3A → methylated Dusp4 promoter → Dusp4 repression → sustained p-ERK → Ptgs2/COX2 induction → PGE2 → EP2/EP4 → p-CREB1 (DNMT3A-dependent step 2b) → Tgfb1 transcription → TGF-β1 secretion → autocrine/paracrine enhancement of efferocytosis

## Variants / alternative routes

- Other AC cargo (cholesterol → LXR; arginine → ornithine/putrescine; fatty acids → IL-10) drive other resolution programs in parallel (Tabas lab series; reviewed in Doran 2020).
- DNMT3A also operates downstream of PGE2-EP2/4 to enable p-CREB1 — a second site of DNMT3A dependence whose mechanism is unresolved.

## Comparison

vs LPS-induced COX2: LPS also induces COX2 in macrophages, but independently of DNMT3A — the AC-specific DNMT3A requirement is a context-specific switch, not a general COX2-induction node.
vs other AC-metabolite pathways: methionine→SAM→DNMT3A is uniquely *epigenetic*. Arginine→ornithine and fatty acid→IL-10 work through transcription factor activation rather than DNA methylation.

## When to use

- Interpreting why efferocytosis-defective macrophages (DNMT3A CHIP carriers, plaque macrophages) fail to resolve inflammation despite intact AC binding
- Designing therapies that boost macrophage SAM availability or DNMT3A activity in atherosclerosis regression
- Predicting that methionine-restricted diets may impair efferocytosis-mediated resolution

## Known limitations

- The direct causal link between Dusp4-promoter methylation and Dusp4 transcriptional repression is inferred from MeDIP enrichment + DNMT3A KO — not directly tested by targeted demethylation
- AC-derived methionine *per se* as the methyl source on the Dusp4 promoter is inferred from 13C-mC tracking on bulk DNA, not site-specific
- The role of TET demethylases in this loop is unaddressed

## Open problems

- Site-specific methyl-mark tracking at the Dusp4 promoter (e.g., 13C5-methionine + targeted bisulfite + LC-MS)
- The molecular mechanism of DNMT3A dependence in the PGE2-EP2/4 → p-CREB1 step
- Whether AC-derived methionine routes preferentially to nuclear SAM pools near DNMT3A vs cytoplasmic pools
- Therapeutic targeting: can SAM supplementation, MAT2A activators, or selective DNMT3A enhancers rescue resolution in CHIP-DNMT3A or advanced atherosclerosis?
- Whether the pathway is preserved or rewired in tumour-associated macrophages

## Key papers

- [[papers/macrophages-use-apoptotic-cell-derived-methionine]] — Ampomah et al. 2022 *Nat Metab* — defines the pathway in vitro (BMDM, HMDM) and in vivo (DEX-thymus, zymosan peritonitis, atherosclerosis) using DNMT3A-KO and chemical/genetic dissection

## My understanding

This pathway is a strong template for "second-wave" epigenetic signalling in macrophages, where post-engulfment metabolite flux writes onto the macrophage DNA to commit it to resolution. For the broader macrophage-immunology literature, it raises the question of which other efferocytosis outputs (IL-10, LXR-cholesterol axis, polyamine signaling) similarly require an epigenetic second step. For atherosclerosis specifically, it provides a candidate mechanism linking DNMT3A CHIP mutations to coronary artery disease that goes beyond general inflammatory dysregulation. The DNMT3A-dependent PGE2 → p-CREB1 step is an unresolved second site of DNMT3A control that deserves dedicated study.
