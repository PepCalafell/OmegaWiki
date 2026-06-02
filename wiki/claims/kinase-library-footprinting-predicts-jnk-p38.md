---
title: "Kinase-footprint inference recovers JNK and p38 as top upstream kinases of M1 macrophages"
slug: kinase-library-footprinting-predicts-jnk-p38
status: supported
confidence: 0.85
tags:
  - macrophage
  - kinase
  - footprinting
  - methods
domain: immunology
source_papers:
  - delineation-signaling-routes-underlie-differences-macrophage
evidence:
  - source: delineation-signaling-routes-underlie-differences-macrophage
    type: supports
    strength: strong
    detail: "Kinase Library footprinting predicted JNK1/2/3 and p38 as top M1 upstream kinases (FDR < 0.1), recapitulating known M1 signal-transduction routes purely from phosphosite sequences."
conditions: "Phosphoproteomics + Kinase Library / NetPhorest / KEA3 inference; in vitro macrophages."
date_proposed: 2026-06-02
date_updated: 2026-06-02
---

## Statement
Motif-based kinase-footprint inference, applied to M1 macrophage phosphoproteomes, recovers the proinflammatory JUN N-terminal kinases (JNK1/2/3) and p38 MAPK as top upstream kinases — validating the footprinting approach against known M1 biology.

## Evidence summary
- "This analysis indicated proinflammatory JUN N-terminal kinases (JNK) 1, JNK2, and JNK3, together with p38 mitogen-activated kinases, as major regulators of the phosphoproteome changes in the M1 macrophages ... FDR < 0.1. Thus, the Kinase Library analysis, even though based solely on phosphopeptide sequences, correctly predicted known major signal transduction routes in the M1 state" (p.12).
- NetPhorest independently recapitulated high p38-family activity in M1 (p.12).

## Conditions and scope
Demonstrates method validity (positive control) before nominating novel kinases; in vitro macrophages.

## Counter-evidence
None within the paper.

## Linked ideas

## Open questions
How well does footprinting generalize to immunosuppressive states where ground-truth kinase wiring is sparse?
