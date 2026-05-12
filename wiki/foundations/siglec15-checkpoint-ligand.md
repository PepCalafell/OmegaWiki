---
title: "SIGLEC15 — Siglec-15 immune co-inhibitory ligand"
slug: siglec15-checkpoint-ligand
domain: "immunology / immune-checkpoint"
status: emerging
aliases:
  - "SIGLEC15"
  - "Siglec-15"
  - "S15"
  - "sialic acid-binding Ig-like lectin 15"
  - "CD33L3"
  - "SIGLEC-15"
  - "Siglec15 macrophage"
  - "S15 PD-L1 mutually exclusive"
tags:
  - immune-checkpoint
  - sialic-acid-receptor
  - macrophage
  - TAM
  - dichotomization
maturity: emerging
date_updated: 2026-05-12
---

## Definition

Sialic acid-binding immunoglobulin-like lectin 15 (SIGLEC15) is a transmembrane glycoprotein in the Siglec receptor family, expressed on myeloid cells and a subset of TAMs. SIGLEC15 was proposed by Wang et al. 2019 (Nat Med) as an immune co-inhibitory ligand normalizing tumor immune evasion in a PD-L1-independent axis, with broad expression on tumor-infiltrating myeloid cells where it is typically mutually exclusive with PD-L1.

## Use as a TAM dichotomization marker

The mutual exclusivity of PD-L1 and SIGLEC15 expression in tumor-infiltrating macrophages is exploited in scRNA-seq workflows to circumvent PD-L1 gene dropout: clusters can be partitioned into PD-L1+SIGLEC15− vs PD-L1−SIGLEC15+ TAMs based on SIGLEC15 expression (which is captured more robustly than PD-L1 in droplet-based scRNA-seq). This dichotomization is used by Wang et al. 2024 (Cell Reports Medicine) to identify mature/activated PD-L1+ vs immunosuppressive PD-L1− TAMs in human breast tumors.

## Therapeutic relevance

- Target of normalization cancer immunotherapy strategies independent of the PD-1/PD-L1 axis (Wang 2019 Nat Med).
- Anti-SIGLEC15 agents (e.g., NC318) entered early-phase clinical trials in PD-L1-low tumors where PD-1/PD-L1 blockade fails.
