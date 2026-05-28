---
title: "GDH / GLUD1 — glutamate dehydrogenase"
slug: glud1-glutamate-dehydrogenase
domain: "molecular biology / amino acid metabolism / mitochondria"
status: mainstream
aliases:
  - GDH
  - GLUD1
  - "glutamate dehydrogenase 1"
  - "glutamate dehydrogenase"
  - "GDH1"
first_introduced: "Glutamate dehydrogenase classic enzymology; leucine allosteric activation characterized mid-20th century; GLUD1 gene cloned 1988"
date_updated: 2026-05-28
source_url: "https://www.ncbi.nlm.nih.gov/gene/2746"
---

## Definition

GDH (encoded by GLUD1) is a mitochondrial-matrix enzyme that catalyzes the reversible oxidative deamination of glutamate to α-ketoglutarate (α-KG) plus ammonia, using NAD(P)⁺/NAD(P)H. It is a key node of glutaminolysis, feeding glutamine-derived carbon into the TCA cycle as α-KG and releasing nitrogen. GDH activity is allosterically regulated: it is activated by ADP and leucine and inhibited by GTP and palmitoyl-CoA. Leucine is the physiological allosteric activator that links branched-chain amino acid levels to glutamine breakdown.

## Intuition

GDH is the valve that decides how much glutamine-derived glutamate is converted into TCA-cycle fuel. Leucine is the "go" signal: when leucine is abundant it binds GDH and opens the valve, accelerating glutaminolysis. In [[papers/mitochondrial-vhl-rewires-cell-metabolism-hypoxia]], blocking leucine breakdown raises leucine, which allosterically fires GDH and drives glutamine into lipids and nucleotides.

## Formal notation

- Reaction: L-glutamate + NAD(P)⁺ + H₂O ⇌ α-ketoglutarate + NH₄⁺ + NAD(P)H.
- Allosteric activators: ADP, leucine; inhibitors: GTP, palmitoyl-CoA, ATP.
- Hexameric enzyme; leucine binds at a regulatory site at the subunit interface (bovine GDH co-crystal PDB: 8ar7; bovine R207 ≈ human R204 forms H-bonds with leucine).
- Human GDH R204M mutant: leucine-unresponsive but retains basal activity.

## Key variants

- GLUD1 vs GLUD2 (hominid-specific retro-gene, GTP-insensitive).
- Activating GLUD1 mutations cause hyperinsulinism-hyperammonemia (HI/HA) syndrome.
- R204M (human) / R207M (bovine): leucine-insensitive separation-of-function mutant used to dissect leucine allostery.

## Known limitations

- GDH operates near equilibrium; flux direction depends on local substrate/cofactor ratios, complicating interpretation of activity assays.
- The GDH inhibitor R162 is a useful tool but has limited potency/selectivity.

## Open problems

- Tissue-specific contribution of GDH-driven glutaminolysis to anabolic vs anaplerotic fates.
- How leucine allostery is integrated with other GDH regulators in vivo.

## Relevance to active research

GDH is the mechanistic linchpin connecting leucine accumulation to glutaminolysis in [[papers/mitochondrial-vhl-rewires-cell-metabolism-hypoxia]]. The leucine-insensitive R204M mutant demonstrates that GDH allostery is required for VHL-promoted hypoxic growth. See [[concepts/leucine-allosteric-gdh-glutaminolysis-activation]] and inhibitor [[foundations/r162-gdh-inhibitor]].
