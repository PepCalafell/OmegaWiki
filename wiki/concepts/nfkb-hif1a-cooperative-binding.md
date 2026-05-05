---
title: "NF-κB / HIF1α cooperative co-binding in hypoxic activated macrophages"
aliases: [HIF1α-p65 co-regulation, NF-κB and HIF1α cooperation, p65-HIF1α cobound peaks]
tags: [transcription-factors, hypoxia, nf-kb, hif, chip-seq, macrophages, cooperative-binding]
maturity: emerging
key_papers: [nf-kb-tet2-promote-macrophage-reprogramming]
first_introduced: "2024 (de la Calle-Fabregat et al., Sci Adv)"
date_updated: 2026-05-05
related_concepts: [mmac1-hypoxic-inflammatory-macrophage]
---

## Definition

A pattern of *non-obligate* co-regulation of inflammatory and hypoxia-response genes by HIF1α and the NF-κB p65 (RELA) subunit in human MO-derived macrophages activated under 1% O₂. ChIP-seq for the two TFs across iMAC₂₁/mMAC₂₁/iMAC₁/mMAC₁ resolves three HIF1α peak clusters (H1–H3) and one dominant p65 cluster (P1) plus a region of overlap. In overlap regions the binding *strengths* of HIF1α and p65 are not linearly correlated (Pearson r = 0.13), so the cooperation is functional/regulatory rather than the consequence of an obligate physical complex.

## Intuition

Two TFs share neighborhoods on the chromatin of hypoxic LPS-activated MACs but each retains a distinct primary motif preference and a distinct gene set:

- **HIF1α-only peaks** — glycolysis / NADH regeneration / canonical hypoxia adaptation.
- **Cobound peaks** — LPS / cellular response to bacterial stimulus / cytokine response.
- **p65-only peaks** — mononuclear cell differentiation / lymphocyte differentiation / cell-cell adhesion.

Critically, the C2 DNA-demethylation cluster co-localizes *exclusively* with p65-specific peaks, **not** HIF1α peaks. So the demethylation arm of the program is wholly p65's job; HIF1α contributes the metabolic-adaptation half.

## Formal notation

Let `H = HIF1α peaks ∪ {H1,H2,H3}` and `P = p65 peaks ∪ P1`. Define:

- HIF1α-specific = H \ P
- p65-specific = P \ H
- cobound = H ∩ P

Then for cobound regions, motif analysis centered on either TF returns predominant HIF1α motif enrichment, with weaker p65 motif enrichment. Binding intensities `(log2 RPKM_HIF1α, log2 RPKM_p65)` over cobound peaks have Pearson r ≈ 0.13 (P = 2.5·10⁻⁴), refuting a "tight complex" hypothesis. C2 ∩ cobound ≈ ∅ in mMAC₁; C2 ⊂ p65-specific.

## Variants

- **mMAC₂₁ baseline**: cobound peaks exist but with low p65 binding intensity and no C2 demethylation.
- **Activation in normoxia (LPS axis only)**: p65 dominant; HIF1α weak.
- **Hypoxia without LPS (iMAC₁)**: HIF1α-driven peaks without the demethylation-coupled inflammatory boost.

## Comparison

- vs **classical "HIF inflammatory program"** (Cramer et al., Palazon et al.): those frame HIF1α as the inflammatory TF; this paper's ChIP+demethylation evidence reassigns the inflammatory-demethylation arm to p65 and confines HIF1α to metabolic adaptation in the macrophage context.
- vs **physical TF-TF complexes** (e.g., NF-κB / Rel-Rel dimers): no evidence of a bound complex here; cooperation is regulatory at the level of shared chromatin, not pairwise interaction.

## When to use

- Modelling hypoxia-driven inflammatory programs in macrophages.
- Designing pharmacological dissection studies that need to separate HIF and NF-κB contributions.
- Reading TF-TF "co-occupancy" claims critically — co-localization at the same regions does not imply correlated binding strengths or shared functional readout.

## Known limitations

- ChIP-seq cannot distinguish co-occupancy in the *same cell* vs alternating occupancy across cell subpopulations; fixed-cell technology averages over them.
- The r = 0.13 statistic argues against linear coupling but does not rule out non-linear / threshold cooperation.
- No genetic perturbation of HIF1α to test whether HIF1α loss reshapes the p65 peak landscape.

## Open problems

- Identifying the exact mechanism by which p65 binding licenses local TET2 demethylation under O₂-restricted conditions.
- Whether HIF1α-specific peaks contribute *indirectly* (via metabolite/itaconate axes) to p65-driven demethylation downstream.
- Generalizing the pattern beyond M-CSF MACs to GM-CSF MACs and tissue-resident TAM lineages.

## Key papers

- [[nf-kb-tet2-promote-macrophage-reprogramming]] — primary source.

## My understanding

The most useful piece of this concept is the *separation of labour* between HIF1α (hypoxia adaptation) and p65 (inflammatory demethylation), and the correctness check that cobinding ≠ correlated binding. Anyone designing a follow-up should respect both: pharmacological inhibition of one TF should not be expected to wipe the other's footprint, and "co-occupancy" headcounts in cobound peak sets should always be paired with binding-intensity correlations.
