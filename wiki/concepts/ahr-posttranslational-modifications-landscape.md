---
title: "AHR posttranslational modifications landscape — phosphorylation, SUMOylation, ubiquitination, ADP-ribosylation, acetylation across AHR/ARNT/AHRR"
aliases:
  - AHR PTM landscape
  - AHR posttranslational modifications
  - AHR phosphorylation map
  - AHR SUMOylation
  - AHR ubiquitination
  - ARNT SUMOylation
  - AHRR SUMOylation
  - PhosphoSitePlus AHR
  - AHR PTM context-specificity
  - cell-type-specific AHR PTMs
  - same-residue opposite-phenotype AHR
tags:
  - AHR
  - posttranslational-modifications
  - phosphorylation
  - SUMOylation
  - ubiquitination
  - ADP-ribosylation
  - acetylation
  - context-specificity
maturity: emerging
key_papers:
  - complex-biology-aryl-hydrocarbon-receptor-activation
first_introduced: "2004 (S12/S36 PKC), expanded by HT-PTM mass spec studies + 2023 Opitz review"
date_updated: 2026-05-26
related_concepts:
  - ahr-context-specificity-pleiotropy
  - ahr-canonical-signalling-pathway
  - ahr-non-canonical-signalling
---

## Definition

The catalogue of reversible covalent modifications (phosphorylation, SUMOylation, ubiquitination, ADP-ribosylation, acetylation, homocitrullination) that are layered onto AHR and its obligate partners ARNT and AHRR. These PTMs alter ligand binding, nuclear shuttling, DNA binding, transcriptional output, and protein stability — and crucially, *which* effect dominates depends on the cell-type-specific kinase / phosphatase / SUMO E3 / SENP / DUB repertoire.

## Intuition

Why does the same AHR residue (e.g. S36) cause opposite phenotypes in different cells? Because the kinase that writes the modification is itself cell-type-restricted: PKC in HeLa/COS-7 vs PKCθ in T cells. PTMs are the molecular layer where "context" gets written onto the receptor.

## Formal notation

Documented sites and effects:

| Protein | Site | PTM | Enzyme | Effect | Cell type |
|---|---|---|---|---|---|
| AHR | S12, S36 | phosphorylation | PKC | impairs ligand-dependent NLS exposure | COS-7, HeLa |
| AHR | S36 | phosphorylation | PKCθ | enhances nuclear import | T cells |
| AHR | S68 | phosphorylation | p38 MAPK | inhibits nuclear export → nuclear accumulation | HaCaT keratinocyte |
| AHR | K63, K510 | SUMOylation | SUMO-1 | stabilises (blocks ubiquitination) but represses transcription | MCF-7 |
| HSP90 | S225, S254 | phosphorylation | n.d. | weakens AHR-HSP90 complex | Hepa-1 |
| ARNT iso1 | S77 | phosphorylation | CKII | required for optimal AHR activity | Karpas 299, Peer |
| ARNT | K245 | SUMOylation | SUMO-1 | inhibits ARNT-PML interaction; minor effect on transcription | MCF-7 |
| AHRR | K542, K583, K660 | SUMOylation | SUMO-1 | enhances repressor activity; promotes ANKRA2/HDAC4/HDAC5 binding | COS-7 |
| AHR | various | ADP-ribosylation | TIPARP | promotes degradation | various |
| AHR | various | mono-ubiquitination | various E3s | proteasomal turnover; partially reversed by UCHL3 | NSCLC |

## Variants

- **High-throughput PhosphoSitePlus-derived sites** (Fig. 3 of the paper): many sites with no assigned kinase.
- **Low-throughput literature-confirmed sites**: small set, well-characterised, but cell-line-restricted.

## Comparison

- Versus nuclear receptor PTMs (GR, AR, ER, PPARG): broadly analogous (cytosolic-to-nuclear shuttling regulated by phosphorylation; SUMO-mediated repression; ubiquitin-driven turnover), but AHR-specific features include the ARNT-dimer-dependent layer and the AHRR-competition layer.

## When to use

- When interpreting AHR phenotypes in a specific cell type — start by asking which kinases/phosphatases the cell expresses.
- When designing AHR-modulating drugs that mimic or block specific PTMs.

## Known limitations

- Most high-throughput PTM sites lack upstream-enzyme attribution.
- Combinatorial PTMs (phospho + SUMO + ubiquitin coexisting) are largely unmapped.
- No structural data exist on PTM-modified AHR in complex with ARNT/XRE.

## Open problems

- Systematic mapping of AHR PTMs across primary human tissues (vs cell lines).
- A "PTM-code" that converts PTM combinations into a predicted AHR transcriptional output.
- Tractable pharmacology: are there PKC-isoform-selective inhibitors that act as cell-type-restricted AHR modulators?

## Key papers

- [[papers/complex-biology-aryl-hydrocarbon-receptor-activation]] — Opitz et al. 2023 reviews and tabulates the field (Table 1 + Fig. 3 of the paper).

## My understanding

PTMs are the most under-exploited layer of AHR regulation for therapy. The same-residue / opposite-phenotype paradigm (S36 PKC vs PKCθ) is a clean example of why "AHR antagonism" has been clinically disappointing — without targeting the PTM context, blunt receptor antagonism cuts both pro- and anti-tumour outputs.
