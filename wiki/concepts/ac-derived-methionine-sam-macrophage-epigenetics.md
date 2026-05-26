---
title: "Apoptotic-cell-derived methionine fuels macrophage SAM and DNA methylation"
aliases:
  - "AC-methionine epigenetics"
  - "apoptotic-cell methionine SAM"
  - "efferocytosed methionine"
  - "AC cargo methionine"
  - "phagolysosomal methionine flux"
  - "corpse-derived methyl donor"
  - "engulfed methionine DNA methylation"
  - "isotope-tracked AC methionine"
  - "13C methionine efferocytosis"
  - "AC-derived metabolite signaling"
  - "phagocyte epigenetic cargo"
tags:
  - macrophage
  - efferocytosis
  - methionine
  - SAM
  - DNA-methylation
  - one-carbon-metabolism
  - epigenetics
  - metabolic-signaling
maturity: emerging
key_papers:
  - macrophages-use-apoptotic-cell-derived-methionine
first_introduced: "Ampomah 2022 Nat Metab"
date_updated: 2026-05-26
related_concepts:
  - dnmt3a-dusp4-efferocytosis-resolution-pathway
  - efferocytosis-anti-inflammatory-clearance
---

## Definition

A subset of methionine residues from engulfed apoptotic-cell proteins, after phagolysosomal degradation, is converted to S-adenosylmethionine (SAM) inside the efferocytosing macrophage. This AC-derived methionine pool is rate-limiting (or substantially contributing) to DNA-methyltransferase-driven methylation events on specific gene-regulatory loci. Isotope tracing (13C5,15N-methionine in apoptotic Jurkat cells → 13C5,15N-SAM and 13C-methylcytosine in macrophage DNA) demonstrates the metabolic route. The phenomenon generalises a broader concept: AC cargo metabolites are repurposed by phagocytes as epigenetic substrates, not just nutrient salvage.

## Intuition

Macrophages eat dying cells daily, recycling biomass. Ampomah 2022 shows that one fraction of this recycled biomass — methionine — is used not for protein synthesis but specifically to drive DNA methylation. This positions efferocytosis as a meta-signal: the *content* of the corpse (its methionine load) directly programs the engulfer's gene expression via epigenetic rewriting.

## Formal notation

- Source: methionine in AC proteins (intracellular pool + protein-bound)
- Route: phagolysosomal hydrolysis → macrophage cytosolic methionine pool → MAT2A → SAM
- Sink: DNA methyltransferases (DNMT3A in macrophages); possibly histone and small-molecule methyltransferases
- Tracing: 13C5,15N-methionine isotope label in Jurkat APCs; LC-MS/MS in sorted PKH26+ macrophages
- Block: bafilomycin A1 (blocks phagolysosomal degradation) abolishes 13C-SAM and 13C-mC in macrophages
- Block: MAT2A inhibition (PF-9366) abolishes 13C-SAM and 13C-mC; exogenous SAM bypasses

## Variants

- Methionine cycle recycling (SAH → homocysteine → methionine → SAM) may contribute a small additional pool
- Other AC-cargo amino acids feed parallel programs: arginine → ornithine/putrescine; cholesterol → LXR; fatty acids → IL-10
- Likely not specific to methionine: any AC-derived methyl-donor (e.g., choline) may contribute, untested

## Comparison

vs extracellular methionine in media: AC-derived methionine works even in methionine-free media — phagocytosed cargo is sufficient. Extracellular methionine is therefore not the rate-limiting substrate for efferocytosis-induced methylation events.
vs other AC metabolites (arginine, cholesterol): methionine→SAM works through *DNA methylation*; other AC metabolites work through TF activation or mRNA stabilisation. The epigenetic route is mechanistically distinct.

## When to use

- Interpreting how dietary methionine restriction may affect macrophage-mediated resolution
- Predicting that efferocytosis defects (impaired phagolysosomal digestion) impair downstream epigenetic programs even when uptake is intact
- Designing isotope-tracing experiments in macrophage biology

## Known limitations

- The relative contribution of AC-methionine vs endogenous macrophage methionine to total SAM is not quantitatively dissected
- The phenomenon is established for DNMT3A targets in macrophages; whether it extends to histone methyltransferases or other methyl-acceptors is untested in this paper
- Site-specificity of AC-methionine-derived methyl groups (e.g., do they preferentially land on Dusp4 vs random loci?) requires chromatin-resolved tracing

## Open problems

- Chromatin-resolved tracing: do AC-derived methyl groups deposit preferentially at specific loci (e.g., Dusp4) or genome-wide?
- Quantitative dissection of methionine source (AC vs media vs recycling)
- Whether other phagocytic targets (pathogens, debris) likewise contribute methionine to phagocyte epigenetic programs
- Generalisation to other professional phagocytes (DCs, tingible-body B-cell-clearing macrophages, RPE cells)
- Cross-talk with histone methylation and small-molecule methylation

## Key papers

- [[papers/macrophages-use-apoptotic-cell-derived-methionine]] — Ampomah et al. 2022 *Nat Metab* — original demonstration with isotope tracing + functional readouts

## My understanding

The phenomenon establishes phagocyte-cargo metabolite repurposing as an epigenetic mechanism, conceptually distinct from "phagocytes use AC cargo for energy/biomass." For tumour-associated macrophage biology, this suggests that the methionine load of dying tumour cells may directly program TAM epigenetic state — a potentially actionable axis in cancer immunology. For atherosclerosis, dietary methionine availability could modulate plaque macrophage resolution programs via this route. The framework also raises the question of whether efferocytosis-induced histone methylation is similarly fed by AC-derived methionine, which would extend the epigenetic-cargo idea beyond DNA into chromatin globally.
