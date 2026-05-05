---
title: "HIF1α and p65 cooperate at cobound chromatin regions without strong physical interaction"
slug: hif1a-p65-cooperate-promoter-regions-without
status: supported
confidence: 0.7
tags:
  - HIF1a
  - NF-kB
  - chromatin
  - transcription-factor
  - hypoxia
domain: "molecular-biology / epigenomics"
source_papers:
  - nf-kb-tet2-promote-macrophage-reprogramming
evidence:
  - source: nf-kb-tet2-promote-macrophage-reprogramming
    type: supports
    strength: moderate
    detail: "ChIP-seq cobinding (~15% overlap of HIF1α H2 cluster with p65 peaks in mMAC1), motif co-enrichment at cobound peaks (HIF + NF-κB + AP-1 + IRF + ETS), weak Pearson correlation of binding intensities (r=0.13, P=2.5×10⁻⁴), distinct functional categories (HIF1α-only=glycolysis, p65-only=immune adhesion, cobound=LPS signaling)."
conditions: "Human M-CSF MACs at 1% O2 + LPS 48h. Conclusion 'without physical interaction' is inferential, not from co-IP."
date_proposed: 2026-05-05
date_updated: 2026-05-05
---

## Statement

In hypoxic LPS-activated MACs (mMAC1), HIF1α and p65 share occupancy at a subset of chromatin regions (~15% of HIF1α H2 cluster overlaps p65 peaks) without strong correlation of binding intensities (Pearson r=0.13). Motifs for both TFs are co-enriched at cobound peaks. The two TFs regulate functionally distinct gene programs at single-TF peaks (HIF1α-only → glycolysis; p65-only → immune adhesion) and a third axis at cobound peaks (LPS signaling). The authors infer cooperative regulation without physical complex formation.

## Evidence summary

- ChIP-seq cobinding analysis: ~15% of HIF1α H2-cluster peaks overlap p65 peaks in mMAC1 (Fig. 4B).
- Motif analysis at cobound peaks: HIF, NF-κB, AP-1, IRF, ETS motifs all enriched (Fig. 4C).
- HIF1α-centered analysis: HIF1α motif dominant, p65 motif weaker; p65-centered: both motifs equal (Fig. 4D).
- Pearson correlation of HIF1α and p65 binding intensities at cobound peaks: r=0.13, P=2.5×10⁻⁴ (Fig. 4F).
- GO functional separation by binding pattern (Fig. 4G).
- Time-resolved Western blot suggests HIF1α stabilizes earlier than nuclear p65 in iMAC1 (Fig. 3A-C).

## Conditions and scope

- Human M-CSF MACs in vitro, 1% O₂, LPS 48 h.
- Conclusion of "cooperation without physical interaction" rests on the low correlation alone; co-IP/proximity-ligation experiments not performed.

## Counter-evidence

- Other systems have reported direct HIF1α-NF-κB physical interaction (e.g., in cancer cells); cell-type specificity of the present finding is not established.
- Low Pearson correlation does not exclude non-linear or switch-like interaction modes.

## Linked ideas

(none yet)

## Open questions

- Is the cooperation switch-like (one TF licenses the other) rather than continuous?
- Do other hypoxic TFs (HIF2α) participate in the cobinding pattern?
- Is the cooperation conserved at C2 demethylated CpGs specifically, or distributed across regulatory elements?
