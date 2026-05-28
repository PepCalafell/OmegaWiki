---
title: "MCCC2 — 3-methylcrotonyl-CoA carboxylase subunit 2"
slug: mccc2-3-methylcrotonyl-coa-carboxylase
domain: "molecular biology / amino acid metabolism / mitochondria"
status: mainstream
aliases:
  - MCCC2
  - "3-methylcrotonyl-CoA carboxylase 2"
  - "methylcrotonoyl-CoA carboxylase beta"
  - "MCCC beta subunit"
  - MCC
  - "3-methylcrotonyl-CoA carboxylase complex"
first_introduced: "MCC enzyme characterized in leucine catabolism (classic biochemistry); MCCC1/MCCC2 genes cloned ~2001 (Gallardo, Baumgartner)"
date_updated: 2026-05-28
source_url: "https://www.ncbi.nlm.nih.gov/gene/64087"
---

## Definition

MCCC2 is the β subunit of mitochondrial 3-methylcrotonyl-CoA carboxylase (MCCC, also called MCC), a biotin-dependent enzyme that catalyzes a rate-limiting step in the catabolism of the branched-chain amino acid leucine (the carboxylation of 3-methylcrotonyl-CoA to 3-methylglutaconyl-CoA). The holoenzyme is a dodecamer of six α (MCCC1) and six β (MCCC2) subunits. MCCC acts specifically on the leucine degradation pathway and not on isoleucine or valine. Loss-of-function mutations in MCCC1/MCCC2 cause 3-methylcrotonyl-CoA carboxylase deficiency, an inborn error of leucine metabolism.

## Intuition

MCCC is the committed gate through which leucine carbon flows toward acetyl-CoA. If you block MCCC, leucine cannot be broken down and accumulates upstream. Cells exploit this: in [[papers/mitochondrial-vhl-rewires-cell-metabolism-hypoxia]] mitochondrial VHL binds MCCC2 to disrupt the MCCC complex, halting leucine breakdown so that leucine builds up and signals downstream.

## Formal notation

- Reaction: 3-methylcrotonyl-CoA + HCO₃⁻ + ATP → 3-methylglutaconyl-CoA + ADP + Pi (biotin-dependent carboxylation).
- Holoenzyme: α₆β₆ dodecamer; MCCC1 (α, biotin carboxylase + biotin carrier) + MCCC2 (β, carboxyltransferase).
- Pathway position: BCAT → BCKDH → isovaleryl-CoA-DH → **MCCC** → methylglutaconyl-CoA hydratase → HMG-CoA lyase → acetyl-CoA + acetoacetate.
- Specific to leucine; isoleucine and valine bypass MCCC.

## Key variants

- MCCC1 (α subunit, gene MCCC1) vs MCCC2 (β subunit, gene MCCC2).
- Regulation by acyl modification: SIRT4 loss increases MCCC1 acylation and disrupts the complex.
- PTM regulation reported in cancer: PRMT5-mediated arginine methylation at MCCC2 R292 (see [[papers/mitochondrial-vhl-rewires-cell-metabolism-hypoxia]]).

## Known limitations

- Most clinical literature concerns the recessive metabolic disorder (3-MCC deficiency), which is often biochemically benign — the physiological importance of partial MCCC modulation in adult tissues is less defined.
- The MCCC complex requires biotinylation of MCCC1; experimental perturbations of one subunit can have indirect effects on holoenzyme assembly.

## Open problems

- Whether MCCC modulation is a general node of metabolic adaptation beyond hypoxia.
- Structural basis of the VHL–MCCC2 interaction and of PRMT5-driven methyl-arginine regulation.
- Therapeutic exploitability of MCCC2 PTMs in VHL-mutant ccRCC and ischemic disease.

## Relevance to active research

Central to leucine/BCAA catabolism and to the non-canonical mitochondrial VHL pathway described in [[papers/mitochondrial-vhl-rewires-cell-metabolism-hypoxia]], where inhibition of MCCC2 phenocopies mitochondrial VHL and supports hypoxic cell growth. See [[concepts/vhl-mccc2-leucine-catabolism-inhibition]] and [[concepts/prmt5-mccc2-arginine-methylation-oxygen-switch]].
