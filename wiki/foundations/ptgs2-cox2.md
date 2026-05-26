---
title: "PTGS2 / COX2 — prostaglandin-endoperoxide synthase 2 (cyclooxygenase 2)"
slug: ptgs2-cox2
domain: enzymology / inflammation
status: mainstream
aliases:
  - "PTGS2"
  - "COX2"
  - "COX-2"
  - "cyclooxygenase 2"
  - "Ptgs2"
  - "prostaglandin G/H synthase 2"
  - "inducible cyclooxygenase"
  - "PGHS2"
first_introduced: "Xie 1991 PNAS (inducible PGHS / mitogen-responsive)"
date_updated: 2026-05-26
source_url: ""
---

## Definition

PTGS2 (Ptgs2 in mouse) encodes cyclooxygenase-2 (COX2), the inducible isoform of the prostaglandin-endoperoxide synthase family that converts arachidonic acid to prostaglandin H2, the precursor of PGE2, PGD2, PGI2, and thromboxanes. COX2 expression is rapidly upregulated by growth factors, cytokines, ERK/MAPK signaling, and efferocytosis in macrophages; its activity defines whether arachidonic acid output is biased toward inflammatory or pro-resolving prostanoids depending on downstream synthase availability (PGES → PGE2; thromboxane synthase → TXA2; etc.).

## Intuition

COX2 is the rate-limiting enzyme for inflammation-associated prostaglandin synthesis but is paradoxically also required for pro-resolution PGE2 output during efferocytosis — the same enzyme, opposite tissue outcome, dictated by receptor context (e.g., EP2/EP4 binding TGFβ1 induction in efferocytosing macrophages vs EP1/EP3 mediating vasoconstriction/inflammation).

## Formal notation

- Gene: PTGS2 (chr1q31; Ptgs2 in mouse)
- Reaction: arachidonic acid + 2 O₂ → prostaglandin H2 → (via PGES) PGE2
- Inducers: LPS, TNFα, IL-1β, PMA, ERK1/2 activation, AC-induced DNMT3A/SAM signalling
- Receptors downstream of PGE2: EP1-EP4
- Pharmacology: NS-398 (COX2-selective); celecoxib, rofecoxib (clinical COX2 inhibitors with cardiovascular side effects)
- Knockout phenotype: Ptgs2-/- mice — kidney developmental defects, female reproductive failure; conditional myeloid KO impairs resolution

## Variants

- COX1 (constitutive housekeeping isoform, PTGS1) — homeostatic prostaglandin
- COX2 (inducible) — context-dependent inflammation and resolution
- COX3 — splice variant of COX1 (controversial)

## Known limitations

- COX2 induction does not by itself predict whether output is PGE2 vs other prostanoids — downstream synthase availability matters
- Selective COX2 inhibitors carry cardiovascular risk; mechanism implicates PGI2 suppression
- Antibody specificity (vs COX1) variable

## Open problems

- Why COX2/PGE2 has opposite roles in resolution (efferocytosis) vs inflammation (acute response)
- Whether COX2 cellular subpopulation matters as much as total expression in atherosclerotic plaques

## Relevance to active research

Central to [[papers/macrophages-use-apoptotic-cell-derived-methionine]] (Ampomah 2022 *Nat Metab*): COX2 is the obligate enzymatic output of the AC→methionine→SAM→DNMT3A→Dusp4-repression→ERK pathway, leading to PGE2 synthesis and EP2/EP4-mediated TGF-β1 induction.
