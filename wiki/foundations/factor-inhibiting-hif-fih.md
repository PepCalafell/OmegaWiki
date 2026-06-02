---
title: "Factor inhibiting HIF (FIH)"
slug: factor-inhibiting-hif-fih
domain: hypoxia signalling
status: mainstream
aliases:
  - FIH
  - FIH-1
  - HIF1AN
  - factor inhibiting HIF-1
  - asparaginyl hydroxylase
first_introduced: "2001"
date_updated: 2026-06-02
source_url: "https://www.uniprot.org/uniprotkb/Q9NWT6"
---

## Definition

Factor inhibiting HIF (FIH, gene *HIF1AN*) is an oxygen- and 2-oxoglutarate-dependent asparaginyl hydroxylase that hydroxylates an asparagine residue (Asn803 in human HIF1α) in the C-terminal transactivation domain of HIFα. This hydroxylation blocks recruitment of the CBP/p300 co-activators, repressing HIF transcriptional activity independently of protein stability.

## Intuition

Where the PHD enzymes control HIFα *abundance* (by flagging it for pVHL-dependent degradation), FIH controls HIFα *activity* (by gating co-activator binding). Because FIH has a lower Km for oxygen than the PHDs, it remains active at oxygen tensions where PHDs are already inhibited — providing a second, graded tier of oxygen sensing that fine-tunes the hypoxic transcriptional response.

## Formal notation

HIF1α-Asn803 + O₂ + 2-oxoglutarate → HIF1α-Asn803-OH + succinate + CO₂ (FIH-catalysed); hydroxyl-Asn803 sterically blocks CBP/p300 → transcriptional repression.

## Key variants

- Substrate scope beyond HIFα: FIH also hydroxylates ankyrin-repeat-domain proteins, including IκB family members (e.g. IκBα, p105/NFKB1), linking oxygen sensing to NF-κB signalling.
- Distinct from the prolyl hydroxylase domain (PHD) enzymes, which target HIFα prolines for pVHL recognition.

## Known limitations

- The full physiological substrate repertoire of FIH (many ankyrin-repeat proteins) and the immune-cell-specific consequences of FIH activity remain incompletely defined.

## Open problems

- Whether FIH can be pharmacologically targeted independently of the PHDs for selective modulation of HIF activity versus stability.

## Relevance to active research

FIH is a core node of the oxygen-sensing apparatus central to hypoxia immunology: it confers hypoxic sensitivity on both the HIF and NF-κB pathways via shared hydroxylase chemistry, a mechanism reviewed in [[regulation-immunity-inflammation-hypoxia-immunological-niches]].
