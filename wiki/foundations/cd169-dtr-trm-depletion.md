---
title: "CD169-DTR mouse for tissue-resident macrophage depletion"
slug: cd169-dtr-trm-depletion
domain: "immunology / mouse genetics / methods"
status: mainstream
aliases:
  - "CD169-DTR"
  - "CD169-DTR mouse"
  - "Siglec1-DTR"
  - "Siglec1-cre DTR"
  - "CD169 diphtheria toxin receptor"
  - "intranasal DT TRM depletion"
  - "alveolar macrophage depletion"
  - "tissue-resident macrophage ablation"
  - "Mac-DTR conditional ablation"
  - "TRM-specific depletion mouse"
first_introduced: "Miyake et al. *Immunity* 2007 (CD169-DTR construct); applied to lung TRMs for cancer studies in Casanova-Acebes et al. *Nature* 2021"
date_updated: 2026-05-06
source_url: ""
---

## Definition

A transgenic mouse line in which the human diphtheria toxin receptor (DTR, encoded by HBEGF) is expressed under the control of the CD169 (Siglec1) promoter. Mice are normally insensitive to diphtheria toxin (DT) because rodent HBEGF cannot bind DT; transgenic CD169-DTR cells become DT-sensitive and undergo apoptosis upon DT administration. CD169 is preferentially expressed on tissue-resident macrophages (alveolar macrophages, splenic marginal zone metallophilic macrophages, lymph-node sub-capsular sinus macrophages) and is largely absent from blood monocytes and most monocyte-derived macrophages, making the line a tool for selective TRM depletion. **Intranasal** DT administration restricts depletion to lung TRMs.

## Intuition

CD169 is a marker enriched on long-term-resident, embryonically-seeded macrophage populations and absent from recently-recruited monocytes. Coupling its promoter to the diphtheria toxin receptor turns CD169 expression into a "kill switch" that can be activated by injecting an otherwise inert protein. The system enables loss-of-function studies of TRMs that would otherwise be impossible (no antibody depletion is TRM-specific; CSF1R inhibitors deplete both TRMs and MDMs).

## Key variants

- **CD169-DTR (this concept)**: Siglec1 promoter drives DTR
- **CSF1R-Mer-iCre + DTR**: alternative macrophage-conditional ablation with broader specificity
- **Lyve1-Cre × DTR**: targets a different TRM lineage (tissue-resident vasculature-associated)
- **Cx3cr1-CreER × DTR-flox**: targets monocyte-derived macrophages instead
- **CD11b-DTR**: pan-myeloid depletion (less specific)

## Known limitations

- Not perfectly TRM-specific outside the lung: CD169 is expressed on splenic and lymph-node TRMs, so systemic DT depletes these too
- Intranasal DT route mitigates off-target effects but does not fully isolate alveolar TRMs from nasal/airway TRMs
- DT-induced apoptosis can release DAMPs that may produce secondary inflammatory effects
- Repeated DT dosing may cause toxicity beyond TRM depletion
- Some MDMs upregulate CD169 in chronic inflammation, blurring the lineage specificity in late-stage disease
- Mice must be on a CD169-DTR background; cannot be combined with arbitrary genetic backgrounds without crossing
- Verification of TRM-only depletion (and not MDM) is required per experiment, especially in tumour models where CD169 expression on MDMs may shift

## Open problems

- More restrictive promoters that target only embryonically-seeded TRMs
- Reversible (tamoxifen-inducible) variants to support pulse-chase TRM ablation
- Single-cell verification of which CD169⁺ populations are depleted in each tissue context
- Combined ablation systems (TRM + MDM dual ablation) for orthogonal tests

## Relevance to active research

[[papers/tissue-resident-macrophages-provide-pro-tumorigenic]] uses CD169-DTR + intranasal DT (15 ng/mouse, days 0 and 3) to selectively deplete lung alveolar TRMs before KP NSCLC tumour engraftment. The experiment demonstrates that TRM depletion before tumour seeding reduces tumour burden, decreases Treg numbers and CD73/CTLA-4 expression on remaining Tregs, and increases CD8⁺ effector infiltration. The same system shows that depletion in established lesions (day 12-15) has no effect, establishing the temporal restriction of TRM niche function. Critical control: the authors verify CD169 absence on Ms4a3-tdTom-traced monocyte-derived MDMs in early lesions, confirming that the depletion is TRM-specific in this model. This methodological approach is the load-bearing causal evidence for the entire pro-tumorigenic-niche concept.
