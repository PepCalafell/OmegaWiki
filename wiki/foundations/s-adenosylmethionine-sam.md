---
title: "SAM — S-adenosylmethionine"
slug: s-adenosylmethionine-sam
domain: metabolism / one-carbon biology
status: mainstream
aliases:
  - "SAM"
  - "S-adenosylmethionine"
  - "AdoMet"
  - "SAMe"
  - "S-adenosyl-L-methionine"
  - "universal methyl donor"
  - "methylation substrate"
first_introduced: "Cantoni 1953"
date_updated: 2026-05-26
source_url: ""
---

## Definition

S-adenosylmethionine (SAM) is the second most widely used enzyme cofactor in biology (after ATP) and the universal methyl-group donor for DNA, histone, RNA, protein, lipid, and small-molecule methylations. SAM is synthesized from methionine and ATP by MAT enzymes (MAT2A in most tissues, MAT1A in liver). After donating its methyl group, SAM becomes S-adenosylhomocysteine (SAH), which is hydrolysed to homocysteine; homocysteine can be remethylated back to methionine via methionine synthase (MS, B12/folate-dependent) or BHMT, closing the methionine cycle.

## Intuition

SAM is the cellular currency for methylation. Tracing SAM origin reveals where methyl groups come from: extracellular methionine, recycled SAH, or — as Ampomah 2022 showed — phagolysosomally degraded apoptotic-cell methionine. Isotope-labelled (13C5,15N) methionine can be tracked through SAM into DNA methyl groups by LC-MS/MS.

## Formal notation

- Synthesis: methionine + ATP → SAM (by MAT2A in macrophages)
- Use: methyltransferase reaction transfers methyl group, generating SAH
- Recycle: SAH → homocysteine + adenosine (SAHH); homocysteine → methionine (MS or BHMT)
- Detection: LC-MS/MS quantification; isotope labelling traces methyl-group origin
- Pharmacology: exogenous SAM supplementation studied for liver disease, depression; works as substrate in MAT2A-inhibitor-rescue experiments

## Variants

- (S,S) vs (R,S) diastereomers; only (S,S) is biologically active
- Free SAM vs MTAP-shunted SAM in nucleotide salvage

## Known limitations

- LC-MS/MS detection complicated by SAM instability at neutral pH
- Cellular pools heterogeneous across organelles; nuclear SAM specifically relevant to DNA methylation

## Open problems

- Mechanisms controlling SAM channeling between competing methyltransferases (DNA vs histone vs polyamine)
- Whether macrophage subcellular compartmentalization sequesters AC-derived methionine specifically near DNMT3A

## Relevance to active research

Central to [[papers/macrophages-use-apoptotic-cell-derived-methionine]] (Ampomah 2022 *Nat Metab*): isotope-labelled (13C5,15N) methionine in apoptotic Jurkat cells is traced into 13C5,15N-SAM and into 13C-methylcytosine on macrophage DNA — direct evidence that AC-derived methionine fuels macrophage DNA methylation via SAM.
