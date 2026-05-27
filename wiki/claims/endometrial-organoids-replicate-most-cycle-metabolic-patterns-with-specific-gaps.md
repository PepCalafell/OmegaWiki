---
title: "Epithelial endometrial organoids replicate most in-vivo cycle-dependent metabolic patterns but diverge in nucleotide salvage and Tn-antigen glycosylation"
slug: endometrial-organoids-replicate-most-cycle-metabolic-patterns-with-specific-gaps
status: weakly_supported
confidence: 0.55
tags:
  - endometrial-organoids
  - menstrual-cycle
  - nucleotide-salvage
  - Tn-antigen-glycosylation
  - in-vitro-vs-in-vivo
domain: "endometrial-biology / organoids / metabolism"
source_papers:
  - atlas-scale-metabolic-activities-inferred-single
evidence:
  - source: atlas-scale-metabolic-activities-inferred-single
    type: supports
    strength: moderate
    detail: "Figure 5f: violin plots comparing scCellFie metabolic-task scores between proliferative and secretory phases in organoid scRNA-seq vs in vivo HECA epithelium. Most cycle-dependent tasks reproduce in vivo trends (blue area); nucleotide-metabolism tasks and Tn-antigen glycosylation deviate (red area). All differences FDR <1% (Wilcoxon rank sum). Key driver genes flagged: GALNT4, APRT, HPRT1."
conditions: "Public organoid scRNA-seq datasets (refs 59, 85); transcriptomic comparison only. Authors note divergences may reflect either inherent organoid limitations or simply harder-to-replicate proliferative→secretory temporal transitions."
date_proposed: 2026-05-27
date_updated: 2026-05-27
---

## Statement

Public scRNA-seq of hormone-stimulated epithelial endometrial organoids reproduces the majority of cycle-dependent metabolic patterns observed in vivo (in HECA), but diverges from in-vivo behavior specifically in nucleotide-salvage pathways and Tn-antigen glycosylation — nominating GALNT4, APRT, and HPRT1 as candidate genes whose expression / regulation needs improvement in next-generation organoid protocols.

## Evidence summary

In Fig 5f, scCellFie task scores in organoid epithelial cells were compared between proliferative and secretory phases against the matched in-vivo HECA epithelial trajectory (Fig 5b,c). Tasks following the same phase-direction were grouped (blue area); those reversing trend were grouped (red area). Nucleotide metabolism and Tn-antigen glycosylation appeared in the red area. The cycle-dependent tasks deviating in organoids peak at the in-vivo proliferative→secretory transition, suggesting organoids may struggle with temporal transitions rather than steady-state phase states.

## Conditions and scope

Two public organoid datasets; no direct organoid-protocol intervention tested. Findings are mismatch-pattern detection, not mechanism.

## Counter-evidence

The authors themselves caveat that organoid divergence may reflect general temporal-transition modeling limits rather than specific pathway problems.

## Linked ideas

None yet.

## Open questions

- Does APRT/HPRT1 supplementation or nucleotide-precursor enrichment of organoid media close the in-vivo–in-vitro gap?
- Are GALNT4-driven O-glycosylation defects an organoid-specific artifact or a feature of the in-vitro epithelial state?
