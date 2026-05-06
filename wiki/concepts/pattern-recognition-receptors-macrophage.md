---
title: "Pattern recognition receptors (PRRs) of macrophages"
aliases:
  - "PRR"
  - "pattern recognition receptor"
  - "TLR NLR RLR ALR CLR"
  - "germline-encoded innate sensors"
  - "PRR families"
  - "innate immune sensors macrophage"
  - "five PRR families"
  - "pattern-triggered immunity"
  - "DAMP PAMP sensing"
tags:
  - macrophage
  - innate-immunity
  - pattern-recognition
  - PRR
  - TLR
  - NLR
  - RLR
  - inflammation
  - immunology
maturity: stable
key_papers:
  - physiology-diseases-tissue-resident-macrophages
first_introduced: "Janeway 1989 (PRR concept); Medzhitov & Janeway 1997; reviewed in Lazarov & Geissmann 2023"
date_updated: 2026-05-06
related_concepts:
  - efferocytosis-anti-inflammatory-clearance
  - macrophage-ontogeny-resident-vs-monocyte-derived
---

## Definition

Pattern recognition receptors (PRRs) are germline-encoded innate immune sensors that recognize conserved molecular patterns associated with pathogens (PAMPs — pathogen-associated molecular patterns) and damaged-self (DAMPs — damage-associated molecular patterns). Lazarov & Geissmann 2023 organize macrophage PRRs into five families on the basis of protein-domain homology: Toll-like receptors (TLRs), RIG-I-like receptors (RLRs), NOD-like receptors (NLRs), AIM2-like receptors (ALRs), and C-type lectin receptors (CLRs). Engagement of PRRs by PAMPs/DAMPs triggers signalling cascades that produce inflammatory mediators (TNF, IL-1, IL-6, type-I IFNs) and, in some cases, phagocytosis.

## Intuition

Macrophages cannot afford to encode receptors for every possible pathogen — there are too many. PRRs solve this by detecting *conserved* features (LPS, dsRNA, flagellin, β-glucan, mannose, CpG-DNA, viral nucleic acids, peptidoglycan fragments) shared across whole pathogen classes. The five families divide labour by ligand class and subcellular localization: TLRs at plasma/endosomal membrane; RLRs/ALRs in cytoplasm sensing intracellular nucleic acids; NLRs in cytoplasm sensing peptidoglycan and danger signals (forming inflammasomes); CLRs at plasma membrane sensing fungal/cellular carbohydrates. Together they cover viruses, bacteria, fungi, protozoa, and damaged self.

## Formal notation

- **Toll-like receptors (TLRs)** — 10 in human; sense lipopolysaccharide (TLR4), lipopeptides (TLR2), flagellin (TLR5), dsRNA (TLR3), CpG-DNA (TLR9), ssRNA (TLR7/8). Plasma membrane (TLR1/2/4/5/6) or endosomal (TLR3/7/8/9). Output: NF-κB / IRF3 / IRF7 → TNF, IL-6, type-I IFN.
- **NOD-like receptors (NLRs)** — sense intracellular peptidoglycan fragments (NOD1, NOD2) or assemble inflammasomes (NLRP3, NLRC4, NLRP1) → caspase-1 → IL-1β, IL-18, gasdermin-D pyroptosis.
- **RIG-I-like receptors (RLRs)** — RIG-I, MDA5, LGP2; sense cytoplasmic viral RNA → MAVS adapter → IRF3 / IRF7 → type-I IFN.
- **AIM2-like receptors (ALRs)** — AIM2 senses cytoplasmic dsDNA → ASC inflammasome → caspase-1 → IL-1β, IL-18 / pyroptosis.
- **C-type lectin receptors (CLRs)** — Dectin-1 (β-glucan), Dectin-2 (mannose), Mincle, DC-SIGN. Sense fungal cell wall + cellular glycans.
- **cGAS-STING** (cyclic GMP-AMP synthase + stimulator of interferon genes) — strictly speaking a separate cytosolic DNA sensor not in the classical 5-family taxonomy but functionally adjacent; produces type-I IFN.

## Variants

- *Plasma membrane PRRs* (TLR2, TLR4, Dectin-1) — sense extracellular pathogens.
- *Endosomal PRRs* (TLR3, TLR7, TLR8, TLR9) — sense pathogens after phagocytosis.
- *Cytoplasmic PRRs* (NLRs, RLRs, ALRs, cGAS) — sense intracellular pathogens that escape phagosomes.
- *Inflammasome-forming NLRs* (NLRP3, NLRC4, NLRP1, AIM2) — produce IL-1β family cytokines and pyroptotic cell death.

## Comparison

vs efferocytic receptors: PRRs trigger inflammation; efferocytic receptors (TIM4, MERTK) trigger anti-inflammatory engulfment. Same cell, opposite outputs depending on receptor engaged.
vs adaptive immunity (TCR/BCR): PRRs are germline-encoded and stereotyped; TCR/BCR are somatically rearranged and clonal. PRRs respond fast (minutes-hours); adaptive responses take days.
vs SIRPα-CD47 'don't-eat-me': PRRs *trigger* phagocytosis when engaged; SIRPα *suppresses* phagocytosis when engaged. Both run continuously and the balance dictates engulfment outcome.

## When to use

- Designing macrophage-targeting adjuvants (TLR4 agonists like MPL; STING agonists in cancer immunotherapy).
- Interpreting septic-shock pathophysiology (LPS-TLR4-NF-κB hyperactivation).
- Predicting which PRR-axis dysfunction underlies which immune deficiency or autoinflammatory syndrome.

## Known limitations

- The 5-family taxonomy is partial — cGAS-STING and several other sensors are increasingly recognized as additional PRR-like systems.
- Cross-family signalling integration is complex (e.g. TLR4-NLRP3 priming-then-activation for IL-1β).
- DAMP biology overlaps with PAMPs in many cases; "self vs non-self" framing is incomplete.

## Open problems

- Why some PRR-deficient patients develop autoinflammation (e.g. NLRP3 gain-of-function = CAPS) while others develop susceptibility to specific infections.
- The role of macrophage PRRs in *sterile* injury (DAMP-driven inflammation, atherosclerosis, neurodegeneration).
- Whether PRR inhibitors can be developed without unacceptable infection susceptibility.

## Key papers

- [[papers/physiology-diseases-tissue-resident-macrophages]] — Lazarov & Geissmann 2023 *Nature* — review summarizes the five PRR families with macrophage examples and notes the role of monocyte-derived macrophages as the principal inflammatory PRR-responders, contrasting with TRMs more focused on homeostatic functions

## My understanding

For my hypoxia-NF-κB work: TLR4-LPS signalling is the upstream driver of the NF-κB activation we use experimentally. TLR4 → MyD88 → IRAK → TAK1 → IKK → NF-κB is the canonical cascade. Hypoxia modulates TLR4 expression and signalling and this is a documented synergy. The PRR concept anchors why inflammatory macrophage states exist in the first place — they are pre-programmed responses to the receptor ligand. The [[foundations/lps-toll-like-receptor-signaling]] foundation already covers TLR4 specifically; this concept covers the broader PRR taxonomy.
