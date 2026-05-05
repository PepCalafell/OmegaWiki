---
title: "HIF1α (Hypoxia-Inducible Factor 1 alpha)"
slug: hif1a
domain: "cell biology / oxygen sensing"
status: mainstream
aliases: [HIF-1α, HIF1A, hypoxia-inducible factor 1 alpha]
first_introduced: "1992 (Semenza & Wang)"
date_updated: 2026-05-05
source_url: "https://www.ncbi.nlm.nih.gov/gene/3091"
---

## Definition

HIF1α is the oxygen-sensitive subunit of the heterodimeric transcription factor HIF-1 (HIF1α / HIF1β/ARNT). Under normoxia, HIF1α is hydroxylated on conserved proline residues by PHD oxygen-dependent prolyl hydroxylases, ubiquitinated by the VHL E3 ligase, and degraded by the proteasome. Under hypoxia (~1–5% O₂ depending on cell type), PHD activity is suppressed, HIF1α accumulates, translocates to the nucleus, dimerizes with HIF1β, and binds hypoxia-response elements (HREs, consensus 5′-RCGTG-3′) to activate transcription of metabolic-adaptation, angiogenic, and survival genes.

## Intuition

HIF1α is the master sensor that lets cells switch from oxidative phosphorylation to glycolysis and induce angiogenesis when O₂ is scarce. It is essential in myeloid cells for proper inflammatory function (Cramer et al., 2003).

## Formal notation

- Gene: *HIF1A* (chr14q23.2 in human)
- Protein: 826 aa, contains bHLH-PAS DNA-binding domain, ODD (oxygen-dependent degradation) domain with hydroxylation sites P402/P564, NTAD/CTAD transactivation domains.
- Half-life under normoxia: ~5 min; under hypoxia: ~30+ min.
- Binding consensus: hypoxia-response element 5′-(A/G)CGTG-3′.

## Key variants

- **HIF1α** (this entry) — broadly expressed, drives the acute hypoxia response.
- **HIF2α (EPAS1)** — overlapping but distinct target sets, dominant in renal/endothelial/Kupffer contexts.
- **HIF3α** — multiple isoforms, several with dominant-negative activity.

## Known limitations

- HIF1α activity in inflammatory macrophages is *contextual*: pro- vs anti-inflammatory readouts differ across studies and cell-state.
- Pharmacological inhibitors (PX-478, echinomycin, BAY-87-2243) have polypharmacology and variably hit HIF1α vs HIF2α.
- Stabilization of HIF1α is also non-canonical: ROS, succinate accumulation (PHD inhibition), and certain inflammatory ligands can stabilize HIF1α independently of O₂.

## Open problems

- HIF1α-independent "hypoxia memory" effects in macrophages.
- HIF1α vs HIF2α selectivity in TAMs.
- Mechanistic basis of cooperation with NF-κB without obligate physical complex (see [[nfkb-hif1a-cooperative-binding]]).

## Relevance to active research

Foundation for hypoxia-related research across immunology, oncology, cardiovascular, and metabolic biology. In the macrophage / TAM literature it is invoked both as an immunosuppression driver (older view) and as an inflammation driver (newer view); the [[nf-kb-tet2-promote-macrophage-reprogramming]] paper resolves part of this contradiction by showing HIF1α handles metabolic adaptation while p65 handles inflammatory demethylation.
