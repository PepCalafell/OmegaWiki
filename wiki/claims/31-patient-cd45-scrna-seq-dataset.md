---
title: "A 31-sample CD45+ scRNA-seq/CITE-seq dataset of inflammatory skin disease yielded 158,037 cells"
slug: 31-patient-cd45-scrna-seq-dataset
status: supported
confidence: 0.9
tags: [skin, scrna-seq, cite-seq, dataset, immunology]
domain: immunology / single-cell
source_papers:
  - classification-human-chronic-inflammatory-skin-disease
evidence:
  - source: classification-human-chronic-inflammatory-skin-disease
    type: supports
    strength: strong
    detail: "Quote (p.2): 'We obtained transcriptomic data from 158,037 single cells after quality control filtering (removal of doublets and poor-quality cells).' Samples: 8 PV, 7 AD, 2 LP, 1 BP, 6 CIR, 7 HC (31 total)."
conditions: "Flow-sorted live CD45+ cells, 10x Chromium 3' scRNA-seq + CITE-seq, ~6000 cells/sample."
date_proposed: 2026-06-10
date_updated: 2026-06-10
---

## Statement

Liu et al. single-cell profiled flow-sorted CD45+ immune cells from 31 human skin samples (8 psoriasis vulgaris, 7 atopic dermatitis, 2 lichen planus, 1 bullous pemphigoid, 6 clinically indeterminate rashes, 7 healthy controls), obtaining 158,037 quality-filtered single-cell transcriptomes with paired CITE-seq protein epitope data.

## Evidence summary

Reported in Results and Methods of [[papers/classification-human-chronic-inflammatory-skin-disease]]. Used [[foundations/scrna-seq-10x-chromium]], [[foundations/cite-seq-citeseq]], and [[foundations/cell-ranger-10x-alignment]].

## Conditions and scope

Punch biopsies of lesional rash skin; mammoplasty/abdominoplasty discards as healthy controls; patients off systemic immunosuppressives ≥4 weeks.

## Counter-evidence

None; descriptive dataset claim.

## Linked ideas

## Open questions

- Whether the cohort size is sufficient to detect APC-restricted signatures.
