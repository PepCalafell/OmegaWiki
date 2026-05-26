---
title: "Tissue-specific lineage-determining factors (LDFs) for macrophages"
aliases:
  - "LDF"
  - "lineage-determining factor"
  - "tissue-specific LDF"
  - "tissue-specific transcription factor macrophage"
  - "SALL1 microglia"
  - "ID3 Kupffer"
  - "PPARG alveolar macrophage"
  - "SPI-C red pulp macrophage"
  - "GATA6 peritoneal macrophage"
  - "NFATC1 osteoclast"
  - "RUNX3 ID2 Langerhans"
  - "tissue-instructed macrophage TF"
  - "core macrophage transcriptional programme"
tags:
  - macrophage
  - transcription-factor
  - tissue-specification
  - ontogeny
  - immunology
  - epigenetics
maturity: active
key_papers:
  - physiology-diseases-tissue-resident-macrophages
  - metabolism-tissue-macrophages-homeostasis-pathology
first_introduced: "Mass 2016 Science; Lavin 2014 Cell; Gosselin 2014 Cell; conceptually crystallized in Lazarov & Geissmann 2023 Nature"
date_updated: 2026-05-06
related_concepts:
  - macrophage-ontogeny-resident-vs-monocyte-derived
  - csf1r-il34-csf2-trophic-axis
---

## Definition

Tissue-specific lineage-determining factors (LDFs) are transcription factors whose preferential expression in tissue-resident macrophage (TRM) subsets defines and maintains tissue-specific identity. Examples: SALL1 (microglia), ID3 (Kupffer), PPARγ (alveolar), SPI-C (red pulp), GATA6 (peritoneal), NFATC1 (osteoclast), RUNX3/ID2 (Langerhans). LDFs are layered on top of a *core macrophage transcriptional programme* shared across all macrophages (PU.1, cMAF, IRF8) which is established in EMP-derived PreMacs prior to tissue colonization.

## Intuition

A macrophage is not a single cell — it is a *core program* (PU.1/cMAF/IRF8) plus a tissue-specific "module" (an LDF or LDF combination). PreMacs already express patches of LDFs stochastically before colonization (detectable at E10.25). The tissue niche then *selects* PreMacs whose LDF matches the niche's instructive signals (TGFβ, IL-34, retinoic acid, desmosterol/LXRα, CSF2, haem). Genetic deletion of a single LDF causes loss of the corresponding TRM subset without affecting others.

## Formal notation

| Tissue | LDF | Niche signal |
|--------|-----|--------------|
| Brain (microglia) | SALL1 | TGFβ + IL-34 |
| Liver (Kupffer) | ID3 | TGFβ + desmosterol/LXRα |
| Lung (alveolar) | PPARγ | TGFβ + CSF2 |
| Spleen (red pulp) | SPI-C | Haem |
| Peritoneum (large peritoneal) | GATA6 | Retinoic acid |
| Skin (Langerhans) | RUNX3, ID2 | TGFβ + IL-34 |
| Bone (osteoclast) | NFATC1 | RANKL + OPG |
| Kidney | IRF9, NFAT | (locally produced cytokines) |

## Variants

- **Stochastic LDF expression model** (favoured by Lazarov & Geissmann 2023): PreMacs randomly express LDF subsets; niche selects matched cells.
- **Instructive LDF expression model**: niche cytokines actively drive LDF expression in undifferentiated PreMacs.
- **Hybrid model**: combinations of cytokines/growth factors collectively encode tissue identity (cocktail hypothesis).

## Comparison

vs core macrophage TFs (PU.1, cMAF, IRF8): core TFs define "macrophage-ness" and are shared; LDFs define tissue identity and are mutually exclusive across subsets.
vs M1/M2 polarization: M1/M2 is a state descriptor (inflammatory vs alternative); LDFs are lineage descriptors (which tissue this macrophage is from).
vs niche signaling: niche signals are extrinsic; LDFs are the cell-intrinsic readout. Both are part of TRM specification.

## When to use

- Predicting which TRM subsets are missing in a given LDF-knockout mouse.
- Designing therapeutic engineering of macrophage subsets — one must induce the right LDF, not just expose to cytokines.
- Mapping scRNA-seq macrophage clusters to anatomical origin via LDF expression patterns.

## Known limitations

- LDF expression is necessary but not sufficient — niche cues co-act.
- Cross-species conservation is incomplete; some mouse LDFs do not cleanly mark human TRM equivalents.
- Multiple LDFs may co-express in a single subset (e.g. RUNX3+ID2 Langerhans).
- Most evidence is loss-of-function; sufficient gain-of-function reprogramming has not been formally demonstrated.

## Open problems

- Whether stochastic or instructive specification dominates in the embryo.
- Whether unique cocktails of cytokines and growth factors can substitute for LDF expression.
- How LDF expression interfaces with the tissue-specific enhancer landscape (Lavin 2014, Gosselin 2014).

## Key papers

- [[papers/physiology-diseases-tissue-resident-macrophages]] — Lazarov & Geissmann 2023 *Nature* — canonical review; consolidates the LDF table (SALL1/ID3/PPARγ/SPI-C/GATA6/NFATC1/RUNX3-ID2) and frames the stochastic-selection vs instructive specification debate
- (Mass 2016 *Science*; Lavin 2014 *Cell*; Gosselin 2014 *Cell*; Sakai 2019 *Immunity*; Okabe & Medzhitov 2014 *Cell* — primary studies; not yet ingested into this wiki)

## My understanding

For my hypoxia-NF-κB work: hypoxic perturbation of macrophage identity does not act on LDFs directly (the Calafell 2024 system uses bone-marrow-derived monocytes that have not engaged LDFs). But the LDF framework matters for *interpreting* in vivo correlates: if an in vivo TRM subset shows hypoxia-driven NF-κB-cooperative HIF1α binding, the LDF context will dictate which downstream genes are accessible. This is a fruitful direction — combining HIF/NF-κB cooperative binding with LDF-defined enhancer maps from Lavin/Gosselin.
