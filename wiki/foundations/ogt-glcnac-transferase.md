---
title: "OGT — O-GlcNAc transferase"
slug: ogt-glcnac-transferase
domain: "cell biology / glycobiology"
status: mainstream
aliases:
  - OGT
  - O-GlcNAc transferase
  - O-linked N-acetylglucosamine transferase
  - UDP-N-acetylglucosamine—peptide N-acetylglucosaminyltransferase
first_introduced: ""
date_updated: 2026-06-02
source_url: "https://www.uniprot.org/uniprotkb/O15294"
---

## Definition

OGT (O-GlcNAc transferase) is the single enzyme that catalyses O-GlcNAcylation — the addition of a single N-acetylglucosamine (GlcNAc) moiety via an O-linkage to serine and threonine residues of nuclear, cytoplasmic, and mitochondrial proteins. It uses the metabolite [[foundations/udp-glcnac-uridine-diphosphate-acetylglucosamine]] as its sugar donor.

## Intuition

OGT is the "writer" of the [[foundations/glcnacylation]] mark; the hydrolase OGA ("O-GlcNAcase") removes it. Because the donor substrate UDP-GlcNAc is the end product of the hexosamine biosynthetic pathway (rate-limited by [[foundations/gfpt1-gfat1-glutamine-fructose-aminotransferase]]), OGT activity couples nutrient flux (glucose, glutamine, acetyl-CoA, UTP) to protein post-translational modification — making O-GlcNAcylation a nutrient-sensing rheostat.

## Formal notation

protein-Ser/Thr-OH + UDP-GlcNAc → protein-Ser/Thr-O-GlcNAc + UDP (OGT-catalysed).

## Key variants

- Three OGT isoforms (nucleocytoplasmic ncOGT, mitochondrial mOGT, short sOGT) arising from alternative splicing.
- Conditional deletion via [[foundations/lysm-cre]] (Lyz2-Cre, "Lyz2ΔOgt") yields myeloid/macrophage-specific loss of O-GlcNAcylation.

## Known limitations

- A single essential gene with thousands of substrates; clean attribution of a phenotype to one O-GlcNAcylated target is difficult.
- Pharmacological OGT inhibitors (e.g. OSMI-1, ST045849) have off-target and viability concerns at high doses.

## Open problems

- Which specific O-GlcNAcylated substrates drive macrophage cell-cycle and residency phenotypes versus bulk modification.

## Relevance to active research

Central enzyme in [[papers/glcnacylation-shapes-macrophage-tissue-residency-alternative]]: macrophage-specific Ogt deletion abolishes IL-4-driven alternative activation and tissue-resident macrophage maintenance, positioning OGT as a metabolic regulator of the macrophage cell cycle.
