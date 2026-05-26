---
title: "GLUE successfully integrates scp-MS and CITE-seq into a joint latent space (silhouette = 0.03)"
slug: glue-integrates-scpms-citeseq-joint-latent
status: supported
confidence: 0.85
tags: [GLUE, multi-omics, integration, scp-MS, CITE-seq, methodological, joint-latent-space]
domain: single-cell methods / integration
source_papers:
  - mapping-early-human-blood-cell-differentiation
evidence:
  - source: mapping-early-human-blood-cell-differentiation
    type: supports
    strength: strong
    detail: "Quote (p.4): 'The resulting joint latent space successfully integrated mRNA cells from the CITE-seq dataset and protein cells from the scp-MS dataset, with a silhouette score of 0.03.'"
conditions: "GLUE variational autoencoder; 2500-cell scp-MS dataset + 9086-cell CITE-seq dataset."
date_proposed: 2026-05-26
date_updated: 2026-05-26
---

## Statement

The first demonstration that an unpaired-integration framework (GLUE) can align scp-MS and CITE-seq data from human BM HSPCs into a single latent space usable for downstream trajectory analysis.

## Evidence summary

Silhouette score of 0.03 indicates successful (if loose) cross-modality mixing; biological variation per metric was preserved before and after integration (fig. S10A). Reported in [[papers/mapping-early-human-blood-cell-differentiation]] (Fig. 3 B-D).

## Conditions and scope

Healthy adult human BM CD34+; six scp-MS donors and four CITE-seq donors (distinct cells).

## Counter-evidence

Silhouette = 0.03 is low in absolute terms — alignment is "good enough" rather than tight.

## Linked ideas

## Open questions

- How does integration quality scale with cell number and proteome depth?
