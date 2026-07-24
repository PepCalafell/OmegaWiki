---
title: "Cell-cycle-dependent transient normoxic HIF-1α stabilization in HCC"
aliases:
  - "normoxic cell-cycle HIF-1α"
  - "G2/M HIF-1α stabilization"
tags:
  - HIF1a
  - hypoxia
  - normoxia
  - cell-cycle
  - CDK1
  - hepatocellular-carcinoma
  - oxygen-independent
maturity: emerging
key_papers:
  - oxygen-independent-expression-hif-during-cell
first_introduced: "Gkotinakou et al. 2026 (FEBS J), building on Warfel/CDK1 work in colon carcinoma"
date_updated: 2026-07-24
related_concepts:
  - warburg-effect-hif1a-glycolytic-reprogramming
  - hif1a-nf-kb-cooperative-chromatin-binding
---

## Definition

In some cancer cells (notably hepatocellular carcinoma lines Huh7 and HepG2), HIF-1α is expressed **transiently under normoxia** in a cell-cycle-dependent manner, peaking at the G2→M transition and declining into G1. Because this pulse occurs only in a small, cell-cycle-restricted subpopulation, HIF-1α appears undetectable in asynchronous normoxic cultures yet still exerts substantial transcriptional/metabolic control. The stabilization is not due to loss of proline hydroxylation but to a **block in HIF-1α ubiquitination and proteasomal degradation** at that cell-cycle phase, coincident with the CDK1/cyclin B1 peak.

## Intuition

HIF-1α is normally destroyed within minutes under normoxia. But at G2/M, active CDK1 (which can phosphorylate HIF-1α at Ser668) transiently shields it from ubiquitination, producing a brief normoxic "pulse" of HIF-1 activity. Averaged over an asynchronous culture the pulse is invisible — but synchronize the cells and it becomes detectable, explaining how HIF-1α can drive metabolism "under normoxia" without steady-state expression.

## Formal notation

- Detected by synchronizing cells with the CDK1 inhibitor [[foundations/ro-3306-cdk1-inhibitor]] (5 µM, ~18–20 h) then releasing; HIF-1α appears ~5–8 h post-release (G2→M), coincident with rising cyclin B1 and a CDK1 peak
- Immunoprecipitated normoxic G2/M HIF-1α is (at least partially) proline-hydroxylated but not substantially ubiquitinated
- Not observed in HeLa cells → cell-type-specific

## Variants

- Reported precedent in colon carcinoma cells (CDK1-Ser668 phosphorylation stabilizes HIF-1α at G2/M)
- Cyclin E–driven G1 HIF-1α expression in mammary epithelial cells (E2F1-dependent + EGLN1/PHD2 downregulation) is a related but distinct cell-cycle route

## Comparison

- Distinct from canonical hypoxic HIF-1α stabilization (PHD inactivation by low O₂)
- Distinct from oncogene/pseudohypoxic HIF-1α stabilization (e.g. VHL loss); here O₂ and VHL are intact
- Complements oxygen-independent transcriptional/translational HIF-1α induction (NF-κB, STAT3, PI3K/AKT) — see [[concepts/hif1a-nf-kb-cooperative-chromatin-binding]]

## When to use

Invoke when explaining how HIF-1 target genes (glycolysis, cholesterol/steroid biosynthesis) can be maintained in well-oxygenated cancer cells, or when reconciling "undetectable HIF-1α" with a functional normoxic HIF-1 signature.

## Known limitations

- Demonstrated in HCC lines (Huh7, HepG2) in vitro; in vivo/patient-tumor evidence for the cell-cycle pulse is indirect (signature correlations)
- Mechanism (ubiquitination block) inferred from a single IP timepoint; direct CDK1→HIF-1α causality not perturbed genetically here

## Open problems

- Which E3-ligase step is blocked, and how CDK1 activity gates it
- Whether the pulse synchronizes metabolism to specific cell-cycle checkpoints (G1/S metabolite demand)

## Key papers

- [[papers/oxygen-independent-expression-hif-during-cell]] — defines the cell-cycle-dependent normoxic HIF-1α pulse in HCC and its ubiquitination-block mechanism

## My understanding

A neat resolution of an apparent paradox: HIF-1α "does nothing under normoxia" only at the population average. The cell-cycle-gated pulse reframes HIF-1 as a constitutive metabolic controller in HCC, tying oxygen-independent HIF biology to the cell cycle — directly relevant to hypoxia-thesis questions about when HIF signaling is truly "off."
