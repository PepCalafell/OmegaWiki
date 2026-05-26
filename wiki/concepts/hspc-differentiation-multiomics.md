---
title: "Human HSPC differentiation hierarchy (multi-omics view)"
aliases:
  - HSPC hierarchy
  - hematopoietic differentiation
  - CD34+ HSPC compartment
  - HSC-MPP-LMPP cascade
  - human hematopoiesis single-cell
  - bone marrow HSPC atlas
  - human CD34+ differentiation
  - MEP-GMP-CLP branching
  - HSPC lineage tree
  - early human hematopoiesis
  - HSC LT-HSC ST-HSC hierarchy
  - hematopoietic stem progenitor cell multi-omics
tags:
  - hematopoiesis
  - HSPC
  - stem-cells
  - bone-marrow
  - differentiation
  - single-cell
maturity: active
key_papers:
  - mapping-early-human-blood-cell-differentiation
first_introduced: "Continuous hierarchy view: Velten et al. 2017 *Nat Cell Biol*; modern multi-omics revision: Furtwängler et al. 2025"
date_updated: 2026-05-26
related_concepts:
  - single-cell-proteomics-mass-spec
  - joint-multimodal-latent-space
---

## Definition

The human hematopoietic stem and progenitor cell (HSPC) compartment, as resolved at single-cell mRNA + protein resolution. HSCs and multipotent progenitors (MPPs) sit at the apex; downstream lie lymphoid-primed multipotent progenitors (LMPPs), then branches into granulocyte-monocyte progenitors (GMPs), common lymphoid progenitors (CLPs), megakaryocyte-erythroid progenitors (MEPs), and basophil-eosinophil-mast progenitors (BaEoMa). Further sub-branching produces dendritic-cell progenitors (GMDP, MDP, pre-pDC, pre-mDC) and B-cell progenitors (pB).

## Intuition

The classical "tree" view (HSC → MPP → CMP/CLP → mature lineages) is now understood as a continuous landscape with priming events and committed progenitor populations that are not cleanly separable by FACS alone. Multi-omics (scRNA-seq + scp-MS + CITE-seq + FACS) provides multiple, partly redundant views of the same continuum.

## Formal notation

Cell-state populations identified in [[papers/mapping-early-human-blood-cell-differentiation]] (11 scp-MS clusters):

- **HSC** — H1F0, HMGA1, HP1BP3, macroH2A1; high glycolysis, low translation.
- **Progenitors 1 and 2** — early LMPP/EMP bifurcation; CD45RA, LCP1, PSME1 mark LMPP side; SOD2 and ALDH1A1 mark EMP side.
- **LMPP** — lymphoid-primed.
- **GMDP** — AZU1, PRTN3, ELANE, CTSG, MPO (azurophil granules).
- **MDP** — LGALS1, PLD4, CD123↑, LYZ, HLA-DRB1; gives rise to pre-pDC, pre-mDC.
- **CLP / pre-pDC** — mixed; LYZ-low distinguishes pre-pDCs from MDPs.
- **pB** — CD10+, TOP2B-high.
- **MEP** — CD71+ BAH-1+ true MEPs (S100A4, RAP1B); BAH-1-negative cells are GMP-like contaminants.
- **BaEoMa** — CD123+, PRG2, CLC.

## Variants

- **scp-MS view** (Furtwängler 2025): 11 clusters from 2500 cells; recapitulates classical hierarchy with refinements at MEP/CMP/BaEoMa boundary.
- **CITE-seq view** (companion dataset): ~9086 cells; Azimuth reference mapping for label transfer.
- **scRNA-seq atlases** (Hay et al., Granja et al., etc.): broader cell counts, more cluster heterogeneity, but no protein layer.

## Comparison

- CMP as a population: the immunophenotypic CMP gate is now understood to be heterogeneous, splitting between myeloid and BaEoMa branches.
- LT-HSC markers: CD90 and CD49f are the textbook markers but underperformed in scp-MS; Endomucin proposed as an alternative.

## When to use

- When interpreting any scRNA-seq atlas of human bone marrow.
- When designing FACS strategies — the paper's CD71/BAH-1 refinement and Endomucin proposal are immediate actionable updates.
- When mapping disease-state HSPCs (AML, MDS, MPN) against a healthy reference.

## Known limitations

- Healthy adult donors only in the reference; pediatric, fetal, and aged BM may differ.
- HSCs are rare and low-signal — the most immature compartment is the least statistically resolved.

## Open problems

- Better LT-HSC markers across human populations.
- Linking the multi-omics hierarchy to functional readouts (LTC-IC, xenografts) gene-by-gene rather than population-by-population.
- Disease state perturbations (MDS, AML) projected onto this multi-omics reference.

## Key papers

- [[papers/mapping-early-human-blood-cell-differentiation]] — the multi-omics reference.

## My understanding

This is the most complete multi-omics human HSPC reference to date; CD71/BAH-1 MEP refinement and Endomucin LT-HSC marker are the immediate practical takeaways for any lab doing FACS-based HSPC isolation.
