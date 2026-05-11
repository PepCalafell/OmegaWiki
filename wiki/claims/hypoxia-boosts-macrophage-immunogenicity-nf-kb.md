---
title: "Hypoxia boosts macrophage immunogenicity via NF-κB-driven epigenetic reprogramming, contradicting the dominant TME suppression paradigm"
slug: hypoxia-boosts-macrophage-immunogenicity-nf-kb
status: supported
confidence: 0.85
tags:
  - hypoxia
  - macrophage
  - NF-kB
  - immunogenicity
  - paradigm-challenge
  - tumor-microenvironment
domain: "immunology"
source_papers:
  - nf-kb-tet2-promote-macrophage-reprogramming
evidence:
  - source: nf-kb-tet2-promote-macrophage-reprogramming
    type: supports
    strength: strong
    detail: "M-CSF MACs differentiated and LPS-activated at 1% O2 (mMAC1) display: increased IL-6/TNF-α secretion; increased HLA-DR/CD80/CD86; decreased IL-10/CD14/CD206/CD163; decreased CD8+ T-cell suppression in coculture. Mechanism: NF-κB-driven C2 cluster (403 CpGs) hypomethylation overrides hypoxic TET inhibition at proinflammatory enhancers. In vivo correlates (IL4I1 MAC, IL1B Mo, ISG Mo) enrich in immune-hot tumors with better OS."
conditions: "Human peripheral blood monocyte-derived M-CSF MACs, 5d differentiation in 1% vs 21% O2, ± LPS 48h. Bladder/ovarian carcinoma in vivo validation. Generalizes to other NF-κB-activating PAMPs (P3C, CpG, polyI:C) and cytokines (TNF-α, IL-1β) but not yet tested in GM-CSF MACs or tissue-resident MACs."
date_proposed: 2026-05-05
date_updated: 2026-05-11
---

## Statement

Contrary to the dominant TME paradigm in which hypoxia universally drives macrophage immunosuppression, low oxygen (1%) *enhances* the immunogenic features of M-CSF-derived macrophages — when paired with NF-κB-activating stimulation. The mechanism is a focal NF-κB-driven DNA demethylation of proinflammatory enhancers (cluster C2, 403 CpGs) that overrides global hypoxic TET inhibition.

## Evidence summary

- Functional: increased IL-6/TNF-α, decreased IL-10, increased HLA-DR/CD80/CD86, decreased CD14/CD163/CD206, decreased T-cell suppression in mMAC1 vs mMAC21 (Calafell et al. 2024, Fig. 1B-D).
- Epigenetic: NF-κB-motif-enriched C2 cluster hypomethylates specifically in mMAC1; p65 ChIP-seq peaks colocalize with C2 (Fisher P = 8.3×10⁻¹⁰³).
- Pharmacological: BAY11-7082 (p65 inhibitor) blocks C2 demethylation; PX-478 (HIF1α inhibitor) does not; 4-octyl itaconate (TET2 inhibitor) phenocopies hypoxia inhibition.
- In vivo: mMAC1 signature enriched in MoMac-VERSE IL4I1/IL1B/ISG clusters; IL4I1 MACs sorted from primary OC recapitulate C2 hypomethylation.
- Clinical: mMAC1 signature associates with better OS in 10/12 TCGA cancer types; BLCA HR = 0.491 (P = 0.003).

## Conditions and scope

Applies to:
- Monocyte-derived (PB-MO) M-CSF MACs under static 1% O₂ + LPS or other NF-κB stimuli.
- Bladder urothelial carcinoma and ovarian carcinoma (validated cohorts).

Does NOT apply (or untested):
- GM-CSF-derived MACs.
- Tissue-resident embryonic MACs (microglia, Kupffer, LCs).
- Cyclic hypoxia / H-R cycles (only static 1% tested).
- Resting hypoxic MACs (iMAC1) which paradoxically down-regulate p65-bound genes.

## Counter-evidence

- Prior literature (Mantovani, Murray, Sica & others; reviewed in Bai 2022) frames hypoxic TAMs as immunosuppressive — but mostly from in vivo TME studies where MAC ontogeny, activation state, and cyclic hypoxia confound. The mMAC1 result is consistent with a *subset* of TAMs (IL4I1+) rather than the bulk TAM population.
- Thienpont 2016 (Nature): tumor hypoxia → DNA hypermethylation via TET inhibition. Calafell 2024 *extends* rather than contradicts — TET inhibition holds globally; NF-κB carves out a focal exception.

## Linked ideas

- HypoxiaVERSE: hypoxia is not a single binary axis; activation state is a critical co-axis.
- Therapeutic exploitation: can mMAC1 / IL4I1 MAC be expanded or induced in vivo to improve ICI response?

## Open questions

- Causal vs correlational role of mMAC1 in TME immune-hot phenotype and improved OS.
- Whether GM-CSF or tissue-resident MACs reproduce the phenotype.
- Whether cyclic hypoxia (H-R cycles) reverses or amplifies the effect.
- Stability of the C2 hypomethylation upon re-oxygenation.
