---
title: "Effector-induced facilitated dissociation (designed)"
aliases:
  - "facilitated dissociation"
  - "induced-fit facilitated dissociation"
  - "effector-accelerated dissociation"
tags:
  - protein-design
  - binding-kinetics
  - allostery
  - conformational-switch
  - off-rate-control
maturity: emerging
key_papers:
  - design-facilitated-dissociation-enables-timing-cytokine
first_introduced: "Broerman et al. 2025, Nature"
date_updated: 2026-06-10
related_concepts:
  - designed-protein-excited-states-kinetic-control
  - induced-fit-power-stroke-flexible-effector
  - switchable-cytokine-mimic-signalling-timing
---

## Definition

Facilitated dissociation is a kinetic mechanism in which an effector molecule (E) binds a target–host (TH) complex to form a transient ternary complex (THE) from which the target dissociates much faster than it would spontaneously. This decouples the usual trade-off in binary interactions: the host can bind the target with high affinity (slow spontaneous off-rate) yet release it rapidly on demand when effector is added. In the designed version, an effector-responsive conformational switch is fused to an arbitrary binder so that, in the effector-bound state, the switch sterically clashes with the target, straining the ternary complex and allosterically driving target release.

## Intuition

Binary interactions force a choice between tight binding (slow off-rate) and fast exchange (fast off-rate). Facilitated dissociation provides a third path: keep the resting complex stable, but add an effector that pries the target loose through a strained intermediate — analogous to toehold-mediated strand displacement in DNA nanotechnology, but for proteins and couplable to biology.

## Formal notation

Mutually exclusive competition (slow): TH + E ⇌ T + HE.
Facilitated dissociation (fast): TH + E ⇌ THE → T + HE, with koff,T:HE ≫ koff,T:H.
Fold acceleration = koff (saturating, +effector) / koff (base, −effector). Observed up to 5,700-fold (ASNeo2 variant).

## Variants

- Mechanism by direct steric overlap between target and effector (most natural examples).
- Mechanism by allosteric switching of steric clashes (this paper) — modular, places no requirement on binder/target.
- Conformational-selection effector binding (rigid effector, slow) vs induced-fit effector binding (flexible effector, fast — see [[induced-fit-power-stroke-flexible-effector]]).
- Forward (effector releases target) vs reverse (target releases effector) facilitated dissociation, with tunable kinetic asymmetry.

## Comparison

Versus mutually exclusive competition: facilitated dissociation is orders of magnitude faster because it routes through a strained ternary intermediate rather than waiting for spontaneous unbinding. Versus natural facilitated-dissociation systems (NF-κB·IκBα, transcription factors on DNA, motor-protein nucleotide exchange): the designed allosteric-clash mechanism is general and modular rather than evolved for a specific pair.

## When to use

When a protein interaction must be both high-affinity (stable until needed) and rapidly reversible on a defined cue — switchable cytokines, fast biosensors, kinetically triggered circuits, reversible split enzymes.

## Known limitations

- Requires tuning the ternary-complex strain energy into a narrow optimal window (see [[designed-protein-excited-states-kinetic-control]]).
- Base off-rate is somewhat increased by residual strain in the target–host complex (e.g. 20-fold for AS1).
- Needs a designed effector-responsive switch fused at an appropriate geometry.

## Open problems

- Predicting strain energy and dissociation acceleration directly from structure.
- Chaining many orthogonal facilitated-dissociation modules into complex protein logic.
- In vivo deployment (immunogenicity, pharmacokinetics of effector + host).

## Key papers

- [[design-facilitated-dissociation-enables-timing-cytokine]] — introduces the general design approach and demonstrates biosensors, circuits, split-enzyme breaking, and a switchable IL-2 mimic.

## My understanding

The core insight is treating the strained ternary complex as a *designed excited state* whose energy is an engineering knob. Because the mechanism is allosteric (switching clashes) rather than requiring the effector to overlap the target epitope, almost any binder can be retrofitted with a fast, effector-triggered off-switch — which is what makes ASNeo2 (seconds-scale IL-2 off-switch) possible.
