---
# === Identification ===
title: "scBench: Evaluating AI Agents on Single-Cell RNA-seq Analysis"
slug: scbench-evaluating-ai-agents-single-cell
arxiv: "2602.09063"
doi: "10.48550/arXiv.2602.09063"
pmid: ""
venue: "arXiv.org"
year: 2026
authors:
  - Kenny Workman
  - Zhen Yang
  - Harihara Muralidharan
  - Aidan Abdulali
  - Hannah Le
first_author: "Kenny Workman"
corresponding_author: "Kenny Workman"

# === Source & metadata ===
source_type: tex
s2_id: "c953d74f195dcb14bdae74987944f63a62b0f514"
date_added: 2026-06-12
ingested_date: 2026-06-12
ingest_version: 1
last_reviewed:

# === Classification ===
importance: 3
tier: TIER_2
tags:
  - benchmark
  - llm-agent
  - scrna-seq
  - single-cell
  - ai-evaluation
  - bioinformatics-tooling
keywords:
  - scBench
  - AI agents
  - single-cell RNA-seq
  - deterministic grading
  - frontier models
  - mini-SWE-agent
domain: methods

# === Biomedical domain ===
tissue: [blood, bone_marrow, multi]
condition: [healthy, cancer]
disease_specific: [CCUS, small_cell_lung_cancer]
species: [human, mouse]
hypoxia_relevant: false
contains_immune_cells: true
contains_myeloid: true

# === Technique ===
techniques: [scRNA-seq_10x, snRNA-seq]
n_samples:
n_cells_total:
integration_method: ""

# === Biology captured ===
key_cell_types:
  - T cell subtypes
  - regulatory T cells
  - CD8 TEM
  - monocytes
  - NK cells
  - cancer-associated fibroblasts
  - DRG neuron subclasses
  - dendritic cells
key_markers:
  - FOXP3
  - CD3D
  - CD16
  - CD56
  - Acta2
  - Col1a1
key_pathways: []

# === User project membership ===
projects: [methods]
priority: reference
read_status: skimmed

# === HypoxiaVERSE-specific ===
hypoxiaverse_status:
exclusion_reason:
data_availability: "github.com/latchbio/scbench (30 canonical evals + trajectories released; full 394-eval suite withheld)"

# === Cross-references ===
code_url: "https://github.com/latchbio/scbench"
cited_by: []
---

## Problem

For many research groups, scRNA-seq *analysis* — not sequencing — is the
rate-limiting step, demanding multi-step, resource-intensive computation. LLM
agents have advanced in software engineering and data analysis, but it is
unclear whether they can extract biological insight from messy, real-world
single-cell datasets. Existing biology benchmarks emphasise recall,
interpretation, or literature-style reasoning and do not require empirical
interaction with data, so there is no standard, deterministic yardstick for
data-grounded scRNA-seq analysis.

## Key idea

**scBench** is a benchmark of 394 verifiable problems distilled from routine
scRNA-seq workflows spanning six sequencing platforms and seven task categories.
Each evaluation pairs a data snapshot (often an AnnData `.h5ad`), a
natural-language task, and a deterministic grader that scores the agent's
structured JSON output pass/fail. The design principle is **"specify what, not
how"**, with anti-shortcut hardening so answers require genuine data
interaction. scBench complements SpatialBench to cover the two dominant
transcriptional assays. See [[llm-agent-single-cell-rna-seq]] and
[[verifiable-deterministic-bioinformatics-benchmark-grading]].

## Method

- **Platforms (6):** Chromium ([[scrna-seq-10x-chromium]]), BD Rhapsody,
  CSGenetics, Illumina (plate-based snRNA-seq, DRG), MissionBio Tapestri
  (DNA+protein), ParseBio (split-pool). Tissues span PBMCs, tumour
  microenvironment (4T1, CDX SCLC), DRG, and hematopoietic (CCUS) samples.
- **Tasks (7):** QC, normalization, dimensionality reduction, clustering, cell
  typing, differential expression, trajectory analysis.
- **Construction:** five-stage pipeline — reproduce target step → define JSON
  schema → select grader family → calibrate tolerances across valid methods →
  harden against shortcuts (strip `X_pca`/`X_umap`, cached labels). A
  deterministic linter validates each eval; three evaluation types (scientific /
  procedural / observational) govern tolerance width.
- **Graders (5):** NumericTolerance, MultipleChoice, MarkerGenePrecisionRecall,
  LabelSetJaccard, DistributionComparison.
- **Harness:** [[mini-swe-agent-harness]] — bash action loop, 100-step cap, two
  timeout layers (300 s/command, 600 s/eval), single attempt per replicate,
  full trajectory logging. Provides scanpy ([[scanpy]]),
  anndata ([[anndata-annotated-data-structure]]), numpy, pandas, scipy,
  matplotlib. Avoids seed/version artifacts (no exact Leiden cluster counts via
  [[leiden-clustering]]; tests biological interpretation rather than
  [[umap-dimensionality-reduction]] coordinates).
- **Statistics:** two-stage aggregation, K=3 replicates, per-eval mean then
  t-distribution 95% CI on n−1 df; all 394 evals equally weighted.

## Results

- 8 frontier models from 4 providers. Claude Opus 4.6 leads at 52.8%, then Opus
  4.5 (49.9%), GPT-5.2 (45.2%), Sonnet 4.5 (44.2%), GPT-5.1 (37.9%), Grok-4.1
  (35.6%), Grok-4 (33.9%), Gemini 2.5 Pro (29.2%). Anthropic occupies the top four.
- Task difficulty gradient: normalization easiest (70.4% mean) → QC (55.3%) →
  clustering (38.3%) → cell typing (34.9%) → differential expression hardest
  (27.0%). DE is also most discriminative (27.7 pp best-worst spread).
- Platform effect (32.7 pp cross-model mean gap, CSGenetics 59.1% → MissionBio
  26.4%) exceeds the 23.6 pp model spread. MissionBio is hardest for all 8
  models and inverts rankings. See
  [[platform-dependence-agent-analysis-accuracy]].
- vs SpatialBench: scRNA-seq more tractable (52.8% vs 38.4% top; 29.2% vs 20.1%
  bottom), rankings preserved at extremes.

## All claims (exhaustive)

- `[c01]` Claude Opus 4.6 reaches 52.8% top accuracy on scBench (p.3) "Claude Opus 4.6 achieves the highest accuracy at 52.8\% (95\% CI: 48.3--57.2\%)" — confidence: high — type: quantitative — links: [[claims/claude-opus-reaches-52-percent-top]] [[concepts/llm-agent-single-cell-rna-seq]]
- `[c02]` Model accuracy spans 29.2–52.8% with a 23.6 pp spread that exceeds SpatialBench's 18.3 pp (p.3) "The 23.6 percentage point spread between best and worst models exceeds SpatialBench's 18.3 pp spread, indicating that scBench discriminates model capability" — confidence: high — type: quantitative — links: [[claims/scbench-model-accuracy-spans-29-53]] [[concepts/llm-agent-single-cell-rna-seq]]
- `[c03]` Sequencing platform affects accuracy as much as model choice (32.7 pp cross-platform gap > 23.6 pp model spread) (p.4) "Cross-model mean accuracy ranges from 59.1\% on CSGenetics to 26.4\% on MissionBio---a 32.7 pp gap that exceeds the 23.6 pp spread between best and worst models" — confidence: high — type: correlational — links: [[claims/sequencing-platform-affects-agent-scrna-seq]] [[concepts/platform-dependence-agent-analysis-accuracy]]
- `[c04]` MissionBio (Tapestri) is the hardest platform for all 8 models and inverts rankings (p.4) "CSGenetics is easiest for six of eight models; MissionBio is hardest for all eight. MissionBio inverts rankings." — confidence: high — type: quantitative — links: [[claims/missionbio-hardest-scrna-seq-platform-all]] [[concepts/platform-dependence-agent-analysis-accuracy]]
- `[c05]` Differential expression is the hardest task; normalization the easiest; 7/8 models share the ordering (p.4) "Differential expression is hardest (mean 27.0\%) ... Normalization is easiest (cross-model mean 70.4\%). Seven of eight models follow the same difficulty ordering." — confidence: high — type: quantitative — links: [[claims/differential-expression-hardest-scrna-seq-task]] [[concepts/llm-agent-single-cell-rna-seq]]
- `[c06]` Differential expression is the most model-discriminative task (27.7 pp spread) (p.4) "Differential expression is also most discriminative, with a 27.7 pp spread between best and worst models. Model differences concentrate in judgment-heavy stages---DE and cell typing" — confidence: medium — type: correlational — links: [[claims/differential-expression-most-model-discriminative-scrna]] [[concepts/llm-agent-single-cell-rna-seq]]
- `[c07]` scRNA-seq is more tractable for agents than spatial transcriptomics; rankings preserved (p.5) "The top model reaches 52.8\% on scBench versus 38.4\% on SpatialBench---scRNA-seq is more tractable. ... Model rankings are preserved at the extremes" — confidence: medium — type: quantitative — links: [[claims/scrna-seq-analysis-more-tractable-agents]] [[foundations/spatialbench-spatial-transcriptomics-agent-benchmark]]
- `[c08]` Deterministic graders + data-snapshot design enable verifiable, data-grounded evaluation (p.1, 8) "Each problem provides a snapshot of experimental data immediately prior to an analysis step and a deterministic grader that evaluates recovery of a key biological result" — confidence: high — type: methodological — links: [[claims/deterministic-graders-enable-verifiable-data-grounded]] [[concepts/verifiable-deterministic-bioinformatics-benchmark-grading]]
- `[c09]` Frontier agents cannot yet autonomously extract scRNA-seq biological insight without human oversight (p.5) "today's agents can accelerate routine analysis but cannot yet be trusted to autonomously answer scientific questions without stringent verification of intermediate results and human oversight" — confidence: medium — type: mechanistic — links: [[claims/frontier-agents-cannot-autonomously-extract-scrna]] [[concepts/llm-agent-single-cell-rna-seq]]

## Discussion captured

### Authors' interpretation

The authors interpret the results as showing that agents for scRNA-seq occupy
"the same capability regime that SpatialBench exposed for spatial
transcriptomics": some capability, but unable to faithfully extract biological
insight from messy data. They read the 23.6 pp model spread as evidence that the
benchmark discriminates capability, and the larger platform swings as evidence
that reliability requires platform-aware context rather than one-size-fits-all
reasoning.

### Comparisons with prior literature (made by authors)

- SpatialBench (Workman et al., 2025) — the sibling benchmark; scBench reuses
  its design template and statistical aggregation, and the head-to-head
  comparison is a central result.
- PubMedQA (Jin et al., 2019) and Tinn et al. (2023) — cited as biology
  benchmarks that emphasise recall/interpretation and do *not* require empirical
  data interaction, motivating scBench's data-grounded design.
- mini-SWE-agent / SWE-agent (Yang et al., 2024) — the harness.
- Scanpy (Wolf et al., 2018), scran pooling (Lun et al., 2016), Leiden (Traag et
  al., 2019), UMAP (McInnes et al., 2018) — tooling/method references.

### Mechanistic hypotheses proposed

- Platform and tractability gaps "likely reflect uneven training data": e.g.,
  MissionBio appears less frequently in public documentation than Chromium
  pipelines; scRNA-seq has far more public datasets than spatial transcriptomics.
- "Models that overfit on Scanpy tutorials without learning transferable
  analysis techniques should collapse on underrepresented platforms."

### Caveats and self-criticism

- Deterministic graders "necessarily discretize scientific judgment into
  automatically checkable chunks."
- "Each evaluation snapshots a single workflow step rather than capturing
  long-horizon iteration where errors compound and thresholds are revisited."

### Future directions suggested

- Platform-aware context, assay-specific tooling, and self-calibration
  heuristics for reliable agents.
- Exposure to representative scRNA-seq workflows across diverse tissue and
  disease contexts during model training.
- scBench as an evolving specification supporting test-driven development of
  agents via both model training and harness engineering.

## Limitations

- Absolute accuracy is harness- and suite-dependent; no explicit seed or
  temperature control (only source of variation is sampling nondeterminism).
- The full 394-eval suite is withheld to prevent training contamination; only 30
  canonical evals and trajectories are public, limiting external reproduction.
- MissionBio Tapestri is a DNA+protein platform, not RNA-seq — included to
  stress-test generalization, but it is not strictly scRNA-seq.
- Trajectory analysis is thinly represented (7 of 394 evaluations).

## Open questions

### Open questions raised by authors

- How to make agents reliable on judgment-heavy tasks (cell typing, DE) that
  require contextual scientific reasoning.
- Whether reliability gains will come primarily from model training or harness
  engineering.

### Open questions identified during ingest

- Do agent improvements on scBench transfer to SpatialBench (and vice versa),
  given preserved extreme rankings but different absolute levels?
- Would providing platform-specific tooling/context close most of the 32.7 pp
  platform gap, isolating "training-data familiarity" as the driver?

## My take

A clean, well-constructed agent-evaluation benchmark. For this wiki — which is
otherwise biology-heavy — its main value is methodological: the
deterministic-grading + "specify what, not how" template
([[verifiable-deterministic-bioinformatics-benchmark-grading]]) is reusable for
designing or critiquing any data-grounded AI evaluation, and the platform-effect
finding ([[platform-dependence-agent-analysis-accuracy]]) is a useful caution
when interpreting agent capability claims on single-cell tooling. Importance 3:
relevant and timely, but a niche preprint with 0 citations as of ingest.

## Related

- [[mini-swe-agent-harness]] — the agent harness used for all evaluations.
- [[spatialbench-spatial-transcriptomics-agent-benchmark]] — sibling benchmark; direct comparison.
- [[llm-agent-single-cell-rna-seq]] — the agent-as-analysis-actor concept.
- [[verifiable-deterministic-bioinformatics-benchmark-grading]] — grading methodology.
- [[platform-dependence-agent-analysis-accuracy]] — platform-effect concept.
- [[scanpy]] · [[anndata-annotated-data-structure]] · [[leiden-clustering]] · [[umap-dimensionality-reduction]] · [[scrna-seq-10x-chromium]] — tooling referenced by the harness/tasks.
