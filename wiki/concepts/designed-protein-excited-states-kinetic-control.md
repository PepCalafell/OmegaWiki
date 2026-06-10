---
title: "Design of protein excited states for kinetic control"
aliases:
  - "designed excited states"
  - "strained intermediate design"
  - "excited-state protein design"
tags:
  - protein-design
  - kinetics
  - strain-energy
  - structural-frustration
  - transition-states
maturity: emerging
key_papers:
  - design-facilitated-dissociation-enables-timing-cytokine
first_introduced: "Broerman et al. 2025, Nature"
date_updated: 2026-06-10
related_concepts:
  - facilitated-dissociation-effector-induced
  - induced-fit-power-stroke-flexible-effector
---

## Definition

A design principle in which the kinetics and dynamics of a protein system are controlled by explicitly engineering high-energy, transiently-populated excited (intermediate) states — not just low-energy ground states. The strained intermediate must be sufficiently high in energy to be poorly populated at rest, yet not so high that the transition through it never occurs; its energy is tuned by controlling the magnitude and direction of the structural deformation required to resolve a designed steric clash.

## Intuition

Classical protein design optimizes ground states to be low-energy and near-ideal. But timing, switching, and motion are governed by the *barriers and intermediates* between states. To design how fast a system moves, you must design the strained states it passes through — making structural frustration a deliberate engineering target rather than a defect to be minimized.

## Formal notation

Strain (spring-model approximation): E_strain ≈ ½·k·Δx², where the effective stiffness k depends on the *direction* of deformation and Δx on its magnitude. Optimal ternary-intermediate energy lies in a window: too low → target won't dissociate; too high → facilitated pathway not faster than spontaneous. Acceleration is maximized by raising intermediate energy without making effector association rate-limiting.

## Variants

- Magnitude-tuned deformation (larger Δx).
- Direction-tuned deformation (deform along a stiffer axis → higher energy per unit Δx).
- Non-uniformly distributed strain → kinetic asymmetry between forward and reverse pathways.

## Comparison

Versus near-ideal/ground-state-only design (RosettaRemodel, parametric helical bundles, RFdiffusion): those generate stable structures but do not explicitly program traversed intermediates. This approach adds the excited state as a first-class design object, validated crystallographically here.

## When to use

When the goal is a kinetic or dynamic property — switching rate, dissociation timing, directional motion — rather than a static fold or affinity.

## Known limitations

- Strain energy is hard to predict; the paper relies on AlphaFold2 deformation predictions plus empirical screening.
- The optimal-energy window is narrow and must be found by sampling fusion geometries.

## Open problems

- A predictive, quantitative map from structure → strain energy → rate acceleration.
- Generalizing excited-state design to motors, ratchets, and multi-step machines.

## Key papers

- [[design-facilitated-dissociation-enables-timing-cytokine]] — uses designed strained ternary excited states to control facilitated-dissociation kinetics; confirms the excited states by X-ray crystallography, DEER, and MD.

## My understanding

This reframes "frustration" and "strain" — usually things designers avoid — as the levers that set kinetics. The crystallographic capture of a deliberately strained, normally-transient ternary complex is the proof-of-concept that excited states can be designed and observed, not just inferred.
