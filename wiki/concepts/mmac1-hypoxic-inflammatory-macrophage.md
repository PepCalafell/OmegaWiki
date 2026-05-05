---
title: "mMAC₁ — Hypoxic Inflammatory Macrophage"
aliases: [mMAC1, hypoxic inflammatory macrophage, hypoxic activated macrophage, mature MAC under 1% O2]
tags: [macrophages, hypoxia, immunology, tumor-microenvironment, dna-methylation, in-vivo-correlate]
maturity: emerging
key_papers: [nf-kb-tet2-promote-macrophage-reprogramming]
first_introduced: "2024 (de la Calle-Fabregat et al., Sci Adv)"
date_updated: 2026-05-05
related_concepts: [nfkb-hif1a-cooperative-binding]
---

## Definition

mMAC₁ denotes a *mature human macrophage* differentiated from peripheral CD14⁺ monocytes in the presence of M-CSF for 5 days under 1% O₂ (hypoxia) and then activated with LPS for 48 h. By construction, mMAC₁ is the hypoxic counterpart of mMAC₂₁ (LPS-activated 21% O₂ MAC). The cell is operationally defined by:

- secreted IL-6 / TNF-α / lower IL-10 vs mMAC₂₁,
- elevated HLA-DR / CD80 / CD86, reduced CD14 / CD206 / CD163,
- reduced suppression of allogeneic CD8⁺ T-cell proliferation,
- a hypoxia-specific DNA-demethylation cluster (C2) at NF-κB-bound LPS-induced enhancers including *IL6* and *TNF*.

## Intuition

mMAC₁ is the empirical counterpoint to "hypoxia → immunosuppressive TAM". When the only TME-derived signal a macrophage receives is low O₂, the cell does *not* default to suppressive M2-like behaviour; it acquires a *more* proinflammatory, antigen-presenting, T-cell–activating phenotype than its normoxic LPS-activated counterpart. The phenotype is portable: an mMAC₁ gene-expression signature plus an mMAC₁ C2 methylation signature both map onto specific in-vivo human MO/MAC populations (notably IL4I1, IL1B Mo, ISG Mo in MoMac-VERSE) and IL4I1⁺ tumor MACs sorted from primary ovarian carcinoma.

## Formal notation

Defined relative to a 4-condition factorial: O₂ ∈ {21%, 1%} × LPS ∈ {–, +}. The four labels are iMAC₂₁, mMAC₂₁, iMAC₁, mMAC₁.

Cluster C2 = {CpGs with FDR < 0.05 and Δβ > 0.2 hypomethylation specifically in mMAC₁ relative to mMAC₂₁} — n ≈ 403 CpGs in the original analysis.

mMAC₁ signature genes: cluster E2 (LPS-up DEGs) ∩ C2-associated genes (Fisher P = 3.03·10⁻⁴⁴).

## Variants

- **iMAC₁**: 1% O₂, no LPS — primed but not yet inflammatory; some intermediate methylation already present at C2.
- **In-vivo equivalents**: IL4I1 Mac (MoMac-VERSE #6), IL1B Mo (#15), ISG Mo (#4) co-expressing the highest fraction of mMAC₁ signature genes.
- **Distinct from M(LPS)** under standard normoxia (mMAC₂₁) and from TREM2⁺/FOLR2⁺ tumor MAC programs which carry the *opposite* prognostic association.

## Comparison

vs **mMAC₂₁**: more proinflammatory, less suppressive, higher MHC-II / costimulatory marker expression, distinct C2 demethylation footprint at NF-κB sites.

vs **TREM2 TAM**: TREM2⁺ MACs are immunosuppressive and associated with poor prognosis in 7/12 TCGA cancer types; mMAC₁/IL4I1 are associated with *better* prognosis.

vs **Classical M1**: M1 is a normoxic LPS+IFNγ construct; mMAC₁ retains LPS but adds the hypoxia-specific NF-κB-mediated demethylation layer that is absent in classical M1 protocols.

## When to use

- When discussing TAM heterogeneity in hypoxic tumor regions (BLCA, OC, and at least 7/12 TCGA cancer types).
- When designing therapeutics aimed at *enhancing* TAM immunogenicity rather than depleting TAMs wholesale.
- When mapping in-vitro MO-derived MAC subtypes to single-cell tumor atlases (MoMac-VERSE).

## Known limitations

- Defined under a single inflammatory stimulus (LPS); other PAMPs/cytokines reproduce the boost qualitatively but not quantitatively.
- Not a tissue-resident MAC ontogeny; covers MO-derived MACs only.
- Survival correlation is observational — causal contribution to T-cell infiltration is inferred from ligand-receptor analysis, not yet proven by in-vivo perturbation.

## Open problems

- A clean genetic loss-of-function to confirm p65 vs HIF1α partitioning at C2 in vivo.
- Whether non-LPS TME ligands (TGF-β, IL-10, lactate) can collapse mMAC₁ back to a suppressive state.
- Time-resolved methylome+transcriptome to settle whether C2 demethylation precedes or follows transcriptional activation.

## Key papers

- [[nf-kb-tet2-promote-macrophage-reprogramming]] — defines mMAC₁ in vitro and validates its in vivo correlate.

## My understanding

mMAC₁ is best treated as a *defined assay readout* (the 1% O₂ + LPS condition) plus a *portable signature* (C2 CpGs + E2 ∩ C2 genes) rather than a fixed in-vivo cell type. Its value is that the same signature carries through MoMac-VERSE, TCGA bulk deconvolution, and FACS-sorted primary ovarian MACs. Anyone using "mMAC₁" should be explicit about which of the three (assay condition / expression signature / methylation signature) they mean — the paper uses the term across all three.
