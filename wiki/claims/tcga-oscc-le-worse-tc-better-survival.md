---
title: "In TCGA HPV-negative OSCC (n=275), high LE score predicts worse DSS/PFI; high TC score predicts improved OS/DSS/PFI"
slug: tcga-oscc-le-worse-tc-better-survival
status: supported
confidence: 0.85
tags: [TCGA, OSCC, survival, prognosis, correlational]
domain: oncology/prognosis
source_papers:
  - spatial-transcriptomics-reveals-distinct-conserved-tumor
evidence:
  - source: spatial-transcriptomics-reveals-distinct-conserved-tumor
    type: supports
    strength: strong
    detail: "n=275 HPV-negative OSCC: LE high vs low — DSS HR 0.60 [0.38–0.96], p<0.05; PFI HR 0.67 [0.45–0.98], p<0.05; OS HR 0.81, p>0.05. TC high vs low — OS HR 1.51, DSS HR 1.93, PFI HR 1.82, all p<0.05. Validated in GSE41613 (n=93) where LE also predicts worse OS and DSS."
conditions: "Cox proportional hazards; single-sample gene-set enrichment score on bulk TCGA RNA-seq"
date_proposed: 2026-05-22
date_updated: 2026-05-22
---

## Statement
Bulk-RNA-seq–derived LE and TC enrichment scores have opposing prognostic effects in OSCC: LE predicts worse outcomes, TC predicts better outcomes, across two independent cohorts.

## Evidence summary
Fig. 5b Kaplan-Meier curves and Cox hazard ratios; replication in GSE41613.

## Conditions and scope
HPV-negative OSCC; bulk RNA-seq with matched survival.

## Counter-evidence
LE-OS in the discovery TCGA cohort is borderline (p>0.05), although DSS/PFI are significant.

## Linked ideas

## Open questions
Whether the LE/TC scores remain prognostic after adjustment for stage, grade and margin status.
