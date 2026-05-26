---
title: "TFBS weavability (k-mer connectivity property of TF binding sites)"
aliases:
  - "TFBS weavability"
  - "weavability of TF binding sites"
  - "k-mer connectivity TFBS"
  - "binding site network connectivity"
  - "(k-1)-overlap graph TFBS"
  - "TFBS network giant component"
  - "weavable TFBS"
  - "binding-site graph connectivity"
  - "Khetan weavability"
tags:
  - transcription-factor
  - DNA-binding
  - graph-theory
  - binding-site-architecture
maturity: emerging
key_papers:
  - multiple-overlapping-binding-sites-determine-transcription
first_introduced: "Khetan, Carroll & Bulyk 2025 Nature"
date_updated: 2026-05-26
related_concepts:
  - overlapping-binding-sites-model
  - padit-seq
---

## Definition

TFBS weavability is the property that, for a given TF, the set of its active k-mers forms a densely connected graph in which nodes are k-mers and edges denote (k-1)-bp sequence overlap. A high-weavability TF has a single giant connected component containing > 80% of its active k-mers, meaning that almost any active k-mer can be reached from any other by a chain of 1-bp shifts. Random k-mer sets do not show this property.

## Intuition

If high-affinity k-mers tend to be flanked by nucleotides that yield additional active (lower-affinity) k-mers, the TF's "binding vocabulary" is internally connected — extended recognition sequences can be assembled by chaining overlapping active k-mers. The Khetan 2025 paper shows this is true for HOXD13 (97.5% of nodes in giant component), for the other five PADIT-seq TFs, and for 199/200 TFs in UniPROBE across 9 DBD families.

## Formal notation

- Graph G_TF = (V, E) where V = active k-mers + reverse complements; E = (k-1)-bp overlap edges
- Weavability metric: |V_largest_CC| / |V|
- Significance: empirical p < 0.001 vs 1,000 size-matched random k-mer networks
- High-affinity nodes also have higher degree (intra-graph hubs)

## Variants

- Strict (top N=500 8-mers from uPBM E-scores)
- Active-set (PADIT-seq active k-mers + reverse complements)
- Cross-family panel (200 TFs across 9 DBD classes in UniPROBE)

## Comparison

vs random k-mer set: random sets show < 1% in largest component
vs cooperativity models: weavability is sequence-intrinsic; cooperativity requires protein-protein contacts
vs PWM information content: weavability is orthogonal to PWM information content — it is about the lattice of allowed k-mers, not their motif compactness

## When to use

- Predicting whether a TF will obey the overlapping-binding-sites model (high weavability → yes)
- Designing synthetic TFBS-rich sequences that "weave" overlapping active sites
- Anticipating which TFs are most vulnerable to multi-site noncoding variants

## Known limitations

- Measured for 200 human/mouse TFs; prokaryotic TFs untested
- The threshold for "active" depends on the affinity assay; comparing weavability across assays is non-trivial
- Functional consequences (cellular gene expression) for low-weavability TFs untested

## Open problems

- Why does weavability arise — selection, biophysics of the DBD, or both?
- Does weavability predict TF dosage robustness or cofactor independence?
- Is weavability altered in TFs with paralog-divergent specificity?

## Relevance to active research

Introduced in [[papers/multiple-overlapping-binding-sites-determine-transcription]] as the structural property underlying the [[overlapping-binding-sites-model]] — the fact that 199/200 surveyed TFs in UniPROBE are weavable suggests the model is a general feature of eukaryotic TF–DNA interactions.
