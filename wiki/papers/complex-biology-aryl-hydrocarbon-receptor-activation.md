---
title: "The complex biology of aryl hydrocarbon receptor activation in cancer and beyond"
slug: complex-biology-aryl-hydrocarbon-receptor-activation
arxiv: ""
doi: "10.1016/j.bcp.2023.115798"
pmid: "37696456"
venue: "Biochemical Pharmacology"
year: 2023
authors:
  - "Christiane A. Opitz"
  - "Pauline Holfelder"
  - "Mirja Tamara Prentzell"
  - "Saskia Trump"
first_author: "Christiane A. Opitz"
corresponding_author: "Christiane A. Opitz"
source_type: pdf
s2_id: "6a9d347795daf4b742836afe416c83afcfdbd000"
date_added: 2026-05-26
ingested_date: 2026-05-26
ingest_version: 1
last_reviewed:
importance: 4
tier: TIER_1
tags:
  - AHR
  - aryl-hydrocarbon-receptor
  - context-specificity
  - ARNT
  - AHRR
  - posttranslational-modifications
  - epigenetic-regulation
  - DNA-methylation
  - histone-modifications
  - non-genomic-AHR
  - tryptophan-metabolism
  - kynurenine
  - IDO1
  - TDO2
  - IL4I1
  - CYP1A1
  - TIPARP
  - HIF1A
  - HIF2A
  - SRC
  - vemurafenib
  - BRAFi-resistance
  - melanoma
  - tumor-suppression
  - tumor-promotion
  - SUMOylation
  - phosphorylation
  - ARNT2
  - HK2
  - TET2
  - CUL4B
  - UCHL3
  - review
keywords:
  - AHR activation
  - ligand diversity
  - AHR expression
  - ARNT
  - AHRR
  - non-genomic AHR effects
  - epigenetic regulation
  - posttranslational modifications
  - DNA methylation
domain: "oncology"

# === Biomedical domain ===
tissue: [multi, in_vitro_only]
condition: [cancer, autoimmune, healthy]
disease_specific: [glioblastoma, acute_lymphoblastic_leukemia, NSCLC, prostate_cancer, hepatocellular_carcinoma, melanoma, breast_cancer, systemic_lupus_erythematosus, rheumatoid_arthritis]
species: [human, mouse]
hypoxia_relevant: true
contains_immune_cells: true
contains_myeloid: true

# === Technique ===
techniques: [literature_review, Cryo-EM_structural, ChIP-seq, mass_spectrometry_PTM, DNA_methylation_EPIC, RNA-seq]
n_samples:
n_cells_total:
integration_method: ""

# === Biology captured ===
key_cell_types:
  - T cell
  - macrophage
  - tumor-associated macrophage
  - keratinocyte
  - hepatocyte
  - B cell
  - intestinal epithelial cell
  - regulatory T cell
key_markers:
  - AHR
  - ARNT
  - ARNT2
  - AHRR
  - HSP90
  - AIP
  - PTGES3
  - SRC
  - STAT1
  - CYP1A1
  - CYP1B1
  - TIPARP
  - UCHL3
  - CUL4B
  - HIF1A
  - HIF2A
  - HK2
  - TET2
  - NT5E
  - CD73
  - KLF6
  - CPS1
  - PAD2
  - IL4I1
  - IDO1
  - TDO2
  - PXR
key_pathways:
  - AHR canonical XRE/DRE signaling
  - AHR non-genomic signaling
  - tryptophan-kynurenine catabolism
  - HIF1A-ARNT crosstalk
  - SRC-EGFR-FAK kinase signaling
  - CUL4B ubiquitin ligase
  - DNA methylation / TET2 demethylation
  - histone acetylation / HDAC
  - PKC / p38 MAPK
  - SUMOylation / SENP

# === User project membership ===
projects: [thesis, hypoxia, skin]
priority: core
read_status: read

# === HypoxiaVERSE-specific ===
hypoxiaverse_status: candidate
exclusion_reason:
data_availability: "review article — no primary data"

# === Cross-references ===
code_url: ""
cited_by: []
---

## Problem

AHR activation drives divergent — sometimes opposite — outcomes across tumour types, immune contexts, and tissues. Despite decades of AHR biology and active development of AHR-pathway drugs (IDO1/TDO2 inhibitors, direct AHR antagonists), clinical results have been disappointing. The authors argue this is because the field has under-appreciated the *combinatorial* sources of context specificity: ligand diversity, receptor and co-factor expression, ARNT paralogs/isoforms, AHRR feedback, crosstalk with transcription factors and signalling pathways, non-genomic AHR actions, posttranslational modifications, epigenetic regulation, and ligand-degrading enzymes. Without integrating these layers, neither preclinical translation nor patient stratification can succeed.

## Key idea

Frame AHR not as a single signalling axis but as a *context-specificity machine*: the same receptor, in different cells and ligand environments, can promote tumour progression, suppress tumour formation, drive Treg expansion, drive Th17 differentiation, mediate immune tolerance, or drive inflammation. The review systematises eleven layers of context specificity (Fig. 1-4 of the paper) that together determine the AHR transcriptional and non-transcriptional output, and motivates therapeutic strategies that target the layer most relevant to a given tumour type rather than the receptor in isolation.

## Method

Narrative literature review covering ~270 primary studies and prior reviews. The authors are a DKFZ/Charité group with primary contributions across many of the cited areas (IL4I1 as metabolic immune checkpoint; AHR-ARNT iso1 in lymphoid malignancies; AHR transcriptional signatures). The review is organised by the eleven modes of context specificity (sections 2-12); each section pairs canonical/textbook evidence with recent mechanistic studies. Figures are conceptual cartoons (created with BioRender.com) summarising canonical signalling (Fig. 1), non-genomic and TF-crosstalk effects (Fig. 2), PTM landscape distilled from PhosphoSitePlus v6.7.1.1 plus low-throughput literature (Fig. 3), and epigenetic regulation of AHR and target genes (Fig. 4).

## Results

The review is structured around eleven layers that the authors argue jointly determine AHR context specificity:

1. **Ligand diversity** (§2). Tryptophan catabolites, eicosanoids, bilirubin, cAMP, dietary, microbial, environmental ligands; vitamin B12 and folic acid as antagonists. Same receptor, different transcriptomes (TCDD vs FICZ vs vemurafenib).
2. **AHR expression** (§3). Tissue-graded — highest in placenta/lung/liver/bladder/bone marrow. Regulated by glucocorticoid signalling (species-divergent) and by Trp deprivation via NRF2 (HEK293) or EGFR-RAS-mTORC1-p38/MAPK (glioblastoma).
3. **ARNT supply and isoforms** (§4). ARNT levels modulated by hypoxia. ARNT2 paralog dimerises with AHR but blunts CYP1A1 induction. ARNT isoform 1 vs 3 ratio (regulated by RBFOX2) determines AHR responsiveness in lymphoid malignancies.
4. **AHR degradation** (§5). Ubiquitin-proteasome dependent; requires ligand + ARNT. UCHL3 deubiquitinates and stabilises AHR (NSCLC stem-like). TIPARP ADP-ribosylates AHR enhancing degradation. Degradation limits magnitude and duration of AHR output.
5. **AHRR feedback** (§6). bHLH/PAS competitor lacking ligand-binding PAS-B. Competes for ARNT and XRE; recruits co-repressors. Tissue-restricted (mainly immune/barrier). Hypomethylation linked to lung cancer risk; hypermethylated and silenced in multiple cancers.
6. **TF and signalling crosstalk** (§7). AHR binds KLF6, RB1 (hypophosphorylated only), E2F1, RELA, RELB, MAF, ESR1. HIF1α and HIF2α compete with AHR for ARNT. Crosstalk with EGFR, STAT, TLR, NF-κB.
7. **Non-genomic AHR** (§8). Cytoplasmic SRC interaction → SRC/EGFR/FAK phosphorylation; AHR-SRC axis = BRAFi-resistance vulnerability in melanoma. STAT1 heterodimer represses STAT signalling. CUL4B-based ubiquitin ligase degrades ESR1/AR/PPARG. AHR-dependent Ca²⁺ elevation by pyrene.
8. **PTMs of AHR** (§9). Phosphorylation at S12/S36 (PKC) impairs nuclear translocation in COS-7/HeLa but PKCθ at S36 enhances it in T cells (cell-type opposite directions). p38/MAPK at S68 enhances HaCaT nuclear accumulation. SUMOylation at K63/K510 stabilises AHR by blocking ubiquitination yet represses its transcriptional activity. ARNT and AHRR also SUMOylated.
9. **Epigenetic regulation of AHR** (§10.1). AHR promoter hypermethylation silences AHR in ~33% of ALL patients and in multiple cancer cell lines. HDAC inhibitors (TSA, butyrate, panobinostat, vorinostat) often induce AHR expression. miR-124, miR-375, miR-548, miR-122 negatively regulate AHR.
10. **Epigenetic regulation of AHR target genes** (§10.2). CYP1A1/CYP1B1 induction sensitive to enhancer methylation in a cell-line-specific way; TCDD induces H3K4me3/H4Ac at CYP1A1 promoter. TCDD enhances promoter hypermethylation of p16, p53, BRCA1 (tumour-suppressor repression). HK2 is an AHR target gene that promotes AHR promoter demethylation, associating with worse cancer survival. AHR induces TET2 → NT5E/CD73 → adenosine in Tregs; downregulated in SLE. AHR-KLF6 binding to non-canonical NC-XREs recruits CPS1 → H1K34 homocitrullination → PAD2 induction.
11. **AHR ligand-degrading enzymes** (§11). CYP1A1/CYP1B1 metabolic clearance of AHR ligands creates a self-limiting negative feedback loop; differential CYP expression contributes to context specificity.

## All claims (exhaustive)

- `[c01]` AHR resides in cytoplasm as a complex with HSP90 dimer, AIP/XAP2/ARA9, PTGES3/p23, and SRC tyrosine kinase; ligand binding exposes NLS and triggers nuclear translocation (p.2-3) "In its inactive state the AHR resides in the cytoplasm and forms a complex with two 90 kDa heat shock proteins (HSP90), the AHR-interacting protein (AIP also known as XAP2 or ARA9), the co-chaperone prostaglandin E synthase 3 (PTGES3 also known as p23) and the protein kinase SRC proto-oncogene, non-receptor tyrosine kinase (SRC)" — confidence: high — type: mechanistic — links: [[concepts/ahr-canonical-signalling-pathway]] [[foundations/hsp90-aip-chaperone-complex]] [[foundations/aryl-hydrocarbon-receptor]] [[claims/ahr-cytosolic-complex-hsp90-aip-p23]]
- `[c02]` AHR-ARNT heterodimer binds xenobiotic response elements (XREs) with consensus 5′-TNGCGTG-3′ to drive canonical AHR target-gene transcription (p.4) "the AHR forms a heterodimer with ARNT (aka HIF1β) and binds to specific XREs with a consensus sequence (5ʹ-TNGCGTG-3ʹ) to regulate multiple target genes" — confidence: high — type: mechanistic — links: [[concepts/ahr-canonical-signalling-pathway]] [[foundations/arnt-hif1b]] [[claims/ahr-arnt-xre-tngcgtg-binding]]
- `[c03]` FICZ and TCDD initially appeared to exert opposing effects on CD4+ T cell differentiation, but optimising FICZ dose/timing to produce TCDD-equivalent CYP1A1 induction yields identical dynamics and responses — i.e. dose and duration of AHR activation, not ligand identity, drive divergence (p.3) "A study following up on this observation optimized the dose and timing of administration of FICZ for TCDD-equivalent cytochrome P450 family 1 subfamily A member 1 (Cyp1a1), AHR target gene, induction and observed the same dynamics and responses for TCDD and FICZ" — confidence: high — type: mechanistic — links: [[concepts/ahr-context-specificity-pleiotropy]] [[foundations/ficz-6-formylindolo-carbazole]] [[foundations/tcdd-2378-tetrachlorodibenzodioxin]] [[claims/ficz-tcdd-converge-on-cyp1a1-dynamics-when-dose-matched]]
- `[c04]` Vemurafenib binds AHR, induces nuclear translocation, but blocks AHR-ARNT binding (proximity ligation), suppresses XRE-luciferase and CYP1A1 transcription — implying a secondary/distinct ligand-binding pocket whose occupancy interferes with the primary TCDD pocket (p.3) "vemurafenib binds the AHR as it displaces radiolabeled TCDD, it leads to nuclear translocation of the AHR, but not to AHR-ARNT binding as evidenced by proximity ligation assay. In line, vemurafenib reduces XRE-luciferase activity and induces neither the mRNA nor the activity of CYP1A1" — confidence: high — type: mechanistic — links: [[concepts/ahr-context-specificity-pleiotropy]] [[foundations/vemurafenib]] [[concepts/ahr-ligand-pharmacology-sahrm]] [[claims/vemurafenib-ahr-secondary-pocket-blocks-arnt]]
- `[c05]` Striking ligand overlap between AHR and the pregnane X receptor (PXR) implies AHR activation co-activates other promiscuous receptors, contributing to ligand-specific heterogeneity of cellular responses (p.3) "Denison and colleagues found a striking overlap between agonists of AHR and the nuclear receptor pregnane X receptor (PXR), suggesting that activation of AHR and crosstalk with other transcription factors may contribute to ligand-specific AHR responses" — confidence: medium — type: mechanistic — links: [[concepts/ahr-context-specificity-pleiotropy]] [[foundations/pxr-pregnane-x-receptor]] [[claims/ahr-pxr-promiscuous-ligand-overlap]]
- `[c06]` Nearly all tumours upregulate at least one Trp-degrading enzyme producing AHR agonists — IDO1/IDO2, TDO2, or IL4I1 — and AHR activation in a given tumour type associates with the dominant expressed enzyme; some tumours show high AHR activity without a Trp-degrading enzyme, implying other ligand sources (p.3) "Nearly all tumors express elevated levels of at least one of the Trp-degrading enzymes and depending on the tumor type AHR activation associates with the expression of one or more of these enzymes. However, several tumors exist that show high AHR activity without association to a Trp-degrading enzyme" — confidence: high — type: correlational — links: [[concepts/microbiota-tryptophan-ahr-ligand-axis]] [[foundations/ido1-indoleamine-dioxygenase]] [[foundations/tdo2-tryptophan-dioxygenase]] [[foundations/il4i1-l-amino-acid-oxidase]] [[claims/ahr-cancer-cells-overexpress-ido1-tdo2-make-kyn]]
- `[c07]` Cryo-EM structures of human AHR-HSP90-AIP with indirubin and unliganded mouse AHR-HSP90-PTGES3 reveal a PAS-B ligand-binding pocket with a polar-residue primary site selective for planar π-rich hydrophobic ligands plus a less geometrically constrained secondary site accommodating larger compounds (p.3-4) "The ligand binding pocket comprises a primary and secondary binding site. Upon binding to indirubin, only the primary site is occupied. In this primary binding site, specific polar amino acid residues determine the selectivity for planar hydrophobic molecules… the secondary binding site appears to be less geometrically constrained, thereby allowing larger compounds to fit" — confidence: high — type: mechanistic — links: [[concepts/ahr-ligand-pharmacology-sahrm]] [[foundations/aryl-hydrocarbon-receptor]] [[claims/ahr-pas-b-cryo-em-primary-secondary-pocket]]
- `[c08]` Trp deprivation induces AHR mRNA and protein and increases AHR activity, via NRF2 signalling in HEK293 cells and via EGFR-RAS-mTORC1 and p38/MAPK signalling in glioblastoma — i.e. AHR is a sensor of intracellular Trp scarcity (p.3) "Recently, deprivation of Trp was discovered to induce AHR mRNA and protein levels resulting in enhanced AHR activity. AHR induction in response to Trp limitation is mediated through potentially cell type-specific mechanisms involving nuclear factor erythroid 2-related factor 2 (NRF2) signaling in HEK 293 cells and epidermal growth factor receptor (EGFR)-rat sarcoma (RAS)-signaling to the mammalian target of rapamycin complex 1 (MTORC1) and p38/mitogen activated protein kinase (MAPK) in glioblastoma cells" — confidence: high — type: mechanistic — links: [[foundations/nrf2-nfe2l2]] [[foundations/mtor-kinase]] [[claims/trp-deprivation-induces-ahr-via-nrf2-egfr-mtor]]
- `[c09]` In murine Hepa-1 cells the ARNT paralog ARNT2 dimerises with AHR equivalently to ARNT under TCDD, outcompetes ARNT when over-expressed, yet AHR-ARNT2 fails to induce CYP1A1 protein and ARNT2 expression reduces TCDD-mediated CYP1A1 induction by ~30% — ARNT2 thus inhibits, rather than supports, canonical AHR transcription (p.4) "ARNT2 expression in cells with reduced ARNT protein results only in minimal induction of CYP1A1 protein. However, the expression of ARNT2 reduces TCDD-mediated induction of endogenous CYP1A1 protein by 30%" — confidence: high — type: mechanistic — links: [[concepts/ahr-arnt-paralogs-and-isoforms]] [[foundations/arnt2-paralog]] [[claims/arnt2-paralog-blunts-canonical-ahr-activation]]
- `[c10]` In lymphoid malignancies the ARNT isoform 1 / isoform 3 ratio (regulated by RBFOX2) determines AHR responsiveness: suppression of ARNT iso1 enhances ligand-driven inflammation while suppression of iso3 mediates immunosuppression (p.4) "Suppression of ARNT isoform 1 enhances AHR responsiveness to ligand activation and mediates inflammation, while suppression of ARNT isoform 3 reduces AHR responsiveness to ligand activation and mediates immunosuppression" — confidence: high — type: mechanistic — links: [[concepts/ahr-arnt-paralogs-and-isoforms]] [[foundations/arnt-hif1b]] [[claims/arnt-isoform-ratio-determines-lymphoid-ahr-response]]
- `[c11]` The deubiquitylase UCHL3 interacts with, deubiquitylates, and stabilises AHR, thereby promoting stem-like properties of non-small-cell lung cancer cells (p.4) "ubiquitin carboxyl terminal hydrolase L3 (UCHL3) was demonstrated to interact with, deubiquitylate, and stabilize AHR, thereby promoting the stem-like characteristics of non-small cell lung cancer cells" — confidence: high — type: mechanistic — links: [[foundations/uchl3-deubiquitinase]] [[foundations/aryl-hydrocarbon-receptor]] [[claims/uchl3-deubiquitinates-stabilises-ahr-nsclc-stemness]]
- `[c12]` AHR degradation is enhanced by the AHR target gene TIPARP via ADP-ribosylation of AHR, completing a negative feedback loop that ensures temporal limitation of AHR-driven transcription (p.4) "AHR degradation is also regulated by the AHR target gene TCDD-inducible poly (ADP-ribose) polymerase (TIPARP), which ADP-ribosylates AHR, hence increasing its susceptibility to degradation" — confidence: high — type: mechanistic — links: [[foundations/tiparp]] [[concepts/ahr-cyp1a1-negative-feedback-clearance]] [[claims/ahrr-tiparp-hif1a-ahr-feedback]]
- `[c13]` In naïve mice, AHRR expression is tissue- and cell-type-restricted — predominantly immune cells of the cutaneous and intestinal barriers (CD11c⁺ myeloid, T cells, ILC3, IELs) — and largely absent from liver and intestinal epithelium; Ahrr knockout protects against LPS septic shock yet aggravates colitis, mirroring some but not all phenotypes of Ahr-deficient mice (p.4-5) "AHRR expression in naïve mice is very cell type-specific … is mainly restricted to immune cells and is most prominent in the cutaneous and intestinal barrier" — confidence: high — type: correlational — links: [[foundations/ahrr-repressor]] [[concepts/ahr-barrier-tissue-il22-antimicrobial]] [[claims/ahrr-tissue-restricted-to-barrier-immune-cells]]
- `[c14]` AHRR DNA hypomethylation is associated with active and past smoking, increased lung cancer risk, decreased lung function, and smoking-related mortality; conversely AHRR is hypermethylated and silenced in breast, cervix, colon, lung, ovary and stomach malignancies (p.5, p.9) "AHRR hypomethylation has been associated with low lung function, increased lung cancer risk and mortality, and with smoking related morbidity and mortality" — confidence: high — type: correlational — links: [[foundations/ahrr-repressor]] [[concepts/ahr-epigenetic-regulation-of-target-genes]] [[claims/ahrr-hypomethylation-smoking-lung-cancer-risk]]
- `[c15]` HIF1α and HIF2α bind ARNT and compete with ligand-bound AHR for ARNT, reducing AHR-XRE transcriptional activity under hypoxia (p.5) "HIF1α and HIF2α also bind to ARNT and compete with ligand-bound AHR for the interaction with ARNT, hence reducing AHR activity" — confidence: high — type: mechanistic — links: [[concepts/ahr-hif-arnt-competition]] [[foundations/hif1a]] [[foundations/hif2a]] [[foundations/arnt-hif1b]] [[claims/hif1a-hif2a-compete-with-ahr-for-arnt]]
- `[c16]` Cytoplasmic AHR-SRC interaction triggers SRC phosphorylation and downstream EGFR/FAK activation; the AHR-SRC axis was identified as a therapeutic vulnerability that mediates BRAF inhibitor resistance in melanoma, and dual AHR+SRC inhibition synergistically suppresses androgen receptor signalling and prostate cancer growth (p.5-6) "the AHR/SRC axis has recently been discovered as a new therapeutic vulnerability that triggers resistance to BRAF (B-Raf proto-oncogene, serine/threonine kinase) inhibitors in melanoma" — confidence: high — type: pharmacological — links: [[concepts/ahr-non-genomic-cytoplasmic-effects]] [[foundations/src-kinase]] [[foundations/vemurafenib]] [[foundations/braf-kinase]] [[claims/ahr-src-axis-drives-brafi-resistance-melanoma]]
- `[c17]` AHR assembles a CUL4B-based E3 ubiquitin ligase that drives ligand-dependent proteasomal degradation of ESR1, androgen receptor, and PPARG — a transcription-independent function of liganded AHR (p.6) "AHR mediates non-transcriptional actions through the assembly of a CUL4B-based ubiquitin ligase complex. Through this mechanism AHR promotes the ligand-dependent proteasomal degradation of specific substrates including ESR1, AR as well as peroxisome proliferator-activated receptor gamma (PPARG)" — confidence: high — type: mechanistic — links: [[concepts/ahr-non-genomic-cytoplasmic-effects]] [[foundations/cul4b-e3-ligase]] [[foundations/pparg-tf]] [[claims/ahr-acts-as-cul4b-e3-ligase]]
- `[c18]` AHR PKC phosphorylation at S12/S36 (COS-7/HeLa) inhibits ligand-dependent nuclear translocation, but PKCθ phosphorylation at S36 enhances nuclear import in T cells — i.e. the same residue gives opposite phenotypes depending on cell-type-specific kinase repertoire (p.6) "AHR phosphorylation at PKC sites S12 or S36 adjacent to the bipartite basic amino acid segment of the NLS inhibits ligand-dependent nuclear translocation in monkey kidney fibroblast-like COS7 and cervical carcinoma HeLa cells. In contrast, AHR phosphorylation at S36 by PKCθ enhances AHR nuclear import in T cells" — confidence: high — type: mechanistic — links: [[concepts/ahr-posttranslational-modifications-landscape]] [[claims/ahr-pkc-phosphorylation-context-dependent-translocation]]
- `[c19]` SUMOylation of AHR at K63/K510 increases AHR protein stability by blocking ubiquitination yet represses its transcriptional activity; AHR ligand stimulation inhibits AHR SUMOylation. AHRR SUMOylation at K542/K583/K660 enhances transcriptional repression and binding to ANKRA2/HDAC4/HDAC5 (p.7-8) "SUMOylation at K63 and K510 stabilized the protein by inhibiting its ubiquitination in MCF-7 cells. SUMOylation repressed the transcriptional activity of AHR, and ligand treatment inhibited SUMOylation of AHR" — confidence: high — type: mechanistic — links: [[concepts/ahr-posttranslational-modifications-landscape]] [[foundations/ahrr-repressor]] [[claims/sumoylation-ahr-stabilises-but-represses-transcription]]
- `[c20]` AHR promoter hypermethylation impairs SP1 binding and silences AHR expression in 33% of acute lymphoblastic leukemia patients and in multiple cancer cell lines (osteosarcoma U2OS/143B, diffuse large B-cell lymphoma U-2932 R2/OCI-LY19, CML K562, ALL Jurkat/REH) (p.8-9) "In acute lymphoblastic leukemia (ALL), hypermethylation of the AHR promoter was found in 33% of patients and impaired binding of SP1 resulting in AHR transcriptional silencing" — confidence: high — type: quantitative — links: [[concepts/ahr-epigenetic-regulation-of-target-genes]] [[foundations/aryl-hydrocarbon-receptor]] [[claims/ahr-promoter-hypermethylation-silences-ahr-all]]
- `[c21]` HK2 is itself an AHR target gene that drives AHR promoter demethylation, creating a positive-feedback loop; HK2 expression is negatively correlated with AHR promoter methylation in multiple cancers and the corresponding methylation pattern associates with worse overall patient survival (p.9) "hexokinase 2 (HK2), an important enzyme for cancer growth, has been reported as an AHR target gene that modulates AHR activity by promoting AHR promoter demethylation. Several cancers show negative correlation of AHR promoter methylation with HK2 expression, which was associated with worse overall patient survival" — confidence: high — type: correlational — links: [[concepts/ahr-epigenetic-regulation-of-target-genes]] [[foundations/hk2-hexokinase-2]] [[claims/hk2-ahr-target-promotes-ahr-promoter-demethylation]]
- `[c22]` TCDD-driven AHR activation increases promoter methylation of tumour suppressors p16(INK4a) and p53 (reducing transcription), and AHR-dependent hypermethylation silences BRCA1 in MCF-7 — implying AHR can act as a tumour promoter via epigenetic repression of tumour suppressors (p.9-10) "TCDD enhanced promoter methylation of the tumor suppressors p16 (INK4a) and p53, thereby reducing their transcription. Moreover, Papoutsis et al. observed AHR-dependent hypermethylation of the CpG island in the proximal promoter of BRCA1 in MCF7 breast cancer cells" — confidence: high — type: mechanistic — links: [[concepts/ahr-epigenetic-regulation-of-target-genes]] [[foundations/brca1-tumor-suppressor]] [[foundations/tp53-tumor-suppressor]] [[foundations/cdkn2a-tumor-suppressor]] [[claims/ahr-tcdd-hypermethylates-tumor-suppressor-promoters]]
- `[c23]` AHR binds the TET2 promoter upon Kyn activation, inducing TET2 which then demethylates the NT5E promoter and increases CD73 expression and adenosine production in Tregs/B cells; in SLE, downregulation of this AHR-TET2-NT5E axis associates with reduced anti-inflammatory adenosine (p.10-11) "TET2 induction by AHR ligand activation promotes demethylation at the promoter of the 5′-nucleotidase NT5E, which encodes the membrane-bound CD73 protein that converts AMP to the anti-inflammatory adenosine. In SLE, downregulation of AHR was associated with increased methylation levels at the NT5E gene promoter" — confidence: high — type: mechanistic — links: [[concepts/ahr-epigenetic-regulation-of-target-genes]] [[foundations/tet-mediated-dna-demethylation]] [[foundations/cd39-ectonucleotidase]] [[claims/ahr-tet2-nt5e-cd73-adenosine-treg-sle]]
- `[c24]` AHR ligand activation recruits an AHR-KLF6 complex to enhancer regions with non-canonical XREs (NC-XREs); KLF6 recruits CPS1, which drives homocitrullination (carbamylation) of histone H1K34 and induction of peptidyl-arginine-deiminase 2 (PAD2), suggesting AHR contributes to citrullination programs relevant to rheumatoid arthritis (p.11) "AHR-KLF6 binding to enhancer regions with non-canonical XREs (NC-XREs), e.g. binding site for AHR heterodimer without ARNT, leads to homocitrullination of H1K34 and induction of peptidyl arginine deiminase 2 (PAD2)" — confidence: medium — type: mechanistic — links: [[concepts/ahr-non-genomic-cytoplasmic-effects]] [[foundations/klf6-tf]] [[claims/ahr-klf6-cps1-h1k34-homocitrullination-pad2]]

## Discussion captured

### Authors' interpretation

The authors interpret the published evidence as showing that AHR's divergent — even opposite — effects (tumour promotion vs tumour suppression; Treg vs Th17) are not paradoxes but predictable consequences of *layered* context specificity. They argue that successful AHR therapeutics will require matching the modality of intervention (direct AHR antagonism, upstream Trp-enzyme inhibition, ligand-degrading-enzyme manipulation, ARNT/ARNT2-targeting) to the specific layer driving the dominant phenotype in the disease/cell type of interest.

### Comparisons with prior literature (made by authors)

- Bersten et al. 2013 Nat Rev Cancer (ref 1) — used to anchor bHLH-PAS family context for AHR.
- Rothhammer & Quintana 2019 Nat Rev Immunol (ref 2) — cited as the environmental-sensor framing of AHR in immunity; their own review extends beyond immunity to layered context specificity.
- Platten et al. 2019 Nat Rev Drug Discov (ref 44) — cited for Trp catabolism as a therapeutic target.
- Sadik et al. 2020 Cell (ref 45, Opitz group's own paper) — cited as the discovery that IL4I1 is a metabolic immune checkpoint activating AHR; central to their argument that *which* Trp-enzyme is expressed dictates the dominant agonist.
- Stockinger et al. 2021 Nat Rev Gastroenterol Hepatol (ref 87) — cited for intestinal AHR and ligand clearance.
- Paris et al. 2022 EMBO Mol Med (ref 123) — cited for AHR-SRC as BRAFi vulnerability in melanoma, supporting their thesis that non-genomic AHR is therapeutically actionable.

### Mechanistic hypotheses proposed

- AHR primary vs secondary PAS-B pocket occupancy could explain how vemurafenib and TCDD induce mutually exclusive transcriptomes; this predicts that "pocket-selective" AHR ligands could mimic ligand-specific outcomes pharmacologically (p.3-4).
- ARNT2 may inhibit, rather than support, canonical AHR signalling in tissues where it is expressed (kidney, CNS, retinal epithelium), explaining tissue-dependent AHR responsiveness (p.4).
- AHR PTM context (kinase repertoire, SUMO E3/SENP balance) could be the *missing variable* that explains why the same residue (e.g. S36) produces opposite phenotypes in different cell types (p.6-7).
- AHR could indirectly shape histone H1 carbamylation via KLF6-CPS1 — a hypothesis with potential mechanistic implications for AHR-driven autoimmune phenotypes such as rheumatoid arthritis (p.11).

### Caveats and self-criticism

- Differences between human and mouse AHR (species-specific ligand selectivity and transcriptional responses) limit in-vivo investigation and may explain failures of translation (p.2).
- AHR PTMs are "not fully understood"; for many sites no kinase has been mapped; the involvement of kinases beyond PKC/tyrosine kinases is "nebulous" (p.8).
- The role of AHR-KLF6-CPS1-mediated carbamylation in cancer has "so far not been further investigated" (p.11).
- Reports of PKC effects on AHR are conflicting across HepG2/HeLa, suggesting cell-type-restricted readouts that the field has not yet rationalised (p.6).

### Future directions suggested

- Map AHR PTMs systematically across tissues and disease states to predict tissue-specific AHR output.
- Explore the carbamylation/citrullination arm of AHR signalling beyond rheumatoid arthritis (i.e. in cancer).
- Characterise ARNT2 contribution to AHR signalling in physiological tissues where it is highly expressed.
- Use pocket-selective AHR ligands to dissociate canonical from non-canonical AHR responses.
- Develop AHR-pathway therapeutics matched to the dominant layer of context specificity in a given indication (Trp-enzyme inhibitor for IDO1-driven tumours, direct AHR antagonist for SRC-axis-driven BRAFi-resistant melanoma, ARNT-isoform-targeting for lymphoid malignancies).

## Limitations

- The review is interpretive, not systematic: there is no PRISMA flow, no inclusion/exclusion protocol, no quantitative synthesis. Coverage privileges areas where the Opitz group has primary expertise (IL4I1, Trp-derived AHR ligands, ARNT iso1, AHR signatures).
- Several mechanistic claims rest on single-cell-line studies (MCF-7 dominates SUMOylation evidence; LNCaP dominates prostate methylation evidence; Caco-2 dominates HDAC inhibitor evidence). Generalisability is not formally assessed.
- The eleven-layer organisation is a useful pedagogical scaffold but the *quantitative* contribution of each layer to a given AHR phenotype is not assigned; the review does not propose any integrative model or score.
- The authors disclose patents (IL4I1 biomarker, AHR transcriptional signature, Trp/Kyn multiplex assay) that overlap with material reviewed — a potential bias for emphasis on IL4I1 over other Trp-enzymes.
- Single-cell-resolved AHR signalling is largely absent from the synthesis — bulk methylation/expression studies dominate the epigenetic section, and single-cell deconvolution of AHR-driven cell-type-specific responses is not discussed.

## Open questions

### Open questions raised by authors

- Which kinases (beyond PKC and tyrosine kinases) directly phosphorylate AHR, and at which residues? Most of the high-throughput PTM sites have no assigned upstream enzyme (Fig. 3).
- Does ARNT2 antagonise AHR in tissues where it is dominantly expressed (CNS, kidney, retinal epithelium)?
- Why do AHRR and CYP1A1 promoter methylation respond in *opposite* directions to maternal smoking exposure if both are downstream of the same AHR axis?
- What is the carbamylation/PAD2 program activated by AHR-KLF6-CPS1 doing in cancer (rather than autoimmunity)?
- Is the secondary AHR ligand-binding pocket pharmacologically targetable for ligand-specific outcomes?

### Open questions identified during ingest

- Can a single quantitative score integrate the eleven layers of context specificity to predict AHR phenotype in a new cell type or tumour? The review does not propose one; this is a tractable bioinformatics problem.
- Are there *single-cell* signatures of layered AHR context specificity (ligand profile × ARNT/ARNT2/iso ratio × AHRR expression × HIF crosstalk) that could be derived from existing scRNA-seq atlases? Relevant for [[concepts/ahr-tam-immunosuppression-tumour]].
- How does cellular hypoxia (HIF1α/HIF2α-ARNT competition) interact with ligand-degrading enzyme expression to determine net AHR activity in the tumour microenvironment? The crosstalk is mentioned but not synthesised.
- Could pocket-selective AHR ligands (suggested by the vemurafenib example) form a class of "biased AHR agonists" analogous to biased GPCR agonists?

## My take

A useful synthesis that goes substantially beyond [[papers/aryl-hydrocarbon-receptor-rehabilitated-target-therapeutic]] in mechanistic depth: where the 2025 Quintana review focuses on therapeutic immune modulation and tapinarof, this 2023 Opitz review systematises the *upstream* layers (PTMs, epigenetics, ARNT paralogs/isoforms, ligand-degrading enzymes, non-genomic effects) that explain why a single receptor produces opposite phenotypes. For my thesis the most actionable framing is the **eleven-layer context-specificity model** — concretely useful for thinking about hypoxia-AHR crosstalk (HIF-ARNT competition is layer 6) and for skin/keratinocyte AHR work (which is hidden in the cell-type-specific PTM and AHRR-barrier sections). The single-cell gap (no integration with scRNA-seq atlases) is an opportunity rather than a weakness. The vemurafenib pocket-occupancy and ARNT2-antagonist mechanisms are particularly novel and under-exploited in current drug discovery.

## Related

- [[papers/aryl-hydrocarbon-receptor-rehabilitated-target-therapeutic]] — Polonio/Quintana 2025 NRDD AHR therapeutic review; complementary therapeutic-immune-modulation framing
- [[papers/role-ahr-host-pathogen-interactions]] — Barreira-Silva/Moura-Alves 2025 NRI review on AHR in host–pathogen interactions (infection focus)
- [[concepts/ahr-canonical-signalling-pathway]] — canonical AHR-ARNT-XRE pathway
- [[concepts/ahr-non-canonical-signalling]] — non-canonical AHR signalling
- [[concepts/ahr-context-specificity-pleiotropy]] — eleven-layer context-specificity framework (this paper)
- [[concepts/ahr-posttranslational-modifications-landscape]] — PTM landscape of AHR/ARNT/AHRR (this paper)
- [[concepts/ahr-epigenetic-regulation-of-target-genes]] — DNA-methylation, histone, miRNA control of AHR and targets (this paper)
- [[concepts/ahr-arnt-paralogs-and-isoforms]] — ARNT2 paralog + ARNT iso1/iso3 (this paper)
- [[concepts/ahr-non-genomic-cytoplasmic-effects]] — SRC, STAT1, CUL4B, Ca²⁺ (this paper)
- [[concepts/ahr-hif-arnt-competition]] — hypoxia-AHR crosstalk via ARNT
- [[concepts/ahr-cyp1a1-negative-feedback-clearance]] — ligand-degrading-enzyme loop
- [[concepts/ahr-ligand-pharmacology-sahrm]] — SAHRMs and pocket-selective ligands
- [[concepts/tryptophan-ido1-kynurenine-immunosuppression]] — Trp catabolism axis
- [[concepts/ahr-tam-immunosuppression-tumour]] — AHR in tumour-associated macrophages
- [[concepts/ahr-treg-th17-balance]] — Treg/Th17/Tr1 polarisation
- [[concepts/microbiota-tryptophan-ahr-ligand-axis]] — microbial Trp-derived AHR ligands
- [[foundations/aryl-hydrocarbon-receptor]] — AHR receptor entity
- [[foundations/arnt-hif1b]] — ARNT/HIF1β
- [[foundations/arnt2-paralog]] — ARNT2
- [[foundations/ahrr-repressor]] — AHRR
- [[foundations/tiparp]] — TIPARP
- [[foundations/cyp1a1-cytochrome]] — CYP1A1
- [[foundations/hsp90-aip-chaperone-complex]] — cytosolic chaperone complex
- [[foundations/tcdd-2378-tetrachlorodibenzodioxin]] — TCDD
- [[foundations/ficz-6-formylindolo-carbazole]] — FICZ
- [[foundations/ido1-indoleamine-dioxygenase]] — IDO1
- [[foundations/tdo2-tryptophan-dioxygenase]] — TDO2
- [[foundations/il4i1-l-amino-acid-oxidase]] — IL4I1
- [[foundations/kynurenine]] — kynurenine
- [[foundations/uchl3-deubiquitinase]] — UCHL3
- [[foundations/cul4b-e3-ligase]] — CUL4B
- [[foundations/src-kinase]] — SRC
- [[foundations/vemurafenib]] — vemurafenib
- [[foundations/braf-kinase]] — BRAF
- [[foundations/hk2-hexokinase-2]] — hexokinase 2
- [[foundations/pxr-pregnane-x-receptor]] — PXR
- [[foundations/hif1a]] — HIF1α
- [[foundations/hif2a]] — HIF2α
- [[people/christiane-opitz]] — corresponding author
- [[people/saskia-trump]]
- [[people/mirja-prentzell]]
- [[people/pauline-holfelder]]
