---
title: "Grade-of-membership / topic modeling for RNA-seq (fastTopics)"
slug: fasttopics-grade-of-membership
domain: bioinformatics / unsupervised modeling
status: mainstream
aliases:
  - grade of membership model
  - GoM model
  - topic model
  - topic modeling RNA-seq
  - fastTopics
  - structure plot
  - LDA-like model expression
  - mixed-membership clustering
first_introduced: "2003"
date_updated: 2026-05-22
source_url: "https://stephenslab.github.io/fastTopics/"
---

## Definition

Grade-of-membership (GoM) / topic models decompose each sample's expression profile into a probability distribution over K latent "topics" (multinomial gene-distributions). Unlike hard clustering, a sample partially belongs to multiple topics, capturing graded biological processes.

## Intuition

Tissues do not occupy single discrete states under perturbation; topic models give each sample a mixture proportion across K topics, where some topics encode baseline tissue identity and others encode shared cross-tissue inflammatory programs.

## Relevance to active research

In Takahama et al. 2024, a k=16 GoM fit to 364 whole-tissue RNA-seq samples across 13 organs separated tissue-identity topics (e.g. k4 small intestine, k15 heart) from sepsis-induced topics (e.g. k9 organism-wide ISG, k13 splenic/lung neutrophil program). Topic modeling thereby disambiguated baseline biology from sepsis-driven biology in a single integrated model.
