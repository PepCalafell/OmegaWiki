---
title: "IL6-driven one-carbon metabolism reprogramming in cancer cachexia"
aliases:
  - "IL6 controls cachexia one-carbon enzymes"
  - "IL6-NNMT axis in cachexia"
tags:
  - IL6
  - cachexia
  - one-carbon-metabolism
  - NNMT
  - inflammation
  - upstream-regulator
maturity: emerging
key_papers:
  - multi-omics-profiling-cachexia-targeted-tissues
first_introduced: "Morigny et al. 2026 (Nat Metab) — formal mechanistic linkage"
date_updated: 2026-05-27
related_concepts:
  - one-carbon-metabolism-cachexia-tissue-overarching
  - nnmt-mnam-liver-cachexia-axis
  - fidas-5-methionine-blockade-rescues-cachexia
---

## Definition

The concept that tumour-secreted IL6 is the dominant upstream driver of one-carbon-metabolism activation in cachexia target tissues, controlling expression of one-carbon enzymes (notably NNMT, MAT1A/MAT2A, KMT2A/B, SAT1, GPX3, GSTA4) and the elevation of one-carbon metabolites (MNAM, methyllysines, thymidine), independently of any effect on tumour size.

## Intuition

If IL6 is the master inflammatory cytokine of cachexia (well established for muscle/adipose effects), the new claim is that IL6 *also* runs the metabolic-epigenetic remodelling — the methylation machinery itself — across host tissues. Removing IL6 (genetically from the tumour or with neutralising antibody) does not shrink the tumour but does abolish the one-carbon signature and rescue weight loss. So IL6 acts through one-carbon metabolism as a load-bearing mechanism, not just as a paracrine wasting signal.

## Formal notation

- Perturbations tested:
  - IL6-neutralising antibody in C26-bearing mice.
  - C26-IL6-KO vs C26-scramble tumour cells (CRISPR Il6 KO).
- Phenotypic readouts:
  - Tumour size: unchanged (KO tumours grow slower initially but reach matched size at endpoint).
  - Body weight loss: rescued.
  - Liver Nnmt mRNA induction: -77% (antibody), -89% (IL6 KO).
  - One-carbon metabolites (MNAM and thymidine in liver; di- and tri-methyllysine in GC muscle): elevated in C26-scr, abolished in C26-IL6-KO.
- Upstream computational evidence: IPA combined-omics upstream-regulator analysis nominates LPS/inflammation, IL6 and TGFB1.
- In vitro recapitulation: recombinant IL6 on C2C12 myotubes induces one-carbon metabolites + atrophy + glucose hypermetabolism; FIDAS-5 (MAT inhibitor) reverses each.

## Variants

- Local tumour-IL6 KO (cell-autonomous IL6 source) vs systemic IL6 neutralisation — both rescue, suggesting tumour is the dominant IL6 source.
- Anti-IL6R (e.g., tocilizumab) untested here — clinical translation question.

## Comparison

- Vs IL6 → STAT3 → muscle atrophy programs (canonical IL6 cachexia biology): this paper adds a tissue-overarching metabolic-enzyme arm beyond muscle-only STAT3 effects.
- Vs LPS-driven inflammation (IPA upstream call): paper notes "LPS" should be read as inflammation in general — IL6 is the experimentally testable handle.
- Vs NF-κB-driven cytokine signalling in cancer-cachexia models (chronic-STING-NF-κB-IL6 axis [[concepts/cin-chronic-sting-nfkb-il6-drives-metastasis]] elsewhere in the wiki): may share the IL6 endpoint but the upstream origin differs.

## When to use

- When framing cachexia interventions that target IL6 (anti-IL6R, JAK inhibitors) — the metabolic-epigenetic arm is now a measurable downstream readout (NNMT mRNA, MNAM levels) for pharmacodynamic monitoring.
- When designing combination therapies pairing IL6 blockade with one-carbon-pathway modulators (FIDAS-5, methionine-restricted diet).

## Known limitations

- The IL6 → transcription-factor → one-carbon-enzyme molecular route is not pinned down (STAT3? NF-κB? specific co-activator?).
- IL6 KO at the tumour level affects multiple downstream programs simultaneously; cell-type-specific IL6R KO (e.g., LysMCre, AlbCre, Myl1Cre) would dissect which host compartment is the effector.
- Only one inflammatory axis tested; other cytokines (IL1B, TNF) could contribute redundantly.

## Open problems

- What is the molecular route from IL6R engagement to Nnmt transcription (STAT3 binding at the Nnmt promoter in liver hepatocytes)?
- Does anti-IL6R therapy in patients (tocilizumab, siltuximab) reduce NNMT/MNAM/sarcosine biomarkers proportionally to weight loss rescue?
- Is the metabolic arm IL6-specific or does any chronic-inflammation cytokine (IL1B, TNF) phenocopy?

## Key papers

- [[papers/multi-omics-profiling-cachexia-targeted-tissues]] — Establishes the IL6 → one-carbon axis with double-pharmacological/genetic dissociation.

## My understanding

This concept is the actionable handle that makes the broader "[[concepts/one-carbon-metabolism-cachexia-tissue-overarching]]" claim therapeutically interesting. IL6 blockade is clinically available; the IL6 → one-carbon route gives a mechanistic biomarker (MNAM, NNMT) for trial design. Combining IL6 blockade with MAT/NNMT inhibition is a plausible next-generation cachexia therapy.
