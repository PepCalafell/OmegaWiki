---
# === Identification ===
title: "A single-cell cytokine dictionary of human peripheral blood"
slug: single-cell-cytokine-dictionary-human-peripheral
arxiv: ""
doi: "10.64898/2025.12.12.693897"
pmid: "41446101"
venue: "bioRxiv"
year: 2025
authors:
  - "Lukas Oesinghaus"
  - "Sören Becker"
  - "Larsen Vornholz"
  - "Efthymia Papalexi"
  - "Joey Pangallo"
  - "Amir Ali Moinfar"
  - "Jenni Liu"
  - "Alyssa La Fleur"
  - "Maiia Shulman"
  - "Alexander B. Rosenberg"
  - "Charles M. Roco"
  - "Georg Seelig"
  - "Fabian J. Theis"
first_author: "Lukas Oesinghaus"
corresponding_author: "Charles M. Roco; Georg Seelig; Fabian J. Theis"

# === Source & metadata ===
source_type: tex
s2_id: "637bef4833b867247c09057957946acc038e5092"
date_added: 2026-05-28
ingested_date: 2026-05-28
ingest_version: 1
last_reviewed:

# === Classification ===
importance: 4
tier: TIER_1
tags:
  - cytokines
  - human-cytokine-dictionary
  - PBMC
  - single-cell
  - perturbation-atlas
  - IL-32
  - cytokine-induced-immune-programs
  - cell-cell-communication
  - donor-variability
  - huCIRA
keywords:
  - Human Cytokine Dictionary
  - 90 cytokines
  - 9.7 million PBMCs
  - split-pool barcoding
  - cytokine response magnitude
  - tissue specificity index
  - IL-32-beta myeloid reprogramming
  - cytokine-induced immune programs (CIP)
  - DRVI
  - huCIRA
  - human-mouse cytokine divergence
  - secondary cytokine cascade
domain: immunology

# === Biomedical domain ===
tissue:
  - blood
  - in_vitro_only
condition:
  - healthy
  - autoimmune
  - cancer
disease_specific:
  - SLE
  - multiple_sclerosis
  - NSCLC
species:
  - human
hypoxia_relevant: false
contains_immune_cells: true
contains_myeloid: true

# === Technique ===
techniques:
  - scRNA-seq_split-pool
  - in_vitro_cytokine_perturbation
  - DRVI_gene_programs
  - enrichment_analysis_huCIRA
  - spatial_transcriptomics
n_samples: 12
n_cells_total: 9697974
integration_method: ""

# === Biology captured ===
key_cell_types:
  - B cell (naive + intermediate)
  - CD4 T cell (naive + memory)
  - CD8 T cell (naive + memory)
  - Treg
  - MAIT cell
  - NKT cell
  - NK CD56hi
  - NK CD56low
  - cDC
  - CD14 monocyte
  - CD16 monocyte
  - HSPC
  - pDC
  - ILC
  - granulocyte
  - plasmablast
key_markers:
  - IL-32
  - IL-15
  - IL-4
  - GM-CSF
  - IFN-β
  - IL-10
  - IL-19
  - IL-24
  - CXCL1
  - CXCL2
  - CXCL3
  - CXCL5
  - CXCL8
  - CXCL9
  - CXCL10
  - CXCL11
  - IFIT1
  - IFIT3
  - IL4I1
  - IGHE
  - CD14
key_pathways:
  - type I IFN / ISG
  - type II IFN / STAT1
  - common γ-chain cytokines
  - IL-32-β signaling
  - chemokine signaling
  - IL-10 family
  - JAK-STAT
  - cytokine-mediated cell-cell communication

# === User project membership ===
projects:
  - thesis
priority: context
read_status: read

# === HypoxiaVERSE-specific ===
hypoxiaverse_status: candidate
exclusion_reason:
data_availability: "Open-access Human Cytokine Dictionary resource + huCIRA Python package (bioRxiv 2025; doi:10.64898/2025.12.12.693897). PMC: PMC12724453."

# === Cross-references ===
code_url: ""
cited_by: []
---

## Problem

Cytokines orchestrate immune responses, but their pleiotropy, context dependence, and functional redundancy mean we still lack a comprehensive, cell-type-resolved view of what each cytokine does to each human immune cell. Prior knowledge is fragmented across heterogeneous experimental systems with batch effects that prevent direct comparison, and the most ambitious existing perturbation atlas (the mouse Immune Dictionary, Cui et al. 2024) is in mouse — leaving open how well it translates to human and missing human-specific cytokines (e.g. IL-32, which has no mouse homologue).

## Key idea

Build a **Human Cytokine Dictionary**: stimulate human PBMCs in vitro with 90 individual cytokines and record the single-cell transcriptional response at massive scale (9,697,974 cells, 12 donors) using Parse Biosciences split-pool barcoding. From this, (i) quantify per-cell-type cytokine response signatures and a continuous response magnitude / tissue-specificity index, (ii) characterize donor-to-donor variation and robust consensus responses, (iii) compare human vs mouse responses, (iv) infer cytokine production and cell–cell/cytokine–cytokine communication networks, (v) decompose responses into data-driven cytokine-induced immune programs (CIPs) via DRVI, and (vi) release **huCIRA**, an open-source enrichment tool to decode cytokine activity in any human dataset (demonstrated on SLE, MS, NSCLC).

## Method

- **Perturbation**: PBMCs from 12 healthy donors (6M/6F, ages 34-75, Seattle Bloodworks) treated in vitro for 24 h with each of 90 individual cytokines or PBS; cytokines span IL-1, common γ-chain, IL-4/IL-13, common β-chain, IL-6, IL-12, IL-10, IL-17, interferons, TNF, complement, growth factors, TGF-β, and more, at upper-range in vitro concentrations.
- **scRNA-seq**: Parse Biosciences split-pool barcoding (GigaLab); 9,697,974 cells retained after QC; 16 major cell types annotated, 12 retained for response analysis (pDC, ILC, granulocytes, plasmablasts dropped for <10 median cells/condition).
- **DE analysis**: donor-aggregated, donor-consensus DEGs and log2FCs (cytokine vs PBS; padj<0.05, |log2FC|>0.25). Continuous response magnitude (p-value-weighted Euclidean distance of log2 expression); tissue specificity index (TSI); per-cell-type "strong impact" threshold.
- **Donor variability**: baseline log2FC vs median; identification of an interferon-high donor group; outlier/response-substructure analysis.
- **Cross-species**: comparison to Cui et al. 2024 mouse Immune Dictionary (81 shared cytokines) and to Kang et al. human IFN-β data; reference database from ImmunoGlobe + immuneXpresso.
- **Networks**: stimulation-agnostic cytokine production per cell type; sender strength × receiver sensitivity = interaction score → cell–cell connection strength; cytokine→cytokine regulation; secondary-response detection (receptor-low responders explained by induced secondary cytokines).
- **Programs**: DRVI (disentangled VAE) → 82 cytokine-induced immune programs (CIPs), annotated into 11 categories.
- **huCIRA**: gseapy-based enrichment tool over DE + CIP gene sets; applied to SLE, MS (scRNA-seq) and NSCLC (spatial).

## Results

- 9,697,974 PBMCs, 90 cytokines, 12 donors, 16 cell types (12 analyzed). Few perturbations shift cell-type composition.
- IL-1, common γ-chain interleukins, IL-4, IL-10, interferons, and IL-32-β are the broadest responders; most cytokines are narrow.
- TSI: TPO most cell-type-specific (0.93, HSPC-only); IL-15 least (0.07, affects all).
- Receptor expression ↔ response magnitude correlate (r≈0.4) above ~8 cpm baseline; high receptor expression ≠ guaranteed response (Decorin, Resistin, TRAIL/FasL, TGF-β1).
- An interferon-high donor group (D1/D3/D4/D10; elevated baseline ISGs; 3/4 oldest) shows distinct responses, but consensus responses remain robust.
- IL-32-β response in CD4 T cells is donor-interferon-state-dependent (IL-10-like only in pre-inflamed donors).
- Human↔mouse responses correlate weakly (median r≈0.19; 11.3% concordant, 6.9% discordant strongly regulated genes); within-human > cross-species even at matched timepoints.
- Cytokine production is strongly cell-type-specific; IL-32 is a dominant T-cell→all connector; NK CD56hi signals broadly, NK CD56low not at all.
- IL-15 is the most prolific cytokine-regulating cytokine (146 events).
- **IL-32-β reprograms myeloid cells** from Th1/antiviral chemokines (CXCL9/10/11, IL-18 down) to neutrophil-recruiting chemokines (CXCL1/2/3/5/8, IL-1α/β up), uniquely inducing the IL-10 family (IL-10/IL-19/IL-24).
- Secondary cascade: NK-derived IFN-γ mediates monocyte responses to IL-2/IL-12/IL-15.
- DRVI → 82 CIPs (57 myeloid, 12 lymphoid, 10 shared) in 11 categories.
- huCIRA recovers disease cytokine activity: SLE flare (type I IFN + IL-15 + IL-32-β), MS (cytotoxic NK CIPs), NSCLC tumor monocytes (GM-CSF/IL-3 → TAM reprogramming).

## All claims (exhaustive)

- `[c01]` Human Cytokine Dictionary = 9.7M PBMCs × 12 donors × 90 cytokines (p.1-2) "we present a Human Cytokine Dictionary, created from high-resolution single-cell transcriptomes of 9,697,974 human peripheral blood mononuclear cells (PBMC) from 12 donors stimulated in vitro with 90 different cytokines" — confidence: high — type: methodological — links: [[foundations/human-cytokine-dictionary-dataset]] [[foundations/parse-biosciences-split-pool-barcoding]] [[claims/human-cytokine-dictionary-profiles-million-pbmcs]]
- `[c02]` Few cytokine perturbations shift PBMC cell-type composition (p.3) "Few perturbations result in major shifts in cell type abundance or composition" — confidence: medium — type: correlational — links: [[claims/few-cytokine-perturbations-cause-major-shifts]]
- `[c03]` IL-1, common γ-chain, IL-4, IL-10, interferons, IL-32-β are the broadest DEG responders (p.5) "IL-1, common γ chain interleukins, IL-4, IL-10, interferons, and IL-32-β have the largest number of DEGs across cell types" — confidence: high — type: correlational — links: [[concepts/cytokine-cell-type-specific-response-pleiotropy]] [[claims/il-common-gamma-chain-il-il]]
- `[c04]` Response tissue-specificity ranges from TPO (TSI 0.93) to IL-15 (TSI 0.07) (p.5) "tissue specificity index (TSI), which is highest for TPO (0.93, only affects HSPCs) and lowest for IL-15 (0.07, affects all cell types)" — confidence: high — type: quantitative — links: [[foundations/il-15-cytokine]] [[concepts/cytokine-cell-type-specific-response-pleiotropy]] [[claims/cytokine-response-tissue-specificity-ranges-tpo]]
- `[c05]` Receptor expression and response magnitude correlate (r≈0.4) above ~8 cpm (p.6) "receptor expression and response magnitude are correlated (r≈0.4) and responses generally require a minimum baseline receptor expression (≈8 counts per million (cpm))" — confidence: medium — type: quantitative — links: [[concepts/cytokine-receptor-expression-insufficient-cytokine-response]] [[claims/cytokine-receptor-expression-response-magnitude-correlated]]
- `[c06]` High receptor abundance ≠ strong response (p.6) "high receptor transcript abundance does not always translate into strong responses ... atypical ligands such as Decorin, Resistin ... death ligands (TRAIL, FasL) ... and TGF-β1" — confidence: high — type: methodological — links: [[concepts/cytokine-receptor-expression-insufficient-cytokine-response]] [[foundations/tgfb1-cytokine]] [[claims/high-receptor-transcript-abundance-does-always]]
- `[c07]` An interferon-high donor group exists (elevated baseline ISGs) (p.8) "A subset of donors (D1, D3, D4, D10) is highly correlated in its baseline log2FC ... high baseline expression of interferon-stimulated genes (ISG) (e.g. IFIT1-3)" — confidence: high — type: correlational — links: [[concepts/donor-baseline-interferon-signaling-heterogeneity]] [[foundations/type-interferon-ifna-ifnb]] [[claims/subset-donors-exhibit-elevated-baseline-interferon]]
- `[c08]` Consensus responses are robust despite donor heterogeneity (p.10) "the overall patterns were thus robust enough that a single set of log2FCs per cell type captures a meaningful consensus response" — confidence: high — type: correlational — links: [[concepts/donor-baseline-interferon-signaling-heterogeneity]] [[claims/cytokine-response-profiles-consistent-across-donors]]
- `[c09]` IL-32-β response in CD4 T cells depends on donor interferon state (p.9) "the response to IL-32-β in CD4 T cells ... depended heavily on the donor interferon state ... strong correlation with the consensus IL-10 log2FCs that is absent in the non-interferon group" — confidence: medium — type: mechanistic — links: [[concepts/donor-baseline-interferon-signaling-heterogeneity]] [[foundations/il-32-cytokine]] [[foundations/il-10-cytokine]] [[claims/il-32-beta-response-cd4-cells]]
- `[c10]` Human and mouse cytokine responses correlate weakly (p.10-11) "cross-species correlations were substantially lower (median r=0.19) ... only ... 11.3% display strongly concordant regulation ... 6.9% ... strong discordant responses" — confidence: high — type: quantitative — links: [[concepts/cross-species-human-mouse-cytokine-response]] [[foundations/immune-dictionary-dataset]] [[claims/human-mouse-cytokine-responses-show-low]]
- `[c11]` Within-human correlation exceeds cross-species even at matched timepoints (p.11) "consistently higher in the within-human comparison (mean r=0.61) than in comparisons across species (mean r=0.45 ... and r=0.34 ...)" — confidence: medium — type: quantitative — links: [[concepts/cross-species-human-mouse-cytokine-response]] [[claims/within-human-cytokine-response-correlation-exceeds]]
- `[c12]` Cytokine production is strongly cell-type specific (p.14) "production for most cytokines is strongly cell type-specific ... IL-10 ... by CD14 Mono, CD40L by CD4 T cells and MAITs, and IL-32 by all T cell subtypes but in particular by Tregs" — confidence: high — type: correlational — links: [[concepts/cytokine-mediated-immune-cell-cell-interactome]] [[claims/cytokine-production-strongly-cell-type-specific]]
- `[c13]` IL-32 is a dominant T-cell→all signaling connector (p.15) "yielding IL-32 as a potential dominant signaling molecule connecting all T cell subtypes to all other cell types" — confidence: medium — type: mechanistic — links: [[concepts/cytokine-mediated-immune-cell-cell-interactome]] [[foundations/il-32-cytokine]] [[claims/il-32-dominant-signaling-molecule-connecting]]
- `[c14]` IL-15 is the most prolific cytokine-regulating cytokine (146 events) (p.15) "the most prolific cytokine, IL-15, activating or repressing the expression of other cytokines 146 times across our cell types" — confidence: high — type: quantitative — links: [[foundations/il-15-cytokine]] [[concepts/cytokine-mediated-immune-cell-cell-interactome]] [[claims/il-15-most-prolific-regulator-other]]
- `[c15]` IL-32-β reprograms myeloid cells to a neutrophil-recruiting chemokine profile (p.16) "IL-32-β shifted the chemokine profile in myeloid cells ... from Th1/interferon-like recruitment (downregulation of CXCL9, CXCL10, CXCL11 ... median log2FC~-3.8) to neutrophil recruitment (upregulation of CXCL1, CXCL2, CXCL3, CXCL5, and CXCL8 ... median log2FC~5)" — confidence: high — type: mechanistic — links: [[concepts/il-32-beta-myeloid-neutrophil-inflammatory]] [[foundations/il-32-cytokine]] [[claims/il-32-beta-reprograms-myeloid-cells]]
- `[c16]` IL-32-β uniquely upregulates the IL-10 family in myeloid cells (p.16) "IL-32-β is also the only cytokine that strongly upregulated the IL-10 family in myeloid cells (IL-10, IL-19, IL-24)" — confidence: medium — type: mechanistic — links: [[concepts/il-32-beta-myeloid-neutrophil-inflammatory]] [[foundations/il-10-cytokine]] [[claims/il-32-beta-uniquely-upregulates-il]]
- `[c17]` NK-derived IFN-γ mediates secondary monocyte responses to IL-2/IL-12/IL-15 (p.18) "For the effect of IL-12, IL-2, and IL-15 on monocytes only IFN-γ released by NK CD56hi fulfills these criteria" — confidence: high — type: mechanistic — links: [[concepts/secondary-cytokine-response-cascade]] [[foundations/ifn-gamma-cytokine]] [[claims/ifn-gamma-nk-cells-mediates-secondary]]
- `[c18]` DRVI identifies 82 CIPs (57 myeloid) in 11 categories (p.21-22) "Applying DRVI to our dataset revealed 82 CIPs ... summarized into 11 broad categories ... The majority of CIPs were found in myeloid populations (57 programs)" — confidence: high — type: methodological — links: [[concepts/cytokine-induced-immune-programs-cip]] [[foundations/drvi-disentangled-representation-variational-inference]] [[claims/drvi-identifies-82-cytokine-induced-immune]]
- `[c19]` huCIRA infers cytokine/program activity from independent datasets (p.23) "we developed huCIRA ... an open-source ... Python tool that interfaces gseapy and supports the use of these gene sets in enrichment analyses and differential cell-cell communication inference" — confidence: high — type: methodological — links: [[foundations/hucira-cytokine-immune-response-analysis]] [[claims/hucira-infers-cytokine-program-activity-independent]]
- `[c20]` huCIRA reveals disease-specific cytokine activity (SLE/MS/NSCLC) (p.23-27) "responses to type I IFNs such as IFN-β are strongly enriched in all cell types in flare ... monocytes in the tumor exhibited significantly enriched GM-CSF and IL-3 signaling" — confidence: medium — type: correlational — links: [[foundations/hucira-cytokine-immune-response-analysis]] [[foundations/gm-csf-cytokine]] [[claims/hucira-reveals-disease-specific-cytokine-activity]]

## Discussion captured

### Authors' interpretation

The authors present the Human Cytokine Dictionary as the largest single-cell perturbation dataset of primary human immune cells to date, enabling systematic characterization of donor-specific and consensus cytokine-driven activities. They emphasize that comparison with the mouse dataset reveals both similarities and substantial differences, and that IL-32-β — which has no mouse homologue — converts a type I antiviral myeloid response into a neutrophil-driven inflammatory program. They frame CIPs (via DRVI) as a biologically meaningful interpretive framework and huCIRA as the community tool that operationalizes the resource for disease and cancer datasets.

### Comparisons with prior literature (made by authors)

- Cui et al. 2024 (mouse Immune Dictionary, *Nature*) — the principal cross-species comparator (81 shared cytokines); human responses diverge substantially.
- Kang et al. (human IFN-β-stimulated PBMC, ~6 h) — time-matched human comparator showing within-human > cross-species correlation.
- ImmunoGlobe (Janeway's Immunobiology curation) + immuneXpresso (PubMed text-mining) — integrated reference database of cytokine–cell interactions.
- Rosenberg et al. 2018 (SPLiT-seq) / Parse Biosciences — the split-pool barcoding assay.
- Moinfar & Theis (DRVI) — disentangled latent decomposition method.
- SLE: ~50% of patients have elevated type I IFN / ISGs (refs 53-55); MS cytotoxic NK and pathogenic B-cell biology (refs 61-64); NSCLC GM-CSF→TAM literature (refs 69-73).

### Mechanistic hypotheses proposed

- IL-32-β acts as a human-specific switch converting monocytes from antiviral/Th1-recruiting to neutrophil-recruiting, self-limited by IL-10-family induction ("aggressive, localized containment").
- Secondary-cascade model: 24 h endpoint transcriptomes reflect primary + induced secondary cytokine signaling (NK IFN-γ relaying IL-2/IL-12/IL-15 to monocytes).
- Pre-existing donor interferon state gates certain responses (IL-32-β IL-10-like response in pre-inflamed CD4 T cells).
- Dataset scale enables AI / virtual-cell models of cytokine perturbation (scaling-law argument).

### Caveats and self-criticism

The authors note: (i) the study is anchored at a single 24 h timepoint, missing early and late dynamics; (ii) sample size (12 donors) gives limited resolution to link response variability to genetic/demographic traits; (iii) human-mouse differences are confounded by experimental design (in vitro/in vivo, time, dose, tissue) and cannot be cleanly ascribed to species; (iv) receptor-low responders may reflect secondary cascades, undetected receptors, or detection limits; (v) ethnicity-associated SLE treatment-response findings are limited by sparse genetic/clinical metadata.

### Future directions suggested

- Additional earlier and later timepoints (signaling dynamics).
- Expansion across multiple organ systems toward a comprehensive human perturbation atlas.
- Larger donor cohorts to link variability to genetics/demographics.
- AI / virtual-cell models trained on the dataset.

## Limitations

- In vitro PBMC only — no tissue/stromal/structural context.
- Single 24 h timepoint — conflates direct and secondary-cascade responses.
- Supraphysiological cytokine doses.
- 12 donors — underpowered for genetic/demographic association.
- Single cytokine per perturbation — no combinatorial logic.
- Cross-species comparison confounded by design, not pure species divergence.
- Disease applications (SLE/MS/NSCLC) rely on external datasets with small n (MS 5/5; NSCLC 1 patient).
- Split-pool platform differs from droplet 10x — cross-platform comparison caveats.

## Open questions

### Open questions raised by authors

- What are the early and late dynamics of cytokine-driven responses beyond 24 h?
- Which cytokine response modules are genuinely conserved vs human-specific across species?
- What genetic/demographic factors drive the interferon-high baseline state and donor response variability?
- Can perturbation atlasing be extended across human organ systems?

### Open questions identified during ingest

- Does the IL-32-β myeloid neutrophil-recruiting switch operate in tumor-associated myeloid cells, and is it hypoxia-modulated?
- Can huCIRA reliably infer cytokine activity in hypoxic tumor niches where cell-type composition departs from PBMC?
- How do CIPs map onto in vivo TAM phenotypes relevant to HypoxiaVERSE?
- Is the receptor-expression-insufficiency / secondary-cascade caveat addressable with multi-timepoint human data?

## My take

This is the human counterpart the field needed to the mouse Immune Dictionary, and at far greater scale (~9.7M cells via Parse split-pool). The two most consequential takeaways are translational: (1) human and mouse cytokine responses agree only weakly at the gene level, and (2) IL-32 — with no mouse homologue — is a dominant human myeloid switch, both of which argue for human-native reference atlases in immunotherapy. For HypoxiaVERSE, huCIRA + the CIP/DE gene sets are directly usable for inferring active cytokines in tumor myeloid/NK scRNA-seq and spatial data; the NSCLC GM-CSF→TAM result and the IL-32-β neutrophil-recruiting axis are concrete hypotheses to test in hypoxic vs normoxic tumor regions. Caveat: in vitro, single-timepoint, supraphysiological-dose PBMC signatures transfer to tissue only approximately, and the secondary-cascade caveat means 24 h responses are cascades, not clean direct effects.

## Related

- [[concepts/cytokine-cell-type-specific-response-pleiotropy]], [[concepts/cytokine-mediated-immune-cell-cell-interactome]], [[concepts/cytokine-receptor-expression-insufficient-cytokine-response]] — human-PBMC confirmations/extensions of mouse Dictionary concepts.
- [[concepts/donor-baseline-interferon-signaling-heterogeneity]], [[concepts/cytokine-induced-immune-programs-cip]], [[concepts/il-32-beta-myeloid-neutrophil-inflammatory]], [[concepts/cross-species-human-mouse-cytokine-response]], [[concepts/secondary-cytokine-response-cascade]] — primary new concept anchors.
- [[foundations/human-cytokine-dictionary-dataset]], [[foundations/hucira-cytokine-immune-response-analysis]], [[foundations/drvi-disentangled-representation-variational-inference]], [[foundations/parse-biosciences-split-pool-barcoding]] — dataset / software / method deliverables.
- [[foundations/il-32-cytokine]], [[foundations/il4-cytokine]], [[foundations/il-15-cytokine]], [[foundations/gm-csf-cytokine]] — central cytokines.
- [[papers/dictionary-immune-responses-cytokines-single-cell]] — the mouse Immune Dictionary (Cui et al. 2024); the direct cross-species comparator and conceptual predecessor.
- [[papers/pairwise-cytokine-code-explains-organism-wide]] — complementary cytokine-perturbation axis (pairwise, in vivo, organism-wide).
