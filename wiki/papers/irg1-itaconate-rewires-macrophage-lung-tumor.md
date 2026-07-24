---
# === Identification ===
title: "IRG1/itaconate rewires macrophage and lung tumor metabolism through G6PD inhibition"
slug: "irg1-itaconate-rewires-macrophage-lung-tumor"
arxiv: ""
doi: "10.1016/j.cmet.2026.05.005"
pmid: "42235511"
venue: "Cell Metabolism"
year: 2026
authors: ["Siavash Mansouri", "Golnaz Hesami", "Anoop Ambikan", "Annika Karger", "Stephan Klatt", "Ujjwal Neogi", "Konda Babu Kurakula", "Blerina Aliraj", "Anne Miller", "Boryana Petrova", "Miloslav Sanda", "Evelyn Sirait-Fischer", "Stefan Guenther", "Carsten Kuenne", "Clemens Ruppert", "Ibrahim Alkoudmani", "Stefan Gattenlöhner", "Sven Zukunft", "Ingrid Fleming", "Arvand Haschemi", "Thorsten Stiewe", "Friedrich Grimminger", "Martin Reck", "Andreas Weigert", "Werner Seeger", "Soni Savai Pullamsetti", "Rajkumar Savai"]
first_author: "Siavash Mansouri"
corresponding_author: "Rajkumar Savai"

# === Source & metadata ===
source_type: pdf
s2_id: "859a66483e962e46b0de6efcf3def59b204b28d3"
date_added: 2026-07-24
ingested_date: 2026-07-24
ingest_version: 1
last_reviewed:

# === Classification ===
importance: 4
tier: TIER_1
tags:
  - tumor-associated-macrophage
  - itaconate
  - IRG1
  - G6PD
  - pentose-phosphate-pathway
  - immunometabolism
  - macrophage-polarization
  - lung-cancer
  - spatial-metabolomics
  - 4-octyl-itaconate
  - ABCG2
  - metabolic-reprogramming
keywords:
  - IRG1/ACOD1
  - itaconate
  - octyl itaconate
  - G6PD
  - pentose phosphate pathway
  - tumor-associated macrophages
  - lung adenocarcinoma
  - NRF2
domain: "oncology"

# === Biomedical domain ===
tissue: [lung, blood, in_vitro_only]
condition: [cancer]
disease_specific: [lung_adenocarcinoma, non_small_cell_lung_cancer]
species: [both]
hypoxia_relevant: false
contains_immune_cells: true
contains_myeloid: true

# === Technique ===
techniques: [spatial_metabolomics_MALDI-MSI, scRNA-seq_10x, LC-MS_metabolomics, 13C_metabolic_flux_tracing, bulk_RNA-seq, proteomics, Olink_proteomics, flow_cytometry, immunofluorescence, molecular_docking, chemoproteomics, precision_cut_lung_slices, bone_marrow_transplant]
n_samples:
n_cells_total:
integration_method: ""

# === Biology captured ===
key_cell_types:
  - tumor-associated macrophage
  - pro-inflammatory (M1) macrophage
  - anti-inflammatory (M2/IL-4) macrophage
  - bone-marrow-derived macrophage
  - lung adenocarcinoma cell
  - monocyte
key_markers:
  - IRG1
  - ACOD1
  - G6PD
  - ABCG2
  - NRF2
  - HMOX1
  - CD80
  - CD206
  - CSF1R
  - TNF
  - KEAP1
  - TKT
key_pathways:
  - pentose phosphate pathway
  - itaconate / IRG1 immunometabolism
  - NRF2 / KEAP1 antioxidant response
  - G6PD-ROS-HMOX1 stress response
  - macrophage polarization
  - nucleotide biosynthesis (ribose-5-phosphate)

# === User project membership ===
projects: [thesis]
priority: core
read_status: read

# === HypoxiaVERSE-specific ===
hypoxiaverse_status: excluded
exclusion_reason: "not a hypoxia-focused study; itaconate/PPP metabolic axis in lung cancer macrophages"
data_availability: "PubMed 42235511; DOI 10.1016/j.cmet.2026.05.005 (CC BY, open access)"

# === Cross-references ===
code_url: ""
cited_by: []
---

## Problem

Tumor-associated macrophages (TAMs) have both tumor-promoting and tumor-inhibiting roles, but the mechanisms distinguishing pro- from anti-tumor macrophages — and how one converts into the other — remain poorly understood. The macrophage immunometabolite **itaconate** (made by IRG1/ACOD1) is well studied in host defense and inflammation, where it inhibits SDH and alkylates KEAP1 to activate NRF2, but its role in lung tumorigenesis and any direct effect on cancer cells were unknown.

## Key idea

Endogenous itaconate is **spatially depleted inside lung tumors** and macrophages are its main source. IRG1/itaconate is anti-tumor in the lung: its loss accelerates tumor growth and skews TAMs pro-tumor, while restoring itaconate with cell-permeable **4-octyl itaconate (Octyl Ita)** suppresses tumors in vivo, ex vivo (human precision-cut lung slices), and in vitro. Mechanistically, itaconate and Octyl Ita **non-covalently inhibit glucose-6-phosphate dehydrogenase (G6PD)**, shutting down oxidative pentose phosphate pathway (PPP) flux. This one node simultaneously (i) starves cancer cells of ribose (anti-proliferative, NRF2-independent) and (ii) reprograms macrophages toward an anti-tumor state (NRF2-dependent). Secreted itaconate (exported via **ABCG2**) also acts non-cell-autonomously on adjacent tumor cells.

## Method

- **Spatial metabolomics**: MALDI-MSI of KrasLA2 and KrasLA2/Irg1−/− lungs mapping itaconate, GSH, and ribose-5-phosphate; metabolic segmentation of tumor vs non-tumor regions.
- **Genetic/transplant models**: KrasLA2/Irg1−/−, orthotopic and i.v. LLC1, and WT→Irg1−/− bone-marrow chimeras; micro-CT tumor quantification; PCNA/caspase-8 IF; flow cytometry (CD80/CD206); Olink proteomics.
- **scRNA-seq**: internal mouse CD45+ TME dataset plus two public human lung adenocarcinoma datasets to localize IRG1 expression.
- **Pharmacology**: Octyl Ita in KrasLA2 (100 mg/kg), LLC1 (orthotopic/subcutaneous), human tumor-derived precision-cut lung slices (TD-PCLS, 250 µM), and a panel of lung cancer cell lines (varying KEAP1 status).
- **Metabolic dissection**: LC-MS PPP metabolomics; [1,2-¹³C₂]-glucose flux tracing; GSH/GSSG; Seahorse OCR/ECAR; transcriptomics + proteomics of A549 and macrophages.
- **Target validation**: G6PD activity assays (cell homogenate + recombinant), Michaelis-Menten kinetics, molecular docking, ITalk chemoproteomics; siG6PD/siABCG2 knockdowns; PPP-metabolite and NAC rescue; TKT overexpression.
- **Human/clinical**: TAM G6PD activity in patient tumors; Kaplan-Meier survival by G6PD/ABCG2; pan-cancer ABCG2 hazard-ratio analysis.

## Results

Itaconate is confined to non-tumor lung tissue and absent in Irg1−/− lungs. IRG1 knockout and hematopoietic IRG1 deficiency both accelerate lung tumor growth and skew TAMs pro-tumor. Octyl Ita raises tumor itaconate and suppresses growth across models while enriching anti-tumor (CD80+) TAMs, and directly inhibits cancer-cell proliferation independent of KEAP1 status. Metabolically, Octyl Ita rapidly depletes PPP intermediates, reduces oxidative PPP flux (¹³C tracing), and lowers GSH — without changing glycolysis or respiration. The target is G6PD: itaconate and Octyl Ita reduce G6PD Vmax non-covalently (docking + kinetics + no cysteine adduct), and G6PD knockdown abolishes further drug effect while PPP metabolites (not NAC) rescue — with reduced ribose (not NADPH) as the primary growth driver. The same axis operates in macrophages (IRG1 suppresses G6PD; Octyl Ita reprograms IL-4 macrophages via NRF2-dependent PPP suppression) and in vivo/human tumors (IRG1 loss raises, Octyl Ita lowers in situ G6PD; IRG1+ human TAMs have lower G6PD). Clinically, high G6PD tracks worse and high ABCG2 tracks better survival, with ABCG2 prognosis flipping sign across cancer types.

## All claims (exhaustive)

- `[c1]` Endogenous itaconate is spatially depleted within lung tumor regions vs adjacent non-tumor tissue `(p.1461)` "Itaconate was markedly reduced in tumor regions compared with adjacent non-tumor tissue, which indicated suppressed itaconate metabolism in lung tumors" — confidence: high — type: correlational — links: [[claims/endogenous-itaconate-spatially-depleted-within-lung]] [[foundations/itaconate-metabolite]] [[foundations/maldi-msi-spatial-metabolomics-imaging]]
- `[c2]` Macrophages are the primary IRG1-expressing cells in human and mouse lung tumors `(p.1461)` "Single-cell RNA sequencing (scRNA-seq) identified macrophages as the major Irg1-expressing population in the mouse lung TME ... IRG1 expression was enriched in myeloid cells, particularly in macrophages and monocytes" — confidence: high — type: methodological — links: [[claims/macrophages-primary-irg1-expressing-cells-lung]] [[foundations/irg1-acod1]] [[foundations/scrna-seq-10x-chromium]]
- `[c3]` IRG1 knockout increases lung tumor growth and metastasis `(p.1461)` "the Irg1 loss significantly increased tumor growth and metastasis, with an increased tumor burden and proliferation but no change in apoptosis" — confidence: high — type: mechanistic — links: [[claims/irg1-knockout-increases-lung-tumor-growth]] [[foundations/irg1-acod1]] [[foundations/kras-oncogene]]
- `[c4]` Hematopoietic IRG1 deficiency is sufficient to accelerate lung tumor progression `(p.1461)` "Bone marrow transplantation demonstrated that hematopoietic IRG1 deficiency was sufficient to accelerate LLC1 tumor progression" — confidence: high — type: mechanistic — links: [[claims/hematopoietic-irg1-deficiency-accelerates-lung-tumor]] [[foundations/irg1-acod1]]
- `[c5]` IRG1 loss shifts TAMs toward a pro-tumor phenotype `(p.1461)` "TAMs from Irg1−/− tumors showed a pro-tumor phenotype, with reduced CD80 and increased CD206" — confidence: high — type: mechanistic — links: [[claims/irg1-loss-shifts-tumor-associated-macrophages]] [[concepts/m1-m2-polarization-paradigm]] [[foundations/irg1-acod1]]
- `[c6]` 4-octyl itaconate reduces lung tumor growth in vivo, ex vivo, and in vitro `(p.1463)` "4-octyl itaconate (Octyl Ita) reduces tumor growth in vitro, in vivo, and in ex vivo human tumor precision-cut lung slices" — confidence: high — type: pharmacological — links: [[claims/octyl-itaconate-reduces-lung-tumor-growth]] [[foundations/4-octyl-itaconate-tet2-inhibitor]] [[foundations/precision-cut-lung-slices-ex-vivo]]
- `[c7]` Octyl itaconate inhibits lung cancer proliferation independent of KEAP1/NRF2 status `(p.1464)` "Octyl Ita potently inhibited proliferation across lung cancer cell lines regardless of Kelch-like ECH-associated protein 1 (KEAP1) status, which indicated KEAP1/NRF2-independent activity" — confidence: high — type: pharmacological — links: [[claims/octyl-itaconate-inhibits-lung-cancer-proliferation]] [[foundations/4-octyl-itaconate-tet2-inhibitor]] [[foundations/nrf2-nfe2l2]]
- `[c8]` IRG1/itaconate directly inhibits cancer cell proliferation cell-autonomously `(p.1464)` "IRG1 overexpression reduced proliferation and cell numbers without affecting apoptosis in A549 and KEAP1-deficient H1650 cells" — confidence: high — type: mechanistic — links: [[claims/irg1-itaconate-directly-inhibits-cancer-cell]] [[concepts/secreted-itaconate-non-cell-autonomous-tumor]] [[foundations/itaconate-metabolite]]
- `[c9]` Octyl itaconate depletes PPP intermediates and impairs oxidative PPP activity `(p.1464)` "the rapid depletion of pentose phosphate pathway (PPP) intermediates within 6 h of treatment ... A reduced ribose-5-phosphate (R5P)/ribulose-5-phosphate (Ru5P) ratio indicated impaired oxidative PPP activity" — confidence: high — type: quantitative — links: [[claims/octyl-itaconate-depletes-pentose-phosphate-pathway]] [[concepts/irg1-itaconate-g6pd-pentose-phosphate-pathway]] [[foundations/pentose-phosphate-pathway]]
- `[c10]` ¹³C-glucose tracing confirms reduced oxidative PPP flux without enhanced glycolysis `(p.1464)` "[1,2-¹³C₂]-glucose tracing showed reduced M + 1 labeling of pentose phosphates ... which confirmed a decreased oxidative PPP flux ... reduced glucose shunting into the oxidative PPP rather than enhanced glycolysis" — confidence: high — type: methodological — links: [[claims/13c-glucose-tracing-confirms-reduced-oxidative]] [[foundations/stable-isotope-13c-glucose-metabolic-flux]] [[foundations/pentose-phosphate-pathway]]
- `[c11]` Octyl itaconate lowers glutathione and the GSH/GSSG ratio (impaired PPP-derived NADPH) `(p.1466)` "Octyl Ita lowered glutathione (GSH) levels and reduced the GSH/GSSG ratio, which was consistent with impaired PPP-derived NADPH production" — confidence: medium — type: mechanistic — links: [[claims/octyl-itaconate-lowers-glutathione-gsh-gssg]] [[foundations/pentose-phosphate-pathway]]
- `[c12]` Itaconate and Octyl itaconate non-covalently inhibit G6PD by reducing Vmax `(p.1467)` "Octyl Ita significantly reduced G6PD activity in A549 cells without affecting protein abundance ... reduced G6PD Vmax (1.52 → 1.19 U) ... Octyl Ita inhibits G6PD through non-covalent pocket binding" — confidence: high — type: mechanistic — links: [[claims/itaconate-non-covalently-inhibits-g6pd-reducing]] [[concepts/irg1-itaconate-g6pd-pentose-phosphate-pathway]] [[foundations/g6pd-glucose-phosphate-dehydrogenase]]
- `[c13]` Molecular docking predicts itaconate and Octyl itaconate bind the G6PD active site `(p.1467)` "Molecular docking predicted that both Octyl Ita and itaconate bind to G6PD, with Octyl Ita showing a slightly higher affinity (−5.9 vs. −5.2 kcal/mol)" — confidence: medium — type: quantitative — links: [[claims/molecular-docking-predicts-itaconate-binds-g6pd]] [[foundations/g6pd-glucose-phosphate-dehydrogenase]]
- `[c14]` G6PD inhibition underlies the anti-proliferative effect of Octyl itaconate `(p.1468)` "Octyl Ita failed to further reduce proliferation in G6PD-knockdown A549 cells ... PPP metabolites ... rescued proliferation, whereas antioxidant treatment with N-acetylcysteine (NAC) had no effect" — confidence: high — type: mechanistic — links: [[claims/g6pd-inhibition-underlies-anti-proliferative-effect]] [[concepts/irg1-itaconate-g6pd-pentose-phosphate-pathway]] [[foundations/g6pd-glucose-phosphate-dehydrogenase]]
- `[c15]` Reduced ribose production, not NADPH depletion, drives growth suppression `(p.1468)` "Overexpression of TKT to increase non-oxidative PPP flux partially restored proliferation, which indicated that reduced ribose production rather than NADPH depletion is the primary driver of growth suppression" — confidence: medium — type: mechanistic — links: [[claims/reduced-ribose-production-rather-than-nadph]] [[foundations/pentose-phosphate-pathway]]
- `[c16]` Octyl itaconate reprograms anti-inflammatory macrophages toward a tumor-suppressive state via PPP suppression `(p.1470)` "Octyl Ita reprograms anti-inflammatory macrophages toward a stress-activated, partially pro-inflammatory state that is associated with redox signaling and metabolic remodeling" — confidence: medium — type: mechanistic — links: [[claims/octyl-itaconate-reprograms-anti-inflammatory-macrophages]] [[concepts/irg1-itaconate-g6pd-pentose-phosphate-pathway]] [[concepts/m1-m2-polarization-paradigm]]
- `[c17]` Pro-inflammatory macrophages have high IRG1/itaconate and low G6PD; anti-inflammatory the opposite `(p.1469)` "pro-inflammatory macrophages exhibited high IRG1 expression and itaconate production, reduced G6PD activity ... IL-4-stimulated anti-inflammatory macrophages displayed lower IRG1/itaconate levels, elevated G6PD activity" — confidence: high — type: correlational — links: [[claims/pro-inflammatory-macrophages-high-irg1-itaconate]] [[concepts/succinate-itaconate-metabolic-set-point]] [[foundations/g6pd-glucose-phosphate-dehydrogenase]]
- `[c18]` Endogenous IRG1/itaconate suppresses G6PD activity in macrophages `(p.1471)` "IRG1 knockdown in pro-inflammatory macrophages ... led to G6PD activity enhancement without altering protein abundance ... Irg1−/− mouse BMDMs displayed elevated G6PD activity following LPS stimulation" — confidence: high — type: mechanistic — links: [[claims/endogenous-irg1-itaconate-suppresses-g6pd-activity]] [[foundations/irg1-acod1]] [[foundations/g6pd-glucose-phosphate-dehydrogenase]]
- `[c19]` Macrophage-secreted itaconate exported via ABCG2 mediates non-cell-autonomous tumor suppression `(p.1471)` "ABCG2 knockdown attenuated the anti-proliferative activity of CM from pro-inflammatory macrophages, which indicated that secreted itaconate contributes to macrophage-mediated tumor suppression" — confidence: medium — type: mechanistic — links: [[claims/macrophage-secreted-itaconate-exported-abcg2-mediates]] [[concepts/secreted-itaconate-non-cell-autonomous-tumor]] [[foundations/abcg2-itaconate-exporter-transporter]]
- `[c20]` IRG1 loss raises and Octyl itaconate lowers in situ G6PD activity in lung tumors in vivo `(p.1471)` "IRG1-deficient mice showed significantly elevated in situ G6PD activity compared with WT controls ... Octyl Ita treatment decreased G6PD activity in orthotopically implanted lung tumors" — confidence: high — type: mechanistic — links: [[claims/irg1-loss-raises-octyl-itaconate-lowers]] [[foundations/g6pd-glucose-phosphate-dehydrogenase]] [[foundations/4-octyl-itaconate-tet2-inhibitor]]
- `[c21]` Human IRG1+ TAMs show lower G6PD activity than IRG1- TAMs `(p.1471)` "CD68+/IRG1+ macrophages exhibited lower G6PD activity than CD68+/IRG1− macrophages, which confirmed that endogenous IRG1/itaconate suppresses G6PD within the TME" — confidence: medium — type: correlational — links: [[claims/human-irg1-positive-tams-show-lower]] [[foundations/g6pd-glucose-phosphate-dehydrogenase]] [[foundations/irg1-acod1]]
- `[c22]` High G6PD predicts worse survival and high ABCG2 predicts better survival in lung adenocarcinoma `(p.1471)` "high G6PD expression is correlated with significantly worse overall survival, whereas high ABCG2 expression—the itaconate exporter—was associated with improved outcomes" — confidence: medium — type: correlational — links: [[claims/high-g6pd-predicts-worse-survival-high]] [[concepts/irg1-itaconate-g6pd-pentose-phosphate-pathway]] [[foundations/abcg2-itaconate-exporter-transporter]]
- `[c23]` ABCG2/itaconate has opposite prognostic value in lung/breast vs colorectal/gastric cancers `(p.1472)` "ABCG2 showed favorable prognostic associations (HR < 1) in lung and breast cancers ... In contrast, ABCG2 was correlated with poor prognosis (HR > 1) in colorectal and gastric cancers" — confidence: medium — type: correlational — links: [[claims/abcg2-itaconate-opposite-prognostic-value-lung]] [[concepts/irg1-itaconate-context-dependent-tumor-role]] [[foundations/abcg2-itaconate-exporter-transporter]]
- `[c24]` Itaconate's PPP effects are NRF2-independent in cancer cells but NRF2-dependent in macrophages `(p.1473)` "itaconate/Octyl Ita modulates PPP metabolism and oxidative stress response in cancer cells in an NRF2-independent manner, while the effects of itaconate/Octyl Ita in macrophages are NRF2-dependent" — confidence: medium — type: mechanistic — links: [[claims/itaconate-ppp-effects-nrf2-independent-cancer]] [[concepts/irg1-itaconate-g6pd-pentose-phosphate-pathway]] [[foundations/nrf2-nfe2l2]]

## Discussion captured

### Authors' interpretation

The authors argue for a previously unknown anti-tumor role of IRG1/itaconate in lung cancer, unified under a single mechanism: non-covalent inhibition of G6PD and consequent suppression of oxidative PPP flux. They interpret IRG1 expression as following **bell-shaped kinetics** during tumor development — an early anti-tumor rise, then decline as tumors progress and pro-tumor macrophages dominate. They emphasize the lung's unique immunometabolic environment (high baseline inflammatory tone, continuous antigen exposure, macrophage-driven epithelial defense) as the reason itaconate is anti-tumor here despite pro-tumor roles elsewhere.

### Comparisons with prior literature (made by authors)

- Casanova-Acebes et al. 2021 *Nature* (ref 32; DOI 10.1038/s41586-021-03651-8) — monocyte-derived macrophages dominate advanced lesions and Irg1 declines with progression; used to support bell-shaped kinetics. In vault: [[papers/tissue-resident-macrophages-provide-pro-tumorigenic]].
- Michelucci et al. 2013 — IRG1/itaconate induction in inflammatory macrophages.
- Mills et al. 2018 *Nature* — Octyl Ita activates NRF2 via KEAP1 cysteine modification (contrasted with NRF2-independent cancer-cell effect here).
- Zhao et al. and others — pro-tumor IRG1 roles in melanoma/ovarian/colorectal/pancreatic via CD8+ T-cell suppression (context contrast).
- Artyomov group — itaconate non-covalently binds PRDX5, supporting a reversible (non-covalent) itaconate mode of action.
- Liu et al. 2017 — IRG1→ROS-dependent STAT-TAP1→MHC-I axis (this study extends IRG1 redox signaling to G6PD/PPP).

### Mechanistic hypotheses proposed

- IRG1 expression follows bell-shaped kinetics during lung tumor development (p.1472).
- Local macrophage-rich niches reach higher effective extracellular itaconate concentrations than bulk measurements suggest (p.1472).
- Cell-type NRF2 dependence reflects differing inflammatory/oxidative states (per Swain et al.) (p.1473).

### Caveats and self-criticism

- Detailed PPP flux analyses were performed mainly in A549; PPP/G6PD dependence across additional genetic subtypes is an open question (p.1473).
- Extracellular itaconate concentrations are generally low; local niche exposure is inferred (p.1472).
- Cannot rule out itaconate/OXGR1 receptor signaling contributions in cancer cells and macrophages (p.1473).
- Itaconate import/export transport mechanisms remain incompletely defined (p.1473).

### Future directions suggested

- Test PPP/G6PD sensitivity across additional lung cancer genetic subtypes.
- Careful, context-aware therapeutic use of itaconate derivatives (tumor origin, immune composition, cellular source) to avoid pro-tumor effects.
- Define transporters controlling intracellular vs extracellular itaconate.

## Limitations

- Single primary cell-line model (A549) for the deepest metabolic-flux dissection.
- Human evidence is largely associative (TAM G6PD activity, TCGA/expression survival, ABCG2 hazard ratios).
- Molecular docking supports but does not structurally prove the itaconate–G6PD binding pose.
- Exogenous itaconate dosing is high and entry-limited; physiological relevance rests on local-niche assumptions.

## Open questions

### Open questions raised by authors

- What controls IRG1 downregulation during lung tumor progression?
- Does PPP/G6PD sensitivity vary across lung cancer genetic subtypes?
- What are the transporters governing itaconate movement in/out of cells?

### Open questions identified during ingest

- Can a co-crystal structure confirm the non-covalent itaconate–G6PD pocket?
- What is the therapeutic window for Octyl Ita given systemic G6PD's role in redox homeostasis (e.g. hemolysis risk)?
- How is direct tumor-cell action reconciled quantitatively with paracrine/macrophage contributions in vivo?

## My take

This is a strong, mechanistically complete immunometabolism paper that lands a genuinely new target: it moves itaconate biology beyond SDH/KEAP1 to **non-covalent G6PD inhibition**, and it uses that single node to explain both tumor-cell-intrinsic anti-proliferation and macrophage reprogramming. The epistasis (G6PD knockdown abolishes the drug effect; PPP metabolites but not NAC rescue) is the load-bearing experiment, and the ribose-vs-NADPH dissection is unusually careful. For a macrophage/TAM thesis it is directly useful: it operationalizes the pro-/anti-tumor macrophage switch as an IRG1–G6PD–PPP metabolic dial and adds a paracrine (ABCG2-exported) metabolite mechanism. The main caveats are the reliance on A549 for flux work, associative human data, and the strong context-dependence that the authors themselves flag — the same axis could be pro-tumor in other tissues. Not hypoxia-centric, but a clean example of spatial-metabolomics-driven target discovery.

## Related

**Concepts**: [[concepts/irg1-itaconate-g6pd-pentose-phosphate-pathway]] · [[concepts/secreted-itaconate-non-cell-autonomous-tumor]] · [[concepts/irg1-itaconate-context-dependent-tumor-role]] · [[concepts/m1-m2-polarization-paradigm]] · [[concepts/succinate-itaconate-metabolic-set-point]] · [[concepts/m1-macrophage-tca-breaks-itaconate-succinate]]

**Foundations (biology)**: [[foundations/irg1-acod1]] · [[foundations/itaconate-metabolite]] · [[foundations/4-octyl-itaconate-tet2-inhibitor]] · [[foundations/g6pd-glucose-phosphate-dehydrogenase]] · [[foundations/pentose-phosphate-pathway]] · [[foundations/abcg2-itaconate-exporter-transporter]] · [[foundations/nrf2-nfe2l2]] · [[foundations/ho-1-hmox1]] · [[foundations/kras-oncogene]]

**Foundations (methods)**: [[foundations/maldi-msi-spatial-metabolomics-imaging]] · [[foundations/stable-isotope-13c-glucose-metabolic-flux]] · [[foundations/precision-cut-lung-slices-ex-vivo]] · [[foundations/scrna-seq-10x-chromium]]

**Papers**: [[papers/tissue-resident-macrophages-provide-pro-tumorigenic]]

**People**: [[people/siavash-mansouri]] · [[people/rajkumar-savai]] · [[people/soni-savai-pullamsetti]] · [[people/werner-seeger]] · [[people/ujjwal-neogi]] · [[people/clemens-ruppert]] · [[people/friedrich-grimminger]]
