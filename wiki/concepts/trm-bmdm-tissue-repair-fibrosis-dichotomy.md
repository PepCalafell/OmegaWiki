---
title: "TRM-restorative / BMDM-fibrotic functional dichotomy in tissue repair"
aliases:
  - "TRM regenerative role"
  - "BMDM fibrotic role"
  - "monocyte-derived macrophage fibrosis"
  - "resident vs recruited macrophage repair"
  - "CCR2 monocyte fibrosis"
  - "tissue repair macrophage dichotomy"
  - "macrophage repair vs fibrosis"
  - "Ccr2-deficient mouse fibrosis"
  - "BMDM-driven tissue fibrosis"
tags:
  - macrophage
  - tissue-repair
  - fibrosis
  - CCR2
  - immunology
  - liver
  - heart
  - kidney
  - lung
maturity: active
key_papers:
  - physiology-diseases-tissue-resident-macrophages
first_introduced: "Duffield 2005 JCI; Wynn & Vannella 2016 Immunity; CCR2-KO fibrosis studies (refs 160-163); reviewed in Lazarov & Geissmann 2023"
date_updated: 2026-05-06
related_concepts:
  - macrophage-ontogeny-resident-vs-monocyte-derived
  - efferocytosis-anti-inflammatory-clearance
  - kupffer-cell-iron-recycling
---

## Definition

Across multiple injury models — liver, heart, kidney, lung — tissue-resident macrophages (TRMs) tend to support tissue repair, regeneration, and resolution, whereas bone-marrow-derived monocyte-derived macrophages (BMDMs) recruited to the site of injury tend to amplify inflammation and drive fibrosis. The dichotomy is operationally demonstrated by CCR2-deficient mice (lacking circulating monocytes) showing substantially milder fibrosis in injury models, and by macrophage-depletion-vs-replacement experiments separating early (TRM) from late (BMDM) phases of repair.

## Intuition

Tissue injury triggers a stereotyped two-wave macrophage response: (1) TRMs respond first, performing efferocytosis, debris clearance, and anti-inflammatory "fix-the-tissue" output (TGFβ at low dose, IL-10, growth factors); (2) circulating monocytes are recruited via CCR2-CCL2 and differentiate into BMDMs that amplify inflammation (TNF, IL-1β, IL-6, ROS, proteases) and, when injury persists, drive a fibrotic outcome via TGFβ overshoot, myofibroblast activation, and ECM deposition. The two populations are *spatially* and *temporally* segregated within the tissue, and removing the recruited population (CCR2 KO, anti-CCL2) leaves repair largely intact while preventing fibrosis.

## Formal notation

- **TRM functions in repair**:
  - Efferocytosis of dying cells with anti-inflammatory output (TGFβ, IL-10, PGE2)
  - Production of growth factors: IGF1, PDGF-CC, WNT ligands, VEGF-A/C, hepatocyte growth factor
  - ECM remodelling via metalloproteases (MMP, ADAMTS1)
  - Examples: Kupffer cells in liver regeneration after partial hepatectomy; dermal macrophages in wound healing (re-epithelialization, vascularization); muscle-resident macrophages secreting IGF1 + ADAMTS1 + glutamine for satellite cell activation
- **BMDM functions in fibrosis**:
  - Pro-inflammatory cytokine amplification (TNF, IL-1β, IL-6)
  - Myofibroblast recruitment via TGFβ overshoot and PDGF
  - Collagen deposition
  - Examples: liver cirrhosis (Duffield 2005), cardiac fibrosis post-MI, kidney fibrosis post-IRI, pulmonary fibrosis
- **CCR2-KO phenotype**: substantially milder fibrosis in liver, heart, kidney, lung injury models — operational evidence for BMDM-driven fibrosis
- **Therapeutic implication**: CCR2 / CCL2 blockade as anti-fibrotic strategy — selectively deplete BMDMs without disturbing TRM repair

## Variants

- *Skin wound healing*: macrophage depletion in early phase impairs re-epithelialization; depletion in late phase produces fibrosis. (Mirza 2009; Wynn & Vannella 2016)
- *Kupffer-mediated liver regeneration*: WNT and HGF from Kupffer cells stimulate hepatic progenitor differentiation.
- *Neonatal heart regeneration* (Aurora 2014): macrophages required; depletion abolishes regenerative capacity.
- *Limb regeneration in salamander, fin in zebrafish*: macrophages required; species-conserved repair function.

## Comparison

vs efferocytosis alone: the dichotomy is broader than efferocytosis — it includes ECM remodelling, growth-factor production, and angiogenesis. Efferocytosis is one of several TRM-restorative mechanisms.
vs M1/M2 polarization: M1/M2 is a state descriptor; this dichotomy is a *lineage* descriptor (TRM vs BMDM origin) that approximately maps to M2-like vs M1-like cytokine profiles but with important exceptions. The lineage-based dichotomy is more predictive of fibrosis outcome than the M1/M2 polarization label.
vs ancillary-cell pairing: this dichotomy is the dynamic, injury-state version of the TRM-as-ancillary-cell model. At homeostasis, TRM = ancillary support; under injury, the ancillary support is augmented by recruited BMDMs that often overshoot and drive fibrosis.

## When to use

- Predicting which macrophage-targeting therapy will reduce fibrosis without abolishing repair.
- Interpreting CCR2-deficient mouse phenotypes across organ injury models.
- Designing temporally-staged macrophage interventions (preserve early TRM repair, block late BMDM fibrotic phase).

## Known limitations

- Many studies use non-specific depletion (clodronate, diphtheria-toxin, anti-F4/80) that hit both populations.
- Some tissues have substantial TRM-replacement-by-BMDM after persistent injury, blurring the distinction.
- Fibrosis is multi-cellular; macrophage contribution overlaps with myofibroblast and endothelial mesenchymal transition.
- Cross-species translation incomplete; human CCR2 inhibitors (cenicriviroc) have produced disappointing anti-fibrotic results in MASH trials, suggesting the mouse model overstates the dichotomy.

## Open problems

- Quantitative thresholds for TRM-vs-BMDM contribution at which repair tips into fibrosis.
- Whether BMDMs that persist in tissue can be re-educated into TRM-like restorative cells.
- Why anti-CCR2 therapy underperforms in human fibrotic disease compared to mouse models.

## Key papers

- [[papers/physiology-diseases-tissue-resident-macrophages]] — Lazarov & Geissmann 2023 *Nature* — review section "Tissue remodelling and regeneration" consolidates the TRM-restorative / BMDM-fibrotic dichotomy across liver, heart, kidney, lung, and notes the CCR2-KO milder-fibrosis phenotype as the operational evidence

## My understanding

This dichotomy is the closest the field has to a *first-pass functional rule* for choosing between macrophage-targeting therapies in fibrotic disease. For my hypoxia-NF-κB work this is mechanistically informative: hypoxia + NF-κB activation in macrophages is closer to the BMDM-fibrotic profile (TNF, pro-inflammatory cytokines), so I should expect hypoxic environments to bias macrophage populations toward fibrotic outcomes. Whether this is true in tumour contexts (where TAMs are mostly BMDM-derived, hypoxic, and pro-tumour) is consistent — TAMs often drive TGFβ overshoot and stromal fibrosis, which supports tumour growth.
