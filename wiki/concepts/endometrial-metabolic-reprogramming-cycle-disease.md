---
title: "Endometrial metabolic reprogramming across cycle, endometriosis, and endometrial carcinoma"
aliases: []
tags:
  - endometrium
  - menstrual-cycle
  - endometriosis
  - endometrial-carcinoma
  - kynurenine
  - mevalonate
  - estrogen-signaling
  - metabolic-reprogramming
maturity: emerging
key_papers:
  - atlas-scale-metabolic-activities-inferred-single
first_introduced: "2025"
date_updated: 2026-05-27
related_concepts:
  - sccellfie-metabolic-task-inference
  - warburg-effect-hif1a-glycolytic-reprogramming
  - tryptophan-ido1-kynurenine-immunosuppression
---

## Definition

A working description of the metabolic programs that distinguish endometrial cell types across the menstrual cycle and become dysregulated in endometriosis and endometrial carcinoma, as inferred from single-cell and spatial transcriptomics with [[sccellfie-metabolic-task-inference]]. Programs include MVA/cholesterol biosynthesis (epithelial proliferation), kynurenine/AHR signaling (oxidative-stress and inflammation buffering), PAPS-mediated estrogen sulfation (local hormone inactivation), and phenylalanine→phenylacetate conversion (decidualization).

## Intuition

The endometrium is a regenerating tissue that cycles between proliferation, secretion, and shedding under estrogen–progesterone control. Each phase imposes distinct metabolic demands: lactate/ATP for proliferation, hormone-modulating sulfation reactions for receptivity, ER-quality-control cycles (calnexin/calreticulin) for stromal decidualization. In endometriosis and EEC, the same metabolic axes are co-opted to sustain inflammation (uM1 macrophages, glucose→lactate, kynurenine) or local estrogen supply (androgen→estrogen conversion, MVA-fueled steroidogenesis).

## Variants

- **Healthy cycle**: glandular epithelial cells show ATP-glycolysis + nucleotide salvage at proliferative→secretory; stromal cells show phenylalanine→phenylacetate at decidualization; luminal cells show thromboxane synthesis for hemostasis.
- **Endometriosis (eutopic)**: uM1 macrophages elevate myo-inositol-bisphosphate → triphosphate (PLC/NF-κB) and methylglyoxal; epithelial cells upregulate malonyl-CoA, lactate, arachidonate; stromal cells downregulate kynurenine and NAD-salvage.
- **Endometriosis (ectopic)**: peritoneal lesions preserve M1 macrophages, luminal-epithelial MVA, HMP-shunt, and phenylalanine conversion.
- **Endometrial carcinoma (EEC)**: spatially-organized glucose→lactate, MVA marker in malignant regions, local androgen→estrogen (ESR1 co-localization), kynurenine→AHR axis correlated with tumorigenesis signature.

## Comparison

vs. global tumour-metabolism atlases ([[warburg-effect-hif1a-glycolytic-reprogramming]]): endometrial findings recapitulate Warburg but add tissue-specific axes (kynurenine–AHR, local steroidogenesis) absent from generic models. vs. metabolomics studies of endometriosis: scCellFie nominates cell-type-resolved sources of bulk metabolic shifts (kynurenine, methylglyoxal) that prior bulk approaches conflated.

## When to use

For endometrial-disease hypothesis generation atop existing scRNA-seq/Visium datasets, for designing organoid validation experiments targeting cycle-dependent metabolic transitions, and as priors for spatial-metabolomics study design.

## Known limitations

All evidence is inferred from transcriptomics; no orthogonal metabolomics in the same samples. Two-donor Visium of endometriotic lesions is the lower bound for ectopic-tissue claims. Organoid–in-vivo discrepancies (Tn antigen glycosylation, nucleotide salvage) limit translation of cycle dynamics to ALI/organoid models.

## Open problems

Confirming kynurenine–AHR signaling causally regulates endometrial-epithelial proliferation; testing MVA-pathway inhibitors in EEC; mapping the contribution of local estrogen biosynthesis to EEC progression independent of obesity-driven systemic estrogen; expanding scCellFie inference to cycle-resolved spatial atlases.

## Key papers

- [[atlas-scale-metabolic-activities-inferred-single]] — first systematic single-cell/spatial metabolic atlas of healthy and diseased endometrium.

## My understanding

A useful first map of endometrial metabolic biology at cell-type resolution. The endometriosis-uM1/methylglyoxal and EEC-local-estrogen findings are the most actionable hypotheses; both warrant orthogonal validation (metabolomics, pharmacological perturbation) before therapeutic prioritization.
