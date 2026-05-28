---
# === Identification ===
title: "Mitochondrial VHL rewires cell metabolism in hypoxia"
slug: mitochondrial-vhl-rewires-cell-metabolism-hypoxia
arxiv: ""
doi: "10.1016/j.cmet.2025.11.013"
pmid: "41435818"
venue: "Cell Metabolism"
year: 2026
authors:
  - "Guobang Li"
  - "Wenfeng Pan"
  - "Long Wu"
  - "Zhiliang Cai"
  - "Haoming Chen"
  - "Xingui Wu"
  - "Tiantian Yu"
  - "Kun Liao"
  - "Hui Zhang"
  - "Xingqiao Wen"
  - "Bo Li"
first_author: "Guobang Li"
corresponding_author: "Xingqiao Wen; Bo Li"

# === Source & metadata ===
source_type: pdf
s2_id: "6992df260f25bfaf4d8079d0e7d4fbb850bbe2cd"
date_added: 2026-05-28
ingested_date: 2026-05-28
ingest_version: 1
last_reviewed: null

# === Classification ===
importance: 4
tier: TIER_1
tags:
  - hypoxia
  - VHL
  - mitochondria
  - non-canonical-signaling
  - leucine
  - BCAA-metabolism
  - MCCC2
  - glutaminolysis
  - GDH
  - GLUD1
  - SRC
  - PRMT5
  - arginine-methylation
  - tyrosine-phosphorylation
  - mitochondrial-protein-import
  - TOM22
  - reductive-carboxylation
  - ccRCC
  - renal-ischemia-reperfusion
  - 13C-tracing
  - VHL-mutation-subtype
keywords:
  - mitochondrial VHL non-canonical hypoxia function
  - VHL-MCCC2 interaction inhibits leucine catabolism
  - leucine allosterically activates GDH to drive glutaminolysis
  - SRC phosphorylates VHL Y185 under hypoxia
  - PRMT5 methylates MCCC2 R292 to block VHL binding
  - hypoxic VHL self-ubiquitination and HIF1A shielding
  - type 2B VHL missense mutants gain mitochondrial function in ccRCC
domain: "metabolism / cell biology / hypoxia / oncology"

# === Biomedical domain ===
tissue:
  - kidney
  - in_vitro_only
condition:
  - cancer
  - healthy
disease_specific:
  - clear_cell_renal_cell_carcinoma_ccRCC
  - renal_ischemia_reperfusion_injury
  - VHL_disease
species:
  - human
  - mouse
hypoxia_relevant: true
contains_immune_cells: false
contains_myeloid: false

# === Technique ===
techniques:
  - immunoprecipitation_proteomics
  - 13C_15N_metabolic_tracing
  - subcellular_fractionation
  - immunofluorescence_confocal
  - super_resolution_microscopy
  - Phos-tag_analysis
  - in_vitro_kinase_assay
  - in_vitro_methyltransferase_assay
  - CRISPR_knockout
  - shRNA_knockdown
  - bulk_RNA-seq
  - qRT-PCR
  - western_blot
  - molecular_docking
  - GDH_activity_assay
  - synthetic_peptide_competition_assay
  - knock-in_mouse
  - renal_ischemia_reperfusion_model
  - xenograft_tumor_model
  - TCGA_survival_analysis
n_samples: null
n_cells_total: null
integration_method: ""

# === Biology captured ===
key_cell_types:
  - HEK293
  - MIA-PaCa-2
  - DLD1
  - RCC10
  - A498_ccRCC
key_markers:
  - VHL
  - MCCC2
  - MCCC1
  - GDH_GLUD1
  - PRMT5
  - SRC
  - TOM22
  - HIF1A
  - EPAS1_HIF2A
  - leucine
  - glutamine
key_pathways:
  - leucine_BCAA_catabolism
  - glutaminolysis_reductive_carboxylation
  - mitochondrial_protein_import_TOM_complex
  - hypoxia_HIF_signaling
  - VHL_ubiquitin_proteasome
  - SRC_tyrosine_phosphorylation
  - PRMT5_arginine_methylation

# === User project membership ===
projects:
  - hypoxia
  - thesis
priority: context
read_status: read

# === HypoxiaVERSE-specific ===
hypoxiaverse_status: excluded
exclusion_reason: "Mechanistic biochemistry/cell-biology paper (cell lines + knock-in mouse + xenografts), not a single-cell/immune hypoxia dataset. Retained as high-value mechanistic context for hypoxic metabolic reprogramming and a non-canonical, HIF-independent VHL function."
data_availability: "RNA-seq at NCBI BioSample; proteomics at ProteomeXchange (accessions in key resources table). No original code."

# === Cross-references ===
code_url: ""
cited_by: []
---

## Problem

Canonically, the VHL tumor suppressor is the substrate-recognition subunit of an E3 ubiquitin ligase that, under normoxia, targets prolyl-hydroxylated HIF-α subunits for degradation. Under hypoxia, HIF-α hydroxylation is attenuated, VHL can no longer recognize HIF-α, and VHL is generally regarded as a passive "standby adaptor." Whether VHL has active, non-canonical roles during hypoxia — when its canonical substrate engagement is lost — was unknown. Resolving this matters because HIF dysregulation cannot explain all VHL-disease and ccRCC phenotypes, hinting at HIF-independent VHL functions.

## Key idea

Under chronic hypoxia, most cytosolic VHL is degraded (via self-ubiquitination once HIF1A no longer shields the complex), while a residual VHL pool translocates into the mitochondria through the TOM complex. Mitochondrial VHL binds MCCC2 and disrupts the MCCC complex, inhibiting leucine catabolism. The resulting leucine accumulation allosterically activates glutamate dehydrogenase (GDH), boosting glutaminolysis to produce the lipids and nucleotides needed for hypoxic cell growth. The VHL–MCCC2 interaction is governed by a dual, oxygen-responsive PTM switch: SRC phosphorylates VHL Y185 (enabling) and represses PRMT5-mediated MCCC2 R292 methylation (de-blocking). The axis operates in vivo (renal ischemia-reperfusion) and is clinically associated with ccRCC VHL-mutation subtypes. The paper reframes VHL as a bona fide, HIF-independent regulator of hypoxic mitochondrial metabolism.

## Method

Human cell lines (HEK293, MIA-PaCa-2, DLD1, and the VHL-deficient ccRCC line RCC10; xenograft-competent A498) were studied at 1% O₂ (hypoxia) vs 21% O₂ (normoxia), with CRISPR VHL knockout and reconstitution of VHL WT and engineered mutants. Approaches included subcellular fractionation and confocal/super-resolution imaging (mitochondrial VHL), co-IP proteomics (VHL interactome), domain mapping and charge mutants (VHL M1/M2 import-dead), CHX/MG132 stability and ubiquitination assays, ¹³C/¹⁵N metabolic tracing of leucine and glutamine, in vitro GDH activity assays with the leucine-insensitive R204M mutant, Phos-tag and in vitro kinase assays (SRC, eCF506 inhibitor), in vitro methyltransferase assays (PRMT5, SAM), protein–protein docking, and synthetic-peptide competition. In vivo, a VhlY151F/Y151F knock-in mouse (equivalent to human VHL Y185F) was subjected to renal ischemia-reperfusion with pharmacology (BCAT-IN-2, R162, eCF506, dietary leucine). Clinical relevance was assessed with ccRCC VHL-mutant panels, xenografts, and TCGA-KIRC survival analyses.

## Results

Hypoxia split VHL into a degraded cytosolic pool and a mitochondrially imported pool. Import depended on positively charged VHL α-domain helices recognized by TOM22; import-dead VHL M2 abolished the hypoxic growth advantage. Mitochondrial VHL bound MCCC2 and disrupted the MCCC complex; MCCC2 depletion phenocopied VHL's hypoxic growth promotion. Tracing showed VHL suppressed leucine→acetyl-CoA flux while stimulating glutaminolysis into lipids and nucleotides; glutamine was required, and citrate+nucleosides rescued VHL-deficient cells. α-KIC/BCAT-inhibitor epistasis proved leucine accumulation (not catabolites) was the driver, acting through GDH (leucine-insensitive GDH R204M abolished the phenotype) rather than mTOR (suppressed in hypoxia). The VHL–MCCC2 interaction required SRC-mediated VHL Y185 phosphorylation and was blocked by PRMT5-mediated MCCC2 R292 dimethylation; SRC simultaneously phosphorylated PRMT5 (Y283) to lift that block under hypoxia. VhlY151F mice suffered worse renal ischemia-reperfusion injury, relieved by BCAT-IN-2 or dietary leucine and reversed by GDH inhibition. Type 2B ccRCC missense VHL mutants gained enhanced mitochondrial enrichment, stronger VHL–MCCC2 binding and faster tumor growth; TCGA missense-VHL tumors progressed faster than truncating ones.

## All claims (exhaustive)

- `[c01]` Chronic hypoxia degrades cytosolic VHL while a residual pool enters mitochondria (p.174–175) "most cytosolic VHL is degraded under chronic hypoxia, with the remaining VHL pool primarily translocating to the mitochondria" — confidence: high — type: mechanistic — links: [[claims/chronic-hypoxia-degrades-cytosolic-vhl-while]] [[concepts/mitochondrial-vhl-noncanonical-hypoxia-function]] [[foundations/vhl-von-hippel-lindau]]
- `[c02]` Hypoxic VHL is self-ubiquitinated at K171/K196 when HIF1A no longer shields the complex (p.175–176) "hypoxic VHL ubiquitination was abolished by mutations at K171 and K196" — confidence: high — type: mechanistic — links: [[claims/hypoxic-vhl-self-ubiquitinated-k171-k196]] [[concepts/hypoxic-vhl-self-ubiquitination-hif1a-shielding]] [[foundations/hif1a]]
- `[c03]` VHL is imported into mitochondria via TOM22 recognition of positive α-domain helices (p.176–177) "These helical structures contain positively charged residues that can be recognized by the translocase of the mitochondrial outer membrane (TOM) complex" — confidence: high — type: mechanistic — links: [[claims/vhl-enters-mitochondria-tom22-recognition-alpha]] [[concepts/mitochondrial-vhl-noncanonical-hypoxia-function]] [[foundations/tom22-mitochondrial-import-receptor]]
- `[c04]` Mitochondrial VHL binds MCCC2 and disrupts the MCCC complex to inhibit leucine catabolism (p.177–178) "Mitochondrial VHL binds and inhibits 3-methylcrotonyl-coenzyme A carboxylase subunit 2 (MCCC2)" — confidence: high — type: mechanistic — links: [[claims/mitochondrial-vhl-binds-mccc2-disrupts-mccc]] [[concepts/vhl-mccc2-leucine-catabolism-inhibition]] [[foundations/mccc2-3-methylcrotonyl-coa-carboxylase]]
- `[c05]` MCCC2 depletion phenocopies VHL growth promotion in hypoxia but not normoxia (p.178) "the growth-promoting effects of VHL WT were fully mimicked by MCCC2 depletion in hypoxia, which did not occur in normoxia" — confidence: high — type: methodological — links: [[claims/mccc2-depletion-phenocopies-vhl-growth-promotion]] [[concepts/vhl-mccc2-leucine-catabolism-inhibition]] [[foundations/mccc2-3-methylcrotonyl-coa-carboxylase]]
- `[c06]` Mitochondrial VHL reduces leucine-derived citrate and acetyl-CoA in hypoxia (p.178–179) "enrichments in citrate and citrate-derived intermediates from U-13C5 leucine were markedly reduced upon VHL WT but not M2 expression in hypoxia" — confidence: high — type: quantitative — links: [[claims/mitochondrial-vhl-reduces-leucine-derived-citrate]] [[concepts/vhl-mccc2-leucine-catabolism-inhibition]] [[foundations/leucine-bcaa]]
- `[c07]` Mitochondrial VHL stimulates glutaminolysis for lipids and nucleotides (p.179) "paradoxically stimulated glutaminolysis to produce acetyl-CoA in a much greater amount ... promoted both reductive lipogenesis and nucleotide production derived from glutamine" — confidence: high — type: mechanistic — links: [[claims/mitochondrial-vhl-stimulates-glutaminolysis-lipids-nucleotides]] [[concepts/leucine-allosteric-gdh-glutaminolysis-activation]] [[foundations/glud1-glutamate-dehydrogenase]]
- `[c08]` Glutamine is essential for VHL-promoted hypoxic growth; citrate+nucleosides rescue VHL-deficient cells (p.179) "glutamine deprivation abolished the growth advantage ... supplementation with citrate plus nucleosides completely rescued the growth defects in VHL-deficient cells" — confidence: high — type: methodological — links: [[claims/glutamine-essential-vhl-promoted-hypoxic-growth]] [[concepts/leucine-allosteric-gdh-glutaminolysis-activation]] [[foundations/slc1a5-asct2-glutamine-transporter]]
- `[c09]` Leucine accumulation, not downstream catabolites, drives the hypoxic VHL phenotype (p.179–180) "KIC supplementation rescued the growth defects in leucine-depleted cells, an effect blocked by co-treatment with a BCAT inhibitor BCAT-IN-2" — confidence: high — type: methodological — links: [[claims/leucine-accumulation-downstream-catabolites-drives-hypoxic]] [[concepts/leucine-allosteric-gdh-glutaminolysis-activation]] [[foundations/bcat-branched-chain-aminotransferase]]
- `[c10]` Leucine, but not isoleucine/valine, allosterically activates GDH dose-dependently (p.180) "leucine, rather than isoleucine or valine, enhanced GDH activity in a dose-dependent manner, covering the physiological range (1-10 μM)" — confidence: high — type: quantitative — links: [[claims/leucine-isoleucine-valine-allosterically-activates-gdh]] [[concepts/leucine-allosteric-gdh-glutaminolysis-activation]] [[foundations/glud1-glutamate-dehydrogenase]]
- `[c11]` Leucine-insensitive GDH R204M abolishes VHL-promoted reductive glutaminolysis and growth in hypoxia (p.180) "Reconstitution of GDH R204M in GDH-depleted cells compromised VHL-promoted cell proliferation and reductive glutaminolysis under hypoxia" — confidence: high — type: methodological — links: [[claims/leucine-insensitive-gdh-r204m-abolishes-vhl]] [[concepts/leucine-allosteric-gdh-glutaminolysis-activation]] [[foundations/glud1-glutamate-dehydrogenase]]
- `[c12]` Leucine repletion fails to activate mTOR under hypoxia, isolating GDH as the effector (p.180) "leucine repletion failed to activate mTOR in low oxygen conditions, likely because hypoxia markedly repressed mTOR activity" — confidence: medium — type: mechanistic — links: [[claims/leucine-repletion-fails-activate-mtor-hypoxia]] [[concepts/leucine-allosteric-gdh-glutaminolysis-activation]] [[foundations/mtor-kinase]]
- `[c13]` SRC phosphorylates VHL Y185 only under hypoxia, enabling the VHL–MCCC2 interaction (p.181–182) "VHL Y185 was phosphorylated by SRC solely under hypoxia" — confidence: high — type: mechanistic — links: [[claims/src-phosphorylates-vhl-y185-only-under]] [[concepts/src-vhl-y185-phosphorylation-mitochondrial-axis]] [[foundations/src-kinase]]
- `[c14]` SRC is hypoxia-induced via HIF-1 and HIF-2 through promoter HREs (p.182) "the hypoxia-promoted SRC activation was mediated by both HIF-1 and HIF-2" — confidence: medium — type: mechanistic — links: [[claims/src-hypoxia-induced-hif-hif-through]] [[concepts/src-vhl-y185-phosphorylation-mitochondrial-axis]] [[foundations/hif2a]]
- `[c15]` PRMT5 dimethylates MCCC2 R292 under normoxia to block the VHL–MCCC2 interaction (p.183–184) "only PRMT5 promoted MCCC2 methylation ... PRMT5 overexpression potentiated R292 dimethylation in MCCC2 to mitigate the hypoxic VHL-MCCC2 interaction" — confidence: high — type: mechanistic — links: [[claims/prmt5-dimethylates-mccc2-r292-under-normoxia]] [[concepts/prmt5-mccc2-arginine-methylation-oxygen-switch]] [[foundations/prmt5-arginine-methyltransferase]]
- `[c16]` SRC phosphorylates PRMT5 Y283 to inhibit MCCC2 R292 dimethylation under hypoxia (p.183–184) "SRC overexpression established the VHL-MCCC2 interaction in normoxia after HIF1A depletion by targeting Y283 ... The non-phosphorylatable PRMT5 Y283F mutation or SRC depletion restored the MCCC complex assembly" — confidence: medium — type: mechanistic — links: [[claims/src-phosphorylates-prmt5-y283-inhibit-mccc2]] [[concepts/prmt5-mccc2-arginine-methylation-oxygen-switch]] [[foundations/prmt5-arginine-methyltransferase]]
- `[c17]` VhlY151F knock-in mice show worsened renal ischemia-reperfusion injury, rescued by BCAT inhibition and dietary leucine (p.185–186) "BCAT-IN-2 markedly relieved the ischemia-reperfusion injury that could be blunted by R162 co-administration ... dietary leucine supplementation alleviated the renal ischemia-reperfusion injury especially in mutant kidneys" — confidence: high — type: mechanistic — links: [[claims/vhly151f-knock-mice-show-worsened-renal]] [[concepts/src-vhl-y185-phosphorylation-mitochondrial-axis]] [[foundations/bcat-in-2-inhibitor]]
- `[c18]` Type 2B VHL missense mutants enhance mitochondrial function and accelerate ccRCC progression (p.186–187) "Xenograft tumors carrying type 2B VHL mutants grew significantly faster than vector control tumors with type 1 mutants ... TCGA-collected ccRCC tumors with frameshift or nonsense VHL mutations (primarily type 1) progressed much slower than tumors with missense VHL mutations" — confidence: medium — type: correlational — links: [[claims/type-2b-vhl-missense-mutants-enhance]] [[concepts/type-2b-vhl-mutation-mitochondrial-gain-of-function-ccrcc]] [[foundations/tcga-the-cancer-genome-atlas]]

## Discussion captured

### Authors' interpretation

The authors argue that VHL is not a passive "standby adaptor" for HIFs under hypoxia but a "bona fide regulator of hypoxic metabolism within mitochondria." Losing canonical (cytosolic, HIF-degrading) function and gaining non-canonical (mitochondrial, MCCC2-inhibiting) function are mechanistically coupled: the same residues (K171/K196) used for self-ubiquitination overlap the TOM22-binding motif, so VHL is either degraded or imported. They frame the leucine→GDH→glutaminolysis route as an economical adaptation — avoiding leucine-derived acetyl-CoA (which would raise cytotoxic ROS under hypoxia) and instead drawing carbon/nitrogen from glutamine.

### Comparisons with prior literature (made by authors)

- Prior reports of low-level mitochondrial VHL in non-hypoxic conditions (refs 27, 31).
- WSB1 as a reported VHL E3 ligase that acts predominantly in normoxia (ref 33).
- SIRT4 loss disrupting the MCCC complex via MCCC1 acylation (ref 93) — contrasted with their VHL–MCCC2 mechanism.
- BCAT/BCAA deregulation in diabetes and cancer (glioma, leukemia, gastric, pancreatic) (refs 41, 44, 51, 80–86).
- PRMT5 as a target in MTAP-deleted tumors via methionine metabolism (refs 94, 95) — motivating proposed methionine–leucine crosstalk.
- Bovine GDH–leucine co-crystal structure (PDB: 8ar7, ref 59) anchoring the leucine-allostery and R204 mutant design.

### Mechanistic hypotheses proposed

- The VHL–MCCC2 interaction is governed by oxygen-responsive PTMs at VHL Y185 (phosphorylation) and MCCC2 R292 (methylation), with SRC as the convergent upstream sensor that both phosphorylates VHL and represses PRMT5.
- Hypoxia inhibits PRMT5 activity (not levels), suggesting a potential crosstalk between methionine/SAM and leucine metabolism exploitable therapeutically.

### Caveats and self-criticism

The authors note that VHL-loss in ischemic tissues yields complex phenotypes dependent on both HIF and VHL, which is why they engineered the separation-of-function VhlY151F knock-in (decoupling the mitochondrial axis from HIF regulation) rather than deleting Vhl.

### Future directions suggested

- Test mitochondrial VHL relevance in other hypoxic pathologies (myocardial ischemia, COPD).
- Determine whether VHL regulates other mitochondrial enzymes (TCA cycle, OXPHOS).
- Pursue dedicated clinical studies to assess translatability to renal cancer patients.
- Explore therapeutic exploitation of the methionine–leucine metabolic crosstalk.

## Limitations

- Most mechanistic work is in cell lines (HEK293, MIA-PaCa-2, DLD1, RCC10, A498) plus one knock-in mouse model and xenografts; broader tissue/in vivo generality is limited.
- The VHL–MCCC2 interface and the pY185–R292 hydrogen bond are derived from protein–protein docking models, not solved structures.
- Clinical evidence is correlative (TCGA-KIRC cohorts, n≈109 per group); no dedicated patient trial.
- K171/K196 are predicted ubiquitination sites; the HIF1A "shielding" model is inferred from depletion/fusion experiments.

## Open questions

### Open questions raised by authors

- Whether mitochondrial VHL matters in other hypoxia-related pathologies (myocardial ischemia, COPD).
- Whether VHL regulates additional mitochondrial enzymes (TCA cycle, OXPHOS).
- Whether the findings translate to renal cancer patients without dedicated clinical design.

### Open questions identified during ingest

- What governs the R167Q (type 2B) exception that does not gain mitochondrial function?
- Is the competitive ubiquitination-vs-import switch a general regulatory principle for substrate-empty E3 ligases?
- Could mutation-subtype-stratified metabolic targeting (SRC/BCAT/GDH inhibitors) be a precision strategy in missense-VHL ccRCC?

## My take

A genuinely paradigm-shifting paper: it converts VHL from a one-trick HIF-degrading adaptor into an oxygen-sensing, mitochondria-localized metabolic regulator, and ties the switch together with an elegant dual-PTM logic converging on SRC. The strongest evidence is the chain of separation-of-function reagents — import-dead VHL M2, MCCC2-binding-dead VHL Y185F, leucine-insensitive GDH R204M, and the VhlY151F knock-in — each isolating one node. The clinical (ccRCC mutation-subtype) and in vivo (renal ischemia) arms elevate it beyond a cell-biology curiosity. For a hypoxia-metabolism knowledge base this is high-value mechanistic context, even if it is not a single-cell dataset.

## Related

- [[concepts/mitochondrial-vhl-noncanonical-hypoxia-function]]
- [[concepts/vhl-mccc2-leucine-catabolism-inhibition]]
- [[concepts/leucine-allosteric-gdh-glutaminolysis-activation]]
- [[concepts/src-vhl-y185-phosphorylation-mitochondrial-axis]]
- [[concepts/prmt5-mccc2-arginine-methylation-oxygen-switch]]
- [[concepts/hypoxic-vhl-self-ubiquitination-hif1a-shielding]]
- [[concepts/type-2b-vhl-mutation-mitochondrial-gain-of-function-ccrcc]]
- [[concepts/warburg-effect-hif1a-glycolytic-reprogramming]] — complementary hypoxic metabolic reprogramming
- [[foundations/vhl-von-hippel-lindau]] · [[foundations/mccc2-3-methylcrotonyl-coa-carboxylase]] · [[foundations/glud1-glutamate-dehydrogenase]] · [[foundations/prmt5-arginine-methyltransferase]] · [[foundations/tom22-mitochondrial-import-receptor]] · [[foundations/bcat-branched-chain-aminotransferase]] · [[foundations/leucine-bcaa]]
