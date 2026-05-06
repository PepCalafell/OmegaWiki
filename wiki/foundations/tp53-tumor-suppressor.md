---
title: "TP53 (Tumor Protein 53 / p53)"
slug: tp53-tumor-suppressor
domain: "molecular-biology / oncology / DNA-damage-response"
status: mainstream
aliases:
  - "TP53"
  - "p53"
  - "tumor protein p53"
  - "guardian of the genome"
  - "TRP53 (mouse)"
  - "Li-Fraumeni syndrome gene"
  - "cellular tumor antigen p53"
first_introduced: "Lane & Crawford 1979; Linzer & Levine 1979"
date_updated: 2026-05-06
source_url: "https://www.uniprot.org/uniprot/P04637"
---

## Definition

TP53 is the most frequently mutated gene in human cancer, encoding a sequence-specific transcription factor that integrates cellular stress signals (DNA damage, oncogene activation, hypoxia, oxidative stress) and induces cell-cycle arrest, senescence, or apoptosis through transactivation of target genes (CDKN1A/p21, BAX, PUMA, MDM2). Wild-type p53 acts as a tetramer; missense mutations in the DNA-binding domain are dominant-negative or gain-of-function and yield characteristic protein accumulation due to lost MDM2-mediated turnover.

## Intuition

p53 is the cell's stress integrator and apoptosis trigger. Hypoxia is one of the canonical p53-activating stresses (Graeber et al. 1996 Nature). Tumors that retain wild-type p53 are biased toward apoptosis under low O₂; tumors with mutant p53 escape this selection, expanding hypoxia-tolerant clones. This selective pressure is the proposed mechanistic link between hypoxia and TP53 mutation in solid tumors.

## Formal notation

- Encoded by TP53 (chr17p13.1 in human; 393 aa)
- Domains: TAD1, TAD2, proline-rich, DNA-binding (DBD, residues 102–292), tetramerization (323–356), C-terminal regulatory
- Most frequent missense hotspots: R175, G245, R248, R249, R273, R282 — DNA-binding contact / structural
- Activated by: ATM/ATR phosphorylation (Ser15, Ser20), USP7-mediated stabilization
- Inactivated by: MDM2 ubiquitination (under normal conditions); p53 transactivates MDM2 → negative feedback
- Hallmark targets: CDKN1A (cell-cycle arrest), BAX/PUMA/NOXA (apoptosis), MDM2 (feedback), GADD45 (DNA repair)

## Key variants

- Germline TP53 mutation → Li-Fraumeni syndrome (early-onset multi-tumor predisposition)
- Mutant TP53 isoforms: R175H, R273H widely used as gain-of-function alleles in mouse models
- Loss-of-function via deletion (less common than missense in tumors)
- Splicing isoforms: Δ40p53, Δ133p53, p53β, p53γ — differential transactivation

## Known limitations

- "TP53 mutation" lumps together loss-of-function, dominant-negative, and gain-of-function mutants with distinct biology.
- IHC-based p53 assays detect *accumulated* mutant protein, missing some loss-of-function null mutants.
- Pancancer mutation calling depends on cohort and pipeline; subclonal TP53 mutations are often missed by bulk sequencing.

## Open problems

- Whether TP53 mutation is a genomic *consequence* of hypoxia (Graeber model: hypoxia selects for apoptosis-deficient subclones) versus an independent oncogenic event is debated; large-scale evidence from [[papers/molecular-landmarks-tumor-hypoxia-across-cancer]] supports the consequence hypothesis but does not prove causality.
- Therapeutic restoration of mutant p53 function (APR-246, eprenetapopt) shows mixed clinical results.

## Relevance to active research

TP53 SNVs are the most consistent pancancer correlate of tumor hypoxia in [[papers/molecular-landmarks-tumor-hypoxia-across-cancer]] (BRCA p=4.38×10⁻⁶¹; LUAD p=1.83×10⁻¹²; multiple tumor types). The paper proposes mutant TP53 as a pillar of the "nimbosus" aggressive phenotype in localized prostate cancer and frames the result as "TP53 mutations may be a genomic consequence of tumor hypoxia."
