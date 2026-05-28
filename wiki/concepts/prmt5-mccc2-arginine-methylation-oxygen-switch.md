---
title: "PRMT5-mediated MCCC2 R292 methylation is an oxygen-responsive block on the VHL–MCCC2 interaction"
aliases:
  - "PRMT5 MCCC2 methylation"
  - "MCCC2 R292 arginine methylation"
  - "MCCC2 methyl-arginine switch"
tags:
  - hypoxia
  - PRMT5
  - MCCC2
  - arginine-methylation
  - post-translational-modification
maturity: emerging
key_papers:
  - mitochondrial-vhl-rewires-cell-metabolism-hypoxia
first_introduced: "Li et al. 2026 Cell Metabolism"
date_updated: 2026-05-28
related_concepts:
  - vhl-mccc2-leucine-catabolism-inhibition
  - src-vhl-y185-phosphorylation-mitochondrial-axis
---

## Definition

Under normoxia, PRMT5 symmetrically dimethylates MCCC2 at arginine 292 (R292); this methyl-arginine sterically/electrostatically blocks VHL from engaging MCCC2. Hypoxia represses this modification (PRMT5 activity is inhibited via SRC-mediated PRMT5 Y283 phosphorylation), de-blocking R292 and permitting the VHL–MCCC2 interaction. MCCC2 methylation is thus the "off" half of a dual-PTM switch, complementary to SRC-driven VHL Y185 phosphorylation.

## Intuition

R292 is the lock and the methyl group is the bolt thrown across it. In normoxia PRMT5 keeps the bolt closed so VHL cannot bind; in hypoxia SRC shuts down PRMT5, the bolt is withdrawn, and (with phospho-Y185 on VHL) the interaction proceeds.

## Formal notation

- PRMT5 (type II PRMT) produces symmetric dimethyl-arginine; only PRMT5 (not PRMT1/PRMT7) methylates MCCC2.
- MCCC2 has three methyl-arginines (R268, R292, R332); only R292 lies in the VHL-binding region (269–300) and is PRMT5-specific.
- R292 heavily methylated at 21% O₂; R292K mutation abolishes methylation.
- MCCC2 R292K: cannot be methylated, but the positive charge is preserved → still cannot disrupt VHL binding unless paired with phosphomimetic VHL Y185E (gain-of-function combination recapitulates the interaction in normoxia).
- PRMT5 levels constant across O₂; activity regulated by SRC-mediated tyrosine phosphorylation (PRMT5 Y283).

## Variants

- PRMT5 Y283F (non-phosphorylatable): restores MCCC complex, blocks VHL phenotype.
- N-MTS–VHL Y185E + MCCC2 R292K: forced gain-of-function interaction under normoxia.

## Comparison

- Versus SRC-pVHL arm: methylation acts on the partner (MCCC2) as a removable block; phosphorylation acts on VHL as a required enabler. Hypoxia toggles both simultaneously through SRC.
- Versus MTAP-PRMT5 cancer dependency: same enzyme, different (metabolic-enzyme) substrate — suggests methionine/SAM–leucine metabolic crosstalk.

## When to use

Invoke when explaining oxygen-gated protein–protein interactions, metabolic-enzyme arginine methylation, or potential SAM/methionine–leucine metabolic crosstalk.

## Known limitations

- R292 methyl-site mapping by MS; interface model from docking.
- In vivo demonstration limited to renal ischemia and ccRCC correlations.

## Open problems

- Broader catalogue of PRMT5 metabolic-enzyme substrates.
- Therapeutic exploitation of the methionine–leucine crosstalk in hypoxic disease.

## Key papers

- [[papers/mitochondrial-vhl-rewires-cell-metabolism-hypoxia]] — Li et al. 2026.

## My understanding

The two-lock design (de-block MCCC2 AND enable VHL) gives the switch hypoxia-specificity that neither PTM alone could. The SRC convergence (phosphorylating both VHL and PRMT5) is the unifying upstream sensor. Links [[foundations/prmt5-arginine-methyltransferase]], [[foundations/mccc2-3-methylcrotonyl-coa-carboxylase]], [[foundations/s-adenosylmethionine-sam]].
