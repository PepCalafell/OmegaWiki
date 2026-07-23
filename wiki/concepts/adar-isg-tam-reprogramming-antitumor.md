---
title: "Adar-loss ISG+ TAM reprogramming for antitumor immunity"
aliases:
  - "Adar KO ISG TAM reprogramming"
  - "ISG+ TAM reprogramming via Adar inactivation"
tags:
  - TAM
  - interferon-stimulated-genes
  - ADAR
  - macrophage-immunotherapy
  - CD8-T-cell
  - anti-PD-1
maturity: emerging
key_papers:
  - functional-genetic-screens-reveal-key-pathways
first_introduced: "2025"
date_updated: 2026-07-23
related_concepts:
  - angiogenic-mhc-ii-tam-mutual-exclusivity
  - core-versus-subset-specific-isg-programs
  - lgp-factor-tam-polarization-axis
---

## Definition

Among TAM functional states, the interferon-stimulated-gene (ISG+) program — not the angiogenic or MHC-II program — correlates with effector CD8+ T-cell activity. Inactivating the RNA-editing enzyme ADAR in myeloid cells forces TAMs into this ISG+ state, expanding ISG+ TAMs, enhancing CXCL10–CXCR3 and CD40–CD40L crosstalk with T cells, reducing CD8 exhaustion, slowing tumor growth, and improving anti–PD-1 response.

## Intuition

If angiogenic and MHC-II are the two dominant poles, ISG+ is the therapeutically desirable third state. Because ADAR normally masks self-dsRNA from innate sensors, removing it makes macrophages "feel" virally infected and turn on interferon programs — a genetic lever to steer TAMs toward recruiting and reinvigorating cytotoxic T cells.

## Formal notation

Not applicable — evaluated by ISG signature scores, ISG+ TAM frequency (CD40+CD64+), CD8 effector (GZMB+) vs. exhausted (LAG3+PD-1+) fractions, and tumor-growth curves ± anti–PD-1.

## Variants

- Genetic: myeloid-specific `Adar` knockout via LSL-Cas9;Lyz2-Cre HSC transplantation.
- Pharmacologic analogue: STING agonists induce a similar ISG TAM phenotype (cited comparison).

## Comparison

Complements the [[core-versus-subset-specific-isg-programs]] concept by tying a specific upstream regulator (ADAR) to an actionable TAM-reprogramming outcome, and sits orthogonal to the [[angiogenic-mhc-ii-tam-mutual-exclusivity]] axis.

## When to use

Invoke when considering macrophage-intrinsic strategies to convert a "cold," angiogenic-TAM-dominated tumor into a T-cell-inflamed one, or to sensitise to checkpoint blockade.

## Known limitations

- Systemic ADAR loss is interferon-toxic; only myeloid-restricted loss was tested.
- Angiogenic TAMs paradoxically increased in Adar-mKO tumors (possible ISG+↔angiogenic trajectory relationship).

## Open problems

- Durability and safety of myeloid ADAR inhibition in vivo.
- Whether ISG+ reprogramming synergises with LGP-axis blockade.

## Key papers

- [[functional-genetic-screens-reveal-key-pathways]] — identifies ISG+ TAMs as the T-cell-supportive state and demonstrates Adar-loss reprogramming with anti–PD-1 synergy.

## My understanding

The correlational anchor (ISG+ TAM ↔ CD8 effector across cohorts) plus the causal intervention (Adar mKO → better antitumor immunity) is a clean bench-to-hypothesis loop; the open risk is translational safety of targeting an essential editing enzyme.
