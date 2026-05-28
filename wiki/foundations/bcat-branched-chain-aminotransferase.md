---
title: "BCAT — branched-chain aminotransferase"
slug: bcat-branched-chain-aminotransferase
domain: "molecular biology / amino acid metabolism"
status: mainstream
aliases:
  - BCAT
  - "branched-chain aminotransferase"
  - BCAT1
  - BCAT2
  - "branched-chain amino acid transaminase"
first_introduced: "BCAT enzymology classic; BCAT1 (cytosolic) and BCAT2 (mitochondrial) isoforms characterized 1990s"
date_updated: 2026-05-28
source_url: "https://www.ncbi.nlm.nih.gov/gene/587"
---

## Definition

BCAT catalyzes the first and reversible step of branched-chain amino acid (BCAA: leucine, isoleucine, valine) catabolism — the transamination of a BCAA to its branched-chain α-keto acid (for leucine, α-ketoisocaproic acid, α-KIC) with concomitant transfer of the amino group to α-ketoglutarate, yielding glutamate. There are two isoforms: cytosolic BCAT1 and mitochondrial BCAT2. BCAT deregulation is implicated in diabetes (systemic BCAA accumulation with insulin resistance) and in multiple cancers (glioma, leukemia, gastric, pancreatic).

## Intuition

BCAT is the on-ramp to BCAA breakdown and is reversible, so it equilibrates leucine with its keto-acid α-KIC. Supplying α-KIC can refill leucine downstream; inhibiting BCAT (e.g., BCAT-IN-2) blocks that interconversion. This reversibility lets experiments test whether leucine itself, rather than downstream catabolites, drives a phenotype.

## Formal notation

- Reaction: BCAA + α-ketoglutarate ⇌ branched-chain α-keto acid + glutamate.
- Leucine ⇌ α-ketoisocaproic acid (α-KIC).
- Isoforms: BCAT1 (cytosolic, BCAT1 gene), BCAT2 (mitochondrial, BCAT2 gene).
- Downstream: branched-chain α-keto acid → BCKDH (irreversible committed step).

## Key variants

- BCAT1 (cytosolic) vs BCAT2 (mitochondrial).
- Inhibitor: BCAT-IN-2 (tool compound) blocks BCAA transamination.

## Known limitations

- Reversibility makes net-flux direction context-dependent.
- Isoform redundancy and compartmentalization complicate interpretation.

## Open problems

- Tissue- and tumor-specific dependence on BCAT1 vs BCAT2.
- Whether BCAT inhibition is therapeutically tractable without metabolic toxicity.

## Relevance to active research

In [[papers/mitochondrial-vhl-rewires-cell-metabolism-hypoxia]], BCAT inhibition (BCAT-IN-2) and α-KIC supplementation are used to prove that leucine accumulation — not downstream catabolites — drives GDH activation and hypoxic adaptation; BCAT-IN-2 was also tested in vivo in renal ischemia-reperfusion. See [[foundations/bcat-in-2-inhibitor]] and [[concepts/leucine-allosteric-gdh-glutaminolysis-activation]].
