---
title: "PHD — prolyl hydroxylase domain enzymes (PHD1, PHD2, PHD3 / EGLN2, EGLN1, EGLN3)"
slug: phd-prolyl-hydroxylases
domain: "molecular-biology / hypoxia-signaling / enzymology"
status: mainstream
aliases:
  - "PHD"
  - "PHDs"
  - "PHD1"
  - "PHD2"
  - "PHD3"
  - "EGLN1"
  - "EGLN2"
  - "EGLN3"
  - "prolyl hydroxylase domain"
  - "HIF prolyl hydroxylase"
  - "α-ketoglutarate-dependent dioxygenase HIF"
  - "Fe(II)/2OG dioxygenase HIF"
  - "oxygen-sensor enzyme"
first_introduced: "Epstein, Gleadle, Bruick et al. 2001 Cell (HIF prolyl-4-hydroxylases as O₂ sensors); Ivan, Kondo et al. 2001 Science"
date_updated: 2026-05-08
source_url: "https://www.uniprot.org/uniprot/Q9GZT9"
---

## Definition

PHDs are α-ketoglutarate-dependent Fe(II) dioxygenases that hydroxylate specific proline residues in HIF-α subunits, generating the hydroxyproline degron recognized by pVHL for ubiquitin-mediated degradation. The three canonical isoforms — PHD1 (EGLN2), PHD2 (EGLN1), PHD3 (EGLN3) — share the dioxygenase chemistry but have distinct tissue distributions and substrate preferences. PHDs are the *upstream sensors* of cellular oxygen for the HIF axis: their catalysis requires O₂ as a co-substrate at concentrations near physiological pO₂, so they lose activity under hypoxia, allowing HIF-α to escape degradation.

## Intuition

The PHD enzymes are the actual oxygen-detecting molecules of the cell. Their catalytic cycle directly consumes O₂ to hydroxylate HIF-α, so a drop in O₂ is read as a drop in PHD activity, which is read as a stabilization of HIF-α, which is read as a transcriptional response. Three isoforms allow tissue-specific tuning. PHD2 is the dominant oxygen sensor for HIF-1α stabilization in most cells; PHD3 is itself a HIF target gene, providing a negative-feedback loop.

## Formal notation

- Co-substrates / cofactors: Fe(II), 2-oxoglutarate (2OG, α-KG), molecular oxygen (O₂).
- Catalytic cycle: PHD-Fe(II)-2OG-HIF-α → O₂ binds → ferryl Fe(IV)=O intermediate → proline hydroxylation → succinate + CO₂ + Fe(II) regenerated.
- Substrate: HIF-α at Pro402 (NODD: N-terminal oxygen-dependent degradation domain) and Pro564 (CODD: C-terminal ODD) for HIF-1α.
- Tunneled O₂ delivery: hydrophobic tunnel delivers dioxygen to the active site (Bai 2022 cites Domene 2020 *J Am Chem Soc*).

Isoforms (Bai 2022 cites Appelhoff 2004 *J Biol Chem*):
- **PHD2 (EGLN1)**: ubiquitous, dominant oxygen sensor for HIF-1α.
- **PHD1 (EGLN2)**: high in testis, also other tissues; some HIF-α preference.
- **PHD3 (EGLN3)**: induced by hypoxia (HIF target); expressed in heart, placenta, brain.

PHD inhibitors (clinical):
- **Roxadustat, Daprodustat, Vadadustat, Molidustat**: HIF-PHD inhibitors approved for renal anemia (induce EPO via HIF stabilization).
- These are *opposite* in mechanism to the HIF-2α PAS-B inhibitors used in cancer — PHD inhibitors *stabilize* HIF, while PAS-B inhibitors *block* HIF function.

Connection to TCA / oncometabolites:
- 2-OG is required substrate; succinate and fumarate are inhibitors (product inhibition; pseudohypoxia in SDH/FH-deficient tumors).
- This is the classical "oncometabolite" link: SDHx-mutant paragangliomas / FH-mutant HLRCC accumulate succinate/fumarate, inhibit PHDs, stabilize HIF-α.

## Key variants

- *PHD1 (EGLN2)*: chromosome 19q13.2; brain, testis enrichment.
- *PHD2 (EGLN1)*: chromosome 1q42.2; ubiquitous; loss-of-function is linked to high-altitude adaptation in Tibetan populations.
- *PHD3 (EGLN3)*: chromosome 14q13.1; HIF-induced; negative feedback regulator.
- *FIH (factor-inhibiting HIF, HIF1AN)*: a related JmjC-domain asparagine hydroxylase (not a proline hydroxylase) acting on HIF-α Asn803 to prevent p300/CBP recruitment — companion enzyme to PHDs in the canonical HIF axis.

## Known limitations

- Each PHD isoform's specific contribution to in vivo hypoxia sensing varies by tissue and physiological state — knockout phenotypes differ.
- PHDs may have non-HIF substrates (e.g. IKKβ, Akt) whose biological significance remains debated.
- PHD inhibitors used clinically (roxadustat etc.) are pan-PHD; isoform-selective inhibitors would be desirable but technically hard.

## Open problems

- Tissue-resolved quantitative model of PHD1/2/3 contributions to HIF-α stabilization across the physiological pO₂ range.
- Mechanistic basis for differential HIF-1α vs HIF-2α regulation by PHDs (different KM for substrates, different localization?).
- Long-term safety of pan-PHD inhibitors in chronic conditions (cardiovascular signals in some trials).

## Relevance to active research

PHDs are the upstream branch of the HIF axis covered in [[papers/hypoxia-driven-crosstalk-between-tumor-tumor]] (Bai 2022). The review notes that PHD-mediated hydroxylation can be decoupled from HIF-α stabilization in pathological cases: PIM1 phosphorylates HIF-1α to block PHD binding regardless of O₂ (Casillas 2021 *Oncogene*); iASPP binds pVHL downstream of PHD-mediated hydroxylation (Zhao 2022). For my hypoxia-NF-κB work, PHD inhibitors (DMOG, FG-4592/roxadustat) are useful tool compounds for stabilizing HIF-α independent of true hypoxia — but they do not reproduce the full hypoxic environment because they leave KDM-axis oxygen sensing and metabolic effects untouched.
