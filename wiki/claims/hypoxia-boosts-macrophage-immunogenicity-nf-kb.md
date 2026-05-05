---
title: "Hypoxia boosts macrophage immunogenicity via NF-κB-driven, TET-dependent demethylation"
slug: hypoxia-boosts-macrophage-immunogenicity-nf-kb
status: supported
confidence: 0.85
tags:
  - hypoxia
  - macrophage
  - NF-kB
  - TET
  - epigenetics
  - tumor-microenvironment
domain: "immunology / epigenetics"
source_papers:
  - nf-kb-tet2-promote-macrophage-reprogramming
evidence:
  - source: nf-kb-tet2-promote-macrophage-reprogramming
    type: supports
    strength: strong
    detail: "Multi-modal evidence (cytokine secretion, surface markers, T-cell suppression, EPIC array C2 demethylation, ChIP-seq p65 binding, BAY11-7082 rescue, 4-octyl itaconate dependence, MoMac-VERSE in vivo correlate, TCGA survival)"
conditions: "Human monocyte-derived M-CSF MACs, 1% O2 vs 21% O2, ± LPS 48h. May not generalize to GM-CSF MACs or tissue-resident MACs."
date_proposed: 2026-05-05
date_updated: 2026-05-05
---

## Statement

Under hypoxia, NF-κB (p65/RELA) drives focal, TET-dependent DNA demethylation at proinflammatory enhancer regions (cluster C2), overriding the global hypoxic suppression of TET activity, and producing a hyperinflammatory MAC state (mMAC1) with enhanced antigen presentation, cytokine secretion, and reduced T-cell-suppressive capacity.

## Evidence summary

Six convergent lines from [[papers/nf-kb-tet2-promote-macrophage-reprogramming]]:

1. Functional: mMAC1 secretes more IL-6/TNF-α, less IL-10, expresses more HLA-DR/CD86/CD80, less CD14/CD206/CD163, fails to suppress CD8⁺ T-cell proliferation.
2. Epigenomic: 403 CpGs (cluster C2) hypomethylated specifically in mMAC1, enriched for NF-κB motifs and at LPS-induced de novo enhancers.
3. Transcriptomic: RNA cluster E2 (LPS-induced, hypoxia-amplified) significantly enriched for C2-associated genes (P=3.03×10⁻⁴⁴); RELA regulon NES rises to 5 in mMAC1.
4. ChIP-seq: C2 regions exclusively associate with p65-specific peaks, not HIF1α.
5. Pharmacology: p65 inhibition (BAY11-7082) restores normoxic methylation; TET inhibition (4-octyl itaconate) blocks both demethylation and gene expression; HIF1α inhibition (PX-478) does *not* affect C2 demethylation.
6. In vivo: mMAC1 signature is recapitulated by IL4I1 MACs in MoMac-VERSE, present in human tumors, and high-mMAC1 / high-IL4I1 / low-C2-methylation patients have significantly better survival in BLCA, OC, and 7–10/12 TCGA cancers.

## Conditions and scope

- In vitro M-CSF MACs from human peripheral blood monocytes.
- Validated in vivo correlate: IL4I1 MACs from primary OC.
- TCGA correlation observed across 12 cancer types with strongest separation in BLCA.
- Does NOT necessarily extend to GM-CSF MACs, tissue-resident embryonic-origin MACs, or non-cancer hypoxia (arthritic joints, ischemic tissues).

## Counter-evidence

- Prior literature (15, 38, 52, 53) reports immunosuppressive effects of hypoxia/HIFs in MACs — context-dependent contradiction is a real caveat.
- iMAC1 (resting hypoxic) shows down-regulation of p65-bound genes, which the authors note as a possibly contradictory paradoxical state.

## Linked ideas

(none yet)

## Open questions

- TET-isoform-specific genetic perturbation needed to confirm TET2 attribution.
- Does the C2-demethylation persist (epigenetic memory) once hypoxia is relieved?
- Is the mMAC1 → T-cell crosstalk causal for the BLCA/OC survival benefit, or merely a co-marker?
