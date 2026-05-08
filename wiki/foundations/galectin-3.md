---
title: "Galectin-3 (Gal-3, LGALS3, Mac-2) — β-galactoside-binding lectin"
slug: galectin-3
domain: "molecular-biology / immunology / oncology"
status: mainstream
aliases:
  - "Galectin-3"
  - "Gal-3"
  - "LGALS3"
  - "Mac-2"
  - "Mac-2 antigen"
  - "epsilon BP"
  - "EBP"
  - "L-29"
  - "CBP-35"
  - "carbohydrate-binding protein 35"
  - "β-galactoside binding lectin"
  - "galectin-3 PD-L1 STAT3"
first_introduced: "Cherayil, Weiner, Pillai 1989 J Exp Med (Mac-2 cloning); Liu et al. 1995 Biochim Biophys Acta (galectin family unification)"
date_updated: 2026-05-08
source_url: "https://www.uniprot.org/uniprot/P17931"
---

## Definition

Galectin-3 (LGALS3, Mac-2) is a member of the β-galactoside-binding lectin (galectin) family — proteins with conserved carbohydrate-recognition domains (CRDs) that recognize β-galactoside (Gal-β-1,3-GlcNAc and Gal-β-1,4-GlcNAc) sugar moieties on glycoproteins. Galectin-3 is uniquely "chimeric": a single C-terminal CRD attached to a long N-terminal collagen-like domain that enables homo-oligomerization and pentamer formation upon ligand binding. It is expressed by macrophages (where it was originally identified as the Mac-2 antigen), epithelial cells, fibroblasts, and many tumor cells. In the hypoxic tumor microenvironment, Galectin-3 is secreted by TAMs (regulated by ROS-NF-κB rather than HIF-1α; Bai 2022) and acts on tumor cells to promote metastasis and angiogenesis. It also drives PD-L1 upregulation via STAT3 phosphorylation, contributing to immune evasion.

## Intuition

Galectin-3 is the most multifunctional galectin: it acts intracellularly (anti-apoptotic, pro-survival), at the cell surface (lattice formation, glycoprotein clustering), and extracellularly (paracrine/endocrine effects). In cancer, its dominant role is via the extracellular pool: TAM-secreted Galectin-3 promotes tumor metastasis, angiogenesis (via VEGFA), and PD-L1 expression. The hypoxic-niche regulation is via ROS-NF-κB, NOT HIF-1α — a surprising finding because most hypoxic-tumor proteins are HIF-driven. This makes Galectin-3 inhibitors potentially complementary (not redundant) to HIF-axis inhibitors.

## Formal notation

Domain structure:
- N-terminal collagen-like domain (proline-rich, glycine-rich, ~110 aa).
- C-terminal CRD (~130 aa).
- Single 26 kDa monomer; pentamerizes upon glycan binding via N-terminal interactions.

Hypoxic regulation in TAMs (Bai 2022):
- "The expression level of HIF-1α is elevated in hypoxic TAMs, [but] HIF-1α inhibitors have no effect on the expression of Gal-3 there, suggesting that HIF-1α may not be involved in Gal-3 expression in hypoxic TAMs."
- HIF-1α inhibitor 2ME2 *upregulates* Gal-3 in normoxia but not hypoxia — counter-intuitive.
- Mechanism: ROS → NF-κB nucleation → Gal-3 transcription.

Outputs:
- TAM-derived Gal-3 → tumor metastasis, angiogenesis (depends on hypoxia degree and duration).
- Gal-3 → PD-L1 upregulation via STAT3 phosphorylation in carcinomas.
- Gal-3 over-expression in TAMs → enhanced VEGFA secretion and glucose consumption.

Therapeutics:
- **GR-MD-02 (Belapectin)**: Galectin-3 inhibitor in NASH and oncology trials.
- **TD139 (PXS-5505)**: inhaled Gal-3 inhibitor for IPF.
- **Anti-Gal-3 antibodies**: in development.

## Key variants

- *Other galectins*: Gal-1 (mononomeric, similar pro-tumor), Gal-7 (skin), Gal-9 (TIM-3 ligand, T-cell exhaustion).
- *Intracellular vs secreted Gal-3*: same protein, different functional pools.
- *Cleaved Gal-3*: matrix metalloproteinases cleave the N-terminal domain, releasing the monomeric CRD with distinct biological properties.

## Known limitations

- Galectin-3 inhibitor clinical trials have been mixed; oncology efficacy uncertain.
- Many Galectin-3 effects are context-dependent (cancer-type, glycosylation profile of target cells).
- Inhibition specificity vs other galectins is challenging.
- Mouse-human translation: shared but with some species-specific glycan-binding preferences.

## Open problems

- Optimal cancer indication for Galectin-3 inhibition.
- Whether Galectin-3 inhibition unmasks anti-PD-L1 response (synergy with immune checkpoint blockade).
- Mechanism of ROS-NF-κB-driven Gal-3 expression in hypoxic TAMs — what is the immediate ROS sensor?
- Why HIF-1α inhibitor 2ME2 upregulates Gal-3 in normoxia but not hypoxia — the molecular logic remains unresolved.

## Relevance to active research

Galectin-3 is foundational for tumor-TAM crosstalk in hypoxic settings. In [[papers/hypoxia-driven-crosstalk-between-tumor-tumor]] (Bai 2022), Galectin-3 is highlighted as a TAM-secreted protein with ROS-NF-κB regulation that paradoxically does NOT depend on HIF-1α despite being upregulated in HIF-1α-high hypoxic TAMs. This makes it a non-canonical hypoxic-TME protein with distinct therapeutic targeting logic. For my hypoxia-NF-κB-macrophage work, Galectin-3 is an interesting marker of NF-κB-driven (but HIF-independent) hypoxic TAM activation.
