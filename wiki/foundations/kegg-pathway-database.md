---
title: "KEGG — Kyoto Encyclopedia of Genes and Genomes pathway database"
slug: kegg-pathway-database
domain: bioinformatics / pathway analysis
status: mainstream
aliases:
  - "KEGG"
  - "KEGG pathway database"
  - "Kyoto Encyclopedia of Genes and Genomes"
first_introduced: "Kanehisa & Goto 2000 Nucleic Acids Res"
date_updated: 2026-05-27
source_url: "https://www.genome.jp/kegg/"
---

## Definition

KEGG is a curated database of biological pathways (metabolic, signalling, disease) with manually drawn pathway maps, defined genes, metabolites, reactions and orthology mappings (KO identifiers). KEGG pathway analysis is a standard enrichment tool for transcriptomics, proteomics and metabolomics studies — testing whether a list of altered genes/metabolites is enriched within a given pathway.

## Intuition

KEGG provides the canonical pathway-level vocabulary for "is this gene/metabolite list enriched in glycolysis / TCA / one-carbon / etc.?" It is the lingua franca of -omics pathway analysis and is built into nearly every analytical pipeline.

## Formal notation

- Pathway IDs (KEGG MAP IDs): e.g., map00010 (glycolysis), map00670 (one-carbon pool by folate), map00240 (pyrimidine metabolism), map00220 (arginine biosynthesis).
- Enrichment test: hypergeometric / Fisher's exact / over-representation test of altered features within pathway members.
- Pathway visualisation: KEGG Mapper / Pathview / MetaboAnalyst overlays.

## Key variants

- KEGG GENES / KEGG COMPOUND / KEGG REACTION / KEGG PATHWAY.
- MSEA (Metabolite Set Enrichment Analysis) — closely related pathway analysis for metabolites.
- Reactome — complementary pathway database with more granular reaction-level detail.

## Known limitations

- KEGG pathway definitions are curated and may lag recent biology.
- Over-representation tests do not account for pathway topology or directionality.
- Metabolite-to-pathway mappings can be incomplete or ambiguous (one metabolite in many pathways).

## Open problems

- Multi-omics-aware pathway analysis frameworks (joint gene + metabolite enrichment).

## Relevance to active research

Used extensively in [[papers/multi-omics-profiling-cachexia-targeted-tissues]] for metabolite-level pathway enrichment: identifies one-carbon pool by folate, pyrimidine metabolism, Gly/Ser/Thr metabolism and arginine biosynthesis as commonly upregulated across cachexia target tissues; TCA cycle, glycolysis and Ala/Asp/Glu metabolism as commonly downregulated.
