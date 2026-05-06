---
title: "MYC (c-Myc proto-oncogene)"
slug: myc-oncogene
domain: "molecular-biology / oncology / transcription"
status: mainstream
aliases:
  - "MYC"
  - "c-Myc"
  - "c-MYC"
  - "myelocytomatosis viral oncogene homolog"
  - "MYC oncogene"
  - "8q24 amplification"
  - "MYCN (paralog, neuroblastoma)"
  - "MYCL (paralog, small-cell lung cancer)"
first_introduced: "Sheiness, Fanshier, Bishop 1978; Vennstrom et al. 1982"
date_updated: 2026-05-06
source_url: "https://www.uniprot.org/uniprot/P01106"
---

## Definition

MYC is a basic helix-loop-helix leucine-zipper (bHLH-LZ) transcription factor that, with its obligate partner MAX, binds E-box sequences (CACGTG) and acts as a master regulator of cell growth, ribosome biogenesis, metabolism, and proliferation. MYC amplification (most often via 8q24 copy-number gain in human cancers) is one of the most common oncogenic alterations across solid tumors. The MYC family also includes MYCN (chr2p24, neuroblastoma-amplified) and MYCL (chr1p34, small-cell lung cancer).

## Intuition

MYC is the master amplifier of biosynthetic capacity. Tumors that gain MYC produce more ribosomes, more nucleotides, more lipids, and more energy, allowing rapid proliferation. Hypoxia is metabolically expensive, and MYC-amplified tumors appear better equipped to survive hypoxic conditions — providing one explanation for why MYC gain co-occurs with high hypoxia in 11 tumor types pancancer.

## Formal notation

- Encoded by MYC (chr8q24.21 in human)
- 439 aa; bHLH-LZ domain at C-terminus (354–439); Myc Boxes (MB1, MB2, MB3a, MB3b, MB4) in N-terminus
- Heterodimerizes with MAX → binds E-box (5′-CACGTG-3′)
- Target classes: ribosomal proteins, RNA polymerases, glycolytic enzymes, nucleotide biosynthesis, lipogenesis
- Counter-regulators: MAX-MAX homodimers; MNT, MAD1/MXD1 family
- Stability: rapid turnover via FBW7/SCF E3 ligase (T58/S62 phosphorylation)

## Key variants

- MYCN (NMYC): chr2p24 amplification in ~25% of high-risk neuroblastoma; defines high-risk disease
- MYCL: chr1p34 amplification in small-cell lung cancer
- BIN1 (a MYC-binding protein) acts as MYC tumor suppressor and is downregulated in many cancers

## Known limitations

- MYC gain via copy-number is more common than point mutation, but transcriptomic readout (MYC mRNA / target signatures) is the more functional metric.
- "MYC pathway activation" assays vary widely; no consensus signature.
- Pharmacological MYC inhibition has been historically intractable (intrinsically disordered domains); recent BET/MYC indirect inhibitors (JQ1, OMOMYC, MYCi) are still preclinical.

## Open problems

- Whether MYC amplification is a primary driver of hypoxia tolerance, or co-selected with hypoxia-associated metabolic features, is unresolved.
- Mechanistic basis for the strong MYCN-hypoxia link in BRCA hypoxic tumors (p=2.75×10⁻³² in [[papers/molecular-landmarks-tumor-hypoxia-across-cancer]]) is not characterized.

## Relevance to active research

MYC oncogene gain associates with elevated tumor hypoxia in 11 tumor types in [[papers/molecular-landmarks-tumor-hypoxia-across-cancer]] — the most consistent oncogene-hypoxia association after PTEN loss. In KIRC specifically, MYC gain shows a strong hypoxia association (Bonferroni p=3.71×10⁻⁸). MYCN gain is enriched in hypoxic BRCA tumors.
