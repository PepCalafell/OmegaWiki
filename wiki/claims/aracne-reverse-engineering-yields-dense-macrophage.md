---
title: "ARACNe reverse engineering yields a dense macrophage gene interaction network (66,744 interactions)"
slug: aracne-reverse-engineering-yields-dense-macrophage
status: supported
confidence: 0.85
tags:
  - macrophage
  - network-biology
  - ARACNe
domain: methods
source_papers:
  - transcriptome-based-network-analysis-reveals-spectrum
evidence:
  - source: transcriptome-based-network-analysis-reveals-spectrum
    type: supports
    strength: strong
    detail: "ARACNe on 9,498 genes yielded 66,744 interactions (avg degree 14.7); corroborated by TINGe; top 10% hubs (869 genes) participate in 30,431 interactions."
conditions: "Mutual-information all-versus-all network, Bonferroni p<1e-7."
date_proposed: 2026-06-02
date_updated: 2026-06-02
---

## Statement
Reverse network engineering with ARACNe on the 9,498 expressed genes reconstructs a dense macrophage activation network of 66,744 interactions (average connectivity 14.7), corroborated by an independent method (TINGe).

## Evidence summary
- "We identified 66,744 interactions resulting in an average degree of connectivity of 14.7" (p.282, Figure 6B).
- "We confirmed these findings with a second RNE approach (TINGe) ... high similarity in the number of interactions, the average degree of connectivity and the rank of hubs" (p.282).
- "The top 10% of hub genes (n = 869) collectively participated in 30,431 interactions" (p.282).

## Conditions and scope
Information-theoretic inference; associative (non-causal) edges.

## Counter-evidence
None.

## Linked ideas

## Open questions
Assigning causal direction to inferred edges.
