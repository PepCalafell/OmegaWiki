---
title: "Dictionary of immune responses to cytokines at single-cell resolution"
slug: dictionary-immune-responses-cytokines-single-cell
arxiv: ""
doi: "10.1038/s41586-023-06816-9"
pmid: "38057668"
venue: "Nature"
year: 2024
authors:
  - "Ang Cui"
  - "Teddy Huang"
  - "Shuqiang Li"
  - "Aileen Ma"
  - "Jorge L. Pérez"
  - "Chris Sander"
  - "Derin B. Keskin"
  - "Catherine J. Wu"
  - "Ernest Fraenkel"
  - "Nir Hacohen"
first_author: "Ang Cui"
corresponding_author: "Ang Cui; Nir Hacohen"
source_type: tex
s2_id: "1aee0fb07f8699a74a9c0ec8419fbc058029eaa8"
date_added: 2026-05-13
ingested_date: 2026-05-13
ingest_version: 1
last_reviewed:
importance: 5
tier: TIER_1
tags:
  - cytokines
  - immune-dictionary
  - IREA
  - single-cell
  - polarization
  - cell-cell-communication
  - immunology-atlas
  - in-vivo-perturbation
  - cytokine-network
  - immune-plasticity
keywords:
  - Immune Dictionary
  - IREA
  - 86 cytokines
  - lymph node perturbation
  - scRNA-seq
  - cell-type-specific cytokine response
  - cytokine pleiotropy
  - polarization states
  - cytokine interactome
  - anti-PD-1
  - TGFβ1
  - IL-18 NK
  - IL-1β multicellular response
domain: immunology
tissue:
  - lymph_node
condition:
  - healthy
species:
  - mouse
hypoxia_relevant: false
contains_immune_cells: true
contains_myeloid: true
techniques:
  - scRNA-seq_10x
  - in_vivo_cytokine_perturbation
  - sample_multiplexing
  - DEG_analysis
  - gene_programme_decomposition
  - subcluster_polarization_analysis
  - cytokine_response_enrichment_IREA
n_samples: 280
n_cells_total: 386703
integration_method: ""
key_cell_types:
  - B cell
  - CD4+ T cell
  - CD8+ T cell
  - γδ T cell
  - Treg cell
  - NK cell
  - ILC
  - pDC
  - cDC1
  - cDC2
  - MigDC
  - Langerhans cell
  - eTAC
  - Macrophage (Marco+, Lyz1+)
  - Monocyte
  - Neutrophil
  - Mast cell
  - Basophil
  - BEC
  - LEC
  - FRC
key_markers:
  - IL-1β
  - IL-1α
  - IL-18
  - IL-2
  - IL-4
  - IL-13
  - IL-12
  - IL-15
  - IL-21
  - IL-23
  - IL-36α
  - IL-7
  - IL-10
  - IFNα1
  - IFNβ
  - IFNγ
  - IFNε
  - IFNκ
  - TNF
  - TGFβ1
  - GM-CSF
  - CD40L
  - TL1A
  - TSLP
  - Cxcl9
  - Cxcl10
  - Ccr7
  - Cd14
  - Hif1a
  - Ctla4
  - Il4i1
  - Gzmb
  - Xcl1
  - Myc
  - Csf2
  - Kit
  - Batf
  - Cd40
  - Cd47
  - PD-1
  - PD-L1
  - Isg15
  - Ifit1
  - Ifit3
  - Stat1
  - Cxcl3
  - Cxcl2
  - Tnfaip3
  - Bcl2
  - Retnla
  - Chchd10
  - Il22
  - Il1b
key_pathways:
  - IL-1 signaling
  - type I IFN / ISGF3
  - type II IFN / STAT1
  - common γ-chain cytokines
  - common β-chain cytokines
  - IL-6/IL-12/STAT3
  - IL-10 family
  - IL-17 family
  - TNF superfamily
  - complement
  - growth factor signaling
  - cytokine-receptor expression mapping
  - cell-cell interactome
projects:
  - thesis
priority: core
read_status: read
hypoxiaverse_status: candidate
exclusion_reason:
data_availability: "Immune Dictionary portal (www.immune-dictionary.org); GEO accession associated with the paper"
code_url: "https://github.com/cui-lab/IREA"
cited_by:
  - single-cell-cytokine-dictionary-human-peripheral
  - immune-dictionary-immune-response-enrichment-analysis
---

## Problem

We lack a global, single-cell-resolution view of how each immune cell type responds to each cytokine in vivo. Prior bulk and cell-line studies obscure pleiotropy, while ligand–receptor inference tools (CellPhoneDB, CellChat, NicheNet) over-rely on receptor transcript expression — a poor predictor of actual cytokine response. The result: ad hoc, cell-line-biased, mechanism-impoverished cytokine biology, despite cytokines being among the most clinically actionable therapeutic targets in oncology and autoimmunity.

## Key idea

Build the **Immune Dictionary**: an in vivo perturbational scRNA-seq atlas covering 86 cytokines × 17+ immune cell types in mouse lymph nodes (>1,400 cytokine × cell-type combinations, 386,703 cells). Use it (i) to quantify per-cell-type cytokine response signatures, (ii) to identify 66 cytokine-driven polarization states, (iii) to map cytokine production sources and (iv) to build a quantitative cytokine-mediated cell–cell interactome. Release **IREA** (Immune Response Enrichment Analysis), the companion software that infers active cytokines, polarization states, and cell–cell communication networks from any transcriptomic dataset by enrichment against the Dictionary's response signatures.

## Method

- **Perturbation**: subcutaneous + intradermal injection of each recombinant carrier-free mouse cytokine (5 μg in 100 μl PBS) in C57BL/6 abdominal flank; PBS controls per batch; 3 mice per cytokine; 14 PBS-injected mice total.
- **Tissue**: bilateral skin-draining inguinal lymph nodes harvested 4 h post-injection.
- **scRNA-seq**: 10x Genomics droplet-based, with cell sorting to rebalance cell-type frequencies and high-throughput multiplexing for batch consistency.
- **Analysis**: clustering for cell-type identity (>20 cell types identified); DEG calling per cytokine × cell type (two-sided Wilcoxon, |log2FC|>0.25, FDR<0.05); gene-programme (GP) decomposition; subcluster-based polarization-state definition; production map from per-cell-type cytokine transcript expression; interactome from production × response matching.
- **Software**: IREA — enrichment test on dictionary signatures + polarization states; outputs radar plots, ES-bar plots, network diagrams.
- **Validation**: applied IREA to anti-PD-1 mouse tumour scRNA-seq (Gubin 2018) and severe COVID-19 PBMC scRNA-seq (Wilk 2020).

## Results

- 386,703 high-quality single-cell transcriptomes across 86 cytokines + PBS; >20 cell types identified.
- Average 51 DEGs per cytokine × cell-type combination (range 0–1,510); 72% upregulated.
- Most cytokines induce highly cell-type-specific gene programmes (IL-1β paradigm).
- Type I IFN (IFNα1, IFNβ) is the exception: induces common, autonomous ISG-I programmes (GP27/33/34) across nearly all cell types.
- 66 cytokine-driven polarization states defined across 17 cell types.
- IL-18 induces unique NK-f polyfunctional state (>1,000 genes; Myc/Xcl1/Csf2/Gzmb/Kit/Batf).
- Macrophage Mac-b (IFNγ → M1-like, Cxcl9/Cxcl10) vs Mac-e (IL-4/IL-13 → M2-like, Chchd10/Glrx/Retnla) recapitulate classical M1/M2 at scRNA-seq resolution.
- Resting B and T cells polarize via cytokines alone (CD40L/IL-21 proliferation; IL-4 → Il4i1+ B-f; IL-23 → γδ T cell Tgd-f / Il22).
- Rare cell types (FRCs, basophils, ILCs) produce the most cytokines (Pearson r = -0.71, P = 0.0065, abundance vs production).
- Most immune cell types affect most others through ≥1 cytokine (high network interconnectivity).
- Receptor expression is necessary but not sufficient for response (false positives + false negatives).
- IREA on anti-PD-1 tumours: Mac → Mac-b (M1-like); NK → NK-e (cytotoxic); TGFβ1 is the most negatively enriched cytokine response.

## All claims (exhaustive)

- `[c01]` Most cytokines induce highly cell-type-specific gene programmes (p.380) "Most of the upregulated genes in response to a particular cytokine were specific to one cell type regardless of thresholds for defining DEGs" — confidence: high — type: correlational — links: [[concepts/cytokine-cell-type-specific-response-pleiotropy]] [[foundations/immune-dictionary-dataset]] [[claims/most-cytokines-induce-highly-cell-type]]
- `[c02]` IL-1β induces distinct gene programmes in almost every immune cell type (p.380) "IL-1α and IL-1β trigger a coordinated multicellular response composed of highly cell-type-specific functions" — confidence: high — type: mechanistic — links: [[concepts/il-multicellular-coordinated-immune-response]] [[foundations/il-beta-cytokine]] [[claims/il-1beta-induces-distinct-gene-programmes]]
- `[c03]` IFNα1 and IFNβ induce a common autonomous antiviral programme across cell types (p.380) "IFNα1 and IFNβ ... induced common antiviral GPs across almost all cell types (GP numbers GP27, GP33 and GP34)" — confidence: high — type: mechanistic — links: [[foundations/type-interferon-ifna-ifnb]] [[concepts/cytokine-cell-type-specific-response-pleiotropy]] [[claims/ifnalpha-ifnbeta-induce-common-autonomous-antiviral]]
- `[c04]` Immune Dictionary defines 66 cytokine-driven polarization states across 17 cell types (p.380) "we defined 66 major polarization states as subclusters significantly enriched for cytokine-treated relative to PBS-treated cells" — confidence: high — type: methodological — links: [[concepts/cytokine-driven-immune-polarization-states-atlas]] [[foundations/immune-dictionary-dataset]] [[claims/immune-dictionary-characterizes-66-cytokine-driven]]
- `[c05]` IL-18 induces a unique polyfunctional NK-f state with >1,000 upregulated genes (p.380) "IL-18 triggered the upregulation of more than 1,000 genes ... an order of magnitude more than cells stimulated with other cytokines ... suggests a polyfunctional role for the IL-18–NK cell axis" — confidence: high — type: mechanistic — links: [[concepts/il-18-polyfunctional-nk-cell-state]] [[foundations/il-18-cytokine]] [[claims/il-18-induces-unique-polyfunctional-nk]]
- `[c06]` IL-4 polarizes B cells to a distinct Il4i1+ state (B-f) (p.380) "B cells were polarized by IL-4 to a distinct Il4i1+ state" — confidence: high — type: mechanistic — links: [[concepts/cytokine-driven-immune-polarization-states-atlas]] [[claims/il-polarizes-cells-distinct-il4i1-positive]]
- `[c07]` CD40L or IL-21 polarize B cells to proliferating phenotype (B-e) (p.380) "CD40L or IL-21 to a proliferating phenotype" — confidence: medium — type: mechanistic — links: [[concepts/cytokine-driven-immune-polarization-states-atlas]] [[claims/cd40l-il-21-polarize-cells-proliferating]]
- `[c08]` IL-23 polarizes γδ T cells to Il22-expressing Tgd-f state (p.380) "a distinct Tgd-f state induced by IL-23 that overexpresses Il22" — confidence: high — type: mechanistic — links: [[concepts/cytokine-driven-immune-polarization-states-atlas]] [[claims/il-23-polarizes-gamma-delta-cells]]
- `[c09]` Mac-b (IFNγ-induced) is M1-like; Mac-e (IL-4/13-induced) is alternatively activated (p.380) "IFNγ induced a 'Mac-b' state that overexpresses M1-associated pro-inflammatory genes (for example, Cxcl9 and Cxcl10). IL-4 and IL-13 induced a distinct 'Mac-e' state ... marked by Chchd10, Glrx and Retnla" — confidence: high — type: mechanistic — links: [[concepts/m1-m2-polarization-paradigm]] [[foundations/ifn-gamma-cytokine]] [[claims/macrophage-mac-state-induced-ifng-m1]]
- `[c10]` Rare cell types (FRCs, basophils, ILCs, eTACs, LECs) produce the most distinct cytokines (p.382) "FRCs expressed the highest number of distinct cytokines ... Other rare cell types in lymph nodes, such as basophils and ILCs, also expressed a large number of cytokines" — confidence: high — type: correlational — links: [[concepts/rare-immune-cell-types-produce-many]] [[claims/cytokine-production-sources-enriched-rare-immune]]
- `[c11]` Inverse correlation between cell-type abundance and cytokine production (Pearson r = -0.71, P = 0.0065) (Fig. 4b, p.382) "rarer cell types are crucial players in immune cell–cell communication networks despite their low numbers" — confidence: high — type: quantitative — links: [[concepts/rare-immune-cell-types-produce-many]] [[claims/inverse-correlation-between-cell-type-abundance]]
- `[c12]` Cytokine receptor expression alone is insufficient to predict cytokine response (p.383) "Some cytokines induced responses even in the absence of highly expressed receptors ... receptor expression alone is not an accurate predictor of cytokine responses" — confidence: high — type: methodological — links: [[concepts/cytokine-receptor-expression-insufficient-cytokine-response]] [[claims/cytokine-receptor-expression-alone-sufficient-predict]]
- `[c13]` Most immune cell types can affect most other cell types through ≥1 cytokine (p.382) "most cell types can affect almost every other cell type through at least one cytokine ... demonstrating a high level of interconnectivity" — confidence: medium — type: correlational — links: [[concepts/cytokine-mediated-immune-cell-cell-interactome]] [[claims/most-immune-cell-types-affect-most]]
- `[c14]` IREA infers cytokine activities, cell polarization and cell–cell networks from transcriptomic data (p.383) "IREA implements statistical tests to assess the enrichment of either cell polarization or cytokine signatures in transcriptomes, which can then be used to derive cell–cell communication networks" — confidence: high — type: methodological — links: [[foundations/irea-immune-response-enrichment-analysis-software]] [[concepts/cytokine-mediated-immune-cell-cell-interactome]] [[claims/irea-enables-inference-cytokine-activities-cell]]
- `[c15]` Anti-PD-1 polarizes tumour macrophages to Mac-b (M1-like) and NK cells to NK-e (cytotoxic) (p.383) "IREA automatically inferred that monocytes and macrophages after treatment polarized into the IFNγ-induced 'Mac-b' (M1-like) state and away from the IL-4-induced 'Mac-e' state ... polarization of NK cells into a cytotoxic 'NK-e' state" — confidence: high — type: correlational — links: [[foundations/irea-immune-response-enrichment-analysis-software]] [[concepts/m1-m2-polarization-paradigm]] [[claims/anti-pd1-treatment-polarizes-tumour-macrophages]]
- `[c16]` TGFβ1 is the most negatively enriched cytokine response in tumours after anti-PD-1 therapy (p.384) "the immunosuppressive cytokine TGFβ1 showed the most negative response in anti-PD-1-treated cells compared with untreated cells" — confidence: high — type: correlational — links: [[foundations/tgfb1-cytokine]] [[foundations/irea-immune-response-enrichment-analysis-software]] [[claims/tgfb1-shows-strongest-negative-cytokine-response]]
- `[c17]` 72% of cytokine-induced DEGs are upregulated (p.379) "the majority (72%) of the DEGs responding to cytokines were upregulated rather than downregulated" — confidence: high — type: quantitative — links: [[foundations/immune-dictionary-dataset]] [[claims/72-percent-cytokine-induced-degs-upregulated]]
- `[c18]` Average 51 DEGs per cytokine × cell-type combination (range 0–1,510) (p.379) "We identified an average of 51 DEGs (span of 0–1,510) per cytokine–cell type combination" — confidence: high — type: quantitative — links: [[foundations/immune-dictionary-dataset]] [[claims/average-51-degs-per-cytokine-cell]]

## Discussion captured

### Authors' interpretation

The authors interpret the Dictionary as evidence that "the complexity of cytokine responses and plasticity of immune cells are much greater than previously appreciated." They emphasize that even a single cytokine triggers distinct responses in each cell type to create a coordinated multicellular immune response, extending early macrophage M1/M2 work to a general principle covering every immune lineage. They position IREA as a general inference framework for any immune-relevant transcriptomic dataset.

### Comparisons with prior literature (made by authors)

- Mills 2000 / Martinez & Gordon 2014: M1/M2 paradigm — extended by Mac-a/b/c/d/e at scRNA-seq resolution.
- Xue 2014 *Immunity*: spectrum model of human macrophage activation — recapitulated and refined.
- Lavin 2014 *Cell*: tissue-resident macrophage enhancer landscapes shaped by local microenvironment — conceptually aligned.
- Crinier 2018 *Immunity*: NK cell diversity in mouse and human — extended by NK-c/e/f.
- Jiang 2021 *Nat Methods* (CytoSig), Browaeys 2020 *Nat Methods* (NicheNet) — IREA positioned as a complementary, signature-based alternative to L-R inference.
- Vento-Tormo 2018, Ramilowski 2015: ligand-receptor networks — critiqued for receptor-only inference.
- Gubin 2018 *Cell*: anti-PD-1 myeloid/lymphoid remodelling — reanalyzed via IREA.
- Garris 2018 *Immunity*: IFN-γ–IL-12 DC–T cell crosstalk in anti-PD-1 response — corroborated.
- Mariathasan 2018 *Nature*: TGFβ attenuates ICB — corroborated.
- Wilk 2020 *Nat Med* (severe COVID-19 PBMC scRNA-seq) — reanalyzed via IREA.

### Mechanistic hypotheses proposed

- Coordinated multicellular response model: cytokines like IL-1β achieve tissue-level function through structured per-cell-type programmes (neutrophil chemokines, MigDC migration, Treg suppression).
- Polyfunctional NK-f state: IL-18 NK biology extends beyond IFNγ-induction to encompass proliferation + cytotoxicity + DC recruitment + myeloid maturation.
- Rare-cell-type broadcasting: stromal and rare innate populations (FRCs, basophils, ILCs) are network hubs.
- Receptor-expression-insufficient hypothesis: response inference must use downstream signatures, not just receptor presence.

### Caveats and self-criticism

The authors acknowledge: (i) some cell-type-specific responses to a single cytokine could reflect secondary effects from induced cytokines (e.g., IL-2/12/15/18 → NK Ifng → secondary IFNγ signatures in B cells/DCs/macrophages); (ii) cytokine responses without receptor expression could be due to insensitive transcript detection, rapid secondary effects, or unknown receptors; (iii) supraphysiological doses and a single 4-h timepoint may miss dose-response and temporal dynamics.

### Future directions suggested

- Different cytokine doses and time points
- Different biological contexts (other tissues, disease states)
- Combinations of stimuli (multi-cytokine perturbations)
- Re-analysis of any cell subpopulation of interest using the dataset

## Limitations

- Mouse only (no human Immune Dictionary equivalent yet).
- Single tissue (skin-draining lymph node) — generalizability to tumour, gut, lung, skin tissue contexts unverified.
- Single timepoint (4 h) — does not capture late waves of response.
- Single cytokine per perturbation — no combinatorial logic captured.
- Supraphysiological cytokine doses.
- Secondary effects (induced cytokines acting on other cells) confound direct vs indirect attribution.
- Receptor detection sensitivity limits the interpretability of receptor-low responder calls.
- Resting B and T cells (no antigen) — physiological lymphocyte contexts mix TCR/BCR + cytokine signals.

## Open questions

### Open questions raised by authors

- How do cytokine combinations interact (synergy, antagonism, dominance)?
- What is the temporal evolution of cytokine-driven polarization states?
- Does the lymph-node dictionary translate to other tissues and to humans?
- How do dose-response relationships shape polarization-state induction?

### Open questions identified during ingest

- Can IREA reliably identify tumour-derived cytokine networks in hypoxic, structurally remodelled tumours where the cell-type composition differs from lymph node?
- How does the Mac-a/b/c/d/e taxonomy map onto hypoxic TAM phenotypes (e.g., mmac1-hypoxic-inflammatory-macrophage)?
- Is the IL-18 NK-f state operative in tumour-infiltrating NK cells?
- Can the Immune Dictionary serve as a reference panel for human PBMC datasets despite species differences?

## My take

This is the most ambitious in vivo perturbational cytokine atlas to date and the natural reference for any project that infers cytokine activity from transcriptomic data. The conceptual contribution — cytokine pleiotropy is structurally encoded in cell-type-specific transcriptional programmes — is more important than any single empirical finding. The IL-18 NK-f discovery is the most striking single mechanistic claim and is worth replication in human NK cells. For HypoxiaVERSE: (i) IREA is immediately applicable to TAM/NK scRNA-seq for inferring active cytokines in hypoxic vs normoxic tumour regions; (ii) the Mac-a/b/c/d/e taxonomy provides a clean reference against which to benchmark hypoxic TAM phenotypes; (iii) the receptor-expression-insufficient observation is a methodological caution for any CellPhoneDB/CellChat work in the project.

## Related

- [[concepts/cytokine-cell-type-specific-response-pleiotropy]], [[concepts/cytokine-driven-immune-polarization-states-atlas]], [[concepts/il-multicellular-coordinated-immune-response]], [[concepts/il-18-polyfunctional-nk-cell-state]], [[concepts/rare-immune-cell-types-produce-many]], [[concepts/cytokine-receptor-expression-insufficient-cytokine-response]], [[concepts/cytokine-mediated-immune-cell-cell-interactome]] — primary concept anchors.
- [[concepts/m1-m2-polarization-paradigm]] — refined by Mac-a/b/c/d/e at scRNA-seq resolution.
- [[foundations/irea-immune-response-enrichment-analysis-software]], [[foundations/immune-dictionary-dataset]] — software + dataset deliverables.
- [[papers/pd-l1-expressing-tumor-associated-macrophages]] — IREA's anti-PD-1 application corroborates Mac-b / M1-like findings; complementary axis.
- [[papers/cross-tissue-single-cell-landscape-human]] — complementary single-cell atlas of macrophage diversity.

- [[papers/aryl-hydrocarbon-receptor-rehabilitated-target-therapeutic]] — NRDD 2025 review of AHR biology and therapeutic targeting; provides pharmacological framework for the Trp-Kyn-AHR / IDO1 / IL4I1 immunosuppression axis discussed here
- [[papers/pairwise-cytokine-code-explains-organism-wide]] — complementary axis: pairwise (vs single) cytokine perturbation, in vivo organism-wide (vs ex vivo lymph node), bulk tissue (vs single-cell) resolution; both papers anchor the cytokine-perturbation literature for the wiki.
- [[papers/single-cell-cytokine-dictionary-human-peripheral]] — the human PBMC counterpart (Oesinghaus/Seelig/Theis 2025); directly compares 81 shared cytokines against this mouse Dictionary and finds only weak human↔mouse gene-level concordance, plus human-specific cytokines (IL-32) absent in mouse.
- [[papers/immune-dictionary-immune-response-enrichment-analysis]] — web-portal companion (Lai, …, Cui; AAI 2025) deploying this atlas + IREA as a freely-available interactive web application with added chemokine coverage and network-analysis upgrades.
