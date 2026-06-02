---
title: "Cytosine base editor (CBE)"
slug: cytosine-base-editor
domain: "genome editing / molecular biology / methods"
status: mainstream
aliases:
  - "CBE"
  - "cytosine base editing"
  - "C-to-T base editor"
  - "BE4max"
  - "eTD-CBE"
first_introduced: "Komor et al. *Nature* 2016"
date_updated: 2026-06-02
source_url: "https://www.nature.com/articles/nature17946"
---

## Definition

A cytosine base editor (CBE) is a CRISPR-derived genome-editing tool that installs a C·G→T·A point mutation at a target site without creating a double-strand break. It fuses a catalytically impaired Cas (nickase or dead Cas9) to a cytidine deaminase (e.g. APOBEC1, rAPOBEC) plus a uracil glycosylase inhibitor (UGI); the deaminase converts cytosine to uracil within a small "editing window" of the protospacer, and DNA repair/replication fixes the change to thymine.

## Intuition

Where nuclease editing (CRISPR-Cas9) cuts DNA and relies on error-prone or template-driven repair, a base editor chemically rewrites a single base in place. This makes it well suited to correcting pathogenic point mutations — but the deaminase acts on *every* cytosine in its activity window, so nearby "bystander" cytosines can be edited too. Avoiding bystander edits is the central engineering challenge, especially at conserved motifs such as splice sites.

## Formal notation

- Architecture: deaminase – nCas9(D10A) or dCas9 – UGI, directed by an sgRNA
- Editing window: typically protospacer positions ~4–8 (PAM-distal numbering)
- Output: C→T (sense) / G→A (antisense)
- Lead engineered variants reduce window width / off-target deamination (e.g. BE4max, BE4max-NG for relaxed NG PAM, high-precision "eTD-CBE")

## Key variants

- **BE3 / BE4 / BE4max** — successive activity- and expression-optimised CBEs
- **BE4max-NG** — relaxed NG-PAM Cas9 for broader targeting (less precise; edits bystanders)
- **eTD-CBE** — next-generation high-precision CBE used to correct *TGM1* c.877-2A>G with no bystander editing
- **Adenine base editors (ABE)** — sister class installing A·T→G·C (distinct deaminase)

## Known limitations

- Bystander editing of additional cytosines within the activity window
- Sequence-context constraints (PAM availability near the target)
- sgRNA-independent (Cas-independent) off-target deamination of DNA/RNA
- Delivery of the large editor + sgRNA to the relevant cell type in vivo

## Open problems

- Narrowing the editing window without sacrificing on-target efficiency
- In vivo delivery to stem/progenitor compartments of barrier tissues
- Long-term durability and competitive dynamics of edited vs unedited cells

## Relevance to active research

[[papers/editing-skin-place-vivo-genome-correction]] screens next-generation CBEs and selects **eTD-CBE** to correct the most common *TGM1* splice-site mutation underlying ARCI, achieving up to 26% on-target editing with no bystander editing in patient keratinocytes — a demonstration that engineered base-editor precision is now compatible with conserved splice motifs, and that the editor can be delivered topically to skin via [[foundations/mrna-lipid-nanoparticle]].
