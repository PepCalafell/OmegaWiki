---
title: "miR-210 (microRNA-210)"
slug: mir-210-mirna
domain: "molecular-biology / hypoxia / non-coding-RNA"
status: mainstream
aliases:
  - "miR-210"
  - "miR-210-3p"
  - "MIR210"
  - "hsa-miR-210"
  - "hypoxamir"
  - "hypoxia-induced microRNA"
  - "canonical hypoxia microRNA"
  - "the hypoxamir"
  - "HIF1A-target microRNA"
first_introduced: "Kulshreshtha et al. 2007 Mol Cell Biol; Camps et al. 2008 Clin Cancer Res; Huang et al. 2009 Mol Cell"
date_updated: 2026-05-06
source_url: "https://www.mirbase.org/mirna/MI0000286/"
---

## Definition

miR-210 is the canonical "hypoxamir" — the most consistently and strongly induced microRNA under hypoxia across cell types and tumor types. It is a direct HIF1A transcriptional target and is induced 5–50-fold under low oxygen. Its mature form (miR-210-3p) targets transcripts in the mitochondrial electron transport chain (ISCU, COX10, SDHD), DNA-damage response (RAD52), and cell-cycle regulation, contributing to the metabolic remodelling of hypoxic cells.

## Intuition

If a single molecular feature were to be picked as "you have been in hypoxia recently," it would be miR-210 abundance. It is the most reproducible hypoxia-induction marker across studies and tissues, and its induction is *near-universal* across tumor types — confirmed in 18 of 19 tumor types in the Bhandari pancancer landscape ([[papers/molecular-landmarks-tumor-hypoxia-across-cancer]]).

## Formal notation

- Encoded by MIR210 (chr11p15.5 in human)
- Mature -3p strand is the dominant functional product
- Pri-miR-210 transcribed by RNA Pol II → Drosha-DGCR8 → pre-miR-210 → Dicer → mature 22-nt miR-210-3p
- HIF1A binds the MIR210 promoter HRE
- Major validated targets:
  - ISCU (iron-sulfur cluster scaffold) — represses electron transport
  - COX10 (heme A:farnesyltransferase) — Complex IV biogenesis
  - SDHD (succinate dehydrogenase D) — Complex II
  - RAD52 — DNA damage response

## Key variants

- miR-210-5p (passenger strand) — minor expression, distinct targets
- Genomic neighbors: miR-210 host gene MIR210HG is itself hypoxia-induced

## Known limitations

- Plasma circulating miR-210 has been proposed as a non-invasive hypoxia biomarker but assay variability is high.
- Bulk-tumor miR-210 mixes malignant and stromal contributions.

## Open problems

- The directionality of miR-210 effects is context-dependent (pro-survival in mild hypoxia vs pro-apoptotic in severe hypoxia + reoxygenation).
- Whether miR-210-mediated mitochondrial repression *causes* the Warburg-like glycolytic shift or merely amplifies a HIF1A-driven program is debated.

## Relevance to active research

In [[papers/molecular-landmarks-tumor-hypoxia-across-cancer]], miR-210 is positively associated with hypoxia score in 18 of 19 tumor types (Spearman ρ range 0.20–0.66) — the most universal pancancer hypoxia-miRNA correlate. miR-210 abundance correlates with LDHA protein abundance in BRCA (ρ=0.72) and OV (ρ=0.42), bridging the miRNA layer to HIF1A-driven glycolysis.
