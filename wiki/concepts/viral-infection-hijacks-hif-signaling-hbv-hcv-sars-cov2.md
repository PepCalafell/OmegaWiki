---
title: "Viral infections hijack HIF signaling: HBV/HBx, HCV core, and SARS-CoV-2 ORF3a as paradigm examples"
aliases:
  - virus-HIF axis
  - viral hijack of hypoxia signaling
  - HBx HIF1a hepatocarcinogenesis
  - HCV core HIF1a normoxic stabilization
  - SARS-CoV-2 ORF3a HIF1a
  - virus-induced pseudohypoxia
  - viral hepatitis hypoxia
  - COVID-19 cytokine storm hypoxia
tags:
  - virology
  - hypoxia
  - HIF1A
  - HIF2A
  - HBV
  - HBx
  - HCV
  - SARS-CoV-2
  - ORF3a
  - cytokine-storm
  - viral-hepatitis
  - hepatocarcinogenesis
maturity: active
key_papers:
  - hypoxia-signaling-human-health-diseases-implications
first_introduced: "HBx-HIF: Lee et al. 2000; SARS-CoV-2-HIF: 2020-2021"
date_updated: 2026-05-21
related_concepts:
  - hif-cross-talk-pi3k-mtor-nfkb-erk-er-stress
  - pseudohypoxia-oncogene-induced-hif-activation
---

## Definition

Multiple human viruses hijack HIF signaling to support their own replication and induce host pathology. The mechanism is generally bidirectional: viral proteins stabilize HIF-α, and stabilized HIF-α reciprocally promotes viral replication. Key examples:

- **HBV X protein (HBx)**: stabilizes HIF-1α via MAPK, MTA1/HDAC1; activates NF-κB to induce HIF-2α; HIF-α activates HBV basal core promoter; HIF-1α offers cccDNA reservoir resisting A3B-mediated immune clearance
- **HCV core protein**: stabilizes HIF-1α under normoxia; elevates VEGF; supports HCV-induced HCC angiogenesis
- **SARS-CoV-2 ORF3a**: induces mitochondrial ROS → HIF-1α stabilization → viral replication + cytokine storm
- **HSV-1, VSV**: HIF-1α facilitates infection (generalizable phenomenon)
- **Counter-effect**: hypoxia reduces ACE2/NRP1/HS expression, lowering SARS-CoV-2 entry — entry vs replication dissociation

## Intuition

Viruses use HIF as a transcriptional co-factor that conveniently increases the cell's biosynthetic and glycolytic capacity (supplying nucleotides, lipids, ATP for replication), suppresses some innate antiviral programs (NF-κB-A3B for HBV), and promotes angiogenesis to support virus-driven tumorigenesis. HIF stabilization is therefore both a viral exploitation and a driver of pathology (cytokine storm in COVID-19, HCC in HBV/HCV).

## Formal notation

HIF-α level (infected) = HIF-α (uninfected) + Δ(viral protein → ROS, MAPK, NF-κB, transcription induction)

Virus replication ∝ HIF-α-driven host metabolic state

## Variants

- Hepatitis viruses → chronic HIF-α stabilization → HCC
- Acute respiratory viruses (SARS-CoV-2) → acute HIF-α surge → cytokine storm
- HSV-1, VSV — HIF-1α as general permissive factor

## Comparison

vs. pseudohypoxic HIF activation in cancer ([[concepts/pseudohypoxia-oncogene-induced-hif-activation]]): same outcome (HIF-α stabilized under normoxia) but via viral proteins rather than oncogenes.

## When to use

When interpreting viral hepatitis carcinogenesis, COVID-19 severity, or chronic-virus-driven pathology; when considering whether HIF inhibitors could repurpose for anti-viral or anti-cytokine-storm therapy.

## Known limitations

In-vivo evidence is heterogeneous; HIF-α can also restrict some viral infections (DNase I induction limits HBV) — net effect is context-dependent.

## Open problems

- Whether HIF inhibitors synergize with antivirals to clear HBV cccDNA
- Whether HIF stabilization is a biomarker of severe COVID-19
- Mechanism of ORF3a-mitochondrial ROS coupling

## Key papers

- [[papers/hypoxia-signaling-human-health-diseases-implications]] — comprehensive review including the Luo Lab's own SARS-CoV-2 ORF3a-HIF-1α work

## My understanding

This concept consolidates a recurrent theme in the review: viral protein-driven HIF stabilization is a unifying mechanism across HBV, HCV, and SARS-CoV-2, with therapeutic implications spanning anti-viral, anti-cancer, and anti-cytokine-storm strategies.
