---
# === Identification ===
title: "Tumor-induced metabolic immunosuppression: Mechanisms and therapeutic targets"
slug: tumor-induced-metabolic-immunosuppression-mechanisms-therapeutic
arxiv: ""
doi: "10.1016/j.celrep.2024.115206"
pmid: ""
venue: "Cell Reports"
year: 2025
authors: ["Jean-Ehrland Ricci"]
first_author: "Jean-Ehrland Ricci"
corresponding_author: "Jean-Ehrland Ricci"

# === Source & metadata ===
source_type: pdf
s2_id: ""
date_added: 2026-05-22
ingested_date: 2026-05-22
ingest_version: 1
last_reviewed:

# === Classification ===
importance: 4
tier: TIER_1
tags: [tumor-metabolism, immunometabolism, tme, icb, car-t, oxphos, glycolysis, glutamine, methionine, asparagine, arginine, tryptophan, ido1, idh-mutation, lactate, mdsc, tam, t-cell-exhaustion, oncology-therapeutics, review]
keywords: ["tumour microenvironment metabolic immunosuppression", "Warburg effect cancer", "OxPhos vs glycolytic DLBCL", "GAPDH metabolic biomarker", "nutrient competition immune cells", "glutamine SLC1A5 competition", "methionine SLC43A2 H3K79me2", "asparagine LCK TCR signalling", "IDO1 kynurenine pathway", "IDH1/IDH2 oncometabolite 2HG", "ASNase OxPhos DLBCL extension", "CAR-T metabolic conditioning", "MPC inhibition UK5099", "metformin AMPK CAR-T", "obesity paradox PD-1 TAM"]
domain: immunometabolism

# === Biomedical domain ===
tissue: [multi, in_vitro_only]
condition: [cancer]
disease_specific: [DLBCL, AML, glioma, ICC, melanoma, NSCLC, hepatocellular_carcinoma, PDAC, ALL, NKTCL, RCC, chondrosarcoma]
species: [human, mouse]
hypoxia_relevant: true
contains_immune_cells: true
contains_myeloid: true

# === Technique ===
techniques: [literature_review]
n_samples:
n_cells_total:
integration_method: ""

# === Biology captured ===
key_cell_types: [CD8_T_cell, NK_cell, M1_macrophage, M2_macrophage, MDSC, Treg, dendritic_cell, B_cell, CAR-T_cell, TAM]
key_markers: [GAPDH, LDH, MCT1, SLC1A5, SLC43A2, ARG1, ASS1, ASNS, IDO1, TDO, IDH1, IDH2, PD-1, PD-L1, CTLA-4, NFAT1, GLUT1, mTORC1, HIF-1α, STAT5, STAT3, NRF2, FOXP3, LCK]
key_pathways: [aerobic_glycolysis, OxPhos, glutaminolysis, kynurenine_pathway, arginine_urea_cycle, methionine_SAM_cycle, asparagine_synthesis, lactate_acidosis_pH_regulation, mTORC1_glycolysis, fatty_acid_oxidation, TCA_cycle, ICB_PD1_CTLA4]

# === User project membership ===
projects: [thesis, hypoxia]
priority: core
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

Cancer cells reprogram their own metabolism (Warburg effect, glutaminolysis, lipid remodelling) and reshape the tumour microenvironment (TME) — nutrient depletion, lactic acidosis, oncometabolite accumulation — in ways that simultaneously sustain tumour growth and impair the antitumour immune response. Despite extensive preclinical evidence that metabolic vulnerabilities can be exploited therapeutically, clinical translation has been almost universally disappointing: of dozens of metabolic inhibitors trialled in oncology, only L-asparaginase and mIDH inhibitors are approved. The review's central question: how should we redesign metabolic-targeting strategies so that they enhance immunotherapy rather than disable it?

## Key idea

Reframe metabolic targeting as an **immuno-metabolic combination problem**, not a single-target exercise. The TME is a competitive metabolic battleground where tumour, stromal, myeloid, and lymphoid cells compete for the same nutrients (glucose, glutamine, arginine, methionine, asparagine, tryptophan) and adapt to the same metabolites (lactate, 2HG, kynurenine). Effective strategies must (i) stratify tumours by metabolic phenotype (e.g., GAPDH-based [[concepts/oxphos-vs-glycolytic-tumor-metabolic-heterogeneity|OxPhos vs glycolytic DLBCL]]), (ii) target tumour metabolism while sparing — or actively boosting — immune metabolism, (iii) combine with ICB or with ex-vivo CAR-T metabolic conditioning rather than testing as monotherapy in unselected populations.

## Method

Narrative review (no original primary data). Curates and synthesises:

- Tumour bioenergetic phenotyping (Warburg, OxPhos heterogeneity, DLBCL stratification).
- Nutrient-competition mechanisms (glucose, glutamine, arginine, methionine, asparagine, tryptophan).
- Metabolite accumulation effects (lactate, kynurenine, 2HG).
- Clinical-trial landscape (ASNase, IDH inhibitors, IDO1 inhibitors, ARG inhibitors, ADI-PEG20).
- ICB combination strategies and the [[concepts/obesity-paradox-tam-pd1-glycolysis|obesity paradox]].
- CAR-T cell metabolic conditioning (pharmacological and genetic).

## Results

- Within-entity tumour metabolic heterogeneity is biomarker-actionable: GAPDH protein discriminates OxPhos-vs-glycolytic DLBCL and predicts ASNase response.
- Stromal/myeloid glucose consumption depletes TME glucose; GLUT1 down-regulation and Ca2+-NFAT1 impairment cripple T-cell function; glycolytic signatures inversely correlate with immune infiltration in melanoma/NSCLC ACT cohorts.
- Lactate efflux with H+ via MCT1/MCT4 acidifies the TME; effector T and NK cells are inhibited while FOXP3+ Tregs are resistant; bicarbonate-transporter SLC4A4 inhibition rescues anti-tumour immunity in PDAC.
- Tumour SLC1A5 outcompetes myeloid cells for glutamine → ER stress via IRE1α/XBP1 and GPR109A → immunosuppressive myeloid polarisation; GLS1 inhibition (CB-839) reshapes MDSC/M1 balance.
- M2-like macrophages depend on glutaminolysis-derived α-KG; GLUL ablation shifts macrophages to M1-like state via glycolysis and HIF-1α.
- Asparagine binds LCK and directly enhances TCR-proximal signalling; ASNase-mediated Asn depletion impairs CD8 activation but later induces NRF2-mediated adaptation; ASNase is approved for ASNS-silenced ALL/NKTCL and extends to OxPhos-dependent DLBCL.
- Tumour SLC43A2 sequesters methionine, lowering T-cell SAM and H3K79me2 → STAT5/IL-2 signalling deficit; tumour-specific SLC43A2 invalidation restores ICB efficacy.
- IDO1/TDO drive tryptophan catabolism → kynurenine; epacadostat + pembrolizumab phase 3 (ECHO-301) failed; new biomarker-stratified trials ongoing.
- MDSC ARG1 depletes TME arginine, suppressing T-cell function; ARG inhibition restores immunity, but ADI-PEG20 systemic arginine depletion is also detrimental to TILs.
- mIDH1/mIDH2 mutations produce 2HG, silence cGAS via hypermethylation, exclude T cells; ivosidenib (AG-120), enasidenib, and brain-penetrant vorasidenib restore T-cell infiltration and are FDA-approved.
- Tumour glycolysis induces high T-cell PD-1, reducing ICB efficacy; the obesity paradox (Bader/Voss/Rathmell 2024) is mechanistically explained by mTORC1-glycolysis-driven PD-1 on TAMs.
- Ex-vivo CAR-T metabolic conditioning (UK-5099 MPC inhibition, MCT1 inhibition, LDH inhibition, metformin, glucose restriction, bicarbonate) and genetic edits (Regnase-1 KO, PRODH2/PGC1α/FH OE, A2AR KO, ARG modulation) improve memory differentiation and persistence.
- Only ASNase and IDH inhibitors are clinically approved metabolic-targeted oncology drugs; most others (notably complex-I inhibitors) failed due to toxicity, plasticity, or lack of biomarker selection.

## All claims (exhaustive)

- `[c01]` Human tumours show within-entity metabolic heterogeneity (glycolytic vs OxPhos) (p.2) — "Within the same tumor entity, some tumors heavily rely on glycolysis and lactate production, while others predominantly depend on mitochondrial function" — confidence: high — type: correlational — links: [[concepts/oxphos-vs-glycolytic-tumor-metabolic-heterogeneity]] [[claims/cancer-metabolic-heterogeneity-glycolytic-vs-oxphos-tumors]]
- `[c02]` GAPDH protein expression discriminates OxPhos vs glycolytic DLBCL and predicts ASNase response (p.2, p.6) — "we reported that glyceraldehyde 3-phosphate dehydrogenase (GAPDH) expression serves as an excellent marker of the metabolic status of DLBCL tumors" — confidence: high — type: methodological — links: [[foundations/gapdh]] [[concepts/oxphos-vs-glycolytic-tumor-metabolic-heterogeneity]] [[claims/gapdh-biomarker-glycolytic-vs-oxphos-dlbcl]]
- `[c03]` Glucose depletion in TME impairs Ca2+-NFAT1 signaling in T cells (p.3) — "Studies in murine models have demonstrated that limited glucose availability hampers the Ca2+-NFAT1 (nuclear factor of activated T cells 1) signaling pathway in T cells, thereby impairing their function" — confidence: high — type: mechanistic — links: [[concepts/nutrient-competition-tumor-immune-cells-tme]] [[claims/glucose-depletion-tme-impairs-tcell-ca-nfat1-signaling]]
- `[c04]` Glycolytic gene signature inversely correlates with immune infiltration in melanoma/NSCLC patients on ACT (p.3) — "the genetic signature of glycolysis inversely correlates with immune cell infiltration in patients with melanoma or non-small cell lung cancer (NSCLC) who have received adoptive T cell therapy" — confidence: medium — type: correlational — links: [[claims/glycolytic-signature-inverse-immune-infiltration-melanoma-nsclc]]
- `[c05]` Tumour lactate efflux acidifies TME and suppresses CD8/NK while sparing FOXP3+ Tregs (p.3) — "regulatory T cells (CD4+, CD25+, and FOXP3+ cells) exhibit resistance to the antiproliferative effect of lactate ... lactate is co-transported with a proton (H+) ... contributes to the acidification of the TME ... primary reason for lactate's ability to limit the anticancer immune response" — confidence: high — type: mechanistic — links: [[concepts/lactate-acidification-tme-immunosuppression]] [[foundations/ldh-lactate-dehydrogenase]] [[foundations/mct1-monocarboxylate-transporter-1]] [[claims/tumor-lactate-acidifies-tme-spares-tregs-suppresses-effector]]
- `[c06]` SLC4A4 bicarbonate-transporter inhibition mitigates PDAC acidosis and improves anticancer immunity (p.3) — "inhibition of the bicarbonate transporter solute carrier family 4 member 4 in pancreatic ductal adenocarcinoma mitigates the acidosis and improves the anticancer immune response" — confidence: medium — type: pharmacological — links: [[concepts/lactate-acidification-tme-immunosuppression]] [[claims/slc4a4-inhibition-pdac-mitigates-acidosis-restores-immunity]]
- `[c07]` Tumour SLC1A5 upregulation drives glutamine starvation of myeloid cells via IRE1α/XBP1 ER stress and GPR109A (p.4) — "Yang et al. identified glutamine competition between cancer cells and myeloid cells mediated by the upregulation of the glutamine transporter SLC1A5 in tumor cells, leading to glutamine scarcity in liver cancer TMEs ... triggers endoplasmic reticulum stress in myeloid cells, promoting their immunosuppressive polarization via the inositol-requiring enzyme-1a and X-box binding protein 1 pathway (IRE1a/XBP1) and increasing G-protein coupled receptor 109A (GPR109A) expression" — confidence: high — type: mechanistic — links: [[foundations/slc1a5-asct2-glutamine-transporter]] [[concepts/glutamine-asymmetric-metabolism-tumor-immune]] [[claims/tumor-slc1a5-glutamine-competition-ire1a-xbp1-myeloid-suppression]]
- `[c08]` GLS1 inhibition with CB-839 reshapes MDSC/M1 balance and synergises with ICB preclinically (p.4, p.8) — "In breast cancer models, inhibiting glutamine metabolism reduced tumor growth by decreasing the recruitment of the immunosuppressive MDSC and promoting M1-like macrophage conversion ... CB-839 ... demonstrated enhanced effectiveness when combined with anti-PD-1 and anti-PD-L1 antibodies in preclinical models, including melanoma" — confidence: medium — type: pharmacological — links: [[foundations/cb-839-telaglenastat]] [[concepts/glutamine-asymmetric-metabolism-tumor-immune]] [[claims/gls1-inhibition-cb839-shifts-macrophage-mdsc-balance]]
- `[c09]` Glutaminolysis-derived α-KG drives M2 macrophage polarisation; GLUL ablation shifts to M1 via HIF-1α (p.4) — "M2-like macrophages depend heavily on glutamine metabolism, with α-KG ... promoting their polarization toward an immunosuppressive state ... inhibiting or genetically ablating glutamine synthetase (GLUL) in macrophages fosters an M1-like phenotype via enhanced glycolysis and hypoxia-inducible factor (HIF)-1a activation" — confidence: high — type: mechanistic — links: [[concepts/glutamine-asymmetric-metabolism-tumor-immune]] [[concepts/m1-m2-polarization-paradigm]] [[claims/glutamine-driven-m2-polarization-akg-glul-axis]]
- `[c10]` Asparagine directly enhances CD8 activation by binding LCK; Asn restriction impairs activation, NRF2 partially rescues (p.4) — "asparagine (Asn) depletion inhibits CD8+ T cell activation ... directly enhances CD8+ T cell activation and antitumor immunity by binding to the tyrosine kinase lymphocyte cell-specific protein-tyrosine kinase (LCK) and promoting its phosphorylation ... prolonged Asn restriction leads to the induction of nuclear factor erythroid 2-related factor 2 (NRF2)" — confidence: high — type: mechanistic — links: [[concepts/asparagine-tcell-activation-lck-axis]] [[claims/asparagine-restriction-suppresses-cd8-asn-lck-tcr-signaling]]
- `[c11]` ASNase is FDA-approved for ASNS-silenced ALL/NKTCL and recently extends to OxPhos-dependent DLBCL (p.4, p.6) — "Currently, ASNase is used clinically only for ALL and NKTCL ... We recently established that patients with DLBCL whose tumors are highly dependent on OxPhos for energy production showed a complete response to ASNase-based treatment" — confidence: high — type: pharmacological — links: [[foundations/l-asparaginase-asnase]] [[concepts/oxphos-vs-glycolytic-tumor-metabolic-heterogeneity]] [[claims/asnase-approved-asns-silenced-malignancies-oxphos-dlbcl-extension]]
- `[c12]` Tumour SLC43A2 outcompetes T cells for methionine, lowering H3K79me2/STAT5/IL-2 signaling; tumour-specific invalidation restores ICB efficacy (p.5) — "tumor cells often overexpress the methionine transporter SLC43A2 ... allowing them to outcompete T cells for methionine, disrupting T cell metabolism and decreasing intracellular SAM levels ... loss of dimethylation at histone H3 lysine 79 (H3K79me2), which is crucial for STAT5 expression and T cell activation ... tumor-specific invalidation of SLC43A2 ... resulted in an increased effect of immunotherapies" — confidence: high — type: mechanistic — links: [[foundations/slc43a2-lat4-methionine-transporter]] [[concepts/methionine-competition-slc43a2-stat5-tcell]] [[claims/slc43a2-methionine-competition-h3k79me2-stat5-tcell-impairment]]
- `[c13]` IDO1/TDO drive tryptophan catabolism → kynurenine immunosuppression; epacadostat phase 3 failed in melanoma; new biomarker trials ongoing (p.5) — "dysregulated activity of IDO1 and TDO can inhibit antitumor immunity ... phase 1/2 trials of epacadostat ... showed potential benefits when combined with ICB in patients with advanced melanoma, the phase 3 study did not demonstrate improvements in progression-free survival or overall survival ... being revisited with new trials with different patient selection" — confidence: high — type: pharmacological — links: [[foundations/ido1-indoleamine-dioxygenase]] [[foundations/kynurenine]] [[foundations/epacadostat]] [[concepts/tryptophan-ido1-kynurenine-immunosuppression]] [[concepts/ahr-tam-immunosuppression-tumour]] [[claims/ido1-tdo-immunosuppression-monotherapy-failure-epacadostat-phase3]]
- `[c14]` MDSC ARG1 depletes TME arginine and suppresses T cells; ARG inhibition restores immunity but ADI-PEG20 also strips TIL arginine (p.5, p.10) — "MDSCs expressing ARG deplete arginine in the TME, thereby suppressing antitumor T cell responses ... Inhibiting ARG can restore arginine levels, resulting in tumor regression and enhanced T cell function ... ADI-PEG20 also depletes arginine levels in T cells within the TME, impairing their function" — confidence: high — type: pharmacological — links: [[foundations/arg1-arginase-1]] [[foundations/adi-peg20]] [[concepts/arginase-mdsc-arginine-depletion-tcell]] [[claims/arg-mdsc-arginine-depletion-tcell-suppression-arg-inhibition]]
- `[c15]` mIDH1/mIDH2 mutations produce 2HG, silence cGAS, exclude T cells; ivosidenib, enasidenib, vorasidenib FDA-approved and restore T-cell infiltration (p.6, p.10) — "gain-of-function mutations in IDH1 or IDH2 were identified in 10%–20% of patients with acute myeloid leukemia ... IDH mutations are associated with elevated levels of 2-hydroxyglutarate (2HG), an oncometabolite ... IDH1-mutant solid tumors exhibit selective hypermethylation and silencing of the cytoplasmic double-stranded DNA sensor cGAS ... AG120 (ivosidenib, which is approved for the treatment of patients with ICC) leads to DNA hypomethylation and activation of cGAS transcription, thereby inducing a strong antitumor T cell response" — confidence: high — type: pharmacological — links: [[foundations/ivosidenib-ag120]] [[foundations/vorasidenib]] [[foundations/2-hydroxyglutarate]] [[concepts/idh1-2-mutation-2hg-immune-exclusion]] [[claims/idh1-2-mutation-2hg-immune-exclusion-cgas-silencing-inhibitor-rescue]]
- `[c16]` Tumour glycolysis induces high T-cell PD-1, lowering ICB efficacy; inhibiting glycolytic genes restores ICB (p.8) — "tumor cell glycolysis induces high PD-1 expression in T cells, reducing the efficacy of immune checkpoint therapy. Conversely, inhibiting glycolytic gene expression in tumor cells can enhance the effectiveness of immune checkpoint therapy" — confidence: medium — type: mechanistic — links: [[concepts/lactate-acidification-tme-immunosuppression]] [[foundations/pd-l1-cd274]] [[claims/tumor-glycolysis-induces-tcell-pd1-reducing-icb-efficacy]]
- `[c17]` Obesity-induced inflammation drives mTORC1-glycolysis-mediated PD-1 on TAMs; anti-PD-1 enhances TAM glycolysis and antigen presentation, explaining the obesity paradox (p.7) — "obesity-induced chronic inflammation selectively triggered PD-1 expression on TAMs through mTORC1 and glycolysis pathways. PD-1 acted as a negative regulator for TAMs, diminishing their glycolysis, phagocytosis, and T cell activation abilities. Blocking PD-1 enhanced macrophage glycolysis ... Myeloid-specific PD-1 deficiency slowed tumor progression, boosted TAM glycolysis and antigen presentation" — confidence: high — type: mechanistic — links: [[concepts/obesity-paradox-tam-pd1-glycolysis]] [[foundations/pd-l1-cd274]] [[claims/obesity-mtorc1-tam-pd1-glycolysis-mechanism-obesity-paradox]]
- `[c18]` MPC inhibition (UK-5099), MCT1 inhibition, LDH inhibition, metformin and bicarbonate ex-vivo conditioning improve CAR-T memory and persistence (p.8) — "genetic deletion and chemical inhibition of the mitochondrial pyruvate carrier (MPC) promote CD8+ T cell differentiation toward a memory phenotype ... CAR-T cells conditioned in vitro with UK5099 ... metformin ... LDH inhibitor has been demonstrated to influence cytokine-mediated T cell differentiation, enhancing the stemness and antitumor activity of CAR-T cells" — confidence: high — type: pharmacological — links: [[foundations/uk5099-mpc-inhibitor]] [[foundations/metformin]] [[concepts/car-t-metabolic-conditioning-persistence]] [[concepts/car-t-cell-therapy]] [[claims/mpc-mct1-ldh-metformin-conditioning-improves-cart-memory-persistence]]
- `[c19]` Genetic edits (Regnase-1 KO, PRODH2/PGC1α/FH OE, A2AR KO, ARG modulation) enhance CAR-T antitumour function and persistence (p.9) — "the knockout of Regnase-1 and overexpression of PRODH2 and PGC1a promote mitochondrial OxPhos and memory formation ... detrimental effects of tumor-derived metabolites, such as fumarate and adenosine, on CAR-T cells can be alleviated by overexpressing fumarate hydratase or knocking down the adenosine A2A receptor ... ASS, OTC, ARG1, and ARG2—can improve the cytotoxicity of antitumor CAR-T cells" — confidence: medium — type: methodological — links: [[concepts/car-t-metabolic-conditioning-persistence]] [[claims/genetic-modification-cart-prodh2-fh-a2ar-regnase-enhances-antitumor]]
- `[c20]` Only ASNase and IDH inhibitors are clinically approved metabolic oncology drugs; most metabolic inhibitors (notably complex-I) failed due to toxicity or tumour plasticity (p.6, p.10) — "out of the dozens of molecules tested in clinical phase, only two have received approval for cancer treatment in humans (L-asparaginase and IDH inhibitors) ... complex I inhibitors initially showed promise but often result in significant toxicity" — confidence: high — type: pharmacological — links: [[foundations/l-asparaginase-asnase]] [[foundations/ivosidenib-ag120]] [[foundations/vorasidenib]] [[claims/metabolic-inhibitor-clinical-translation-asnase-idh-only-approved]]

## Discussion captured

### Authors' interpretation

Ricci frames cancer metabolism not as a tumour-cell-only problem but as a competitive ecosystem in which tumour, stromal, myeloid, and lymphoid cells share substrates and metabolites. Therapeutic failure of metabolic monotherapies follows from this: blocking one nutrient axis routinely impairs antitumour immunity alongside the tumour. The way forward is biomarker-guided combination with immunotherapy, plus ex-vivo CAR-T metabolic conditioning, where the inhibitor is applied to cells, not patients. Two prior author successes are highlighted: DLBCL GAPDH-based stratification and ASNase response prediction.

### Comparisons with prior literature (made by authors)

- Cites Swanton 2024 Cell ("Hallmarks of systemic disease") for the TME ecosystem framework.
- Builds on Bader/Voss/Rathmell 2020 Mol Cell ("Targeting metabolism to improve TME"), De Martino 2024 Nat Rev Immunol, and Fendt 2024 Cell (Warburg centenary).
- Highlights Caro 2012 Cancer Cell (DLBCL OxPhos vs glycolytic subtypes) as foundational.
- Cites Apostolova & Pearce review on lactate and effector T-cell function.
- Cites Bian 2020 Nature for methionine-SLC43A2-H3K79me2.
- Cites Yang et al. for SLC1A5-IRE1α-XBP1 myeloid axis.
- Cites Bader/Voss/Rathmell 2024 for obesity-paradox TAM PD-1 mTORC1.
- Cites Pham 2018 for STAT5BN642H and INDIGO trial for vorasidenib (cross-link to [[papers/jak-stat-signaling-maintains-homeostasis-cells]]).

### Mechanistic hypotheses proposed

- "Targeting glutamine transporters, such as SLC1A5, or downstream signaling pathways could restore glutamine availability to immune cells, reprogramming the TME to favor antitumor immunity" (p.4).
- The obesity paradox is mechanistically explained by TAM PD-1 induction via mTORC1-glycolysis (p.7).
- Metabolic conditioning of CAR-T cells ex vivo is a "safe, efficient, and readily applicable" route to memory-biased products (p.8).
- Tumour metabolic phenotype is more clinically informative than mRNA omics — protein and metabolomic measurement at the tumour itself is needed (p.10).

### Caveats and self-criticism

- Author acknowledges that mRNA omics underrepresents in-vivo enzyme activity (ASNS expression case).
- Standard culture media misrepresent mammalian plasma metabolism; immunodeficient-mouse-cell-line studies do not capture immune component.
- Many metabolic inhibitors that look promising preclinically fail clinically because of plasticity, toxicity, and absence of biomarker selection.

### Future directions suggested

- Develop clinically practical metabolic-phenotyping methods (in-vivo carbon tracing, spatial metabolomics).
- Combine metabolic inhibitors with ICB based on biomarker-driven patient selection.
- Use nanoparticles or antibody-coupled molecules to deliver metabolic inhibitors selectively to tumour cells.
- Build immunocompetent spontaneous-tumour models to test metabolic immunotherapies.
- Personalised approaches accounting for diet, obesity, diabetes, microbiota.

## Limitations

- Narrative review, no original primary data.
- Heavy emphasis on the author's own DLBCL/ASNase work; some axes (lipid metabolism, secreted nucleotides) deliberately deferred to other reviews.
- Coverage of certain emerging axes (lactylation post-translational mod, microbiota-metabolite signalling) is light.
- Citation balance is reviewer-skewed; not a systematic review.

## Open questions

### Open questions raised by authors

- How to develop clinically compatible methods to phenotype tumour metabolism non-invasively?
- Can metabolic inhibitors be made tumour-selective via nanoparticle or antibody-coupled delivery?
- Will biomarker-stratified IDO1 trials succeed where unselected trials failed?
- Does CB-839 + nivolumab (NCT02771626) show clinical benefit?
- Can immunocompetent spontaneous-tumour models replace cell-line xenografts for metabolic immunotherapy testing?

### Open questions identified during ingest

- How does the metabolic landscape under hypoxia (relevant to thesis) reshape immune metabolism? E.g., is the lactate-acidosis-Treg-sparing asymmetry amplified in hypoxic niches?
- Are tumour metabolic phenotypes (OxPhos vs glycolytic) stable across spatial niches, or do they shift with hypoxia / nutrient gradients?
- Cross-link to [[papers/jak-stat-signaling-maintains-homeostasis-cells]]: does tonic JAK-STAT signalling cross-talk with TME metabolic state — i.e., does baseline ISG signalling change under glucose / glutamine / methionine depletion in TILs?
- Cross-link to [[papers/atlas-guided-discovery-transcription-factors-cell]]: do metabolic stresses (lactate, low Met, low Asn) shift TF programmes captured in the multi-state TF atlas?
- Is there a unifying biomarker (e.g., extracellular pH + lactate + GAPDH IHC) that could stratify patients across multiple metabolic-immunotherapy combinations?

## My take

This is the most useful single review I have read on tumour metabolic immunosuppression — comprehensive in scope, honest about the clinical-translation failures, and clearly oriented toward "combine, stratify, condition" rather than "inhibit-and-hope." For my thesis, three takeaways:

1. **OxPhos-vs-glycolytic stratification is the model**: GAPDH-IHC-style biomarkers for tumour metabolic phenotype are practically deployable and should be a default companion to any combination metabolic-immune trial.
2. **Hypoxia + lactate-acidosis are interlocking**: my hypoxia-driven thesis work intersects this review on multiple axes — HIF1α drives glycolysis (Warburg), lactate efflux acidifies TME, hypoxic niches harbour the most immune-suppressive TAMs (link with [[concepts/hypoxia-pd-l1-tam-immune-evasion]] and [[concepts/lactate-driven-tam-m2-polarization]]).
3. **CAR-T metabolic conditioning is the pragmatic frontier**: applying inhibitors ex vivo rather than to patients bypasses systemic toxicity and creates a clinically deployable lever — and the Moraly et al. companion review identifies the gene-edit cocktail to combine.

The recurring clinical lesson — that monotherapy and unselected populations doom metabolic inhibitors — is the most important takeaway from a translational perspective.

## Related

- [[concepts/oxphos-vs-glycolytic-tumor-metabolic-heterogeneity]]
- [[concepts/nutrient-competition-tumor-immune-cells-tme]]
- [[concepts/lactate-acidification-tme-immunosuppression]]
- [[concepts/glutamine-asymmetric-metabolism-tumor-immune]]
- [[concepts/methionine-competition-slc43a2-stat5-tcell]]
- [[concepts/asparagine-tcell-activation-lck-axis]]
- [[concepts/arginase-mdsc-arginine-depletion-tcell]]
- [[concepts/tryptophan-ido1-kynurenine-immunosuppression]]
- [[concepts/idh1-2-mutation-2hg-immune-exclusion]]
- [[concepts/car-t-metabolic-conditioning-persistence]]
- [[concepts/obesity-paradox-tam-pd1-glycolysis]]
- [[concepts/car-t-cell-therapy]]
- [[concepts/warburg-effect-hif1a-glycolytic-reprogramming]]
- [[concepts/lactate-driven-tam-m2-polarization]]
- [[concepts/hif-dependent-glycolysis-immune-cell-differentiation]]
- [[concepts/immune-checkpoint-blockade]]
- [[concepts/tumour-immune-microenvironment]]
- [[concepts/m1-m2-polarization-paradigm]]
- [[concepts/ahr-tam-immunosuppression-tumour]]
- [[foundations/gapdh]]
- [[foundations/ldh-lactate-dehydrogenase]]
- [[foundations/mct1-monocarboxylate-transporter-1]]
- [[foundations/slc1a5-asct2-glutamine-transporter]]
- [[foundations/slc43a2-lat4-methionine-transporter]]
- [[foundations/l-asparaginase-asnase]]
- [[foundations/cb-839-telaglenastat]]
- [[foundations/metformin]]
- [[foundations/ivosidenib-ag120]]
- [[foundations/vorasidenib]]
- [[foundations/ido1-indoleamine-dioxygenase]]
- [[foundations/arg1-arginase-1]]
- [[foundations/epacadostat]]
- [[foundations/adi-peg20]]
- [[foundations/2-hydroxyglutarate]]
- [[foundations/uk5099-mpc-inhibitor]]
- [[foundations/kynurenine]]
- [[foundations/hif1a]]
- [[foundations/pd-l1-cd274]]
- [[people/jean-ehrland-ricci]]
