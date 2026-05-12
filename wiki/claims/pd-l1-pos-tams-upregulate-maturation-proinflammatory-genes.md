---
title: "PD-L1+/hi TAMs upregulate maturation markers (CD83, HLA-DRA/B), pro-inflammatory cytokines (IL1B, CXCL2/3/8, CCL3/4), and complement (C1QA/B/C)"
slug: pd-l1-pos-tams-upregulate-maturation-proinflammatory-genes
status: supported
confidence: 0.9
tags:
  - PD-L1
  - TAM
  - maturation
  - HLA-DR
  - CD83
  - IL1B
  - CXCL8
  - C1Q
  - breast-cancer
domain: "immunology / scRNA-seq"
source_papers:
  - pd-l1-expressing-tumor-associated-macrophages
evidence:
  - source: pd-l1-expressing-tumor-associated-macrophages
    type: supports
    strength: strong
    detail: "Wang 2024 Fig. 1G-J, S4D: DEG analysis of PD-L1+/hi vs PD-L1−/lo TAMs from in-house luminal BC scRNA-seq identifies CD83, CD74, HLA-DRA/B, HLA-DQA/B (maturation); IL1B, CXCL2/3/8, CCL3/4/18 (pro-inflammatory chemokines/cytokines); C1QA/B/C (complement); FOS, JUNB, CEBPD (transcriptional activators). Replicated in Pal 2021 TNBC scRNA-seq. ELISA on flow-sorted TAMs confirms higher IL1β and CCL4 secretion by PD-L1+/hi TAMs after 16h (Fig. 1J, paired t test, *p<0.05, **p<0.01)."
conditions: "Untreated primary breast tumors; ER+ and TNBC; ex vivo digested single-cell suspensions."
date_proposed: 2026-05-12
date_updated: 2026-05-12
---

## Statement

In human breast cancer TAMs, PD-L1+/hi vs PD-L1−/lo dichotomization reveals a coherent gene expression signature in PD-L1+ TAMs spanning antigen presentation/maturation (CD83, HLA class II), pro-inflammatory cytokine/chemokine secretion (IL1B, CXCL2/3/8, CCL3/4/18), complement opsonin synthesis (C1Q), and AP-1 / CEBPD transcriptional activation. ELISA validation confirms protein-level differential secretion of IL1β and CCL4.

## Evidence summary

- Wang 2024 Fig. 1G (volcano), Fig. 1H (selected genes), Fig. 1J (ELISA validation).
- Replication: Fig. S4D-E (Pal 2021 TNBC).

## Conditions and scope

- Differential expression at cluster level (PD-L1+/hi vs PD-L1−/lo subpopulations).
- Protein validation in flow-sorted TAMs from n=4 patients (ELISA).

## Counter-evidence

- None in this paper; pan-cancer myeloid atlases (Cheng 2021) report similar mature/pro-inflammatory TAM clusters but do not always explicitly tie them to PD-L1.

## Linked ideas

- Underlies [[concepts/pd-l1-immunostimulatory-tam-phenotype]]
- Functional consequence demonstrated in claim [[claims/pd-l1-pos-macs-stimulate-cd8-proliferation-cytotoxicity]].

## Open questions

- Whether the mature/pro-inflammatory phenotype is causally driven by PD-L1 expression or co-emerges with it from upstream maturation signals.
