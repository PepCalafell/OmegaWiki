---
title: "Hypoxic inflammatory MAC (mMAC₁ / IL4I1) signatures correlate with better overall survival in multiple human cancers, including bladder and ovarian carcinoma"
slug: mmac1-signature-correlates-with-better-survival
status: weakly_supported
confidence: 0.55
tags: [macrophages, prognosis, tcga, bladder-cancer, ovarian-cancer, signature-deconvolution, immunology]
domain: "tumor immunology"
source_papers: [nf-kb-tet2-promote-macrophage-reprogramming]
evidence:
  - source: nf-kb-tet2-promote-macrophage-reprogramming
    type: supports
    strength: moderate
    detail: "TCGA pan-cancer survival analysis using mMAC₁ / iMAC₁ / mMAC₂₁ / iMAC₂₁ gene signatures shows mMAC₁ + IL4I1 high abundance correlates with better OS in 7/12 cancer types tested (notably BLCA and OC). High C2-CpG methylation in BLCA tumors correlates with worse OS. mMAC₁ abundance correlates strongly with T-cell percentage in BLCA (r=0.74, P=2.2·10⁻⁶⁷). Sorted IL4I1⁺ ovarian tumor MACs reproduce the in vitro mMAC₁ methylation+TF program ex vivo (n=5)."
conditions: "Bulk-RNA-seq deconvolution (CIBERSORTx) for TCGA cohorts with paired methylation arrays available. Effect is strongest in immune-hot BLCA and OC tumors. Does not hold in 5/12 cancer types tested. Sample size of primary ovarian sorted populations is small (n=5)."
date_proposed: 2026-05-05
date_updated: 2026-05-05
---

## Statement

Tumors enriched for the mMAC₁ in-vitro–derived signature (proinflammatory, hypoxic, NF-κB-demethylated) — and their in-vivo correlate IL4I1⁺ MACs in single-cell atlases — show better overall survival in 7 of 12 TCGA cancer types tested, with the cleanest effect in bladder urothelial carcinoma (BLCA) and ovarian carcinoma (OC). The opposite signature (high C2-CpG methylation, indicating *absence* of mMAC₁-like populations) correlates with worse survival in BLCA. The mMAC₁ signature also correlates strongly with T-cell infiltration and predicted T-cell-activating ligand-receptor signaling.

## Evidence summary

- **Pan-cancer survival (TCGA)**: high mMAC₁ / IL4I1 signatures correlate with better OS in 7/12 cancer types; high mMAC₂₁ / TREM2 signatures with worse OS in 7/12.
- **BLCA-specific**: Kaplan-Meier curves show high mMAC₁ → better OS (HR < 1; P = 0.003); high C2-CpG methylation → worse OS (P < 0.001).
- **T-cell co-infiltration (BLCA)**: mMAC₁ abundance vs T-cell estimated fraction r = 0.74 (P = 2.2·10⁻⁶⁷); iMAC₂₁ vs T cell r = −0.27 (P = 5·10⁻⁸).
- **Predicted ligand-receptor (CellChat in BLCA scRNA-seq)**: mMAC₁ → T cell signals include CXCL9-CXCR3, CXCL10-CXCR2, ICAM1-SPN, MHC-class-I-CD8, MIF-CD74+CD44/CXCR4 — consistent with T-cell chemotaxis and TCR activation.
- **Primary OC validation (n=5)**: FACS-sorted IL4I1⁺ MACs from ovarian tumors recapitulate the mMAC₁ DNA-methylation pattern and TF activity (RELA, HIF1A) on bulk RNA-seq + EPIC.

## Conditions and scope

- Holds for: BLCA, OC, and at least 5 other TCGA cancer types where IL4I1 / mMAC₁ signature behaviour is consistent.
- Does **not** hold in: 5/12 cancer types where signatures show opposite or null effects — the paper notes that MAC populations may have opposing roles in different cancers.
- Sample sizes for primary tissue validation are small (n=5 OC).
- Bulk deconvolution depends on CIBERSORTx assumptions; signature carry-over from in-vitro to in-vivo populations relies on MoMac-VERSE cluster identity.

## Counter-evidence

- Several studies place IL4I1 macrophages as having "tolerogenic" / "regulatory" features, complicating the simple "IL4I1 = good prognosis" mapping (the source paper acknowledges this in the discussion).
- 5/12 TCGA cancer types do not reproduce the better-survival association.
- TREM2 association with poor prognosis is not universal — its role is "tissue-specific and depends on polarization programs" (cited in source).

## Linked ideas

(none yet)

## Open questions

- Why 5/12 cancer types do not reproduce the mMAC₁ → better OS correlation. Tissue / metabolic / TME-composition modifiers are unidentified.
- Whether therapeutic *induction* of an mMAC₁-like state in vivo (e.g., via local NF-κB modulation under hypoxic TME conditions) actually improves outcomes.
- The relative weight of mMAC₁ direct effect on T cells vs. confounding via overall immune-hot vs immune-cold tumor classification.
- Replication in independent cohorts (non-TCGA) and with prospective MAC-targeting trial data.
