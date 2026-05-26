---
title: "Top-10 TREM2 mac program genes stratify IMbrave150 HCC patients (atezolizumab+bevacizumab) by overall survival"
slug: trem2-program-stratifies-imbrave150-overall-survival
status: supported
confidence: 0.8
tags:
  - TREM2-program
  - IMbrave150
  - overall-survival
  - atezolizumab
  - bevacizumab
  - HCC
  - bulk-RNA-seq
  - prognostic
domain: "translational immuno-oncology"
source_papers:
  - trem2-macrophages-associated-enhanced-response-pd
evidence:
  - source: trem2-macrophages-associated-enhanced-response-pd
    type: supports
    strength: strong
    detail: "IMbrave150 phase III (n=358, atezolizumab+bevacizumab in unresectable HCC). Top-10 TREM2 mac genes scored per patient bulk RNA-seq; quartile cut TREM2hi (top) vs TREM2lo (bottom) yields significant OS difference favouring TREM2hi (Fig. 4c top)."
conditions: "Bulk RNA-seq, atezolizumab + bevacizumab regimen, unresectable HCC. Quartile-cut stratification."
date_proposed: 2026-05-26
date_updated: 2026-05-26
---

## Statement

A transcriptional score built from the top-10 genes of the TREM2 mac mRNA program stratifies IMbrave150 phase III HCC patients (n=358; atezo+bev) into a TREM2hi top-quartile with significantly improved overall survival vs TREM2lo bottom-quartile.

## Evidence summary

- Phase III IMbrave150 (atezolizumab+bevacizumab, unresectable HCC, n=358).
- Bulk RNA-seq scored with the top-10 TREM2-mac genes.
- Kaplan-Meier OS: TREM2hi > TREM2lo, log-rank significant.

## Conditions and scope

- Quartile-cut on a 10-gene score; not prospectively optimised.
- Bulk RNA-seq cannot distinguish TREM2-mac abundance from intrinsic tumor TREM2 expression.

## Counter-evidence

- The same score fails to stratify POPLAR NSCLC atezolizumab patients ([[claims/trem2-program-fails-stratify-poplar-nsclc-atezo]]) — tissue-dependent.

## Linked ideas

- [[concepts/hepatic-trem2-protective-tam-program]]
- [[foundations/imbrave150-trial]]

## Open questions

- Does deconvolution (e.g., CIBERSORTx) recover the mac-cell-fraction effect cleanly?
