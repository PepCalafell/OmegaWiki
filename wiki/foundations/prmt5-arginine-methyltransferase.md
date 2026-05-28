---
title: "PRMT5 — protein arginine methyltransferase 5"
slug: prmt5-arginine-methyltransferase
domain: "molecular biology / post-translational modification / epigenetics"
status: mainstream
aliases:
  - PRMT5
  - "protein arginine methyltransferase 5"
  - "type II PRMT"
  - "symmetric dimethylarginine methyltransferase"
first_introduced: "PRMT5 identified 1999 (Pollack et al., as JBP1); type II arginine methyltransferase activity characterized early 2000s"
date_updated: 2026-05-28
source_url: "https://www.ncbi.nlm.nih.gov/gene/10419"
---

## Definition

PRMT5 is the major type II protein arginine methyltransferase, catalyzing symmetric dimethylation of arginine residues (sDMA) on histone and non-histone substrates using S-adenosylmethionine (SAM) as the methyl donor. It functions in a complex with MEP50/WDR77 and regulates splicing, transcription, DNA damage response, and metabolism. PRMT5 is a prominent cancer target, especially in MTAP-deleted tumors where accumulated MTA partially inhibits PRMT5, creating a synthetic-lethal vulnerability.

## Intuition

PRMT5 stamps a symmetric dimethyl mark on arginines that changes how partner proteins read or bind the substrate. In [[papers/mitochondrial-vhl-rewires-cell-metabolism-hypoxia]], PRMT5 dimethylates MCCC2 at R292; this methyl-arginine blocks VHL from engaging MCCC2. Removing the mark (under hypoxia, when PRMT5 is repressed) licenses the VHL–MCCC2 interaction.

## Formal notation

- Reaction: protein-Arg + 2 SAM → protein-Arg(sDMA) + 2 SAH.
- PRMT classes: type I (PRMT1, asymmetric DMA), type II (PRMT5, symmetric DMA), type III (PRMT7, monomethyl).
- Functions in PRMT5–MEP50 octameric complex.
- Activity repressed by tyrosine phosphorylation (e.g., SRC-mediated pY283 in MCCC2-regulatory context).

## Key variants

- PRMT5 vs PRMT1 (type I) vs PRMT7 (type III) — distinguished by methyl-arginine product.
- MTAP-deletion synthetic lethality: MTA accumulation makes PRMT5 selectively druggable.

## Known limitations

- Broad substrate range makes phenotype attribution to a single methyl site difficult.
- First-generation PRMT5 inhibitors had on-target toxicity; MTA-cooperative inhibitors are newer.

## Open problems

- Full catalogue of metabolic-enzyme arginine-methylation substrates.
- How oxygen tension and tyrosine phosphorylation jointly tune PRMT5 activity in vivo.

## Relevance to active research

PRMT5-mediated MCCC2 R292 methylation is the oxygen-responsive switch that gates the VHL–MCCC2 interaction in [[papers/mitochondrial-vhl-rewires-cell-metabolism-hypoxia]], suggesting crosstalk between methionine/SAM metabolism and leucine catabolism. See [[concepts/prmt5-mccc2-arginine-methylation-oxygen-switch]].
