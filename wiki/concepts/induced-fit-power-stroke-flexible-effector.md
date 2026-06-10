---
title: "Induced-fit power stroke via flexible effector"
aliases:
  - "induced-fit power stroke"
  - "flexible-effector power stroke"
  - "fold-upon-binding driven switching"
tags:
  - protein-design
  - induced-fit
  - power-stroke
  - intrinsically-disordered
  - conformational-change
maturity: emerging
key_papers:
  - design-facilitated-dissociation-enables-timing-cytokine
first_introduced: "Broerman et al. 2025, Nature"
date_updated: 2026-06-10
related_concepts:
  - facilitated-dissociation-effector-induced
  - designed-protein-excited-states-kinetic-control
---

## Definition

A mechanism by which an intrinsically disordered (flexible) effector peptide weakly engages a conformational switch in its starting state (X), then folds and forms more extensive interactions as the switch transitions to the strained state (Y), thereby driving the conformational change against a resisting (strain-generating) force — analogous to the power strokes of motor proteins. The energy released by folding-upon-binding compensates the uphill steps of the transition, lowering the effective barrier.

## Intuition

A rigid effector can only dock once the switch has already opened (conformational selection), so a bound target that blocks opening makes binding slow. A flexible effector can grab the closed state first and then "pull" the switch open as it folds — an induced-fit power stroke — so it switches faster even though, counter-intuitively, it binds less tightly than the rigid version.

## Formal notation

Conformational selection (rigid 3hb effector): THX ⇌ THY, then E binds only THY; THX→THY is rate-limiting (saturating apparent on-rate = kswitch).
Induced-fit (flexible peptide effector): E binds THX, then drives THX·E → THY·E; apparent on-rate increases linearly with [E], exceeding kswitch.

## Variants

- Flexible/disordered peptide effector (induced-fit, fast, lower affinity).
- Rigid structured three-helix-bundle (3hb) effector (conformational selection, slow, higher affinity).

## Comparison

Directly compared in the same designed system: the peptide and 3hb make nearly identical interfaces with AS1, but the disordered peptide accelerates both effector association and target dissociation beyond the conformational-switch rate, whereas the rigid 3hb saturates at kswitch. This isolates flexibility/folding-upon-binding as the driver — a comparison difficult to make in natural motors like kinesin.

## When to use

When a designed switch must be driven rapidly through a strained transition against a load (e.g. a bound target blocking the conformational change).

## Known limitations

- The flexible effector binds more weakly than a rigid one; very weak engagement could limit driving force.
- Requires a switch that keeps an open effector cleft throughout the transition.

## Open problems

- Quantifying how much folding energy is converted into conformational driving force.
- Designing effectors that are both fast (flexible) and high-affinity.

## Key papers

- [[design-facilitated-dissociation-enables-timing-cytokine]] — demonstrates that a flexible peptide effector yields faster facilitated dissociation than a rigid effector via an induced-fit power stroke, with kinetic evidence (linear vs hyperbolic apparent on-rate).

## My understanding

The flexible-vs-rigid comparison is the mechanistic heart of the paper: it shows experimentally that disorder + folding-upon-binding is a *feature* for fast driven motion, mirroring how induced folding underlies the kinesin power stroke, and explaining why the weaker-binding peptide outperforms the tighter-binding 3hb.
