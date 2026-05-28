---
# === Identification ===
title: "The transition from monocyte to tissue-resident macrophage requires DHPS"
slug: transition-monocyte-tissue-resident-macrophage-requires
arxiv: ""
doi: "10.1038/s41586-025-09972-2"
pmid: "41565804"
venue: "Nature"
year: 2026
authors:
  - "Gustavo E. Carrizo"
  - "Pianpian Lin"
  - "Seung Hyun Lee"
  - "Kevin Shenderov"
  - "Camille Blériot"
  - "Minsun Cha"
  - "Lena Schimmelpfennig"
  - "Zhen Shen"
  - "Nikki van Teijlingen Bakker"
  - "Katarzyna M. Grzes"
  - "Beth Kelly"
  - "Niloufar Safinia"
  - "Kate L. Schole"
  - "Yaarub Musa"
  - "Gerhard Mittler"
  - "Yoh Zen"
  - "Edward J. Pearce"
  - "Florent Ginhoux"
  - "David E. Sanin"
  - "Daniel J. Puleston"
  - "Erika L. Pearce"
first_author: "Gustavo E. Carrizo"
corresponding_author: "Daniel J. Puleston; Erika L. Pearce"

# === Source & metadata ===
source_type: pdf
s2_id: "db56cfd9011a24741152b248b8623d45e8f54b94"
date_added: 2026-05-28
ingested_date: 2026-05-28
ingest_version: 1
last_reviewed:

# === Classification ===
importance: 4
tier: TIER_1
tags:
  - macrophage
  - tissue-resident-macrophage
  - immunometabolism
  - polyamine
  - hypusine
  - eIF5A
  - translation
  - monocyte
keywords:
  - DHPS
  - deoxyhypusine synthase
  - eIF5A hypusination
  - tissue-resident macrophage
  - monocyte differentiation
  - cell adhesion
domain: immunology

# === Biomedical domain ===
tissue: [lung, liver, kidney, bone_marrow, blood, multi]
condition: [healthy]
disease_specific: []
species: [mouse]
hypoxia_relevant: false
contains_immune_cells: true
contains_myeloid: true

# === Technique ===
techniques: [scRNA-seq_10x, bulk_RNA-seq, flow_cytometry, proteomics, RiboTag, parabiosis, clodronate_depletion, confocal_imaging, immunofluorescence]
n_samples:
n_cells_total:
integration_method: ""

# === Biology captured ===
key_cell_types:
  - tissue-resident macrophages
  - monocyte-derived macrophages
  - alveolar macrophages
  - Kupffer cells
  - microglia
  - kidney macrophages
  - peritoneal macrophages
key_markers:
  - DHPS
  - eIF5A
  - TIM-4 (Timd4)
  - Siglec-F
  - CX3CR1
  - F4/80
  - CD64
  - CD11b
  - CD11c
  - ST2 (Il1rl1)
  - L1CAM
  - E-cadherin (Cdh1)
  - Tnik
key_pathways:
  - polyamine-hypusine-eIF5A axis
  - cell adhesion
  - integrin-mediated signalling
  - Wnt/β-catenin
  - IL-33/ST2 signalling
  - efferocytosis

# === User project membership ===
projects: [thesis]
priority: context
read_status: not_read

# === HypoxiaVERSE-specific ===
hypoxiaverse_status:
exclusion_reason:
data_availability: ""

# === Cross-references ===
code_url: ""
cited_by: []
---

## Problem

Tissue-resident macrophages (RTMs) are seeded embryonically and self-renew locally, but during damage bone-marrow-derived monocytes enter tissues and differentiate into RTMs. The cell-intrinsic mechanisms that control the monocyte-to-RTM transition — and that maintain mature RTMs — *across tissues* (i.e. irrespective of tissue-specific identity factors such as GM-CSFR or GATA-6) were unknown.

## Key idea

The polyamine spermidine fuels [[foundations/deoxyhypusine-synthase-dhps]]-mediated hypusination of the translation factor [[foundations/eif5a-hypusine]], and this hypusine-eIF5A axis is a tissue-agnostic, cell-intrinsic requirement for monocytes to become mature RTMs and for mature RTMs to persist. Mechanistically, hypusinated eIF5A is needed to efficiently translate a subset of cell-adhesion and signalling mRNAs that underpin tissue residency. See [[concepts/polyamine-hypusine-axis-macrophage-residency]] and [[concepts/eif5a-selective-translation-cell-adhesion-mrnas]].

## Method

Myeloid-specific DHPS deletion (Dhps-ΔM = Dhps^flx/flx [[foundations/lysm-cre]], Rosa26-eYFP reporter) and inducible deletion in mature RTMs ([[foundations/cx3cr1-creer-fate-mapping]]). Multi-tissue flow cytometry and imaging; [[foundations/parabiosis]] and competitive bone-marrow chimeras to assess monocyte contribution vs self-renewal; [[foundations/clodronate-liposomes]] depletion-replenishment assays; [[foundations/scrna-seq-10x-chromium]] of peritoneal and lung macrophages; global proteomics; bulk RNA-seq across three tissues; [[foundations/ribotag-ribosome-profiling]] to read the macrophage translatome; functional adhesion (EDTA detachment), morphology (confocal/Imaris) and efferocytosis assays.

## Results

DHPS deletion does not abolish macrophage generation but causes a global loss of mature RTMs across peritoneum, lung, liver, heart, brain, spleen and kidney, with persistent futile monocytic influx. Parabiosis and chimeras show DHPS-deficient niches lose self-maintenance. DHPS-deficient macrophages proliferate less and die more. scRNA-seq reveals expansion of immature monocyte-derived states and loss of mature Timd4+ RTMs; proteomics, bulk RNA-seq and RiboTag converge on a downregulated cell-adhesion/signalling program (e.g. ST2/Il1rl1, Tnik, L1CAM, E-cadherin). Functionally, the cells are less adherent, morphologically altered, defective in efferocytosis, and fail to maintain lung (alveolar proteinosis) and liver homeostasis.

## All claims (exhaustive)

- `[c01]` DHPS is required for RTM differentiation and maintenance across tissues (abstract) "deoxyhypusine synthase (DHPS)... is required for RTM differentiation and maintenance" — confidence: high — type: mechanistic — links: [[concepts/polyamine-hypusine-axis-macrophage-residency]] [[foundations/deoxyhypusine-synthase-dhps]] [[claims/dhps-required-rtm-differentiation-maintenance]]
- `[c02]` Myeloid DHPS deletion causes a global RTM defect across ≥7 tissues (p.3) "Dhps-ΔM Rosa26eYFP mice exhibited substantial defects in RTMs in the peritoneum (TIM-4+), lung (Siglec-F+), liver (TIM-4+), heart (TIM-4+), brain (CX3CR1+), spleen (TIM-4+) and kidney" — confidence: high — type: correlational — links: [[foundations/tim-4-timd4]] [[foundations/siglec-f-eosinophil-marker]] [[claims/dhps-deletion-global-rtm-defect-across-tissues]]
- `[c03]` DHPS is dispensable for initial macrophage development but required for residency acquisition (Discussion) "DHPS deletion permits initial macrophage development but prevents these cells from taking up residence in tissues" — confidence: high — type: mechanistic — links: [[foundations/csf1r-receptor]] [[claims/dhps-dispensable-initial-macrophage-development]]
- `[c04]` Loss of mature RTMs drives persistent but futile monocytic influx (abstract) "resulting in persistent but ultimately futile monocyte influx" — confidence: high — type: mechanistic — links: [[concepts/macrophage-ontogeny-resident-vs-monocyte-derived]] [[claims/dhps-loss-drives-futile-monocyte-influx]]
- `[c05]` Parabiosis shows DHPS-deficient niches are replenished by WT monocytes (p.3) "among the WT:Dhps-ΔM mice, RTM niches in the Dhps-ΔM mice comprised cells from the WT parabiont" — confidence: high — type: methodological — links: [[foundations/parabiosis]] [[claims/parabiosis-dhps-niches-monocyte-replenished]]
- `[c06]` In competitive chimeras, DHPS-deficient monocytes fail to repopulate RTM pools (p.3) "monocytes from CD45.2+ Dhps-ΔM bone marrow precursors failed to repopulate RTM pools in irradiated WT recipient mice" — confidence: high — type: methodological — links: [[claims/dhps-monocytes-fail-repopulate-chimera]]
- `[c07]` After clodronate depletion, DHPS-deficient monocytes enter but fail to re-establish mature RTMs (p.3) "monocytes entered and differentiated into a persistent population of CD64+CD11c+ macrophages but failed to re-establish the local SIGLEC-F+CD11blow lung RTM pool" — confidence: high — type: methodological — links: [[foundations/clodronate-liposomes]] [[claims/dhps-fails-reestablish-rtm-post-clodronate]]
- `[c08]` DHPS-deficient macrophages show less proliferation and more death (p.4) "DHPS-deficient macrophages expressed less Ki-67 and more active caspase-3" — confidence: high — type: correlational — links: [[claims/dhps-macrophages-reduced-proliferation-increased-death]]
- `[c09]` Inducible deletion in mature RTMs causes their loss (maintenance requirement) (p.5) "Kidney RTMs were lost by day 45 post-tamoxifen... mature RTMs rely on DHPS for persistence" — confidence: high — type: mechanistic — links: [[foundations/cx3cr1-creer-fate-mapping]] [[claims/dhps-required-mature-rtm-persistence]]
- `[c10]` scRNA-seq shows reduced Timd4+ RTMs and expanded immature monocyte-derived clusters (p.5) "diminished frequency of canonical, mature RTMs in Dhps-ΔM mice as defined by Timd4 expression (cluster 3)" — confidence: high — type: correlational — links: [[foundations/scrna-seq-10x-chromium]] [[claims/scrna-dhps-reduced-timd4-expanded-immature]]
- `[c11]` The DHPS-deficient immature block has a tissue-independent signature (p.6) "these cells failed to acquire the RTM signature imposed by the tissue and remained as immature macrophages" — confidence: high — type: mechanistic — links: [[claims/dhps-block-immature-transitional-state-tissue-independent]]
- `[c12]` Proteomics shows decreased adhesion/integrin signalling/metabolism and increased inflammation (p.6) "significant decreases in metabolism, cell adhesion and integrin-mediated signalling pathways, along with increases in immune activation and inflammation" — confidence: high — type: correlational — links: [[claims/dhps-proteomics-decreased-adhesion-increased-inflammation]]
- `[c13]` RiboTag identifies 13 ribosome-depleted transcripts enriched for adhesion/signalling/apoptosis (p.7) "13 genes that were significantly reduced on ribosomes... included Icos, Cd28, Axin2, Tnik, Amigo2, Fam83g, Il1rl1, Rab44 and Oasl1" — confidence: high — type: methodological — links: [[foundations/ribotag-ribosome-profiling]] [[concepts/eif5a-selective-translation-cell-adhesion-mrnas]] [[claims/ribotag-13-transcripts-reduced-dhps]]
- `[c14]` ST2 (Il1rl1) is hypusine-dependent; reduced ST2 impairs IL-33 alternative activation (p.7) "ST2 was decreased on peritoneal macrophages from Dhps-ΔM mice, and... the ability of these macrophages to alternatively activate in response to IL-33 in vitro was impaired" — confidence: medium — type: mechanistic — links: [[foundations/st2-il1rl1-il33-receptor]] [[claims/st2-il1rl1-hypusine-dependent-il33-response-impaired]]
- `[c15]` Bulk RNA-seq across three tissues: adhesion/signalling/migration genes most downregulated (p.7-9) "pathways of cell adhesion, signalling and migration as the most significantly downregulated" — confidence: high — type: correlational — links: [[claims/bulk-rnaseq-adhesion-signalling-downregulated-dhps]]
- `[c16]` L1CAM and E-cadherin (Cdh1) downregulated at transcript and protein level (p.9) "genes encoding cell adhesion molecules L1CAM and E-cadherin (l1cam and Cdh1)... were downregulated... consistent with the finding of decreased protein expression" — confidence: high — type: correlational — links: [[foundations/tnik-kinase]] [[claims/l1cam-ecadherin-downregulated-dhps]]
- `[c17]` DHPS-deficient macrophages detach much faster (functional adhesion defect) (p.9) "approximately 50% of the cells detaching after 2 min, compared with fewer than 10% of control cells" — confidence: high — type: quantitative — links: [[claims/dhps-macrophages-reduced-adhesion-edta]]
- `[c18]` DHPS-deficient macrophages show altered morphology and reduced tissue interaction (p.9) "larger with a different pattern of localization in the alveoli, that is, less stromal cell overlap... larger and more spherical" — confidence: high — type: correlational — links: [[claims/dhps-macrophages-altered-morphology-tissue-interaction]]
- `[c19]` DHPS-deficient macrophages are defective in efferocytosis (p.9-10) "reduced dead cell uptake and Cypher5E fluorescence... Dhps-ΔM mice had significantly more sRBCs in the circulation after 90 min" — confidence: high — type: mechanistic — links: [[concepts/efferocytosis-anti-inflammatory-clearance]] [[claims/dhps-macrophages-defective-efferocytosis]]
- `[c20]` Loss of functional alveolar macrophages causes alveolar proteinosis and lung infiltration (p.10) "BAL fluid from Dhps-ΔM mice demonstrated alveolar proteinosis that worsened over time... increased presence of CD45+ cells" — confidence: high — type: correlational — links: [[claims/dhps-alveolar-proteinosis-lung-inflammation]]
- `[c21]` Myeloid DHPS is required to restore liver homeostasis after depletion (p.10) "livers of Dhps-ΔM mice exhibited congestion... abnormal sinusoids... and extensive necrosis" — confidence: high — type: mechanistic — links: [[foundations/kupffer-cells]] [[claims/dhps-required-liver-homeostasis-post-depletion]]
- `[c22]` Model: CSF1R drives initial development; the polyamine–hypusine pathway determines tissue occupancy (Discussion) "CSF1R signalling drives the initial macrophage program, and then the polyamine–hypusine pathway determines subsequent tissue occupancy" — confidence: medium — type: mechanistic — links: [[concepts/polyamine-hypusine-axis-macrophage-residency]] [[claims/csf1r-initial-program-hypusine-tissue-occupancy-model]]

## Discussion captured

### Authors' interpretation

The authors propose that monocyte interaction within a tissue is a primary driver of RTM differentiation, and that the polyamine–hypusine axis is a cell-intrinsic node supporting expression of the cell-adhesion and signalling molecules required for the monocyte–macrophage tissue relationship. DHPS-deficient monocytes remain as immature monocyte-derived macrophages (a state normally seen only during damage) and consequently lack homeostatic functions and cannot maintain tissue homeostasis.

### Comparisons with prior literature (made by authors)

- Prior work from the group: hypusinated eIF5A boosts respiration and macrophage alternative activation (Puleston et al., *Cell Metab.* 2019); polyamine metabolism governs T-helper lineage fidelity (Puleston et al., *Cell* 2021).
- DHPS in myeloid inflammation: suppresses inflammatory macrophage accumulation in obese adipose tissue (Anderson-Baucum et al., *Cell Metab.* 2021) and controls antimicrobial translation (Gobert et al., *Cell Rep.* 2020).
- eIF5A elongation/termination roles (Schuller et al., *Mol. Cell* 2017; Saini et al., *Nature* 2009).
- Tissue-specific RTM identity factors GM-CSFR and GATA-6 (Guilliams 2013; Rosas 2014).

### Mechanistic hypotheses proposed

- Hypusinated eIF5A is required to translate stall-prone (e.g. proline-rich) transcripts; TNIK is proline-rich and ST2 has diproline motifs, potentially conferring hypusine dependency (p.10).
- Specific transcription/chromatin factors might themselves be hypusine-dependent, such that the entire RTM transcriptional program (including adhesion/signalling) is never enacted (p.11).

### Caveats and self-criticism

- Which exact motifs require hypusinated eIF5A is "not completely clear"; transcriptional vs translational contributions to protein deficits are hard to disentangle.
- ST2's contribution may be peritoneum-specific and "may not be important for the RTM transition in other tissues"; multiple genes, not one, likely drive the phenotype.
- A recent report that spermidine reduces RIPK1 activation in a DHPS-dependent manner leaves open whether proteins other than eIF5A are hypusinated.

### Future directions suggested

- Determine which transcripts in macrophages are hypusine-eIF5A-dependent and drive in vivo tissue behaviour.
- Investigate how extracellular and intracellular polyamine levels gate hypusine synthesis in health and disease.
- Explore whether other proteins are modified by the polyamine–hypusine axis, and implications for therapeutic macrophage targeting and ageing.

## Limitations

- Entirely mouse-based; human relevance inferred, not tested.
- Several key omics datasets are single experiments with three biological replicates.
- Synthetic-tex ingest source (PDF-derived) means figure-panel statistics are read from extracted text, not the original layout.

## Open questions

### Open questions raised by authors

- Which mRNA motifs confer hypusine dependency beyond polyproline?
- How do polyamine levels in a cell influence hypusine and translation across biological contexts?
- Are proteins other than eIF5A modified by the polyamine–hypusine axis?

### Open questions identified during ingest

- Can pharmacological DHPS/eIF5A modulation be used to reshape resident-macrophage pools therapeutically (e.g. in fibrosis, ageing, tumour TAMs)?
- Does the same translational block operate in tumour-associated macrophages, given the wiki's heavy TAM focus?

## My take

The conceptual advance is reframing RTM tissue residency as partly a *translational* decision gated by a metabolite (spermidine → hypusine). The RiboTag experiment is the linchpin: by reading the translatome rather than the transcriptome, the authors localize the defect to translation of adhesion/signalling messages. For the macrophage-ontogeny axis already in this wiki, this supplies a cell-intrinsic mechanism complementary to the developmental-origin framing.

## Related

- [[concepts/macrophage-ontogeny-resident-vs-monocyte-derived]] — supplies the developmental-origin framework this mechanism acts within.
- [[concepts/polyamine-hypusine-axis-macrophage-residency]] — the central concept introduced.
- [[concepts/eif5a-selective-translation-cell-adhesion-mrnas]] — the translational-control mechanism.
- [[papers/physiology-diseases-tissue-resident-macrophages]] — canonical RTM ontogeny review (Lazarov & Geissmann 2023).
- [[papers/metabolism-tissue-macrophages-homeostasis-pathology]] — RTM metabolic programming context.
