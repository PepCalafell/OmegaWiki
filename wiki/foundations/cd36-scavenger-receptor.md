---
title: "CD36 — scavenger receptor / fatty acid translocase"
slug: cd36-scavenger-receptor
domain: cell surface / lipid biology / phagocytosis
status: mainstream
aliases:
  - "CD36"
  - "FAT"
  - "fatty acid translocase"
  - "SR-B2"
  - "scavenger receptor B2"
  - "GPIV"
  - "platelet glycoprotein IV"
  - "thrombospondin receptor"
  - "oxLDL receptor"
  - "apoptotic-cell binding receptor"
first_introduced: "Tandon 1989 (GPIV); Endemann 1993 (oxLDL receptor)"
date_updated: 2026-05-26
source_url: ""
---

## Definition

CD36 is a class B scavenger receptor / fatty-acid translocase expressed on macrophages, platelets, microvascular endothelium, adipocytes, and skeletal muscle. It binds oxidized LDL (driving foam cell formation), long-chain fatty acids (mediating uptake), thrombospondin-1, plasmodium-infected erythrocytes, and — relevant to efferocytosis — apoptotic-cell-displayed signals that trigger ERK1/2 activation and engulfment cooperation with MERTK/TAM receptors.

## Intuition

CD36 reads "damaged/apoptotic surface" cues across many cargoes: oxidized lipid (oxLDL → atherosclerotic foam cell), apoptotic cell, infected erythrocyte. Engagement triggers Src-family kinase → ERK1/2 activation in macrophages, contributing to the early signalling of efferocytosis before phagolysosomal degradation.

## Formal notation

- Gene: CD36 (chr7q21)
- Ligands: oxLDL, long-chain fatty acids, thrombospondin-1, apoptotic cells (PS-displaying), Plasmodium PfEMP1
- Downstream signalling: Fyn / Lyn Src-kinases → ERK1/2 activation; PI3K
- Macrophage role: oxLDL uptake (atherogenesis), efferocytosis (cooperatively with MERTK), inflammatory priming
- Detection / perturbation: anti-CD36 antibody, siCd36, CD36 KO mice
- Disease: atherosclerosis (drives foam cell formation); platelet dysfunction

## Variants

- Soluble CD36 — circulating biomarker
- Splice variants with different N-glycosylation patterns

## Known limitations

- Overlapping function with other scavenger receptors (SR-A, LOX-1) complicates KO phenotypes
- Lipid uptake function vs phagocytic function hard to separate

## Open problems

- Whether CD36-driven ERK activation requires PS recognition, OxPS recognition, or thrombospondin bridging in efferocytosis
- The relative contribution of CD36 vs MERTK to ERK activation in different macrophage states

## Relevance to active research

Central to [[papers/macrophages-use-apoptotic-cell-derived-methionine]] (Ampomah 2022 *Nat Metab*): siCd36 robustly reduces AC-induced p-ERK1/2, COX2, and TGF-β1 MFI in macrophages — establishing CD36 as the principal early ERK activator in this pathway. MerTK-KO macrophages show only modest decreases, indicating CD36 dominates ERK activation here.
