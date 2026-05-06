---
title: "TERT (Telomerase Reverse Transcriptase)"
slug: tert-telomerase
domain: "molecular-biology / oncology / telomere-biology"
status: mainstream
aliases:
  - "TERT"
  - "telomerase reverse transcriptase"
  - "hTERT"
  - "telomerase catalytic subunit"
  - "EST2 (yeast homolog)"
  - "TP2"
  - "TRT"
first_introduced: "Greider & Blackburn 1985 (telomerase activity); Meyerson et al. 1997 Cell (TERT cloning)"
date_updated: 2026-05-06
source_url: "https://www.uniprot.org/uniprot/O14746"
---

## Definition

TERT is the catalytic protein subunit of telomerase, the ribonucleoprotein reverse-transcriptase complex that adds TTAGGG repeats to chromosome ends using its RNA component (TERC) as template. TERT is a HIF1A target — its expression is induced under hypoxia — and its reactivation is a hallmark of human cancer, with promoter mutations (C228T, C250T) being among the most common non-coding mutations in solid tumors.

## Intuition

TERT is the "immortality switch" of cancer cells. Most somatic cells express little to no telomerase, so each division shortens telomeres until replicative senescence. Cancers reactivate TERT (via promoter mutation, gene amplification, structural rearrangement, or transcriptional induction by HIF1A/MYC) to escape this barrier. Hypoxia upregulates TERT through HIF1A binding at the TERT promoter, providing a metabolic-stress link to telomere maintenance.

## Formal notation

- Encoded by TERT (chr5p15.33 in human; 1132 aa)
- Domains: TEN (N-terminal), TRBD (RNA-binding), RT (reverse transcriptase, catalytic), C-terminal extension
- Active complex: TERT + TERC (RNA template) + dyskerin/NOP10/NHP2/GAR1 (H/ACA box)
- Promoter: ETS-binding sites; the recurrent C228T and C250T promoter mutations create de novo GABP-binding sites that drive transcription
- Hypoxia regulation: HIF1A binds the TERT promoter; HIF1A induces TERT mRNA in hypoxic cells

## Key variants

- TERT promoter mutations (C228T, C250T): most frequent in melanoma, glioblastoma, hepatocellular carcinoma, urothelial cancer
- TERT structural variants: chromosomal rearrangements bringing strong enhancers near TERT (e.g., neuroblastoma)
- TERT amplification: less common, but associates with telomere lengthening
- ALT (alternative lengthening of telomeres): TERT-independent telomere maintenance via homologous recombination, common in mesenchymal tumors

## Known limitations

- TERT mRNA does not perfectly track telomerase activity; post-transcriptional regulation is significant.
- Telomere length measurements (qPCR, Southern, TelSeq) have variable resolution; bulk-tumor telomere length integrates malignant + stromal compartments.

## Open problems

- The negative correlation between PTEN mRNA and TERT mRNA in localized prostate cancer (CPC-GENE ρ=−0.36; reported in [[papers/molecular-landmarks-tumor-hypoxia-across-cancer]]) is unexplained mechanistically.
- Therapeutic targeting of telomerase (imetelstat, BIBR1532) has had modest clinical success.

## Relevance to active research

TERT is one of 51 HIF1A targets correlated with hypoxia score in localized prostate cancer in [[papers/molecular-landmarks-tumor-hypoxia-across-cancer]]. The hypoxia × PTEN × TERT three-way interaction significantly predicts telomere length (Bonferroni p=4.34×10⁻², linear model), and the lowest PTEN mRNA is observed in hypoxic + high-TERT tumors. This positions TERT at the center of a hypoxia-PTEN-telomere axis in PCa aggressiveness.
