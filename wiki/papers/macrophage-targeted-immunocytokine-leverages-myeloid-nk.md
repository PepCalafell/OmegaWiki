---
title: "Macrophage-targeted immunocytokine leverages myeloid, T, and NK cell synergy for cancer immunotherapy"
slug: macrophage-targeted-immunocytokine-leverages-myeloid-nk
arxiv: ""
doi: "10.1016/j.cell.2025.10.030"
pmid: ""
venue: "Cell"
year: 2025
authors:
  - "Michelle von Locquenghien"
  - "Pascale Zwicky"
  - "Ken Xie"
  - "Diego Adhemar Jaitin"
  - "Fadi Sheban"
  - "Adam Yalin"
  - "Florian Uhlitz"
  - "Chamutal Gur"
  - "Reut Sharet Eshed"
  - "Eyal David"
  - "Kfir Mazuz"
  - "Caroline Jennings Marin"
  - "Ankita Sankar"
  - "Devin Mediratta"
  - "Roberto Avellino"
  - "Assaf Weiner"
  - "Ido Amit"
first_author: "Michelle von Locquenghien"
corresponding_author: "Ido Amit"
source_type: pdf
s2_id: ""
date_added: 2026-05-27
ingested_date: 2026-05-27
ingest_version: 1
last_reviewed:
importance: 4
tier: TIER_1
tags:
  - TREM2
  - immunocytokine
  - MiTE
  - IL-2
  - IL-2-superkine
  - MMP14
  - tumor-associated-macrophage
  - protease-activated-prodrug
  - cancer-immunotherapy
  - PD-1
  - CTLA-4
  - patient-derived-tumor-fragment
  - RCC
  - scRNA-seq
  - CITE-seq
  - MERFISH
  - NK-cell
  - CD8-T-cell
keywords:
  - MiTE-144
  - αTREM2-IL-2SK
  - IL-2 superkine
  - MMP14-cleavable linker
  - SGRSENIRTA
  - hTREM2 mice
  - MC38
  - MCA205
  - patient-derived tumor fragment
  - PDTF
  - renal cell carcinoma
  - MrVI
  - Hotspot
  - MultiNicheNetR
  - ResolVI
  - totalVI
domain: immunology
tissue:
  - bone_marrow
  - blood
  - kidney
  - lung
  - colon
  - breast
  - ovary
  - multi
condition:
  - cancer
disease_specific:
  - renal_cell_carcinoma
  - colorectal_cancer
  - lung_cancer
  - breast_cancer
  - ovarian_cancer
species:
  - human
  - mouse
hypoxia_relevant: true
contains_immune_cells: true
contains_myeloid: true
techniques:
  - scRNA-seq_10x
  - CITE-seq
  - spatial_MERFISH
  - bulk_RNA-seq
  - flow_cytometry
  - SPR
  - ELISA
  - SDS-PAGE
  - immunofluorescence
  - in_vivo_efficacy_syngeneic
  - patient_derived_tumor_fragment_ex_vivo
  - HEK-Blue_reporter
  - pharmacokinetics_biodistribution
n_samples:
n_cells_total: 2189317
integration_method: "scVI / totalVI / MrVI"
key_cell_types:
  - tumor-associated macrophage (TAM, including hypoxic / IFN-response / C1q / antigen-presenting / proliferating)
  - moMAC
  - dendritic cell (cDC1, migratory DC, moDC)
  - CD8 T cell (effector, stem-like, proliferating, exhausted)
  - CD4 T cell
  - regulatory T cell (Treg)
  - NK cell (early, intermediate, late, proliferating, mature)
  - granulocyte / neutrophil
  - cancer-associated fibroblast
key_markers:
  - TREM2
  - MMP14
  - IL-2
  - IL-2Rβ (CD122)
  - IL-2Rα (CD25)
  - PD-1 (PDCD1)
  - CTLA-4
  - PD-L1 (CD274)
  - CD80
  - CD86
  - CXCL9
  - SPP1
  - C1QC
  - CD163
  - MRC1
  - CIITA
  - HLA-DRA
  - FOXP3
  - GZMA
  - GZMB
  - PRF1
  - TCF7
  - TOX
  - MKI67
  - ARG1
  - NOS2
  - HMOX1
  - S100A8
  - S100A9
  - LGALS1
  - IFIT1
  - IFIT2
  - IFIT3
key_pathways:
  - TREM2-DAP12 myeloid checkpoint
  - IL-2 / IL-2R cytokine signaling
  - MMP14-mediated ECM/protease activity
  - PD-1 / CTLA-4 immune checkpoint
  - TAM-T cell ligand-receptor circuitry
  - MHC class I antigen presentation
  - cDC1 development (Irf1/Id2/Irf8/Nfil3)
  - NK / CD8 cytotoxic effector programmes (perforin, granzymes)
projects:
  - thesis
priority: core
read_status: deep_read
hypoxiaverse_status: candidate
exclusion_reason:
data_availability: "scRNA-seq data deposited per Cell paper data policy (see Methods / Data availability section)"
code_url: ""
cited_by: []
---

## Problem

Cancer immunotherapy has been transformed by checkpoint blockade (ICIs) and antibody-cytokine fusions (ICKs), yet large fractions of patients remain refractory because of the immunosuppressive tumor microenvironment dominated by tumor-associated macrophages (TAMs) — particularly TREM2⁺ TAMs. Three concrete bottlenecks limit current approaches: (1) systemic toxicity from non-specific cytokine activity (notably IL-2); (2) limited durability against the TME's macrophage-driven suppression; (3) reliance on T-cell-only immunity, which is bypassed by MHC class I downregulation. Anti-TREM2 monotherapies reprogram TAMs but show only minor anti-tumor benefit, and conventional IL-2 immunocytokines drive lethal cytokine-storm toxicity at therapeutic doses.

## Key idea

A new class of "myeloid-targeted immunocytokines and natural killer/T cell enhancers" (MiTEs): a single trans-acting molecule that links an antagonistic anti-TREM2 antibody (Fc-Null IgG1) to an IL-2 superkine (H9 SK, IL-2Rβ-biased) masked by an extracellular IL-2Rβ blocking domain joined via an MMP14-selective cleavage peptide (SGRSENIRTA). The construct is biologically inert in circulation. Within the TME, TAM-restricted MMP14 cleaves the linker, releasing active IL-2 superkine in trans onto neighbouring T and NK cells while the anti-TREM2 arm reprograms macrophages locally. Lead candidate: MiTE-144 (single mask, single cleavage site, low background).

## Method

- **Spatial pan-cancer atlas.** ~1.86 M-cell MERFISH analysis of breast, lung, colorectal, ovarian human tumors with ResolVI transcript-assignment correction; empirical CDFs of immune cell minimum distances.
- **Pan-cancer molecular interactions.** Integrated 332,723-cell scRNA-seq (123 tumors / 67 adjacent-healthy) with scVI integration and MultiNicheNetR for tumor-vs-adjacent ligand-receptor differential analysis; additional ~13.8 M-cell pan-immune atlas for protease specificity.
- **Molecule engineering.** αTREM2 antibody selection against human TREM2 in hTREM2 humanised mice; HEK-Blue CD122/CD132 reporter, SPR, ELISA, FACS for binding/bioactivity; SDS-PAGE for cleavage kinetics; substrate specificity screen (Aronson et al.) selected SGRSENIRTA linker.
- **Toxicity / efficacy.** Naive and MC38- / MCA205-bearing C57BL/6 or hTREM2 mice; pharmacokinetics, biodistribution, body weight, serum cytokines (IFN-γ, IL-2, IL-6), ALT/AST, spleen weight, histopathology of liver and lungs; tumor volume, weight; combination with αPD-1 and αCTLA-4.
- **Single-cell readouts.** 45,505 immune cells from 45 MC38 hTREM2 mice across 9 treatment arms; MrVI for treatment-aware distance networks; Hotspot for module discovery; DEG analysis (padj<0.05, |logFC|>1).
- **Ex vivo human validation.** Five RCC patient-derived tumor fragments (PDTFs) treated 48 h with IgG / MiTE-144 / αPD-1 / MiTE-144+αPD-1; CITE-seq with 146-marker panel on 93,087 cells; totalVI integration; cross-species transcriptional comparison.

## Results

- TAMs are the closest immune neighbours of T cells across human tumor types (MERFISH 1.86 M cells); supporting integrated scRNA-seq shows TAM-T cell L-R network is the densest immune-pair circuitry and is enriched in TME vs adjacent-healthy.
- TREM2 is significantly enriched in tumor tissue across 14 TCGA cancer types (>10,000 patients). Antagonistic αTREM2 monotherapy reprograms TAMs molecularly (Mmp12↓, Spp1↓, Siglec1/Trem1/Ifit2 preserved) but shows only minor MC38 tumor control.
- Unmasked αTREM2-IL-2 superkine ICKs administered systemically caused lethal cytokine-storm toxicity (IFN-γ, IL-2, IL-6 ↑↑) and hepatotoxicity (ALT/AST ↑↑); two 100 μg doses killed all treated mice.
- MMP14 is TAM-specifically expressed among immune cells (PBMC atlas, healthy tissues, tumor-adjacent, tumors comparison) and strongly co-expressed with TREM2 in tumor TAMs (weighted co-expression; lung tumor immunofluorescence). CAFs also express MMP14 but lack TREM2.
- The SGRSENIRTA linker is selectively cleaved by MMP14 (vs MMP3/7/10/11). Cleaved MiTE constructs bind IL-2Rβ with KD ~ 1-15 nM (vs WT IL-2 280 nM). Intact MiTEs show ~3-log lower IL-2 bioactivity; MMP14 cleavage restores activity. MiTE-144 (lowest background among variants) was selected as lead.
- MiTE-144 at 200 μg i.v. repeated showed no detectable systemic toxicity (stable weight, normal IFN-γ/IL-2/IL-6, normal ALT/AST, no splenomegaly, no liver/lung inflammation); preferential tumor accumulation; t½ = 11.88 h (vs αTREM2-IL-2SK 9.43 h).
- MiTE-144 monotherapy almost completely abrogated MC38 tumor growth, outperforming αTREM2, αPD-1, αCTLA-4, and αTREM2+ICI combinations. Replicated in MCA205. MiTE-144 + αCTLA-4 eradicated MC38 tumors in 6/7 mice.
- TME reprogramming (45,505-cell scRNA-seq, 9 arms): MiTE-144 treatments formed a transcriptionally distinct cluster (MrVI), with TAM shift away from TREM2/MMP14 and IFN-response toward inflammatory monocyte-like (S100a8, Hp, Ly6i) and hypoxia-associated (Arg1, Nos2, Hmox1) modules; DCs gained MHC-I and cDC1 programmes; NK cells gained cytotoxic and proliferative phenotypes while shedding early-exhaustion markers; CD8 T cells gained cytotoxic, proliferative and stem-like (Tcf7) programmes while losing Tox; MiTE-144 disrupted conserved TAM-T cell suppressive L-R axes (Cd86-Ctla4, Pdcd1-Cd48, Tgfbr1-Tgfb1, Lgals1-Cd69, etc.). Treg expansion (modest in TME, marked in tdLNs) was abrogated by αCTLA-4 combination.
- Translational validation (5 RCC PDTFs, 146-marker CITE-seq, 93,087 cells, totalVI): MiTE-144 expanded CD8 cycling/memory and intermediate NK cells without expanding Tregs or hypoxic TAMs; induced conserved cytotoxic program (PRF1, GZMA/B/H, MCM3/4) and downregulated exhaustion-associated genes (CXCR4, DUSP1, TNFAIP3); CITE-seq protein: CD25/CD69/NKG2D ↑; PD-1/LAG-3 mildly ↑ but reduced under αPD-1 combination — supporting synergy with checkpoint blockade. Cross-species transcriptomic comparison shows conserved immunostimulation between mouse and human.

## All claims (exhaustive)

- `[c01]` TAMs are predominant immune neighbours of T cells across major human cancers (p.7099-7100) "TAMs are the predominant immune population in close spatial proximity to T cells within the TME" — confidence: high — type: correlational — links: [[concepts/tam-t-cell-spatial-proximity-tme]] [[foundations/merfish-imaging-spatial]] [[foundations/resolvi-spatial-transcript-correction]] [[claims/tams-predominant-spatial-proximity-t-cells-pan-cancer]]
- `[c02]` TAM-T cell ligand-receptor circuitry is the densest immune-cell-pair network and is enriched in TME (p.7100) "we observed predominant interaction circuitry between TAMs and T cells… all significantly upregulated in the TME" — confidence: high — type: methodological — links: [[concepts/tam-t-cell-spatial-proximity-tme]] [[foundations/multinichenetr-cell-cell-comm]] [[claims/tam-t-cell-ligand-receptor-network-enriched-tme]]
- `[c03]` TREM2 is significantly enriched in tumors vs healthy tissue across 14 TCGA cancer types (p.7101) "TREM2 is a tumor-enriched target highly upregulated in the TME compared to healthy tissues" — confidence: high — type: correlational — links: [[foundations/trem2-receptor]] [[foundations/tcga-the-cancer-genome-atlas]] [[claims/trem2-enriched-in-tumors-vs-healthy-tcga]]
- `[c04]` Anti-TREM2 monotherapy reprograms TAMs but shows only minor anti-tumor efficacy in MC38 (p.7102) "treatment of mice with MC38 tumors showed limited efficacy, as assessed by tumor volume and weight" — confidence: high — type: pharmacological — links: [[foundations/trem2-receptor]] [[concepts/myeloid-targeted-immunocytokine-mite]] [[claims/anti-trem2-monotherapy-reprograms-tams-limited-efficacy]]
- `[c05]` Unmasked αTREM2-IL-2 superkine ICK is lethally toxic systemically (IFN-γ/IL-2/IL-6 storm, ALT/AST hepatotoxicity) (p.7102) "two doses of 100 μg of either αTREM2-IL-2SK or control αRSV-IL-2SK resulted in mortality (n = 7/group)" — confidence: high — type: pharmacological — links: [[foundations/il-2-cytokine]] [[concepts/mmp14-protease-activated-il2-prodrug]] [[claims/anti-trem2-il-2sk-ick-induces-lethal-systemic-toxicity]]
- `[c06]` MMP14 is TAM-specifically expressed among tumor immune cells (p.7103) "MMP14 stood out due to its high, TAM-specific expression and minimal background activity in other immune cells" — confidence: high — type: correlational — links: [[foundations/mmp14-matrix-metalloproteinase]] [[concepts/mmp14-trem2-tam-marker-pair]] [[claims/mmp14-tam-specific-protease-immune-cells]]
- `[c07]` MMP14 and TREM2 are strongly co-expressed in tumor TAMs and co-localized in tumor tissue but not adjacent-healthy (p.7103) "Weighted co-expression analysis revealed a strong correlation between MMP14 and TREM2 in both human and murine tumors" — confidence: high — type: correlational — links: [[concepts/mmp14-trem2-tam-marker-pair]] [[claims/mmp14-trem2-coexpression-tumor-tissue-specific]]
- `[c08]` The SGRSENIRTA linker is selectively cleaved by MMP14 vs MMP3/7/10/11 (p.7103) "MMP14 induced robust, time-dependent cleavage, whereas the other MMPs exhibited little to no activity or residual non-specific digestion" — confidence: high — type: methodological — links: [[foundations/mmp14-matrix-metalloproteinase]] [[concepts/mmp14-protease-activated-il2-prodrug]] [[claims/sgrsenirta-linker-mmp14-selective-cleavage]]
- `[c09]` Cleaved MiTE IL-2 superkine domains bind IL-2Rβ with ~100-270-fold higher affinity than WT IL-2 (KD 1.26 nM-14.52 nM vs 280 nM) (p.7103) "KD = 1.26 × 10⁻⁹ M (MiTE-76)… compared to WT IL-2 (KD = 2.80 × 10⁻⁷ M)" — confidence: high — type: quantitative — links: [[foundations/il-2-cytokine]] [[concepts/myeloid-targeted-immunocytokine-mite]] [[claims/cleaved-mites-270-fold-higher-il2rb-affinity-vs-wt-il2]]
- `[c10]` Intact masked MiTEs show ~3-log lower IL-2 bioactivity than αTREM2-IL-2SK; MMP14 cleavage restores it (p.7103) "showing up to a 3-log reduction in IL-2SK activity in intact MiTEs and full restoration after MMP14 cleavage" — confidence: high — type: quantitative — links: [[concepts/mmp14-protease-activated-il2-prodrug]] [[claims/masked-mites-3log-il2-bioactivity-reduction]]
- `[c11]` MiTE-144 at 200 μg i.v. repeated dosing produces no detectable systemic toxicity (p.7105) "MiTE-144 induced no systemic inflammation or hepatotoxicity, as indicated by stable body weight, unaltered cytokine, and ALT/AST enzyme levels" — confidence: high — type: pharmacological — links: [[concepts/myeloid-targeted-immunocytokine-mite]] [[claims/mite144-no-systemic-toxicity-repeated-iv-dosing]]
- `[c12]` MiTE-144 has preferential tumor accumulation and extended t½ (11.88 h vs 9.43 h for αTREM2-IL-2SK) (p.7105) "MiTE-144 displayed a slower elimination rate and extended half-life (11.88 h) compared with αTREM2-IL-2SK (9.43 h)" — confidence: high — type: quantitative — links: [[concepts/myeloid-targeted-immunocytokine-mite]] [[claims/mite144-preferential-tumor-accumulation-extended-half-life]]
- `[c13]` MiTE-144 outperforms αTREM2, αPD-1, αCTLA-4 monotherapies (and αTREM2+ICI combinations) in MC38; replicated in MCA205 (p.7105) "MiTE-144 outperformed multiple ICI monotherapies, including αTREM2, αPD-1, and αCTLA-4" — confidence: high — type: pharmacological — links: [[concepts/myeloid-targeted-immunocytokine-mite]] [[foundations/mc38-syngeneic-tumor-model]] [[foundations/pd-1-receptor-pdcd1]] [[foundations/ctla-4-checkpoint]] [[claims/mite144-superior-tumor-control-vs-ici-monotherapies-mc38]]
- `[c14]` MiTE-144 + αCTLA-4 eradicates MC38 tumors in 6/7 mice (p.7105) "leading to complete eradication of tumors in 6 out of 7 mice" — confidence: high — type: quantitative — links: [[concepts/myeloid-targeted-immunocytokine-mite]] [[foundations/ctla-4-checkpoint]] [[claims/mite144-ctla4-combo-eradicates-mc38-6-of-7-mice]]
- `[c15]` MiTE-144 reprograms TAMs away from TREM2/MMP14 and IFN-response toward inflammatory monocyte-like and hypoxia-associated states (p.7107-7108) "MiTE-144 upregulated inflammatory, monocyte-like modules (S100a8, Hp, and Ly6i) and hypoxia-associated modules (Arg1, Nos2, and Hmox1), while strongly reducing IFN-response genes" — confidence: medium — type: mechanistic — links: [[concepts/myeloid-targeted-immunocytokine-mite]] [[foundations/hif1a]] [[foundations/mrvi-multi-resolution-variational-inference]] [[foundations/hotspot-gene-module-analysis]] [[claims/mite144-reprograms-tams-toward-inflammatory-hypoxia-states]]
- `[c16]` MiTE-144 induces MHC class I antigen-presentation and cDC1 programmes in DCs (p.7108) "MiTE-144-based treatments induced genes associated with MHC class I antigen presentation (e.g., H2-Q5, H2-Q6, H2-Q7, and H2-K1) and development of cDC1s (e.g., Irf1, Id2, Irf8, and Nfil3)" — confidence: medium — type: mechanistic — links: [[concepts/myeloid-targeted-immunocytokine-mite]] [[claims/mite144-induces-mhc-i-and-cdc1-programs-in-dcs]]
- `[c17]` MiTE-144 activates NK cells (Prf1, Mki67↑; Cd27, Tigit, Tnfrsf18↓) and increases NK counts in TME and tdLNs (p.7108-7109) "the upregulation of late and activation (Klrg1 and Ctla4), cytotoxic (Prf1), and proliferation genes (Mki67, Mcm3, McM4)" — confidence: high — type: mechanistic — links: [[concepts/myeloid-targeted-immunocytokine-mite]] [[foundations/il-2-cytokine]] [[claims/mite144-activates-nk-cytotoxic-proliferation-reduces-exhaustion]]
- `[c18]` MiTE-144 upregulates CD8 T cytotoxic / proliferation / stemness programs (Gzma, Mki67, Tcf7↑) while downregulating Tox; amplified by αCTLA-4 (p.7109) "MiTE-144 promoted the upregulation of cytotoxic, proliferation, and stemness-associated genes (e.g., Gzma, Mki67, and Tcf7)" — confidence: high — type: mechanistic — links: [[concepts/myeloid-targeted-immunocytokine-mite]] [[foundations/ctla-4-checkpoint]] [[claims/mite144-cd8-cytotoxic-proliferation-stemness-reduces-exhaustion]]
- `[c19]` MiTE-144 mildly expands Tregs in TME and markedly in tdLNs; αCTLA-4 combination abrogates Treg expansion (p.7109) "MiTE-144 treatments slightly increased Treg frequencies in the TME and markedly in the tdLNs. However, this effect was effectively abrogated by combining αCTLA-4 treatment with MiTE-144" — confidence: medium — type: pharmacological — links: [[concepts/myeloid-targeted-immunocytokine-mite]] [[foundations/ctla-4-checkpoint]] [[claims/mite144-treg-expansion-blocked-by-ctla4-combo]]
- `[c20]` MiTE-144 disrupts conserved suppressive TAM–T cell L-R axes (Cd86-Ctla4, Pdcd1-Cd48, Ccr8-Ccl3, Lgals1-Cd69, Tgfbr1-Tgfb1) between mouse and human (p.7109-7110) "MiTEs and their combinatorial treatments with αPD-1 or αCTLA-4 disrupt multiple TAM-T cell immunosuppressive interaction axes" — confidence: medium — type: mechanistic — links: [[concepts/tam-t-cell-spatial-proximity-tme]] [[concepts/myeloid-targeted-immunocytokine-mite]] [[claims/mite144-disrupts-conserved-suppressive-tam-t-cell-lr-axes]]
- `[c21]` MiTE-144 ex vivo on RCC PDTFs expands CD8 cycling/memory T and intermediate NK without expanding Tregs or hypoxic TAMs (p.7111) "consistent expansion of CD8+ cycling and memory T cells, as well as intermediate-stage NK cells… Tregs and hypoxic TAMs remained unchanged or were reduced" — confidence: medium — type: pharmacological — links: [[concepts/myeloid-targeted-immunocytokine-mite]] [[concepts/tumour-explant-short-term-culture]] [[foundations/cite-seq-citeseq]] [[foundations/totalvi-cite-seq-modeling]] [[claims/mite144-rcc-pdtf-expands-effector-not-treg]]
- `[c22]` In human PDTFs, MiTE-144 induces conserved cytotoxic program (PRF1, GZMA/B/H, MCM3/4/6, CCND2↑; CXCR4, DUSP1, TNFAIP3, TOX↓) in T and NK cells (p.7111-7112) "robust upregulation of cytolytic effector genes, including PRF1, GZMA, and GZMB" — confidence: medium — type: mechanistic — links: [[concepts/myeloid-targeted-immunocytokine-mite]] [[foundations/cite-seq-citeseq]] [[claims/mite144-conserved-cytotoxic-program-human-t-and-nk]]
- `[c23]` MiTE-144 elicits conserved immunostimulation between mouse and human tumor immune responses (p.7112) "Cross-species global molecular comparisons with our murine treatment data revealed a conserved immunostimulatory response between human and mouse immune programs" — confidence: medium — type: correlational — links: [[concepts/myeloid-targeted-immunocytokine-mite]] [[claims/mite144-cross-species-conserved-immunostimulation-mouse-human]]
- `[c24]` The IL-2 superkine (H9 SK, IL-2Rβ-biased) is designed to expand effector T cells over Tregs but the bias is incomplete in vivo (p.7102, 7109) "synthetic IL-2 variant ('superkine' SK), engineered to exhibit increased affinity to IL-2Rβ, thereby preferentially expanding effector T cells over Tregs" — confidence: medium — type: pharmacological — links: [[foundations/il-2-cytokine]] [[concepts/myeloid-targeted-immunocytokine-mite]] [[claims/il2-superkine-h9-il2rb-bias-effector-over-treg]]
- `[c25]` Effective MiTE-144 therapy co-induces TAM inflammatory-monocyte-like AND hypoxia modules — a state that challenges the canonical hypoxic-TAM-is-suppressive framing (p.7107-7108) "MiTE-144 upregulated inflammatory, monocyte-like modules… and hypoxia-associated modules" — confidence: medium — type: mechanistic — links: [[concepts/myeloid-targeted-immunocytokine-mite]] [[foundations/hif1a]] [[foundations/hif2a]] [[claims/mite144-disturbs-canonical-m1-m2-axis-coexpressing-inflammatory-hypoxia]]

## Discussion captured

### Authors' interpretation

The authors interpret MiTEs as a paradigm-shifting molecular class for cancer immunotherapy because they address three concurrent limitations of prior ICKs: (1) systemic toxicity (solved by TAM-protease-restricted activation); (2) limited durability (solved by simultaneous TAM reprogramming + lymphocyte activation); (3) T-cell-only dependence (solved by recruiting NK cells through IL-2Rβ-biased signalling and disrupting MHC-I evasion routes). They argue the MERFISH-derived TAM-T proximity is the biological foundation that makes trans-acting design feasible, and present MiTE-144 + αCTLA-4 as a near-curative regimen in a syngeneic mouse model with translational validation in human RCC PDTFs.

### Comparisons with prior literature (made by authors)

- Prior TAM-targeting (MARCO, VISTA, IDO1) — referenced as monotherapies with limited clinical efficacy
- TREM2 prior work — Molgora 2020, Katzenelenbogen 2020, Park 2021, Binnewies 2021 (TREM2 as TAM checkpoint, αTREM2 monotherapy limits)
- IL-2 superkine — Levin et al. 2012 Nature (H9 SK)
- Pro-cytokine / TME-conditional cytokine field — multiple references (refs 54–61) cited in Discussion, situating MiTEs vs prior αPD-L1-IL-15 (Mansurov 2022), αPD-1-IL-2 (Codarri Deak 2022), αTIM3-IL-2 (Sahin 2022)
- MMP14-TREM2 co-expression and CAF MMP14 — Sabbota et al. 2010, Knapinska 2017
- Knobs-into-holes bispecific engineering — Ridgway 1996

### Mechanistic hypotheses proposed

- "Dual TAM-T cell targeting by MiTE-144 thus provided more potent immune activation than checkpoint blockade alone." (p.7106) — proposing the bispecific TAM-T axis as a distinct mechanism class
- αCTLA-4 amplifies MiTE-144 effects "by depleting Tregs and reinforcing CD8+ T cell responses" (p.7110) — proposing Treg depletion as the operative mode of αCTLA-4 in this combination
- "MiTE-144 induces a shift from early toward a highly proliferative and cytotoxic NK phenotype, allowing sustained NK cell-mediated anti-tumor immunity" (p.7109) — proposing NK-mediated anti-tumor immunity as the third pillar (beyond myeloid reprogramming and T-cell activation)

### Caveats and self-criticism

The authors acknowledge: (1) long-term safety of protease-activated IL-2 must be established in non-human primates and chronic dosing; (2) study limited to RCC + syngeneic murine models — generalisation to other tumor types untested; (3) one of five RCC PDTFs was a non-responder; (4) IL-2 superkine still expanded Tregs in vivo despite design intent; (5) MiTE-144 + αCTLA-4 blunts the DC MHC-I / cDC1 reprogramming effect — combination effects on antigen presentation not fully characterised.

### Future directions suggested

- Test MiTEs across diverse tumor types beyond RCC and MC38/MCA205
- Combine MiTEs with radiotherapy, chemotherapy, or other immunotherapies
- Tune cytokine cargoes (IL-15 or tailored IL-2 variants)
- Establish long-term safety in non-human primates with chronic dosing
- Investigate ADA formation rates with masked vs unmasked IL-2

## Limitations

- Single TREM2 antagonist clone — generalisation to other αTREM2 mABs uncertain
- MC38 / MCA205 are highly immunogenic syngeneic models — translation to poorly inflamed human tumors is the standard caveat
- PDTF ex vivo culture (48 h) does not capture chronic-dosing dynamics, ADA formation, or stromal remodelling
- MMP14 expression in cancer-associated fibroblasts could activate MiTE outside TAMs (acknowledged but not quantified in vivo)
- Hypoxia-marked TAM upregulation under effective therapy is reported but not functionally dissected — the inferred TAM "state" remains transcriptional

## Open questions

### Open questions raised by authors

- Long-term safety of protease-activated IL-2 in primates and chronic dosing
- Activity of MiTEs across tumor types beyond RCC, MC38, MCA205
- Combination with radiotherapy / chemotherapy / other immunotherapies
- ADA formation under masked IL-2 strategies
- Rational tuning of cytokine cargo (IL-15, tailored IL-2 variants)

### Open questions identified during ingest

- Does CAF MMP14 cause off-target MiTE activation in stromal-rich tumors (PDAC, lung NSCLC)?
- Is the hypoxia-associated TAM state co-induced by MiTE-144 functionally similar to canonical "hypoxic-suppressive" TAMs (cf. [[hypoxia-pd-l1-tam-immune-evasion]])? Resolving this matters for the user's thesis (hypoxia-macrophage axis).
- How does MiTE-144 interact with [[trem2-mac-pd1-immune-niche-quartet]] HCC niche — does it disrupt or reinforce?
- Could MiTE-class molecules be adapted to other TAM-restricted enzymes (cathepsin B/L, ADAM proteases)?
- What is the in vivo cytokine "diffusion radius" of trans-released IL-2 SK in tumor tissue — required for predicting collateral activation?

## My take

A landmark TAM-targeted immunotherapy paper that resolves three known limitations of prior immunocytokines in a single integrated molecule. The most novel conceptual contribution is the "trans-acting" framing: separating antibody localisation (TREM2) from cytokine activation (MMP14 protease cleavage). For my thesis (macrophage / hypoxia / immune-suppression in skin and tumor), three threads matter:
1. Strong empirical TAM-T cell proximity backbone — useful primary citation for any spatial argument
2. MMP14-TREM2 co-expression as a TAM-specific signature — useful biomarker pair
3. The unexpected co-induction of hypoxia modules during effective therapy challenges the "hypoxic TAM = bad" narrative and is worth a follow-up read alongside [[ahr-tam-immunosuppression-tumour]] and [[hypoxia-pd-l1-tam-immune-evasion]] — the hypoxic TAM state may be more context-dependent than current consensus

The Amit-lab + Immunai collaboration positions this as a translational programme; expect follow-on clinical-stage MiTE-class agents within a few years.

## Related

- [[papers/trem2-macrophages-associated-enhanced-response-pd]] — Hamon 2025 partner paper on TREM2-mac niche in HCC ICB response
- [[papers/macrophages-targets-next-generation-cancer-immunotherapy]] — review covering TAM-targeted therapeutics, TREM2, and masked-antibody strategies
- [[concepts/myeloid-targeted-immunocytokine-mite]]
- [[concepts/mmp14-protease-activated-il2-prodrug]]
- [[concepts/trans-acting-immunocytokine]]
- [[concepts/tam-t-cell-spatial-proximity-tme]]
- [[concepts/mmp14-trem2-tam-marker-pair]]
- [[concepts/trem2-tumor-associated-macrophage]]
- [[concepts/trem2-mac-pd1-immune-niche-quartet]]
- [[concepts/masked-antibody-tme-conditional]]
- [[concepts/innate-immune-checkpoint-blockade]]
- [[concepts/pan-cancer-tam-atlas-23-clusters]]
- [[concepts/cxcl9-spp1-tam-ratio-ici-biomarker]]
- [[concepts/tumour-explant-short-term-culture]]
- [[foundations/trem2-receptor]]
- [[foundations/il-2-cytokine]]
- [[foundations/mmp14-matrix-metalloproteinase]]
- [[foundations/pd-1-receptor-pdcd1]]
- [[foundations/ctla-4-checkpoint]]
- [[foundations/mc38-syngeneic-tumor-model]]
- [[foundations/merfish-imaging-spatial]]
- [[foundations/scrna-seq-10x-chromium]]
- [[foundations/scvi-deep-generative-model]]
- [[foundations/totalvi-cite-seq-modeling]]
- [[foundations/cite-seq-citeseq]]
- [[foundations/mrvi-multi-resolution-variational-inference]]
- [[foundations/hotspot-gene-module-analysis]]
- [[foundations/multinichenetr-cell-cell-comm]]
- [[foundations/resolvi-spatial-transcript-correction]]
- [[foundations/nichenet-ligand-target-inference]]
- [[foundations/cellchat-cell-cell-communication]]
- [[foundations/tcga-the-cancer-genome-atlas]]
- [[people/ido-amit]]
- [[people/assaf-weiner]]
- [[people/michelle-von-locquenghien]]
