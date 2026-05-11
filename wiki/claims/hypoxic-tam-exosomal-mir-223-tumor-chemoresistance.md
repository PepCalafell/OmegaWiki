---
title: "Hypoxic-TAM-derived exosomal miR-223 lowers tumor PTEN to activate PI3K/AKT, increasing tumor viability and chemoresistance"
slug: hypoxic-tam-exosomal-mir-223-tumor-chemoresistance
status: supported
confidence: 0.80
tags:
  - miR-223
  - TAM
  - exosome
  - PTEN
  - PI3K
  - AKT
  - chemoresistance
  - hypoxia
  - TAM-to-tumor
  - reverse-direction-crosstalk
domain: "oncology / immunology / exosome-biology"
source_papers:
  - hypoxia-driven-crosstalk-between-tumor-tumor
evidence:
  - source: hypoxia-driven-crosstalk-between-tumor-tumor
    type: supports
    strength: medium
    detail: "Bai 2022 (DOI 10.1186/s12943-022-01645-2, p.9) reviews that exosomal miR-223 derived from hypoxic TAMs is internalized by co-cultured tumor cells, leading to PTEN suppression, PI3K/AKT activation, decreased apoptosis, increased cell viability, and enhanced drug resistance. Documents the TAM→tumor exosomal direction, complementing the more widely characterized tumor→TAM exosomal direction."
conditions: "Demonstrated in epithelial ovarian cancer and other systems; in vitro co-culture evidence with hypoxic TAMs (1% O₂) transferring exosomes to tumor cells."
date_proposed: 2026-05-11
date_updated: 2026-05-11
---

## Statement

Most hypoxia-driven exosomal-miRNA mechanisms in the TME describe tumor cells educating TAMs via secreted exosomes. The miR-223 mechanism reverses this direction: hypoxic TAMs (1% O₂) package miR-223 into exosomes, which are then internalized by tumor cells. Inside tumor cells, miR-223 suppresses PTEN expression, releasing PI3K/AKT signaling, which (a) decreases apoptosis, (b) increases cell viability, and (c) enhances resistance to cytotoxic chemotherapy. This is a TAM→tumor exosomal channel that contributes to therapy resistance via the same PTEN-PI3K-AKT axis used in the tumor→TAM direction by exosomal miR-301a-3p.

## Evidence summary

- [[papers/hypoxia-driven-crosstalk-between-tumor-tumor]] — Bai 2022 *Molecular Cancer*.
- Concept: [[concepts/hypoxia-exosomal-mirna-tam-polarization]] (this is the reverse direction).
- Foundation: [[foundations/pten-tumor-suppressor]].

## Conditions and scope

- Hypoxic-TAM source (M2 polarized, 1% O₂); recipient is tumor cell, not other immune cell.
- In vitro co-culture evidence; in vivo specificity (does miR-223 traffic exclusively in TAM-derived exosomes vs other exosome sources?) is less established.

## Counter-evidence

- miR-223 is also abundantly expressed in neutrophils and platelets — exosomal miR-223 in vivo could derive from these populations, not exclusively from TAMs.
- Some studies report miR-223 as tumor-suppressive in other cancer contexts.

## Linked ideas

(none yet)

## Open questions

- What HIF-driven exosome-loading machinery (nSMase2, Rab27a, Alix) packages miR-223 specifically in hypoxic TAMs?
- Does pharmacological inhibition of TAM exosome release (e.g. GW4869) reverse chemoresistance in PTEN-low tumors?
