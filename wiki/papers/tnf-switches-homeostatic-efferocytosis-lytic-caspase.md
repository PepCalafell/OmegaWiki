---
# === Identification ===
title: "TNF switches homeostatic efferocytosis to lytic caspase-8-dependent pyroptosis and IL-1β maturation"
slug: "tnf-switches-homeostatic-efferocytosis-lytic-caspase"
arxiv: ""
doi: "10.1126/sciimmunol.adq0043"
pmid: "40540586"
venue: "Science Immunology"
year: 2025
authors: ["Hayley I. Muendlein", "Wilson M. Connolly", "Jamie Leiriao", "Mei-An Nolan", "Jennifer Judge", "Irina Smirnova", "Rebecca Batorsky", "Alexander Poltorak"]
first_author: "Hayley I. Muendlein"
corresponding_author: "Hayley I. Muendlein; Alexander Poltorak"

# === Source & metadata ===
source_type: pdf
s2_id: "f9401d50984298705da9dee8619c27ff868357a0"
date_added: 2026-06-03
ingested_date: 2026-06-03
ingest_version: 1
last_reviewed:

# === Classification ===
importance: 4
tier: TIER_1
tags: [efferocytosis, efferoptosis, pyroptosis, caspase-8, gasdermin-d, il-1beta, sepsis, sirs, innate-immunity, trif]
keywords: [efferoptosis, caspase-8, GSDMD, TRIF, ZBP1, RIPK1, TAK1, cFLIP, phosphatidylserine, PLCgamma, TIM3, NLRP3, sepsis, SIRS]
domain: "immunology"

# === Biomedical domain ===
tissue: [spleen, lung, kidney, blood, in_vitro_only]
condition: [healthy]
disease_specific: [sepsis, SIRS]
species: [mouse, human]
hypoxia_relevant: false
contains_immune_cells: true
contains_myeloid: true

# === Technique ===
techniques: [flow_cytometry, immunofluorescence, immunoblot, co-immunoprecipitation, qPCR, ELISA, TUNEL, live_cell_imaging, mouse_genetics]
n_samples:
n_cells_total:
integration_method: ""

# === Biology captured ===
key_cell_types: [macrophages, neutrophils, THP-1_macrophages]
key_markers: [CD68, F4/80, CD11b, Ly6G, cleaved_caspase-8, GSDMD_p30, IL-1beta]
key_pathways: [TRIF_signaling, caspase-8_pyroptosis, TAK1-NF-kB, PLCgamma-MAPK, phosphatidylserine_recognition]

# === User project membership ===
projects: [thesis]
priority: context
read_status: read

# === HypoxiaVERSE-specific ===
hypoxiaverse_status:
exclusion_reason:
data_availability: ""

# === Cross-references ===
code_url: ""
cited_by: []
---

## Problem

Efferocytosis — the clearance of dead/dying cells by phagocytes — is canonically anti-inflammatory and immunologically silent, supporting tissue repair and resolution. Whether efferocytosis remains silent under dysregulated inflammation such as sepsis/SIRS (where TNF and IL-1β are elevated and cell death is rampant) had not been tested.

## Key idea

Elevated TNF acts as a master switch that converts homeostatic efferocytosis of dying neutrophils by macrophages into a lytic, caspase-8- and GSDMD-dependent pyroptosis — termed **efferoptosis** — accompanied by inflammasome-independent IL-1β maturation. Blocking efferocytosis (PS-receptor inhibition) protects mice from TNF-induced SIRS and *E. coli* sepsis.

## Method

- Mouse models: TNF-induced SIRS (9 μg mTNF i.v.) and *E. coli* (DH5α, 1×10⁹ CFU i.p.) septic peritonitis, with WT, Trif−/−, Tnfr1−/− mice; neutrophil depletion (anti-Ly6G 1A8) and αTIM3 antibody/sitravatinib interventions.
- In vitro coculture of WT/Trif−/−/Tnfr1−/− macrophages with neutrophils ± TNF; genetic panel (Casp8 D387A, Gsdmd−/−, Zbp1−/−, Ripk1 D138N, Ripk1−/− fetal-liver, Nlrp3−/−, Casp1−/−, Gsdme−/−, Cd14−/−); human THP-1 macrophages + hTNF + murine neutrophils.
- Readouts: PI incorporation kinetics (WGA-labeled macrophages), pHrodo/CFSE efferocytosis tracking, flow cytometry (CD11b/F4/80/Ly6G, Live/Dead), immunoblot (caspase-8 p43/p18, GSDMD p30, IL-1β p17, TAK1/NF-κB/MAPK), RIPK1 immunoprecipitation, qPCR (Il1b, Tnf, Cflar, Nos2), ELISA, TUNEL, Evans blue, immunofluorescence; pharmacology (U-73122 PLC inhibitor, annexin V PS masking, PS-coated beads).

## Results

TRIF-dependent neutrophil responses drive vascular permeability and organ cell death (lung/kidney). In the spleen, ~75% of CD68+ macrophages show cleaved caspase-8 and ~30% show GSDMD p30 after TNF, reduced by TRIF deficiency or neutrophil depletion. In coculture, TNF + WT neutrophils kill 100% of WT macrophages within 8 h via a TRIF/caspase-8/GSDMD/ZBP1-dependent, NLRP3/caspase-1-independent pyroptosis with direct caspase-8-mediated IL-1β maturation. Efferocytosis inhibits TAK1/NF-κB (lowering cFLIP) while PLCγ downstream of PS receptors sustains MAPK and pro-Il1b. Death is initiated by PS recognition (blocked by annexin V, CD14 loss, αTIM3/sitravatinib; mimicked by PS beads). In vivo, TIM3 inhibition improves survival and lowers serum IL-1β/LDH in TNF-SIRS (but exacerbates lung/kidney damage), and TNFR1 deficiency protects in *E. coli* sepsis.

## All claims (exhaustive)

- `[c1]` TNF switches efferocytosis to lytic caspase-8 efferoptosis (p.1) "when activated with TNF, phagocytes efferocytosing neutrophils initiated a caspase-8-dependent, but NLRP3 inflammasome-independent, form of pyroptosis, which we termed 'efferoptosis'" — confidence: high — type: mechanistic — links: [[claims/tnf-switches-efferocytosis-to-efferoptosis]] [[concepts/efferoptosis-tnf-driven-pyroptotic-switch]] [[concepts/efferocytosis-anti-inflammatory-clearance]] [[concepts/caspase-8-dependent-pyroptosis]] [[foundations/tnf-tumor-necrosis-factor]] [[foundations/caspase-8-casp8]]
- `[c2]` IL-1β maturation is inflammasome-independent, via direct caspase-8 cleavage (p.6) "IL-1β maturation was similarly dependent on caspase-8, but independent of caspase-1, suggesting direct cleavage of pro-IL-1β by caspase-8" — confidence: high — type: mechanistic — links: [[claims/il1b-maturation-inflammasome-independent-caspase8]] [[concepts/inflammasome-independent-il-1b-maturation]] [[concepts/caspase-8-dependent-pyroptosis]] [[foundations/caspase-8-casp8]] [[foundations/caspase-1-casp1]] [[foundations/il-1-beta-cytokine]] [[foundations/nlrp3-inflammasome]]
- `[c3]` Efferoptosis requires TRIF (p.5) "there was a substantial reduction of cell death in Trif-/- and Tnfr1-/- macrophages cultured under the same conditions" — confidence: high — type: mechanistic — links: [[claims/efferoptosis-requires-trif]] [[concepts/efferoptosis-tnf-driven-pyroptotic-switch]] [[concepts/trifosome-death-complex]] [[foundations/trif-ticam1]] [[foundations/tnfr1-tnfrsf1a-receptor]]
- `[c4]` Efferoptosis requires caspase-8 catalytic cleavage (p.5) "macrophages with noncleavable caspase-8 (D387A) or GSDMD deficiency exhibited attenuated cell death" — confidence: high — type: mechanistic — links: [[claims/efferoptosis-requires-caspase8-cleavage]] [[concepts/efferoptosis-tnf-driven-pyroptotic-switch]] [[concepts/caspase-8-dependent-pyroptosis]] [[foundations/caspase-8-casp8]]
- `[c5]` Efferoptosis requires gasdermin D (p.5) "macrophages with noncleavable caspase-8 (D387A) or GSDMD deficiency exhibited attenuated cell death" — confidence: high — type: mechanistic — links: [[claims/efferoptosis-requires-gsdmd]] [[concepts/efferoptosis-tnf-driven-pyroptotic-switch]] [[concepts/caspase-8-dependent-pyroptosis]] [[foundations/gasdermin-d-gsdmd]]
- `[c6]` Efferoptosis requires ZBP1 (p.5) "cell death was also dependent on Z-DNA binding protein 1 (ZBP1)" — confidence: high — type: mechanistic — links: [[claims/efferoptosis-requires-zbp1]] [[concepts/efferoptosis-tnf-driven-pyroptotic-switch]] [[concepts/trifosome-death-complex]] [[foundations/zbp1-z-dna-binding-protein]]
- `[c7]` Efferoptosis is NLRP3- and caspase-1-independent (p.5) "Nlrp3-/- and Casp1-/- macrophages were equally susceptible to cell death as WT macrophages" — confidence: high — type: mechanistic — links: [[claims/efferoptosis-independent-nlrp3-caspase1]] [[concepts/caspase-8-dependent-pyroptosis]] [[concepts/inflammasome-independent-il-1b-maturation]] [[foundations/nlrp3-inflammasome]] [[foundations/caspase-1-casp1]]
- `[c8]` RIPK1 scaffolding, not kinase activity, supports efferoptosis (p.5) "kinase inactive (Ripk1D138N/D138N) macrophages were as susceptible as WT ... RIPK1 [deficient] exhibited delayed kinetics of cell death" — confidence: high — type: mechanistic — links: [[claims/ripk1-scaffold-not-kinase-efferoptosis]] [[concepts/trifosome-death-complex]] [[foundations/ripk1-kinase]]
- `[c9]` Neutrophils+TNF assemble a RIPK1-ZBP1-caspase-8 TRIFosome (p.5) "ZBP1 was constitutively bound to RIPK1 in resting macrophages, and this binding was enhanced by treatment with neutrophils and TNF ... binding of the p43 and p18 active fragments of caspase-8" — confidence: high — type: mechanistic — links: [[claims/trifosome-assembly-neutrophils-tnf]] [[concepts/trifosome-death-complex]] [[foundations/ripk1-kinase]] [[foundations/zbp1-z-dna-binding-protein]] [[foundations/caspase-8-casp8]]
- `[c10]` Efferocytosis inhibits TAK1/NF-κB but spares MAPK (p.6) "Coculture of macrophages with neutrophils had little impact on macrophage MAPK activation ... while strongly inhibiting NF-kB activation ... traced back to a loss of TAK1 phosphorylation" — confidence: high — type: mechanistic — links: [[claims/efferocytosis-inhibits-tak1-nfkb-spares-mapk]] [[concepts/efferoptosis-tnf-driven-pyroptotic-switch]] [[foundations/tak1-map3k7-kinase]] [[foundations/nf-kb-p65-rela]] [[foundations/mapk1-3-erk1-2-kinases]]
- `[c11]` Efferocytosis lowers prosurvival cFLIP to license death (p.8) "coculture of macrophages with neutrophils decreased the TNF-mediated up-regulation of Cflar" — confidence: high — type: mechanistic — links: [[claims/efferocytosis-lowers-cflip-cflar]] [[concepts/efferoptosis-tnf-driven-pyroptotic-switch]] [[foundations/cflip-cflar]] [[foundations/tak1-map3k7-kinase]]
- `[c12]` ~75% of splenic CD68+ macrophages show cleaved caspase-8 after TNF (p.3) "we observed cleaved caspase-8 (CC8) staining in ~75% of CD68+ cells in the spleens of WT mice 4 hours after injection with TNF, which was reduced in Trif-/- spleens" — confidence: high — type: quantitative — links: [[claims/cleaved-caspase8-75pct-splenic-macrophages]] [[concepts/efferoptosis-tnf-driven-pyroptotic-switch]] [[foundations/caspase-8-casp8]] [[foundations/trif-ticam1]]
- `[c13]` ~30% of splenic macrophages show GSDMD p30, reduced ~60% in Trif-/- (p.3) "punctate signal in ~30% of CD68+ cells in the spleens of WT mice, which was reduced by ~60% in TRIF-deficient mice" — confidence: high — type: quantitative — links: [[claims/gsdmd-p30-30pct-splenic-macrophages]] [[concepts/efferoptosis-tnf-driven-pyroptotic-switch]] [[foundations/gasdermin-d-gsdmd]] [[foundations/trif-ticam1]]
- `[c14]` Neutrophil depletion halves splenic macrophage caspase-8/GSDMD activation (p.3) "neutrophil depletion decreased the percentage of CD68+ cells with CC8 and cleaved GSDMD by ~50%" — confidence: high — type: mechanistic — links: [[claims/neutrophil-depletion-reduces-macrophage-pyroptosis]] [[concepts/efferoptosis-tnf-driven-pyroptotic-switch]] [[foundations/caspase-8-casp8]] [[foundations/gasdermin-d-gsdmd]]
- `[c15]` Phosphatidylserine recognition initiates efferoptosis (p.7) "we coated dead neutrophils with annexin V to block exposed PS and observed a substantial decrease in macrophage cell death ... the stimulation of macrophages with PS-conjugated beads was sufficient to induce cell death in TNF-activated macrophages" — confidence: high — type: mechanistic — links: [[claims/ps-recognition-initiates-efferoptosis]] [[concepts/efferoptosis-tnf-driven-pyroptotic-switch]] [[concepts/efferocytosis-anti-inflammatory-clearance]] [[foundations/phosphatidylserine-eat-me-signal]] [[foundations/cd14-receptor]] [[foundations/tim3-havcr2-receptor]] [[foundations/mertk-tam-receptors]]
- `[c16]` PLCγ downstream of PS receptors sustains MAPK and pro-IL-1β (p.8) "Treatment with a PLC inhibitor (U-73122) inhibited and delayed MAPK activation ... it abrogated the production of both pro- and mature IL-1β" — confidence: high — type: mechanistic — links: [[claims/plcg-mapk-drives-il1b-upregulation]] [[concepts/inflammasome-independent-il-1b-maturation]] [[foundations/plc-gamma-plcg]] [[foundations/mapk1-3-erk1-2-kinases]] [[foundations/il-1-beta-cytokine]]
- `[c17]` Neutrophil coculture raises Il1b but lowers Tnf mRNA (p.6) "treatment of macrophages with neutrophils and TNF not only promoted IL-1β maturation but also enhanced the up-regulation of pro-Il1b mRNA ... coculture of macrophages with neutrophils resulted in a strong decrease in Tnf mRNA levels" — confidence: medium — type: correlational — links: [[claims/transcriptional-dichotomy-il1b-up-tnf-down]] [[concepts/inflammasome-independent-il-1b-maturation]] [[foundations/il-1-beta-cytokine]] [[foundations/tnf-tumor-necrosis-factor]]
- `[c18]` Efferoptosis is GSDME-independent despite caspase-3 activation (p.8) "efferoptosis occurred independently of GSDME despite the activation of caspase-3" — confidence: high — type: mechanistic — links: [[claims/efferoptosis-gsdme-independent]] [[concepts/caspase-8-dependent-pyroptosis]] [[foundations/gasdermin-e-gsdme]] [[foundations/caspase-8-casp8]]
- `[c19]` Human THP-1 macrophages undergo efferoptosis and release mature IL-1β (p.6) "simultaneous treatment of human macrophages with hTNF and mNeuts resulted in increased macrophage cell death and IL-1β release" — confidence: medium — type: methodological — links: [[claims/human-thp1-macrophages-efferoptosis]] [[concepts/efferoptosis-tnf-driven-pyroptotic-switch]] [[foundations/il-1-beta-cytokine]] [[foundations/tnf-tumor-necrosis-factor]]
- `[c20]` TIM3 inhibition improves survival and cuts serum IL-1β/LDH in TNF-SIRS (p.8) "We observed attenuated TNF-induced hypothermia and improved survival in αTIM3-treated mice ... reduced serum IL-1β and LDH levels" — confidence: high — type: pharmacological — links: [[claims/tim3-inhibition-protects-tnf-sirs]] [[concepts/efferoptosis-tnf-driven-pyroptotic-switch]] [[foundations/tim3-havcr2-receptor]] [[foundations/il-1-beta-cytokine]] [[foundations/caspase-8-casp8]]
- `[c21]` Efferocytosis is protective in lung and kidney (p.8) "TIM3 inhibition did not prevent and even exacerbated TNF-induced cell death as measured by TUNEL staining in the lung and kidney" — confidence: medium — type: mechanistic — links: [[claims/efferocytosis-protective-in-lung-kidney]] [[concepts/efferocytosis-anti-inflammatory-clearance]] [[foundations/tim3-havcr2-receptor]]
- `[c22]` TRIF drives TNF-induced neutrophil recruitment and organ damage (p.2) "extensive infiltration of Ly6G+ neutrophils in the lungs of wild-type mice 4 hours after injection with TNF that was abrogated in Trif-/- mice" — confidence: high — type: mechanistic — links: [[claims/trif-drives-neutrophil-organ-damage]] [[concepts/trifosome-death-complex]] [[foundations/trif-ticam1]] [[foundations/tnf-tumor-necrosis-factor]]
- `[c23]` Efferoptosis is TNF-dependent in E. coli septic peritonitis (p.12) "in the absence of TNF signaling, macrophages are capable of undergoing homeostatic efferocytosis without switching to lytic efferoptosis" — confidence: high — type: mechanistic — links: [[claims/efferoptosis-tnf-dependent-ecoli-sepsis]] [[concepts/efferoptosis-tnf-driven-pyroptotic-switch]] [[foundations/tnfr1-tnfrsf1a-receptor]] [[foundations/tnf-tumor-necrosis-factor]]
- `[c24]` Timing of neutrophil depletion determines TNF lethality (p.12) "mice treated with 1A8 4 hours before injection were highly sensitive to TNF-induced lethality, with 100% of mice succumbing within 5 hours" — confidence: medium — type: mechanistic — links: [[claims/neutrophil-depletion-timing-determines-lethality]] [[concepts/efferoptosis-tnf-driven-pyroptotic-switch]] [[foundations/tnf-tumor-necrosis-factor]]

## Discussion captured

### Authors' interpretation

The authors interpret efferoptosis as an additional mechanism by which homeostatic neutrophil regulation becomes dysregulated in sepsis: elevated TNF transforms anti-inflammatory efferocytosis into lytic death that feeds the inflammatory milieu. They argue the caspase-8-dependent mechanism resolves the discrepancy that Gsdmd−/− mice are protected from TNF-SIRS while Casp1−/− mice are not. Detection of dying neutrophils inhibits TNF-mediated NF-κB (lowering cFLIP) without blocking MAPK, which instead runs through PLCγ downstream of PS receptors (e.g. MERTK) to up-regulate pro-IL-1β.

### Comparisons with prior literature (made by authors)

They tie efferoptosis to prior caspase-8-mediated pyroptosis in *Yersinia* infection and LPS/TNF + TAK1 inhibition (refs 15–19), to their own TRIFosome/ZBP1-RIPK1 work (refs 29, 30), to caspase-8 IL-1β cleavage in fungal infection (ref 32), to MERTK→PLCγ activation by apoptotic thymocytes (ref 33), and note Gsdmd−/− protection from TNF lethality (ref 27). They cite the largely unsuccessful clinical history of TNF blockade in sepsis (refs 38, 39).

### Mechanistic hypotheses proposed

- Caspase-8 directly cleaves pro-IL-1β (and GSDMD) without caspase-1 (p.6).
- PLCγ downstream of PS receptors provides the priming step for pro-IL-1β in the absence of TAK1 activity (p.8).
- TAK1-mediated MAPK and NF-κB activation can be uncoupled (p.6).
- Efferoptosis may explain the in vivo vs in vitro discrepancy of TNF-induced death (phagocytes meet large aggregates of dying cells in vivo) (p.12).

### Caveats and self-criticism

The authors note their studies used bolus TNF and high-dose *E. coli*, which induce extensive synchronized death — convenient for quantification but not physiological; whether efferoptosis contributes under physiological chronic TNF/turnover remains undetermined. They stress that the beneficial roles of efferocytosis must not be disregarded (TIM3 inhibition worsened lung/kidney damage).

### Future directions suggested

Models of sepsis/autoimmunity that better recapitulate clinical elevated TNF and cellular turnover; PS receptors as therapeutic targets, possibly combined with TNF blockade; immunomodulation at the level of TRIF or TNFR1 to generate phagocytes that clear dead cells without undergoing efferoptosis.

## Limitations

- Mouse-centric; human evidence limited to a THP-1 cell line with murine neutrophils.
- Acute, supraphysiological challenge models (bolus TNF, high-dose bacteria).
- No single-cell/omics characterization; mechanistic dissection is targeted but model-bound.
- Tissue heterogeneity: efferocytosis is lethal in spleen but protective in lung/kidney, complicating any systemic therapeutic.

## Open questions

### Open questions raised by authors

- Does efferoptosis occur and contribute to pathology under physiological (chronic) conditions?
- Can TRIF/TNFR1-level immunomodulation decouple harmful efferoptosis from beneficial efferocytosis?

### Open questions identified during ingest

- Which efferocytic cell types beyond splenic macrophages undergo efferoptosis in vivo?
- Is the PLCγ→pro-IL-1β priming arm shared with other IL-1 family cytokines?
- How is the PS-recognition signal mechanistically relayed to TRIFosome assembly?

## My take

A conceptually clean inversion of a textbook process: efferocytosis as a context-dependent liability under high TNF. The separation of the death arm (TAK1-loss → caspase-8/GSDMD) from the IL-1β arm (PS receptor → PLCγ/MAPK priming + direct caspase-8 cleavage) is the strongest mechanistic contribution. Relevance to the thesis: connects efferocytosis/macrophage biology to inflammasome-independent IL-1β and caspase-8 pyroptosis.

## Related

- [[concepts/efferoptosis-tnf-driven-pyroptotic-switch]]
- [[concepts/caspase-8-dependent-pyroptosis]]
- [[concepts/inflammasome-independent-il-1b-maturation]]
- [[concepts/trifosome-death-complex]]
- [[concepts/efferocytosis-anti-inflammatory-clearance]]
- [[people/hayley-muendlein]]
- [[people/alexander-poltorak]]
