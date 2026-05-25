---
title: "KRTCAP2 — Keratinocyte-Associated Protein 2 — pan-cancer prognostic biomarker and N-glycosylation modulator"
aliases:
  - "KRTCAP2"
  - "Keratinocyte-Associated Protein 2"
  - "KCP2"
  - "OST complex accessory subunit KRTCAP2"
  - "KRTCAP2 oncogene"
  - "KRTCAP2 immune-exclusion biomarker"
  - "N-glycosylation pan-cancer biomarker"
  - "KRTCAP2 prognostic gene"
  - "KRTCAP2 Treg-associated marker"
  - "KRTCAP2 HCC gastric uveal melanoma biomarker"
tags:
  - KRTCAP2
  - pan-cancer
  - biomarker
  - N-glycosylation
  - immune-exclusion
  - prognosis
  - drug-target
maturity: emerging
key_papers:
  - development-hypoxia-responsive-macrophage-prognostic-model
first_introduced: "Liu et al. 2021 (uveal melanoma); Lee et al. 2022 (gastric); Sun et al. 2023 Colloids Surf B (HCC); Ge et al. 2025 (PDAC + pan-cancer)"
date_updated: 2026-05-25
related_concepts:
  - hypoxia-pd-l1-tam-immune-evasion
---

## Definition

KRTCAP2 (Keratinocyte-Associated Protein 2; also KCP2) encodes a small membrane-anchored accessory subunit of the oligosaccharyltransferase (OST) complex involved in N-linked glycosylation of nascent polypeptides at the ER. Originally annotated as keratinocyte-enriched, KRTCAP2 is now recognised as a pan-cancer prognostic marker: expression is elevated in tumour vs adjacent normal tissue across most TCGA types, escalates with stage, and correlates with poor OS, DSS, DFS, and PFS in nearly all tested malignancies. KRTCAP2 expression also tracks an immune-excluded / Treg-enriched TME signature across cancers, and is one of 13 genes in the Ge 2025 PDAC hypoxia-responsive-macrophage prognostic model.

## Intuition

KRTCAP2 is the kind of gene that nucleates a pan-cancer biomarker story: its expression is regulated, its protein product participates in a near-universal cellular process (N-glycosylation), and its product can plausibly modify many downstream cell-surface signals (PD-L1, MHC, integrins, mucins). It first emerged from prognostic gene-discovery work in HCC, gastric and uveal melanoma; Ge 2025 extends it as a pan-TCGA story by anchoring its discovery in PDAC hypoxia biology.

## Formal notation

- Function: OST complex accessory subunit, regulates ribosomal binding to translocon and N-glycosylation throughput at the ER membrane.
- Pan-cancer behaviour (Ge 2025, Fig 7A–G): HR>1 for OS/DSS/DFS/PFS across most TCGA types; overexpressed in tumour vs normal; stage-escalating.
- Immune correlations (Ge 2025): negative with CD8+ T, γδ T, CD4+ memory-activated, M1 macrophages, activated DCs, neutrophils, monocytes, resting mast; positive with Tregs.

## Variants

- Tissue context: KRTCAP2 effect sizes vary by cancer type; strongest reports in HCC, gastric, uveal melanoma, PDAC.
- KRTCAP2 may act via OST-complex throughput or via independent membrane-protein interactions; mechanism not resolved.

## Comparison

- vs other OST subunits (DDOST, STT3A/B, RPN1/2): KRTCAP2 is the smallest accessory subunit; its prognostic enrichment is more specific than core OST subunits.
- vs CD276/B7-H3, TROP2, FAP as pan-cancer biomarkers: KRTCAP2 is intracellular / ER-resident, so it is a *prognostic* biomarker rather than a directly druggable surface antigen — it nominates the OST pathway, not itself, as a therapeutic target.

## When to use

- When constructing pan-cancer prognostic gene panels for biomarker discovery.
- When interrogating links between glycosylation throughput and immune-exclusion phenotypes.
- When generating hypotheses for OST-pathway pharmacological inhibition (e.g. NGI-1).

## Known limitations

- Most evidence is correlative bulk-RNA TCGA-based; no causal perturbation in immune-competent cancer models.
- Pan-cancer claims rely on CIBERSORT/LM22 deconvolution, which has known limitations.
- No direct measurement of OST activity or N-glycosylation output as a function of KRTCAP2 dose.

## Open problems

- Causal: does KRTCAP2 knockdown reduce tumour growth and increase CD8+ infiltration in immune-competent models?
- Mechanism: is the Treg / CD8 phenotype mediated by N-glycosylation of a specific surface ligand (PD-L1, MHC-I, sialylated mucin)?
- Therapeutic: does NGI-1 or other OST inhibitors phenocopy KRTCAP2 loss?

## Key papers

- [[papers/development-hypoxia-responsive-macrophage-prognostic-model]] — Ge et al. 2025 PDAC + pan-cancer analysis surfacing KRTCAP2 as a recurrent prognostic gene.

## My understanding

KRTCAP2 is a plausible candidate biomarker but the supporting evidence (Ge 2025 + 3 prior single-cancer reports) is entirely bulk-RNA correlative. For thesis-relevant reasoning it deserves the category "interesting hypothesis-generating gene, not yet causally validated."
