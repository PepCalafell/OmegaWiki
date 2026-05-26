---
title: "totalVI — paired probabilistic modeling for CITE-seq"
slug: totalvi-cite-seq-modeling
domain: "methods / single-cell-integration"
status: mainstream
aliases:
  - totalVI
  - total-VI
  - CITE-seq probabilistic modeling
  - scvi-tools totalVI
  - paired mRNA-ADT model
  - Gayoso totalVI
  - totalVI integration
  - antibody-derived tag VAE
first_introduced: "Gayoso et al. 2021 *Nat Methods* — Joint probabilistic modeling of single-cell multi-omic data with totalVI"
date_updated: 2026-05-26
source_url: "https://docs.scvi-tools.org/en/stable/user_guide/models/totalvi.html"
---

## Definition

totalVI is a variational autoencoder for paired CITE-seq data (scRNA-seq + antibody-derived tags, ADTs) measured on the same cells. It jointly models mRNA counts (negative binomial), ADT counts (background + foreground mixture), and batch effects, producing a denoised joint latent representation and per-cell denoised mRNA/ADT values.

## Intuition

Raw ADT counts include high background from non-specific antibody binding. Treating background and foreground as a mixture model — and learning batch effects jointly with mRNA — gives a cleaner protein signal than naive normalization and a shared latent space for downstream tasks.

## Formal notation

Per cell *n*: latent z_n ~ N(0, I); mRNA_ng ~ NB(f_g(z_n, batch)); ADT_np ~ Mixture(background_p, foreground(z_n, batch)). Inference via amortized VI.

## Key variants

- scVI (mRNA only) and totalVI (mRNA + ADT) share the scvi-tools backbone.
- multiVI extends to mRNA + ATAC.
- scANVI: semi-supervised variant.

## Known limitations

- Requires paired ADT-mRNA data; cannot directly handle unpaired multi-omics (use GLUE for that).
- ADT mixture model assumes well-separated background/foreground — fails for low-abundance epitopes.

## Open problems

- Generalization to >2 modalities per cell.
- Calibration of denoised values against ground-truth absolute quantification.

## Relevance to active research

- Used in [[papers/mapping-early-human-blood-cell-differentiation]] to model the CITE-seq companion dataset (~9086 cells, four donors) before unpaired integration with scp-MS via GLUE.
