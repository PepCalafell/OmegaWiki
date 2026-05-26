---
title: "Hepatic TREM2 macs uniquely express CALR (calreticulin), a pro-phagocytic surface molecule that counteracts CD47 don't-eat-me signaling"
slug: hepatic-trem2-macs-calr-counters-cd47-pro-phagocytic
status: weakly_supported
confidence: 0.65
tags:
  - TREM2
  - CALR
  - calreticulin
  - CD47
  - pro-phagocytic
  - efferocytosis
  - liver
  - HCC
domain: "tumor immunology / mac biology"
source_papers:
  - trem2-macrophages-associated-enhanced-response-pd
evidence:
  - source: trem2-macrophages-associated-enhanced-response-pd
    type: supports
    strength: medium
    detail: "Hepatic TREM2 macs uniquely upregulate CALR among tissue-specific DEGs (Fig. 3h). Authors propose that surface calreticulin facilitates cell-debris clearance by counteracting SIRPα/CD47 anti-phagocytic signaling — but no functional or perturbation experiment in this paper."
conditions: "scRNA-seq DEG; no functional perturbation."
date_proposed: 2026-05-26
date_updated: 2026-05-26
---

## Statement

Hepatic TREM2 macs in HCC uniquely upregulate CALR (calreticulin) relative to NSCLC TREM2 macs. The authors interpret surface calreticulin as a pro-phagocytic 'eat-me' signal that counteracts the CD47-SIRPα 'don't-eat-me' axis, hypothesised to facilitate clearance of apoptotic tumor cell debris.

## Evidence summary

- DEG-level upregulation of CALR in HCC TREM2 macs.
- Canonical calreticulin pro-phagocytic biology referenced.

## Conditions and scope

- Inference from canonical CALR biology; no functional validation in this paper.
- Surface vs intracellular CALR not distinguished by scRNA-seq.

## Counter-evidence

- CALR mRNA upregulation does not guarantee surface display; ER-stress-induced ecto-CALR is distinct from cytosolic CALR.

## Linked ideas

- [[concepts/sirpa-cd47-don-t-eat-me-axis]]
- [[concepts/hepatic-trem2-protective-tam-program]]

## Open questions

- Does CALR surface display in hepatic TREM2 macs drive measurable enhanced efferocytosis of tumor debris vs lung TREM2 macs?
