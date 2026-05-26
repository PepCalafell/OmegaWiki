---
title: "Chromatin regulators HMGA1, HP1BP3, and macroH2A1 (H2AFY) decrease during early HSC differentiation — visible on protein but weak or absent on mRNA"
slug: chromatin-regulators-decrease-on-protein-during-hsc-differentiation
status: supported
confidence: 0.85
tags: [HSC, chromatin, HMGA1, HP1BP3, macroH2A1, H2AFY, H1F0, mechanistic, mRNA-protein-discordance]
domain: hematopoiesis / chromatin biology
source_papers:
  - mapping-early-human-blood-cell-differentiation
evidence:
  - source: mapping-early-human-blood-cell-differentiation
    type: supports
    strength: strong
    detail: "Quote (p.6): 'many proteins involved in chromatin structure among HSC-correlating factors, including the previously mentioned H1 linker histone H1F0, the H1-like protein HP1BP3, which is required for HSC self-renewal (67), the histone macroH2A1 (H2AFY), associated with HSC homeo-stasis (68), and the chromatin regulator HMGA1, important for HSC regenerative capacity (69). Again, the decrease of these chromatin regulators during early HSC differentiation was better described via scp-MS.'"
conditions: "HSC subset trajectory analysis; correlation of protein vs mRNA abundance with pseudotime."
date_proposed: 2026-05-26
date_updated: 2026-05-26
---

## Statement

Multiple chromatin regulators known to govern HSC self-renewal and homeostasis decrease in protein abundance during early HSC differentiation — but this signal is captured by scp-MS, not by scRNA-seq, illustrating mRNA-protein discordance for chromatin regulators specifically.

## Evidence summary

Per-gene mRNA vs protein correlation with pseudotime in the HSC subset. Reported in [[papers/mapping-early-human-blood-cell-differentiation]] (Fig. 5B, fig. S13-S17).

## Conditions and scope

Healthy adult human BM CD34+ HSPCs; HSC subset only.

## Counter-evidence

None within scope.

## Linked ideas

## Open questions

- Mechanism: are these proteins translationally regulated, degradation-protected, or co-stabilized in chromatin complexes?
