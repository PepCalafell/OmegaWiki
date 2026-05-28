---
title: "LysM-Cre (myeloid Cre driver)"
slug: lysm-cre
domain: "mouse genetics / method"
status: mainstream
aliases:
  - "LysM-Cre"
  - "LysM–Cre"
  - "Lyz2-Cre"
  - "lysozyme M Cre"
first_introduced: "Clausen et al., Transgenic Res. 1999"
date_updated: 2026-05-28
source_url: ""
---

## Definition

LysM-Cre is a knock-in mouse line expressing Cre recombinase from the lysozyme 2 (Lyz2) locus, driving recombination of floxed alleles in cells of the myeloid lineage — monocytes, macrophages and neutrophils. It is the workhorse driver for myeloid-specific gene deletion.

## Intuition

LysM-Cre answers "what does this gene do in myeloid cells?" by deleting it wherever lysozyme M is expressed. Recombination efficiency varies by population (high in mature macrophages, lower in some monocyte/DC subsets), so a reporter such as Rosa26-eYFP is typically used to mark recombined cells.

## Formal notation

n/a

## Key variants

- Combined with Rosa26-eYFP/RFP reporters for lineage marking.
- Contrasted with inducible drivers ([[foundations/cx3cr1-creer-fate-mapping]]) for temporal control in mature resident macrophages.

## Known limitations

- Incomplete and population-variable recombination.
- Activity in neutrophils and some non-macrophage myeloid cells complicates macrophage-specific claims.

## Open problems

- n/a

## Relevance to active research

Used to generate Dhps-ΔM (myeloid DHPS-deleted) mice; the YFP reporter gates recombined cells for flow cytometry and imaging.
