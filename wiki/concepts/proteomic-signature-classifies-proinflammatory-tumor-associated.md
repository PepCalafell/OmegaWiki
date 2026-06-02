---
title: "Proteomic signatures classify proinflammatory tumor-associated macrophages"
aliases:
  - proteomics-derived macrophage signature
tags:
  - macrophage
  - proteomics
  - signature
  - scRNA-seq
  - TAM
  - classification
maturity: emerging
key_papers:
  - delineation-signaling-routes-underlie-differences-macrophage
first_introduced: "Totu, Bossart et al. 2025 NAR Molecular Medicine"
date_updated: 2026-06-02
related_concepts:
  - m1-m2-polarization-paradigm
  - gold-standard-bulk-tam-signatures
  - tumor-associated-macrophage-immunosuppression
---

## Definition

The demonstration that protein-level signatures of in vitro polarized M1 vs M2 human macrophages — defined from unbiased proteomics — transfer to single-cell RNA-seq data from patient tumors and successfully separate proinflammatory from immunosuppressive macrophage populations, outperforming classification by a single canonical marker such as CD163.

## Intuition

In vivo TAMs do not split cleanly into M1/M2, but a coarse proinflammatory-vs-immunosuppressive distinction is clinically useful. A multi-protein signature, learned from cleanly controlled in vitro states and applied as a gene-set activity score, captures that distinction in messy patient scRNA-seq better than any one receptor — because single markers (CD163, CD206) are individually noisy and context-dependent.

## Formal notation

- Signature sources compared: proteomics-derived (top M1/M2 proteins), CD163 alone, literature "core set", literature "extended set"
- Applied via gene-set activity / ModuleScore on patient macrophages (HCC: Sharma et al.; brain metastases: Gonzalez et al.)
- Outcome: up to ~89% of macrophages classified M1-like; proteomic M1-like cells enriched in IFN-γ / TNFA-NFKB / inflammatory hallmark pathways (FDR < 0.05)

## Variants

- Datasets: hepatocellular carcinoma (HCC) and brain metastases (BrM)
- Signature granularity: single-marker vs multi-marker proteomic vs literature lists

## Comparison

vs CD163-alone classification: the single marker failed to cleanly separate the two states across expression thresholds, whereas knowledge-based multi-marker lists and the proteomic signature succeeded. vs gene-expression M1/M2 signatures shown elsewhere to fail in the TME: this argues the failure is about *single markers*, and that curated multi-marker proteomic sets recover a usable proinflammatory axis.

## When to use

- Annotating proinflammatory vs immunosuppressive macrophages in tumor scRNA-seq
- Arguing for multi-marker over single-marker macrophage classification in clinical samples

## Known limitations

- Validates a coarse two-class axis, not the full in vivo macrophage spectrum
- Signatures trained on in vitro monocyte-derived macrophages
- Small sample sizes for some clinical correlations (e.g. tumor-of-origin comparisons)

## Open problems

- Whether proteomic signatures can also resolve immunosuppressive sub-states in vivo
- Generalization across more tumor types and platforms

## Key papers

- [[papers/delineation-signaling-routes-underlie-differences-macrophage]] — shows proteomics-derived M1/M2 signatures separate proinflammatory macrophages in patient HCC and brain-metastasis scRNA-seq, outperforming CD163 alone.

## My understanding

A useful bridge from in vitro proteomics to clinical scRNA-seq, and a concrete argument (within this vault's macrophage-classification debate) that multi-marker beats single-marker. It complements claims that M1/M2 *gene* signatures fail in the TME by clarifying the failure is single-marker reliance, not the proinflammatory axis itself.
