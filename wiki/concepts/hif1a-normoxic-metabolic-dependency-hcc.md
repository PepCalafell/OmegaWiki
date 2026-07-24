---
title: "HIF-1α-dependent normoxic metabolic reprogramming in hepatocellular carcinoma"
aliases:
  - "normoxic HIF-1α metabolic dependency HCC"
  - "HIF-1α glycolysis and cholesterol under normoxia"
tags:
  - HIF1a
  - hypoxia
  - normoxia
  - glycolysis
  - cholesterol
  - steroid-biosynthesis
  - hepatocellular-carcinoma
  - cancer-metabolism
maturity: emerging
key_papers:
  - oxygen-independent-expression-hif-during-cell
first_introduced: "Gkotinakou et al. 2026 (FEBS J)"
date_updated: 2026-07-24
related_concepts:
  - warburg-effect-hif1a-glycolytic-reprogramming
  - normoxic-cell-cycle-dependent-hif1a-hcc
---

## Definition

In hepatocellular carcinoma cells, HIF-1α is required to maintain the expression of enzymes in two core biosynthetic/energetic pathways — **glycolysis/gluconeogenesis** and **steroid/cholesterol biosynthesis** — even under normoxia (21% O₂), and not only under hypoxia. CRISPR/Cas9 HIF1A knockout in Huh7 cells reduces glycolytic enzyme levels (HK2, GAPDH; confirmed in HepG2) and steroid/cholesterol biosynthetic enzymes plus total cellular cholesterol, and impairs normoxic growth/survival. This normoxic metabolic dependency is HCC-specific: it is absent in HeLa cells, where these pathways are not HIF-1α-dependent under normoxia.

## Intuition

HCC cells behave as if hypoxic even when oxygenated: HIF-1 keeps the glycolytic and lipid/cholesterol biosynthetic machinery running to feed rapid liver-cancer-cell proliferation. Remove HIF-1α and the well-oxygenated HCC cell loses ~a quarter of its regulated proteome, its cholesterol supply, and its ability to grow — a vulnerability not shared by non-hepatic HeLa cells.

## Formal notation

- ~26% of the Huh7 proteome (vs ~10% in HeLa) is differentially expressed upon HIF1A knockout under normoxia
- KEGG-enriched HIF-1α-upregulated normoxic pathways in Huh7: carbon metabolism, glycolysis/gluconeogenesis, steroid biosynthesis (also terpenoid/pyruvate, HIF-1 signaling)
- HIF-1α-downregulated (upregulated in KO): oxidative phosphorylation, TCA cycle, pentose phosphate pathway components
- Total cholesterol (free + esters) reduced in HIF1A⁻/⁻ Huh7 under both normoxia and hypoxia; unchanged in HeLa

## Variants

- Hypoxic HIF-1 glycolytic reprogramming (the classic Warburg axis) — see [[concepts/warburg-effect-hif1a-glycolytic-reprogramming]]
- Cell-type-specific coactivator repertoires proposed to explain why HeLa lacks this dependency

## Comparison

- Extends the Warburg/HIF glycolysis paradigm from hypoxia into normoxia and adds a cholesterol/steroid biosynthetic arm
- Mechanistically enabled by the cell-cycle-gated normoxic HIF-1α pulse ([[concepts/normoxic-cell-cycle-dependent-hif1a-hcc]])
- Proteomic (protein-level) readout, distinct from prior transcriptomic HIF-target studies that may not reflect protein changes

## When to use

Invoke when arguing that HIF-1α is a therapeutic vulnerability in HCC irrespective of tumor oxygenation, or when distinguishing cell-type-specific normoxic HIF-1 metabolic control from generic hypoxic glycolysis.

## Known limitations

- In vitro cell-line evidence (Huh7, HepG2, HeLa); no in vivo metabolic tracing
- Signature-to-survival link is correlative (TCGA/GEPIA2 mRNA), not causal
- Two biological replicates for core proteomics (third confirmatory replicate)

## Open problems

- Whether normoxic HIF-1α-dependent cholesterol supply is druggable in HCC without hypoxia-targeting
- Contribution of HIF-1-dependent amino-acid/glucose transporter induction to the growth phenotype

## Key papers

- [[papers/oxygen-independent-expression-hif-during-cell]] — proteomic demonstration of HCC-specific normoxic HIF-1α control of glycolysis and cholesterol/steroid biosynthesis

## My understanding

The most clinically suggestive part of the paper: HIF-1α inhibition might damage HCC cells even in normoxic tumor regions, because the cells depend on HIF-1 for baseline biosynthesis, not just hypoxic survival. The cholesterol/steroid arm is an underappreciated, potentially targetable node.
