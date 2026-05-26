---
title: "scProtVelo — single-cell protein velocity and translation dynamics"
aliases:
  - scProtVelo
  - protein velocity
  - single-cell protein velocity
  - translation dynamics modeling
  - mRNA-protein latent variable model
  - transcription translation degradation model
  - velocity from protein abundance
  - scProtVelo translation kinetics
  - protein RNA velocity
tags:
  - trajectory-inference
  - multi-omics
  - translation
  - single-cell
  - methods
maturity: emerging
key_papers:
  - mapping-early-human-blood-cell-differentiation
first_introduced: "Furtwängler et al. 2025 *Science* (introduces scProtVelo as part of the scp-MS + scRNA-seq integration)"
date_updated: 2026-05-26
related_concepts:
  - mrna-protein-discordance
  - single-cell-proteomics-mass-spec
---

## Definition

scProtVelo is a latent-variable model that simultaneously fits gene-specific transcription, translation, mRNA-degradation, and protein-degradation rates from paired (or integrated) single-cell mRNA and protein abundance measurements. It generalizes the RNA-velocity formulation (Manno et al. 2018, Bergen et al. 2020) by adding a translation axis: the time delay between an mRNA change and its protein response encodes translation rate.

## Intuition

RNA velocity uses spliced vs unspliced mRNA to infer the direction of transcript change. scProtVelo uses mRNA vs protein to infer the direction of translation change. The temporal lag — mRNA rises first, protein follows — is the signal, and the inferred rate constants are gene-specific.

## Formal notation

For each gene *g* and cell *i* with mRNA abundance *m_gi* and protein abundance *p_gi*, scProtVelo learns parameters {α_g (transcription), β_g (translation), γ_g (mRNA degradation), δ_g (protein degradation)} that explain the observed (m, p) trajectory in pseudotime. The model uses pseudotime annotations as a prior to break the symmetry between activation and repression states, then fits a steady-state approximation per gene.

Compared to a linear baseline (protein = a·mRNA + b), scProtVelo explained ~50% of protein variance vs ~36% for the linear model (median R²) across the erythroid and pre-mDC trajectories in [[papers/mapping-early-human-blood-cell-differentiation]].

## Variants

- Erythroid trajectory: scProtVelo recovers correct cell-progression direction whereas standard scVelo produces an erroneous Late→Early Eryth backflow.
- Pre-mDC trajectory: scProtVelo applied as a validation, with comparable model fit to ground-truth differential expression.

## Comparison

- vs scVelo: scVelo uses splicing kinetics; scProtVelo uses translation kinetics. scProtVelo can capture post-transcriptional dynamics that scVelo cannot.
- vs simple linear mRNA→protein: 40% relative gain in explained protein variance.
- vs MultiVelo (Li et al. 2022): MultiVelo adds chromatin (snmC / snATAC); scProtVelo adds protein. Conceptually parallel but at the opposite end of the central dogma.

## When to use

- When you have paired or integrated single-cell mRNA + protein measurements (CITE-seq + scp-MS, or future paired methods).
- When you suspect translation regulation matters (HSC quiescence, metabolic states, immune activation).
- When RNA velocity alone gives implausible directionalities.

## Known limitations

- Requires a pseudotime prior — risks circularity if pseudotime is derived from the same modalities.
- Currently restricted to single trajectories per fit; multi-trajectory inference is acknowledged as a future direction.
- High protein missingness (~68% per cell in scp-MS) limits per-gene fits to the most consistently quantified proteins.

## Open problems

- Joint inference of multiple co-existing trajectories.
- Generalization to non-paired multimodal data (currently relies on the GLUE-integrated joint latent space).
- Validation against ground-truth pulse-SILAC translation rates.

## Key papers

- [[papers/mapping-early-human-blood-cell-differentiation]] — introduces scProtVelo.

## My understanding

A genuinely novel methodological contribution: the third dimension (translation) is the one that splicing kinetics cannot reach, and the paper shows it produces a measurable variance-explanation gain. The pseudotime-as-prior dependency is the obvious weak spot to interrogate in follow-ups.
