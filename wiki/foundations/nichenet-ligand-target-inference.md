---
title: "NicheNet — ligand → target gene regulatory potential inference"
slug: nichenet-ligand-target-inference
domain: "computational-biology / methods"
status: mainstream
aliases:
  - "NicheNet"
  - "ligand-target inference"
  - "regulatory potential ligand"
  - "intercellular signaling NicheNet"
  - "ligand activity scoring"
  - "Browaeys 2020 NicheNet"
  - "ligand-receptor downstream targets"
  - "cell-cell communication with downstream effects"
first_introduced: "Browaeys, Saelens, Saeys 2020 *Nature Methods*"
date_updated: 2026-05-06
source_url: "https://github.com/saeyslab/nichenetr"
---

## Definition

NicheNet predicts which ligands expressed by sender cells most likely drive downstream gene expression changes in receiver cells, by combining (i) prior-knowledge ligand-receptor and intracellular signaling/transcription networks into a "ligand-target regulatory potential" matrix and (ii) the receiver cell's observed differentially expressed gene (DEG) set. Ligands are then ranked by AUROC / Pearson against the DEG list.

## Intuition

CellChat / CellPhoneDB ask "which L-R pairs are co-expressed between cell types?". NicheNet goes one step further and asks "given that receiver cells X are differentially expressed against background, which sender ligands best *explain* those DEGs through plausible signaling cascades?" — closing the loop from ligand to downstream transcriptional effect.

## Formal notation

- Input: scRNA-seq with sender + receiver annotations + receiver DEG set
- Prior network: ligand → receptor → signaling proteins → TFs → targets, with weighted edges from public PPI/curation
- Compute regulatory potential P(target | ligand) by random-walk-with-restart on the prior network
- Score each ligand by Pearson / AUROC between P(*|ligand) and observed DEG vector
- Output: ranked ligand list + per-ligand top target genes

## Key variants

- NicheNet original (R, 2020)
- LIANA — meta-tool that aggregates NicheNet alongside CellChat, CellPhoneDB, etc.
- MultiNicheNet — multi-condition extension

## Known limitations

- Prior network is biased to well-studied pathways
- Ligand activity is inferred, not measured; off-target predictions occur
- Spatial context is not modeled

## Open problems

- Updating prior with cell-type-specific signaling wiring
- Validation rate against perturbation datasets

## Relevance to active research

[[papers/cross-tissue-single-cell-landscape-human]] uses NicheNet on liver-cancer scRNA-seq (Sharma et al. 2020) to predict T-cell→TAM interactions, identifying IFNG (from CD8⁺ T cells) and CD40LG (from CD4⁺ T cells) as the top ligands explaining the IL4I1_Mac and ISG_Mo programs in the tumour periphery.
