---
title: "NNMT-MNAM axis in cachectic liver"
aliases:
  - "hepatic NNMT induction in cachexia"
  - "MNAM accumulation cachectic liver"
tags:
  - NNMT
  - MNAM
  - liver
  - cachexia
  - nicotinamide-methylation
  - methylation-detoxification
maturity: emerging
key_papers:
  - multi-omics-profiling-cachexia-targeted-tissues
first_introduced: "Mizuno et al. (cited as ref 24); formal IL6-coupled cachexia axis: Morigny et al. 2026"
date_updated: 2026-05-27
related_concepts:
  - one-carbon-metabolism-cachexia-tissue-overarching
  - il6-driven-cachexia-one-carbon-reprogramming
---

## Definition

The concept that in cancer cachexia the liver upregulates NNMT (nicotinamide N-methyltransferase) and accumulates its product MNAM (1-methylnicotinamide), with NNMT/MNAM acting as the dominant hepatic methyl-acceptor system of the broader one-carbon-cachexia response — under direct IL6 control (Nnmt mRNA induction is suppressed 77% by anti-IL6 antibody and 89% by tumour-cell IL6 KO).

## Intuition

Among the tissues remodelled by cachexia, the liver has a *different* methyl-acceptor signature than muscle/adipose: instead of methyllysines and sarcosine, it accumulates MNAM. This is consistent with the liver's role as a methylation-detox organ (MNAM is a stable methylated nicotinamide derivative excreted in urine; NNMT-driven methylation acts as a methyl-group sink). In cachexia this sink is *amplified*, and IL6 is the switch.

## Formal notation

- NNMT reaction: nicotinamide (NAM) + SAM → 1-methylnicotinamide (MNAM) + SAH.
- Observed changes in C26 cachectic liver:
  - Nnmt mRNA: strongly induced (Fig. 4d).
  - MNAM (metabolite #10): ↑ fold-change in liver Cax vs Ctrl.
  - Mat1a: strongly induced (provides SAM substrate).
- IL6 control:
  - C26-scr → ↑ Nnmt; C26-IL6-KO → near-baseline Nnmt (-89%).
  - IL6-neutralising antibody: -77% Nnmt induction.
  - MNAM elevation abolished by IL6 KO.
- Conserved across models: C26, Panc02, 8025, ApcMin, LLC, KPP, humanised SW480.
- Patient translation: liver biopsies from sarcopenic cancer patients show ↑ NNMT vs non-sarcopenic.

## Variants

- Liver NNMT induction has prior precedent in the Mizuno et al. paper (ref 24): "remote solid cancers rewire hepatic nitrogen metabolism via host NNMT" — the present paper extends this to a coordinated multi-tissue context.
- NNMT biology in other contexts (adipocyte NNMT in obesity, cancer-cell NNMT in tumour aggressiveness) is well-documented; the cachexia-specific framing is the new contribution.

## Comparison

- Vs muscle KMT2A/B-methyllysine signature: NNMT acts on a small-molecule acceptor (NAM), not protein lysines; tissue-typed enzymology.
- Vs adipose phospholipid methylation (PEMT-driven): yet another tissue-specific methyl sink.

## When to use

- When interpreting hepatic urea-cycle / nitrogen-metabolism shifts in cachexia (NNMT-driven NAM methylation diverts NAM from NAD+ salvage — potential link to mitochondrial NAD pool).
- When considering NNMT inhibitors as cachexia therapy candidates.
- When monitoring patient urinary MNAM as a non-invasive cachexia biomarker.

## Known limitations

- The mechanistic link between NNMT-driven NAM methylation and hepatic dysfunction in cachexia is not directly tested (e.g., no Nnmt-KO liver-rescue experiment).
- Liver-specific Nnmt KO would be the cleanest test; not performed here.
- Whether elevated MNAM has independent biological activity (vs. just being a flux marker) is not addressed.

## Open problems

- Does liver-specific Nnmt KO rescue cachexia phenotypes in tumour-bearing mice?
- Is plasma/urinary MNAM a quantitative biomarker for cachexia severity in patients?
- Does NNMT inhibition combine additively with IL6 blockade to improve cachexia outcomes?
- What is the impact of NNMT-driven NAD+ salvage diversion on hepatic mitochondrial function in cachexia?

## Key papers

- [[papers/multi-omics-profiling-cachexia-targeted-tissues]] — Establishes the IL6-controlled NNMT-MNAM liver axis in cachexia.

## My understanding

NNMT-MNAM is the cleanest individual molecular handle within the broader cachexia one-carbon story. The combination of (i) liver tissue specificity, (ii) -89% IL6 KO suppression, (iii) Mizuno-et-al precedent, (iv) patient sarcopenia liver translation, and (v) druggability of NNMT (small-molecule inhibitors exist) makes this the highest-priority near-term translation target.
