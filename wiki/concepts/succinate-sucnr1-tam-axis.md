---
title: "Tumor-derived succinate engages SUCNR1 on TAMs to drive M2 polarization, recruitment, and EMT"
aliases:
  - "succinate macrophage axis"
  - "SUCNR1 macrophage signaling"
  - "GPR91 oncometabolite"
  - "succinate TAM EMT"
  - "succinate IL-1β macrophage"
  - "succinate PI3K HIF-1α macrophage"
  - "succinate IL-6 cancer migration"
  - "tumor-derived oncometabolite SUCNR1"
  - "succinate dehydrogenase deficiency tumor"
  - "TCA intermediate macrophage signaling"
tags:
  - succinate
  - SUCNR1
  - GPR91
  - oncometabolite
  - macrophage-polarization
  - hypoxia
  - TAM
  - EMT
  - cancer-cell-migration
  - HIF-1α
maturity: emerging
key_papers:
  - hypoxia-driven-crosstalk-between-tumor-tumor
first_introduced: "Tannahill 2013 Nature (succinate-IL-1β-HIF-1α in inflammatory macrophages); Wu 2020 Cell Metab (succinate-SUCNR1-tumor migration); reviewed Bai 2022"
date_updated: 2026-05-08
related_concepts:
  - tumor-associated-macrophage-immunosuppression
  - lactate-driven-tam-m2-polarization
  - macrophage-induced-emt-tumor-invasiveness
---

## Definition

A metabolic-paracrine axis in which the TCA-cycle intermediate succinate, secreted by hypoxic / metabolically reprogrammed tumor cells (lung cancer in the canonical study), engages the GPCR succinate receptor SUCNR1 (also known as GPR91) on tumor-associated macrophages and on tumor cells, activating a PI3K → HIF-1α signaling axis. The macrophage-side output is recruitment, migration, and M2-skewed phenotype with IL-6 secretion that promotes cancer cell migration. The tumor-side output is direct tumor-cell migration and EMT through tumor-cell-autonomous SUCNR1 → PI3K/HIF-1α. Succinate accumulation also boosts HIF-1α protein levels and IL-1β secretion in macrophages — a parallel inflammatory output. The axis is one of the cleanest cases of an oncometabolite acting as a direct receptor-ligand signal between tumor and immune compartment.

## Intuition

Hypoxic and Warburg-shifted tumors leak metabolic intermediates beyond just lactate; succinate is one of the most signaling-active TCA intermediates because it has a dedicated receptor (SUCNR1/GPR91) on multiple cell types. Tumor cells releasing succinate set up a local field that simultaneously (a) recruits and polarizes macrophages and (b) acts on the tumor cells themselves to drive EMT — a *cell-non-autonomous and cell-autonomous combined* effect from the same molecule. The downstream is anchored on PI3K → HIF-1α, which means that the succinate signal *amplifies* HIF-1α already stabilized by hypoxia, just like lactate does.

## Formal notation

Succinate signaling ligand and receptor:
- Source: hypoxic / SDH-deficient / Warburg-shifted tumor cells release succinate into TME.
- Receptor: SUCNR1 (GPR91) — Gαi/Gαq-coupled GPCR.
- SUCNR1 is expressed on macrophages, tumor cells, dendritic cells, platelets, retina, kidney.

Macrophage-side cascade:
- Tumor succinate → SUCNR1 on TAM → PI3K activation → HIF-1α stabilization.
- Outputs: TAM recruitment, TAM migration, M2-skewed polarization.
- M2 TAMs secrete IL-6 → enhances cancer cell migration.

Tumor-side cascade:
- Tumor succinate → SUCNR1 on tumor cell → PI3K → HIF-1α → cancer cell migration and EMT.

Inflammatory route (parallel, in macrophages):
- Succinate accumulation in macrophages (LPS-stimulated; intracellular) → robust HIF-1α boost → IL-1β secretion (Tannahill 2013).
- Succinate produced by tumors and acting extracellularly (Wu 2020) is distinct from intracellular succinate accumulation in macrophages, but they converge on HIF-1α.

## Variants

- *Tumor-extrinsic succinate* (Wu 2020 lung cancer): tumor releases succinate; SUCNR1 on TAM and on tumor cell both engaged.
- *Macrophage-intrinsic succinate accumulation* (Tannahill 2013): TCA cycle break under LPS leads to internal succinate buildup → HIF-1α → IL-1β.
- *SDH-deficient tumors* (paragangliomas, GIST): genetic succinate accumulation is constitutive and could drive a chronic SUCNR1 signal.

## Comparison

vs lactate-driven TAM M2 polarization: both oncometabolites act via GPCRs and converge on HIF-1α; lactate uses PKA-CREB downstream, succinate uses PI3K. They likely cooperate rather than compete.
vs intracellular vs extracellular succinate routing: intracellular succinate (Tannahill 2013) drives IL-1β in inflammatory macrophages; extracellular tumor-derived succinate (Wu 2020) drives M2-like polarization in TAMs — opposite outputs from the same molecule depending on routing.
vs HIF-1α-driven hypoxia program directly: succinate amplifies hypoxia's HIF-1α signal in TAMs; the two are reinforcing.
vs the canonical SDH-deficient paraganglioma phenotype: pheochromocytomas / paragangliomas with SDHx mutation have constitutive intracellular succinate elevation and a "pseudohypoxia" phenotype; the Bai review notes that Belzutifan is being tested in this setting.

## When to use

- When extending a hypoxic tumor-TAM model beyond lactate: succinate is the next-most-active oncometabolite signal.
- For SDH-deficient tumors and paragangliomas: SUCNR1 antagonists may have therapeutic value beyond HIF-2α inhibitors.
- When designing TAM-targeted therapy: SUCNR1 blockade cuts the macrophage recruitment and M2 conversion in a HIF-1α-dependent manner.
- For interpreting TAM-tumor co-culture data: succinate concentration in conditioned media is an underappreciated variable.

## Known limitations

- The Wu 2020 lung-cancer mechanism is the dominant cited evidence; cross-cancer-type validation is limited.
- SUCNR1 has multiple ligands and modulators; succinate is dominant at micromolar-to-millimolar concentrations but other compounds may co-engage.
- Distinguishing intracellular vs extracellular succinate effects in vivo is technically hard.
- SUCNR1 antagonists are in early development; therapeutic translation is preclinical.

## Open problems

- A unified pharmacological model of SUCNR1 antagonism in TAM and tumor cell — does the same antagonist hit both?
- Whether SUCNR1 signaling in TAM converges with the lactate-GPCR axis at common downstream nodes (HIF-1α, mTOR).
- The role of cyclic / intermittent hypoxia in modulating tumor-cell succinate release: H-R cycles induce ROS bursts that may release succinate transiently.
- Tissue-resident macrophage vs monocyte-derived macrophage SUCNR1 expression — likely heterogeneous and ontogeny-linked.

## Key papers

- [[papers/hypoxia-driven-crosstalk-between-tumor-tumor]] — Bai et al. 2022 *Molecular Cancer*. The "Oncometabolites" section synthesizes the succinate-SUCNR1 mechanism in the context of the broader hypoxia-driven crosstalk.

## My understanding

For my thesis, this is a complementary oncometabolite axis to lactate that I had not foregrounded. Future single-cell metabolic / IL-1β-related analyses of mMAC1 should include SUCNR1 as a candidate marker. Therapeutically, succinate-receptor antagonism could be a partner to HIF inhibitor strategies.
