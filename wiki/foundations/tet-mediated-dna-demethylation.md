---
title: "TET-mediated DNA demethylation"
slug: tet-mediated-dna-demethylation
domain: "epigenetics"
status: mainstream
aliases: [TET, ten-eleven translocation, TET2, 5hmC, 5-hydroxymethylcytosine, active demethylation]
first_introduced: "2009 (Tahiliani et al., discovery of TET1; subsequent TET2/TET3 characterization)"
date_updated: 2026-05-05
source_url: "https://www.ncbi.nlm.nih.gov/gene/54790"
---

## Definition

TET methylcytosine dioxygenases (TET1, TET2, TET3) are α-ketoglutarate / Fe²⁺ / O₂-dependent enzymes that catalyze sequential oxidation of 5-methylcytosine (5mC) to 5-hydroxymethylcytosine (5hmC), 5-formylcytosine (5fC), and 5-carboxylcytosine (5caC). Subsequent base-excision repair (TDG-mediated) restores unmethylated cytosine, completing **active DNA demethylation**.

## Intuition

If DNMT enzymes (DNMT1/3A/3B) write CpG methylation, TET enzymes are the *erasers* that actively remove it. They require oxygen as a substrate, so TET activity scales with O₂ availability — making TETs a natural epigenetic node where physiology of oxygen meets the regulation of gene expression.

## Formal notation

Reaction:
- 5mC + α-KG + O₂ —[TET, Fe²⁺]→ 5hmC + succinate + CO₂
- 5hmC → 5fC → 5caC by further TET oxidation
- 5fC/5caC → C by TDG + BER

Cofactor sensitivities:
- O₂: Km in the range that makes TET partially inactive at < 5% O₂.
- α-KG: depleted by IDH1/2 mutations producing 2-HG (R-2HG inhibits TETs).
- Itaconate (Mn²⁺-coordinating immunometabolite): inhibits TET2; 4-octyl itaconate is the cell-permeable analogue used in macrophage studies.

## Key variants

- **TET1** — embryonic / pluripotent contexts; CpG-island bias.
- **TET2** — most haematopoietic; mutated in clonal haematopoiesis and AML; principal TET in macrophages.
- **TET3** — neuronal contexts and zygotic paternal demethylation.

## Known limitations

- TET activity depends on O₂; under prolonged hypoxia global hypermethylation is the *expected* default.
- Distinguishing 5mC from 5hmC requires bisulfite-based assays paired with specific 5hmC chemistry (oxBS-seq, TAB-seq) or antibody-based readouts.
- Catalytic-independent functions of TETs (chromatin scaffolding, OGT recruitment) complicate "TET inhibitor → demethylation loss" interpretations.

## Open problems

- Locus-specific TET2 recruitment under hypoxia: how does p65 binding license TET2-mediated demethylation when global TET activity is reduced (cf. [[nf-kb-tet2-promote-macrophage-reprogramming]])?
- The kinetics of 5mC→5hmC→C at NF-κB-bound enhancers vs TF-binding events.
- Therapeutic windows for itaconate-class TET inhibitors that differentially modulate TAM vs other myeloid phenotypes.

## Relevance to active research

Foundation across haematological malignancy, macrophage biology, neurobiology, and regenerative medicine. In TAM biology, TET2 is the principal active demethylation engine and is targeted by both metabolic (itaconate) and pharmacological (4-octyl itaconate) interventions. TET-mediated demethylation is also load-bearing in the [[mmac1-hypoxic-inflammatory-macrophage]] phenotype, where p65-licensed TET activity rewrites the inflammatory enhancer landscape in 1% O₂.
