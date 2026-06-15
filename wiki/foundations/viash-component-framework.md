---
title: "Viash component framework"
slug: viash-component-framework
domain: bioinformatics / reproducible-pipelines
status: mainstream
aliases:
  - Viash
  - viash component
first_introduced: "Cannoodt et al. 2024, J. Open Source Softw. 9, 6089"
date_updated: 2026-06-15
source_url: "https://viash.io/"
---

## Definition

Viash is a meta-framework that turns a single script (in Bash, Python or R) plus a small YAML metadata file (`config.vsh.yaml`) into a self-contained, containerised, language-agnostic pipeline component with a defined command-line interface. Components can be composed into Nextflow workflows.

## Intuition

Reproducible benchmarking needs every method, dataset loader and metric to run identically anywhere. Viash standardises that packaging: each component declares its inputs, outputs and dependencies, builds into a versioned Docker container, and exposes a uniform API, so a contributor can add a new method just by writing one script that follows the task's interface.

## Key variants

- **Component types**: dataset loader, method, metric, utility.
- **Runners**: local execution, containerised execution, Nextflow pipeline assembly.

## Known limitations

- Contributors must containerise their tool and conform to the task API, which is non-trivial up-front effort.
- Adds a packaging layer that authors must learn on top of their analysis code.

## Open problems

Lowering the contribution barrier so method authors can onboard tools without deep Viash/Docker expertise.

## Relevance to active research

Viash is the component substrate of the Open Problems platform: each task is a directory of Viash components (datasets, methods, metrics) run in versioned Docker containers, which is what gives the living benchmark its reproducibility and language-agnosticism.
