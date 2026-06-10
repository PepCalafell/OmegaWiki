---
title: "Ruxolitinib — JAK1/JAK2 inhibitor"
slug: ruxolitinib-jak-inhibitor
domain: "pharmacology / immunology"
status: mainstream
aliases:
  - "ruxolitinib"
  - "INCB018424"
  - "Jakafi"
first_introduced: "Incyte; FDA approval 2011 (myelofibrosis)"
date_updated: 2026-06-10
source_url: "https://go.drugbank.com/drugs/DB08877"
---

## Definition

Ruxolitinib is a small-molecule ATP-competitive inhibitor selective for Janus kinases JAK1 and JAK2. By blocking JAK catalytic activity it prevents STAT phosphorylation downstream of many cytokine receptors, including the IL-2 receptor (JAK1/JAK3 → STAT5). Clinically used in myelofibrosis, polycythaemia vera, graft-versus-host disease, and atopic dermatitis.

## Intuition

It is the canonical "turn off JAK-STAT signalling now" pharmacological tool — a benchmark for how completely cytokine signalling can be acutely shut down.

## Formal notation

Inhibits JAK1/JAK2 kinase activity → blocks receptor-associated JAK trans-phosphorylation → no STAT5 phosphorylation.

## Key variants

- Other JAK inhibitors: tofacitinib (JAK1/3), baricitinib (JAK1/2), upadacitinib (JAK1).

## Known limitations

- Not receptor-specific: blocks all JAK1/2-dependent cytokine signalling, causing cytopenias/immunosuppression.
- Reversible/competitive — requires sustained drug presence.

## Open problems

- Achieving pathway- or ligand-specific signalling shutdown, which receptor-level switches can provide.

## Relevance to active research

In [[design-facilitated-dissociation-enables-timing-cytokine]], ruxolitinib is the positive-control "off-switch": the designed effector terminates ASNeo2-driven STAT5 phosphorylation nearly as effectively as ruxolitinib, but acts at the receptor (ligand dissociation) rather than by blocking JAK kinase activity, giving ligand-specific rather than pathway-wide shutdown. Connects to [[stat5-tf]] and [[il-2-cytokine]].
