---
# === Identification ===
title: "Systemic hypoxia suppresses solid tumor growth"
slug: systemic-hypoxia-suppresses-solid-tumor-growth
arxiv: ""
doi: "10.64898/2026.02.09.704975"
pmid: "41726896"
venue: "bioRxiv"
year: 2026
authors: [Ayush D. Midha, Brandon T. L. Chew, Benedict M. H. Choi, Jung Min Suh, Chris Carpenter, Alan H. Baik, Tej A. Joshi, Skyler Y. Blume, Augustinus G. Haribowo, Pedro Ruivo, Will R. Flanigan, Ankur Garg, Daniel D. Zhang, Vishvak Subramanyam, Rebecca Shuere, Youngho Seo, Henry VanBrocklin, Hani Goodarzi, Isha H. Jain]
first_author: "Ayush D. Midha"
corresponding_author: "Isha H. Jain; Hani Goodarzi"

# === Source & metadata ===
source_type: pdf
s2_id: "78f0d1cc17ec20d100eb8f46408776a956414a00"
date_added: 2026-06-02
ingested_date: 2026-06-02
ingest_version: 1
last_reviewed:

# === Classification ===
importance: 4
tier: TIER_1
tags: [hypoxia, cancer-metabolism, purine-metabolism, tumor-suppression, oncology, immunotherapy]
keywords: [systemic hypoxia, de novo purine synthesis, tumor metabolism, HypoxyStat, GENEVA, gemcitabine, anti-CTLA4]
domain: oncology

# === Biomedical domain ===
tissue: [pancreas, breast, multi]
condition: [cancer]
disease_specific: [pdac, breast_cancer, ccRCC]
species: [mouse, human]
hypoxia_relevant: true
contains_immune_cells: true
contains_myeloid: false

# === Technique ===
techniques: [scRNA-seq_10x, metabolomics, stable_isotope_tracing, 18F-FDG_PET, CRISPR_KO, flow_cytometry, histopathology]
n_samples:
n_cells_total:
integration_method: ""

# === Biology captured ===
key_cell_types: [PDAC cells, breast cancer cells, clear cell renal cell carcinoma cells]
key_markers: [SLC2A1, GLUT1, PPAT, MTHFD1, MTHFD2, PAICS, ATIC, IMP, AMP, HIF-1a, ARNT, PTEN, MYC, CTLA4]
key_pathways: [de novo purine synthesis, purine salvage, HIF signaling, insulin/PI3K signaling, glycolysis]

# === User project membership ===
projects: [thesis, hypoxia]
priority: core
read_status: read

# === HypoxiaVERSE-specific ===
hypoxiaverse_status: candidate
exclusion_reason:
data_availability: ""

# === Cross-references ===
code_url: ""
cited_by: []
---

## Problem

Local intratumoral hypoxia is a hallmark of solid tumors and a classical *negative* prognostic factor: hypoxic niches activate HIFs, promote angiogenesis and glucose uptake, and confer resistance to radio- and chemotherapy. But the effect of **systemic (whole-body) hypoxia** — the kind induced by altitude — on tumor growth and metabolism had not been explored. The authors ask whether global, host-level oxygen deprivation acts like local hypoxia (pro-tumor) or differently.

## Key idea

Systemic hypoxia **paradoxically suppresses** solid tumor growth across diverse preclinical models, and does so by suppressing **de novo purine synthesis** in tumors — independent of hypoglycemia, hypoinsulinemia, or tumor-intrinsic HIF activation. The effect is non-resistant, synergizes with chemotherapy and immunotherapy, and can be achieved pharmacologically with the hemoglobin-O2-affinity modulator **HypoxyStat**. This challenges the paradigm of hypoxia as uniformly pro-tumor.

## Method

- **In vivo tumor models**: subcutaneous Panc02 PDAC and orthotopic E0771 breast cancer in C57BL/6J mice; tamoxifen-inducible KPC (KrasG12D;p53fl/fl;Pdx1-CreER) genetic PDAC model. Mice housed at 21% (normoxia), 11% (moderate hypoxia), or 8% (hypoxia) O2.
- **Tumor oxygenation**: direct intratumoral pO2 via Clark-type electrode.
- **[[concepts/geneva-multiplexed-mosaic-xenograft]]**: 20-line human mosaic xenografts in NSG mice + 10x scRNA-seq; SNP-deconvolution for lineage-specific fitness and cell-cycle scoring.
- **Mechanism exclusion**: 30% glucose supplementation; Pten-KO (constitutive insulin signaling); Arnt/HIF-1β-KO (HIF-null) Panc02 clones; 18F-FDG uptake.
- **Metabolomics** of tumor homogenates and tumor interstitial fluid; **dual stable-isotope tracing** (γ-15N-glutamine for de novo synthesis, 8-13C-adenine for salvage) in vitro and via in vivo infusion.
- **Therapy**: serial re-implantation (resistance test); hypoxia + gemcitabine; hypoxia + anti-CTLA4; HypoxyStat dosing; county-level elevation vs cancer-mortality epidemiology.

## Results

Systemic hypoxia reduced tumor growth in every model and lowered intratumoral pO2. In GENEVA, pooled growth fell but lineage responses were heterogeneous (most lines lost fitness; SH4, 786O and Caki1 gained). Tumor suppression survived glucose supplementation, constitutive insulin signaling (Pten-KO), and HIF ablation (Arnt-KO). Metabolomics showed depletion of purine nucleotides; tracing showed suppressed de novo purine synthesis with compensatory salvage. De novo purine gene expression correlated with hypoxia fitness and tracked Myc-target downregulation. No resistance emerged over four passages; hypoxia synergized with gemcitabine and anti-CTLA4; HypoxyStat recapitulated the effect; higher-elevation US counties had lower cancer mortality.

## All claims (exhaustive)

- `[c01]` Systemic hypoxia (8% O2) reduces tumor growth across Panc02, E0771 and KPC models (p.1) "systemic hypoxia ... decreases tumor growth in vivo across multiple cancer types and preclinical models" — confidence: high — type: methodological — links: [[concepts/systemic-hypoxia-anti-tumor-therapy]] [[claims/systemic-hypoxia-reduces-solid-tumor-growth-multimodel]]
- `[c02]` Systemic hypoxia lowers intratumoral pO2 (p.3) "tumors from mice housed in hypoxic conditions exhibited lower pO2 than those from normoxic counterparts" — confidence: high — type: quantitative — links: [[concepts/systemic-hypoxia-anti-tumor-therapy]] [[claims/systemic-hypoxia-lowers-intratumoral-po2]]
- `[c03]` GENEVA: hypoxia suppresses pooled growth with heterogeneous lineage responses (p.5) "systemic hypoxia led to a marked and significant decrease in mosaic tumor growth in the multiplexed xenograft setting" — confidence: high — type: methodological — links: [[concepts/geneva-multiplexed-mosaic-xenograft]] [[concepts/systemic-hypoxia-anti-tumor-therapy]] [[claims/hypoxia-tumor-suppression-heterogeneous-across-lineages-geneva]]
- `[c04]` SH4, 786O, Caki1 (incl. ccRCC) gain fitness under hypoxia (p.5) "a subset, including SH4 (melanoma), 786O, and Caki1 (renal cell carcinomas), showed increased relative growth" — confidence: medium — type: correlational — links: [[concepts/geneva-multiplexed-mosaic-xenograft]] [[claims/ccrcc-and-select-lines-resist-hypoxia-tumor-suppression]]
- `[c05]` Hypoxia shifts cells toward G1 arrest / reduced S-phase (p.5) "hypoxia induced a shift toward G1 arrest and reduced S-phase occupancy" — confidence: medium — type: correlational — links: [[concepts/systemic-hypoxia-anti-tumor-therapy]] [[claims/hypoxia-shifts-cancer-cells-toward-g1-arrest]]
- `[c06]` Suppression independent of hypoglycemia (glucose supplementation no rescue) (p.5) "Glucose supplementation ... had no discernible effect in hypoxic mice" — confidence: high — type: mechanistic — links: [[concepts/systemic-hypoxia-anti-tumor-therapy]] [[claims/hypoxia-tumor-suppression-independent-of-hypoglycemia]]
- `[c07]` Hypoxic tumors take up ~2x more 18F-FDG via GLUT1/SLC2A1 (p.5) "tumors in hypoxic mice took up twice as much 18F-FDG as those in normoxic mice" — confidence: medium — type: quantitative — links: [[concepts/systemic-hypoxia-anti-tumor-therapy]] [[claims/hypoxic-tumors-increase-glucose-uptake-glut1]]
- `[c08]` Suppression independent of insulin signaling (Pten-KO still suppressed) (p.6) "hypoxia treatment still significantly decreased the growth of Pten-deficient tumors" — confidence: high — type: mechanistic — links: [[concepts/systemic-hypoxia-anti-tumor-therapy]] [[foundations/pten-tumor-suppressor]] [[claims/hypoxia-tumor-suppression-independent-of-insulin-signaling]]
- `[c09]` Suppression independent of tumor-intrinsic HIF (Arnt-KO still suppressed) (p.7) "HIF-dependent transcription in cancer cells is not necessary for tumor suppression in hypoxia" — confidence: high — type: mechanistic — links: [[concepts/systemic-hypoxia-anti-tumor-therapy]] [[foundations/arnt-hif1b]] [[foundations/hif1a]] [[claims/hypoxia-tumor-suppression-independent-of-tumor-hif]]
- `[c10]` Hypoxia depletes tumor purine nucleotides (adenine, adenosine, AMP) (p.7) "Nucleotide intermediates and nucleotide derivatives were among the most significantly depleted metabolites" — confidence: high — type: quantitative — links: [[concepts/de-novo-purine-synthesis-suppression-hypoxic-tumor]] [[claims/systemic-hypoxia-depletes-tumor-purine-nucleotides]]
- `[c11]` Hypoxia suppresses de novo purine synthesis (15N tracing) in vitro and in vivo (p.9) "both the in vitro and in vivo labeling experiments indicate that hypoxia suppressed de novo purine synthesis" — confidence: medium — type: mechanistic — links: [[concepts/de-novo-purine-synthesis-suppression-hypoxic-tumor]] [[claims/systemic-hypoxia-suppresses-de-novo-purine-synthesis]]
- `[c12]` Hypoxia increases reliance on purine salvage (13C-AMP up) (p.9) "increased the fraction of AMP carrying a 13C label, indicating ... an increased reliance on salvage" — confidence: medium — type: mechanistic — links: [[concepts/de-novo-purine-synthesis-suppression-hypoxic-tumor]] [[claims/systemic-hypoxia-increases-purine-salvage-reliance]]
- `[c13]` Aspartate depletion does NOT explain in vivo purine suppression (p.9) "aspartate levels were not depleted, suggesting that aspartate deprivation does not explain the depletion of purine nucleotides" — confidence: medium — type: mechanistic — links: [[concepts/de-novo-purine-synthesis-suppression-hypoxic-tumor]] [[claims/aspartate-depletion-does-not-explain-hypoxia-purine-suppression]]
- `[c14]` De novo purine gene expression correlates with fitness in hypoxia (p.9) "key de novo purine synthesis genes ... were significantly and positively associated with relative fitness in hypoxia" — confidence: medium — type: correlational — links: [[concepts/de-novo-purine-synthesis-suppression-hypoxic-tumor]] [[concepts/geneva-multiplexed-mosaic-xenograft]] [[claims/de-novo-purine-gene-expression-correlates-fitness-hypoxia]]
- `[c15]` Purine suppression tracks Myc-target downregulation (p.11) "changes in the expression of the de novo purine synthesis genes ... were correlated with changes in the expression of most Myc targets" — confidence: low — type: correlational — links: [[concepts/de-novo-purine-synthesis-suppression-hypoxic-tumor]] [[foundations/myc-oncogene]] [[claims/hypoxia-purine-suppression-tracks-myc-target-downregulation]]
- `[c16]` De novo purine synthesis more essential in vivo than in vitro (Zhu 2021 screen) (p.9) "genes involved in de novo purine synthesis were some of the most essential genes for tumor growth in vivo" — confidence: medium — type: correlational — links: [[concepts/de-novo-purine-synthesis-suppression-hypoxic-tumor]] [[claims/de-novo-purine-synthesis-more-essential-in-vivo-than-in-vitro]]
- `[c17]` No resistance over 4 serial passages (p.11) "tumors in hypoxic mice consistently grew slower ... no overt resistance phenotype emerged" — confidence: high — type: methodological — links: [[concepts/systemic-hypoxia-anti-tumor-therapy]] [[claims/tumors-do-not-acquire-resistance-to-systemic-hypoxia]]
- `[c18]` Synergy with gemcitabine chemotherapy (p.11) "the combination of the two treatments further slowed tumor growth" — confidence: high — type: pharmacological — links: [[concepts/systemic-hypoxia-anti-tumor-therapy]] [[claims/systemic-hypoxia-synergizes-with-gemcitabine]]
- `[c19]` Synergy with anti-CTLA4 ICI (near-complete suppression) (p.11) "systemic hypoxia plus ICI further decreased tumor growth, nearly completely abolishing cancer progression" — confidence: medium — type: pharmacological — links: [[concepts/systemic-hypoxia-anti-tumor-therapy]] [[foundations/ctla-4-checkpoint]] [[claims/systemic-hypoxia-synergizes-with-anti-ctla4-ici]]
- `[c20]` HypoxyStat recapitulates inhaled hypoxia's tumor suppression (p.13) "HypoxyStat dosing was sufficient to decrease tumor growth ... to a comparable degree as inhaled hypoxia" — confidence: low — type: pharmacological — links: [[concepts/hypoxystat-hemoglobin-oxygen-affinity-modulator]] [[concepts/systemic-hypoxia-anti-tumor-therapy]] [[claims/hypoxystat-recapitulates-inhaled-hypoxia-tumor-suppression]]
- `[c21]` Higher US-county elevation correlates with lower cancer mortality (p.13) "Higher altitude was significantly negatively correlated with AAMR" — confidence: low — type: correlational — links: [[concepts/systemic-hypoxia-anti-tumor-therapy]] [[claims/higher-altitude-correlates-lower-cancer-mortality]]
- `[c22]` Systemic vs local hypoxia have opposite effects on tumors (p.1) "These findings challenge the long-held paradigm of hypoxia as a negative prognostic factor" — confidence: medium — type: mechanistic — links: [[concepts/systemic-hypoxia-anti-tumor-therapy]] [[claims/systemic-vs-local-tumor-hypoxia-opposite-effects]]

## Discussion captured

### Authors' interpretation

The authors interpret systemic-hypoxia tumor suppression as a disruption of the intratumoral "division of labor": under local hypoxia, well-oxygenated pockets perform energetically costly biosynthesis (nucleotides) and feed salvageable substrates to hypoxic regions, supporting aggression; under *systemic* hypoxia the whole tumor is deprived, causing tumor-wide nucleotide depletion. They propose suppressed de novo purine synthesis as a central mechanism, possibly downstream of reduced Myc activity, and frame it as a protective metabolic adaptation that nonetheless slows growth.

### Comparisons with prior literature (made by authors)

- Warburg's glucose-consumption observation and nutrient-deprivation anti-tumor strategies (glucose, arginine, methionine) — framing host-nutrient manipulation.
- Local tumor hypoxia promoting angiogenesis/nutrient uptake/therapy resistance (HIF biology).
- In vitro hypoxia making aspartate limiting for purine synthesis (contrasted: aspartate not depleted in vivo here).
- Zhu et al. 2021 (ref 48) CRISPR metabolic screen — de novo purine genes essential in vivo > in vitro.
- ccRCC VHL-loss/HIF biology; Caki1 is VHL-WT yet hypoxia-resistant.

### Mechanistic hypotheses proposed

- "Suppression of de novo purine synthesis in hypoxia might be a protective adaptation because building new AMP molecules is energetically costly" (p.13-14).
- Decreased Myc activity may mediate purine-synthesis suppression (p.13, correlative).
- Disrupted division of labor may extend to other costly processes (cholesterol synthesis, lipogenesis) (p.14).

### Caveats and self-criticism

- Effects "likely multifactorial" given global physiological changes of systemic hypoxia.
- Causal role of Myc not established ("further work is required").
- Hypoxanthine enrichment in TIF may reflect turnover rather than available salvage substrate.
- ccRCC resistance mechanism (VHL-independent) unexplained.

### Future directions suggested

- Dissect tumor-intrinsic vs extrinsic growth signaling, exogenous nutrient availability, and immune surveillance under systemic hypoxia.
- Optimize hemoglobin-O2-affinity compounds (HypoxyStat) to widen the therapeutic window.
- Investigate/limit side effects (pulmonary hypertension, erythrocytosis, edema).

## Limitations

- Single preprint, not peer-reviewed; predominantly mouse models; many findings from one line (Panc02).
- GENEVA uses immunocompromised NSG hosts (no adaptive immunity) for the human-line mechanism work.
- Fitness/gene-expression associations are correlational; Myc causality untested.
- Altitude-cancer epidemiology is ecological/correlational with residual-confounding risk.

## Open questions

### Open questions raised by authors

- What is the precise role of decreased Myc activity in mediating tumor suppression?
- How do tumor-extrinsic factors (nutrients, immune surveillance) contribute?
- How can pharmacological hypoxia be optimized for a safe therapeutic window in humans?

### Open questions identified during ingest

- Does systemic-hypoxia tumor suppression require any immune contribution (given anti-CTLA4 synergy) vs pure metabolic effect?
- Would direct pharmacological de novo purine-synthesis inhibition phenocopy systemic hypoxia, and is the combination additive?
- What metabolic feature renders VHL-WT ccRCC lines resistant?

## My take

A genuinely paradigm-shifting framing for the hypoxia thesis: systemic vs local hypoxia have opposite tumor effects, with a clean metabolic mechanism (de novo purine suppression) and a translational handle (HypoxyStat). The mechanism-exclusion experiments (glucose, insulin/Pten, HIF/Arnt) are unusually rigorous for establishing what is *not* responsible. Strongest as a metabolic story; the Myc and epidemiology arms are suggestive rather than conclusive.

## Related

- [[concepts/systemic-hypoxia-anti-tumor-therapy]]
- [[concepts/de-novo-purine-synthesis-suppression-hypoxic-tumor]]
- [[concepts/geneva-multiplexed-mosaic-xenograft]]
- [[concepts/hypoxystat-hemoglobin-oxygen-affinity-modulator]]
- [[foundations/kras-oncogene]]
- [[foundations/myc-oncogene]]
- [[foundations/pten-tumor-suppressor]]
- [[foundations/arnt-hif1b]]
- [[foundations/hif1a]]
- [[foundations/tp53-tumor-suppressor]]
- [[foundations/ctla-4-checkpoint]]
- [[people/ayush-midha]]
- [[people/isha-jain]]
- [[people/hani-goodarzi]]
