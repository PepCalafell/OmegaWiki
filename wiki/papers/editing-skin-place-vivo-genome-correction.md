---
# === Identification ===
title: "Editing the skin in place: In vivo genome correction of rare skin disease"
slug: editing-skin-place-vivo-genome-correction
arxiv: ""
doi: "10.1016/j.stem.2026.01.003"
pmid: ""
venue: "Cell Stem Cell"
year: 2026
authors: [Rohan Palanki, Emily Fitzgerald, Alexandre J. Poirier, Michael J. Mitchell]
first_author: "Rohan Palanki"
corresponding_author: "Michael J. Mitchell"

# === Source & metadata ===
source_type: pdf
s2_id: ""
date_added: 2026-06-02
ingested_date: 2026-06-02
ingest_version: 1
last_reviewed:

# === Classification ===
importance: 2
tier: TIER_3
tags: [genome-editing, base-editing, gene-therapy, genodermatosis, lipid-nanoparticle, commentary]
keywords: [in situ genome editing, cytosine base editor, mRNA-LNP, TGM1, ARCI, ichthyosis, transdermal delivery, skin stem cells]
domain: "cell biology"

# === Biomedical domain ===
tissue: [skin]
condition: [healthy]
disease_specific: [arci, ichthyosis]
species: [human, mouse]
hypoxia_relevant: false
contains_immune_cells: true
contains_myeloid: false

# === Technique ===
techniques: [base_editing, mRNA_LNP, laser_microablation, reflectance_confocal_microscopy, qPCR, DESI_mass_spectrometry]
n_samples:
n_cells_total:
integration_method: ""

# === Biology captured ===
key_cell_types: [keratinocytes, basal keratinocytes (skin stem cells)]
key_markers: [TGM1, TG1]
key_pathways: [cornified envelope formation, skin barrier function]

# === User project membership ===
projects: [skin]
priority: reference
read_status: read

# === HypoxiaVERSE-specific ===
hypoxiaverse_status: excluded
exclusion_reason: "Not hypoxia-related; dermatology / gene-therapy commentary"
data_availability: ""

# === Cross-references ===
code_url: ""
cited_by: []
---

## Problem

Rare genetic skin diseases (genodermatoses — epidermolysis bullosa, ichthyoses, ectodermal dysplasias) are individually uncommon but collectively affect millions, causing chronic pain, infection, dehydration, and lifelong barrier dysfunction with few options beyond symptomatic care. Most are monogenic, making them conceptually well suited to gene therapy — yet prior approaches relied on *gene augmentation* (adding a functional copy, e.g. the FDA-approved HSV-1 collagen-VII therapy Vyjuvek), which does not correct the underlying mutation, may disrupt physiological gene regulation, and often lacks durability or scalability. The formidable barrier properties of human skin further limit effective intervention. This Preview asks how the previewed study overcomes the twin challenges of editing precision and delivery to make true in situ genome correction of skin feasible.

## Key idea

This is a **Preview / commentary** in *Cell Stem Cell* (Palanki, Fitzgerald, Poirier & Mitchell) on the primary study by **Apaydin & Sadhnani et al.** (Cell Stem Cell 2026, 33:233–252.e12), which demonstrates in situ genome editing of human skin to correct the most common *TGM1* mutation underlying autosomal recessive congenital ichthyosis (ARCI). The commentary frames the work as requiring two coupled advances: (1) a precision cytosine base editor able to correct a single nucleotide in a conserved splice motif **without** bystander edits, and (2) a topical mRNA-LNP delivery system that, paired with transient laser-microablation barrier modulation, reaches and transfects the basal keratinocyte (skin stem cell) compartment for durable correction.

## Method

As a Preview, this paper reports no primary data of its own; it summarises and contextualises the previewed study:

- **Editor screening**: next-generation cytosine base editors engineered for precision; lead candidate **eTD-CBE** vs standard **BE4max-NG**, evaluated in ARCI patient-derived keratinocytes for on-target vs bystander editing at *TGM1* c.877-2A>G.
- **3D human ARCI skin model**: on-target gene-correction rate and restoration of wild-type TG1 enzyme activity.
- **Delivery**: topical mRNA-LNPs combined with **laser microablation** generating transient micropores into viable epidermis; pore depth controlled by non-invasive **reflectance confocal microscopy**; basal-keratinocyte transfection quantified.
- **Safety**: human skin explants, in vitro immune-cell models, and in vivo mouse studies; immunogenicity, local inflammation on repeat dosing, and biodistribution via in vivo imaging, qPCR, and DESI mass spectrometry; genomic safety via sgRNA-dependent and -independent off-target methods.

## Results

eTD-CBE achieved up to 26% on-target editing with no bystander editing in patient keratinocytes (vs ~20% at both target and bystander for BE4max-NG); in a 3D ARCI skin model it gave a 12% mean correction rate and restored ~30% of wild-type TG1 activity, likely sufficient to alleviate the most severe symptoms. Topical mRNA-LNPs plus laser microablation transfected 39.1% of basal keratinocytes. The platform showed minimal immunogenicity, no local inflammation on repeat dosing, and confinement of LNP/cargo to treated skin with limited systemic spread and a strong genomic safety profile.

## All claims (exhaustive)

- `[c01]` eTD-CBE: up to 26% on-target editing with no bystander editing in ARCI keratinocytes (vs BE4max-NG ~20% at both) (p.1) "eTD-CBE, achieved up to 26% editing at the target nucleotide in ARCI patient-derived keratinocytes with no editing at the bystander nucleotide" — confidence: high — type: quantitative — links: [[concepts/bystander-free-precision-base-editing]] [[foundations/cytosine-base-editor]] [[claims/etd-cbe-bystander-free-26-percent]]
- `[c02]` eTD-CBE: 12% mean on-target correction and 30% restoration of wild-type TG1 activity in a 3D ARCI skin model (p.1) "eTD-CBE mediated a 12% mean on-target gene correction rate and 30% restoration of wild-type TG1 enzyme activity" — confidence: high — type: quantitative — links: [[foundations/transglutaminase-1]] [[concepts/in-situ-genome-editing-skin]] [[claims/etd-cbe-restores-30-percent-tg1]]
- `[c03]` Topical mRNA-LNP + laser microablation transfects 39.1% of basal keratinocytes (skin stem cells) in a 3D ARCI skin model (p.1) "LNPs encapsulating base-editing cargos transfected 39.1% of basal keratinocytes (skin stem cells) in a three-dimensional ARCI skin model" — confidence: high — type: methodological — links: [[concepts/laser-microablation-transdermal-lnp-delivery]] [[foundations/mrna-lipid-nanoparticle]] [[claims/microablation-mrna-lnp-transfects-39-percent]]
- `[c04]` Topical mRNA-LNPs: minimal immunogenicity, no local inflammation on repeat dosing, confined to treated skin (p.2) "topically applied mRNA-LNPs showed minimal immunogenicity and no evidence of local inflammation, even after repeat administration ... both LNPs and genetic cargo remained confined to the treated skin with limited systemic dissemination" — confidence: high — type: mechanistic — links: [[foundations/mrna-lipid-nanoparticle]] [[claims/topical-mrna-lnp-low-immunogenicity-confined]]
- `[c05]` ~1/3 of ARCI cases are caused by TGM1 mutations; c.877-2A>G is the most common (splice-acceptor disruption) (p.1) "Approximately one-third of ARCI cases are caused by mutations in TGM1 ... The most common mutation in the TGM1 gene is c.877-2A>G, which disrupts a canonical splice acceptor site" — confidence: high — type: correlational — links: [[foundations/transglutaminase-1]] [[foundations/autosomal-recessive-congenital-ichthyosis]] [[claims/tgm1-mutations-cause-one-third-arci]]

## Discussion captured

### Authors' interpretation

The commentary authors (Palanki et al.) interpret the previewed work as advancing therapeutic genome editing in three ways: it is one of the clearest demonstrations to date that in situ genome editing of human skin is feasible, precise, and functionally meaningful using a non-viral, topically applied delivery system; it highlights the therapeutic value of targeting skin stem cells directly rather than relying on transient correction of differentiated cells or ex vivo grafting; and it underscores the value of 3D human tissue models for evaluating editing strategies in complex tissues. They stress that the "central innovation lies not in the editor itself but in its delivery."

### Comparisons with prior literature (made by authors)

- **Vyjuvek (beremagene geperpavec)** — FDA-approved topical HSV-1 gene-augmentation therapy delivering collagen VII for dystrophic epidermolysis bullosa (ref 6); contrasted as augmentation, not correction.
- LNP-mediated in vivo editing previously demonstrated in **muscle** (Kenjo et al. Nat Commun 2021, ref 8), **eye/cornea** (Mirjalili Mohanna et al. J Control Release 2022, ref 9), and **brain** (Palanki et al. ACS Nano 2023, ref 10) — skin had lagged behind.
- Reviews of genodermatosis genetics and gene-editing challenges (De Stefano & Christiano 2014, ref 2; Uitto 2012, ref 3; Morren et al. 2022, ref 4; Piñón Hofbauer et al. 2024, ref 7).

### Mechanistic hypotheses proposed

- "A modular platform that integrates barrier modulation with LNP-mediated delivery of precision genome editors could, in principle, be adapted to hundreds of genodermatoses" (p.2) — generalisation hypothesis beyond the single *TGM1* mutation.
- Targeting basal keratinocytes (skin stem cells) implies "a durable and potentially curative treatment" (p.1).

### Caveats and self-criticism

The commentary explicitly lists remaining gaps: the need to test the platform in a more disease-relevant model using primary patient cells rather than immortalised human cells; to confirm durability of TGM1 enzyme restoration beyond the 48 h studied; to analyse competitive dynamics of corrected vs uncorrected skin stem cells; and, translationally, to extend efficacy to greater surface areas since target diseases typically affect the whole body.

### Future directions suggested

- Validate in primary patient-cell / in vivo disease-relevant models.
- Establish long-term durability of restored TG1 activity (>48 h).
- Study competitive dynamics between corrected and uncorrected stem cells.
- Scale delivery to large body-surface areas; extend the modular platform across the genodermatosis spectrum.

## Limitations

- This is a secondary Preview/commentary, not primary research; all quantitative claims are relayed from Apaydin & Sadhnani et al. and inherit that paper's scope.
- Previewed evidence is largely in vitro / 3D skin model and immortalised human cells; durability confined to 48 h; surface-area scaling untested.
- Peripheral to this wiki's hypoxia/cancer/immunology core — ingested for the genome-editing and skin-delivery methodology.

## Open questions

### Open questions raised by authors

- Does the approach work in primary patient cells and a disease-relevant in vivo model?
- Is restored TG1 enzyme activity durable beyond 48 h?
- What are the competitive dynamics of corrected vs uncorrected skin stem cells?
- Can efficacy be extended to whole-body surface areas?

### Open questions identified during ingest

- How comprehensively was bystander-free editing validated under genome-wide off-target profiling?
- How transferable is the barrier-modulation + LNP platform to other genodermatosis loci with different mutation classes (deletions, large rearrangements) not amenable to base editing?
- What is the manufacturing / regulatory path for a combined device (laser microablation) + biologic (mRNA-LNP editor) therapy?

## My take

A clear, well-structured Preview that crystallises *why* the previewed study matters: the bottleneck for skin gene therapy was never just the editor but reaching the stem-cell compartment behind the barrier, and the laser-microablation + topical mRNA-LNP route is the transferable advance. For this wiki it is peripheral (no hypoxia/cancer link), but it seeds reusable methodology pages — cytosine base editing, mRNA-LNP delivery, and bystander-free splice-site correction — that may recur. Treat the numbers as secondhand until the primary paper is ingested.

## Related

- [[concepts/in-situ-genome-editing-skin]]
- [[concepts/laser-microablation-transdermal-lnp-delivery]]
- [[concepts/bystander-free-precision-base-editing]]
- [[foundations/cytosine-base-editor]]
- [[foundations/mrna-lipid-nanoparticle]]
- [[foundations/transglutaminase-1]]
- [[foundations/autosomal-recessive-congenital-ichthyosis]]
- [[people/rohan-palanki]]
- [[people/michael-mitchell]]
