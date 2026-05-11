---
title: "Hypoxic LPS-activated macrophages secrete more IL-6 and TNF-α and less IL-10 than normoxic counterparts"
slug: hypoxia-enhances-proinflammatory-cytokine-secretion-macrophages
status: supported
confidence: 0.9
tags:
  - hypoxia
  - macrophage
  - IL-6
  - TNF-alpha
  - IL-10
  - cytokine-secretion
  - LPS
domain: "immunology"
source_papers:
  - nf-kb-tet2-promote-macrophage-reprogramming
evidence:
  - source: nf-kb-tet2-promote-macrophage-reprogramming
    type: supports
    strength: strong
    detail: "ELISA on cell-culture supernatants from M-CSF MACs differentiated 5d in 1% vs 21% O2 ± LPS 48h (n=4). mMAC1 shows significantly higher IL-6 and TNF-α (Fig. 1B, P<0.05) and lower IL-10 than mMAC21. Mechanistically tied to NF-κB-driven C2 cluster hypomethylation of IL6 and TNF loci."
conditions: "Human PB-MO-derived M-CSF MACs; 1% vs 21% O2 differentiation; 48h LPS activation. n=4 biological replicates."
date_proposed: 2026-05-05
date_updated: 2026-05-11
---

## Statement

Macrophages differentiated and LPS-activated under hypoxia (mMAC1) secrete higher levels of the proinflammatory cytokines IL-6 and TNF-α, and lower levels of the anti-inflammatory cytokine IL-10, compared to their normoxic counterparts (mMAC21). This is one of the functional anchors of the hypoxic immunogenic phenotype.

## Evidence summary

- ELISA quantification of IL-6, TNF-α, IL-10 in cell-culture supernatants (Calafell 2024 Fig. 1B, n=4).
- The IL6 and TNF loci specifically show C2 cluster hypomethylation in mMAC1 (Fig. 1F, fig. S1C), providing an epigenetic basis.
- Consistent with the NF-κB-driven proinflammatory program (cluster E2, GO: response to LPS/TNF/IL-1, positive regulation of NF-κB).

## Conditions and scope

- Human peripheral blood monocyte M-CSF MACs.
- 1% O₂ static hypoxia + LPS (48h).
- Bulk supernatant cytokine measurement (not single-cell secretion).

## Counter-evidence

- Other in vivo hypoxic TAM studies report mixed IL-10 patterns (e.g., increased IL-10 in some MoMac-VERSE clusters), but those studies use different MAC ontogeny and chronic hypoxia.

## Linked ideas

- Direct functional readout for HypoxiaVERSE mMAC1 phenotype.
- Candidate biomarker for monitoring mMAC1 induction in clinical settings.

## Open questions

- Single-cell secretion dynamics (do all mMAC1 cells secrete more, or is it a subpopulation?).
- Whether the cytokine shift is causally tied to C2 demethylation or runs in parallel.
- Persistence after re-oxygenation.
