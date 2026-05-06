---
title: "Hypoxia-associated CNAs preferentially occur early in tumor evolution (in trunk, not branch)"
slug: hypoxia-cnas-occur-early-trunk-evolution
status: supported
confidence: 0.9
tags:
  - hypoxia
  - subclonal-evolution
  - trunk
  - CNAs
  - early-driver
  - selection
  - prostate-cancer
domain: "oncology / cancer-genomics / tumor-evolution"
source_papers:
  - molecular-landmarks-tumor-hypoxia-across-cancer
evidence:
  - source: molecular-landmarks-tumor-hypoxia-across-cancer
    type: supports
    strength: strong
    detail: "In 191 localized PCa tumors with reconstructed subclonal architecture, 99% (660 of 667) of hypoxia-associated CNAs that showed biased evolutionary timing preferentially occured early during tumor evolution (in trunk, not branch). Observed/expected ratio = 73, P=6.71×10⁻²⁴⁹ (hypergeometric test). Quote (p.314): 'Of the CNAs associated with hypoxia that showed biased evolutionary timing, 99% (660 of 667) preferentially occured early during tumor evolution, thus underscoring hypoxia as an early event in prostate tumor development.'"
conditions: "Localized prostate cancer with WGS-based subclonal phylogeny reconstruction (n=191). Generalization to other tumor types not directly tested."
date_proposed: 2026-05-06
date_updated: 2026-05-06
---

## Statement

In localized prostate cancer, copy-number aberrations associated with tumor hypoxia overwhelmingly occur *early* in tumor evolution — placed in the trunk of the subclonal phylogeny, present in all subclones — rather than late branch events. 99% (660/667) of hypoxia-associated CNAs with biased evolutionary timing are trunk events; observed/expected = 73, P=6.71×10⁻²⁴⁹. This positions hypoxia as an *early* selective pressure in tumor development that fixes aggressive somatic alterations population-wide, before subclonal divergence.

## Evidence summary

- [[papers/molecular-landmarks-tumor-hypoxia-across-cancer]] — primary evidence: 191 PCa tumors with reconstructed phylogenies; massive enrichment toward trunk timing.
- Mechanistic interpretation: hypoxia exerts selection at the bottleneck of tumor initiation, favoring subclones that escape apoptosis (mutant TP53), tolerate replication stress (PTEN loss), and maintain telomeres (TERT induction). These subclones then expand population-wide.

## Conditions and scope

- Localized PCa with bulk-WGS + subclonal architecture reconstruction.
- Generalization to other tumor types (BRCA, LUAD) not directly tested.
- Phylogeny accuracy depends on tumor purity and CNA complexity.

## Counter-evidence

- Direct causal proof requires longitudinal modelling.
- Bulk WGS may misclassify some trunk vs branch events; magnitude of misclassification likely insufficient to overturn 99% finding.

## Linked ideas

(none yet)

## Open questions

- Does the trunk-bias of hypoxia-associated CNAs hold in BRCA, LUAD, or other cancer types with subclonal reconstructions?
- Mechanistically, how does an *episodic* hypoxic event during tumor initiation produce trunk-fixed CNAs decades later?
- Whether anti-hypoxia interventions early in tumor development would prevent these trunk events
