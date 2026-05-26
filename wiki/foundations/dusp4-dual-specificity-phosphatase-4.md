---
title: "DUSP4 — dual-specificity phosphatase 4"
slug: dusp4-dual-specificity-phosphatase-4
domain: signalling / phosphatase
status: mainstream
aliases:
  - "DUSP4"
  - "MKP-2"
  - "MAP kinase phosphatase 2"
  - "Dusp4"
  - "dual-specificity phosphatase 4"
  - "ERK phosphatase"
  - "MKP2"
first_introduced: "Guan & Butch 1995"
date_updated: 2026-05-26
source_url: ""
---

## Definition

DUSP4 (MKP-2) is a member of the dual-specificity phosphatase family that dephosphorylates the activation-loop tyrosine and threonine of MAP kinases (ERK1/2, JNK, p38), providing negative feedback to mitogenic and stress signaling. In macrophages, AC-induced ERK1/2 activation transiently triggers DUSP4 expression, creating a feedback loop that limits ERK output unless DUSP4 is itself repressed by upstream DNA methylation.

## Intuition

DUSP4 is the off-switch ERK provides itself. To sustain ERK signaling for downstream gene induction (e.g., Ptgs2), cells must either bypass or repress DUSP4 — DNA methylation of its promoter by DNMT3A is one such mechanism.

## Formal notable

- Substrates: ERK1/2 (primary), JNK, p38
- Inducers: ERK activation (negative feedback)
- Repression: DNA methylation at the CpG-rich Dusp4 promoter by DNMT3A in efferocytosing macrophages
- Knockdown / KO: siDusp4 prolongs p-ERK and rescues efferocytosis-induced COX2/TGFβ1 in DNMT3A-deficient macrophages
- Detection: methylated DNA immunoprecipitation (MeDIP) at Dusp4 promoter

## Variants

- DUSP1 (MKP-1) — related family member, AC-induced changes not observed in Ampomah 2022
- Cytoplasmic vs nuclear MKPs differ in substrate access

## Known limitations

- Selective inhibitors lacking; genetic silencing required
- Overlapping substrate specificity with DUSP1/6/9 complicates phenotyping

## Open problems

- Whether other DUSPs are co-regulated with DUSP4 during efferocytosis
- Direct vs indirect repression of Dusp4 by DNMT3A — is the methylation event the actual repressor?

## Relevance to active research

Central to [[papers/macrophages-use-apoptotic-cell-derived-methionine]] (Ampomah 2022 *Nat Metab*): DUSP4 is the obligate node whose DNMT3A-mediated repression enables sustained ERK1/2 activation, leading to Ptgs2-PGE2-TGFβ1 induction. siDusp4 rescues the efferocytosis defect in DNMT3A-KO macrophages — direct epistatic evidence.
