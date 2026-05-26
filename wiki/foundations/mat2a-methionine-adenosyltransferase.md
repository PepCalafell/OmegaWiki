---
title: "MAT2A — methionine adenosyltransferase 2A"
slug: mat2a-methionine-adenosyltransferase
domain: metabolism / one-carbon biology
status: mainstream
aliases:
  - "MAT2A"
  - "methionine adenosyltransferase 2A"
  - "SAM synthetase"
  - "S-adenosylmethionine synthase"
  - "MAT II"
  - "AdoMet synthetase"
  - "PF-9366 target"
first_introduced: "Cantoni 1953 (SAM); reviewed in Lu 2000 FASEB"
date_updated: 2026-05-26
source_url: ""
---

## Definition

MAT2A catalyzes the ATP-dependent condensation of methionine to S-adenosylmethionine (SAM), the universal methyl-group donor for cellular DNA, RNA, protein, and small-molecule methylation reactions. MAT2A is the ubiquitous, growth-associated MAT isoenzyme expressed across most tissues (including macrophages), while MAT1A/MAT3 is restricted to mature hepatocytes.

## Intuition

If DNMT3A is the writer of DNA methylation, MAT2A is the supplier of its ink. Cellular SAM availability is rate-limiting for many methylation events, particularly in cells where local methionine is scarce; MAT2A inhibition (PF-9366) thus phenocopies DNMT inhibition for downstream gene-regulatory effects. In efferocytosing macrophages, MAT2A converts apoptotic-cell-derived methionine to SAM that fuels DNMT3A.

## Formal notation

- Reaction: methionine + ATP → SAM + PPi + Pi
- Inhibitor: PF-9366 (allosteric MAT2A inhibitor; Quinlan 2017)
- Isoforms: MAT2A (ubiquitous, regulatory subunit MAT2B), MAT1A (hepatic)
- Cofactor: Mg²⁺
- Cancer relevance: MTAP-deleted cancers depend on MAT2A — clinical interest in MAT2A inhibitors for synthetic lethality

## Variants

- MAT2A vs MAT1A: tissue distribution; MAT1A produces SAM at much higher fluxes in liver
- MAT2B regulatory subunit modulates MAT2A activity allosterically

## Known limitations

- PF-9366 has imperfect selectivity at high concentrations
- Cellular SAM also feeds non-DNA methylation (RNA, histones, small molecules) — MAT2A inhibition has pleiotropic effects

## Open problems

- Whether macrophage MAT2A is regulated by efferocytosis itself (e.g., AC engagement) beyond simple methionine substrate supply
- The contribution of methionine cycle recycling (SAH → homocysteine → methionine) vs de novo methionine import to macrophage SAM pools

## Relevance to active research

Central to [[papers/macrophages-use-apoptotic-cell-derived-methionine]] (Ampomah 2022 *Nat Metab*): MAT2A inhibition with PF-9366 or siMat2a blocks AC-induced Ptgs2/Tgfb1 and TGF-β1 secretion; exogenous SAM rescues this block independent of MAT2A activity. Methionine cycle recycling provides only a minor contribution in this context.
