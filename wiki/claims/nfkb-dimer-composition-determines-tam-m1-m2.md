---
title: "NF-κB dimer composition (p50-p50 vs p65-p50) determines whether TAMs polarize toward M1 or M2"
slug: nfkb-dimer-composition-determines-tam-m1-m2
status: weakly_supported
confidence: 0.6
tags:
  - NF-κB
  - p50
  - p65
  - RELA
  - NFKB1
  - dimer-composition
  - macrophage-polarization
  - M1
  - M2
  - TAM
domain: "molecular-biology / immunology"
source_papers:
  - hypoxia-driven-crosstalk-between-tumor-tumor
evidence:
  - source: hypoxia-driven-crosstalk-between-tumor-tumor
    type: supports
    strength: moderate
    detail: "Bai 2022 review (DOI 10.1186/s12943-022-01645-2, p.12) synthesizes the dimer-composition argument: 'Lipopolysaccharide promotes the overexpression of p50-p50 homodimers, allowing M1 to M2 macrophage reprogramming. In contrast, Bufalin promotes the overexpression of p65-p50 heterodimers, leading to the transition of macrophage from M2 to M1.' Five NF-κB family members (p65/RELA, p50/NFKB1, p52/NFKB2, c-REL, RELB) couple to form distinct homo- or heterodimers with opposing polarization effects. The model resolves the apparent paradox of conflicting NF-κB-on-TAM literature: NF-κB-p50-siRNA M2→M1 transition (Saccani 2006); NF-κB pathway blockade M2→M1 (Hagemann 2008); increased NF-κB activity reducing tumor burden (de Boer 2017)."
conditions: "Mechanistic model based on multiple primary studies in vitro and in mice. Direct dimer-composition measurement (ChIP-seq for p65 vs p50 vs heterodimer) in TAMs from human tumors is rare. Inferred from indirect evidence (siRNA, dimer-driving stimuli)."
date_proposed: 2026-05-08
date_updated: 2026-05-08
---

## Statement

The NF-κB transcription factor family comprises five members — p65 (RELA), p50 (NFKB1), p52 (NFKB2), c-REL, RELB — that couple into different homo- and heterodimers. The same NF-κB pathway can drive opposite TAM polarization outcomes depending on dimer composition: p50-p50 homodimers favor M2 polarization (LPS-driven M1→M2 reprogramming), while p65-p50 heterodimers favor M1 polarization (Bufalin-driven M2→M1 transition). The dimer-composition framework resolves the apparent paradox in the NF-κB-on-TAM literature, where some studies (Saccani 2006; Hagemann 2008) found NF-κB blockade switches M2→M1, while others (de Boer 2017) found increased NF-κB activity reduces tumor burden via persistent M1 polarization.

## Evidence summary

- [[papers/hypoxia-driven-crosstalk-between-tumor-tumor]] — Bai 2022 *Molecular Cancer* review (p.12) synthesizes the dimer-composition model.
- Underlying primary studies (cited in Bai 2022): Saccani et al. 2006 *Cancer Res* (NF-κB p50 siRNA in M2 → M1); Hagemann et al. 2008 *J Exp Med* (NF-κB blockade M2→M1); Porta et al. 2009 *PNAS* (LPS p50-p50 homodimers in M1→M2 tolerance); a study cited as [165] reports increased NF-κB activity reducing tumor burden with persistent M1 polarization.

## Conditions and scope

- Demonstrated in vitro and in murine models; human TAM dimer-composition data are sparse.
- LPS-driven p50-p50 homodimer accumulation is a well-known immune-tolerance mechanism (Hagemann 2008) and the canonical source of the M1→M2 reprogramming model.
- Bufalin (a Chinese herbal compound) drives p65-p50 heterodimer accumulation and reverses the polarization to M1.
- Other NF-κB family members (p52, c-REL, RELB) are mentioned but not centrally featured.

## Counter-evidence

- Direct dimer-composition measurement in primary human TAMs (e.g. ChIP-seq for p65 vs p50 in patient TAM samples) is rare.
- The dimer-composition model is largely a *narrative* synthesis; quantitative attribution of M1 vs M2 outcome to specific dimer ratios is inferred rather than directly measured.
- Other transcription factor families (STAT family, IRF family) co-regulate macrophage polarization and partially confound NF-κB-only attribution.
- The model does not fully accommodate the IL4I1+ PD-L1+ IDO1+ TAM cluster from MoMac-VERSE, which has both M1 and M2 features.

## Linked ideas

(none yet)

## Open questions

- Direct dimer-composition measurement (ChIP-seq for p65 vs p50 vs heterodimer) in TAMs from human tumors.
- Hypoxia-specific dimer composition: do hypoxic TAMs have different p50:p65 ratios than normoxic TAMs?
- Cross-talk with HIF-1α: when HIF-1α and NF-κB co-bind hypoxic enhancers ([[claims/hif1a-p65-cooperate-promoter-regions-without]]), is the relevant NF-κB dimer p65-p50 (M1-favoring) or p50-p50 (M2-favoring)?
- Therapeutic strategy: drugs that bias dimer composition vs drugs that block NF-κB pathway entirely.
