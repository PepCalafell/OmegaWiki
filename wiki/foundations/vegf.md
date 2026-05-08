---
title: "VEGF — vascular endothelial growth factor"
slug: vegf
domain: "molecular-biology / angiogenesis / oncology"
status: mainstream
aliases:
  - "VEGF"
  - "VEGFA"
  - "VEGF-A"
  - "vascular endothelial growth factor"
  - "vascular endothelial growth factor A"
  - "VPF"
  - "vascular permeability factor"
  - "angiogenic growth factor"
  - "VEGFR2 ligand"
  - "KDR ligand"
  - "Flk-1 ligand"
  - "VEGFR1 / Flt-1 ligand"
  - "anti-VEGF target"
first_introduced: "Senger et al. 1983 Science (vascular permeability factor); Ferrara & Henzel 1989 BBRC (purified VEGF); Forsythe et al. 1996 Mol Cell Biol (HIF-1α drives VEGF)"
date_updated: 2026-05-08
source_url: "https://www.uniprot.org/uniprot/P15692"
---

## Definition

VEGF (vascular endothelial growth factor; principally referring to VEGFA) is the master angiogenic growth factor that drives endothelial proliferation, vascular permeability, and new blood vessel formation. VEGFA is the prototypic HIF-1α / HIF-2α target gene under hypoxia: it carries hypoxia-response elements (HREs) and is robustly induced when HIF-α stabilizes. In the tumor microenvironment, VEGF is produced by tumor cells and by tumor-associated macrophages (TAMs), and it acts on endothelial cells via VEGFR1 (FLT1), VEGFR2 (KDR / FLK1), and VEGFR3 (FLT4) receptors to drive tumor neovascularization. Anti-VEGF therapies (bevacizumab/Avastin, anti-VEGFR2 ramucirumab, VEGF-trap aflibercept) are FDA-approved across multiple cancer types and form the cornerstone of anti-angiogenic oncology.

## Intuition

When tumors outgrow their blood supply, hypoxic regions emerge; HIF-α stabilizes; VEGF is transcribed; new blood vessels grow toward the hypoxic tumor; the tumor expands further. This positive-feedback loop is the heart of cancer angiogenesis. VEGF is also produced by hypoxic TAMs as a paracrine mediator that drives both vascular and tumor-cell effects (the latter via VEGFR2 expression on tumor cells). Anti-VEGF therapy interrupts this loop and is a foundational anti-angiogenic strategy across oncology.

## Formal notation

VEGF family:
- **VEGFA** (most-studied, dominant tumor angiogenic factor)
- **VEGFB** (cardiac homeostasis emphasis)
- **VEGFC** / **VEGFD** (lymphangiogenesis)
- **PIGF** (placenta growth factor)

VEGFA isoforms (alternative splicing):
- VEGF121, VEGF165 (canonical), VEGF189, VEGF206
- Also anti-angiogenic VEGFxxxb isoforms

Receptors:
- **VEGFR1 (FLT1)** — high-affinity binder, mostly negative regulator of VEGFR2 signaling (decoy).
- **VEGFR2 (KDR / FLK1)** — main pro-angiogenic signaling receptor on endothelium.
- **VEGFR3 (FLT4)** — lymphangiogenesis (binds VEGFC/D).
- **NRP1** — co-receptor for VEGFR2 (also binds Sema3A — see Bai 2022 cervical / Lewis lung carcinoma TAM mechanism).

Hypoxia-responsive transcription:
- HIF-1α / HIF-2α bind HREs in VEGFA promoter.
- VEGFA is the canonical "hypoxia + angiogenesis" target gene.

VEGF in TAM context (Bai 2022):
- TAM-derived VEGF: hypoxic TAMs produce VEGF (mRNA and protein) time-dependently.
- TAM VEGF binds tumor-cell VEGFR → PI3K-Akt and p38 MAP kinase activation → tumor proliferation and invasion.
- Tumor-derived VEGF + IL-6 (HNSCC) → TAM M2 polarization → CCL15 release → CCR1-NF-κB on tumor → gefitinib resistance.
- VEGF is the canonical readout of HIF-1α activity in PX-478 mechanistic experiments.

Anti-VEGF therapeutics:
- **Bevacizumab (Avastin)**: anti-VEGFA mAb; FDA-approved across multiple cancers.
- **Ramucirumab**: anti-VEGFR2 mAb.
- **Aflibercept (Zaltrap)**: VEGF-trap fusion.
- **Sunitinib, Sorafenib, Lenvatinib, Cabozantinib, Pazopanib, Axitinib**: multi-targeted TKIs hitting VEGFRs.

## Key variants

- *VEGFA splice isoforms*: pro-angiogenic vs anti-angiogenic VEGFxxxb.
- *Tumor-cell VEGF vs TAM-derived VEGF*: same molecule, different cellular sources, different therapeutic implications.
- *NRP1 co-receptor*: enables VEGFR2 signaling and is also Sema3A receptor — the same NRP1 link explains why hypoxic-niche TAM capture (Sema3A-NRP1) and angiogenic stimulation (VEGF-VEGFR2-NRP1) co-localize biochemically.

## Known limitations

- Anti-VEGF therapy resistance is common (vessel co-option, alternative angiogenic pathways: FGF, PDGF, ANGPT2).
- Hypertension, proteinuria, GI perforation are class adverse events.
- Bevacizumab failed in some indications (early breast cancer adjuvant).
- TAM-derived VEGF can compensate when tumor-cell VEGF is depleted, complicating bevacizumab response prediction.

## Open problems

- Predictive biomarker for anti-VEGF benefit (no robust one despite multiple trials).
- Optimal combination with checkpoint blockade in TAM-rich tumors (e.g. atezolizumab + bevacizumab in HCC and ccRCC is the contemporary front line).
- TAM-specific VEGF blockade vs pan-VEGF blockade — therapeutic differentiation.

## Relevance to active research

VEGF is foundational for any cancer-hypoxia work because it is the canonical HIF target and the principal anti-angiogenic-therapy target. In [[papers/hypoxia-driven-crosstalk-between-tumor-tumor]] (Bai 2022), VEGF appears in multiple sections: HNSCC tumor → M2 TAM polarization, TAM-derived VEGF → tumor cell PI3K/Akt/p38, lactate-driven TAM VEGFA secretion (Galectin-3 axis), and VEGF as the canonical readout for PX-478 HIF-1α inhibitor activity. In [[papers/molecular-landmarks-tumor-hypoxia-across-cancer]] (Bhandari 2019), VEGFA is one of the 51 HIF1A target genes correlating with hypoxia score in localized prostate cancer.
