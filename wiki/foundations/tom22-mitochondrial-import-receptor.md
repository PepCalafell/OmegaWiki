---
title: "TOM22 / TOM complex — translocase of the outer mitochondrial membrane"
slug: tom22-mitochondrial-import-receptor
domain: "cell biology / mitochondrial protein import"
status: mainstream
aliases:
  - TOM22
  - "TOM complex"
  - "translocase of the outer membrane"
  - TOMM22
  - "TOM20/22/70"
  - "mitochondrial import receptor"
first_introduced: "TOM complex characterized in yeast and mammals 1990s (Pfanner, Neupert labs)"
date_updated: 2026-05-28
source_url: "https://www.ncbi.nlm.nih.gov/gene/56993"
---

## Definition

The TOM (translocase of the outer membrane) complex is the main gateway for nuclear-encoded proteins entering the mitochondria. Its receptor subunits TOM20, TOM22, and TOM70 recognize mitochondrial targeting signals — typically N-terminal amphipathic helices rich in positively charged residues — and hand precursors to the TOM40 import channel. TOM22 is a central receptor and organizer of the complex, recognizing presequences via both its cytosolic and intermembrane-space domains.

## Intuition

TOM is the front door of the mitochondrion, and TOM22 is the doorman that reads a protein's "mitochondrial address" (a positively charged helix). Proteins not normally destined for mitochondria can sneak in if they expose such a helix. In [[papers/mitochondrial-vhl-rewires-cell-metabolism-hypoxia]], hypoxia exposes helical positive residues on VHL that TOM22 recognizes, importing VHL into the mitochondria.

## Formal notation

- Receptors: TOM20 (presequence recognition), TOM22 (central receptor/organizer), TOM70 (carrier/hydrophobic precursors).
- Channel: TOM40 β-barrel; small subunits TOM5/6/7.
- Substrate signal: N-terminal positively charged amphipathic helix (mitochondrial targeting sequence, MTS).
- VHL α-domain helices 1–2 carry positive residues recognized by TOM22; mutating them (VHL M1/M2) blocks import.

## Key variants

- TOM20 vs TOM22 vs TOM70 receptor specificity.
- N-MTS fusion: appending a canonical N-terminal MTS forces a cargo into mitochondria (used as a gain-of-function tool).

## Known limitations

- Import competence depends on precursor folding state and chaperones; in vitro reconstitution may not capture cytosolic competition.
- Receptor redundancy complicates loss-of-function interpretation.

## Open problems

- How non-canonical, signal-less proteins exploit TOM receptors under stress.
- Whether competitive import (VHL complex assembly vs TOM22 binding) is a general regulatory switch.

## Relevance to active research

TOM22-mediated import is the entry mechanism for non-canonical mitochondrial VHL under hypoxia in [[papers/mitochondrial-vhl-rewires-cell-metabolism-hypoxia]]; competition between the cytosolic VHL (VBC) complex and TOM22 binding determines VHL's fate (degradation vs mitochondrial import). See [[concepts/mitochondrial-vhl-noncanonical-hypoxia-function]].
