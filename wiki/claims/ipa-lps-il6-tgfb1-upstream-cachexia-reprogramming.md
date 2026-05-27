---
title: "IPA combined-omics upstream-regulator analysis nominates LPS/inflammation as the principal driver of cachexia metabolic reprogramming, with IL6 and TGFB1 as further regulators"
slug: ipa-lps-il6-tgfb1-upstream-cachexia-reprogramming
status: supported
confidence: 0.75
tags: [IPA, upstream-regulator, LPS, IL6, TGFB1, cachexia, inflammation]
domain: cachexia / multi-omics
source_papers:
  - multi-omics-profiling-cachexia-targeted-tissues
evidence:
  - source: multi-omics-profiling-cachexia-targeted-tissues
    type: supports
    strength: moderate
    detail: "Fig. 4g + Ext Fig. 5j: IPA combined-omics upstream-regulator analysis of transcriptome + metabolome of Cax vs Ctrl mice across 5 tissues. Top hits: lipopolysaccharide (LPS), β-oestradiol, TGFB1. Authors interpret LPS as 'inflammation in general' and proceed to test IL6 perturbations downstream."
conditions: "IPA Qiagen integrated analysis; significance ranked by -log10(P)."
date_proposed: 2026-05-27
date_updated: 2026-05-27
---

## Statement

Combined-omics IPA upstream-regulator analysis identifies lipopolysaccharide (LPS) / general inflammation, β-oestradiol, and TGFB1 as the top predicted upstream regulators of cachexia metabolic reprogramming; the authors interpret this as evidence for inflammation as the primary driver and test IL6 directly in follow-up experiments.

## Evidence summary

Quoted: "lipopolysaccharide and, by extension, inflammation as the first determinant to drive the substantial metabolic reprogramming occurring in cachexia."

## Conditions and scope

IPA predictions are statistical inferences from gene/metabolite overlaps with curated regulator-target sets — directly testable predictions rather than measured upstream activity.

## Counter-evidence

LPS as a literal regulator is unlikely in tumour-bearing mice without overt endotoxin exposure; IPA's LPS hit should be read as "broad inflammatory signature."

## Linked ideas

## Open questions

- The specific transcription factors downstream of IL6 (STAT3? NF-κB?) that drive one-carbon enzyme induction in each tissue.
