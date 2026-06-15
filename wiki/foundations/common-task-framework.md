---
title: "Common task framework"
slug: common-task-framework
domain: benchmarking / meta-science
status: mainstream
aliases:
  - CTF
  - common task framework
first_introduced: "Donoho 2017 (50 Years of Data Science)"
date_updated: 2026-06-15
source_url: "https://doi.org/10.1080/10618600.2017.1384734"
---

## Definition

The common task framework (CTF) is a benchmarking paradigm in which a community agrees on a shared task: a fixed dataset, a held-out evaluation set, and a single quantitative metric, against which all competing methods are scored under identical conditions. Public competitions and leaderboards operationalise the CTF.

## Intuition

By fixing the task and metric in advance and exposing them to everyone, the CTF removes most of the degrees of freedom that let method developers flatter their own tools, and it makes progress measurable and comparable across groups. Donoho identifies the CTF as one of the secret engines of progress in machine learning and predictive modelling.

## Key variants

- **Held-out competition** (Kaggle / NeurIPS challenges): private test set scored automatically.
- **Living benchmark platform**: a continuously updated CTF where the method/dataset/metric pool grows over time.

## Known limitations

- Optimising a single fixed metric can encourage overfitting to the task definition rather than the underlying scientific goal.
- A poorly chosen metric or dataset locks the whole community onto the wrong target.

## Open problems

How to design task/metric definitions that resist gaming while still capturing the real scientific objective.

## Relevance to active research

The common task framework is the conceptual foundation cited by the Open Problems platform for defining single-cell tasks as shared, quantitatively scored challenges, including its NeurIPS competitions.
