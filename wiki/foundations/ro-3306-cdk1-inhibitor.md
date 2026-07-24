---
title: "RO-3306 — selective CDK1 inhibitor (G2/M synchronization)"
slug: ro-3306-cdk1-inhibitor
domain: "chemical biology / cell-cycle tools"
status: mainstream
aliases:
  - "RO-3306"
  - "RO3306"
first_introduced: "Vassilev et al. 2006"
date_updated: 2026-07-24
source_url: "https://pubmed.ncbi.nlm.nih.gov/16920801/"
---

## Definition

RO-3306 is a potent, ATP-competitive, selective small-molecule inhibitor of CDK1 (cyclin-dependent kinase 1). By blocking CDK1 activity it arrests cells reversibly at the G2/M boundary. Washing out the inhibitor releases cells synchronously into mitosis, making RO-3306 a standard tool for cell-cycle synchronization.

## Intuition

A reversible "pause button" at the G2/M gate: hold cells with RO-3306, then release to watch a synchronized population march through mitosis into G1 — the trick used to reveal transient, cell-cycle-restricted normoxic HIF-1α expression that is invisible in asynchronous cultures.

## Formal notation

- Target: CDK1 (Ki ≈ 20 nM); ~10-fold selectivity over CDK2
- Used at 5 µM for ~18–20 h to arrest, then PBS wash + fresh medium to release
- Molecular target: [[cdk1-cyclin-dependent-kinase-1]]

## Key variants

- Other synchronization approaches: nocodazole (M-phase), thymidine block (G1/S), serum starvation (G0)

## Known limitations

- Not perfectly CDK1-selective at high doses; can affect CDK2
- Arrest/release perturbs metabolism; synchronized cells are not fully physiological
- Releases a partially synchronous population (~60% past G1 in the source paper)

## Open problems

- Distinguishing direct CDK1-substrate effects (e.g. HIF-1α Ser668) from indirect consequences of mitotic arrest/release

## Relevance to active research

Key synchronization tool enabling detection of transient normoxic HIF-1α expression at G2/M in Huh7 and HepG2 cells. Relevant to cell-cycle and hypoxia-signaling methodology in the vault.
