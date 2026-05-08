---
# === Identification ===
title: "NF-κB and TET2 promote macrophage reprogramming in hypoxia that overrides the immunosuppressive effects of the tumor microenvironment"
slug: nf-kb-tet2-promote-macrophage-reprogramming
arxiv: ""
doi: "10.1126/sciadv.adq5226"
pmid: ""
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
corresponding_author: "Esteban Ballestar; Carlos de la Calle-Fabregat"

# === Source & metadata ===
source_type: pdf
s2_id: ""
date_added: 2026-05-05
ingested_date: 2026-05-05
ingest_version: 1
last_reviewed: null

# === Classification ===
importance: 4
tier: TIER_1
tags:
  - macrophage
  - hypoxia
  - epigenetics
  - tumor-microenvironment
  - DNA-methylation
  - NF-kB
  - HIF1a
  - TET2
  - immunology
  - cancer
keywords:
  - mMAC1
  - hypoxic inflammatory macrophage
  - NF-κB
  - TET2
  - HIF1α
  - tumor microenvironment
  - cluster C2
  - DNA demethylation
  - IL4I1 macrophage
  - immune infiltration
domain: "immunology / epigenetics / oncology"

# === Biomedical domain ===
tissue:
  - blood
  - bladder
  - ovary
  - in_vitro_only
condition:
  - cancer
  - healthy
disease_specific:
  - bladder_urothelial_carcinoma
  - ovarian_carcinoma
species:
  - human
hypoxia_relevant: true
contains_immune_cells: true
contains_myeloid: true

# === Technique ===
techniques:
  - bulk_RNA-seq
  - ChIP-seq
  - EPIC_array
  - flow_cytometry
  - scRNA-seq_10x
  - Western_blot
  - immunofluorescence
  - ELISA
  - coculture_T_cell_proliferation
  - HOMER_motif
  - DoRothEA
  - GSEA
  - CIBERSORTx
  - CellChat
  - Kaplan_Meier
n_samples: 4
n_cells_total: null
integration_method: ""

# === Biology captured ===
key_cell_types:
  - monocyte
  - macrophage_M-CSF
  - mMAC21
  - mMAC1
  - iMAC21
  - iMAC1
  - IL4I1_macrophage
  - TREM2_macrophage
  - FOLR2_macrophage
  - IL1B_monocyte
  - ISG_monocyte
  - CD8_T_cell
key_markers:
  - HLA-DR
  - CD86
  - CD80
  - CD14
  - CD206
  - CD163
  - IL6
  - TNF
  - IL10
  - IL4I1
  - TREM2
  - FOLR2
key_pathways:
  - NF-kB
  - HIF1a
  - TLR/LPS
  - TET-DNA-demethylation
  - STAT-IFN
  - glycolysis
  - antigen-presentation

# === User project membership ===
projects:
  - hypoxia
  - thesis
priority: core
read_status: deep_read

# === HypoxiaVERSE-specific ===
hypoxiaverse_status: included
exclusion_reason: null
data_availability: "GEO accessions referenced in Supplementary Methods (table S1A-B; S2A-C; S4A-E; S5)"

# === Cross-references ===
code_url: ""
cited_by: []
---

## Problem

Macrophage (MAC) presence in the tumor microenvironment (TME) is largely associated with poor prognosis because TME cues reprogram MACs toward immunosuppressive phenotypes. Hypoxia is a hallmark TME feature commonly framed as immunosuppressive, but the literature reports contradictory effects of hypoxia and HIFs on MAC immune function. The direct causal link between hypoxia, DNA methylation dynamics, and MAC immunogenicity in the TME has been unclear, and TET-mediated demethylation — required for MAC maturation — is itself oxygen-dependent, so the question of how hypoxic MACs reprogram their epigenome remained open.

## Key idea

Hypoxia paradoxically *boosts* MAC immunogenicity rather than suppressing it: under low O₂, NF-κB (p65/RELA) drives a focal, TET-dependent DNA demethylation program at proinflammatory loci that overrides the bulk hypoxic inhibition of TET activity. This NF-κB–driven C2 hypomethylation signature, together with HIF1α-dominated transcriptional reprogramming, defines a hypoxic inflammatory MAC state ("mMAC1") that mirrors in vivo IL4I1 MACs and correlates with better survival in immune-infiltrated bladder and ovarian carcinomas.

## Method

- In vitro differentiation: human peripheral blood monocytes → MACs with M-CSF for 5 days at 21% O₂ (normoxia) or 1% O₂ (hypoxia), ± LPS for 48 h. Four conditions: iMAC21, iMAC1, mMAC21, mMAC1.
- Functional readouts: cytokine ELISA (IL-6, TNF-α, IL-10), surface marker flow cytometry (HLA-DR, CD86, CD80, CD14, CD206, CD163), CD8⁺ T-cell suppression assay.
- DNA methylation: Illumina Infinium MethylationEPIC array; differential methylation analysis → clusters C1 (n=2782 hypomethylated normoxia), C2 (n=403 hypoxia-specific demethylated in mMAC1), C3 (n=903 hypermethylated normoxia).
- Transcriptomics: bulk RNA-seq → expression clusters E1–E4 (3737 DEGs total). DoRothEA TF regulon activity, GSEA, GO enrichment.
- TF chromatin binding: ChIP-seq for HIF1α (clusters H1 hypoxia-only, H2 LPS-only, H3 hypoxia+LPS) and p65 (single P1 cluster, max in mMAC1). HOMER motif analysis.
- Mechanistic perturbations: BAY11-7082 (p65 inhibitor), PX-478 (HIF1α inhibitor), 4-octyl itaconate (TET2 inhibitor) for 3 h before LPS.
- Activator generality: P3C, CpG, polyI:C, TNF-α, IL-1β stimulation; "swap" experiment changing O₂ 2 h before LPS.
- Western blot / immunofluorescence for HIF1α and p65 protein levels and nuclear/cytoplasmic localization.
- In vivo signature mapping: MoMac-VERSE scRNA-seq atlas (10) → identification of IL1B Mo, IL4I1 Mac, ISG Mo as in vivo correlates of mMAC1.
- Clinical correlation: TCGA pan-cancer survival analysis (12 cancers); bladder urothelial carcinoma (BLCA) Kaplan-Meier curves; CIBERSORTx deconvolution; CellChat cell-cell communication on BLCA scRNA-seq.
- Tumor sorting: flow-sorted IL4I1, TREM2, FOLR2 MACs from primary ovarian carcinoma → DNA methylation + bulk RNA-seq.

## Results

- mMAC1 secretes more IL-6 and TNF-α and less IL-10 than mMAC21, expresses higher HLA-DR/CD86/CD80, lower CD14/CD206/CD163, and loses CD8⁺ T-cell-suppressive capacity (Fig. 1B–D).
- DMP cluster C2 (403 CpGs) is hypomethylated specifically in mMAC1 vs. mMAC21 and is highly enriched in NF-κB family motifs (Fig. 1E–F). Demethylated CpGs include IL6 and TNF loci. C2 regions correspond to LPS-induced de novo enhancers gaining H3K4me1 and H3K27ac.
- Bulk RNA-seq cluster E2 (LPS-up genes, especially in mMAC1) is significantly enriched in C2-associated genes (Fisher's exact P = 3.03 × 10⁻⁴⁴, Fig. 2D).
- DoRothEA: HIF1A is the top-ranked regulon in iMAC21 vs iMAC1 but is overtaken by STAT2 and IRF1 in mMAC21 vs mMAC1; the RELA regulon NES rises from 3.8 (resting) to 5 (activated) in hypoxia.
- NF-κB-activating ligands (LPS, P3C, CpG, polyI:C, TNF-α, IL-1β) all induce greater inflammatory expression in hypoxia, indicating NF-κB overactivation (not stimulus-specific) drives the boost (Fig. S2E).
- "Swap" experiment: 2 h of hypoxia before LPS is sufficient to recapitulate canonical hypoxic gene expression (Fig. S2F–G).
- HIF1α protein increases in hypoxia in both cytoplasm and nucleus; p65 increases in cytoplasm in hypoxia and translocates to the nucleus after LPS (Fig. 3A–C).
- ChIP-seq: ~15% of HIF1α H2 peaks overlap with p65 peaks in mMAC1; cobound peaks are enriched in HIF, NF-κB, AP-1, IRF, and ETS motifs (Fig. 4B–C).
- HIF1α and p65 binding intensities at cobound peaks correlate weakly (Pearson r = 0.13, P = 2.5 × 10⁻⁴), arguing for cooperation without physical interaction (Fig. 4F).
- Functional gene-class separation: HIF1α-only peaks → glycolysis genes; p65-only peaks → immune differentiation; cobound peaks → LPS signaling (Fig. 4G).
- C2 demethylated regions are exclusively associated with p65-specific peaks, not HIF1α (Fig. 4I–J).
- Pharmacology: p65 inhibition (BAY11-7082) restores C2 methylation in mMAC1 to mMAC21 levels; HIF1α inhibition does not. TET2 inhibition (4-octyl itaconate) blocks both demethylation and gene expression. p65 inhibition reduces target gene expression (Fig. 4K–L).
- mMAC1 transcriptomic and C2-demethylation signatures are enriched on three MoMac-VERSE clusters: #15 IL1B Mo, #6 IL4I1 Mac, #4 ISG Mo (Fig. 5A–C).
- TCGA: hypoxic MAC signatures (iMAC1, mMAC1, IL4I1) associate with better survival in 7–10/12 cancer types; normoxic signatures (iMAC21, mMAC21, TREM2, FOLR2) associate with worse survival in 6–10/12 (Fig. S5D, Fig. 5D).
- BLCA: low C2 methylation is significantly associated with better overall survival (HR = 1.72, P = 0.00589, Fig. 5E).
- BLCA cell-type deconvolution: mMAC1 percentage is strongly correlated with T-cell percentage (r = 0.74, P = 2.2 × 10⁻⁶⁷); iMAC21 anticorrelates (r = −0.27, P = 5 × 10⁻⁸).
- CellChat mMAC1↔T-cell ligand-receptor pairs: CXCL9:CXCR3, CXCL10:CXCR2 (chemotaxis); ICAM1:SPN (trafficking); HLA-A/B/C/E/F:CD8 (TCR activation); MIF:CD74 + CD44/CXCR4 (costimulation) (Fig. 5H).
- Sorted IL4I1 MACs from primary ovarian tumors recapitulate the C2 demethylation pattern, are most enriched for the p65 motif, and show highest RELA + HIF1A regulon activity, while TREM2/FOLR2 MACs do not (Fig. 5J–L).

## All claims (exhaustive)

- `[c01]` mMAC1 produces more IL-6 and TNF-α than mMAC21 (p.3) "mature hypoxic MACs (mMAC1) produced higher levels of the inflammatory cytokines interleukin-6 (IL-6) and tumor necrosis factor–α (TNF-α)" — confidence: high — type: quantitative — links: [[concepts/mmac1-hypoxic-inflammatory-macrophage]] [[claims/hypoxia-enhances-proinflammatory-cytokine-secretion-macrophages]]
- `[c02]` mMAC1 produces less IL-10 than mMAC21 (p.3) "lower levels of the anti-inflammatory cytokine IL-10 than mature normoxic MACs (mMAC21)" — confidence: high — type: quantitative — links: [[concepts/mmac1-hypoxic-inflammatory-macrophage]]
- `[c03]` mMAC1 expresses higher HLA-DR/CD86/CD80 than mMAC21 (p.3) "mMAC1 expressed higher levels of the major histocompatibility complex (MHC) class II human leukocyte antigen–DR (HLA-DR) and costimulatory proteins CD86 and CD80" — confidence: high — type: correlational — links: [[concepts/mmac1-hypoxic-inflammatory-macrophage]]
- `[c04]` mMAC1 expresses lower CD14/CD206/CD163 than mMAC21 (p.3) "resting/immunoregulatory MAC surface proteins CD14, CD206, and CD163 were decreased in mMAC1" — confidence: high — type: correlational
- `[c05]` Hypoxic MACs lose CD8⁺ T-cell suppressive capacity (p.3) "displayed a decreased capacity to suppress CD8+ T cell proliferation than normoxic cells" — confidence: high — type: methodological — links: [[claims/hypoxia-enhances-proinflammatory-cytokine-secretion-macrophages]]
- `[c06]` Hypoxia partially blocks the bulk DNA demethylation associated with normoxic MAC differentiation (cluster C1, p.4) "hypoxia partially blocks the DNA methylation changes associated with MAC differentiation in normoxic conditions" — confidence: high — type: mechanistic — links: [[claims/hypoxia-inhibits-ap-driven-demethylation-during]]
- `[c07]` Cluster C2 (403 CpGs) is hypomethylated specifically in mMAC1 (p.4) "cluster C2 displayed a marked hypomethylation specifically in mature hypoxic MACs (mMAC1)" — confidence: high — type: quantitative — links: [[concepts/cluster-c2-hypoxia-hypomethylation-signature]] [[claims/c2-cluster-cpg-demethylation-specific-hypoxic]]
- `[c08]` C2 CpGs are enriched in NF-κB family motifs (p.4) "DMPs in cluster C2 displayed hypoxia-associated demethylation specific to activated MACs and were highly enriched in motifs of the NF-κB family" — confidence: high — type: methodological — links: [[concepts/nf-kb-mediated-dna-demethylation-hypoxia]]
- `[c09]` C2 demethylated CpGs include IL6 and TNF loci (p.4) "Specific examples of demethylated CpGs in cluster C2 included those in the loci of genes such as IL6 and TNF" — confidence: high — type: mechanistic
- `[c10]` C2 regions are LPS-induced de novo enhancers (gain H3K4me1 + H3K27ac after activation) (p.4) "cluster C2 regions gain canonical enhancer (H3K4me1) and enhancer activation (H3K27ac) histone marks after activation" — confidence: high — type: mechanistic
- `[c11]` RNA cluster E2 is significantly enriched in C2-associated genes (Fisher's P=3.03×10⁻⁴⁴) (p.5) "Cluster C2-associated genes were specifically enriched within cluster E2, calculated by a Fisher's exact test" — confidence: high — type: quantitative
- `[c12]` DoRothEA: HIF1A is top regulon in iMAC21 vs iMAC1, but STAT2/IRF1 dominate mMAC21 vs mMAC1 (p.6) "HIF1A was overcome by signal transducer and activator of transcription 2 (STAT2) and interferon regulatory factor 1 (IRF1) regulon scores" — confidence: high — type: methodological
- `[c13]` RELA regulon NES rises from 3.8 (resting hypoxia) to 5 (LPS-activated hypoxia) (p.6) "(NES = 3.8 in iMAC21 versus iMAC1; 5 in mMAC21 versus mMAC1)" — confidence: high — type: quantitative
- `[c14]` NF-κB-activating ligands (LPS, P3C, CpG, polyI:C, TNF-α, IL-1β) all increase inflammatory gene expression in hypoxia vs normoxia (p.6) "Stimulation with pathogen-associated molecular pattern (PAMP) LPS, Pam3-Cys (P3C), CpG, poly I:C, and cytokines TNF-α and IL-1β induced increased expression of inflammatory genes in hypoxia" — confidence: high — type: mechanistic
- `[c15]` 2 h of hypoxia before LPS is sufficient to recapitulate canonical hypoxic gene expression (p.6) "swapping MACs from normoxia to hypoxia 2 hours before activation with LPS proved to be sufficient to increase expression equaling canonical hypoxia levels" — confidence: high — type: mechanistic
- `[c16]` HIF1α protein increases in hypoxia in cytoplasm and nucleus; p65 increases in cytoplasm in hypoxia and shifts to nucleus after LPS (p.7) "HIF1α protein was increased in hypoxia both in the cytoplasm and the nucleus, whereas p65 was increased in the cytoplasm in hypoxic conditions and increased in the nuclei after activation" — confidence: high — type: mechanistic
- `[c17]` HIF1α has 3 ChIP-seq peak clusters (H1/H2/H3); p65 has a single P1 cluster maximal in mMAC1 (p.7) "p65 ChIP-seq peaks revealed one single tendency (P1), showing maximum binding strength in mMAC1" — confidence: high — type: methodological
- `[c18]` ~15% of HIF1α H2-cluster peaks overlap with p65 peaks in mMAC1 (p.8) "p65 motif was also significantly enriched in HIF1α cluster H2, which showed the highest overlap with p65 peaks (~15%) in mMAC1" — confidence: high — type: quantitative
- `[c19]` HIF1α/p65 binding correlation at cobound peaks is weak (Pearson r=0.13, P=2.5×10⁻⁴) (p.8) "the intensity of binding of both TFs in mMAC1 common peaks did not show a clear linear correlation (Pearson's r = 0.13)" — confidence: high — type: quantitative — links: [[concepts/hif1a-nf-kb-cooperative-chromatin-binding]] [[claims/hif1a-p65-cooperate-promoter-regions-without]]
- `[c20]` HIF1α-only genes enrich in glycolysis; p65-only in immune differentiation; cobound in LPS signaling (p.8) "HIF1α-only bound genes were mainly associated with categories related to glycolytic metabolism; p65-only bound genes were associated with immune cell differentiation and adhesion, and genes with cobinding peaks were predominantly associated with the LPS-mediated signaling pathway" — confidence: high — type: methodological
- `[c21]` C2 demethylated regions are exclusively associated with p65-specific peaks, not HIF1α (p.8) "C2 regions are exclusively associated with p65-specific peaks" — confidence: high — type: mechanistic — links: [[claims/c2-cluster-cpg-demethylation-specific-hypoxic]]
- `[c22]` BAY11-7082 (p65 inhibitor) restores C2 methylation in mMAC1 to mMAC21 levels; PX-478 (HIF1α inhibitor) does not (p.8) "inhibition of p65 alone (but not of HIF1α alone) was able to hamper DNA demethylation in hypoxia" — confidence: high — type: pharmacological — links: [[claims/p65-inhibition-blocks-hypoxia-specific-demethylation]]
- `[c23]` 4-octyl itaconate (TET2 inhibitor) blocks C2 demethylation and reduces gene expression (p.8) "samples treated with 4-octyl itaconate showed particularly high DNA methylation levels, as well as decreased mRNA expression" — confidence: high — type: pharmacological
- `[c24]` mMAC1 signature is enriched on MoMac-VERSE clusters #15 IL1B Mo, #6 IL4I1 Mac, #4 ISG Mo (p.9) "we identified an enrichment of mMAC1 gene expression signature, as well as mMAC1-specific DNA demethylation signature (C2-associated genes) on three tissue MO/MAC populations" — confidence: high — type: methodological — links: [[claims/il4i1-macrophages-vivo-correlates-mmac1]]
- `[c25]` High mMAC1 signature associates with better survival in 10/12 TCGA cancer types; mMAC21 with worse in 10/12 (p.10) "patients with high signatures/scores ... of hypoxic MAC signatures (iMAC1 and mMAC1) generally displayed a better overall survival in several different cancer types (10 of 12 cases)" — confidence: high — type: correlational — links: [[claims/mmac1-signature-correlates-better-cancer-survival]]
- `[c26]` TREM2 MAC signature: poor prognosis in 7/12; FOLR2 in 6/12 (p.10) "the TREM2 MAC signature displayed the highest association with a poor prognosis, showing decreased survival in 7 of 12 cancer type series followed by FOLR2 MACs, with 6 of 12" — confidence: medium — type: correlational — links: [[claims/trem2-macrophages-associate-poor-cancer-prognosis]]
- `[c27]` BLCA: low C2 methylation associates with better survival (HR=1.72, P=0.00589) (p.10) "patients with low methylation levels in C2 CpGs displayed a significantly higher survival" — confidence: high — type: quantitative
- `[c28]` BLCA: mMAC1 % strongly correlates with T-cell % (r=0.74, P=2.2×10⁻⁶⁷); iMAC21 anticorrelates (r=−0.27, P=5×10⁻⁸) (p.10) "T cell percentage was significantly correlated with mMAC1 (r = 0.74, P = 2.2·10⁻⁶⁷) and ... anticorrelated with iMAC21 (r = −0.27, P = 5·10⁻⁸)" — confidence: high — type: quantitative — links: [[claims/mmac1-chemoattracts-cells-cxcl9-cxcl10]]
- `[c29]` CellChat mMAC1↔T-cell pairs include CXCL9:CXCR3, CXCL10:CXCR2, ICAM1:SPN, HLA-A/B/C/E/F:CD8, MIF:CD74+CD44/CXCR4 (p.10) "Cell-cell communication analysis revealed several significant ligand-receptor pairs between mMAC1 and T cells" — confidence: high — type: methodological
- `[c30]` Sorted IL4I1 OC MACs have lowest C2 methylation; p65 most enriched motif; highest RELA/HIF1A regulon (p.11) "the IL4I1 population showed the lowest average methylation levels ... p65 was the most enriched motif in the demethylated CpGs associated specifically with IL4I1" — confidence: high — type: methodological — links: [[claims/il4i1-macrophages-vivo-correlates-mmac1]]

## Discussion captured

### Authors' interpretation

- Hypoxia *boosts* MAC immunogenicity rather than acting purely as an immunosuppressive cue, contradicting the dominant TME framing.
- The mechanism is a paradoxical NF-κB-driven, TET-dependent focal demethylation that *overrides* the global hypoxic inhibition of TET activity at a small set of proinflammatory loci (cluster C2).
- HIF1α and p65 cooperate without physical interaction (low correlation of binding intensities at cobound peaks), suggesting a cooperative regulatory grammar rather than a complex.
- mMAC1 corresponds in vivo to IL4I1 MACs (and to a lesser extent IL1B Mo and ISG Mo), and these populations are associated with improved cancer outcomes via T-cell recruitment and activation.

### Comparisons with prior literature (made by authors)

- Authors cite (26) [Thienpont et al. 2016, *Nature*] for the prior finding that tumor hypoxia causes DNA hypermethylation by reducing TET activity. Their cluster C1 result *agrees* with that observation, but their cluster C2 result *qualifies* it: NF-κB can override hypoxic TET inhibition at proinflammatory loci.
- They cite (10) [Mulder et al. 2021, *Immunity*, MoMac-VERSE] as the human MO/MAC reference atlas used to project their in vitro signatures.
- They cite (42) for the recent observation that IL4I1 MACs perform efferocytosis and predispose to immune-checkpoint-inhibitor response, matching their own prognostic finding.
- They cite (43) on TREM2⁺ MACs as immunosuppressors, consistent with their poor-prognosis finding for TREM2.
- They cite (40) for 4-octyl itaconate as a strong TET2 inhibitor, used as a positive control.
- They cite (15, 38, 52, 53) to highlight that "proposed effects of hypoxia and HIFs on MAC function are highly contradictory," motivating the work.

### Mechanistic hypotheses proposed

- "NF-κB is able to override the effect of hypoxia and enhances TET-mediated demethylation for a specific group of proinflammatory genes" (p.11).
- "p65 and HIF1α common peaks ... a cooperation mechanism that is independent of a physical interaction among HIF1α and p65 proteins" (p.8).
- mMAC1 → T-cell crosstalk through CXCL9/10, ICAM1, HLA-class-I and MIF interactions explains the observed correlation between mMAC1 abundance and T-cell infiltration in BLCA.

### Caveats and self-criticism

- "to interrogate the gene regulatory role of DNA methylation, further time-resolved analyses of paired methylome and transcriptome would be required to establish the sequence of events" (p.11) — the directionality DNA-methylation ↔ transcription is not formally resolved.
- iMAC1 (resting hypoxic) shows down-regulation of p65-bound genes, which the authors interpret as possibly reflecting an "incomplete differentiation process in hypoxic conditions" — a caveat for the broader claim that hypoxia is universally pro-immunogenic.
- The authors note the contradictory literature on hypoxia/HIFs in MACs (15, 38, 52, 53) and frame their own conclusions as context-dependent (presence/absence of inflammatory insult).

### Future directions suggested

- Time-resolved paired methylome + transcriptome to nail down causal sequence at C2 loci.
- Therapeutic implication: hypoxic inflammatory MACs are "actionable target cells to modulate anticancer immune responses" (Abstract / Discussion).
- Generalization across other hypoxic pathologies (arthritic joints, ischemic tissues) is implicit but not tested.

## Limitations

- In vitro M-CSF-derived MACs from peripheral blood monocytes — does not capture tissue-resident embryonic-origin MACs or the full complexity of TME signals.
- Hypoxia is modeled as a binary 21% vs 1% O₂ exposure; intermediate or fluctuating oxygen tensions (more physiological in tumors) are not addressed.
- Cluster C2 contains only 403 CpGs — a small fraction of the methylome; the authors do not formally exclude TET1 or TET3 contributions vs TET2.
- No genetic loss-of-function for TET2 (only chemical inhibition with 4-octyl itaconate, which has off-target effects on inflammasome/IRG1).
- TCGA bulk-deconvolution-based survival association is correlational, not causal.
- CellChat ligand-receptor inferences are predictions from gene expression, not validated protein interactions.

## Open questions

### Open questions raised by authors

- What is the precise temporal sequence of NF-κB binding, TET recruitment, and demethylation at C2 loci?
- Why is HIF1α inhibition only partially effective at reducing inflammatory gene expression while not affecting C2 demethylation? Are there HIF1α-independent transcriptional layers?
- Does the paradoxical "incomplete differentiation" pattern of iMAC1 (down-regulation of p65-bound genes) generalize to other hypoxic non-inflammatory contexts?

### Open questions identified during ingest

- TET2 vs TET1/TET3 specificity at C2 loci is not resolved by chemical TET inhibition alone — a TET-isoform-specific genetic perturbation experiment would close this.
- Does the same NF-κB-driven C2 demethylation occur in tissue-resident or embryonic-origin MACs, or is it specific to monocyte-derived M-CSF MACs?
- Is the mMAC1 ↔ T-cell crosstalk causally responsible for the survival benefit in BLCA, or merely a co-occurring marker of immune-hot tumors?
- How does mMAC1 relate to the trained-immunity literature, given the persistent epigenetic remodeling observed?

## My take

This is a mechanistically rich paper that resolves a genuine paradox in the field: how can MACs in hypoxic tumors maintain inflammatory output if TETs require oxygen? The C2-cluster identification + p65-driven focal demethylation + clinical mapping to IL4I1 MACs forms a coherent story across in vitro, in vivo, and TCGA layers. The strongest result is the orthogonal pharmacological confirmation (BAY vs PX-478 vs 4-octyl itaconate), which cleanly separates p65-dependent demethylation from HIF1α-dependent transcription. The weakest link is the absence of TET-isoform-specific genetic perturbation. Highly relevant for the HypoxiaVERSE thesis project.

## Related

- Concepts: [[concepts/mmac1-hypoxic-inflammatory-macrophage]], [[concepts/nf-kb-mediated-dna-demethylation-hypoxia]], [[concepts/hif1a-nf-kb-cooperative-chromatin-binding]], [[concepts/cluster-c2-hypoxia-hypomethylation-signature]], [[concepts/tumor-associated-macrophage-immunosuppression]]
- Foundations (biological): [[foundations/hif1a]], [[foundations/nf-kb-p65-rela]], [[foundations/tet-mediated-dna-demethylation]], [[foundations/lps-toll-like-receptor-signaling]]
- Foundations (methods): [[foundations/dorothea-tf-regulon-analysis]], [[foundations/homer-motif-enrichment-analysis]], [[foundations/illumina-methylationepic-array]], [[foundations/chip-seq]], [[foundations/cibersortx-deconvolution]], [[foundations/cellchat-cell-cell-communication]]
- Claims: [[claims/hypoxia-boosts-macrophage-immunogenicity-nf-kb]], [[claims/c2-cluster-cpg-demethylation-specific-hypoxic]], [[claims/p65-inhibition-blocks-hypoxia-specific-demethylation]], [[claims/hif1a-p65-cooperate-promoter-regions-without]], [[claims/mmac1-signature-correlates-better-cancer-survival]], [[claims/trem2-macrophages-associate-poor-cancer-prognosis]], [[claims/il4i1-macrophages-vivo-correlates-mmac1]], [[claims/mmac1-chemoattracts-cells-cxcl9-cxcl10]], [[claims/hypoxia-inhibits-ap-driven-demethylation-during]], [[claims/hypoxia-enhances-proinflammatory-cytokine-secretion-macrophages]]
- People: [[people/carlos-de-la-calle-fabregat]], [[people/josep-calafell-segura]], [[people/esteban-ballestar]], [[people/florent-ginhoux]]
