---
title: "Ontogeny-divergent HIF-1α function in macrophage metabolism and inflammation"
aliases:
  - "ontogeny-divergent HIF-1α macrophage"
  - "HIF-1α divergence BMDM TR-AM"
  - "macrophage ontogeny HIF dependence"
tags:
  - HIF1A
  - macrophage-ontogeny
  - BMDM
  - alveolar-macrophage
  - immunometabolism
  - tissue-residency
  - glycolysis
  - oxidative-phosphorylation
maturity: active
key_papers:
  - hif-regulates-mitochondrial-function-bone-marrow
first_introduced: "Woods et al. 2025 (Sci. Rep.) — explicit BMDM-vs-TRAM HIF-1α dissection"
date_updated: 2026-05-27
related_concepts:
  - macrophage-ontogeny-resident-vs-monocyte-derived
  - hif-dependent-glycolysis-immune-cell-differentiation
  - tissue-specific-metabolic-programming-macrophages
  - warburg-effect-hif1a-glycolytic-reprogramming
---

## Definition

The biological observation that HIF-1α — long treated as a generic master regulator of macrophage glycolytic metabolism and pro-inflammatory effector function — actually exerts highly divergent functions depending on macrophage ontogeny. In monocyte-derived macrophages (BMDMs), HIF-1α is required at baseline for glycolytic capacity, ETC-inhibitor resistance, and full pro-inflammatory cytokine output, and its loss derepresses a c-Myc–driven mitochondrial/ribosomal-biogenesis program. In long-lived tissue-resident alveolar macrophages (TR-AMs), HIF-1α is functionally silent at steady state and during LPS exposure, becoming load-bearing only under hypoxia or pharmacological PHD inhibition, where it drives a glycolytic rescue against ETC failure.

## Intuition

HIF-1α is not a context-free transcription factor — its in-vivo function is filtered through cell-type-specific chromatin and metabolic baselines. A glycolytic, monocyte-derived macrophage has wired its core program around HIF-1α; an OXPHOS-dependent, tissue-niche-shaped alveolar macrophage has decoupled from HIF-1α and only re-engages it under metabolic emergency.

## Formal notation

- **BMDMs (Hif1a⁻/⁻ baseline)**: ↓ECAR, ↓glycolytic gene/protein expression, ↑OCR, ↑TCA metabolites, ↑ETC complex protein, ↑Myc regulon, ↑ribosomal biogenesis, ↓TNFα/IL-6/IL-1β post-LPS.
- **TR-AMs (Hif1a⁻/⁻ baseline)**: ≈0 transcriptomic change (10 DEGs), no metabolic or cytokine phenotype.
- **TR-AMs (Hif1a⁻/⁻ + FG-4592)**: lost glycolytic shift, sensitised to rotenone/antimycin-induced death.
- **LPS in TR-AMs**: no HIF-1α nuclear translocation observed in this study.

## Variants

- **Postnatal HIF-1α silencing**: HIF-1α target genes are progressively suppressed during TR-AM maturation after birth (Soucek 2019), aligning with the dispensability shown here.
- **Recruited monocyte-derived alveolar macrophages**: predicted to behave BMDM-like with respect to HIF-1α; not formally tested here.

## Comparison

Contrasts with the long-standing view (built on BMDM/peritoneal-macrophage models) that HIF-1α is a universal driver of macrophage inflammation. It refines [[concepts/hif-dependent-glycolysis-immune-cell-differentiation]] by adding an ontogeny axis.

## When to use

When interpreting any HIF-1α perturbation experiment in macrophages — the same drug or knockout will yield opposite metabolic-inflammatory readouts depending on whether the cell is BMDM-like or tissue-resident-like. Especially relevant for ARDS therapy design, where TR-AM survival is desirable and recruited-macrophage activation is harmful.

## Known limitations

- Demonstrated formally only in BMDM vs alveolar TR-AM; other tissue-resident macrophages (Kupffer, microglia, peritoneal LPMs) not tested under the same paradigm.
- In-vitro inducible LysM-CreERT2 system; partial deletion possible.
- Pharmacological HIF stabilization (FG-4592) substitutes for true hypoxia.

## Open problems

- Does ontogeny-divergent HIF-1α function generalize to other tissue-resident macrophage populations (microglia, Kupffer, peritoneal, TAMs)?
- What chromatin-state difference rewires TR-AMs to be HIF-1α-independent at baseline?
- In tumor-associated macrophages of mixed ontogeny (some resident, some recruited), can HIF-targeting strategies be made ontogeny-selective?

## Key papers

- [[papers/hif-regulates-mitochondrial-function-bone-marrow]] — defining paper.
- [[papers/metabolism-tissue-macrophages-homeostasis-pathology]] — broader review of tissue-shaped metabolism.

## My understanding

This concept has immediate consequences for the hypoxia/macrophage thesis: any in-vivo HIF-1α intervention (PX-478, belzutifan, PHD inhibitors) will hit ontogenically heterogeneous macrophage pools differently — the recruited-macrophage compartment may be depressed while the resident compartment is unaffected, which could be either therapeutic (ARDS) or counter-productive (tumor settings where both compartments contribute). It also predicts that scRNA-seq-derived "HIF activity scores" should be interpreted ontogeny-by-ontogeny.
