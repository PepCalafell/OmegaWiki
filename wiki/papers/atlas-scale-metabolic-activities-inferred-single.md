---
# === Identification ===
title: "Atlas-scale metabolic activities inferred from single-cell and spatial transcriptomics"
slug: atlas-scale-metabolic-activities-inferred-single
arxiv: ""
doi: "10.1101/2025.05.09.653038"
pmid: ""
venue: "bioRxiv (preprint)"
year: 2025
authors:
  - "Erick Armingol"
  - "James Ashcroft"
  - "Magda Mareckova"
  - "Martin Prete"
  - "Valentina Lorenzi"
  - "Cecilia Icoresi Mazzeo"
  - "Jimmy Tsz Hang Lee"
  - "Marie Moullet"
  - "Omer Ali Bayraktar"
  - "Christian Becker"
  - "Krina Zondervan"
  - "Luz Garcia-Alonso"
  - "Nathan E. Lewis"
  - "Roser Vento-Tormo"
first_author: "Erick Armingol"
corresponding_author: "Roser Vento-Tormo"

# === Source & metadata ===
source_type: pdf
s2_id: ""
date_added: 2026-05-27
ingested_date: 2026-05-27
ingest_version: 1
last_reviewed: null

# === Classification ===
importance: 3
tier: TIER_2
tags:
  - scCellFie
  - metabolic-task-inference
  - single-cell-metabolism
  - spatial-metabolism
  - endometrium
  - endometriosis
  - endometrial-carcinoma
  - kynurenine-AHR
  - mevalonate-pathway
  - GPR-rules
  - genome-scale-metabolic-model
  - CELLxGENE
  - Visium
  - metabolite-CCC
  - estrogen-biosynthesis
keywords:
  - scCellFie metabolic-task inference
  - CELLxGENE 30M-cell metabolic atlas
  - kynurenine–AHR signaling endometrial epithelium
  - mevalonate marker malignant EEC cells
  - uM1 macrophage methylglyoxal in endometriosis
  - local androgen-to-estrogen conversion EEC
  - glucose-to-lactate spatial organization in EEC
  - endometrial organoid metabolic fidelity
domain: "methods / metabolism / endometrial biology / oncology"

# === Biomedical domain ===
tissue:
  - uterus
  - endometrium
  - ovary
  - peritoneum
  - multi
condition:
  - healthy
  - cancer
  - inflam_precancer
disease_specific:
  - endometriosis
  - endometrioid_endometrial_cancer_EEC
species:
  - human
  - mouse
hypoxia_relevant: false
contains_immune_cells: true
contains_myeloid: true

# === Technique ===
techniques:
  - scRNA-seq_10x
  - snRNA-seq
  - spatial_visium
  - cell2location_deconvolution
  - GAM_temporal_modeling
  - moran_i_spatial_autocorrelation
  - metabolite-receptor_CCC
  - GPR-rule_metabolic_task_inference
  - KNN_smoothing
n_samples: null
n_cells_total: 30000000
integration_method: ""

# === Biology captured ===
key_cell_types:
  - endometrial_glandular_epithelial
  - endometrial_luminal_epithelial
  - endometrial_stromal_fibroblast
  - decidualized_stromal_fibroblast
  - uterine_M1_macrophage_uM1
  - ovarian_theca_cell
  - ovarian_granulosa_cell
  - lens_fiber_cell
  - pancreatic_acinar_cell
  - adrenal_chromaffin_cell
  - hepatocyte
  - malignant_EEC_cell
key_markers:
  - HMGCR
  - MAOA
  - MAOB
  - APRT
  - HPRT1
  - GALNT4
  - AHR
  - ESR1
  - S100A8
  - S100A9
  - LCN2
  - CTS1
  - LTF
  - CXCL1
  - SAA1
  - SAA2
key_pathways:
  - mevalonate_cholesterol_biosynthesis
  - kynurenine_tryptophan_AHR_signaling
  - glycolysis_glucose_to_lactate
  - PAPS_sulfation_estrogen_inactivation
  - thromboxane_synthesis
  - phenylalanine_to_phenylacetate
  - calnexin_calreticulin_cycle
  - sex_hormone_biosynthesis_steroidogenesis
  - inositol_phosphate_PLC_NFkB
  - methylglyoxal_glycation
  - NAD_salvage
  - nucleotide_salvage_pathway

# === User project membership ===
projects: []
priority: reference
read_status: read

# === HypoxiaVERSE-specific ===
hypoxiaverse_status: excluded
exclusion_reason: "Endometrial / reproductive metabolism focus; not hypoxia-centric. Useful methodologically (single-cell + spatial metabolic-task inference via GPR rules on GEMs) and as a reference for kynurenine-AHR cross-tissue immune-metabolism comparisons."
data_availability: "Visium of peritoneal endometriotic lesions available upon reasonable request from authors; reanalyzed public datasets: HECA (Marečková 2024, Garcia-Alonso 2021), Barkley 2022 EEC Visium, ovarian scRNA-seq (Wagner et al.). Atlas at https://www.sccellfie.org"

# === Cross-references ===
code_url: "https://github.com/earmingol/scCellFie"
cited_by: []
---

## Problem

Cellular metabolism shapes identity, communication, and disease, but methods to measure it at single-cell or spatial resolution remain technically inaccessible to most labs. Single-cell and spatial transcriptomics are ubiquitous, yet existing transcriptomics-based metabolic-inference tools are either bulk-only (CellFie), too slow for atlas scale (FBA variants like Compass), or opaque (deep-learning fluxes like scFEA). There is no scalable, biochemically interpretable framework that exploits genome-scale metabolic models, gene-protein-reaction (GPR) enzyme logic, and per-cell or per-spot resolution simultaneously — and there is no atlas-scale resource mapping metabolic activities across human cell types and organs in a queryable form.

## Key idea

The authors present **scCellFie**, a computational framework that extends the CellFie metabolic-task formalism to single-cell and spatial transcriptomics by combining (a) CELLxGENE-derived per-gene expression thresholds, (b) GPR-rule evaluation (min over enzyme-complex subunits, max over isoenzymes) over [[genome-scale-metabolic-model]] reconstructions (Human1, Mouse1), and (c) weighted task-level aggregation that adjusts for reactions shared across tasks. Applied to ~30M cells in the [[czi-cellxgene-atlas]] (April 2024 snapshot), it produces a queryable web atlas of metabolic-task activities across 2,195 cell-type × organ combinations (https://www.sccellfie.org). Domain applications in the human endometrium recover known cycle-dependent epithelial and stromal programs, identify kynurenine–AHR signaling and MVA-pathway activity as central to epithelial physiology, and nominate disease-specific metabolic axes in endometriosis (uM1 macrophage NF-κB signaling via inositol-trisphosphate; methylglyoxal production; epithelial glycolysis-lactate-arachidonate co-upregulation) and endometrial carcinoma (spatially organized glucose→lactate, MVA marker in malignant regions, local androgen→estrogen conversion with ESR1 co-localization, and kynurenine→AHR axis correlated with a tumorigenesis signature).

## Method

**Framework (Fig 1).** Three-step inference: (1) gene expression → gene scores using precomputed thresholds calibrated against the CELLxGENE atlas; (2) gene scores → reaction activities via GPR rules (AND/min for complex subunits, OR/max for isoenzymes); (3) reaction activities → task scores aggregated and weighted to downweight reactions shared by multiple tasks. Optional KNN-based smoothing $X' = (1-\alpha) X + \alpha (S X)$ handles sparsity; chunked execution scales to millions of cells. Integrates natively with [[scanpy]].

**Database.** 218 human and 203 mouse tasks built on Human1/Mouse1 GEMs, covering seven core metabolic functions plus five secretion-related functions, plus newly added sex-hormone biosynthesis tasks (testosterone, progesterone, estradiol, estrone, estrone-sulfate, etc.) and tasks for tyrosine→melanin and GABA synthesis. Authors manually corrected reaction mappings and removed redundancies.

**Analysis modules.** (a) Metabolic-marker detection (cell-type / region-specific tasks via TF-IDF). (b) Differential metabolic activity (Wilcoxon rank-sum + Cohen's D + FDR). (c) Temporal trajectory analysis via generalized additive models (GAMs). (d) Spatial autocorrelation via Moran's I. (e) Metabolite-mediated cell-cell communication: ligand = task-level metabolite-biosynthesis score in sender; receptor = receptor gene expression in receiver; either cell-type-level or neighborhood-spatial.

**Data.** ~30M cells from CZI CELLxGENE (April 2024 snapshot, 668 datasets); HECA scRNA-seq for endometrium (Marečková 2024, Garcia-Alonso 2021); ovarian scRNA-seq for hormone-task validation; endometrial-organoid scRNA-seq; Visium of mid-secretory endometrium (Garcia-Alonso 2021); newly generated Visium of two donors' peritoneal endometriotic lesions; published EEC Visium (Barkley 2022). cell2location ([[cell2location-deconvolution]]) used for spot-level cell-type deconvolution.

## Results

- **Validation of new hormone-biosynthesis tasks (Fig 2).** Androgenic theca cells score highest for cholesterol→progesterone and androstenedione tasks; granulosa cells highest for androstenedione→E1 and E2 tasks; immune cells unexpectedly high for estrone→estrone-sulfate (suggesting an immune-cell role in estrogen homeostasis via sulfation).

- **CELLxGENE atlas of metabolic activities (Fig 3).** Recapitulates known organ-specific biology — glutathione in lens fiber cells, starch degradation in pancreatic acinar cells, adrenaline in adrenal chromaffin / sympathetic neurons, taurocholate in hepatocytes — across 2,195 cell-type × organ combinations. Browsable at https://www.sccellfie.org.

- **Healthy endometrial cell-type markers (Fig 4).** Epithelial cells: PAPS synthesis (sulfation substrate), local estrogen inactivation (estrone→estrone-sulfate, pre-luminal in early secretory), MVA synthesis (highest in luminal), thromboxane synthesis (luminal — hemostasis). Stromal cells: phenylalanine→phenylacetate, calnexin/calreticulin cycle (decidualization, uterine receptivity). Kynurenine→AHR CCC strong between epithelial subtypes in HECA, co-localizes in glands and lumen on Visium.

- **Menstrual-cycle metabolic dynamics (Fig 5).** GAM analysis identifies 14 cycle-dependent tasks in glandular epithelium (peak ATP-glycolysis and glucose→lactate at proliferative→secretory transition; secretory-phase upregulation of kynurenine, NAD-salvage, phenylalanine metabolism). Only 4 cycle-dependent tasks in luminal epithelium, all overlapping with glandular. Stromal-cell dominant change: phenylalanine→phenylacetate at decidualization (MAOA/MAOB as determinant genes). Organoid–in-vivo comparison: most cycle-dependent patterns reproduce; nucleotide salvage and Tn-antigen glycosylation diverge (GALNT4, APRT, HPRT1 flagged).

- **Endometriosis dysregulation (Fig 6).** Macrophages are the only immune cells with significant metabolic dysregulation; uM1 macrophages elevate myo-inositol-bisphosphate→trisphosphate (PLC → NF-κB) and methylglyoxal production. Epithelial cells upregulate malonyl-CoA / lipid synthesis, glucose→lactate, arachidonate (prostaglandin precursor); stromal cells downregulate kynurenine and NAD-salvage. Visium of two peritoneal endometriotic-lesion donors shows preserved M1 macrophages and luminal epithelial cells; mevalonate synthesis, HMP shunt, and phenylalanine conversion active in lesion regions.

- **Endometrial carcinoma (Fig 7).** Glucose→lactate spatially organized (Moran's I = 0.379), enriched in malignant regions. MVA synthesis marks malignant-cell spots. Cholesterol→sex-hormone biosynthesis not detected in malignant regions, but androgen→estrogen intermediate is, with estradiol-biosynthesis and ESR1 receptor significantly co-localized in malignant regions. N-formylanthranilate (tryptophan→kynurenine pathway) shows the highest correlation with an EEC tumorigenesis signature (S100A9, S100A8, LCN2, CTS1, LTF, CXCL1, SAA1, SAA2); L-kynurenine→AHR CCC significantly elevated in malignant regions.

## All claims (exhaustive)

- `[c01]` scCellFie infers metabolic-task activities at single-cell and spatial resolution via GPR rules over GEMs, scaling to ~30M cells (Methods + Fig 1) "scCellFie enables single-cell resolution through improvements on optimizing mathematical operations for analysis speed-up and smoothing gene expression to handle data sparsity" — confidence: high — type: methodological — links: [[concepts/sccellfie-metabolic-task-inference]] [[foundations/metabolic-task-cellfie]] [[foundations/genome-scale-metabolic-model]] [[claims/sccellfie-scales-metabolic-task-inference-to-single-cell-and-spatial]]
- `[c02]` Applied to the [[czi-cellxgene-atlas]], scCellFie produces an atlas of 2,195 cell-type × organ metabolic-activity combinations that recovers known organ-specific biology (lens-glutathione, pancreas-starch, adrenal-adrenaline, hepatocyte-taurocholate) (Fig 3c-d) "These examples recapitulating known biology demonstrate scCellFie's utility for identifying organ- and cell-specific metabolic functions across large-scale atlases" — confidence: medium — type: quantitative — links: [[foundations/czi-cellxgene-atlas]] [[claims/cellxgene-atlas-recovers-organ-and-cell-type-specific-metabolic-functions]]
- `[c03]` MVA synthesis is a marker task of endometrial epithelial cells (highest in luminal cells, early secretory phase) and is preserved as a marker of malignant cells in EEC and of luminal-epithelial regions in peritoneal endometriotic lesions (Fig 4c, 6f, 7d) "we now extend its relevance to malignant cells in endometrial carcinoma" — confidence: medium — type: correlational — links: [[concepts/endometrial-metabolic-reprogramming-cycle-disease]] [[foundations/hmg-coa-reductase]] [[claims/mva-pathway-shared-marker-endometrial-epithelium-and-malignant-eec-cells]]
- `[c04]` The tryptophan→kynurenine→AHR axis is active in healthy endometrial epithelium and significantly elevated in malignant EEC regions, with N-formylanthranilate showing the highest correlation with an EEC tumorigenesis signature (Fig 4c,f,g; Fig 7g,h) "synthesis of N-formylanthranilate from tryptophan strongly correlated with tumorigenesis potential" — confidence: medium — type: correlational — links: [[concepts/tryptophan-ido1-kynurenine-immunosuppression]] [[foundations/ahr-ido1-tryptophan-axis]] [[concepts/endometrial-metabolic-reprogramming-cycle-disease]] [[claims/kynurenine-ahr-axis-active-endometrial-epithelium-and-elevated-in-eec]]
- `[c05]` In endometriosis, uM1 macrophages specifically elevate myo-inositol-bisphosphate→trisphosphate conversion (via PLC isoforms → NF-κB) and methylglyoxal production, consistent with their proinflammatory phenotype (Fig 6a,c) "This process activates NF-κB signaling, which plays a key role in inflammation" — confidence: medium — type: mechanistic — links: [[concepts/endometrial-metabolic-reprogramming-cycle-disease]] [[claims/um1-macrophages-elevated-inositol-trisphosphate-and-methylglyoxal-endometriosis]]
- `[c06]` EEC malignant regions show inferred androgen→estrogen intermediate activity and significant co-localization of estradiol biosynthesis with ESR1 receptor expression, supporting a local intra-tumoral estrogen-signaling axis (Fig 7e; Supp Fig 9b-d) "our results suggest that this may be the case in endometrial carcinoma" — confidence: low-medium — type: mechanistic — links: [[concepts/endometrial-metabolic-reprogramming-cycle-disease]] [[claims/local-androgen-to-estrogen-conversion-in-endometrial-carcinoma-tumor-microenvironment]]
- `[c07]` Glucose→lactate conversion is spatially organized in EEC tissue (Moran's I = 0.379) with significantly higher activity in malignant-cell regions, recapitulating the Warburg effect at spatial resolution (Fig 7c; Supp Fig 8a) "lactate production is a fundamental feature of cancer metabolism" — confidence: high — type: quantitative — links: [[concepts/warburg-effect-hif1a-glycolytic-reprogramming]] [[foundations/10x-visium-spatial-transcriptomics]] [[claims/glucose-to-lactate-spatially-organized-malignant-regions-endometrial-carcinoma]]
- `[c08]` Hormone-stimulated epithelial endometrial organoids reproduce most in-vivo cycle-dependent metabolic patterns but diverge in nucleotide salvage and Tn-antigen glycosylation (driver genes: GALNT4, APRT, HPRT1), nominating targets for organoid-protocol refinement (Fig 5f) "we identified specific discrepancies that could inform organoid optimization" — confidence: medium — type: methodological — links: [[concepts/endometrial-metabolic-reprogramming-cycle-disease]] [[claims/endometrial-organoids-replicate-most-cycle-metabolic-patterns-with-specific-gaps]]

## Discussion captured

### Authors' interpretation

The authors interpret scCellFie as a comprehensive, customizable, scalable framework that fills a methodological gap between bulk-only CellFie, slow FBA-based methods (Compass), and opaque deep-learning fluxes (scFEA). They argue its biochemical interpretability via GPR rules — explicitly modelling enzyme complexes and isoenzymes — combined with metabolite-CCC and spatial analyses, distinguishes it from gene-set-enrichment alternatives. For endometrium, they interpret MVA and kynurenine pathways as supporting proliferation and oxidative-stress mitigation respectively; phenylalanine→phenylacetate and calnexin/calreticulin cycle as supporting stromal decidualization and uterine receptivity; in disease, lactate/lipid/arachidonate upregulation as drivers of atypical proliferation and proinflammatory phenotypes in endometriosis, and kynurenine-AHR, MVA, and local estrogen synthesis as candidate therapeutic axes in EEC.

### Comparisons with prior literature (made by authors)

- Cites CellFie (Richelle 2021) as the bulk-resolution antecedent of metabolic-task inference.
- Cites Compass (FBA-based) and scFEA (deep learning) as comparators with complementary trade-offs.
- Cites Marečková 2024 for the prior observation of uM1 macrophage imbalance in endometriosis (which the new metabolic findings extend).
- Cites Barkley 2022 for the EEC Visium dataset reanalyzed.
- Cites human metabolic atlases (refs 48, 110) as bulk-only or limited cell-type predecessors that scCellFie's atlas extends.

### Mechanistic hypotheses proposed

- "this metabolic activity may be central in regulating this amino acid's abundance after ovulation and preparing the tissue for a potential implantation" (phenylalanine→phenylacetate in decidualizing stroma, p. 16) — mechanistic.
- "our results suggest that this may be the case in endometrial carcinoma" — local androgen→estrogen conversion supplies EEC tumors with estrogen independent of systemic obesity-driven supply (p. 21–22).
- "kynurenine-AHR signaling may support endometrial epithelial cells to manage the inflammation and oxidative stress during tissue remodeling" (p. 13).

### Caveats and self-criticism

- "scCellFie … assumes that gene expression levels closely reflect metabolic activity, which may not always occur due to differences between mRNA and protein abundances, or post-transcriptional regulation and enzyme kinetics" (Limitations, p. 26).
- "dependency on the metabolic tasks defined in the database, which may miss other important functions or incorrectly predict activities due to misannotations" (Limitations, p. 26).
- "their divergent behavior may also reflect challenges in replicating temporal transitions in organoid models" (organoid-divergence caveat, p. 17).

### Future directions suggested

- Use proteomics-driven thresholds for higher-confidence metabolic-activity inference.
- Community-driven additions of new metabolic tasks and technology-specific thresholds.
- Integrate with metabolomics for orthogonal validation.
- Add network-visualization and additional analysis modules.

## Limitations

- Transcriptomic proxy: mRNA abundance is an imperfect proxy for enzyme activity; post-translational regulation, enzyme kinetics, and metabolite concentrations are not modeled.
- Bounded by GEM completeness and the curated metabolic-task list (218 human, 203 mouse).
- CELLxGENE-derived thresholds may need recalibration for non-10x Chromium or snRNA-seq data.
- No paired metabolomics validation in any dataset shown.
- EEC analysis based on a single Visium dataset (Barkley 2022); endometriotic-lesion Visium limited to two donors.
- Organoid-vs-in-vivo divergences cannot disambiguate organoid-specific gaps from generic temporal-transition modeling limits.

## Open questions

### Open questions raised by authors

- How can metabolomics best be integrated with scCellFie inference at single-cell or spatial resolution?
- Can technology-specific thresholds (community-contributed) improve out-of-distribution inference?
- What is the role of the immune-cell estrogen-sulfation activity unexpectedly identified in ovarian scRNA-seq?

### Open questions identified during ingest

- Pharmacological validation of MVA inhibitors (statins) in EEC organoid/PDX models.
- Whether AHR antagonism or IDO1 inhibition alters EEC progression in vivo.
- Whether glyoxalase or PLC inhibition normalizes uM1 inflammatory phenotype in endometriosis donor biopsies.
- Cross-cohort replication of the kynurenine–EEC tumorigenesis correlation.
- Calibration of scCellFie task scores vs. paired single-cell metabolomics (SCoPE-MS / NanoSIMS, etc.).

## My take

A methodologically solid bridge between genome-scale metabolic modeling and modern single-cell/spatial atlases. The framework's most valuable contribution is making metabolic-task scoring tractable at CELLxGENE scale while preserving GPR-rule biochemical interpretability — that combination did not exist before. The endometrial biology serves as proof-of-concept rather than definitive disease biology: most of the EEC and endometriosis findings are inference-only on single Visium datasets and warrant orthogonal validation. The kynurenine–AHR axis in EEC and the uM1 methylglyoxal axis in endometriosis are the most novel testable hypotheses; the MVA marker claim in EEC is the most therapeutically actionable; the local androgen→estrogen claim is the most controversial and needs strongest validation. As a bioRxiv preprint (May 2025) the work is not peer-reviewed; importance set to 3 reflects strong methodological novelty and atlas resource value pending peer review and downstream uptake.

## Related

- [[sccellfie-metabolic-task-inference]] — framework concept page.
- [[endometrial-metabolic-reprogramming-cycle-disease]] — endometrial biology concept page.
- [[metabolic-task-cellfie]] — foundational task definition.
- [[genome-scale-metabolic-model]] — Human1/Mouse1 reconstructions.
- [[czi-cellxgene-atlas]] — substrate atlas.
- [[10x-visium-spatial-transcriptomics]] — spatial platform used.
- [[cell2location-deconvolution]] — spot deconvolution method.
- [[scanpy]] — integration backbone.
- [[ahr-ido1-tryptophan-axis]] — kynurenine-AHR foundation literature.
- [[hmg-coa-reductase]] — MVA-pathway rate-limiting enzyme.
- [[warburg-effect-hif1a-glycolytic-reprogramming]] — glucose-to-lactate cancer-metabolism context.
- [[tryptophan-ido1-kynurenine-immunosuppression]] — kynurenine-pathway immuno-oncology context.
- [[erick-armingol]] · [[roser-vento-tormo]] · [[nathan-e-lewis]] — authors.
