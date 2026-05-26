---
# === Identification ===
title: "Metabolism of tissue macrophages in homeostasis and pathology"
slug: metabolism-tissue-macrophages-homeostasis-pathology
arxiv: ""
doi: "10.1038/s41423-021-00791-9"
pmid: "34876704"
venue: "Cellular & Molecular Immunology"
year: 2022
authors:
  - "Stefanie K. Wculek"
  - "Gillian Dunphy"
  - "Ignacio Heras-Murillo"
  - "Annalaura Mastrangelo"
  - "David Sancho"
first_author: "Stefanie K. Wculek"
corresponding_author: "David Sancho"

# === Source & metadata ===
source_type: pdf
s2_id: "44b49f0f73f9475409ff766d026792ef903c44a3"
date_added: 2026-05-26
ingested_date: 2026-05-26
ingest_version: 1
last_reviewed: null

# === Classification ===
importance: 4
tier: TIER_1
tags:
  - macrophage
  - immunometabolism
  - tissue-resident-macrophage
  - alveolar-macrophage
  - kupffer-cell
  - red-pulp-macrophage
  - microglia
  - osteoclast
  - peritoneal-macrophage
  - efferocytosis
  - itaconate
  - hif1a
  - pparg
  - lxr
  - spi-c
  - nrf2
  - iron-metabolism
  - lipid-metabolism
  - fibrosis
  - regeneration
  - review
keywords:
  - tissue macrophage metabolism
  - immunometabolism
  - M1 / M2 paradigm
  - itaconate IRG1
  - succinate HIF-1α
  - PPARγ alveolar macrophage
  - SPI-C NRF2 BACH1 iron axis
  - Kupffer cell metabolism
  - GATA6 / RXR / C/EBPβ peritoneal macrophage
  - microglia OXPHOS glutamine
  - osteoclast HIF-1α glycolysis
  - efferocytosis UCP2 DRP1
  - HIF-independent M2 transition regeneration
  - AMPKα1 tissue regeneration
  - IPF AM MCU PGC-1α
domain: "immunology / immunometabolism / cell biology"

# === Biomedical domain ===
tissue:
  - lung
  - liver
  - spleen
  - peritoneum
  - bone_marrow
  - brain
  - kidney
  - adipose
  - heart
  - skeletal_muscle
  - intestine
  - multi
condition:
  - healthy
  - cancer
  - autoimmune
  - inflam_precancer
disease_specific:
  - alveolar_proteinosis
  - idiopathic_pulmonary_fibrosis
  - atherosclerosis
  - metabolic_syndrome
  - obesity_insulin_resistance
  - systemic_lupus_erythematosus
  - rheumatoid_arthritis
  - mycobacterium_tuberculosis_infection
  - myocardial_infarction
  - skeletal_muscle_injury
species:
  - human
  - mouse
hypoxia_relevant: true
contains_immune_cells: true
contains_myeloid: true

# === Technique ===
techniques:
  - review
  - synthesis
n_samples: null
n_cells_total: null
integration_method: ""

# === Biology captured ===
key_cell_types:
  - tissue_resident_macrophage_TRM
  - alveolar_macrophage
  - interstitial_macrophage_lung
  - kupffer_cell
  - liver_capsular_macrophage
  - red_pulp_macrophage
  - marginal_zone_macrophage
  - marginal_metallophilic_macrophage
  - tingible_body_macrophage
  - erythroid_island_macrophage
  - large_peritoneal_macrophage
  - small_peritoneal_macrophage
  - microglia
  - osteoclast
  - kidney_resident_macrophage
  - WAT_resident_macrophage
  - cardiac_macrophage
  - skeletal_muscle_macrophage
  - intestinal_lamina_propria_macrophage
  - bone_marrow_derived_macrophage_BMDM
key_markers:
  - PPARG
  - LXRA
  - LXRB
  - SPI-C
  - NRF2
  - BACH1
  - HMOX1
  - ferroportin
  - ferritin
  - CD163
  - LRP1
  - GATA6
  - RXRA
  - RXRB
  - CEBPB
  - BACH2
  - SREBP1
  - SREBP2
  - VHL
  - HIF1A
  - HIF2A
  - IRG1
  - ACOD1
  - itaconate
  - succinate
  - IDH1
  - SDH
  - PDK
  - PGC-1β
  - PGC-1α
  - SLC1A5
  - c-Myc
  - mTOR
  - AMPKα1
  - UCP2
  - DRP1
  - DNM1L
  - PPARδ
  - CD36
  - GPR18
  - resolvin D2
  - arginase-1
  - iNOS
  - MCU
key_pathways:
  - M1-glycolysis-Warburg
  - M2-OXPHOS-FAO-glutaminolysis
  - TCA-cycle-breaks-citrate-itaconate-succinate
  - PPARγ-lipid-catabolism-alveolar-macrophage
  - LXRα-cholesterol-marginal-zone-macrophage
  - SPI-C-NRF2-BACH1-HO-1-iron-recycling
  - GATA6-RXR-CEBPβ-LPM-identity
  - osteoclast-OXPHOS-to-glycolysis-bone-exposure
  - microglia-glucose-glutamine-mTOR-switch
  - efferocytosis-UCP2-DRP1-FAO-PPARδ
  - AMPKα1-anti-inflammatory-regeneration
  - HIF-independent-M2-transition-muscle-regeneration
  - IPF-AM-MCU-PGC-1α-FAO

# === User project membership ===
projects:
  - thesis
  - hypoxia
priority: core
read_status: read

# === HypoxiaVERSE-specific ===
hypoxiaverse_status: included
exclusion_reason: null
data_availability: ""

# === Cross-references ===
code_url: ""
cited_by: []
---

## Problem

In-vitro macrophage immunometabolism is well-characterized — M1 cells reprogram to glycolysis with TCA-cycle breaks, M2 cells lean on OXPHOS/FAO/glutaminolysis. But macrophages in vivo occupy a vast diversity of tissue niches (lung, spleen, liver, peritoneum, brain, bone, kidney, fat, heart, gut), each with distinct fuels, oxygen tensions, and functional demands. The metabolic programs that actually run in these tissue-resident macrophage (TRM) populations — and how they support homeostatic functions or are perturbed in disease — were scattered across an organ-by-organ literature with no unified synthesis. This review aims to provide that synthesis and to argue that **tissue-instructed metabolism is a co-determinant of macrophage identity**, not just a downstream consequence of polarization.

## Key idea

Tissue-resident macrophages run **tissue-specific metabolic programs** that are tightly coupled to their lineage-determining transcription factors (PPARγ in alveolar macs, SPI-C in red pulp, GATA6 in LPMs, etc.) and to the metabolic resources of their niche: surfactant lipid in the lung, heme-iron in spleen/liver, mineralized bone in osteoclasts, glutamate in the peritoneum, fluctuating glucose/glutamine in the brain. These programs serve dual functions: they **execute the cell's homeostatic task** (surfactant clearance, iron recycling, bone resorption, neuronal support) and they **stabilize the cell's identity** (metabolic deficiencies cause loss of TRM number and function). The in-vitro M1/M2 paradigm captures only one slice of this picture — proinflammatory activation does install Warburg-like glycolysis with itaconate/succinate-driven HIF-1α stabilization (the canonical "TCA-cycle break" model), but tissue context dominates the baseline. Crucially, in tissue regeneration (muscle injury, MI) the macrophage transition from proinflammatory to resolutive state takes place in a hypoxic niche but is **HIF-independent**; AMPKα1, PPARδ/γ, efferocytosis-driven FAO, and macrophage-secreted glutamine are the actual drivers. Pathology (alveolar proteinosis, atherosclerosis, IPF, insulin resistance, kidney inflammation) frequently presents as **metabolic dysregulation of specific TRM populations**, identifying their metabolism as a therapeutic target.

## Method

This is a *Review* article, not primary research. The authors:

- Curate the in-vitro M1/M2 immunometabolism literature (LPS/IFNγ vs IL-4/IL-13 BMDMs) as a reference point.
- Synthesize organ-by-organ TRM metabolic profiles (Table 1) covering 17 macrophage populations across 11 organ systems, with ontogeny, markers, functions, and metabolic features.
- Present three integrative figures: Fig. 1 in-vitro M1/M2 vs in-vivo proinflammatory/anti-inflammatory; Fig. 2 lipid handling in alveolar, adipose-tissue, and atherosclerotic macrophages; Fig. 3 microenvironmental metabolic rewiring in RPMs (iron), LPMs (yeast/oxLDL/IL-4), osteoclasts (bone exposure).
- Discuss tissue-regeneration metabolic switches (skeletal muscle, MI) and unresolved fibrosis (IPF AMs).
- Cover adipose-tissue macrophage adaptations to overnutrition (truncated in the recovered PDF text but referenced in the abstract).

## Results

This is a synthesis, so "results" are the major crystallizations from the cited literature; atomic claims are itemized in `## All claims (exhaustive)`. Highlights:

1. **M1 macrophages introduce two TCA-cycle breaks** — IDH1 down → citrate/itaconate accumulation; itaconate ⊣ SDH → succinate accumulation → HIF-1α stabilization → sustained Warburg-like reprogramming.
2. **M2 macrophages depend on glutaminolysis-driven α-KG and OXPHOS/FAO**, with JMJD3 demethylation enabling the M2 transcriptional program; PPARγ, PPARδ, STAT6, IRF4 drive lipid handling.
3. **Alveolar macrophages are committed to lipid catabolism** via PPARγ (induced by GM-CSF/TGFβ), with LXRα/ABCG1, C/EBPβ, BACH2, VHL/HIF, and mTOR/SREBP all contributing to surfactant clearance.
4. **Red pulp and Kupffer macrophages run the SPI-C/NRF2/BACH1 iron-recycling axis** (HO-1, ferroportin, ferritin) alongside LXRα/PPARγ lipid-cholesterol handling. KCs depend specifically on LXRα for lineage identity (Notch-instructed); RPMs depend on PPARγ.
5. **Marginal zone and metallophilic macrophages depend on LXRα/β** for development and *immune clearance* function — a non-canonical, non-cholesterol-efflux role.
6. **LPMs are GATA6/RXR/C-EBPβ-identified lipid handlers** that use glutamate as tissue-niche fuel and recruit mitochondria to phagosomes during the respiratory burst.
7. **Microglia run baseline OXPHOS** with plastic glucose↔glutamine fuel switching under aglycemia (mTOR-dependent). Aging-driven PGE2/EP2 signalling sequesters glucose into glycogen, lowering bioenergetics and worsening neuroinflammation.
8. **Osteoclasts switch from OXPHOS/FAO/glutaminolysis (at rest, c-Myc/SLC1A5-driven) to HIF-1α-driven glycolysis upon bone exposure** to power resorption.
9. **Efferocytosis induces metabolic rewiring** — initial glycolysis then UCP2/DRP1-required mitochondrial FAO of corpse-derived lipids, with PPARδ/γ-driven anti-inflammatory programs.
10. **Tissue regeneration M2 transition is HIF-independent** — HIFs needed for proinflammatory infiltration but not the resolutive switch; AMPKα1, resolvin D2/GPR18, arginase-1, and macrophage-secreted glutamine drive resolution.
11. **Unresolved fibrosis (IPF) shows AMs locked in MCU/mtROS/PGC-1α-driven FAO**; reversal to glycolysis is protective preclinically. Itaconate/IRG1 is depleted in IPF AMs, and exogenous itaconate is antifibrotic.

## All claims (exhaustive)

Atomic claims, each with page (recovered PDF), exact quote, confidence, type, and links. TIER_1 review → 18 claims.

- `[c01]` M1 macrophage classical activation introduces two TCA-cycle breaks producing citrate, itaconate, and succinate accumulation (p.385) "two breaks within the TCA cycle [24, 25]. Isocitrate dehydrogenase (IDH)-1, the enzyme that converts isocitrate to α-ketoglutarate (αKG), is downregulated, allowing accumulation of citrate and synthesis of itaconate ... Itaconate inhibits succinate dehydrogenase (SDH; complex II of the ETC)... leading to the second break in the TCA cycle and succinate accumulation" — confidence: high — type: mechanistic — links: [[concepts/m1-macrophage-tca-breaks-itaconate-succinate]] [[foundations/itaconate-metabolite]] [[foundations/irg1-acod1]] [[claims/m1-macrophages-introduce-two-tca-breaks-citrate-itaconate-succinate]]
- `[c02]` Itaconate inhibits SDH, modulates M1 cytokines, and is antifibrotic in lung (p.385, p.393) "Itaconate has also been shown to modulate macrophage cytokine production independently of succinate accumulation ... Itaconate and its synthesizing enzyme immune-responsive gene 1 (IRG1) are reduced in AMs from idiopathic pulmonary fibrosis patients ... AMs lacking itaconate are more profibrotic ... itaconate administration is preclinically used for the treatment of fibrosis" — confidence: high — type: pharmacological — links: [[concepts/m1-macrophage-tca-breaks-itaconate-succinate]] [[foundations/itaconate-metabolite]] [[foundations/irg1-acod1]] [[claims/itaconate-inhibits-sdh-limits-inflammation-fibrosis]]
- `[c03]` Alveolar macrophage identity and function depend on PPARγ-driven lipid catabolism induced by GM-CSF and TGFβ (p.386) "AM development from embryonic progenitors is dependent on granulocyte-macrophage (GM)-CSF- and transforming growth factor (TGF)β-mediated induction of the signature transcription factor PPARγ, a master regulator of lipid metabolism ... PPARγ-deficient AMs are dramatically reduced in number and accumulate intracellular lipids due to reduced lipid catabolism and FAO" — confidence: high — type: mechanistic — links: [[concepts/alveolar-macrophage-lipid-catabolism-pparg]] [[foundations/pparg-tf]] [[claims/alveolar-macrophages-depend-on-pparg-lipid-catabolism-identity]]
- `[c04]` SPI-C and NRF2 induce HO-1, ferroportin, and ferritin in RPMs and Kupffer cells via heme-mediated BACH1 sequestration (p.389) "most genes involved in iron handling are induced by Spi-C and nuclear factor erythroid 2–related factor (NRF)2 transcription factors ... Intracellular iron or heme ... sequesters BACH1, resulting in the expression of genes required for iron metabolism, including heme oxygenase 1 (HO-1), ferroportin and ferritin" — confidence: high — type: mechanistic — links: [[concepts/spi-c-nrf2-iron-axis-rpm-kupffer]] [[foundations/spi-c-tf]] [[foundations/nrf2-nfe2l2]] [[foundations/bach1-tf]] [[foundations/ho-1-hmox1]] [[claims/spi-c-nrf2-induce-iron-recycling-program-rpm-kupffer]]
- `[c05]` LXRα/β control marginal-zone and metallophilic macrophage development and microbial clearance independent of reverse cholesterol transport (p.389) "the development of MZMs and MMMs is controlled by LXRα/β ... rather than involving regulation of reverse cholesterol transport, the function of LXRs in macrophages of the marginal zone is connected with their immune function and clearance of phagocytosed cargo, as LXRα/β-deficient mice exhibit increased susceptibility to infection due to defective microbe control" — confidence: high — type: mechanistic — links: [[concepts/lxr-marginal-zone-macrophage-clearance]] [[foundations/lxra-tf]] [[claims/lxr-controls-marginal-zone-macrophage-development-microbial-clearance]]
- `[c06]` Kupffer cells upregulate glucose uptake and PDK-dependent glycolysis upon immunogenic activation, losing IL-10 tolerogenic function (p.389) "Upon immunogenic activation, KCs upregulate glucose uptake and pyruvate dehydrogenase kinase (PDK)-dependent glycolytic metabolism, which diminishes their tolerogenic function of IL-10 production" — confidence: medium — type: mechanistic — links: [[concepts/tissue-specific-metabolic-programming-macrophages]] [[claims/kupffer-glycolytic-switch-on-activation-suppresses-il10-tolerance]]
- `[c07]` LPM differentiation, survival, and lipid handling require GATA6, RXRα/β, and C/EBPβ (p.390) "GATA6-deficient LPMs display an even further increased OCR ... C/EBPβ controls lipid metabolism-related genes in LPMs, and C/EBPβ-deficient LPMs exhibit striking upregulation of LXRα and PPARγ. Moreover, loss of RXRs in LPMs also results in an enhanced lipid metabolism signature and lipid accumulation ... all three transcription factors have been reported to be vital for murine LPM differentiation, survival, maturation and polarization" — confidence: high — type: mechanistic — links: [[concepts/lpm-gata6-rxr-cebp-lipid-identity]] [[foundations/gata6-tf]] [[foundations/c-ebp-beta]] [[claims/lpm-gata6-rxr-cebpb-required-for-lpm-identity]]
- `[c08]` LPMs recruit mitochondria to phagosomes for antimicrobial respiratory burst via glutaminolysis-driven ETC complex II induction (p.390) "Upon stimulation of LPMs with zymosan or yeast, mitochondria are recruited to phagosomes contributing to an antimicrobial respiratory burst, specifically via glutaminolysis-mediated induction of ETC complex II" — confidence: medium — type: mechanistic — links: [[concepts/lpm-gata6-rxr-cebp-lipid-identity]] [[claims/lpm-mitochondria-recruited-to-phagosomes-respiratory-burst]]
- `[c09]` oxLDL via CD36 reduces FAO/OXPHOS, repurposes ETC for ROS, then drives a glycolytic shift with NF-κB-driven inflammation in peritoneal macrophages (p.390) "exposure of thioglycolate-elicited murine SPMs and LPMs to a distinct class of stimulants such as CD36-binding oxidized low-density lipoprotein (oxLDL) results in reductions in FAO and OXPHOS and upregulation of glycolysis in concert with increased nuclear factor kappa-light-chain-enhancer of activated B cells (NF-κB) activation and inflammatory cytokine production ... oxLDL-induced inflammatory activation is in fact dependent on a primary repurposing of the ETC toward ROS and superoxide production" — confidence: medium — type: mechanistic — links: [[concepts/lpm-gata6-rxr-cebp-lipid-identity]] [[foundations/nf-kb-p65-rela]] [[claims/oxldl-cd36-shifts-peritoneal-macrophages-to-glycolysis-nfkb-inflammation]]
- `[c10]` Microglia switch from glucose to glutamine as OXPHOS substrate under aglycemia in an mTOR-dependent manner (p.390) "microglia have been shown to adjust to hypoglycemia/aglycemia and switch from glucose as their main fuel to glutamine to support their OXPHOS metabolism, a process requiring mTOR" — confidence: medium — type: mechanistic — links: [[concepts/microglia-metabolic-plasticity-bioenergetics]] [[foundations/mtor-kinase]] [[claims/microglia-switch-glucose-to-glutamine-mtor-dependent-aglycemia]]
- `[c11]` In aged microglia, PGE2/EP2 signalling sequesters glucose into glycogen, lowering bioenergetics and worsening neuroinflammation; EP2 blockade rescues memory (p.391) "During aging, the prostaglandin E2/EP2 signaling axis causes reduced glycolytic flux and OXPHOS in microglia via glucose sequestration into glycogen. Blocking the EP2 cascade rescues bioenergetics in microglia, ameliorates aging-associated neural inflammation and improves memory" — confidence: medium — type: mechanistic — links: [[concepts/microglia-metabolic-plasticity-bioenergetics]] [[claims/aging-microglia-pge2-ep2-axis-glycogen-sequestration-impairs-bioenergetics]]
- `[c12]` Osteoclastogenesis requires mitochondrial biogenesis and OXPHOS complex I fuelled by glutaminolysis through SLC1A5 and c-Myc (p.391) "this system seems to rely on mitochondrial biogenesis and OXPHOS, especially complex I of the ETC, which is regulated by iron uptake, PGC-1β and alternative NF-κB ... OXPHOS is likely fueled by glutaminolysis and controlled by c-Myc. This is evidenced by the upregulation of glutamine importer solute carrier family 1 member 5 (Slc1a5) and glutaminase-1 during osteoclastogenesis and the fact that glutamine withdrawal as well as inhibition of Slc1a5 or c-Myc reduces osteoclast differentiation" — confidence: high — type: mechanistic — links: [[concepts/osteoclast-bone-resorption-glycolytic-switch]] [[claims/osteoclastogenesis-requires-oxphos-complex-i-glutaminolysis-c-myc]]
- `[c13]` Active osteoclasts switch to HIF-1α-driven glycolysis and lactate production upon bone exposure to power resorption (p.391) "Activation of murine osteoclasts with bone powder does induce enhanced glycolytic activity compared to that in unstimulated cells, and the bone resorption activity of osteoclasts is driven by enhanced glycolysis, HIF-1α and lactate production ... the collagen degradation activity of human osteoclasts is diminished when the cells are cultured in the absence of glucose" — confidence: high — type: mechanistic — links: [[concepts/osteoclast-bone-resorption-glycolytic-switch]] [[foundations/hif1a]] [[claims/osteoclasts-switch-to-hif1a-glycolysis-on-bone-exposure-for-resorption]]
- `[c14]` Continuous efferocytosis requires UCP2-driven ΔΨm lowering and DRP1-driven mitochondrial fission (p.392) "mitochondrial uncoupling protein 2 and dynamin-related protein 1, which reduce the mitochondrial membrane potential and mitochondrial fission, respectively, were found to be required for effective and continuous efferocytosis by macrophages" — confidence: high — type: mechanistic — links: [[concepts/efferocytosis-metabolic-rewiring-fao]] [[foundations/ucp2-mitochondrial-uncoupler]] [[foundations/drp1-dnm1l]] [[claims/efferocytosis-requires-ucp2-drp1-mitochondrial-rewiring]]
- `[c15]` Catabolism of apoptotic cells fuels FAO and induces PPARδ/PPARγ-driven anti-inflammatory programs (p.392) "The catabolism of phagocytosed apoptotic cells by macrophages leads to an increase in the OCR fueled by FAO ... The significant external lipid substrate provided by apoptotic cells also increases the expression of PPARδ in macrophages, which increases opsonin expression and activates a transcriptional program required for apoptotic cell clearance and anti-inflammatory gene expression" — confidence: high — type: mechanistic — links: [[concepts/efferocytosis-metabolic-rewiring-fao]] [[foundations/pparg-tf]] [[claims/efferocytosis-induces-fao-and-pparg-ppard-anti-inflammatory-program]]
- `[c16]` Macrophage M2 transition during muscle regeneration occurs in a hypoxic niche but is HIF-independent (p.392) "the deletion of HIF does not affect the shift of macrophages toward an anti-inflammatory phenotype in the context of skeletal muscle regeneration ... tissue regeneration was not affected by HIF deletion in LysM-expressing cells in two models of muscle injury and was only slightly affected in a third model of mild tissue trauma. These observations imply that although the macrophage transition from a proinflammatory to a resolutive state takes place in a hypoxic environment, it is independent of HIFs" — confidence: medium — type: mechanistic — links: [[concepts/hif-independent-m2-transition-tissue-regeneration]] [[foundations/hif1a]] [[foundations/hif2a]] [[claims/m2-macrophage-transition-hif-independent-in-muscle-regeneration]]
- `[c17]` AMPKα1 in macrophages is required for the anti-inflammatory phenotype and skeletal muscle regeneration (p.392) "AMPK1α, a key metabolic enzyme that can enhance OXPHOS, increases its activity in macrophages shortly upon tissue injury and is essential for the anti-inflammatory phenotype of macrophages and appropriate muscle regeneration" — confidence: high — type: mechanistic — links: [[concepts/hif-independent-m2-transition-tissue-regeneration]] [[foundations/ampk-prkaa]] [[claims/macrophage-ampk-required-for-anti-inflammatory-phenotype-tissue-regeneration]]
- `[c18]` Macrophages synthesize and secrete glutamine to support satellite-cell growth during muscle regeneration; inhibiting macrophage glutamine oxidation improves regeneration (p.392) "macrophages synthesize and secrete glutamine to promote the growth of satellite cells and improve muscle regeneration. Furthermore, macrophage-targeted inhibition of glutamine oxidation by glutamine dehydrogenase-1 improves muscle regeneration in muscle injury and ischemia models" — confidence: medium — type: mechanistic — links: [[concepts/hif-independent-m2-transition-tissue-regeneration]] [[claims/macrophages-secrete-glutamine-to-support-satellite-cell-muscle-regeneration]]
- `[c19]` In idiopathic pulmonary fibrosis, alveolar macrophages shift to FAO via MCU/mtROS-driven PGC-1α; blockade reverses to glycolysis and protects from fibrosis (p.393) "AMs from fibrosis murine models first increase glycolysis and then switch metabolically to FAO ... The FAO increase is dependent on the mitochondrial calcium uniporter (MCU) and mtROS increase-driven expression of PGC-1α. Indeed, blockade of this mechanism in AMs causes metabolic reversal to glycolysis and protects mice from fibrosis" — confidence: medium — type: pharmacological — links: [[concepts/alveolar-macrophage-lipid-catabolism-pparg]] [[claims/idiopathic-pulmonary-fibrosis-alveolar-macrophages-shift-fao-mcu-mtros-pgc1a]]

## Discussion captured

### Authors' interpretation

The authors interpret the literature as supporting a unifying view: **macrophage cellular metabolism is not just a downstream consequence of polarization but a co-determinant of tissue-resident macrophage identity**. The in-vitro M1/M2 paradigm — while mechanistically rich (TCA breaks, itaconate, succinate-HIF, glutaminolysis-α-KG-JMJD3) — captures only one face of macrophage metabolism; **organ-specific metabolic programs are tightly entangled with lineage-determining transcription factors** (PPARγ-AM, SPI-C-RPM, GATA6-LPM, etc.), making metabolism and identity inseparable. The repeated motif is that **disease arises when this entanglement is broken**: PPARγ loss → alveolar proteinosis; HO-1 loss → splenic/hepatic macrophage collapse and hemolytic anemia; IRG1/itaconate loss in IPF → unrestrained fibrosis; LXRα/β loss → splenic-MZM-defective antimicrobial clearance. The authors argue this opens a therapeutic frontier: **targeted manipulation of macrophage cellular metabolism** for fibrosis, atherosclerosis, alveolar proteinosis, metabolic syndrome, and possibly cancer.

For tissue regeneration specifically, the authors stress that the dominant in-vitro mental model — "hypoxia → HIF → M1/M2 polarization" — is too simple: in vivo, the macrophage M1→M2 transition during muscle regeneration is **HIF-independent**, driven instead by AMPKα1, efferocytosis-induced FAO/PPARδ, resolvin D2/GPR18 lipid-mediator gradients, and arginase-1-driven collagen synthesis. HIFs matter for infiltration and the day-1 glycolytic burst, not for resolution itself.

### Comparisons with prior literature (made by authors)

- **In-vitro M1/M2 immunometabolism**: O'Neill & Pearce 2016 *J Exp Med* (ref 13) — foundational immunometabolism review; Tannahill 2013 *Nature* (refs 24, 25, 38) — succinate→HIF-1α; Mills 2016 *Cell* (ref 26) — itaconate as immunoregulator.
- **Tissue-resident macrophage diversity**: Lavin 2014 *Cell* and Gosselin 2014 *Cell* — tissue-instructed enhancer landscapes; Mass 2016 *Science* — EMP-derived TRM ontogeny.
- **PPARγ and alveolar macrophages**: Schneider 2014 (refs 66, 71, 72) — GM-CSF/PPARγ for AM; A-Gonzalez 2017 (ref 70) — lipid handling across TRM populations.
- **SPI-C/heme/iron axis**: Kohyama 2009, Haldar 2014 (refs 104, 105) — heme→SPI-C in RPMs; Bonnardel 2019 and Sakai 2019 (refs 7–8) — Notch/SPI-C/LXRα in Kupffer cells.
- **Osteoclast metabolism**: Indo 2013, Arnett 2003, Lemma 2017, Morten 2013, Go 2020 — bidirectional OXPHOS↔glycolysis switch with bone exposure.
- **Efferocytosis metabolism**: Park 2011 (UCP2, ref 154), Wang 2017 (DRP1, ref 155), Mukundan 2009 (PPARδ, ref 159).
- **Tissue regeneration HIF**: Lodge 2022 and others — LysM-Cre HIF1α/HIF2α conditional KO in muscle injury (refs 148, 149).
- **IPF AM metabolism**: Gu 2019 (MCU/PGC-1α, ref 168), Cui 2019 (itaconate/IRG1, ref 169), Tsitoura 2016 (iron, ref 170).

### Mechanistic hypotheses proposed

- **Tissue-niche-fuel hypothesis** (p.390 for LPMs, p.385–390 generally): each TRM is metabolically tuned to a specific local fuel (glutamate for LPMs, surfactant lipid for AMs, heme for RPMs/KCs, mineralized bone for osteoclasts).
- **Metabolism-as-identity hypothesis**: cellular metabolism is not a downstream readout of TRM identity but a co-constructor of it; disruption of metabolic enzymes/transcription factors collapses both metabolism and identity.
- **HIF-uncoupling-in-regeneration hypothesis**: hypoxia is present in the wound bed but does not drive the M2 transition; HIF effects are restricted to infiltration and the day-1 glycolytic burst.
- **Therapeutic-metabolic-targeting hypothesis** (p.393 for fibrosis): "targeted manipulation of cellular metabolism in macrophages is a promising target to increase the speed of wound healing and prevent inadequate tissue regeneration".

### Caveats and self-criticism

- Most metabolic data are **mouse-derived BMDM or in-vitro tissue-elicited cells**; in-situ TRM metabolic profiling in humans is sparse.
- For Kupffer/RPM lipid-cholesterol handling: "the actual metabolic activity of KCs or RPMs handling lipids and cholesterol or its relevance for the functions of these cells in homeostasis remains largely unclear" (p.389).
- Clinical translation has lagged: NAC and metformin in IPF show no benefit despite preclinical signal (p.393), because the strategies are not macrophage-directed.
- Coverage gap: tingible-body macrophage metabolism is essentially unstudied; intestinal-macrophage metabolism is mostly inferred from microbiota-derived butyrate signalling.

### Future directions suggested

- Targeted manipulation of macrophage cellular metabolism in fibrosis, atherosclerosis, and cancer.
- Better in-situ profiling of human TRM metabolism (the field is mostly murine and mostly in-vitro).
- Reconciliation of "metabolic activity" vs "metabolic signature" — many claims rest on transcriptomic gene-set enrichment rather than direct flux measurements.

## Limitations

This is a *Review*, not a primary study; conventional methodological limitations do not apply. Interpretive limitations:

- **Mouse-centric** — most cited TRM-metabolism evidence is murine; human TRM metabolism is inferred indirectly (IPF AMs, lupus KRMs, RA synovial macrophages).
- **In-vitro vs in-vivo gap** — much of the M1/M2 / itaconate / succinate-HIF model is from BMDM cultures; the review notes but does not fully resolve how much of this applies to tissue-resident macrophages in vivo.
- **Transcriptomic-signature-as-metabolism** — many "metabolic features" in Table 1 are gene-expression enrichments, not direct flux measurements.
- **Coverage** — peritoneal SPMs, tingible-body macrophages, intestinal subsets, cardiac TRM in homeostasis are underrepresented because the underlying primary literature is thin.
- **Truncated PDF extraction** — the recovered source text breaks off at the adipose-tissue overnutrition section, so atherosclerosis, MASH, obesity, and cancer-macrophage metabolism are present in the abstract/figures but not in the body text captured. The published article continues through these topics; ingest should be considered conservative.

## Open questions

### Open questions raised by authors

- The actual *flux* (not just transcriptomic signature) of lipid and cholesterol handling in KCs and RPMs and its homeostatic relevance (p.389).
- Whether observed metabolic shifts in M1/M2 polarization are causes or consequences of polarization (p.387 — discussed for FAO inhibitors in M2).
- Why clinical metabolic interventions in IPF (NAC, metformin) fail despite preclinical macrophage signal — i.e. translational gap (p.393).
- The metabolism of tingible-body macrophages and other understudied TRM subsets (Table 1 "to be investigated").
- Whether targeting macrophage metabolism is therapeutically tractable in fibrosis, atherosclerosis, and metabolic syndrome (p.393).

### Open questions identified during ingest

- How does the HIF-independent M2 transition during muscle regeneration interact with the canonical succinate→HIF-1α / itaconate axis of M1 polarization? If HIF is dispensable for resolution but central for M1 activation, what handles the "off-switch" of HIF-1α at day 2–3 after injury?
- The review notes that **macrophages produce growth factors under PPARγ control** for skeletal muscle regeneration — is this an in-vivo correlate of the [[papers/nf-kb-tet2-promote-macrophage-reprogramming]] PPARγ/TET2 axis or distinct?
- How does the SPI-C/NRF2/HO-1 iron-recycling program in RPMs/KCs interact with **hypoxia-driven changes** in iron handling (e.g. HIF stabilization by iron via IRP1, IDO/ferroptosis links)? The review hints at but does not detail this.
- For my own thesis context: **how does the in-vivo tissue-resident metabolic program of TAMs compare with the IPF-AM "FAO-locked" state**? Both involve macrophages in chronic, lipid-rich, hypoxic microenvironments; mechanistic parallels could be exploited.
- The clinical implication of itaconate/IRG1 depletion in IPF AMs maps onto the user's wiki: 4-OI (cell-permeable itaconate) is a TET2 inhibitor — does its antifibrotic action in IPF involve TET2-mediated macrophage reprogramming, connecting to the [[papers/nf-kb-tet2-promote-macrophage-reprogramming]] axis?

## My take

This is the single most useful **tissue-by-tissue immunometabolism synthesis** for biomedical macrophage research in 2022. For my thesis on hypoxic NF-κB-driven macrophage reprogramming, it serves three functions:

1. **Ground truth for what "macrophage metabolism" means in vivo**: the review repeatedly stresses that BMDM in-vitro M1/M2 patterns are not the whole story. Anyone (including me) extrapolating Calafell-2024-style BMDM hypoxia experiments to tissue-resident TAMs needs to read this carefully — tissue-imprinted PPARγ, LXRα, SPI-C, GATA6 programs may dominate or invert in-vitro predictions.

2. **Hypoxia-metabolism cross-talk catalogue**: VHL/HIF tunes AM lipid metabolism; HIF-1α stabilizes after succinate accumulation in M1; HIF-1α drives osteoclast resorption glycolysis; HIF-1α is *not* required for muscle-regeneration M2 transition. These context-specific hypoxia roles map directly onto the [[concepts/hif-bidirectional-regulation-programmed-cell-death]] and [[concepts/hif-cross-talk-pi3k-mtor-nfkb-erk-er-stress]] hubs and complement the in-vitro hypoxia work I am doing.

3. **Itaconate/IRG1 ↔ TET2 bridge**: itaconate's role as both an immunoregulator and a TET2 inhibitor (via 4-OI) suggests a metabolic loop coupling M1 polarization, NF-κB activation, and epigenetic reprogramming. My [[papers/nf-kb-tet2-promote-macrophage-reprogramming]] work intersects this loop at the TET2 step — the metabolic upstream (itaconate flux) is something I have not explicitly considered and should.

For the wiki: this paper is a TIER_1 anchor for **tissue-resident macrophage immunometabolism**. It complements [[papers/physiology-diseases-tissue-resident-macrophages]] (the ontogeny anchor) by adding the metabolic layer to the same TRM populations. The two reviews together form a clean two-pillar foundation: ontogeny + function in Lazarov 2023; metabolism + identity in Wculek 2022.

Reading note: the **"metabolism-as-identity"** framing is the conceptual gift here. It rhymes with the "ancillary cell" framing of Lazarov 2023 but extends it to the molecular level: it's not enough to say "alveolar macrophages clear surfactant"; the correct framing is "alveolar macrophages *are* lipid-catabolizing cells *because* their metabolism is PPARγ-instructed by their niche, and any pathology that breaks this metabolism collapses both identity and function."

## Related

- [[concepts/tissue-specific-metabolic-programming-macrophages]] — central concept this review introduces
- [[concepts/m1-macrophage-tca-breaks-itaconate-succinate]] — newly extracted concept
- [[concepts/alveolar-macrophage-lipid-catabolism-pparg]] — newly extracted concept
- [[concepts/spi-c-nrf2-iron-axis-rpm-kupffer]] — newly extracted concept
- [[concepts/lxr-marginal-zone-macrophage-clearance]] — newly extracted concept
- [[concepts/lpm-gata6-rxr-cebp-lipid-identity]] — newly extracted concept
- [[concepts/osteoclast-bone-resorption-glycolytic-switch]] — newly extracted concept
- [[concepts/microglia-metabolic-plasticity-bioenergetics]] — newly extracted concept
- [[concepts/efferocytosis-metabolic-rewiring-fao]] — newly extracted concept
- [[concepts/hif-independent-m2-transition-tissue-regeneration]] — newly extracted concept
- [[concepts/m1-m2-polarization-paradigm]]
- [[concepts/tissue-specific-lineage-determining-factors-macrophage]]
- [[concepts/macrophage-ontogeny-resident-vs-monocyte-derived]]
- [[concepts/kupffer-cell-iron-recycling]]
- [[concepts/efferocytosis-anti-inflammatory-clearance]]
- [[concepts/osteoclast-multinucleated-macrophage-bone]]
- [[concepts/csf1r-il34-csf2-trophic-axis]]
- [[concepts/hif-dependent-glycolysis-immune-cell-differentiation]]
- [[concepts/glutamine-asymmetric-metabolism-tumor-immune]]
- [[concepts/warburg-effect-hif1a-glycolytic-reprogramming]]
- [[foundations/pparg-tf]]
- [[foundations/lxra-tf]]
- [[foundations/gata6-tf]]
- [[foundations/spi-c-tf]]
- [[foundations/nrf2-nfe2l2]]
- [[foundations/ho-1-hmox1]]
- [[foundations/bach1-tf]]
- [[foundations/c-ebp-beta]]
- [[foundations/itaconate-metabolite]]
- [[foundations/irg1-acod1]]
- [[foundations/mtor-kinase]]
- [[foundations/ampk-prkaa]]
- [[foundations/ucp2-mitochondrial-uncoupler]]
- [[foundations/drp1-dnm1l]]
- [[foundations/hif1a]]
- [[foundations/hif2a]]
- [[foundations/4-octyl-itaconate-tet2-inhibitor]]
- [[foundations/nf-kb-p65-rela]]
- [[foundations/slc1a5-asct2-glutamine-transporter]]
- [[people/stefanie-k-wculek]]
- [[people/david-sancho]]
- [[papers/physiology-diseases-tissue-resident-macrophages]] — Lazarov 2023, sibling TRM review (ontogeny + function); together with this paper forms the two-pillar TRM foundation
- [[papers/nf-kb-tet2-promote-macrophage-reprogramming]] — Calafell 2024, NF-κB / TET2 macrophage reprogramming intersects the itaconate / immunometabolism / epigenetics loop discussed here
- [[papers/hypoxia-driven-crosstalk-between-tumor-tumor]] — TAM hypoxic metabolic axis, complementary to in-vivo TRM metabolism
