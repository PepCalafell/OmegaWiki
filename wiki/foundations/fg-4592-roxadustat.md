---
title: "FG-4592 / Roxadustat (PHD inhibitor, HIF stabilizer)"
slug: fg-4592-roxadustat
domain: "pharmacology / hypoxia-signaling"
status: mainstream
aliases:
  - "FG-4592"
  - "Roxadustat"
  - "ASP1517"
  - "FG4592"
first_introduced: "FibroGen, clinical trials early 2010s; approved for renal anemia (China 2018, EU 2021)"
date_updated: 2026-05-27
source_url: "https://pubchem.ncbi.nlm.nih.gov/compound/11256664"
---

## Definition

FG-4592 (roxadustat) is an orally bioavailable, small-molecule inhibitor of the prolyl hydroxylase domain (PHD/EGLN) enzymes. By blocking PHD-mediated hydroxylation of HIFα at the conserved proline residues, it prevents VHL-dependent ubiquitination, stabilizing HIF-1α and HIF-2α even under normoxia ("pseudohypoxia"). It is clinically used to treat chronic-kidney-disease anemia by inducing HIF-driven erythropoietin and iron-handling genes.

## Intuition

A drug that simulates hypoxia at the transcriptional level without limiting oxygen — useful both as a clinical erythropoiesis booster and as a research tool to dissect HIF-dependent vs HIF-independent components of the hypoxic response.

## Formal notation

- Target: PHD1/PHD2/PHD3 (EGLN2/EGLN1/EGLN3)
- Mechanism: 2-oxoglutarate–mimetic competitive inhibitor
- Typical in-vitro concentration: 25–50 µM
- Result: nuclear accumulation of HIF-1α, induction of HRE-driven genes (EPO, VEGF, glycolytic enzymes)

## Key variants

- Other HIF-stabilizing PHD inhibitors: daprodustat, vadadustat, molidustat, desidustat.

## Known limitations

- Stabilizes both HIF-1α and HIF-2α — not isoform-selective.
- Off-target effects on other 2-OG-dependent dioxygenases (TET, JmjC demethylases) at high doses.
- Pseudohypoxia eliminates HIF-independent hypoxic effects (mitochondrial ROS, lipid changes) — useful for isolation but loses physiological completeness.

## Open problems

- Long-term safety in non-renal indications (cancer risk debated due to angiogenesis/HIF-2α activation).
- Cell-type-specific transcriptional outputs of pharmacological vs physiological HIF stabilization.

## Relevance to active research

In [[papers/hif-regulates-mitochondrial-function-bone-marrow]] (Woods et al., *Sci. Rep.* 2025), FG-4592 (25 µM, 16 h) is used to dissociate steady-state HIF-1α function from inducible/stress-activated HIF-1α function in BMDMs vs alveolar macrophages, revealing that TR-AMs require HIF-1α only for FG-4592-induced glycolytic rescue against ETC inhibitors, while BMDMs depend on HIF-1α at baseline and exhibit a Myc-driven mitochondrial compensation upon HIF-1α loss.
