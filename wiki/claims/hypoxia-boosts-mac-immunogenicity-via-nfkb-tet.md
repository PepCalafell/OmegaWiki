---
title: "Hypoxia boosts macrophage immunogenicity via NF-κB-driven, TET-mediated demethylation of inflammatory enhancers — p65, not HIF1α, is the demethylation driver"
slug: hypoxia-boosts-mac-immunogenicity-via-nfkb-tet
status: supported
confidence: 0.75
tags: [macrophages, hypoxia, nf-kb, tet2, hif1a, dna-methylation, inflammation, mechanism]
domain: "immunology / epigenetics"
source_papers: [nf-kb-tet2-promote-macrophage-reprogramming]
evidence:
  - source: nf-kb-tet2-promote-macrophage-reprogramming
    type: supports
    strength: strong
    detail: "Cluster C2 (≈403 CpGs) is hypoxia-specifically demethylated in mMAC₁; C2 sits exclusively under p65-specific ChIP-seq peaks (not HIF1α). BAY11-7082 (p65 inhibitor) — but not PX-478 (HIF1α inhibitor) — restores C2 methylation to mMAC₂₁-like levels and blocks IL6/IRF1/NFKB1/CCL5 mRNA up-regulation. 4-octyl itaconate (TET inhibitor) confirms demethylation is required for the inflammatory boost. Cobound HIF1α/p65 peaks show no linear correlation in binding intensity (r=0.13)."
conditions: "Established in human peripheral MO-derived MACs differentiated 5 days with M-CSF in 1% vs 21% O₂ and activated with LPS (or PAMPs / TNF-α / IL-1β) for 48 h. Generalization to GM-CSF MACs, tissue-resident TAMs, and other inflammatory ligands not yet established."
date_proposed: 2026-05-05
date_updated: 2026-05-05
---

## Statement

In human macrophages activated under hypoxia (1% O₂), the NF-κB p65 subunit — and *not* HIF1α — is the primary driver of locus-specific TET-mediated DNA demethylation at a cluster of inflammatory enhancers (cluster C2, including *IL6* and *TNF*). This demethylation is required for the hypoxia-specific overexpression of proinflammatory cytokines and confers an *enhanced* immunogenic phenotype on hypoxic-activated MACs (mMAC₁) — directly contradicting the prevailing view that hypoxia is uniformly immunosuppressive on macrophages.

## Evidence summary

- **DNA methylation (EPIC arrays)**: Cluster C2 (≈403 CpGs, FDR<0.05, |Δβ|>0.2) is specifically demethylated in mMAC₁ vs mMAC₂₁; enriched in NF-κB-family motifs.
- **Transcriptomics (bulk RNA-seq)**: Cluster E2 (LPS-up DEGs) is significantly enriched among C2-associated genes (Fisher P = 3.03·10⁻⁴⁴).
- **TF binding (ChIP-seq HIF1α + p65)**: C2 CpGs co-localize exclusively with p65-specific peaks; cobound HIF1α/p65 regions do not show C2 demethylation. Pearson r between HIF1α and p65 binding intensities at cobound peaks = 0.13 (P = 2.5·10⁻⁴).
- **Pharmacological dissection (Fig. 4K–L of source)**: BAY11-7082 (p65i) restores C2 methylation and blocks inflammatory mRNA boost; PX-478 (HIF1αi) does not; 4-octyl itaconate (TET inhibitor) blocks demethylation and reduces mRNA, confirming demethylation is mechanistically required.
- **Cross-stimulus replication**: P3C, CpG, polyI:C, TNF-α, IL-1β all reproduce the hypoxia inflammatory boost qualitatively (fig. S2E of source) — argues for NF-κB-driven, not stimulus-specific, mechanism.
- **In vivo correlate**: mMAC₁ signature (C2 + E2 ∩ C2 genes) is enriched in IL4I1 / IL1B / ISG MAC populations in MoMac-VERSE and in IL4I1⁺ ovarian tumor MACs sorted from primary tissue.

## Conditions and scope

Holds under:
- Human peripheral CD14⁺ MO-derived MACs.
- M-CSF differentiation (5 days) under 1% vs 21% O₂.
- LPS or other inflammatory stimuli for 48 h.

Not yet established for:
- GM-CSF MACs (where the inflammatory program differs).
- Tissue-resident TAM lineages of non-monocyte origin.
- Co-presented suppressive ligands (TGF-β, IL-10, lactate).
- Genetic loss of function for HIF1α / p65 / TET2 (only pharmacological dissection so far).

## Counter-evidence

- Older literature (Murdoch & Lewis, Henze & Mazzone) frames hypoxia in TAMs as immunosuppressive; the source paper attributes much of the inconsistency to use of mixed/co-presented suppressive ligands rather than isolated O₂ restriction.
- Some HIF1α studies in myeloid cells (Cramer et al. 2003) ascribe the inflammatory program directly to HIF1α; this claim refines that view by partitioning HIF1α (metabolic adaptation) and p65 (inflammatory demethylation).

## Linked ideas

(none yet — would attach future ideation about therapeutically inducing mMAC₁ in vivo)

## Open questions

- Mechanism of locus-specific TET2 recruitment by p65 under O₂-restricted conditions.
- Whether p65-driven demethylation precedes or follows transcriptional activation (time-resolved methylome+transcriptome required).
- Robustness of the partition (HIF1α metabolic vs p65 inflammatory) in non-LPS contexts and tissue-resident TAM lineages.
- Genetic / CRISPR validation of HIF1α-independence of C2 demethylation.
