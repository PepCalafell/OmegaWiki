---
title: "CSF1R / IL-34 / CSF2 trophic axis for macrophage development and survival"
aliases:
  - "CSF1R signaling"
  - "CSF1-CSF1R"
  - "IL-34 CSF1R"
  - "GM-CSF CSF2 alveolar"
  - "macrophage trophic factor"
  - "M-CSF receptor signaling"
  - "macrophage growth factor axis"
  - "CSF1R / FMS / c-fms"
  - "CSF2R alveolar macrophage"
  - "IL34 keratinocyte macrophage"
tags:
  - macrophage
  - cytokine-receptor
  - trophic-factor
  - immunology
  - development
maturity: stable
key_papers:
  - physiology-diseases-tissue-resident-macrophages
first_introduced: "Stanley & Heard 1977 (CSF1); Lin 2008 (IL-34); Burgess 1977 (GM-CSF/CSF2); consolidated in Lazarov & Geissmann 2023"
date_updated: 2026-05-06
related_concepts:
  - macrophage-ontogeny-resident-vs-monocyte-derived
  - tissue-specific-lineage-determining-factors-macrophage
---

## Definition

The CSF1R / IL-34 / CSF2 trophic axis comprises three cytokine ligands (CSF1/M-CSF, IL-34, CSF2/GM-CSF) and two receptors (CSF1R, CSF2R) that together control the development, survival, and tissue-specific maintenance of macrophages. CSF1 and IL-34 both bind CSF1R but have non-overlapping tissue distributions; CSF2 binds CSF2R and is essential for alveolar macrophages. Loss-of-function in any component causes tissue-specific or pan-tissue macrophage deficiencies.

## Intuition

Macrophages are not autonomous — every tissue must "feed" its TRMs with the right trophic cocktail. CSF1 (broadly produced, found as both secreted and membrane-bound isoforms) supports most TRMs. IL-34 (produced by neurons and keratinocytes) selectively supports microglia and Langerhans cells. CSF2/GM-CSF (produced by lung type II pneumocytes) selectively supports alveolar macrophages. Disrupting these signals causes tissue-specific TRM loss and corresponding diseases (microglia loss → leukoencephalopathy; alveolar mac loss → alveolar proteinosis).

## Formal notation

- **CSF1R** (CD115, FMS, c-fms): class III receptor tyrosine kinase
  - Ligands: CSF1 (membrane-bound + secreted isoforms), IL-34
  - Tissue dependence: most TRMs require CSF1R; microglia and Langerhans cells specifically require IL-34
- **CSF2R** (GM-CSFR): heterodimeric αβc receptor
  - Ligand: CSF2 (GM-CSF)
  - Tissue dependence: alveolar macrophages (CSF2 from type II pneumocytes); also controls PPARγ expression in alveolar macs
- **Disease genetics**:
  - CSF1R bi-allelic LOF → paediatric leukoencephalopathy + osteopetrosis (microglia absent)
  - CSF1R hypomorph (heterozygous) → ALSP (adult-onset leukoencephalopathy with spheroids)
  - CSF1-deficient mice: deficient in most TRMs, but spare Langerhans cells and microglia (rescued by IL-34)
  - IL-34-deficient mice: selective loss of Langerhans cells and microglia
  - CSF2 / CSF2R / PPARG LOF → alveolar proteinosis (alveolar macs cannot degrade surfactant)

## Variants

- Anti-CSF1R blocking antibodies (clinical: pexidartinib, emactuzumab) → deplete TAMs and TRMs as immunotherapy strategy.
- IL-34 reagents → microglia/Langerhans-selective depletion.
- CSF1 isoform engineering → membrane-bound CSF1 rescues most tissues but not liver, adrenal, spleen, peritoneal cavity (suggests soluble CSF1 has unique reach).

## Comparison

vs CCR2-CCL2 axis: CCR2 controls *monocyte recruitment* from bone marrow; CSF1R controls *macrophage maintenance* once in tissue. Both are exploited therapeutically but have orthogonal effects.
vs niche LDFs: trophic factors are *survival* signals; LDFs are *identity* signals. Both are required.

## When to use

- Predicting which TRM subset will be lost when blocking a specific receptor.
- Interpreting why anti-CSF1R drugs cause certain tissue side effects (osteopetrosis, microglia depletion) but not others.
- Designing trophic-factor-supplementation strategies for TRM regeneration.

## Known limitations

- CSF1 and IL-34 share CSF1R but their downstream signaling and effects diverge — mechanism incompletely understood.
- Most evidence is murine; human equivalents are inferred from disease genetics (CSF1R Mendelian disorders).

## Open problems

- Why CSF1 isoforms have tissue-restricted rescue capability.
- Whether IL-34 has CSF1R-independent receptors with biological relevance (PTP-ζ has been proposed).
- Whether boosting CSF2 in non-alveolar tissues can confer alveolar-like phenotypes.

## Key papers

- [[papers/physiology-diseases-tissue-resident-macrophages]] — Lazarov & Geissmann 2023 *Nature* — review and synthesis of CSF1R/IL-34/CSF2 axis with tissue-specific dependencies and Mendelian disease links

## My understanding

For my work on hypoxia-driven macrophage reprogramming: monocyte-to-macrophage differentiation in our in vitro system is M-CSF-driven (CSF1R agonism), so CSF1R signaling is upstream of every experiment. Whether hypoxia modulates CSF1R signaling itself, or only acts downstream after differentiation, is an underexplored axis worth tracking. The clinical relevance of CSF1R inhibitors in cancer also makes this a translationally important node.
