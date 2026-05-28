---
title: "Leucine (branched-chain amino acid)"
slug: leucine-bcaa
domain: "biochemistry / amino acid metabolism / nutrient signaling"
status: mainstream
aliases:
  - leucine
  - L-leucine
  - "branched-chain amino acid leucine"
first_introduced: "Leucine isolated 1819 (Proust); classic essential amino acid"
date_updated: 2026-05-28
source_url: "https://pubchem.ncbi.nlm.nih.gov/compound/6106"
---

## Definition

Leucine is an essential branched-chain amino acid (BCAA) and the most abundant BCAA in the human body. Beyond protein synthesis, leucine is a signaling metabolite: it activates mTORC1 (via sestrin2/leucyl-tRNA synthetase sensing) and allosterically activates glutamate dehydrogenase (GDH). Its catabolism proceeds via BCAT → BCKDH → MCCC toward acetyl-CoA. Leucine handling links nutrient status to anabolic signaling and is dysregulated in diabetes and cancer.

## Intuition

Leucine is both a building block and a messenger. As a messenger it reports "amino acids are plentiful" — turning on growth signaling (mTOR) and pushing glutamine into the TCA cycle (via GDH). Manipulating leucine levels (by blocking its breakdown, or by supplementation) changes downstream metabolism even without changing protein synthesis.

## Formal notation

- Structure: (2S)-2-amino-4-methylpentanoic acid; essential BCAA.
- Signaling: mTORC1 activation (sestrin2 sensor); GDH allosteric activation (binds GDH regulatory site, physiological range ~1–10 μM intramitochondrial).
- Catabolism: leucine → α-KIC (BCAT) → isovaleryl-CoA (BCKDH) → 3-methylcrotonyl-CoA → MCCC → acetyl-CoA + acetoacetate.

## Key variants

- Leucine vs isoleucine vs valine (the three BCAAs); only leucine activates GDH and is uniquely processed by MCCC at the carboxylation step.
- α-KIC: the keto-acid form, interconvertible with leucine via BCAT.

## Known limitations

- Compartmentalization (cytosolic vs mitochondrial leucine pools) matters for which signaling output dominates.
- mTOR vs GDH outputs can diverge depending on context (e.g., hypoxia suppresses mTOR).

## Open problems

- Relative contribution of leucine's mTOR vs GDH signaling roles across tissues.
- How intramitochondrial leucine is sensed and buffered.

## Relevance to active research

In [[papers/mitochondrial-vhl-rewires-cell-metabolism-hypoxia]], mitochondrial leucine accumulation (from VHL-mediated MCCC2 inhibition) allosterically activates GDH to drive glutaminolysis under hypoxia; notably leucine repletion failed to activate mTOR because hypoxia represses mTOR, isolating the GDH axis. Dietary leucine supplementation ameliorated renal ischemia-reperfusion injury in vivo. See [[concepts/leucine-allosteric-gdh-glutaminolysis-activation]].
