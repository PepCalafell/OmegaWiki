---
title: "NetPhorest — kinase/phosphatase specificity prediction"
slug: netphorest-kinase-prediction
domain: methods
status: mainstream
aliases:
  - NetPhorest
  - NetworKIN/NetPhorest
first_introduced: "Miller et al. 2008 Science Signaling"
date_updated: 2026-06-02
source_url: "http://netphorest.info/"
---

## Definition

NetPhorest is a probabilistic atlas of sequence-based predictors that assigns phosphorylation sites to the kinase families (or phosphatase/binding-domain groups) most likely to recognize them, returning posterior probabilities for each candidate family from the local sequence context.

## Intuition

NetPhorest predicts kinase *families* rather than individual kinases, trading specificity for robustness: it answers "which family of enzymes plausibly targets this site" with calibrated probabilities, making it useful for footprinting when individual-kinase resolution is unattainable.

## Formal notation

- Input: phosphosite sequence windows
- Output: posterior probability per kinase family (kept if posterior > prior and above a threshold, e.g. >0.035)
- Typically the top families per site are retained for enrichment testing

## Key variants

- Family-level prediction vs individual-kinase prediction (Kinase Library)
- Component of the NetworKIN framework integrating context

## Known limitations

- Family-level granularity cannot pinpoint a single kinase
- Sequence-only model omits cellular context and abundance

## Open problems

- Improving from family- to kinase-level resolution while preserving calibration
- Integrating with expression to filter inactive families

## Relevance to active research

Used alongside the Kinase Library and KEA3 to predict upstream kinase families for upregulated macrophage phosphosites; it recapitulated high p38-family activity in M1 and supported the construction of kinase–kinase signaling networks for each macrophage state.
