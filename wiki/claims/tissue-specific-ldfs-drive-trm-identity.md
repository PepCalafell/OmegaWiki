---
title: "Tissue-specific lineage-determining factors (LDFs) drive TRM identity, and their genetic deletion causes subset-specific deficiencies"
slug: tissue-specific-ldfs-drive-trm-identity
status: supported
confidence: 0.9
tags:
  - macrophage
  - LDF
  - tissue-specification
  - transcription-factor
  - immunology
domain: immunology / developmental biology
source_papers:
  - physiology-diseases-tissue-resident-macrophages
evidence:
  - source: physiology-diseases-tissue-resident-macrophages
    type: supports
    strength: strong
    detail: "Lazarov & Geissmann 2023 Nature review consolidates LDF→TRM-subset mapping with KO evidence: ID3 KO depletes Kupffer cells; SALL1 KO depletes microglia; PPARγ KO depletes alveolar macrophages; SPI-C KO depletes red pulp macrophages; GATA6 KO depletes large peritoneal macrophages."
conditions: "Mouse genetic loss-of-function evidence; cross-species (human) inferred from disease genetics and TRM transcriptomes."
date_proposed: 2026-05-06
date_updated: 2026-05-06
---

## Statement

Tissue-resident macrophage identity is established and maintained by tissue-specific lineage-determining transcription factors (LDFs) layered on top of the core macrophage programme (PU.1, cMAF, IRF8). Specific LDFs include SALL1 (microglia), ID3 (Kupffer cells), PPARγ (alveolar macrophages), SPI-C (red pulp macrophages), GATA6 (large peritoneal macrophages), and NFATc1 (osteoclasts). Genetic deletion of any single LDF causes loss or dysfunction of the corresponding TRM subset without broadly affecting other TRMs.

## Evidence summary

The principal evidence in [[papers/physiology-diseases-tissue-resident-macrophages]] is a synthesis of multiple primary studies (Mass 2016 *Science*, Sakai 2019 *Immunity*, Okabe & Medzhitov 2014 *Cell*, Kohyama 2009 *Nature*, etc.) that each individually reported subset-specific deletion phenotypes. The convergent picture is consistent enough that the field treats LDF→TRM-subset mapping as essentially established, with disagreement only at the level of mechanism (stochastic vs instructive specification).

## Conditions and scope

- Murine genetic evidence is the primary substrate; human translation rests on TRM transcriptome similarity, not direct LOF (since human LDF LOF cases are rare or undescribed).
- The KO phenotypes are subset-deletion, not subset-conversion — there is no claim that LDF-X expression in a non-cognate macrophage type converts identity (gain-of-function evidence is incomplete).
- LDFs do not act alone — niche signals (TGFβ, IL-34, CSF2, retinoic acid, haem) and core TFs (PU.1, IRF8) co-act.

## Counter-evidence

- Some TRM subsets express *multiple* LDFs (e.g. RUNX3+ID2 in Langerhans cells), suggesting combinatorial rather than single-LDF specification.
- "Tissue-specific" niche cytokines like TGFβ are in fact broadly expressed, calling into question whether the niche side of the LDF-niche pairing is as discriminating as the LDF side.
- *No* gain-of-function reprogramming of one TRM into another via single LDF expression has been formally demonstrated — so LDFs are necessary but sufficiency remains unproven.

## Linked ideas

(none yet)

## Open questions

- Whether forced LDF expression in a non-cognate macrophage can install a foreign TRM identity (sufficiency test).
- The interaction between LDF expression and the tissue-specific enhancer landscape (Lavin 2014, Gosselin 2014).
- Whether human TRM dysfunction in disease (e.g. SLE) involves dysregulated LDFs.
