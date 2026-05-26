---
title: "CTHRC1+ CAF / SLPI+ TAM profibrotic spatial ecotype"
aliases:
  - profibrotic ecotype
  - CTHRC1-SLPI ecotype
  - eFibro_CTHRC1 + Macro_SLPI ecotype
  - profibrotic spatial niche
  - tumor leading-edge profibrotic niche
  - CAF-TAM profibrotic colocalization
  - matrix-remodeling ecotype
  - TGFβ1-IL-1β profibrotic niche
  - shared upstream profibrotic axis
  - pan-cancer profibrotic spatial ecotype
tags:
  - pan-cancer
  - spatial
  - niche
  - ecotype
  - caf
  - tam
  - profibrotic
  - ecm
  - immune-exclusion
  - tme
maturity: emerging
key_papers:
  - spatiotemporal-analyses-pan-cancer-single-cell
first_introduced: "2025"
date_updated: 2026-05-26
related_concepts:
  - cthrc1-efibro-ecm-remodeling-pan-cancer-caf
  - slpi-macrophage-profibrotic-tam
  - col11a1-spp1-fibrotic-axis-cd8-exclusion-nsclc
  - epithelial-proinflammatory-niche-il1b-il1r1-luad-precursor
---

## Definition

A pan-cancer spatial ecotype defined by colocalization of CTHRC1+ ECM-remodeling fibroblasts and SLPI+ profibrotic macrophages at the malignant–normal interface. Signature scores correlate at R>0.5 in ST data across BRCA, CRC, OV, PAAD, PLC and SCC; multiplexed IHC validates CTHRC1+CD68+SLPI+ colocalization in HNSC, oral cancer, and NSCLC. NicheNet identifies TGFβ1 and IL-1β as shared upstream ligands activating both cell types.

## Intuition

Two profibrotic lineages — fibroblast and macrophage — converge on a single tissue niche and a single upstream signaling axis (TGFβ1 + IL-1β → SMAD + NF-κB / STAT). This converts what used to be two separate stromal/myeloid stories into one targetable spatial unit at the tumor edge.

## Comparison

- Mechanistically downstream of the **early IL1B-IL1R1 epithelial-proinflammatory niche** ([[concepts/epithelial-proinflammatory-niche-il1b-il1r1-luad-precursor]]) — that niche is precursor-prevalent and inflammatory, the CTHRC1+/SLPI+ ecotype is invasive-stage and ECM-dominated. The IL-1β axis links them.
- More canonical / pan-cancer than COL11A1+/SPP1+ NSCLC-specific axis ([[concepts/col11a1-spp1-fibrotic-axis-cd8-exclusion-nsclc]]).
- Couples a known matrix-remodeling CAF program to a fibrotic-TAM program; complementary to ECM-Mac ([[concepts/ecm-mac-collagen-producing-tam]]).

## Key papers

- [[papers/spatiotemporal-analyses-pan-cancer-single-cell]] — defines the ecotype via 62 ST slides, in-house mIHC, and NicheNet upstream inference; links to worse TCGA survival in SKCM (P=2.54×10⁻⁵) and BRCA (P=0.0229) when the ecotype dominates patient classification.

## When to use

- Designing combination anti-stromal therapies: blocking TGFβ1 and/or IL-1β should disrupt both CAF and TAM components simultaneously.
- Interpreting immune-exclusion phenotypes at the tumor leading edge — particularly DHP/NIHS patients in the pan-cancer ecosystem subtyping.
- Building spatial-omics inference pipelines: CTHRC1 + SLPI + CD68 staining as a minimal panel for the ecotype.

## Open problems

- Is the ecotype hypoxia-driven? Cross-reference to [[papers/molecular-landmarks-tumor-hypoxia-across-cancer]] and hypoxia-TAM concepts in the wiki is warranted.
- Are CTHRC1+ CAFs upstream of SLPI+ TAM recruitment, or vice versa, or do both originate independently from the shared TGFβ1/IL-1β niche?
- Could LGALS9–CD44/HAVCR2 blockade synergize with TGFβ1 blockade to maximally restore T-cell infiltration?
