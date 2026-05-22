---
title: "Fowlkes–Mallows stability identifies biologically meaningful spatial cluster counts"
slug: fowlkes-mallows-stability-identifies-biologically-meaningful
status: supported
confidence: 0.8
tags:
  - clustering
  - model-selection
  - methodological
  - spatial-omics
domain: methods
source_papers:
  - cellcharter-reveals-spatial-cell-niches-associated
evidence:
  - source: cellcharter-reveals-spatial-cell-niches-associated
    type: supports
    strength: moderate
    detail: "FMI-based stability auto-selects n=9 for the DLPFC cohort (manual ground truth has 7 layers + white matter), same in 12-sample and 42-sample versions (Fig. 1h). n=4 and n=11 are stable solutions for mouse spleen; n=3/8/20 are stable for the NSCLC CosMx cohort and reflect cancer/individual-tumor/intratumor states."
conditions: "Requires multiple GMM runs at each candidate n; the stability curve must show a clear local maximum at the chosen n."
date_proposed: 2026-05-22
date_updated: 2026-05-22
---

## Statement

Selecting cluster counts by Fowlkes–Mallows-Index agreement across runs at n−1, n, n+1 produces solutions that map onto biologically interpretable structures and are more robust than AIC, BIC, or negative log-likelihood at increasing sample counts.

## Evidence summary

DLPFC FMI curves (Fig. 1h) identify n=9 in both 12-sample and 42-sample cohorts. AIC/BIC/NLL either lack a clear elbow or grow with sample count (Extended Data Fig. 2b). Mouse spleen — n=4 and n=11 stable. NSCLC CosMx — n=3/8/20 stable, hierarchical.

## Conditions and scope

Stability is criterion-specific; the chosen n is still subject to biological interpretation (e.g., the NSCLC paper analyses the n=20 solution downstream while noting biological hierarchy of the smaller solutions).

## Open questions

- Is FMI-stability robust to the choice of l-hop neighborhood depth?
