---
title: "TAM–T cell spatial proximity in the TME (predominant immune cell-pair across cancers)"
aliases:
  - "TAM-T cell proximity"
  - "TAM-T cell colocalization"
tags:
  - tumor-associated-macrophage
  - T-cell
  - spatial-transcriptomics
  - MERFISH
  - tumor-microenvironment
  - ligand-receptor
maturity: emerging
key_papers:
  - macrophage-targeted-immunocytokine-leverages-myeloid-nk
  - multiomics-analysis-cxcl9-macrophages-immunotherapy-response
first_introduced: "von Locquenghien et al. 2025 Cell (MERFISH 1.86 M-cell pan-cancer atlas)"
date_updated: 2026-05-27
related_concepts:
  - trem2-mac-pd1-immune-niche-quartet
  - cxcl9-spp1-tam-ratio-ici-biomarker
  - pan-cancer-tam-atlas-23-clusters
---

## Definition

A spatial-transcriptomics-derived observation that, across major human solid tumors (breast, lung, colorectal, ovarian), TAMs are the immune cell type most consistently in close spatial proximity to T cells within the tumor microenvironment, ahead of DCs, Tregs, NK cells, and other immune populations. Quantified by empirical cumulative distribution functions (CDFs) of minimum distances on MERFISH data, and supported by ligand-receptor interaction enrichment (MultiNicheNetR) in tumor vs adjacent-healthy tissue.

## Intuition

If TAMs sit physically closest to T cells across tumor types, they are the dominant local immunomodulators of T-cell function. This co-localisation underwrites both the immunosuppressive effect (CD80/86-CTLA-4, PD-L1-PD-1, TGFBR1-TGFB, LGALS-CD69 axes are TAM-T cell axes) and the therapeutic opportunity (a TAM-localised cytokine can act in trans on T cells).

## Formal notation

- Dataset: 1.86 M cells, MERFISH, four tumor types
- Quantification: empirical CDFs of nearest-neighbor distances, TAM-T < DC-T < other pairs (except DCs in ovarian)
- Validated molecularly: 332,723-cell scRNA-seq integration with MultiNicheNetR, showing TAM-T cell L-R network density > other pairs

## Comparison

- vs DC-T cell proximity: comparable in ovarian cancer, lower in breast/lung/colon
- vs Treg-T cell proximity: TAM-T is closer in all four cancers
- vs TAM-NK proximity: TAM-T closer than TAM-NK

## When to use

- As biological rationale for TAM-targeted trans-acting therapeutics
- For prioritising TAM-T cell L-R axes (CXCL9-CXCR3, CD80-CTLA-4, ICOSLG-ICOS, TGFB-TGFBR) as drug targets
- For interpreting spatial niche analyses (e.g., the TREM2-mac quartet niche)

## Known limitations

- MERFISH gene panel is targeted (~500-1000 genes), not unbiased — proximity claims depend on accurate cell typing
- Heterogeneity within "T cell" cluster (CD8 effector vs CD4 helper vs Treg) is collapsed in proximity stats
- Tumor-type sample size: four cancers — generalization to others (HCC, RCC, melanoma, GBM) remains open

## Open problems

- Whether TAM-T proximity is causal for T-cell exhaustion or a consequence
- How TAM subsets (TREM2⁺ vs TREM2⁻, hypoxia vs IFN-response) differentially shape T-cell state
- Single-cell resolution of T-cell subtype dependence on TAM proximity

## Key papers

- [[papers/macrophage-targeted-immunocytokine-leverages-myeloid-nk]] — MERFISH 1.86 M-cell pan-cancer demonstration

## My understanding

A foundational empirical claim that grounds the entire MiTE design rationale: if TAMs are the closest immune neighbour of T cells, then a TAM-targeted molecule with a trans-acting cytokine is the natural lever to manipulate the T-cell compartment without systemic exposure. The MERFISH atlas-level claim is also a useful primary citation for any future macrophage-T-cell niche paper.
