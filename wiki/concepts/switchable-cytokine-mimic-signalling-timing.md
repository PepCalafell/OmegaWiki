---
title: "Switchable cytokine mimic for temporal control of signalling (ASNeo2)"
aliases:
  - "switchable IL-2 mimic"
  - "ASNeo2"
  - "switchable cytokine"
tags:
  - cytokine-engineering
  - IL-2
  - signalling-dynamics
  - protein-design
  - T-cell
  - immunology
maturity: emerging
key_papers:
  - design-facilitated-dissociation-enables-timing-cytokine
first_introduced: "Broerman et al. 2025, Nature"
date_updated: 2026-06-10
related_concepts:
  - facilitated-dissociation-effector-induced
  - mmp14-protease-activated-il2-prodrug
  - trans-acting-immunocytokine
---

## Definition

A designed cytokine agonist whose signalling can be switched off within seconds by adding a small effector, by coupling the cytokine's receptor-engaging module to a facilitated-dissociation switch. ASNeo2 fuses the de novo IL-2 mimic Neo2 to a designed hinge switch so that, on effector binding, the switch sterically clashes with the common gamma chain (γc), driving rapid dissociation of γc from the active IL-2Rβγc signalling complex — providing the "off-switch" that natural IL-2 signalling lacks.

## Intuition

Natural IL-2 signalling terminates only slowly (complex internalization/degradation over hours), so one cannot ask "what does 5 minutes of IL-2 signalling do?". A switchable cytokine gives an external knob to start and stop signalling on a seconds timescale, turning ligand residence time into an experimental variable and a potential therapeutic safety feature.

## Formal notation

ASNeo2 (Neo2–switch fusion) + IL-2Rβ + γc → active βγc complex → JAK1/3 → pSTAT5.
+ effector → state Y clash with γc → koff,γc accelerated up to 1,500-fold (5,700-fold for an optimized degradation-safeguarded variant) → signalling stops.

## Variants

- ASNeo2 (base switchable IL-2 mimic, ~1,500-fold γc off-rate acceleration).
- Degradation-safeguarded topological variants (one reaching 5,700-fold — the highest fold-change among all designed systems in the paper).

## Comparison

Versus other engineered cytokine-safety strategies in the vault — [[mmp14-protease-activated-il2-prodrug]] (TME-restricted unmasking, spatial control) and [[trans-acting-immunocytokine]] / [[myeloid-targeted-immunocytokine-mite]] (cell-targeted delivery): those control *where* a cytokine is active, whereas the switchable mimic controls *when/how long* it is active, with seconds-scale temporal resolution and an explicit external off-switch.

## When to use

To dissect the temporal dynamics of cytokine signalling (early events, residence-time dependence), or for therapeutic schemes where systemic effector deactivates any cytokine escaping the administration site.

## Known limitations

- Demonstrated in vitro and in cultured/primary human cells; in vivo pharmacology and immunogenicity untested.
- Requires co-administration of the effector to switch off.

## Open problems

- Whether disrupting signalling at the cell surface vs endosome yields distinct cellular responses.
- Translating seconds-scale control to therapeutic timing of immune activation.

## Key papers

- [[design-facilitated-dissociation-enables-timing-cytokine]] — builds ASNeo2 and uses it to show that sustained IL-2 signalling is required for proliferation while brief transient signalling suffices for apoptosis protection, with distinct transcriptional programs.

## My understanding

This is the immunology payoff of the whole design platform: a cytokine you can switch off in seconds lets you separate "sustained" from "transient" IL-2 signalling and read out divergent fates (proliferation needs duration; survival/BCL2 needs only a brief pulse). It is conceptually orthogonal to spatial cytokine-restriction strategies already in the vault — temporal rather than spatial control.
