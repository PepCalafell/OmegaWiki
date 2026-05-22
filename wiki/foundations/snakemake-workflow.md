---
title: "Snakemake — reproducible bioinformatics workflow engine"
slug: snakemake-workflow
domain: "methods / workflow-engine / bioinformatics-infrastructure"
status: mainstream
aliases:
  - Snakemake
  - snakemake pipeline
  - snakemake workflow
  - Köster Snakemake
  - bioinformatics workflow engine
  - DAG-based bioinformatics pipeline
  - reproducible bioinformatics workflow
  - snakemake-wrappers
  - snakemake conda environments
  - snakemake Snakefile
first_introduced: "Köster & Rahmann 2012/2018 *Bioinformatics* (Snakemake — a scalable bioinformatics workflow engine)"
date_updated: 2026-05-22
source_url: "https://snakemake.readthedocs.io"
---

## Definition

Snakemake is a Python-based workflow engine that defines bioinformatics pipelines as DAGs of rules with declared inputs, outputs, and shell/Python actions. It tracks dependencies, parallelises across cores or cluster jobs, manages conda environments per rule, and supports reproducible re-execution.

## Strengths

- De-facto standard for reproducible bioinformatics pipelines.
- Native cluster (SLURM, SGE) and cloud (Google, Azure, Kubernetes) support.
- Conda integration for per-rule environment isolation.
- Used to drive scIB benchmark — see [[foundations/scib-benchmark-pipeline]].

## Known limitations

- Steep learning curve for new bioinformaticians.
- Snakefile DSL diverges from pure Python.

## Relevance to active research

Snakemake underpins the scIB integration benchmark and many other large-scale reproducible single-cell pipelines. See [[papers/benchmarking-atlas-level-data-integration-single]].
