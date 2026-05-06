---
title: "Chromothripsis under hypoxia in prostate cancer"
aliases:
  - "chromothripsis"
  - "chromothriptic event"
  - "catastrophic structural rearrangement"
  - "chromosome shattering"
  - "hypoxia-driven chromothripsis"
  - "PCa chromothripsis"
  - "hypoxic genome catastrophe"
  - "single-event massive rearrangement"
tags:
  - chromothripsis
  - hypoxia
  - structural-variants
  - genomic-instability
  - prostate-cancer
  - WGS
maturity: stable
key_papers:
  - molecular-landmarks-tumor-hypoxia-across-cancer
first_introduced: "Stephens et al. 2011 Cell (chromothripsis); Fraser et al. 2017 Nature (PCa)"
date_updated: 2026-05-06
related_concepts: []
---

## Definition

Chromothripsis is a single catastrophic event in which a localized genomic region — typically one chromosome arm or one chromosome — undergoes tens to hundreds of double-strand breaks and is religated in random order, producing a characteristic pattern of clustered structural variants with oscillating copy number across one or two ploidy states. In localized prostate cancer, hypoxia is significantly associated with elevated rates of chromothripsis (Bonferroni-adjusted P=2.69×10⁻², Mann-Whitney U test in [[papers/molecular-landmarks-tumor-hypoxia-across-cancer]]).

## Intuition

Chromothripsis is the genomic equivalent of an earthquake: a single moment in tumor evolution where a chromosome shatters and is reassembled imperfectly. Hypoxia plus replication stress plus DNA-repair deficiency (HR/MMR downregulation) can plausibly trigger such events. The fact that hypoxia statistically associates with chromothripsis suggests that hypoxic regions of tumors are more likely to experience these catastrophic genomic events.

## Formal notation

- Per-tumor count of chromothriptic regions, called from WGS using algorithms like ShatterSeek, ChromoSig, Chromothripsis Explorer
- In CPC-GENE PCa: hypoxia ↔ chromothripsis Bonferroni P=2.69×10⁻² (Mann-Whitney U)
- One of six "nimbosus" features (with hypoxia, PTEN loss, mutant TP53, shorter telomeres, IDC-CA)
- Often co-occurs with kataegis (clustered SNV mutations, particularly C>T/C>G in APOBEC context)

## Variants

- Single-arm chromothripsis: most common
- Whole-chromosome chromothripsis
- Inter-chromosomal chromothripsis (chromoplexy): structurally similar but spans chromosomes
- Kataegis (associated phenomenon): localized hypermutation, often co-occurring with chromothripsis loci

## Comparison

| SV type | Footprint | Triggering mechanism (proposed) |
|---|---|---|
| Chromothripsis | localized, hundreds of breaks | mitotic-error / micronucleus shattering |
| Chromoplexy | inter-chromosomal | replication-fork collapse |
| Breakage-fusion-bridge | telomeric | telomere crisis |
| BFB-driven amplification | localized amplicon | telomere/repair crisis |

## When to use

- Identifying tumors with catastrophic genomic events
- Linking hypoxia / replication stress to specific SV mechanisms
- Risk stratification: chromothripsis presence is prognostic in PCa

## Known limitations

- Calling chromothripsis from short-read WGS is noisy; long-read and optical mapping improve sensitivity
- Distinguishing chromothripsis from progressive chromosomal instability requires careful pattern recognition
- Single-cell DNA-seq has refined chromothripsis timing models recently

## Open problems

- Mechanistic basis for the hypoxia-chromothripsis association: micronucleus formation under hypoxia? Replication fork collapse?
- Whether anti-hypoxia therapy reduces chromothripsis incidence in vivo
- Chromothripsis at specific loci (e.g., chr10 PTEN region in PCa) may be mechanistically distinct from genome-wide chromothripsis

## Key papers

- [[papers/molecular-landmarks-tumor-hypoxia-across-cancer]] — chromothripsis associated with hypoxia in localized PCa (Bonferroni P=2.69×10⁻²); part of nimbosus

## My understanding

Chromothripsis under hypoxia is a mechanistically suggestive but molecularly underdeveloped link. It positions hypoxia not just as a slow mutagenic pressure but as a potential trigger for catastrophic genomic events. In localized PCa it is a key node of the nimbosus framework alongside PTEN loss and TP53 mutation.
