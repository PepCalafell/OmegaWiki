---
title: "Benchmarking atlas-level data integration in single-cell genomics"
slug: benchmarking-atlas-level-data-integration-single
arxiv: ""
doi: "10.1038/s41592-021-01336-8"
pmid: "34949812"
venue: "Nature Methods"
year: 2022
authors:
  - "Malte D. Luecken"
  - "Maren Büttner"
  - "Kridsadakorn Chaichoompu"
  - "Anna Danese"
  - "Marta Interlandi"
  - "Michaela F. Mueller"
  - "Daniel C. Strobl"
  - "Luke Zappia"
  - "Martin Dugas"
  - "Maria Colomé-Tatché"
  - "Fabian J. Theis"
first_author: "Malte D. Luecken"
corresponding_author: "Maria Colomé-Tatché; Fabian J. Theis"
source_type: pdf
s2_id: "d88158745b69f5732397175389101e2d98799c00"
date_added: 2026-05-22
ingested_date: 2026-05-22
ingest_version: 1
last_reviewed:
importance: 5
tier: TIER_1
tags:
  - benchmarking
  - data-integration
  - single-cell
  - scRNA-seq
  - scATAC-seq
  - batch-correction
  - methods
  - atlas
  - HCA
keywords:
  - scIB
  - data integration
  - batch effect
  - scRNA-seq integration
  - scATAC-seq integration
  - Harmony
  - scVI
  - scANVI
  - Scanorama
  - scGen
  - BBKNN
  - LIGER
  - Conos
  - MNN
  - FastMNN
  - Seurat v3
  - ComBat
  - trVAE
  - DESC
  - SAUCIE
  - kBET
  - LISI
  - ASW
  - silhouette
  - NMI
  - ARI
  - HVG
  - Snakemake
  - benchmarking
  - reference atlas
  - Human Cell Atlas
domain: methods
tissue:
  - multi
  - blood
  - bone_marrow
  - lung
  - pancreas
  - brain
condition:
  - healthy
disease_specific: []
species:
  - human
  - mouse
hypoxia_relevant: false
contains_immune_cells: true
contains_myeloid: false
techniques:
  - scRNA-seq_10x
  - scRNA-seq_Smart-seq2
  - snRNA-seq
  - scATAC-seq
  - simulation
  - Snakemake_pipeline
n_samples: 85
n_cells_total: 1200000
integration_method: ""
key_cell_types:
  - CD4_T_cells
  - CD8_T_cells
  - CD14_monocytes
  - CD16_monocytes
  - B_cells
  - NK_cells
  - erythrocytes
  - HSPCs
  - megakaryocyte_progenitors
  - plasmacytoid_dendritic_cells
key_markers: []
key_pathways: []
projects:
  - thesis
  - methods
priority: core
read_status: skimmed
hypoxiaverse_status:
exclusion_reason:
data_availability: "scIB Python module + Snakemake pipeline; 23 published datasets re-curated. Website: https://theislab.github.io/scib-reproducibility"
code_url: "https://github.com/theislab/scib ; https://github.com/theislab/scib-pipeline"
cited_by:
  - interpretable-inflammation-landscape-circulating-immune-cells
---

## Problem

Single-cell atlases (Human Cell Atlas, Tabula Muris) combine samples across donors, laboratories, protocols, tissues and species, producing complex nested batch effects that linear batch-removal methods (ComBat, simple Harmony) cannot adequately resolve while preserving biological variation. As of 2020, ≥49 scRNA-seq integration tools existed but no benchmark had compared them on atlas-level complexity using objective, varied metrics. Prior benchmarks (Tran 2020, Chazarra-Gil 2021) used simpler tasks, evaluated single output types, and concluded that linear methods like Harmony / ComBat suffice — guidance that does not generalise to atlas data.

## Key idea

Build a benchmark (**scIB** — single-cell Integration Benchmark) of 16 integration methods × up to 4 preprocessing combinations × 13 atlas-scale integration tasks (5 scRNA-seq, 6 scATAC-seq, 2 simulation; up to 1M cells, 23 batches), evaluated by 14 metrics in two families (batch effect removal vs biological-variance conservation) with a 40/60 weighted aggregate score. Critically, (a) introduce graph-extensions of kBET and LISI so the same metric works on graph / embedding / gene-matrix outputs; (b) add three label-free bio-conservation metrics (cell-cycle conservation, HVG conservation, trajectory conservation) that previous benchmarks lacked; (c) deliver the result as a reusable, reproducible scIB Python module and Snakemake pipeline. Operationalise the tradeoff between batch removal and bio-conservation as the central design axis of integration-method selection.

## Method

- **Methods benchmarked (16)**: MNN, FastMNN, Seurat v3 (CCA and RPCA), scVI, scANVI, Scanorama, BBKNN, LIGER, Conos, SAUCIE, Harmony, ComBat, DESC, trVAE, scGen.
- **Tasks (13)**: pancreas (9 batches, 16k cells), lung (16 donors, 32k), human immune (10 donors, 33k), human+mouse immune (23 samples, 98k), mouse brain RNA (4 datasets, 979k cells), mouse brain scATAC small + large × {peaks, windows, gene activity} (6 tasks), 2 simulations.
- **Preprocessing decisions**: HVG (yes/no) × scaling (yes/no), where applicable. Up to 68 setups per task; 590 attempted runs total.
- **Batch-removal metrics (5)**: kBET (extended to graph), graph iLISI (extension of iLISI), batch ASW, kNN graph connectivity, PCA regression.
- **Label-conservation metrics (5)**: NMI, ARI, cell-type ASW, isolated label F1, isolated label silhouette, graph cLISI.
- **Label-free bio-conservation metrics (3 NEW)**: cell-cycle variance conservation, HVG overlap conservation, trajectory conservation (diffusion-map-based).
- **Aggregate score**: weighted 40% batch / 60% bio-conservation; method-best preprocessing reported on each task.
- **Output handling**: methods producing multiple outputs (genes, embeddings, graph) are evaluated as separate runs.
- **Scalability**: peak memory and CPU runtime under Snakemake; cap 4 days per run.
- **Usability**: scored on documentation, tutorials, GitHub activity, robustness publications — criteria adapted from Saelens 2019 trajectory benchmark.

## Results

- **Overall best on RNA tasks**: scANVI, Scanorama, scVI, scGen — top four — see [[claims/scanvi-scanorama-scvi-top-rna-integration]].
- **Cell-label methods (scGen, scANVI) win when labels available** — see [[claims/cell-label-integration-methods-win-with-labels]].
- **Batch-removal vs bio-conservation tradeoff is the central design axis** — see [[claims/batch-removal-vs-bioconservation-tradeoff]] and [[concepts/batch-removal-vs-bioconservation-tradeoff]].
- **HVG selection improves integration** (74% of comparisons higher overall, 81% better batch removal, 66% better bio-conservation) — see [[claims/hvg-selection-improves-integration]].
- **Scaling shifts toward batch removal at cost of bio-conservation** (79% / 72% of comparisons respectively) — see [[claims/scaling-shifts-integration-to-batch-removal]].
- **scATAC-seq: only LIGER and Harmony consistently integrate batches** (peaks/windows space) — see [[claims/liger-harmony-best-scatac-integration]].
- **scATAC feature space matters: peaks/windows > gene activity** — see [[claims/scatac-peaks-windows-beat-gene-activity]] and [[concepts/scatac-feature-space-tradeoff]].
- **Only 27% of scATAC integration outputs beat unintegrated baseline** (vs 85% on RNA) — see [[claims/most-scatac-methods-worsen-data]].
- **Harmony best for simple tasks, weaker on complex** — see [[claims/harmony-simple-tasks-only]].
- **MNN-based methods (Scanorama, FastMNN) consistently strong on RNA** — see [[claims/mnn-anchor-methods-strong-rna]].
- **Embedding outputs tend to outperform gene-corrected outputs at the same method** — see [[claims/embedding-outputs-outperform-gene-corrected]].
- **scVI scales without runtime growth thanks to epoch heuristic; trVAE / scGen / Seurat v3 / MNN fail to scale** — see [[claims/scvi-scales-trvae-scgen-fail]].
- **Strongest batch effect contributors: species > nuclei-vs-cell > spatial location > inter-platform** — see [[claims/strongest-batch-effects-species-nuclei]].
- **ComBat / BBKNN / SAUCIE are fastest; scVI / scANVI / BBKNN most memory-efficient** — see [[claims/combat-bbknn-fastest-scvi-low-memory]].
- **The scIB pipeline becomes a reproducible reference resource for scRNA-seq integration** — see [[claims/scib-pipeline-reproducible-benchmark-resource]].

## All claims (exhaustive)

- `[c01]` Scanorama, scANVI and scVI are the top-3 RNA integration methods on real atlas tasks, with scGen's gene-corrected output ranked first most often but failing to scale to 1M-cell mouse brain (p.45) "Overall, the embeddings output by Scanorama, scANVI and scVI perform best… scGen was ranked first most frequently, but it was penalized for not running on the 1 million mouse brain task in 4 days on a CPU" — confidence: high — type: methodological — links: [[foundations/scanvi-semi-supervised]] [[foundations/scvi-deep-generative-model]] [[foundations/scanorama-integration]] [[foundations/scgen-perturbation-integration]] [[claims/scanvi-scanorama-scvi-top-rna-integration]]
- `[c02]` Methods that consume cell identity labels (scGen, scANVI) perform well across tasks and are the only ones that retain cell-state differences present in only a single batch (p.44) "Methods that use cell identity information (scGen and scANVI)… scGen and scANVI are the only methods that are able to preserve cell state differences that are each present only in a single batch" — confidence: high — type: methodological — links: [[foundations/scgen-perturbation-integration]] [[foundations/scanvi-semi-supervised]] [[concepts/batch-removal-vs-bioconservation-tradeoff]] [[claims/cell-label-integration-methods-win-with-labels]]
- `[c03]` Across integration methods and tasks, there is a consistent tradeoff between batch-effect removal and biological-variance conservation: SAUCIE/LIGER/BBKNN/Seurat v3 favor batch removal; DESC/Conos favor bio-conservation; Scanorama/scVI/FastMNN balance both (p.43-44) "Particularly in more complex integration tasks, we observed a tradeoff between batch effect removal and bio-conservation… While methods such as SAUCIE, LIGER, BBKNN and Seurat v3 tend to favor the removal of batch effects… DESC and Conos make the opposite choice, and Scanorama, scVI and FastMNN (gene) balance these two objectives" — confidence: high — type: mechanistic — links: [[concepts/batch-removal-vs-bioconservation-tradeoff]] [[claims/batch-removal-vs-bioconservation-tradeoff]]
- `[c04]` HVG selection improves integration performance over full feature input: 74% of paired comparisons higher overall, 81% better batch removal, 66% better bio-conservation; trajectory and cell-cycle conservation are the exceptions favoring full features (p.45) "for HVGs, 74% of comparisons had a higher overall score; 81% had better batch removal and 66% had better bio-conservation scores. Notable exceptions were trajectory and cell-cycle conservation scores" — confidence: high — type: quantitative — links: [[foundations/hvg-selection-scrna]] [[claims/hvg-selection-improves-integration]]
- `[c05]` Scaling the input data systematically shifts integration toward batch removal at the cost of bio-conservation (79% of comparisons higher batch removal; 72% lower bio-conservation) (p.45) "Independent of the method, scaling resulted in higher batch removal scores (79% of comparisons) but lower bio-conservation (72% of comparisons)" — confidence: high — type: quantitative — links: [[concepts/batch-removal-vs-bioconservation-tradeoff]] [[claims/scaling-shifts-integration-to-batch-removal]]
- `[c06]` On scATAC-seq, only LIGER and Harmony — methods that prioritize batch removal — consistently integrate batches in peak / window feature space; most other methods fail (p.46-47) "LIGER and Harmony, which focus on batch removal over bio-conservation… fully merged batches within cell-type clusters. This trend could also be seen on the large ATAC peak and window tasks" — confidence: high — type: methodological — links: [[foundations/liger-nmf-integration]] [[foundations/harmony-integration]] [[foundations/atac-seq]] [[claims/liger-harmony-best-scatac-integration]]
- `[c07]` In scATAC-seq, peaks and windows feature spaces preserve more cell-type variation than gene-activity features; mean bio-conservation 0.61 (peaks) / 0.59 (windows) vs 0.39 (gene activity) (p.46) "mean bio-conservation score for integration outputs on gene activity space is substantially lower than on peaks and windows (genes 0.39; peaks 0.61; windows 0.59)" — confidence: high — type: quantitative — links: [[concepts/scatac-feature-space-tradeoff]] [[foundations/atac-seq]] [[claims/scatac-peaks-windows-beat-gene-activity]]
- `[c08]` Only 27% of scATAC integration outputs (on peaks) beat the best unintegrated baseline, compared to 85% on RNA — many methods actively degrade the data (p.46) "only 27% of integration outputs performed better than the best unintegrated result (on peaks)… compared to 85% on RNA tasks" — confidence: high — type: quantitative — links: [[concepts/scatac-feature-space-tradeoff]] [[claims/most-scatac-methods-worsen-data]]
- `[c09]` Harmony performs well on simple RNA integration tasks and simulations but ranks outside the top third on complex real-data tasks (p.45, p.48) "Harmony ranked outside the top third of methods for more complex real data tasks, but was favorable for simulations and real data with less complex biological variation… the use of Harmony is appropriate for simple integration tasks with distinct batch and biological structure" — confidence: high — type: methodological — links: [[foundations/harmony-integration]] [[claims/harmony-simple-tasks-only]]
- `[c10]` MNN-based / anchor-based methods (Scanorama, FastMNN) consistently perform well on complex RNA integration tasks, suggesting MNN-anchor matching is a strong general inductive bias (p.45) "methods based on mutual nearest neighbors to find anchors between batches (for example, Scanorama and FastMNN) tended to perform well" — confidence: high — type: mechanistic — links: [[foundations/mnn-fastmnn-integration]] [[foundations/scanorama-integration]] [[claims/mnn-anchor-methods-strong-rna]]
- `[c11]` Higher-abstraction outputs (embeddings) tend to outperform gene-corrected matrix outputs of the same method (e.g. Scanorama embedding > Scanorama gene, FastMNN embedding > FastMNN gene) (p.45) "The methods with a higher level of abstraction tended to rank higher (in particular comparing Scanorama and FastMNN's embeddings and corrected expression matrix output)" — confidence: high — type: methodological — links: [[claims/embedding-outputs-outperform-gene-corrected]] [[foundations/scanorama-integration]] [[foundations/mnn-fastmnn-integration]]
- `[c12]` scVI's runtime is independent of dataset size thanks to a training-epoch heuristic that scales epochs inversely with cell count; in contrast, trVAE fails above 34k cells without GPU and Seurat v3 / MNN / scGen fail above 100k cells under CPU resource caps (p.46) "scVI and scANVI did not increase with the dataset size due to a heuristic that was suggested to scale training epochs with the number of data points… trVAE could not integrate datasets with >34,000 cells, while Seurat v3, MNN and scGen failed to integrate datasets with >100,000 cells" — confidence: high — type: quantitative — links: [[foundations/scvi-deep-generative-model]] [[foundations/scanvi-semi-supervised]] [[foundations/trvae-conditional-vae]] [[foundations/scgen-perturbation-integration]] [[claims/scvi-scales-trvae-scgen-fail]]
- `[c13]` Strongest batch-effect contributors ranked by integration difficulty: inter-species > nuclei-vs-cell > inter-tissue / inter-platform > inter-patient > replicate; species and modality often blur the batch / biology boundary (p.48-49, Fig 5b) "The most challenging batch effects across the integration tasks were due to species, sampling locations and single-nucleus versus single-cell data. These batch effect contributors can also be interpreted as biological signals rather than technical noise" — confidence: medium — type: correlational — links: [[concepts/batch-removal-vs-bioconservation-tradeoff]] [[claims/strongest-batch-effects-species-nuclei]]
- `[c14]` ComBat, BBKNN and SAUCIE have the fastest CPU runtimes; scVI, scANVI and BBKNN are the most memory-efficient (p.46) "ComBat, BBKNN and SAUCIE performed best in terms of runtime and scVI, scANVI and BBKNN are the most memory efficient" — confidence: high — type: quantitative — links: [[foundations/combat-batch-correction]] [[foundations/bbknn-integration]] [[foundations/scvi-deep-generative-model]] [[claims/combat-bbknn-fastest-scvi-low-memory]]
- `[c15]` The 40/60 batch/bio-conservation aggregate ranking is robust to alternative aggregation schemes: Spearman rank correlation > 0.96 across tasks compared to alternative aggregations from Saelens 2019 (p.48) "Our metric aggregation approach follows best practices for robust ranking in machine learning tasks and indeed produced consistent overall rankings when compared to alternatives (overall rank correlation, Spearman's R > 0.96 for all tasks)" — confidence: high — type: methodological — links: [[foundations/scib-benchmark-pipeline]] [[claims/scib-pipeline-reproducible-benchmark-resource]]
- `[c16]` The scIB Python module + Snakemake pipeline becomes a reproducible reference resource for scRNA-seq integration method evaluation and atlas-construction workflows (p.49) "the reproducible scIB-pipeline Snakemake pipeline and the scIB python module for users to easily benchmark their particular integration scenario… this work will become a reference for method developers" — confidence: high — type: methodological — links: [[foundations/scib-benchmark-pipeline]] [[foundations/snakemake-workflow]] [[claims/scib-pipeline-reproducible-benchmark-resource]]
- `[c17]` Three new label-free bio-conservation metrics — cell-cycle conservation, HVG overlap conservation and trajectory conservation — capture biological variation beyond cell-type labels, with Scanorama gene / ComBat / MNN best at HVG and cell-cycle conservation and Scanorama / scGen / FastMNN best at trajectory conservation (p.43-44) "Methods that favor bio-conservation and output corrected expression matrices tended to better conserve cell state variation. Indeed, Scanorama (gene), ComBat and MNN consistently performed well at conserving cell-cycle variance and HVGs in the integrated data. Trajectory structure was slightly better conserved in the overall high-performing methods Scanorama, scGen and FastMNN" — confidence: high — type: methodological — links: [[concepts/label-free-bio-conservation-metrics]] [[foundations/scanorama-integration]] [[claims/label-free-metrics-capture-trajectories-cellcycle]]
- `[c18]` Linear / classical methods (Harmony, ComBat) outperformed more complex nonlinear methods in earlier benchmarks (Tran 2020, Chazarra-Gil 2021); this paper reverses that finding on atlas-complexity tasks where nonlinear deep-learning methods (scVI, scANVI) dominate (p.41) "Previous studies on benchmarking methods for data integration… finding that ComBat or the linear, principal component analysis (PCA)-based, Harmony method outperformed more complex, nonlinear, methods… on more complex integration tasks, Scanorama (embeddings) and scVI worked well" — confidence: high — type: methodological — links: [[concepts/atlas-level-data-integration]] [[claims/atlas-complexity-favors-deep-learning-integration]]

## Discussion captured

### Authors' interpretation

Method choice for scRNA-seq integration should follow three axes: usability (output type, language, documentation), scalability (cells, features, GPU), and expected performance (batch-effect strength, need for nuanced cell states, batch/biology confounding, trajectories, compositional shifts). Authors recommend scANVI/scGen when labels exist; Scanorama or scVI when labels do not and the task is complex; Harmony or BBKNN/Seurat v3 for small or simple tasks. On scATAC-seq, authors recommend LIGER or Harmony on peaks/windows, and note that PCA/SVD-based dimensionality reduction may be inappropriate for binary chromatin-accessibility data.

The paper frames the batch-removal-vs-bio-conservation tradeoff as the central conceptual contribution, not just an empirical observation, and proposes that retaining batch effects may sometimes be preferable to removing them when batch and biology are confounded (e.g. spatial location, species).

### Comparisons with prior literature (made by authors)

- Tran et al. 2020 (Genome Biology) and Chazarra-Gil et al. 2021 (Nucleic Acids Research, BatchBench) concluded that ComBat / Harmony win — but only on simpler tasks; this study contradicts that conclusion on atlas-scale tasks.
- Saelens et al. 2019 trajectory-inference benchmark is cited as the methodological precedent for ranking-aggregation robustness checks and for usability scoring.
- Maier-Hein et al. 2018 Nature Communications is cited for "why rankings should be interpreted with care."
- Büttner et al. 2019 (kBET, Nature Methods) is the prior work the authors extend to graph outputs.

### Mechanistic hypotheses proposed

- MNN-anchor matching generalises better than parametric latent-space methods on complex batch structure because anchors are local and do not assume a global batch geometry.
- Deep-learning methods (scVI, scANVI, scGen) outperform on large-cell-count tasks because they can fit nonlinear batch effects given enough data; their inferior performance on small tasks reflects underfitting / over-regularisation.
- PCA / SVD-based methods (FastMNN, Scanorama, Conos, SAUCIE) underperform on scATAC-seq because covariance fails to capture binary, sparse chromatin signal.
- Scaling removes feature-magnitude variation that is partly informative of cell-state biology, hence the shift toward batch removal at the cost of bio-conservation.

### Caveats and self-criticism

- Hyperparameters were taken from method tutorials; per-task hyperparameter optimization (not done) would likely improve every method.
- Cell-identity labels were predefined per batch by the authors; label quality affects scANVI / scGen and the bio-conservation metrics that depend on labels.
- The 40/60 batch/bio weighting is a choice that affects rankings — authors verify robustness via Spearman > 0.96 vs alternatives but acknowledge weighting is task-dependent.
- scATAC-seq integration is evaluated on only mouse brain (3 source datasets) — limited generalisability across tissues.
- Output-type heterogeneity (graph vs embedding vs gene matrix) is partly handled via separate evaluation, but cross-output-type ranking is inherently noisy.

### Future directions suggested

- Dedicated nonlinear dimensionality-reduction methods for scATAC-seq combined with MNN-anchor matching (e.g. SCALE + FastMNN-style).
- Larger-scale and GPU-native integration methods as cell counts grow.
- Statistical models that analyze raw data while accounting for batch as a covariate, rather than removing batch — particularly across aggregated datasets where current integration fails.
- Joint multimodal integration extending these benchmarks to CITE-seq, ATAC + RNA, and protein.
- Reference-mapping (Azimuth-style) projection benchmarks that build on scIB metrics.

## Limitations

- Hyperparameters not per-task optimized; results reflect tutorial-default settings.
- Cell-identity labels are author-curated per batch and therefore not gold-standard for bio-conservation metrics that depend on them.
- 40/60 batch/bio aggregate weighting is an editorial choice; alternative weightings give different ordering tails (head is robust at Spearman > 0.96).
- scATAC-seq tested only on mouse brain data; no scATAC-seq tissue diversity benchmark.
- Multimodal integration (CITE-seq, paired RNA+ATAC) excluded.
- Methods released after November 2020 are not included (the field has since produced scArches, totalVI, MultiVI, etc.).

## Open questions

### Open questions raised by authors

- How should integration methods for scATAC-seq combine nonlinear dimensionality reduction (LSI, SCALE) with MNN-anchor matching?
- Can methods that retain batch effects (statistical models with batch as a covariate) outperform integration on aggregated, very-large datasets where integration is intractable?
- For confounded batch/biology axes (species, spatial location), is removal ever desirable, or should the field develop "batch-aware analysis" instead of "batch-removal"?

### Open questions identified during ingest

- The scIB pipeline excludes reference-mapping methods (Azimuth, scArches, scANVI in reference-projection mode) — how does the benchmark generalize when integration is reformulated as projection?
- Does the 40/60 weighting transfer to cytokine-perturbation and spatial-omics atlas-construction tasks (relevant for thesis project), where the bio-conservation target is gene-program preservation rather than cell-type cluster recovery?
- Among the consistent top-3 (scANVI / Scanorama / scVI), which best preserves continuous TAM-state trajectories in TME atlases — a question this benchmark does not specifically address?
- Has the field's choice of integration default moved (post-2022) given this benchmark's recommendation — are Scanorama and scVI now the de-facto atlas defaults?

## My take

This is the foundational benchmark for atlas-level scRNA-seq integration and shapes how the Theis lab and the Human Cell Atlas community choose integration methods. Three pieces are directly load-bearing for thesis-relevant work: (i) the batch-removal vs bio-conservation tradeoff framing — when building TAM/T-cell or cytokine-perturbation atlases I should use scANVI if labels are available (preserves rare cell states), Scanorama otherwise; (ii) the warning that scaling improves batch removal but kills bio-conservation — practical relevance for any preprocessing pipeline; (iii) the scATAC-seq finding that LIGER/Harmony on peaks+windows is the only path that works — directly applicable if any TAM-spatial work pulls scATAC. The 40/60 aggregate is sensible but slightly bio-conservation-skewed for TME work where I care more about preserving rare-state biology than perfect batch erasure. The paper's central claim that nonlinear deep-learning methods reverse the Harmony/ComBat dominance on complex tasks is the canonical citation when justifying scVI/scANVI choice. Critical limitation for me: no reference-mapping benchmark and no CITE-seq, so I will need to cross-reference with the scArches / totalVI / MultiVI literature.

## Related

- [[concepts/batch-removal-vs-bioconservation-tradeoff]]
- [[concepts/atlas-level-data-integration]]
- [[concepts/scatac-feature-space-tradeoff]]
- [[concepts/label-free-bio-conservation-metrics]]
- [[concepts/scrna-atlas-as-reference-projection]]
- [[foundations/scvi-deep-generative-model]]
- [[foundations/scanvi-semi-supervised]]
- [[foundations/scanorama-integration]]
- [[foundations/harmony-integration]]
- [[foundations/bbknn-integration]]
- [[foundations/mnn-fastmnn-integration]]
- [[foundations/liger-nmf-integration]]
- [[foundations/scgen-perturbation-integration]]
- [[foundations/combat-batch-correction]]
- [[foundations/trvae-conditional-vae]]
- [[foundations/seurat-v3-integration]]
- [[foundations/scib-benchmark-pipeline]]
- [[foundations/snakemake-workflow]]
- [[foundations/kbet-batch-test]]
- [[foundations/lisi-local-inverse-simpson]]
- [[foundations/silhouette-asw-metric]]
- [[foundations/hvg-selection-scrna]]
- [[foundations/atac-seq]]
- [[people/malte-luecken]]
- [[people/maria-colome-tatche]]
- [[people/fabian-theis]]
