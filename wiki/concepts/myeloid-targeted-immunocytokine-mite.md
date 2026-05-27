---
title: "Myeloid-targeted immunocytokine (MiTE) — dual TAM/lymphocyte trans-acting prodrug class"
aliases:
  - "MiTE"
  - "myeloid-targeted immunocytokine"
  - "MiTE-144"
tags:
  - immunocytokine
  - TREM2
  - IL-2
  - tumor-associated-macrophage
  - prodrug
  - protease-activation
  - cancer-immunotherapy
  - bispecific
maturity: emerging
key_papers:
  - macrophage-targeted-immunocytokine-leverages-myeloid-nk
first_introduced: "von Locquenghien et al. 2025 Cell (Amit lab, Weizmann + Immunai)"
date_updated: 2026-05-27
related_concepts:
  - masked-antibody-tme-conditional
  - trans-acting-immunocytokine
  - mmp14-protease-activated-il2-prodrug
  - trem2-tumor-associated-macrophage
  - innate-immune-checkpoint-blockade
---

## Definition

MiTEs (myeloid-targeted immunocytokines and natural killer/T cell enhancers) are a class of trans-acting immunocytokine prodrugs designed to simultaneously antagonise the myeloid checkpoint TREM2 on tumor-associated macrophages and deliver IL-2 to cytotoxic lymphocytes. The IL-2 moiety is engineered as an IL-2 superkine (H9 SK, IL-2Rβ-biased), masked by an extracellular IL-2Rβ blocking domain that is cleaved by the TAM-specific protease MMP14, restricting IL-2 activity to the tumor microenvironment.

## Intuition

MiTE = (anti-TREM2 antibody) ─ (MMP14 cleavage linker) ─ (IL-2 superkine + IL-2Rβ mask). In circulation the construct is inert (no off-target IL-2 toxicity, no TREM2-Fc effector function). At the tumor site, TAMs concentrate MMP14, which cleaves the linker, releasing active IL-2 superkine in trans onto neighbouring T and NK cells while the anti-TREM2 arm simultaneously reprograms macrophages.

## Formal notation

- Variants tested: MiTE-76, MiTE-95, MiTE-144, MiTE-208 (different blocking-domain and linker valencies)
- Lead: MiTE-144 (one IL-2SK + one IL-2Rβ blocking domain + one MMP14 cleavage site)
- Fc: Fc-Null (N297A) IgG1 — abrogates FcγR binding and ADCC
- Linker: SGRSENIRTA (high MMP14 hydrolysis specificity)
- Receptor affinity: post-cleavage KD = 1.26 × 10⁻⁹ M (vs WT IL-2 KD = 2.80 × 10⁻⁷ M)

## Variants

- Single-mask + single-cleavage (MiTE-76 / MiTE-95) — higher background activity
- Single-mask + single-cleavage with low-background design (MiTE-144) — lead candidate
- Dual-mask + dual-cleavage (MiTE-208) — lowest background but lower potency
- αRSV-IL-2SK (masked) — non-targeting control to isolate TREM2 contribution

## Comparison

- vs αTREM2 monotherapy: MiTE-144 markedly more efficacious in MC38 and MCA205
- vs αPD-1, αCTLA-4: MiTE-144 outperforms each as monotherapy
- vs αTREM2 + αPD-1 / + αCTLA-4: MiTE-144 alone matches or exceeds
- vs MiTE-144 + αCTLA-4: synergistic, eradicating tumors in 6/7 MC38 mice
- vs prior immunocytokines (αPD-L1-IL-15, αPD-1-IL-2, αTIM3-IL-2): MiTE acts in trans on myeloid + lymphoid axes; prior ICKs act in cis on a single compartment

## When to use

- Solid tumors with high TAM infiltration and immunosuppressive myeloid microenvironment
- ICI-refractory tumors where T-cell-only therapies fail
- Combinatorial designs with αCTLA-4 to deplete Tregs

## Known limitations

- Long-term safety of protease-activated IL-2 not yet established in primates or chronic dosing
- Activity demonstrated in RCC PDTFs and MC38/MCA205 — generalisation to other tumor types is open
- MMP14 expression by cancer-associated fibroblasts may introduce TME activation outside TAMs
- Murine models only test human TREM2 via hTREM2 humanised mice — additional immunogenic axes unstudied

## Open problems

- Optimal cytokine cargo (IL-2 superkine vs IL-15 vs tailored IL-2 variants)
- Adaptive resistance: do tumors downregulate MMP14 under selective pressure?
- Combination with radiotherapy / chemotherapy / other immunotherapies
- ADA formation rates with masked IL-2 in human trials

## Key papers

- [[papers/macrophage-targeted-immunocytokine-leverages-myeloid-nk]] — first description; MiTE-144 lead candidate, MC38/MCA205 and RCC PDTF validation

## My understanding

MiTEs are a clean conceptual unification of three previously separate ideas: TREM2 antagonism, IL-2 receptor-biased superkine engineering, and protease-cleavable cytokine masking. The Amit lab's contribution is integrating them into a single trans-acting molecule that delivers two effects at the right place at the right time. For my thesis (macrophage / hypoxia / immune-suppression), MiTEs are notable because they upregulate hypoxia-associated TAM modules (Arg1, Nos2, Hmox1) while still being therapeutic — that runs against the common framing that hypoxic TAMs are uniformly bad. Worth a careful re-read for that tension.
