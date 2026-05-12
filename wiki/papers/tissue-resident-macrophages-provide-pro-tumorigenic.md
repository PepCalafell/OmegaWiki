---
# === Identification ===
title: "Tissue-resident macrophages provide a pro-tumorigenic niche to early NSCLC cells"
slug: tissue-resident-macrophages-provide-pro-tumorigenic
arxiv: ""
doi: "10.1038/s41586-021-03651-8"
pmid: "34135508"
venue: "Nature"
year: 2021
authors:
  - "María Casanova-Acebes"
  - "Erica Dalla"
  - "Andrew M. Leader"
  - "Jessica LeBerichel"
  - "Jovan Nikolic"
  - "Blanca M. Morales"
  - "Markus Brown"
  - "Christie Chang"
  - "Leanna Troncoso"
  - "Steven T. Chen"
  - "Ana Sastre-Perona"
  - "Matthew D. Park"
  - "Alexandra Tabachnikova"
  - "Maxime Dhainaut"
  - "Pauline Hamon"
  - "Barbara Maier"
  - "Catherine M. Sawai"
  - "Esperanza Agulló-Pascual"
  - "Markus Schober"
  - "Brian D. Brown"
  - "Boris Reizis"
  - "Thomas Marron"
  - "Ephraim Kenigsberg"
  - "Christine Moussion"
  - "Philippe Benaroch"
  - "Julio A. Aguirre-Ghiso"
  - "Miriam Merad"
first_author: "María Casanova-Acebes"
corresponding_author: "María Casanova-Acebes; Miriam Merad"

# === Source & metadata ===
source_type: pdf
s2_id: "a3dfb0d6aa1770797a5e72044b2a3b265d15f915"
date_added: 2026-05-06
ingested_date: 2026-05-06
ingest_version: 1
last_reviewed: null

# === Classification ===
importance: 5
tier: TIER_1
tags:
  - tissue-resident-macrophage
  - alveolar-macrophage
  - monocyte-derived-macrophage
  - tumor-microenvironment
  - lung-cancer
  - NSCLC
  - macrophage-ontogeny
  - lineage-tracing
  - EMT
  - regulatory-T-cell
  - immunosuppression
  - scRNA-seq
  - ATAC-seq
  - mouse-model
  - immunology
keywords:
  - tissue-resident macrophage
  - TRM
  - alveolar macrophage
  - monocyte-derived macrophage
  - NSCLC
  - lung adenocarcinoma
  - EMT
  - TWIST1
  - ZEB1
  - regulatory T cell
  - CTLA-4
  - CD73
  - CD169-DTR
  - Map17-creER
  - Cx3cr1-creER
  - Ms4a3
  - PPARG
  - MARCO
  - SIGLEC1
  - TREM2
  - SPP1
  - APOE
  - GPNMB
  - KP model
  - B16-OVA
domain: "immunology / oncology / cell biology"

# === Biomedical domain ===
tissue:
  - lung
condition:
  - cancer
disease_specific:
  - NSCLC
  - lung_adenocarcinoma
species:
  - human
  - mouse
hypoxia_relevant: false
contains_immune_cells: true
contains_myeloid: true

# === Technique ===
techniques:
  - scRNA-seq_10x
  - bulk_RNA-seq
  - ATAC-seq
  - flow_cytometry
  - confocal_imaging
  - lineage_tracing
  - 3D_spheroid_coculture
  - transwell_migration
  - diphtheria_toxin_depletion
n_samples: 35
n_cells_total:
integration_method: ""

# === Biology captured ===
key_cell_types:
  - alveolar-macrophage-TRM
  - monocyte-derived-macrophage
  - CD14-monocyte
  - CD16-monocyte
  - regulatory-T-cell
  - CD8-T-cell
  - CD4-T-cell
  - KP-tumor-cell
key_markers:
  - PPARG
  - MARCO
  - SIGLEC1
  - STMN1
  - MKI67
  - MRC1
  - CD68
  - APOE
  - TREM2
  - SPP1
  - GPNMB
  - C1QA
  - CD14
  - VCAN
  - S100A12
  - FCGR3A
  - CX3CR1
  - CCR2
  - LY6C2
  - MMP12
  - MMP14
  - CCL17
  - CXCL9
  - TGFB1
  - CDH1
  - TWIST1
  - ZEB1
  - VEGFA
  - PLAU
  - FOXP3
  - CD73
  - CTLA-4
key_pathways:
  - macrophage-ontogeny
  - epithelial-mesenchymal-transition
  - regulatory-T-cell-differentiation
  - antigen-presentation-MHC-II
  - tissue-remodelling

# === User project membership ===
projects:
  - thesis
priority: context
read_status: read

# === HypoxiaVERSE-specific ===
hypoxiaverse_status:
exclusion_reason:
data_availability: "Mouse scRNA-seq and ATAC-seq deposited at GEO (accession in original paper); human scRNA-seq is the reanalysed Leader/Lavin Mount Sinai NSCLC cohort (35 patients)."

# === Cross-references ===
code_url: ""
cited_by: []
---

## Problem

The macrophage compartment of the tumour microenvironment (TME) is functionally diverse, but the contribution of distinct ontogenic lineages — embryonically-seeded tissue-resident macrophages (TRMs) versus adult bone-marrow-derived monocyte-derived macrophages (MDMs) — to tumour progression in NSCLC was unresolved. It was unclear whether TRMs and MDMs played overlapping or distinct roles, when each population mattered during tumour growth, and whether either lineage could be selectively targeted for therapy.

## Key idea

In early NSCLC, alveolar TRMs (group I; PPARG⁺/MARCO⁺/SIGLEC1⁺) physically accumulate close to seeded tumour cells and provide a **pro-tumorigenic niche**: they induce an EMT/invasiveness programme in tumour cells (TWIST1/ZEB1/E-cadherin reduction) and uniquely enhance regulatory T cell (Treg) suppressive programmes (CD73, CTLA-4). As tumours progress, TRMs are displaced to the periphery and replaced by monocyte-derived TREM2⁺/SPP1⁺/APOE⁺ macrophages (group II; MDMs). Specific depletion of TRMs (CD169-DTR) before tumour engraftment reduces tumour burden in both KP NSCLC and B16-OVA melanoma; depletion in established lesions has no effect — the niche function is restricted to the earliest stages of cancer progression.

## Method

- **Human scRNA-seq**: reanalysis of CD45⁺ leukocytes from 35 early-stage treatment-naive NSCLC patients (Leader et al. preprint 2020 / Lavin et al. Cell 2017 cohort), Mount Sinai. Maximum-likelihood clustering (Martin et al. 2019).
- **Mouse orthotopic NSCLC**: tail-vein injection of KP (KrasG12D, p53⁻/⁻) lung epithelial cells, GFP-labelled, into C57BL/6 mice. Genetic NSCLC model: SPC-Cre adenovirus in transgenic KP mice.
- **Lineage tracing**: tamoxifen-inducible Map17(Pdzk1ip1)-creER × R26-LSL-tdTom (labels adult HSC progeny); Cx3cr1-creER × R26-YFP (labels monocyte progeny); Ms4a3-tdTom reporter (Liu 2019, monocyte-restricted).
- **TRM-specific depletion**: CD169-DTR mice (Siglec1 promoter drives diphtheria toxin receptor); intranasal diphtheria toxin (15 ng/mouse) ablates lung TRMs without affecting circulating monocytes/MDMs.
- **Bulk RNA-seq + ATAC-seq**: FACS-sorted TRMs (50,000 cells for ATAC; 20,000 for RNA-seq) from naive lungs, day-15 tumours, day-30 tumours. STAR + DESeq2 + limma; Bowtie2 + MACS2 + GREAT.
- **3D spheroid co-culture**: KP-GFP cells with TRMs or bone marrow monocytes (BMMs) in Matrigel; live time-lapse imaging (IncuCyte); E-cadherin / TWIST1 / β-catenin immunofluorescence; transwell migration with conditioned medium.
- **Treg differentiation assay**: ex vivo co-culture of naive T cells with purified tumour TRMs vs MDMs; FACS for FOXP3, CD25, CTLA-4, CD73.
- **B16-OVA validation**: intravenous B16-BFP-F10/OVA into CD169-DTR + DT vs WT + DT mice.

## Results

- Human and mouse NSCLC contain four conserved myeloid groups: I (TRM-like, PPARG⁺/MARCO⁺/SIGLEC1⁺/STMN1⁺), II (MDM, TREM2⁺/APOE⁺/SPP1⁺/GPNMB⁺/C1Q⁺), III (CD14⁺ classical monocytes), IV (CD16⁺/CX3CR1⁺ non-classical monocytes). Cross-species PPARG/MARCO and TREM2/SPP1/APOE signatures are conserved.
- Map17-creER and Cx3cr1-creER fate mapping: group I cluster is depleted of label-positive cells (independent of adult HSCs), group II cluster is heavily labelled (monocyte-derived).
- TRMs decrease in advanced (day 30) tumours; MDMs dominate. TRMs localise close to KP tumour cells until day 15, then redistribute to tumour periphery, resembling tuberculosis-granuloma topology.
- 1,670 DEGs in TRMs from tumour-bearing vs healthy lungs (P<0.05); 1,322 induced in early lesions. Tumour TRMs upregulate MMP12, MMP14, ADAMDEC1, TSPAN4, MHC-II (H2-AA/AB1/Q7), CCL17, CXCL9; downregulate IL1B, NLRP1B, AMER2, RIPOR2, DGKG, FMNL3, RASGRP4.
- ATAC-seq: minimal global chromatin remodelling in tumour-associated TRMs vs healthy; most accessibility changes occur early at MMP12/MMP13 loci; MHC-II loci remain open throughout.
- 3D spheroid co-culture: TRMs (not BMMs) drive an EMT/invasiveness programme — reduced E-cadherin protein, TWIST1 induction, increased dispersion; ITGB1/RHOA/LAMC2/PLAU/VEGFA upregulation in KP cells. TRM-conditioned medium also suffices for transwell migration.
- Ex vivo: TRMs and MDMs both induce Treg differentiation, but only TRMs uniquely upregulate CD73 and CTLA-4 on differentiated Tregs.
- Tregs localise close to TRMs in tumour lesions; Treg accumulation correlates with tumour growth.
- CD169-DTR + intranasal DT specifically depletes lung TRMs (CD169 expression negligible on monocytes/MDMs in lungs; confirmed by Ms4a3-tdTom). Depletion does not affect tumour cell seeding at 24h.
- TRM depletion before KP injection reduces tumour size and lung tumour area (not number of foci); increases CC3⁺ apoptotic cells and p27⁺ slow-cycling cells; reduces Treg cells; reduces CTLA-4/CD73 on Tregs; increases CD3⁺ T cells and IFNγ⁺TNF⁺CD8⁺ cells; raises CD8/Treg ratio. Effect is restricted to tumour; spleen and tumour-draining lymph node Tregs unchanged.
- TRMs in KP-deficient mice show reduced TWIST1⁺ and ZEB1⁺ KP cells in vivo — confirms in-vivo EMT-driver role.
- TRM depletion in already-established tumours (day 12-15 onwards) has no effect on tumour burden, Tregs, or CD8/Treg ratio.
- B16-OVA melanoma: TRM depletion reduces tumour burden (day 14); expands IFNγ⁺TNF⁺ effector CD4⁺ and CD8⁺ T cells; reduces PD-1 MFI on T cells; reduces Tregs; raises CD8/Treg ratio; tumour reduction not associated with increased OVA-specific OT-I/OT-II expansion.

## All claims (exhaustive)

- [trm-mdm-distinct-ontogeny-nsclc] TRMs (group I, MARCO⁺/PPARG⁺/SIGLEC1⁺) and MDMs (group II, TREM2⁺/APOE⁺/SPP1⁺) are ontogenically distinct in NSCLC, derived from embryonic-resident vs adult HSC lineages respectively (p.578-580) "the tumour-associated group I cluster in mice and its homologous cluster in humans arise from the TRM lineage, independent of adult HSCs, whereas all other clusters are derived from adult haematopoiesis, probably through a monocyte intermediate" — confidence: high — type: mechanistic — links: [[concepts/macrophage-ontogeny-resident-vs-monocyte-derived]] [[concepts/trem2-tumor-associated-macrophage]] [[claims/trm-mdm-distinct-ontogeny-nsclc]]
- [trm-frequency-decreases-mdm-increases-advanced-nsclc] TRMs decrease and MDMs dominate advanced NSCLC tumours compared to non-involved lung in both mouse and human (p.580-581) "there was a marked reduction in the number of TRMs in both mouse and human tumours compared to normal lung tissues, whereas MDMs dominated advanced tumour lesions" — confidence: high — type: correlational — links: [[concepts/tissue-resident-macrophage-tumor-niche]] [[claims/trm-frequency-decreases-mdm-increases-advanced-nsclc]]
- [trm-localize-close-tumor-cells-early-stage] TRMs localise close to KP tumour cells until day 15 and then redistribute to the tumour periphery as the tumour expands (p.581) "tumour cells localized close to TRMs up to day 15 after tumour seeding, before redistributing to the periphery of tumour lesions, resembling human granuloma lesions" — confidence: high — type: correlational — links: [[concepts/tissue-resident-macrophage-tumor-niche]] [[claims/trm-localize-close-tumor-cells-early-stage]]
- [trm-tumor-1670-degs-vs-healthy-lung] 1,670 DEGs distinguish TRMs in tumour-bearing lungs from healthy-lung TRMs (P<0.05); 1,322 are induced in early lesions (p.581) "We identified 1,670 differentially expressed genes (DEGs) between TRMs isolated from tumour-bearing lungs compared to TRMs from healthy control lungs (day 30, P < 0.05; Supplementary Table 3). Among them, 1,322 DEGs were induced in early lesions" — confidence: high — type: quantitative — links: [[claims/trm-tumor-1670-degs-vs-healthy-lung]]
- [trm-tumor-upregulate-mmp-mhcii-ccl17-cxcl9] Tumour-associated TRMs upregulate MMP12/MMP14/ADAMDEC1, TSPAN4, MHC-II (H2-AA/AB1/Q7), CCL17, CXCL9; downregulate IL1B and NLRP1B (p.581) "Early tumour TRMs expressed genes encoding peptidases (Mmp12, Mmp14 and Adamdec1), integrin-binding molecules (Tspan4), major histocompatibility complex (MHC) class II molecules (H2-M2, H2-AA, H2-AB1 and H2-Q7) and T cell chemoattractants (Ccl17 and Cxcl9), and showed a significant downregulation in the expression of Il1b transcripts and genes encoding inflammasome mediators (Nlrp1b)" — confidence: high — type: mechanistic — links: [[concepts/tissue-resident-macrophage-tumor-niche]] [[claims/trm-tumor-upregulate-mmp-mhcii-ccl17-cxcl9]]
- [trm-minimal-chromatin-changes-tumor-seeding] Tumour-associated TRMs show minimal global ATAC-seq chromatin accessibility changes vs healthy-lung TRMs, with localised early changes at MMP12/MMP13 (p.581) "We found minimal changes in chromatin accessibility in tumour-associated TRMs compared to healthy control lungs (Extended Data Fig. 4c), consistent with the fact that TRMs are heavily imprinted by the tissue microenvironment in which they reside" — confidence: high — type: mechanistic — links: [[foundations/atac-seq]] [[claims/trm-minimal-chromatin-changes-tumor-seeding]]
- [tumor-trm-upregulate-mhcii-antigen-presentation] Tumour-associated TRMs upregulate MHC-II expression (H2-AA/H2-AB1/H2-Q7) — antigen-presentation enhanced in early lesions (p.581-582) "tumour-associated TRMs upregulated their expression of MHC class II genes in early NSCLC lesions, suggesting that these TRMs might contribute to the presentation of antigens to CD4+ T cells" — confidence: high — type: mechanistic — links: [[claims/tumor-trm-upregulate-mhcii-antigen-presentation]]
- [trm-induce-emt-program-tumor-cells-spheroids] TRMs (but not bone-marrow monocytes) drive an EMT programme in KP cells in 3D spheroids: reduced E-cadherin, TWIST1 induction, ITGB1/RHOA/PLAU/VEGFA upregulation, increased invasive protrusions (p.582) "Tumour cells cultured with TRMs expressed a distinct molecular program associated with tumour cell migration, epithelial–mesenchymal transition (EMT) and lipid metabolic changes ... after co-culture with TRMs, tumour cells showed a significant reduction in their protein expression of E-cadherin" — confidence: high — type: mechanistic — links: [[concepts/macrophage-induced-emt-tumor-invasiveness]] [[claims/trm-induce-emt-program-tumor-cells-spheroids]]
- [trm-conditioned-medium-promotes-kp-migration] TRM-conditioned medium (cell-free) is sufficient to promote KP tumour-cell migration in transwell assays — TRM secretome carries the invasiveness signal (p.582) "The ability of TRMs to promote invasiveness in KP cells was further established through a transwell migration assay using conditioned medium derived from tumour TRMs" — confidence: high — type: mechanistic — links: [[concepts/macrophage-induced-emt-tumor-invasiveness]] [[claims/trm-conditioned-medium-promotes-kp-migration]]
- [trm-deficient-tumors-show-reduced-twist1-zeb1] KP tumour cells in TRM-depleted (CD169-DTR + DT) mice show reduced TWIST1 and ZEB1 expression in vivo at day 5 (p.582-583) "tumour cells that formed in the absence of TRMs expressed reduced levels of the EMT-associated transcription factor TWIST1" — confidence: high — type: correlational — links: [[concepts/macrophage-induced-emt-tumor-invasiveness]] [[claims/trm-deficient-tumors-show-reduced-twist1-zeb1]]
- [trm-uniquely-enhance-cd73-ctla4-on-treg] TRMs and MDMs are equally efficient at promoting Treg differentiation, but only TRMs uniquely upregulate CD73 and CTLA-4 on the differentiated Treg cells (p.582) "both compartments were similarly efficient at promoting the differentiation of naive T cells into Treg cells, but that TRMs were uniquely able to enhance the expression of CD73 and CTLA-4 on differentiated Treg cells compared to MDMs" — confidence: high — type: mechanistic — links: [[concepts/trm-induced-treg-licensing]] [[claims/trm-uniquely-enhance-cd73-ctla4-on-treg]]
- [trm-tumor-produce-ccl17-tgfb1] Tumour-associated TRMs express high levels of CCL17 and TGFβ1, chemokines associated with Treg recruitment / differentiation / expansion (p.582) "tumour-associated TRMs expressed high levels of Ccl17 and Tgfb1, which are known to contribute to the recruitment, differentiation and expansion of Treg cells" — confidence: high — type: mechanistic — links: [[concepts/trm-induced-treg-licensing]] [[claims/trm-tumor-produce-ccl17-tgfb1]]
- [treg-localize-close-trm-tumor] FOXP3⁺ Treg cells localise close to TRMs (MRC1⁺) in tumour lesions; their tumour accumulation correlates with tumour growth in mice (p.582) "Treg cells established close contacts with TRMs in tumour lesions, and that the accumulation of Treg cells correlated with tumour growth in mice" — confidence: high — type: correlational — links: [[concepts/trm-induced-treg-licensing]] [[claims/treg-localize-close-trm-tumor]]
- [cd169-dtr-depletes-trm-not-mdm] Intranasal diphtheria toxin into CD169-DTR mice specifically depletes lung TRMs without affecting other myeloid populations; CD169 expression is negligible on monocytes and MDMs in lungs and early tumour lesions (p.582) "intranasal instillation of diphtheria toxin into CD169-DTR mice depleted TRMs specifically, in the lungs, without affecting other myeloid cell populations" — confidence: high — type: methodological — links: [[foundations/cd169-dtr-trm-depletion]] [[claims/cd169-dtr-depletes-trm-not-mdm]]
- [trm-depletion-no-effect-tumor-seeding-24h] TRM depletion does not affect KP tumour cell seeding: similar numbers of KP cells were recovered from TRM-sufficient vs -deficient lungs 24 hours after injection (p.582-583) "Reduced tumour burden was not a result of impaired tumour cell seeding, as similar numbers of KP cells were recovered from the lungs of TRM-sufficient or -deficient mice 24 hours after injection" — confidence: high — type: correlational — links: [[claims/trm-depletion-no-effect-tumor-seeding-24h]]
- [trm-depletion-reduces-tumor-burden-early-nsclc] TRM depletion (CD169-DTR + DT) before KP tumour engraftment reduces tumour burden (size and area, but not number of foci) and increases apoptotic CC3⁺ cells and slow-cycling p27⁺ cells (p.582-583) "depletion of TRMs reduced the size of tumours without affecting the number of tumour lesions" — confidence: high — type: pharmacological — links: [[concepts/tissue-resident-macrophage-tumor-niche]] [[claims/trm-depletion-reduces-tumor-burden-early-nsclc]]
- [trm-depletion-reduces-treg-cd73-ctla4] TRM depletion reduces tumour Treg cell numbers and reduces CTLA-4 and CD73 expression on the remaining Treg cells; effect restricted to tumour (no change in spleen or tumour-draining lymph node) (p.583) "depletion of TRMs not only resulted in a reduction in the number of Treg cells in early lesions, but also altered the molecular programs of Treg cells, leading to reduced expression of CTLA-4 and CD73" — confidence: high — type: mechanistic — links: [[concepts/trm-induced-treg-licensing]] [[claims/trm-depletion-reduces-treg-cd73-ctla4]]
- [trm-depletion-increases-cd8-effector-tcells] TRM depletion increases tumour CD3⁺ infiltrating T cells, IFNγ⁺TNF⁺CD8⁺ effector T cells, and the CD8⁺/Treg ratio (p.583) "We also found increases in the total number of CD3+ T cells, the total number of IFNγ+TNF+CD8+ T cells and the ratio of CD8+ T cells to Treg cells in tumour lesions in TRM-depleted mice" — confidence: high — type: mechanistic — links: [[claims/trm-depletion-increases-cd8-effector-tcells]]
- [trm-depletion-no-effect-established-tumors] TRM depletion in already-established KP lesions (day 12-15 onwards) does NOT affect tumour burden, Treg compartment, CD8/Treg ratio, or CD3⁺ TIL number — TRM niche function is restricted to early stages (p.583) "In contrast to early-stage tumour lesions, depletion of TRMs in established KP lesions (days 12–15) did not affect tumour burden, the Treg compartment, the CD8+ T cell/Treg cell ratio or the number of CD3+ tumour-infiltrating T cells" — confidence: high — type: mechanistic — links: [[concepts/tissue-resident-macrophage-tumor-niche]] [[claims/trm-depletion-no-effect-established-tumors]]
- [trm-depletion-reduces-b16-melanoma-tumor] TRM depletion in B16-OVA melanoma reduces tumour burden, expands IFNγ⁺TNF⁺ effector CD4⁺ and CD8⁺ T cells, and reduces PD-1 MFI on T cells, despite no change in OVA-specific OT-I/OT-II expansion (p.583) "A stronger effect on tumour growth was observed when TRMs were depleted in the more immunogenic B16-OVA model of metastatic melanoma" — confidence: high — type: pharmacological — links: [[claims/trm-depletion-reduces-b16-melanoma-tumor]]
- [trm-mdm-conserved-cross-species-pparg-trem2] Group I (PPARG/MARCO/SIGLEC1/STMN1) and group II (TREM2/SPP1/APOE/GPNMB/CCR2/CD14) macrophage signatures are conserved across human and mouse NSCLC despite broad cross-species macrophage divergence (p.580) "Mouse and human group I clusters shared many genes, including high expression of scavenger receptors (MARCO and SIGLEC1), cell-cycle genes (STMN1 and TUBA1B)—suggesting self-renewal potential—and the transcription factor PPARG. Mouse and human group II clusters also shared many genes, including genes associated with lipid metabolism (APOE, TREM2, SPP1 and GPNMB)" — confidence: high — type: methodological — links: [[concepts/macrophage-ontogeny-resident-vs-monocyte-derived]] [[concepts/trem2-tumor-associated-macrophage]] [[claims/trm-mdm-conserved-cross-species-pparg-trem2]]

## Discussion captured

### Authors' interpretation

The authors interpret their findings as establishing TRMs as a **critical contributor to early lung cancer progression**, providing both an EMT-promoting niche and a Treg-licensing function. They argue that TRMs are heavily tissue-imprinted (consistent with minimal chromatin remodelling) but functionally subverted in early tumour lesions to deliver an EMT signal to neighbouring tumour cells while expanding immunosuppressive Tregs. The temporal restriction (early-only effect) is interpreted as evidence that TRMs act as a "founder niche" that helps tumour cells establish and escape immune control, after which monocyte-derived MDMs take over the macrophage compartment.

### Comparisons with prior literature (made by authors)

- Self-renewing TRM origin: Ginhoux et al. *Science* 2010 (microglia); Hashimoto et al. *Immunity* 2013; Schulz et al. *Science* 2012 — establish embryonic origin of TRMs.
- Sawai et al. *Immunity* 2016 (Map17-creER labelling adult HSCs) — provides the genetic tool used here.
- Yona et al. *Immunity* 2013 (Cx3cr1-creER) — alternative monocyte fate-mapping tool.
- Liu et al. *Cell* 2019 (Ms4a3 fate-map) — companion monocyte-restricted reporter.
- Zilionis et al. *Immunity* 2019 — independent NSCLC scRNA-seq used to validate group I as alveolar TRM signature.
- Leach et al. *Cell Reports* 2020 — bulk RNA-seq of purified human alveolar macrophages used as orthogonal validation.
- Lavin et al. *Cell* 2017 (Merad lab) — original Treg enrichment finding in NSCLC; this paper extends with mechanism.
- Mantovani et al. *Nat Rev Clin Oncol* 2017 — TAMs as cancer therapy targets, framing of the problem.
- Russell et al. *Nat Immunol* 2009 — granuloma topology comparison for TRM redistribution to tumour periphery.
- Yang et al. *Cell* 2004; Dongre & Weinberg *Nat Rev Mol Cell Biol* 2019 — TWIST1 / EMT framework used to interpret KP-TRM 3D co-culture findings.
- Mucida et al. *Science* 2007; Soroosh et al. *J Exp Med* 2013; Mizukami et al. *Int J Cancer* 2008 — CCL17 / TGFβ-driven Treg differentiation, extended here to TRMs.

### Mechanistic hypotheses proposed

- **EMT-niche hypothesis**: tumour-associated TRMs secrete factors (VEGFA, PLAU/uPA among them) that activate EMT in adjacent tumour cells; "molecules such as VEGFA and the urokinase-type plasminogen activator (uPA, encoded by Plau) ... have been linked to an immunosuppressive microenvironment that is related to the differentiation of Treg cells".
- **Treg-licensing hypothesis**: TRMs uniquely enhance Treg suppressive programmes (CD73, CTLA-4) via CCL17 and TGFβ1 signalling, distinct from MDM-driven Treg differentiation alone.
- **Temporal-niche hypothesis**: the niche function of TRMs is restricted to early tumour lesions (≤ day 12); once established, tumours are independent of TRMs and can be sustained by MDM-dominated TME.

### Caveats and self-criticism

- TRMs and MDMs were assigned by transcriptional signatures plus Map17-creER / Cx3cr1-creER fate mapping; complete labelling efficiency (especially for MDMs) is implicit.
- The 3D spheroid co-culture and ex vivo Treg differentiation systems are necessarily reductionist; the authors validate key findings (TWIST1/ZEB1, Treg modulation) in vivo.
- The authors note that B16-OVA tumour reduction was not associated with OVA-specific T cell expansion, suggesting non-antigen-specific (general T-cell-tolerance) effects of TRM depletion — they do not fully resolve the mechanism.

### Future directions suggested

- Therapeutic targeting of TRMs for **early NSCLC prevention or treatment** ("identifies TRMs as a potential target for the prevention or treatment of early NSCLC lesions").
- Better dissection of CCL17/TGFβ1-driven Treg licensing.
- Whether the EMT-niche function generalises to other early epithelial cancers.

## Limitations

- Mouse-centric mechanism: Map17/Cx3cr1/Ms4a3 fate mapping and CD169-DTR depletion are mouse tools; human TRM identity is inferred from cross-species signature similarity.
- CD169-DTR is not perfectly TRM-specific outside the lung (CD169 is expressed by some splenic and lymph-node macrophages); the authors mitigate by intranasal route and confirm specificity in lung.
- ATAC-seq sample size (3 biological replicates per condition) is modest.
- 3D spheroid co-culture uses bulk-sorted TRMs; intra-TRM heterogeneity may confound signal attribution.
- In vivo TWIST1/ZEB1 quantification is at day 5, a single early time point.
- Bulk RNA-seq of TRMs cannot resolve emerging tumour-associated subpopulations within group I.
- The paper does not directly identify the secreted factor(s) responsible for TRM-induced EMT (only correlates with VEGFA / PLAU / TGFβ1 expression).

## Open questions

### Open questions raised by authors

- Which specific factor(s) secreted by TRMs are necessary and sufficient for the EMT/invasiveness programme in adjacent tumour cells?
- Why is the niche function restricted to early lesions — what changes in TRMs (or in tumours) by day 12-15 that abolishes the dependence?
- Is TRM-driven EMT generalisable to other early epithelial cancers beyond NSCLC?
- How can TRMs be selectively targeted in patients without affecting beneficial homeostatic functions (surfactant clearance)?

### Open questions identified during ingest

- How does the alveolar TRM PPARG⁺/MARCO⁺ signature relate to MoMac-VERSE cluster #2 (HES1) versus a missing alveolar-specific cluster?
- Whether the TREM2/SPP1/APOE/GPNMB MDM signature here corresponds 1:1 to MoMac-VERSE cluster #3 TREM2_Mac in human pan-cancer atlases.
- What is the contribution of HIF1α / hypoxia signalling to the TRM-induced EMT programme — does hypoxia prime the niche?
- Are there epigenetic regulators (TET2, NF-κB, PPARG) that switch the TRM compartment between homeostatic and pro-tumorigenic states (relevant to thesis-project axis)?

## My take

A landmark paper for the field of cancer macrophage biology and a critical reference for thesis work that needs to disentangle ontogeny (TRM vs MDM) from polarisation/state. The Casanova-Acebes et al. study is the canonical citation for "alveolar TRMs are the early-niche, MDMs dominate later" in NSCLC, and provides the most direct *in vivo* causal evidence (CD169-DTR depletion) for a niche role. The temporal restriction (early-only effect) is mechanistically intriguing and largely under-explored — likely reflects loss of TRM-tumour contact once tumours expand past the original parenchymal niche. For HypoxiaVERSE the paper is contextual rather than directly load-bearing: the hypoxic mMAC1 signature is monocyte-derived, mapping to group II MDM territory (TREM2/SPP1/APOE/GPNMB axis), so the TRM/MDM dichotomy here is the upstream framework that contextualises mMAC1 as a state within the MDM compartment. The MHC-II upregulation and CCL17/TGFβ1 production by tumour TRMs may be relevant when comparing the immunogenic state of TRMs vs the immunosuppressive state of monocyte-derived TAMs.

## Related

- [[papers/pd-l1-expressing-tumor-associated-macrophages]] — Wang 2024 Cell Reports Medicine; in human BC PD-L1+ MoDMs are immunostimulatory — complementary ontogeny axis where TRM (not MoDM) drive suppression in NSCLC
- [[concepts/macrophage-ontogeny-resident-vs-monocyte-derived]] — extended in NSCLC: this paper applies Map17-creER and Cx3cr1-creER fate mapping to assign group I to TRM (embryonic) and group II to MDM (adult-HSC) lineage in lung cancer
- [[concepts/trem2-tumor-associated-macrophage]] — group II MDM signature here (TREM2/SPP1/APOE/GPNMB) corresponds to the canonical TREM2 TAM cluster
- [[concepts/tumor-associated-macrophage-immunosuppression]] — TRM-Treg axis is a parallel immunosuppressive mechanism alongside TREM2/IL4I1 TAM programmes
- [[concepts/tissue-resident-macrophage-tumor-niche]] — concept introduced by this paper
- [[concepts/macrophage-induced-emt-tumor-invasiveness]] — concept introduced by this paper
- [[concepts/trm-induced-treg-licensing]] — concept introduced by this paper
- [[foundations/kp-nsclc-mouse-model]] — primary in vivo model
- [[foundations/cd169-dtr-trm-depletion]] — TRM ablation tool
- [[foundations/pdzk1ip1-map17-creer-fate-mapping]] — adult HSC fate mapping
- [[foundations/cx3cr1-creer-fate-mapping]] — monocyte fate mapping
- [[foundations/ms4a3-tdtom-monocyte-tracing]] — monocyte-restricted reporter
- [[foundations/atac-seq]] — chromatin accessibility profiling
- [[foundations/scrna-seq-10x-chromium]] — primary transcriptomic platform
- [[papers/cross-tissue-single-cell-landscape-human]] — Mulder 2021 MoMac-VERSE provides the pan-cancer reference atlas where TREM2 TAM is cluster #3; complementary to the NSCLC-specific niche mechanism here
- [[papers/nf-kb-tet2-promote-macrophage-reprogramming]] — Calafell 2024 MAC reprogramming under hypoxia is mechanistically orthogonal but contextually related (hypoxic mMAC1 is monocyte-derived and maps to MDM territory)
