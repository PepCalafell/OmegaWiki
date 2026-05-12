---
# === Identification ===
title: "NF-κB and TET2 promote macrophage reprogramming in hypoxia that overrides the immunosuppressive effects of the tumor microenvironment"
slug: nf-kb-tet2-promote-macrophage-reprogramming
arxiv: ""
doi: "10.1126/sciadv.adq5226"
pmid: "39292770"
venue: "Science Advances"
year: 2024
authors:
  - "Carlos de la Calle-Fabregat"
  - "Josep Calafell-Segura"
  - "Margaux Gardet"
  - "Garett Dunsmore"
  - "Kevin Mulder"
  - "Laura Ciudad"
  - "Aymeric Silvin"
  - "Joaquim Moreno-Càceres"
  - "Ángel L. Corbí"
  - "Cristina Muñoz-Pinedo"
  - "Judith Michels"
  - "Sébastien Gouy"
  - "Charles-Antoine Dutertre"
  - "Javier Rodríguez-Ubreva"
  - "Florent Ginhoux"
  - "Esteban Ballestar"
first_author: "Carlos de la Calle-Fabregat"
corresponding_author: "Carlos de la Calle-Fabregat; Esteban Ballestar"

# === Source & metadata ===
source_type: pdf
s2_id: "e774e5990a3519727f0ecfce6062f2d67e15e016"
date_added: 2026-05-05
ingested_date: 2026-05-11
ingest_version: 2
last_reviewed: null

# === Classification ===
importance: 4
tier: TIER_1
tags:
  - hypoxia
  - macrophage
  - NF-kB
  - TET2
  - DNA-methylation
  - HIF1a
  - p65
  - RELA
  - tumor-microenvironment
  - bladder-cancer
  - ovarian-cancer
  - immunogenicity
  - ChIP-seq
  - EPIC-array
  - DoRothEA
  - MoMac-VERSE
  - IL4I1
  - LPS
  - inflammation
keywords:
  - hypoxic macrophage reprogramming
  - NF-κB-mediated DNA demethylation
  - TET-mediated demethylation under hypoxia
  - HIF1α NF-κB co-regulation
  - hypoxic inflammatory macrophage
  - mMAC1
  - cluster C2 hypomethylation
  - tumor-associated macrophage immunogenicity
  - IL4I1 macrophage in vivo correlate
  - bladder urothelial carcinoma prognosis
  - ovarian carcinoma macrophage
domain: "immunology / epigenetics / oncology"

# === Biomedical domain ===
tissue:
  - blood
  - bone_marrow
  - bladder
  - ovary
  - in_vitro_only
condition:
  - healthy
  - cancer
disease_specific:
  - bladder_urothelial_carcinoma
  - ovarian_carcinoma
  - hypoxic_tumor_microenvironment
species:
  - human
hypoxia_relevant: true
contains_immune_cells: true
contains_myeloid: true

# === Technique ===
techniques:
  - EPIC_array
  - bulk_RNA-seq
  - ChIP-seq
  - flow_cytometry
  - immunofluorescence
  - Western_blot
  - ELISA
  - qRT-PCR
  - CD8_T_cell_coculture
  - scRNA-seq_10x
  - CIBERSORTx_deconvolution
  - CellChat
  - DoRothEA
  - HOMER_motif_analysis
  - GSEA
  - TCGA_survival_analysis
n_samples: 4
n_cells_total: null
integration_method: ""

# === Biology captured ===
key_cell_types:
  - monocyte_derived_macrophage
  - iMAC21_normoxic_immature
  - iMAC1_hypoxic_immature
  - mMAC21_normoxic_LPS_activated
  - mMAC1_hypoxic_LPS_activated
  - IL4I1_TAM
  - IL1B_monocyte
  - ISG_monocyte
  - TREM2_TAM
  - FOLR2_TAM
  - CD8_T_cell
  - bladder_urothelial_carcinoma
  - ovarian_carcinoma
key_markers:
  - HIF1A
  - RELA_p65
  - NFKB1
  - IL6
  - TNF
  - IL10
  - HLA-DR
  - CD86
  - CD80
  - CD14
  - CD163
  - CD206
  - IRF1
  - STAT2
  - IL4I1
  - CXCL9
  - CXCL10
  - CCL5
  - TET2
  - HIF2A
key_pathways:
  - HIF1α_canonical_hypoxia_response
  - NF-κB_LPS_TLR4_signaling
  - TET-mediated_active_DNA_demethylation
  - HIF1α-NF-κB_non-physical_co-regulation
  - MHC_class_II_antigen_presentation
  - CXCL9_CXCL10_T_cell_chemotaxis
  - IFN_STAT_signaling
  - AP-1_RUNX_ETS_macrophage_differentiation

# === User project membership ===
projects:
  - hypoxia
  - thesis
priority: core
read_status: deep_read

# === HypoxiaVERSE-specific ===
hypoxiaverse_status: included
exclusion_reason: null
data_availability: "GEO accessions in original paper (DNA methylation EPIC arrays, RNA-seq, ChIP-seq). Sci Adv 10, eadq5226 (2024), CC BY-NC license."

# === Cross-references ===
code_url: ""
cited_by: []
---

## Problem

In the tumor microenvironment (TME), tumor-associated macrophages (TAMs) are commonly reprogrammed into immunosuppressive cells, and their presence is largely associated with poor prognosis. Hypoxia, a near-universal TME feature, is widely framed as an immunosuppressive cue: low oxygen inhibits TET methylcytosine dioxygenases (which depend on O₂, Fe²⁺, and α-ketoglutarate), driving aberrant hypermethylation of tumor-suppressor genes and dampening inflammatory programs. Yet the *direct* effect of hypoxia on macrophage (MAC) function — and the *cell-type-specific* interplay between HIF and NF-κB transcriptional programs in MACs — remains controversial, with literature reporting both pro- and anti-inflammatory outcomes. The paper asks: does hypoxia silently suppress MAC immunogenicity (the dominant narrative), or does hypoxia paradoxically *enhance* it via specific epigenetic-transcriptional mechanisms that have been missed by prior work?

## Key idea

Hypoxia, contrary to the prevailing TME paradigm, *boosts* macrophage immunogenicity. The mechanism is a non-canonical NF-κB-driven epigenetic-transcriptional axis that overrides global hypoxic TET inhibition at a focal 403-CpG cluster (C2) of proinflammatory enhancers. In vitro M-CSF-differentiated MACs from human monocytes, when LPS-activated under 1% O₂ ("mMAC1"), display: (i) increased IL-6/TNF-α/HLA-DR/CD80/CD86 and decreased CD14/CD163/CD206 + reduced T-cell suppression; (ii) hypoxia-specific de novo DNA demethylation of cluster C2 enriched in NF-κB motifs; (iii) HIF1α and p65 ChIP-seq peaks that converge on inflammatory promoters/enhancers via non-physical cooperation (Pearson r = 0.13), with HIF1α binding preceding p65 binding in time; (iv) pharmacological dissection (BAY11-7082, PX-478, 4-octyl itaconate) showing p65 inhibition — but not HIF1α inhibition — blocks C2 demethylation, while TET2 inhibition recapitulates the methylation gain. The mMAC1 signature is found in vivo in IL4I1⁺ MACs (and IL1B Mo, ISG Mo) of the MoMac-VERSE atlas, sorted from primary ovarian tumors recapitulates the C2 hypomethylation, and correlates with better overall survival in bladder urothelial carcinoma (BLCA), ovarian carcinoma (OC), and other immune-hot cancers. Cell-cell communication analysis identifies CXCL9:CXCR3, CXCL10:CXCR2, HLA class I:CD8, and MIF:CD74 mMAC1↔T-cell pairs that link this MAC state to T-cell activation. The work *challenges the paradigm* of hypoxia as uniformly immunosuppressive and proposes mMAC1 (IL4I1 MAC in vivo) as an actionable target for anti-cancer immunity.

## Method

In vitro differentiation system: human peripheral blood monocytes (MOs) differentiated to MACs in the presence of M-CSF for 5 days under normoxia (21% O₂) or hypoxia (1% O₂), then activated with LPS (or vehicle) for 48 hours. Four conditions: iMAC21 (normoxic resting), mMAC21 (normoxic activated), iMAC1 (hypoxic resting), mMAC1 (hypoxic activated). Functional assays: ELISA for IL-6/TNF-α/IL-10 in supernatants; flow cytometry for HLA-DR/CD86/CD80/CD14/CD163/CD206; allogeneic CD8⁺ T-cell proliferation co-culture (CFSE dilution). Epigenomics: Illumina Infinium MethylationEPIC arrays profiling DMPs (FDR<0.05, |Δβ|>0.2) → three CpG clusters (C1: 2782, C2: 403, C3: 903). Transcriptomics: bulk RNA-seq, FDR<0.05, |log2FC|>1 → four clusters (E1-E4) of 3737 DEGs; GO enrichment; GSEA; DoRothEA TF regulon inference; HOMER motif analysis. ChIP-seq for HIF1α and p65 across all four conditions → three HIF1α clusters (H1-H3) and one p65 cluster (P1); consensus peak calling; co-occurrence analysis; motif enrichment in HIF1α-specific, p65-specific, and cobound peaks. Pharmacology: pre-treatment of MAC21/MAC1 with BAY11-7082 (p65 inhibitor), PX-478 (HIF1α inhibitor), 4-octyl itaconate (TET2 inhibitor) before LPS; readout = EPIC methylation + qRT-PCR. NF-κB-stimulus generalization: P3C, CpG, polyI:C, TNF-α, IL-1β substituted for LPS; "swap" experiments swap hypoxic/normoxic conditions before activation. In vivo validation: signature projection onto MoMac-VERSE (13-tissue human MNP scRNA-seq atlas, Mulder 2021); TCGA survival analysis in 12 cancer types; CIBERSORTx deconvolution of TCGA-BLCA bulk RNA-seq; CellChat ligand-receptor analysis on BLCA scRNA-seq; flow cytometry sorting of IL4I1/TREM2/FOLR2 MACs from primary ovarian tumors followed by EPIC + bulk RNA-seq.

## Results

### 1. Hypoxia enhances MAC immunogenicity at the functional and epigenetic levels (Fig. 1)
- mMAC1 secretes more IL-6 and TNF-α and less IL-10 than mMAC21.
- mMAC1 has higher HLA-DR/CD86/CD80 and lower CD14/CD206/CD163 — antigen-presenting, less immunoregulatory phenotype.
- mMAC1 suppresses allogeneic CD8⁺ T-cell proliferation *less* than mMAC21 — i.e., reduced suppressive capacity.
- EPIC array DMPs aggregate into 3 clusters: C1 (2782 CpGs, hypomethylated in normoxic differentiation, AP-1-motif enriched, blunted in hypoxia); C2 (403 CpGs, hypomethylated specifically in mMAC1, NF-κB-motif enriched, with TNF/IL6 loci as examples); C3 (903 CpGs, hypermethylated in normoxic differentiation, RUNX/ETS motifs, blunted in hypoxia).
- Cluster C2 is enriched in intergenic/open-sea regions and gains H3K4me1/H3K27ac de novo enhancer marks after LPS in normoxia — distal LPS-responsive enhancers.

### 2. Transcriptomic reprogramming is HIF1α + NF-κB + STAT/IRF (Fig. 2)
- 3737 DEGs cluster into E1 (233, up in hypoxia), E2 (1452, up in activated, more in mMAC1), E3 (732, down in hypoxia), E4 (1330, down on activation).
- C2-associated genes are specifically enriched in E2 (P = 3.03×10⁻⁴⁴; Fisher's exact).
- DoRothEA: HIF1A is the top regulon on the hypoxia axis in resting MACs; in activated MACs, STAT2/IRF1/RELA overtake HIF1A — i.e., LPS+hypoxia activates *additional* inflammatory regulons beyond HIF1A. RELA NES = 3.8 (iMAC21 vs iMAC1) → 5 (mMAC21 vs mMAC1).
- NF-κB-activating stimuli LPS, P3C, CpG, polyI:C, TNF-α, IL-1β all converge on the same hypoxic up-regulation — it is NF-κB activation, not LPS specifically, that drives the response.
- "Swap" experiments (transferring cells between O₂ conditions 2h before LPS) recapitulate the response: the activation step, not the differentiation step, is the hypoxic-sensitive window.

### 3. HIF1α + p65 cooperate at chromatin without physical interaction (Fig. 3 & 4)
- Both HIF1α and p65 proteins peak in mMAC1. HIF1α increases in both nucleus and cytoplasm under hypoxia; p65 accumulates cytoplasmically under hypoxia but specifically translocates to the nucleus upon LPS.
- ChIP-seq HIF1α clusters: H1 (hypoxia-induced), H2 (LPS-induced), H3 (both). p65 cluster P1 peaks in mMAC1.
- HIF1α-specific peaks enriched in HIF + ETS motifs; H2/H3 also enriched in AP-1 + IRF; cobound HIF1α/p65 peaks enriched in HIF, NF-κB, AP-1, IRF, ETS motifs.
- Cobound peak HIF1α-p65 binding intensity correlates weakly (Pearson r = 0.13, P = 2.5×10⁻⁴): cooperation is not via direct physical interaction.
- HIF1α binds cobound peaks earlier (already in iMAC1) than p65 (which peaks in mMAC1) → HIF1α priming hypothesis.
- HIF1α-only peaks → glycolysis GO categories; p65-only peaks → immune cell differentiation/adhesion; cobound peaks → LPS-mediated signaling pathway.
- GSEA: HIF1α-bound and p65-bound genes are up only by hypoxia or LPS respectively; cobound genes up by either challenge alone. iMAC1 *down*-regulates p65-bound genes — paradoxical inflammatory suppression of unstimulated hypoxic MACs.
- C2 CpGs co-localize with strong p65 signal (not HIF1α) in mMAC1; p65-specific peak set is exclusively associated with C2 regions (Fisher P = 8.3×10⁻¹⁰³).

### 4. Pharmacological dissection: p65 — not HIF1α — drives C2 demethylation; TET2 inhibition phenocopies hypoxia inhibition (Fig. 4K-L)
- BAY11-7082 (p65 inhibitor) blocks C2 demethylation in mMAC1, restoring methylation to mMAC21 levels.
- PX-478 (HIF1α inhibitor) does NOT block C2 demethylation alone.
- 4-octyl itaconate (TET2 inhibitor) increases C2 methylation and decreases C2-target gene expression — TET2 is necessary for active demethylation.
- p65 inhibition decreases C2-target gene expression (NFKB1, CCL5, IRF1, IL6); HIF1α inhibition partially decreases some — additional HIF1α-dependent mechanisms.

### 5. mMAC1 signature maps in vivo to IL4I1 / IL1B Mo / ISG Mo (Fig. 5A-C)
- Projection of mMAC1 gene + C2 DNA methylation signatures onto MoMac-VERSE (13-tissue MNP atlas, Mulder 2021): preferential enrichment in cluster #15 (IL1B Mo), #6 (IL4I1 Mac), #4 (ISG Mo).
- TREM2 Mac (#3) and FOLR2 Mac (#2) are *negative controls* — not enriched.

### 6. mMAC1 correlates with better cancer survival (Fig. 5D-E & fig. S5D)
- Hypoxic MAC signatures (iMAC1, mMAC1, IL4I1) associated with better OS in 10/12 (mMAC1) and 7/12 (IL4I1) TCGA cancer types.
- Normoxic signatures (iMAC21, mMAC21) associated with worse OS in 10/12.
- TREM2 worst (7/12 poor prognosis); FOLR2 mixed.
- BLCA Kaplan-Meier: mMAC1 HR = 0.491 (CI 0.302-0.797, P = 0.003); mMAC21 HR = 2.266 (1.401-3.663, P < 0.001).
- BLCA C2 low-methylation → better survival, HR = 1.72 (1.169-2.53, P = 0.00589).

### 7. mMAC1 ↔ T-cell crosstalk drives an immune-hot TME (Fig. 5F-H)
- BLCA CIBERSORTx deconvolution separates "immune hot" (n=161) vs "immune cold" (n=226) tumors. Immune-hot tumors are mMAC1- and T-cell-rich; mMAC1 and T-cell percentages correlate (r = 0.74, P = 2.2×10⁻⁶⁷); iMAC21 anticorrelates (r = -0.27, P = 5×10⁻⁸).
- CellChat ligand-receptor pairs mMAC1 → T cell include CXCL9:CXCR3 and CXCL10:CXCR2 (chemotaxis), ICAM1:SPN (trafficking), HLA-A/B/C/E/F:CD8 (TCR/antigen-presentation), and MIF:CD74+CXCR4/CD44 (costimulation).

### 8. IL4I1 MACs sorted from primary ovarian tumors recapitulate the mMAC1 program (Fig. 5I-L)
- Sorting strategy from Mulder 2021 (with optimizations) yields IL4I1, TREM2, FOLR2 MAC populations from OC.
- IL4I1 MACs have the lowest C2 methylation among the three populations.
- p65 motif is the most enriched motif in IL4I1-specific demethylated CpGs.
- RELA and HIF1A regulons up-regulated only in IL4I1 (not TREM2/FOLR2); RFX5/NFKB1/IRF1/E2F4 regulons also active in IL4I1, mirroring mMAC1.

## All claims (exhaustive)

- `[c01]` Hypoxia enhances macrophage immunogenicity rather than uniformly suppressing it, manifest as proinflammatory cytokine secretion, antigen-presenting surface markers, and reduced T-cell suppression (p.1-2) "hypoxia boosts their immunogenicity" — confidence: high — type: mechanistic — links: [[concepts/mmac1-hypoxic-inflammatory-macrophage]] [[concepts/tumor-associated-macrophage-immunosuppression]] [[claims/hypoxia-boosts-macrophage-immunogenicity-nf-kb]]
- `[c02]` mMAC1 (hypoxic LPS-activated MAC) secretes higher levels of IL-6 and TNF-α and lower levels of IL-10 than mMAC21 (normoxic LPS-activated MAC) (p.2, Fig. 1B) "mature hypoxic MACs (mMAC1) produced higher levels of the inflammatory cytokines interleukin-6 (IL-6) and tumor necrosis factor–α (TNF-α) and lower levels of the anti-inflammatory cytokine IL-10 than mature normoxic MACs (mMAC21)" — confidence: high — type: quantitative — links: [[concepts/mmac1-hypoxic-inflammatory-macrophage]] [[foundations/nf-kb-p65-rela]] [[claims/hypoxia-enhances-proinflammatory-cytokine-secretion-macrophages]]
- `[c03]` mMAC1 expresses higher HLA-DR, CD80, CD86 and lower CD14, CD163, CD206 than mMAC21, consistent with enhanced antigen presentation and reduced immunoregulatory phenotype (p.2, Fig. 1C) "mMAC1 expressed higher levels of the major histocompatibility complex (MHC) class II human leukocyte antigen–DR (HLA-DR) and costimulatory proteins CD86 and CD80 than their normoxic counterpart... resting/immunoregulatory MAC surface proteins CD14, CD206, and CD163 were decreased in mMAC1 versus mMAC21" — confidence: high — type: quantitative — links: [[concepts/mmac1-hypoxic-inflammatory-macrophage]] [[claims/mmac1-higher-mhcii-costim-lower-suppressive-markers]]
- `[c04]` Hypoxic MACs (iMAC1 and mMAC1) display decreased capacity to suppress CD8⁺ T-cell proliferation versus normoxic counterparts in a coculture assay (p.2, Fig. 1D, fig. S1A) "Hypoxic cells, both at steady state and after activation, displayed a decreased capacity to suppress CD8+ T cell proliferation than normoxic cells in a coculture assay" — confidence: high — type: methodological — links: [[concepts/mmac1-hypoxic-inflammatory-macrophage]] [[claims/hypoxic-macs-lose-cd8-suppressive-capacity]]
- `[c05]` Hypoxia partially blocks AP-1-driven DNA demethylation that normally occurs during MAC differentiation (cluster C1, 2782 CpGs) (p.2-3, Fig. 1E-F) "Clusters C1 and C3 corresponded with hypomethylated and hypermethylated CpG sites, respectively, in normoxic MACs when compared to MOs. In these clusters, the methylation tendency was partially inhibited in hypoxia... DMPs in cluster C1... were enriched in motifs of the activator protein 1 (AP-1) complex, canonically associated with MAC differentiation" — confidence: high — type: methodological — links: [[foundations/tet-mediated-dna-demethylation]] [[claims/hypoxia-inhibits-ap-driven-demethylation-during]]
- `[c06]` Cluster C2 (403 CpGs) shows hypoxia-specific de novo DNA demethylation in LPS-activated MACs and is highly enriched in NF-κB motifs; example loci include IL6 and TNF (p.3, Fig. 1E-F, fig. S1C) "cluster C2 displayed a marked hypomethylation specifically in mature hypoxic MACs (mMAC1)... DMPs in cluster C2 displayed hypoxia-associated demethylation specific to activated MACs and were highly enriched in motifs of the NF-κB family" — confidence: high — type: mechanistic — links: [[concepts/cluster-c2-hypoxia-hypomethylation-signature]] [[concepts/nf-kb-mediated-dna-demethylation-hypoxia]] [[foundations/homer-motif-enrichment-analysis]] [[claims/c2-cluster-cpg-demethylation-specific-hypoxic]]
- `[c07]` Cluster C2 regions are enriched in intergenic/open-sea genomic locations and gain de novo H3K4me1/H3K27ac enhancer marks upon LPS activation, characteristic of distal LPS-responsive enhancers (p.3, fig. S1D-E) "cluster C2 regions gain canonical enhancer (H3K4me1) and enhancer activation (H3K27ac) histone marks after activation in normoxic conditions... suggesting that C2 regions consist of LPS-dependent de novo enhancers" — confidence: high — type: methodological — links: [[concepts/cluster-c2-hypoxia-hypomethylation-signature]] [[claims/c2-regions-lps-dependent-de-novo-enhancers]]
- `[c08]` C2-associated genes are specifically enriched in the transcriptional cluster E2 (LPS-up-regulated, higher in mMAC1) with Fisher's exact P = 3.03×10⁻⁴⁴; GSEA NES = 1.8, FDR = 0.001 for mMAC1 vs mMAC21 (p.4, Fig. 2A,D-E) "Cluster C2–associated genes were specifically enriched within cluster E2, calculated by a Fisher's exact test... significantly associated with... up-regulated genes between mMAC21 and mMAC1 in a gene set enrichment analysis (GSEA)" — confidence: high — type: quantitative — links: [[concepts/cluster-c2-hypoxia-hypomethylation-signature]] [[claims/c2-genes-enriched-e2-transcriptional-cluster]]
- `[c09]` In mMAC21 vs mMAC1, DoRothEA-inferred RELA regulon NES = 5 (vs 3.8 in iMAC21 vs iMAC1), and STAT2/IRF1 overtake HIF1A as top regulons — indicating inflammatory regulons co-active with hypoxic regulons in mMAC1 (p.4, Fig. 2F) "RELA (encoding the p65 subunit of the canonical NF-κB complex) regulon was also significantly activated in hypoxic conditions, although to a greater extent in the LPS-activated conditions (NES = 3.8 in iMAC21 versus iMAC1; 5 in mMAC21 versus mMAC1)" — confidence: high — type: quantitative — links: [[foundations/dorothea-tf-regulon-analysis]] [[foundations/nf-kb-p65-rela]] [[claims/dorothea-hif1a-rela-irf-stat-co-active-mmac1]]
- `[c10]` NF-κB activation, not LPS specifically, drives hypoxic up-regulation of inflammatory genes — P3C, CpG, polyI:C, TNF-α, and IL-1β converge on the same hypoxic response (p.4, fig. S2E) "Stimulation with pathogen-associated molecular pattern (PAMP) LPS, Pam3-Cys (P3C), CpG, poly I:C, and cytokines TNF-α and IL-1β induced increased expression of inflammatory genes in hypoxia as compared to normoxia, in most cases... suggesting that NF-κB overactivation, rather than a particular stimulus, is responsible for the up-regulation of inflammatory genes in hypoxic MACs" — confidence: high — type: pharmacological — links: [[foundations/nf-kb-p65-rela]] [[foundations/lps-toll-like-receptor-signaling]] [[claims/nf-kb-overactivation-not-specific-stimulus-drives-hypoxic-inflammation]]
- `[c11]` The activation step, not the differentiation step, is the hypoxia-sensitive window: 2-hour swap of MACs between O₂ conditions before LPS reproduces canonical hypoxic gene-expression response (p.4-5, fig. S2F-G) "swapping MACs from normoxia to hypoxia 2 hours before activation with LPS proved to be sufficient to increase expression equaling canonical hypoxia levels, and vice versa... LPS activation in hypoxia is sufficient to boost gene expression of inflammatory genes independently of oxygen levels during differentiation" — confidence: high — type: methodological — links: [[claims/hypoxic-activation-not-differentiation-window-critical]]
- `[c12]` HIF1α and p65 protein both peak in mMAC1; HIF1α increases in nucleus and cytoplasm under hypoxia while p65 cytoplasmic under hypoxia and nuclear upon LPS — distinct subcellular dynamics for the two TFs (p.5-6, Fig. 3A-C, fig. S3A-B) "HIF1α protein was increased in hypoxia both in the cytoplasm and the nucleus, whereas p65 was increased in the cytoplasm in hypoxic conditions and increased in the nuclei after activation... The condition showing higher absolute expression of both TFs was mMAC1" — confidence: high — type: mechanistic — links: [[foundations/hif1a]] [[foundations/nf-kb-p65-rela]] [[claims/hif1a-p65-protein-peak-in-mmac1-distinct-localization]]
- `[c13]` HIF1α and p65 ChIP-seq cobinding peaks in mMAC1 show low intensity correlation (Pearson r = 0.13, P = 2.5×10⁻⁴), demonstrating cooperative chromatin binding without obligate physical interaction (p.7, Fig. 4E-F) "intensity of binding of both TFs in mMAC1 common peaks did not show a clear linear correlation (Pearson's r = 0.13)... suggesting a cooperation mechanism that is independent of a physical interaction among HIF1α and p65 proteins" — confidence: high — type: mechanistic — links: [[concepts/hif1a-nf-kb-cooperative-chromatin-binding]] [[foundations/chip-seq]] [[claims/hif1a-p65-cooperate-promoter-regions-without]]
- `[c14]` On cobound peaks, HIF1α binding is established earlier in time (already high in iMAC1) than p65 binding (which peaks in mMAC1) — HIF1α primes p65 recruitment (p.7, Fig. 4E, fig. S4C) "although p65 binding mainly increases after activation in hypoxia (mMAC1), HIF1α binding is notably elevated in the hypoxic steady state (iMAC1), suggesting a prior activation of HIF1α over p65 on commonly bound regions" — confidence: medium — type: mechanistic — links: [[concepts/hif1a-nf-kb-cooperative-chromatin-binding]] [[claims/hif1a-binds-earlier-than-p65-cobound-peaks]]
- `[c15]` HIF1α-only-bound genes are enriched in glycolytic GO terms; p65-only-bound in immune differentiation/adhesion; cobound peaks specifically in LPS-mediated signaling — distinct functional outputs (p.7-8, Fig. 4G-H) "HIF1α-only bound genes were mainly associated with categories related to glycolytic metabolism; p65-only bound genes were associated with immune cell differentiation and adhesion, and genes with cobinding peaks were predominantly associated with the LPS-mediated signaling pathway" — confidence: high — type: methodological — links: [[concepts/hif1a-nf-kb-cooperative-chromatin-binding]] [[claims/hif1a-only-p65-only-cobound-peaks-distinct-functions]]
- `[c16]` Cluster C2 CpGs co-localize with strong p65 ChIP-seq signal (not HIF1α) in mMAC1; C2 regions are exclusively associated with p65-specific peak set (Fisher P = 8.3×10⁻¹⁰³) (p.8, Fig. 4I-J) "C2 regions were characterized by a strong p65 signal in mMAC1, whereas the HIF1α signal was not notably high... C2 regions are exclusively associated with p65-specific peaks" — confidence: high — type: quantitative — links: [[concepts/cluster-c2-hypoxia-hypomethylation-signature]] [[claims/c2-cpgs-colocalize-p65-specific-peaks]]
- `[c17]` BAY11-7082 (p65 inhibitor) blocks hypoxia-specific C2 demethylation while PX-478 (HIF1α inhibitor) does not — p65 is the necessary driver of C2 demethylation (p.8, Fig. 4K) "inhibition of p65 alone (but not of HIF1α alone) was able to hamper DNA demethylation in hypoxia, which appeared at levels comparable to those of MAC21" — confidence: high — type: pharmacological — links: [[concepts/nf-kb-mediated-dna-demethylation-hypoxia]] [[foundations/px-478-hif1a-inhibitor]] [[foundations/bay11-7082-p65-inhibitor]] [[claims/p65-inhibition-blocks-hypoxia-specific-demethylation]]
- `[c18]` 4-octyl itaconate (TET2 inhibitor) increases methylation at cluster C2 and decreases mRNA expression of C2-target genes, demonstrating TET2-mediated active demethylation is required for proinflammatory expression in mMAC1 (p.8, Fig. 4K-L) "samples treated with 4-octyl itaconate showed particularly high DNA methylation levels, as well as decreased mRNA expression, suggesting that DNA methylation is determinant in regulating the expression of these proinflammatory genes" — confidence: high — type: pharmacological — links: [[foundations/tet-mediated-dna-demethylation]] [[foundations/4-octyl-itaconate-tet2-inhibitor]] [[claims/tet-inhibition-blocks-c2-demethylation-target-expression]]
- `[c19]` mMAC1 gene-expression and C2 DNA-methylation signatures preferentially enrich in MoMac-VERSE clusters #15 (IL1B Mo), #6 (IL4I1 Mac), #4 (ISG Mo); TREM2 (#3) and FOLR2 (#2) MACs are negative controls (p.9, Fig. 5A-C, fig. S5A) "we identified an enrichment of mMAC1 gene expression signature, as well as mMAC1-specific DNA demethylation signature (C2-associated genes) on three tissue MO/MAC populations... clusters #15 (IL1B Mo), #6 (IL4I1 Mac), and #4 (ISG Mo)" — confidence: high — type: correlational — links: [[concepts/mmac1-hypoxic-inflammatory-macrophage]] [[concepts/momac-verse-mnp-verse-atlas]] [[concepts/il4i1-tumor-associated-macrophage]] [[claims/mmac1-signature-enriched-momac-verse-il4i1-il1b-isg]]
- `[c20]` mMAC1 / IL4I1 signatures correlate with better overall survival in 10/12 (mMAC1) and 7/12 (IL4I1) TCGA cancer types, including bladder urothelial carcinoma (mMAC1 HR = 0.491, P = 0.003) and ovarian carcinoma; normoxic mMAC21 and TREM2 signatures associate with worse OS (p.9-10, Fig. 5D, fig. S5D-E) "patients with high signatures/scores... of hypoxic MAC signatures (iMAC1 and mMAC1) generally displayed a better overall survival in several different cancer types (10 of 12 cases)" — confidence: high — type: correlational — links: [[concepts/mmac1-hypoxic-inflammatory-macrophage]] [[concepts/tumor-associated-macrophage-immunosuppression]] [[foundations/tcga-the-cancer-genome-atlas]] [[claims/mmac1-signature-correlates-better-cancer-survival]]
- `[c21]` In BLCA, mMAC1 percentage correlates with T-cell percentage (r = 0.74, P = 2.2×10⁻⁶⁷); CellChat identifies CXCL9:CXCR3 and CXCL10:CXCR2 chemoattraction pairs and HLA class I:CD8/MIF:CD74 costimulatory pairs between mMAC1 and T cells (p.10, Fig. 5F-H) "T cell percentage was significantly correlated with mMAC1 (r = 0.74, P = 2.2·10−67)... Cell-cell communication analysis revealed several significant ligand-receptor pairs between mMAC1 and T cells, related to T cell chemotaxis (CXCL9:CXCR3 and CXCL10:CXCR2)" — confidence: high — type: mechanistic — links: [[foundations/cibersortx-deconvolution]] [[foundations/cellchat-cell-cell-communication]] [[claims/mmac1-chemoattracts-cells-cxcl9-cxcl10]]
- `[c22]` IL4I1 MACs sorted from primary ovarian tumors recapitulate C2 hypomethylation (lowest among IL4I1/TREM2/FOLR2), exhibit p65 as the top-enriched motif in their demethylated CpGs, and up-regulate RELA + HIF1A regulons — the in vivo correlate of mMAC1 (p.10-11, Fig. 5I-L) "Through sorting by flow cytometry, we purified IL4I1, TREM2, and FOLR2 MACs through a gating strategy... the IL4I1 population showed the lowest average methylation levels... p65 was the most enriched motif in the demethylated CpGs associated specifically with IL4I1... the expression of genes in the RELA and HIF1A regulons were only up-regulated in IL4I1" — confidence: high — type: methodological — links: [[concepts/il4i1-tumor-associated-macrophage]] [[concepts/mmac1-hypoxic-inflammatory-macrophage]] [[claims/il4i1-macrophages-vivo-correlates-mmac1]]
- `[c23]` Unstimulated hypoxic MACs (iMAC1) paradoxically *down-regulate* p65-bound genes, suggesting an incomplete differentiation/inflammatory-suppression state preceding LPS activation (p.8, Fig. 4H) "MACs differentiated in hypoxia but unstimulated with LPS (iMAC1) showed a significant down-regulation of p65-bound genes... which suggests an inflammatory suppression of these cells, possibly because of an incomplete differentiation process in hypoxic conditions" — confidence: medium — type: mechanistic — links: [[concepts/mmac1-hypoxic-inflammatory-macrophage]] [[claims/imac1-paradoxical-down-p65-bound-genes]]

## Discussion captured

### Authors' interpretation

The authors interpret hypoxia as a paradigm-challenging modulator of MAC immunology. Under low O₂, hypoxia globally suppresses TET-mediated demethylation (consistent with prior work), yet NF-κB activation creates a focal exception — overriding hypoxic TET inhibition at a 403-CpG cluster of proinflammatory enhancers. They argue that HIF1α dominates the *broad* transcriptional reprogramming, but p65 is the *primary driver* of the focal DNA demethylation that anchors the heightened inflammatory program. The non-physical cooperation between HIF1α and p65 (low intensity correlation on cobound peaks) is interpreted as a non-stoichiometric coregulation mediated possibly by shared cofactors, sequential recruitment (HIF1α first), or cooperative chromatin opening rather than complex formation. In vivo, the same signature appears in IL4I1⁺ MACs (and IL1B/ISG monocytes) of immune-hot tumors and correlates with better survival — framed as a reversal of the immunosuppressive-TAM paradigm.

### Comparisons with prior literature (made by authors)

- **Thienpont et al. 2016 (ref 26)** — tumor hypoxia causes DNA hypermethylation in tumor cells via TET inhibition. Authors *extend* this: in MACs the same TET inhibition is bypassed for NF-κB targets.
- **Mulder et al. 2021 / MoMac-VERSE (ref 10)** — provides the IL4I1 Mac, IL1B Mo, ISG Mo, TREM2 Mac, FOLR2 Mac definitions; authors map their in vitro mMAC1 onto this atlas.
- **Bain et al. / Cohen et al. (ref 38)** — earlier work where authors showed hypoxia influences MAC differentiation; this paper extends to the activation step.
- **Park et al. (ref 42)** — IL4I1 MACs in colorectal cancer with active efferocytosis; authors integrate with mMAC1 finding.
- **Ginhoux et al. and others (refs 16, 29, 30)** — previous studies treating hypoxia as immunosuppressive in TME; authors *challenge* this paradigm specifically for monocyte-derived MACs at activation.
- **TET2 inhibitor 4-octyl itaconate (ref 40)** — used as positive control; authors confirm the mechanistic dependence.

### Mechanistic hypotheses proposed

- "NF-κB is able to override the effect of hypoxia and enhances TET-mediated demethylation for a specific group of proinflammatory genes" (p.10-11) — focal NF-κB-tethered TET activity hypothesis.
- The non-physical HIF1α-p65 cooperation suggests indirect mechanisms: "cooperation mechanism that is independent of a physical interaction among HIF1α and p65 proteins" (p.7).
- HIF1α priming preceding p65 binding suggests pioneer-like behavior of HIF1α on shared enhancers.

### Caveats and self-criticism

- "Further time-resolved analyses of paired methylome and transcriptome would be required to establish the sequence of events" (p.10).
- The in vitro M-CSF MAC system may not generalize to tissue-resident embryonic MACs.
- Pharmacological dissection (BAY11-7082, PX-478) is not as clean as genetic knockout; off-target effects remain possible.
- "Possible paradoxical role of hypoxia depending on the cellular context (e.g., presence or absence of an inflammatory insult)" (p.8) — the authors explicitly acknowledge the iMAC1 down-regulation paradox.

### Future directions suggested

- Time-resolved methylome+transcriptome to establish sequence of events.
- TET isoform specificity (TET1 vs TET2 vs TET3) at C2 loci.
- Whether GM-CSF-derived or tissue-resident MACs reproduce the C2 hypomethylation under hypoxia.
- Whether mMAC1 ↔ T-cell crosstalk is causally responsible for the BLCA/OC survival benefit.
- Therapeutic exploitation: targeting mMAC1 / IL4I1 MAC as actionable cells for anti-tumor immunity.

## Limitations

- In vitro system uses only M-CSF-derived MACs from peripheral blood monocytes — generalization to GM-CSF, tissue-resident, or embryonic MACs is not tested.
- ChIP-seq for TET1/2/3 is not performed — the link between p65 binding and TET2 recruitment at C2 is inferred from the 4-octyl itaconate phenotype rather than directly shown.
- HIF1α and p65 ChIP-seq are not paired with HIF2α; HIF2α contribution is therefore not assessed.
- DoRothEA TF regulon inference is correlation-based and assumes mostly known regulons — novel context-specific NF-κB targets may be missed.
- In vivo validation is limited to ovarian tumors (sorted) and BLCA TCGA bulk + scRNA-seq; primary sorted IL4I1 MACs from BLCA are not profiled.
- The pharmacological inhibitors are not orthogonally validated by genetic perturbation (TET2 KO, RELA KO).
- The 1% O₂ in vitro hypoxia is a static condition and does not model cyclic hypoxia / H-R cycles seen in vivo.
- Survival correlations are TCGA-derived and lack causal validation; confounding by tumor type, stage, or immune-infiltration baseline is possible.

## Open questions

### Open questions raised by authors

- How is the temporal sequence of HIF1α / p65 binding and DNA demethylation orchestrated mechanistically? (paired time-resolved methylome+transcriptome required)
- Which TET isoform is responsible for C2 demethylation? Is TET2 specifically recruited by p65?
- Does GM-CSF or tissue-resident lineage reproduce the C2 hypomethylation under hypoxia?
- Is the mMAC1 ↔ T-cell crosstalk the *causal* driver of the BLCA/OC survival benefit, or correlational?
- Can mMAC1 / IL4I1 MAC be therapeutically expanded or induced in vivo for anti-tumor immunity?

### Open questions identified during ingest

- What is the HIF1α-p65 cofactor that mediates non-physical cooperation? Candidates: p300/CBP, BRD4, mediator complex, chromatin remodelers.
- Why is iMAC1 (hypoxic unstimulated) p65-bound-gene-down while mMAC1 is p65-bound-gene-up — what's the molecular switch?
- How does NF-κB recruitment of TET2 evade the canonical Fe²⁺/2-OG/O₂ requirement? Is there a hypoxia-resistant TET isoform or post-translational modification?
- How robust is the mMAC1 ↔ IL4I1 mapping to other tumor types (HCC, NSCLC, breast, melanoma) and to chronic non-malignant hypoxia (arthritis, ischemic tissues)?
- Does the C2 hypomethylation persist after re-oxygenation, or is it reversible?
- Does mMAC1 / IL4I1 MAC enhance ICI response (PD-1/PD-L1 blockade) as the OS data and Park 2024 (CRC efferocytosis) collectively suggest?

## My take

This paper is one of the two foundational works of the HypoxiaVERSE thesis (co-first authored by the user, Calafell-Segura) and provides the canonical *mMAC1* concept used downstream throughout this wiki. Several aspects make it especially valuable to the thesis:

1. **Paradigm reversal**: the work explicitly challenges the "hypoxia = TAM immunosuppression" narrative dominant in TME literature (e.g., Bai 2022 review) and provides a clean experimental dissection of *when* hypoxia is suppressive vs immunogenic (resting vs activated). For the HypoxiaVERSE atlas, this means hypoxia is not a single binary axis — the activation state is a critical second axis.
2. **Methodological template**: the integration of EPIC arrays + bulk RNA-seq + ChIP-seq + DoRothEA + pharmacological dissection + in vivo signature projection (MoMac-VERSE) + TCGA survival + scRNA-seq deconvolution + CellChat is a strong methodological template for follow-up work in the thesis (especially the cross-modality validation pattern).
3. **Open mechanistic puzzle (HIF1α-p65 cooperation without complex)**: the non-physical cooperation (r=0.13) is a real mechanistic gap and a candidate research direction — chromatin priming vs cofactor-bridging vs sequential recruitment are all testable. This is a natural experimental follow-up for the thesis (e.g., proximity ligation, co-IP, BioID, or CUT&Tag for chromatin readers).
4. **iMAC1 paradox**: the down-regulation of p65-bound genes in unstimulated hypoxic MACs is mentioned briefly but not dissected — a sub-thesis worth its own treatment.
5. **Therapeutic angle**: the mMAC1/IL4I1 → better OS correlation is striking but causally unproven. Whether mMAC1-promoting interventions improve ICI response is a high-value question.

Caveats worth keeping in mind: TET2 recruitment is inferred not shown; M-CSF/PB-monocyte system may not generalize to tissue-resident MACs; static 1% O₂ may not capture cyclic hypoxia dynamics.

## Related

- [[papers/cross-tissue-single-cell-landscape-human]] — MoMac-VERSE atlas providing IL4I1/TREM2/FOLR2/IL1B Mo/ISG Mo cluster definitions used here as in vivo correlates
- [[papers/pd-l1-expressing-tumor-associated-macrophages]] — Wang 2024 Cell Reports Medicine; parallel paradigm reversal for PD-L1+ TAM immunostimulatory phenotype in human breast cancer (complementary to this paper's hypoxic MAC reversal)
- [[papers/hypoxia-driven-crosstalk-between-tumor-tumor]] — comprehensive review of hypoxia → TAM polarization mechanisms; this paper is one of the rare counterexamples (hypoxia *enhances* MAC immunogenicity)
- [[papers/molecular-landmarks-tumor-hypoxia-across-cancer]] — pan-cancer hypoxia signatures; complementary axis (tumor-cell-intrinsic) to this paper's MAC-centric axis
- [[papers/tissue-resident-macrophages-provide-pro-tumorigenic]] — counterpoint: shows TRMs (not MoDMs) drive immunosuppression in NSCLC; this paper uses MoDMs
- [[papers/physiology-diseases-tissue-resident-macrophages]] — broad TRM review; useful for contextualizing MoDM-derived mMAC1 vs TRM biology
- [[concepts/mmac1-hypoxic-inflammatory-macrophage]] — core concept defined by this paper
- [[concepts/cluster-c2-hypoxia-hypomethylation-signature]] — core methylation signature defined here
- [[concepts/nf-kb-mediated-dna-demethylation-hypoxia]] — core mechanism defined here
- [[concepts/hif1a-nf-kb-cooperative-chromatin-binding]] — chromatin cooperation phenomenon defined here
- [[concepts/il4i1-tumor-associated-macrophage]] — in vivo correlate
- [[concepts/momac-verse-mnp-verse-atlas]] — in vivo reference atlas
- [[concepts/tumor-associated-macrophage-immunosuppression]] — the paradigm this paper challenges
- [[foundations/hif1a]] — central TF
- [[foundations/nf-kb-p65-rela]] — central TF
- [[foundations/tet-mediated-dna-demethylation]] — mechanism foundation
- [[foundations/illumina-methylationepic-array]] — methylation profiling platform
- [[foundations/chip-seq]] — TF binding profiling
- [[foundations/homer-motif-enrichment-analysis]] — motif analysis pipeline
- [[foundations/dorothea-tf-regulon-analysis]] — TF activity inference
- [[foundations/cibersortx-deconvolution]] — bulk RNA-seq deconvolution
- [[foundations/cellchat-cell-cell-communication]] — ligand-receptor inference
- [[foundations/tcga-the-cancer-genome-atlas]] — survival cohort
- [[foundations/px-478-hif1a-inhibitor]] — HIF1α inhibitor used
- [[foundations/lps-toll-like-receptor-signaling]] — activation signal
