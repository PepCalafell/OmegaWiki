---
title: "Adipose tissue-resident macrophage / PDGF-CC / lipid storage axis"
aliases:
  - "WAT macrophage lipid storage"
  - "PDGFcc fat macrophage"
  - "white adipose tissue resident macrophage"
  - "adipose tissue macrophage diet-regulated"
  - "fat-resident macrophage PDGF-CC"
  - "fat-associated macrophage"
  - "adipose macrophage energy storage"
  - "diet-regulated PDGF-CC"
  - "Cox 2021 PDGFcc axis"
  - "adipocyte lipid storage growth factor"
tags:
  - macrophage
  - adipose-tissue
  - obesity
  - lipid-metabolism
  - PDGF
  - homeostasis
  - immunology
maturity: active
key_papers:
  - physiology-diseases-tissue-resident-macrophages
first_introduced: "Cox et al. 2021 Science (PDGFcc/diet-regulated lipid storage); reviewed and contextualized in Lazarov & Geissmann 2023"
date_updated: 2026-05-06
related_concepts:
  - macrophage-ontogeny-resident-vs-monocyte-derived
  - trm-bmdm-tissue-repair-fibrosis-dichotomy
---

## Definition

White adipose tissue-resident macrophages (WAT-TRMs) — distinct from BMDM-derived obesity-associated macrophages — sense dietary nutrients and produce the growth factor PDGF-CC, which acts paracrinely on white adipocytes to promote lipid storage. Loss of WAT-TRMs or PDGF-CC redirects unstored energy to brown adipose tissue (BAT), where it is dissipated as heat. The axis is conserved between mouse and *Drosophila* and is non-inflammatory, contrasting with the pro-inflammatory CCR2-recruited BMDMs that drive obesity-associated insulin resistance.

## Intuition

A well-fed organism stores excess energy as lipid in white adipocytes — but the *signal* to store is carried by adipose-resident macrophages, not by the adipocytes themselves sensing nutrients directly. WAT-TRMs respond to dietary fat by upregulating PDGF-CC, which acts on adipocyte PDGFR-α to support lipid uptake and droplet maintenance. Without WAT-TRMs (or without PDGF-CC), white adipocytes fail to store fully and the organism's energy ledger shifts toward BAT thermogenesis (heat dissipation, weight loss). This is *anti-inflammatory homeostasis*; the obesity-associated TNF-driven inflammation comes from a different population — CCR2-recruited BMDMs.

## Formal notation

- **WAT-TRM**: yolk-sac-derived, self-renewing, F4/80⁺ TIM4⁺ Lyve1⁺ MHC-II^low population (mouse)
- **Diet-regulated effector**: PDGF-CC (also called PDGF-C) — secreted growth factor
- **Receptor on adipocyte**: PDGFR-α (with PDGFR-β heterodimers)
- **Output**: enhanced adipocyte lipid uptake and storage (white)
- **Loss-of-function phenotypes**:
  - *PDGF-CC KO mouse*: reduced WAT lipid storage, increased BAT thermogenesis, lean phenotype on high-fat diet
  - *WAT-TRM depletion*: similar — loss of WAT lipid expansion
- **Conserved in *Drosophila***: fat-body macrophages perform analogous lipid-storage support function
- **Counter-population**: CCR2-recruited BMDMs in obesity → produce TNF, drive insulin resistance, ectopic lipid deposition (steatosis)

## Variants

- *Steady-state WAT-TRM* — PDGF-CC-producing, supports lipid storage.
- *BAT-resident macrophage* — control thermogenesis; MECP2-dependent; enhance heat dissipation under cold exposure.
- *SLC6A2⁺ noradrenaline-scavenging macrophage* — controls lipid storage via sympathetic noradrenaline scavenging in adult mice.
- *Obesity-associated BMDM* — TNF-producing, pro-inflammatory; distinct lineage; TREM2-dependent lipid-associated macrophage (LAM) sub-state.

## Comparison

vs liver Kupffer cells: both are TRMs supporting parenchymal lipid/energy biology; Kupffer = iron recycling, WAT-TRM = lipid storage. Both are anti-inflammatory at homeostasis.
vs lipid-associated macrophage (LAM, TREM2-dependent): LAMs accumulate around dying adipocytes in obesity; they are *not* the same as PDGF-CC-producing TRMs. LAMs are partially BMDM-derived and partially TRM-converted.

## When to use

- Interpreting why CSF1R or CCR2 inhibitors have differential effects on lean vs obese metabolic phenotypes.
- Predicting metabolic consequences of macrophage-targeting therapies in cancer (could disrupt lipid storage and cause unintended cachexia).
- Designing therapies for lipodystrophy (could supplement PDGF-CC) or obesity (could block WAT-TRM PDGF-CC to redirect energy to BAT).

## Known limitations

- Mouse-centric mechanism; human PDGF-CC role in adipose biology is not validated by genetics.
- Distinguishing WAT-TRM from LAM is delicate — markers overlap.
- Whether PDGF-CC also signals to non-adipocyte stromal cells in WAT is unresolved.

## Open problems

- Pharmacological exploitability — can PDGF-CC blockade safely mimic exercise/cold-induced thermogenesis without disrupting tissue homeostasis?
- Cross-talk with leptin / adiponectin axes.
- Role in MASH / NASH where ectopic liver lipid is the disease substrate.

## Key papers

- [[papers/physiology-diseases-tissue-resident-macrophages]] — Lazarov & Geissmann 2023 *Nature* — section on adipose macrophages summarizing the PDGF-CC mechanism, conservation in *Drosophila*, and contrast with CCR2-recruited inflammatory BMDMs in obesity
- (Cox et al. 2021 *Science* — primary paper; not yet ingested into this wiki; co-authored by review co-author Nehemiah Cox)

## My understanding

This axis is one of the cleanest demonstrations of the *ancillary cell* model — adipocytes don't fully "decide" to store lipids without macrophage signal. For my work this is largely orthogonal (no WAT in our system), but it provides a conceptual template: hypoxic macrophages may have analogous tissue-specific instructive roles that are NOT captured by inflammatory cytokines. PDGF-CC is the kind of "quiet, instructive" output that a hypoxic-NF-κB programme might paradoxically suppress while activating loud TNF/IL-6 outputs.
