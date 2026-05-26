---
title: "MeDIP — methylated DNA immunoprecipitation"
slug: medip-methylated-dna-immunoprecipitation
domain: method / epigenomics
status: mainstream
aliases:
  - "MeDIP"
  - "methylated DNA immunoprecipitation"
  - "5-methylcytosine ChIP"
  - "MeDIP-qPCR"
  - "MeDIP-seq"
  - "5mC IP"
  - "anti-5mC immunoprecipitation"
first_introduced: "Weber 2005 Nat Genet"
date_updated: 2026-05-26
source_url: ""
---

## Definition

MeDIP is an affinity-enrichment method for methylated DNA using anti-5-methylcytosine antibodies to immunoprecipitate fragments carrying 5mC marks. Followed by qPCR (MeDIP-qPCR) at candidate loci or sequencing (MeDIP-seq) for genome-wide coverage. Provides a methylation enrichment readout without bisulfite conversion, complementary to EPIC arrays and WGBS.

## Formal notation

- Input: sheared genomic DNA (200-500 bp fragments)
- Capture: anti-5mC antibody (commercial, multiple clones)
- Readout: qPCR fold-enrichment vs IgG control at candidate loci; or NGS library prep for genome-wide
- Validation: positive controls at imprinted loci (H19, IGF2); negative at housekeeping promoters
- Caveats: antibody bias toward CpG-dense regions; lower resolution than bisulfite methods

## Variants

- hMeDIP — hydroxymethyl-cytosine (5hmC) IP
- MBD-seq — methyl-CpG-binding protein enrichment alternative
- MeDIP-seq vs WGBS — enrichment-based vs base-resolution

## Known limitations

- Bias toward CpG-dense regions
- Low resolution (~150-bp fragments)
- Quantitative comparison across samples requires careful normalization

## Open problems

- Standardization across antibody lots

## Relevance to active research

Used in [[papers/macrophages-use-apoptotic-cell-derived-methionine]] (Ampomah 2022 *Nat Metab*) to demonstrate AC-induced 5mC enrichment at the CpG-rich Dusp4 promoter in WT macrophages and its abolition in DNMT3A-KO macrophages — direct evidence for DNMT3A targeting Dusp4 in efferocytosis.
