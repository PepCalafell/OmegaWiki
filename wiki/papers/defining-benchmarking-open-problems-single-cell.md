---
# === Identification ===
title: "Defining and benchmarking open problems in single-cell analysis"
slug: defining-benchmarking-open-problems-single-cell
arxiv: ""
doi: "10.1038/s41587-025-02694-w"
pmid: ""
venue: "Nature Biotechnology"
year: 2025
authors:
  - Malte D. Luecken
  - Scott Gigante
  - Daniel B. Burkhardt
  - Robrecht Cannoodt
  - Daniel C. Strobl
  - Nikolay S. Markov
  - Luke Zappia
  - Giovanni Palla
  - Wesley Lewis
  - Daniel Dimitrov
  - Michael E. Vinyard
  - D. S. Magruder
  - Michaela F. Mueller
  - Alma Andersson
  - Emma Dann
  - Qian Qin
  - Dominik J. Otto
  - Michal Klein
  - Olga Borisovna Botvinnik
  - Louise Deconinck
  - Kai Waldrant
  - Sai Nirmayi Yasa
  - Artur Szałata
  - Andrew Benz
  - Zhijian Li
  - Open Problems Jamboree Members
  - Jonathan M. Bloom
  - Angela Oliveira Pisco
  - Julio Saez-Rodriguez
  - Drausin Wulsin
  - Luca Pinello
  - Yvan Saeys
  - Fabian J. Theis
  - Smita Krishnaswamy
first_author: "Malte D. Luecken"
corresponding_author: "Fabian J. Theis; Smita Krishnaswamy"

# === Source & metadata ===
source_type: pdf
s2_id: ""
date_added: 2026-06-15
ingested_date: 2026-06-15
ingest_version: 1
last_reviewed:

# === Classification ===
importance: 4
tier: TIER_1
tags:
  - benchmarking
  - single-cell
  - methods-evaluation
  - reproducibility
  - cell-cell-communication
  - batch-integration
  - community-platform
keywords:
  - Open Problems
  - living benchmark
  - common task framework
  - single-cell analysis
  - method benchmarking
  - Viash
domain: methods

# === Biomedical domain ===
tissue: [multi]
condition: [healthy, cancer]
disease_specific: [triple_negative_breast_cancer]
species: [human, mouse]
hypoxia_relevant: false
contains_immune_cells: true
contains_myeloid: false

# === Technique ===
techniques: [scRNA-seq_10x, scATAC-seq, spatial_visium]
n_samples:
n_cells_total:
integration_method: ""

# === Biology captured ===
key_cell_types:
  - TNBC atlas cell types (CCC source/target)
  - mouse brain atlas cell types (CCC source/target)
key_markers:
  - TGF-β1
  - TGFβR1
  - BMP6
  - ALK2
  - IL-10
  - IL-10R
key_pathways:
  - ligand-receptor signalling

# === User project membership ===
projects: [methods]
priority: reference
read_status: not_read

# === HypoxiaVERSE-specific ===
hypoxiaverse_status:
exclusion_reason:
data_availability: "Figshare + CELLxGENE (per-task public datasets); https://openproblems.bio/datasets"

# === Cross-references ===
code_url: "https://github.com/openproblems-bio/openproblems"
cited_by: []
---

## Problem

Single-cell genomics has produced over 1,700 analysis algorithms (as of Feb 2024), but the benchmarks meant to guide method selection are fragmented and non-reproducible: independent benchmarks of the same task share <10% of datasets and metrics and recommend different winners. Bespoke, developer-run benchmarks tend to inflate the performance of the authors' own newest methods, and even neutral registered-report benchmarks age and cannot be reused or extended. The field lacks a standardized, neutral, continuously updated way to determine which method performs best in which context.

## Key idea

Replace static benchmark *papers* with a living benchmark *platform*. **Open Problems in Single-Cell Analysis** (openproblems.bio) is a community-guided, cloud-hosted platform that hosts 12 single-cell tasks (9 base + subtasks), each decomposed into datasets, methods and metrics, that are continuously re-run and re-ranked as the community contributes new components. It operationalises the common task framework for single-cell analysis: evaluation becomes reusable infrastructure rather than a publication event.

## Method

- **Architecture**: each task is a directory with subdirectories for datasets, methods, metrics and utilities. Each task needs ≥1 dataset, ≥1 metric and ≥2 baseline methods (defining performance upper/lower bounds for linear metric scaling).
- **Components**: every dataset loader, method and metric is a [[foundations/viash-component-framework]] component — a single Bash/Python/R script plus a `config.vsh.yaml` — run in a versioned Docker container for reproducibility; data are pulled from public repositories (Figshare, [[foundations/czi-cellxgene-atlas]]).
- **Contribution flow**: adding a method is a GitHub pull request following the task API; new contributions are auto-tested in the cloud and, when accepted, auto-submitted to the website.
- **Conceptual basis**: the [[foundations/common-task-framework]] (Donoho 2017) — fixed task, shared metric, neutral scoring — extended into a continuously updated form. Builds directly on the [[foundations/scib-benchmark-pipeline]] (Luecken et al. 2022) and reuses its batch-integration tasks for NeurIPS competitions.
- **Example task (CCC)**: cell–cell communication is split into a source–target subtask (spatial co-localization ground truth) and a ligand–target subtask (cytokine-activity ground truth), scored by AUPRC and odds ratio over the top 5% of predicted pairs, with mean/max aggregation of ligand–receptor scores.

## Results

- The platform launched with 9 tasks (12 with subtasks) spanning label projection, dimensionality reduction, batch integration, spatial decomposition, denoising, multimodal matching, CCC, perturbation prediction and spatially variable genes.
- CCC task: expression-magnitude scoring beats specificity scoring; max aggregation beats mean; top performers are CellPhoneDB and LIANA's magnitude ensemble; methods are reliable mainly on their top predictions.
- Best-practice findings reproduced across tasks: logistic regression beats complex batch-modeling methods for label projection (even with added noise); batch effects are easier to correct in graphs than embeddings/matrices; denoising prefers variance-stabilizing non-standard preprocessing; simple models win for perturbation prediction.
- Community reach: NeurIPS 2021/2022 multimodal competitions drew 260 and 1,600 participants; several top performers had no prior single-cell experience yet beat SOTA.

## All claims (exhaustive)

- `[c01]` Open Problems is a living, community-guided platform hosting 12 single-cell tasks (9 base + subtasks). (p.1035, p.1037) "we present Open Problems, a living, extensive, community-guided platform including 12 current single-cell tasks" — confidence: high — type: methodological — links: [[concepts/static-versus-living-benchmark-paradigm]] [[foundations/openproblems-benchmark]] [[claims/open-problems-hosts-12-single-cell]]
- `[c02]` Over 1,700 single-cell analysis algorithms had been published as of February 2024. (p.1035) "over 1,700 published algorithms (as of February 2024)" — confidence: high — type: quantitative — links: [[foundations/openproblems-benchmark]] [[claims/over-1700-single-cell-analysis-algorithms]]
- `[c03]` Independent single-cell benchmarks overlap in <10% of datasets and metrics. (p.1035) "datasets and metrics typically have less than 10% overlap between benchmarks" — confidence: medium — type: quantitative — links: [[concepts/benchmark-self-assessment-bias]] [[claims/single-cell-benchmarks-overlap-less-than]]
- `[c04]` At least four batch-integration benchmarks exist, each recommending a different optimal method (19 methods × 18 metrics). (p.1035, Fig.1a) "at least four benchmarks of batch integration methods exist, each of which uses different sets of datasets and metrics and suggests different optimal methods" — confidence: high — type: quantitative — links: [[concepts/benchmark-self-assessment-bias]] [[foundations/scib-benchmark-pipeline]] [[claims/four-independent-batch-integration-benchmarks-recommend]]
- `[c05]` Benchmarks run by method-developing groups inflate their own newest models' performance. (p.1035) "when benchmarks are implemented by the same groups introducing new methods, the evaluations tend to inflate performance of the newest models via custom hyperparameter selection and data processing" — confidence: medium — type: correlational — links: [[concepts/benchmark-self-assessment-bias]] [[claims/method-developer-run-benchmarks-inflate-performance]]
- `[c06]` In the CCC task, expression-magnitude scoring outperforms specificity scoring. (p.1038) "methods that rely on expression magnitude outperform approaches that rely on expression specificity" — confidence: medium — type: methodological — links: [[foundations/liana-cell-cell-interaction-inference]] [[foundations/cellphonedb-ligand-receptor]] [[claims/magnitude-based-cell-cell-communication-scoring]]
- `[c07]` Max aggregation of ligand–receptor scores outperforms mean aggregation across CCC tasks/methods. (p.1038) "max aggregation of ligand–receptor scores outperformed mean aggregation across tasks and methods" — confidence: medium — type: methodological — links: [[foundations/liana-cell-cell-interaction-inference]] [[claims/max-aggregation-ligand-receptor-scores-outperforms]]
- `[c08]` Top CCC performers are CellPhoneDB and LIANA's magnitude ensemble. (p.1038) "the top performers across tasks are CellPhoneDB and LIANA's ensemble model of expression magnitude scoring methods" — confidence: medium — type: methodological — links: [[foundations/cellphonedb-ligand-receptor]] [[foundations/liana-cell-cell-interaction-inference]] [[claims/cellphonedb-liana-magnitude-ensemble-top-cell]]
- `[c09]` CCC methods are reliable only on top-ranked interactions; analysts should focus on high-scoring predictions. (p.1038) "methods are better at prioritizing a small fraction of relevant interactions while being prone to noise when their full interaction rankings are considered" — confidence: medium — type: mechanistic — links: [[foundations/liana-cell-cell-interaction-inference]] [[claims/cell-cell-communication-methods-accurate-only]]
- `[c10]` Logistic regression beats complex batch-modeling methods for label projection on all four reference datasets, even with added noise. (p.1038) "a simple logistic regression model outperforms more complex methods that explicitly model batch effects, even when noise is added to the training data" — confidence: high — type: methodological — links: [[concepts/simple-baselines-outperform-complex-single-cell]] [[claims/logistic-regression-outperforms-complex-batch-modeling]]
- `[c11]` Batch effects are easier to correct in single-cell graphs than in embeddings or expression matrices. (p.1038) "it is easier to correct for batch effects in single-cell graphs than in latent embeddings or expression matrices" — confidence: medium — type: methodological — links: [[concepts/batch-removal-vs-bioconservation-tradeoff]] [[foundations/scib-benchmark-pipeline]] [[claims/batch-effects-easier-correct-single-cell]]
- `[c12]` Denoising methods perform best with non-standard variance-stabilizing preprocessing. (p.1038) "denoising methods perform best with non-standard preprocessing approaches that better stabilize variance" — confidence: medium — type: methodological — links: [[concepts/simple-baselines-outperform-complex-single-cell]] [[claims/denoising-methods-perform-best-variance-stabilizing]]
- `[c13]` Simple models tend to outperform complex models for perturbation prediction. (p.1038) "simple models tend to outperform more complex ones for perturbation prediction" — confidence: medium — type: methodological — links: [[concepts/simple-baselines-outperform-complex-single-cell]] [[claims/simple-models-outperform-complex-models-perturbation]]
- `[c14]` NeurIPS 2021/2022 multimodal competitions drew 260 and 1,600 participants. (p.1038) "competitions for multimodal data integration at NeurIPS 2021 and 2022, with over 260 and 1,600 participants, respectively" — confidence: high — type: quantitative — links: [[foundations/openproblems-benchmark]] [[claims/neurips-single-cell-competitions-drew-260]]
- `[c15]` Single-cell-naive competitors substantially outperformed state-of-the-art integration methods. (p.1038) "the developers of multiple top performers had no previous experience with single-cell data, yet were able to submit solutions that substantially outperformed state-of-the-art methods" — confidence: medium — type: correlational — links: [[concepts/static-versus-living-benchmark-paradigm]] [[foundations/openproblems-benchmark]] [[claims/single-cell-naive-competitors-outperformed-state]]

## Discussion captured

### Authors' interpretation

The authors frame Open Problems as a "shift in perspective on method selection for data analysts and method evaluation for developers," moving the field toward higher, community-maintained standards. They argue the platform's community-centered, self-cleansing process (metrics can be removed or amended when biased) promotes the longevity of hosted benchmarks, and that evolving the CCC task beyond its original benchmark publication generated new insight (magnitude > specificity; max > mean).

### Comparisons with prior literature (made by authors)

- Cites four prior batch-integration benchmarks — Tran et al. (Genome Biol. 2020), Mereu et al. (Nat. Biotechnol. 2020), Luecken et al. (Nat. Methods 2022, doi:10.1038/s41587-021-01336-9 region; the scIB paper), Chazarra-Gil et al. (NAR 2021) — as the motivating example of divergent conclusions.
- Cites the common task framework (Donoho 2017) as the conceptual basis.
- Cites the original CCC benchmark (Dimitrov et al., Nat. Commun. 2022, doi:10.1038/s41467-022-30755-0) as the seed for the CCC task.
- Cites Heumos et al. (Nat. Rev. Genet. 2023) and Luecken & Theis (Mol. Syst. Biol. 2019) as best-practice references, and points to Single-Cell Best Practices (sc-best-practices.org) as the intended consumer of platform recommendations.

### Mechanistic hypotheses proposed

- That CCC methods "are better at prioritizing a small fraction of relevant interactions while being prone to noise" over full rankings (p.1038) — explaining why max aggregation and top-5% evaluation favour the strongest signals.

### Caveats and self-criticism

- A community-centered approach "may lead to suboptimal metrics being contributed" (p.1036), mitigated by the ability to remove/amend metrics later.
- Several tasks were defined by method developers rather than from independent benchmarks (e.g. spatial decomposition), so task framing is not fully neutral.
- The collated CCC results shown are from Open Problems v1, an explicitly evolving snapshot.

### Future directions suggested

- Community development to refine and add further open problems; the 9–12 tasks are "a starting point."
- Using living tasks as quantifiable targets for the wider ML community lacking single-cell expertise, including via competitions.
- Method developers submitting prototype and final solutions for automated evaluation, with results includable (CC-BY) in their own method papers.

## Limitations

- Adoption requires non-trivial effort: contributors must containerise their tool as a Viash component and conform to the task API.
- Platform-maintainer-chosen metrics can implicitly favour certain method families.
- CCC (and other) results are snapshots that change as the living platform evolves; the rankings here are v1.
- Ground-truth proxies (spatial co-localization, cytokine activity) for CCC are imperfect stand-ins for true cellular communication.

## Open questions

### Open questions raised by authors

- How best to expand the task set and metric pool with sustained community participation while keeping quality high.
- Whether competition-driven, metric-optimised solutions translate to real-world single-cell analysis.

### Open questions identified during ingest

- How much the neutral-hosting model actually reduces self-assessment inflation versus registered reports.
- In which regimes model complexity genuinely beats simple baselines for single-cell tasks.
- Governance: how to prevent platform-level metric bias as the maintainer set grows.

## My take

This is the canonical publication of the Open Problems platform that the vault already encoded as [[foundations/openproblems-benchmark]]. For my own single-cell work the transferable priors are concrete: (1) seriously tune a simple baseline before adopting a complex model ([[concepts/simple-baselines-outperform-complex-single-cell]]); (2) treat developer-run benchmark rankings with the [[concepts/benchmark-self-assessment-bias]] lens; (3) for CCC analyses, trust only top-ranked predictions and prefer magnitude-based methods (CellPhoneDB/LIANA). It is the living-benchmark successor to scIB ([[papers/benchmarking-atlas-level-data-integration-single]]) from the same Theis-lab lineage.

## Related

- [[papers/benchmarking-atlas-level-data-integration-single]] — scIB; the prior static batch-integration benchmark this platform builds on and absorbs as a task.
- [[concepts/static-versus-living-benchmark-paradigm]]
- [[concepts/benchmark-self-assessment-bias]]
- [[concepts/simple-baselines-outperform-complex-single-cell]]
- [[concepts/batch-removal-vs-bioconservation-tradeoff]]
- [[foundations/openproblems-benchmark]] · [[foundations/scib-benchmark-pipeline]] · [[foundations/common-task-framework]] · [[foundations/viash-component-framework]] · [[foundations/liana-cell-cell-interaction-inference]] · [[foundations/cellphonedb-ligand-receptor]] · [[foundations/czi-cellxgene-atlas]]
