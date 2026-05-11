---
title: "HIF-1α has stronger pVHL affinity than HIF-2α; proline-hydroxylation site differentially modulates HIF-α / pVHL interaction"
slug: hif1a-stronger-vhl-affinity-than-hif2a
status: supported
confidence: 0.85
tags:
  - HIF1A
  - HIF2A
  - VHL
  - PHD
  - proline-hydroxylation
  - protein-protein-affinity
  - structural-biology
  - oxygen-sensing
domain: "molecular-biology / hypoxia / structural-biology"
source_papers:
  - hypoxia-driven-crosstalk-between-tumor-tumor
evidence:
  - source: hypoxia-driven-crosstalk-between-tumor-tumor
    type: supports
    strength: medium
    detail: "Bai 2022 (DOI 10.1186/s12943-022-01645-2, p.5) summarizes that HIF-1α has stronger affinity for pVHL than HIF-2α, with different sites of proline hydroxylation playing different roles in HIF-α / pVHL interactions. Structural and biochemical work (e.g. Hon 2002 Nature, Min 2002 Science) provides the affinity-difference evidence."
conditions: "Established biochemically and structurally; explains in part why HIF-2α has a longer half-life and dominates the late-hypoxia transcriptional program."
date_proposed: 2026-05-11
date_updated: 2026-05-11
---

## Statement

HIF-1α and HIF-2α are paralogous α-subunits of the HIF transcription factor that share regulatory machinery (PHD/VHL/FIH) but differ in pVHL affinity. HIF-1α binds pVHL more strongly than HIF-2α, contributing to its faster turnover under normoxia / reoxygenation. The specific proline residues that are hydroxylated by PHDs (Pro402 and Pro564 in HIF-1α; equivalent residues in HIF-2α) and the surrounding sequence context dictate the strength of the HIF-α / pVHL interaction. Functionally, this affinity asymmetry helps explain why HIF-2α dominates the *late* (chronic) hypoxic transcriptional program while HIF-1α dominates the *early* (acute) hypoxic program, and why HIF-2α-specific inhibitors (Belzutifan, PT2385) target a clinically distinct biology than HIF-1α inhibitors (PX-478).

## Evidence summary

- [[papers/hypoxia-driven-crosstalk-between-tumor-tumor]] — Bai 2022 *Molecular Cancer*.
- Foundations: [[foundations/hif1a]], [[foundations/vhl-von-hippel-lindau]].
- Structural-biology evidence: Hon 2002 *Nature* on pVHL-HIF1α structure; Min 2002 *Science* on the same.

## Conditions and scope

- The affinity asymmetry holds in vitro with purified proteins; in vivo, additional post-translational modifications further modulate the interaction.
- HIF-2α-specific stabilization in ccRCC (VHL-loss) explains why HIF-2α inhibitors are the lead clinical asset for ccRCC.

## Counter-evidence

- Some primary studies report comparable HIF-1α and HIF-2α pVHL affinities under specific buffer conditions.
- Cell-type-specific factors (CITED2, p300, FIH) can mask the intrinsic affinity difference.

## Linked ideas

(none yet)

## Open questions

- Does the affinity asymmetry contribute to the temporal switch from HIF-1α-dominant (acute) to HIF-2α-dominant (chronic) hypoxic transcription, or is the switch driven primarily by differential transcription / translation?
- Can the affinity difference be pharmacologically exploited by isoform-selective pVHL-recruiting PROTAC degraders?
