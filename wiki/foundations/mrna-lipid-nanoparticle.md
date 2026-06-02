---
title: "mRNA lipid nanoparticle (mRNA-LNP)"
slug: mrna-lipid-nanoparticle
domain: "drug delivery / nanomedicine / methods"
status: mainstream
aliases:
  - "mRNA-LNP"
  - "LNP"
  - "lipid nanoparticle"
  - "ionizable lipid nanoparticle"
  - "mRNA-lipid nanoparticle"
first_introduced: "Semple et al. *Nat Biotechnol* 2010 (ionizable LNP); clinically validated by mRNA COVID-19 vaccines 2020"
date_updated: 2026-06-02
source_url: "https://www.nature.com/articles/nbt.1602"
---

## Definition

A lipid nanoparticle (LNP) is a ~50–150 nm self-assembled particle — typically an ionizable lipid, helper phospholipid, cholesterol, and a PEG-lipid — that encapsulates and delivers nucleic-acid cargo (most often mRNA) into cells. The ionizable lipid is neutral at physiological pH (low toxicity in circulation) but protonates in the acidic endosome, promoting endosomal escape and cytosolic cargo release where the mRNA is translated.

## Intuition

LNPs solve the core problem of nucleic-acid therapeutics: naked mRNA is unstable, immunogenic, and cannot cross cell membranes. The LNP shields the cargo, ferries it across the membrane, and releases it intracellularly. The same platform that delivers vaccine antigen mRNA can deliver a genome-editor mRNA (base editor + sgRNA), making transient, non-viral, re-dosable genome editing possible.

## Formal notation

- Composition (molar %): ionizable lipid (~50) : phospholipid (~10) : cholesterol (~38) : PEG-lipid (~1.5)
- Cargo: mRNA (vaccine antigen, replacement protein, or genome-editor) ± sgRNA
- Key tunable: ionizable lipid pKa (~6.2–6.5 optimal for endosomal escape), particle size, PEG density
- Biodistribution biased to liver by default; reformulation/targeting redirects to other tissues

## Key variants

- **Vaccine LNPs** (e.g. SM-102, ALC-0315) — antigen mRNA delivery
- **Organ-targeted LNPs** (SORT lipids, ligand-decorated) — redirect tropism off-liver
- **Genome-editing LNPs** — co-deliver editor mRNA + sgRNA for transient in vivo editing (muscle, eye, brain, and now skin)
- **Topical / transdermal LNPs** — local skin delivery, often paired with barrier-modulation to reach viable epidermis

## Known limitations

- Default hepatic tropism; extrahepatic delivery requires reformulation
- PEG-related anti-PEG immunity on repeat dosing
- Barrier tissues (skin, mucosa) exclude LNPs without physical/chemical permeabilisation
- Transient expression — an advantage for transient editors, a limit for sustained protein replacement

## Open problems

- Reaching tissue stem-cell compartments behind physical barriers (e.g. basal keratinocytes)
- Scaling local delivery to large surface areas / whole organs
- Minimising innate immune activation on repeat administration

## Relevance to active research

[[papers/editing-skin-place-vivo-genome-correction]] uses topically applied mRNA-LNPs to deliver a [[foundations/cytosine-base-editor]] into human skin, combined with [[concepts/laser-microablation-transdermal-lnp-delivery]] to breach the skin barrier. LNPs encapsulating base-editing cargo transfected 39.1% of basal keratinocytes (skin stem cells) in a 3D ARCI skin model with minimal immunogenicity and limited systemic dissemination — extending the LNP-mediated in vivo editing previously shown in muscle, eye, and brain to skin.
