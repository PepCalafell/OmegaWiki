---
title: "SUCNR1 / GPR91 — succinate receptor"
slug: sucnr1-succinate-receptor
domain: "molecular-biology / metabolism / cell-signaling"
status: mainstream
aliases:
  - "SUCNR1"
  - "GPR91"
  - "succinate receptor"
  - "succinate receptor 1"
  - "G-protein-coupled receptor 91"
  - "Gαi-coupled succinate sensor"
  - "Gαq-coupled succinate sensor"
  - "extracellular succinate sensor"
  - "oncometabolite GPCR"
  - "TAM SUCNR1"
first_introduced: "He, Dunne et al. 2004 Nature (deorphanized GPR91 as succinate receptor); Wu et al. 2020 Cell Metab (SUCNR1 in lung cancer macrophage axis)"
date_updated: 2026-05-08
source_url: "https://www.uniprot.org/uniprot/Q9BXA5"
---

## Definition

SUCNR1 (also known as GPR91) is a G-protein-coupled receptor expressed on the surface of macrophages, dendritic cells, kidney epithelial cells, retinal cells, platelets, and many cancer cells, with succinate (a TCA-cycle intermediate) as its high-affinity endogenous ligand. SUCNR1 was deorphanized in 2004 and is now recognized as a principal extracellular succinate sensor. Coupling to Gαi and Gαq signaling, SUCNR1 activates PI3K, MAPK, and HIF-1α axes downstream. In the tumor microenvironment, tumor-derived extracellular succinate engages SUCNR1 on TAMs to drive their recruitment, M2-skewed polarization, and IL-6 secretion that promotes cancer cell migration; the same axis on tumor cells drives cancer cell migration and EMT through PI3K/HIF-1α.

## Intuition

For decades, succinate was known only as a TCA-cycle intermediate. The 2004 deorphanization of GPR91 as a succinate receptor — and the 2020 Wu et al. demonstration of its role in lung cancer macrophage recruitment — repositioned succinate as a *signaling* molecule. SUCNR1 lets cells sense extracellular succinate concentration changes (which rise dramatically in inflammation, hypoxia, and SDH-deficient tumors). The TAM-side activation by SUCNR1 yields the same M2 polarization output as lactate but via PI3K-HIF-1α, providing a parallel oncometabolite-receptor signaling channel.

## Formal notation

Receptor properties:
- 7TM GPCR; ~330 aa.
- Coupled to Gαi (cAMP↓) and Gαq (Ca²⁺↑, PKC) depending on cell type.
- Endogenous ligand: succinate (~50-300 µM extracellular under inflammation/hypoxia; reaches mM levels in some pathologies).

Signaling outputs (Bai 2022 cites):
- TAM SUCNR1 → PI3K → HIF-1α stabilization.
- TAM outputs: recruitment, migration, M2-skewed polarization, IL-6 secretion.
- Tumor cell SUCNR1 → PI3K/HIF-1α → cancer cell migration and EMT.
- IL-6 from M2 TAMs → enhances cancer cell migration (paracrine reinforcement).

Disease links:
- Diabetes / hyperglycemia: kidney SUCNR1 signaling.
- Inflammation: macrophage SUCNR1 in LPS-driven IL-1β secretion (Tannahill 2013).
- Cancer: lung cancer (Wu 2020), SDH-deficient paragangliomas (chronic SUCNR1 stimulation).
- Retinopathy: SUCNR1 on retinal cells in diabetic retinopathy.

Therapeutics:
- SUCNR1 antagonists are in early preclinical development.
- No FDA-approved selective SUCNR1 modulators yet.

## Key variants

- *SUCNR1 / GPR91* — only known succinate-specific GPCR.
- Other oncometabolite receptors: GPR81 (lactate), HCA2 (β-hydroxybutyrate).
- Distinct from intracellular succinate sensing (PHD inhibition by accumulated succinate in SDH-deficient cells).

## Known limitations

- Most SUCNR1 functional data come from rodent / cell-culture models; translation to human cancer is incomplete.
- SUCNR1 antagonists are not yet clinically validated.
- SUCNR1 expression at single-cell resolution across TAM clusters is poorly mapped.
- Cross-talk with other oncometabolite GPCRs (e.g. lactate-GPR81) at common downstream nodes is not fully characterized.

## Open problems

- Identification of selective, clinically tractable SUCNR1 antagonists.
- TAM cluster-level mapping of SUCNR1 expression (which MoMac-VERSE / Casanova-Acebes cluster is the SUCNR1+ subset?).
- Synergy with HIF-axis inhibitors and immune checkpoint blockade.
- Role in SDH-deficient paragangliomas and IDH-mutant gliomas where oncometabolite chemistry is constitutive.

## Relevance to active research

SUCNR1 is foundational for the succinate-driven branch of hypoxic tumor-TAM crosstalk. In [[papers/hypoxia-driven-crosstalk-between-tumor-tumor]] (Bai 2022), SUCNR1 is the central GPCR in the "Oncometabolites" section, mediating tumor-derived succinate's effect on TAM recruitment, M2 polarization, and on tumor-cell EMT. For my hypoxia-NF-κB-macrophage thesis, SUCNR1 is a candidate macrophage-side oncometabolite sensor to consider in datasets where TAM phenotypes correlate with tumor metabolic activity.
