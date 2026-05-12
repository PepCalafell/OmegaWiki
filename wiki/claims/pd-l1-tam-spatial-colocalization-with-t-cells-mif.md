---
title: "PD-L1+ TAMs spatially co-localize with CD8+/CD4+ T cells within 20 μm while PD-L1− TAMs co-localize with cancer cells; PD-L1− TAMs also self-cluster"
slug: pd-l1-tam-spatial-colocalization-with-t-cells-mif
status: supported
confidence: 0.9
tags:
  - PD-L1
  - TAM
  - spatial-biology
  - mIF
  - CD8
  - cancer-cell
  - breast-cancer
domain: "spatial immunology"
source_papers:
  - pd-l1-expressing-tumor-associated-macrophages
evidence:
  - source: pd-l1-expressing-tumor-associated-macrophages
    type: supports
    strength: strong
    detail: "Wang 2024 Fig. 4A-E, S9A: multiplex immunofluorescence on untreated primary breast tumors (n=36) staining PD-L1, CD68, CD3, CD8, cytokeratin, DAPI. Within a 20 μm radius (assumed interaction range), PD-L1+ TAMs have significantly more CD8+ and CD4+ T cells nearby than PD-L1− TAMs; PD-L1− TAMs have significantly more cancer cells nearby (Wilcoxon paired test, ****p<0.0001, **p<0.01). PD-L1− TAMs but not PD-L1+ TAMs self-cluster (paired t test ****p<0.0001). CellPhoneDB + CellChat on scRNA-seq identifies 843 vs 729 significant L-R interactions for PD-L1+ vs PD-L1− TAMs (Fig. 4F): PD-L1+ TAMs preferentially interact with T cells via AREG-ICAM1, CD162-CD62L, ANXA1, MIF; PD-L1− TAMs interact with cancer cells via FN1-integrin αVβ1, COL6A2-integrin α2β1, SPP1, VEGFA."
conditions: "Untreated primary breast tumors (n=36); whole-slide mIF with phenotype mapping; 20 μm proximity threshold."
date_proposed: 2026-05-12
date_updated: 2026-05-12
---

## Statement

PD-L1+ vs PD-L1− TAMs in human breast tumors show opposite spatial engagement preferences: PD-L1+ TAMs lie near T cells (CD8+ and CD4+, <20 μm) while PD-L1− TAMs lie near cancer cells. PD-L1− TAMs also self-cluster, suggesting local immunosuppressive niches. The pattern is corroborated by CellPhoneDB + CellChat ligand-receptor analyses, which identify T-cell-engaging interactions specifically in PD-L1+ TAMs and ECM/cancer-cell-engaging interactions in PD-L1− TAMs.

## Evidence summary

- Wang 2024 Fig. 4A (mIF panel), 4B (TAM/cancer ratio), 4C-D (proximity quantification), 4E (PD-L1− self-cluster), 4F (CellPhoneDB/CellChat dot plots).
- Fig. S9A (representative mIF image).

## Conditions and scope

- 20 μm interaction radius is a common but empirical assumption.
- n=36 untreated primary tumors; no replication in treated or metastatic settings.
- Cytokeratin+ cancer-cell calling assumes epithelial origin; rare mesenchymal cancer cells may be missed.

## Counter-evidence

- None directly; ICI-treated cohorts not examined.

## Linked ideas

- Spatial mechanism behind functional differences in [[claims/pd-l1-pos-macs-stimulate-cd8-proliferation-cytotoxicity]] and [[claims/pd-l1-neg-macs-suppress-cd8-bite-killing]].
- Supports [[concepts/pd-l1-immunostimulatory-tam-phenotype]] at the spatial-architecture level.

## Open questions

- Whether the spatial pattern is causally established by chemotactic gradients (CXCL9, CXCL10) or by passive co-localization.
- Whether PD-L1− TAM self-clustering reflects efferocytotic / tissue-repair niches.
