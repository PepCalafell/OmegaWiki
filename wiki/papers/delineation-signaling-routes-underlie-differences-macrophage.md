---
# === Identification ===
title: "Delineation of signaling routes that underlie differences in macrophage phenotypic states"
slug: delineation-signaling-routes-underlie-differences-macrophage
arxiv: ""
doi: "10.1093/narmme/ugaf013"
pmid: "41255709"
venue: "NAR Molecular Medicine"
year: 2025
authors: [Tiberiu Totu, Jonas Bossart, Elana Caire, Katharina Sribike, Chen Li, Markus Rottmar, Bettina Sobottka, Guocan Yu, Vanesa Ayala-Nunez, Marija Buljan]
first_author: "Tiberiu Totu"
corresponding_author: "Marija Buljan"

# === Source & metadata ===
source_type: pdf
s2_id: "424295b8a7bcf4b7d53ed42da6973a248691bccf"
date_added: 2026-06-02
ingested_date: 2026-06-02
ingest_version: 1
last_reviewed:

# === Classification ===
importance: 3
tier: TIER_2
tags: [macrophage, polarization, phosphoproteomics, proteomics, kinase, signaling, TAM, immunosuppression]
keywords: [macrophage polarization, phosphoproteomics, kinase activity footprinting, PAK2, PKCalpha, FOS, NCOR2, proteomic signature, tumor-associated macrophages]
domain: immunology

# === Biomedical domain ===
tissue: [blood, in_vitro_only, multi]
condition: [cancer, healthy]
disease_specific: [hepatocellular_carcinoma, brain_metastasis]
species: [human]
hypoxia_relevant: false
contains_immune_cells: true
contains_myeloid: true

# === Technique ===
techniques: [LC-MS/MS_proteomics, phosphoproteomics_TiIMAC, flow_cytometry, scRNA-seq_10x, bulk_RNA-seq]
n_samples:
n_cells_total:
integration_method: ""

# === Biology captured ===
key_cell_types: [M1 macrophages, M2a macrophages, M2c macrophages, monocyte-derived macrophages, tumor-associated macrophages]
key_markers: [CD86, CD206/MRC1, CD163, CD209, PAK2, PKCalpha/PRKCA, PKACalpha/PRKACA, RIPK2, JAK2, PDPK1, LRRK2, FOS, NCOR2, PPARgamma, MAFB, HSF1, PML]
key_pathways: [JAK-STAT, NF-kB, MAPK, mTOR, PPAR signaling, interferon signaling]

# === User project membership ===
projects: [thesis]
priority: context
read_status: read

# === HypoxiaVERSE-specific ===
hypoxiaverse_status:
exclusion_reason:
data_availability: "PRIDE PXD043978"

# === Cross-references ===
code_url: "https://github.com/MOFHM/MacrophageSignaling"
cited_by: []
---

## Problem

Macrophages occupy a broad spectrum of functional states between proinflammatory (M1-like) and immunosuppressive (M2-like) poles, and reprogramming tumor-associated macrophages (TAMs) is an attractive therapeutic strategy. While the signaling cascades that define *proinflammatory* macrophages (IFN-γ/JAK–STAT, p38, JNK, NF-κB) are well characterized, the pathways that drive *immunosuppressive* polarization are only incompletely mapped — and prior signaling studies relied mostly on murine cells, THP-1 lines, or small antibody panels rather than unbiased measurement in primary human cells.

## Key idea

Perform an in-depth, unbiased (phospho)proteomic characterization of **primary human** M1, M2a, and M2c macrophages, then infer the active **kinases** behind each state by phosphoproteomic footprinting. This nominates **PAK2 and PKCα** (with PKACα, PDPK1, LRRK2) as central kinases of immunosuppressive macrophages and, via multi-omics network integration, **FOS, NCOR2, and PPARγ** as central transcription regulators of the M2a state. The resulting proteomic signatures transfer to patient tumor scRNA-seq and separate proinflammatory macrophages better than the single marker CD163.

## Method

- **Cells**: CD14⁺ monocytes from four healthy blood donors, differentiated and polarized in vitro to M1 (LPS+IFN-γ), M2a (IL-4/IL-13), or M2c (IL-10); validated by flow cytometry (CD86/CD206/CD163). All states of a donor compared in a matched design.
- **Proteomics & phosphoproteomics**: FASP digestion; Ti-IMAC phosphopeptide enrichment; Orbitrap Fusion Lumos LC-MS/MS; [[foundations/maxquant-proteomics]] (Andromeda) with label-free quantification; MSstatsPTM-style adjustment of phosphopeptide changes for protein-abundance changes.
- **Differential analysis**: moderated t-tests, BH-FDR < 0.05, |log2FC| ≥ 1; KEGG/Reactome over-representation (CPDB, DAVID).
- **Kinase-activity footprinting** ([[concepts/kinase-activity-footprint-inference-phosphoproteomics]]): [[foundations/kinase-library-phosphosite-atlas]], [[foundations/netphorest-kinase-prediction]], [[foundations/kea3-kinase-enrichment-analysis]], plus curated PhosphoSitePlus/SIGNOR annotations; AlphaFold structures for activation-loop visualization.
- **Network integration**: STRING/BioGRID/IntAct interactions; current-flow betweenness centrality; MONET modularity decomposition; six public macrophage transcriptome datasets (M1/M2a/M2c) re-analyzed (DESeq2, DTU via DRIMseq, TRRUST TF inference).
- **Clinical validation**: scRNA-seq of patient HCC (Sharma et al.) and brain metastases (Gonzalez et al.); macrophages scored with proteomic vs literature vs CD163 signatures (Seurat ModuleScore / gene-set activity).

## Results

The matched (phospho)proteome quantified 5342 proteins and 5905 phosphopeptides (2313 phosphoproteins). Hundreds of proteins distinguished M1 from M2a (675) and M2c (806), recovering canonical markers (M1: CD86, GBP1, IDO1, ISG15, MX1; M2: CD209, CD206, CD163). At the phosphosite level, 71 kinases differed between M1 and M2, with MAPK over-represented. Activation-loop phosphosites pinpointed RIPK2 (S176, M1), JAK2 (S518, M1), PKCα (T497, both M2), and PKACα (T198, M2c). Footprinting recovered known M1 kinases (JNK1/2/3, p38) and nominated novel immunosuppressive-state kinases (IRAK1/4 in M2a; CAMKK2/GAK in M2c). PML carried 12 M1-high phosphoresidues. Network integration flagged FOS/NCOR2/PPARγ (M2a TF hubs) and PKCα (highest M2a centrality). Finally, proteomic signatures separated proinflammatory macrophages in patient HCC and brain-metastasis scRNA-seq (up to 89% M1-like), outperforming CD163 alone; proinflammatory macrophage fraction correlated with B-cell fraction in brain metastases (ρ = 0.91).

## All claims (exhaustive)

- `[c01]` Deep (phospho)proteomics of primary human M1/M2a/M2c quantifies 5342 proteins and 5905 phosphopeptides (p.9) "The label-free proteome and phosphoproteome quantification resulted in the identification of a total of 5342 proteins and 5905 phosphopeptides, which mapped to 2313 phosphoproteins" — confidence: high — type: methodological — links: [[foundations/maxquant-proteomics]] [[claims/deep-proteomic-phosphoproteomic-map-primary-human]]
- `[c02]` 675 / 806 proteins differentially expressed M1-vs-M2a / M1-vs-M2c (p.9) "675 and 806 proteins had significantly different expression levels between M1 and M2a, and between M1 and M2c macrophages, respectively" — confidence: high — type: quantitative — links: [[concepts/m1-m2-polarization-paradigm]] [[claims/hundreds-proteins-differentially-expressed-between-m1]]
- `[c03]` PAK2 and PKCα inferred as central regulators of immunosuppressive macrophages (abstract) "Analysis of direct and indirect evidence of kinase activities suggested PAK2 and PKCα kinases as important regulators of in vitro immunosuppressive macrophages" — confidence: medium — type: methodological — links: [[concepts/pak2-pkc-alpha-regulators-immunosuppressive-macrophages]] [[foundations/pak2-kinase]] [[foundations/pkc-alpha-prkca]] [[claims/pak2-pkc-alpha-inferred-regulators-vitro]]
- `[c04]` PKCα activation-loop T497 phosphorylated higher in both M2a and M2c (p.11) "the activation residue of the PKCα kinase (aka PRKCA), T497, had higher phosphorylation levels in both M2 states when compared to M1" — confidence: high — type: mechanistic — links: [[foundations/pkc-alpha-prkca]] [[claims/pkc-alpha-activation-loop-t497-phosphorylation]]
- `[c05]` PKACα activation-loop T198 phosphorylated higher in M2c (p.11) "the protein kinase cAMP-activated catalytic subunit alpha (PKACα aka PRKACA) T198 phosphosite was measured at a significantly higher level than in the M1 state" — confidence: high — type: correlational — links: [[foundations/pkac-alpha-prkaca]] [[claims/pkac-alpha-activation-loop-t198-phosphorylation]]
- `[c06]` RIPK2 autophosphorylation site S176 phosphorylated higher in M1 (p.11) "the S176 phosphoresidue within the RIPK2 kinase had a significantly higher phosphorylation level in the M1 state ... annotated as an auto-phosphorylation site essential for the RIPK2 catalytic activity" — confidence: high — type: mechanistic — links: [[foundations/ripk2-kinase]] [[claims/ripk2-autophosphorylation-site-s176-higher-m1]]
- `[c07]` JAK2 S518 phosphorylated higher in M1 (p.10) "Among the kinases with significantly higher phosphosite levels ... in the M1 state ... was JAK2 (S518), which is known to be related to the main axis of the JAK-STAT proinflammatory pathways" — confidence: medium — type: correlational — links: [[foundations/jak2-kinase]] [[claims/jak2-s518-phosphorylation-higher-m1-proinflammatory]]
- `[c08]` 71 kinases differentially phosphorylated M1-vs-M2, MAPK enriched (p.10) "71 protein kinases had significantly different quantitative levels of one or more phosphosites in the comparison between M1 and M2 phosphoproteomes ... 21 of the 71 ... belonged to the MAPK signaling pathway" — confidence: high — type: quantitative — links: [[foundations/mapk1-3-erk1-2-kinases]] [[claims/71-kinases-differentially-phosphorylated-between-m1]]
- `[c09]` Kinase Library footprinting recovers JNK and p38 as top M1 kinases (p.12) "the Kinase Library analysis, even though based solely on phosphopeptide sequences, correctly predicted known major signal transduction routes in the M1 state" — confidence: high — type: methodological — links: [[concepts/kinase-activity-footprint-inference-phosphoproteomics]] [[foundations/kinase-library-phosphosite-atlas]] [[claims/kinase-library-footprinting-predicts-jnk-p38]]
- `[c10]` IRAK1/IRAK4 inferred in M2a; CAMKK2/GAK in M2c (p.12) "Analysis of phosphoresidues upregulated in the M2a state suggested a high activity of interleukin 1 receptor-associated kinase (IRAK) 1 and IRAK4 kinases ... In M2c macrophages ... upregulation of the GAK and ... CAMKK2 kinases" — confidence: low — type: methodological — links: [[foundations/lrrk2-kinase]] [[claims/irak1-irak4-inferred-upregulated-m2a-camkk2]]
- `[c11]` FOS, NCOR2, PPARγ central transcription regulators of the M2a network (p.13) "central network elements in the M2a state included transcription regulators FOS, NCOR2, and PPARγ" — confidence: medium — type: methodological — links: [[concepts/fos-ncor2-ppargamma-transcriptional-hub-immunosuppressive]] [[foundations/fos-transcription-factor]] [[foundations/ncor2-nuclear-receptor-corepressor]] [[foundations/pparg-tf]] [[claims/fos-ncor2-ppargamma-central-transcription-regulators]]
- `[c12]` PML carries 12 phosphoresidues higher in M1 (p.10) "the tumor suppressor promyelocytic leukemia protein (PML), which had 12 phosphoresidues with higher phosphorylation levels in the M1 state compared to both M2a and M2c macrophages" — confidence: high — type: quantitative — links: [[foundations/pml-promyelocytic-leukemia-protein]] [[claims/pml-tumor-suppressor-carries-twelve-phosphoresidues]]
- `[c13]` Proteomic signatures separate proinflammatory macrophages in patient tumor scRNA-seq (p.14) "the signature proteins defined here through the proteome characterization of in vitro macrophages were able to distinguish proinflammatory macrophages in the both analyzed clinical single cell datasets" — confidence: high — type: methodological — links: [[concepts/proteomic-signature-classifies-proinflammatory-tumor-associated]] [[claims/proteomic-signatures-separate-proinflammatory-macrophages-patient]]
- `[c14]` CD163 alone fails to classify proinflammatory vs immunosuppressive macrophages (p.14) "CD163 alone as a marker was not able to classify proinflammatory and immunosuppressive macrophages ... while the two knowledge-based lists clearly defined proinflammatory clinical macrophage subsets" — confidence: high — type: methodological — links: [[concepts/proteomic-signature-classifies-proinflammatory-tumor-associated]] [[claims/cd163-alone-fails-classify-proinflammatory-versus]]
- `[c15]` Proinflammatory macrophage fraction correlates with B-cell fraction in brain metastases (p.14) "a strong correlation between the fraction of proinflammatory macrophages and B cells (Spearman ρ = 0.91, P < 2.1 × 10⁻⁶)" — confidence: medium — type: correlational — links: [[claims/proinflammatory-macrophage-fraction-correlates-cell-fraction]]

## Discussion captured

### Authors' interpretation
The authors argue that simplified in vitro models, despite their limitations, can map major signaling routes with clinically relevant assays that cannot be used in vivo. They recapitulate the well-known proinflammatory roles of p38, JNK, and JAK kinases in M1 and place RIPK2 (phosphorylated in its active loop) upstream of NF-κB. For immunosuppressive states — historically less well described — they propose PDPK1, PKCα, PKACα, PAK2, and LRRK2 as propagating kinases (with documented substrate relationships among them), and FOS/NCOR2/PPARγ as central M2a transcription regulators. They frame unbiased proteomic signatures as a powerful means to categorize macrophages in the TME, superior to single markers.

### Comparisons with prior literature (made by authors)
- RIP1 and PI3Kγ as previously highlighted immunosuppressive-macrophage kinases of therapeutic interest (Wang et al. 2018; Kaneda et al. 2016).
- Prior macrophage signaling work limited to murine cells / THP-1 / small antibody panels (refs 27–30); transcriptomic-only primary-human studies (refs 31–33).
- PAK2 regulating myeloid-derived suppressor cell development; WNK1 suppressing inflammatory cytokines; LRRK2 in Parkinson's and inflammatory bowel disease; CAMKK2 high in TAMs supporting tumor growth.
- M2a TFs MAFB and HSF1, and kinases PKCα/PDPK1, associated with aggressive tumor growth (refs 133, 134, 144, 174).
- Effective macrophage classification benefits from multiple markers (ref 113), versus CD163-only mass-cytometry classifications (refs 168, 169).

### Mechanistic hypotheses proposed
- Activation-loop phosphorylation of RIPK2 (S176), PKCα (T497), and PKACα (T198) reflects switching of these kinases to active states in the respective phenotypes (p.11).
- IRAK1/4 with TRAF6 can form a complex activating JNK/NF-κB, but binding of negative regulators (IRAK-M) could redirect substrate choice, explaining apparent increased IRAK activity in M2a (p.12).
- PKACα and PKCα drive protumoral immunosuppressive phenotypes via anti-inflammatory / NF-κB-suppressive signaling (p.11).

### Caveats and self-criticism
- In vitro M2 macrophages are not identical to in vivo TAMs; macrophages promoting tumor growth often have phenotypes not directly resembling in vitro M2 cells (p.14, p.17).
- M2c showed less pronounced proteome changes than M1/M2a, possibly due to stimulus concentration/duration (p.17).
- Interaction databases are biased toward well-studied proteins, which can skew network-derived hubs (p.16).
- Neither PKCα, PKACα, PAK2, nor LRRK2 had previously been defined as central immunosuppressive-macrophage regulators — these are nominations requiring validation (p.17).

### Future directions suggested
- Further exploration of the activity and clinical relevance of PDPK1, PKCα, PKACα, PAK2, and LRRK2 in immunosuppressive macrophages.
- Use of unbiased proteomic signatures to expand and refine clinically relevant macrophage-state biomarkers in the TME.
- Rational rewiring of cellular signaling pathways to reprogram macrophage states therapeutically.

## Limitations

- In vitro monocyte-derived macrophages; in vivo TAM states are richer and may differ.
- Kinase activities are largely *inferred* from phosphoproteomic footprints (Kinase Library / KEA3 / NetPhorest), not directly measured or perturbed.
- High phosphoproteome missingness requires imputation; M2c had limited proteome changes.
- Clinical validation is reanalysis of two public scRNA-seq cohorts with small per-tumor-type sample sizes.
- Network centrality is sensitive to interaction-database completeness and literature bias.

## Open questions

### Open questions raised by authors
- What are the precise activities and clinical roles of PKCα, PKACα, PAK2, PDPK1, and LRRK2 in immunosuppressive macrophages?
- Can rational signaling rewiring reprogram macrophage states in the TME?
- How best to expand state-specific macrophage biomarkers from unbiased proteomic signatures?

### Open questions identified during ingest
- Do perturbations (inhibition/knockdown) of PAK2 or PKCα causally revert immunosuppressive polarization in primary human macrophages?
- How do the kinase hubs (PAK2/PKCα) mechanistically connect to the TF hubs (FOS/NCOR2/PPARγ)?
- Is the strong macrophage–B-cell correlation in brain metastases mechanistic, and does it predict immunotherapy response?

## My take

A signaling-resolution complement to this vault's marker- and transcriptome-heavy TAM literature: it asks *which kinases* wire the immunosuppressive pole, an axis most macrophage-polarization papers leave implicit. The strongest evidence is the activation-loop phosphorylation of PKCα (T497) and PKACα (T198) and the positive-control recovery of JNK/p38 in M1; the PAK2/FOS/NCOR2 nominations are network-level and await perturbation. For thesis use it is most valuable as (i) a source of mechanistic kinase/TF hypotheses for immunosuppressive macrophages and (ii) a concrete argument that multi-marker proteomic signatures beat single markers (CD163) for classifying proinflammatory TAMs in patient scRNA-seq.

## Related

- [[concepts/pak2-pkc-alpha-regulators-immunosuppressive-macrophages]]
- [[concepts/fos-ncor2-ppargamma-transcriptional-hub-immunosuppressive]]
- [[concepts/kinase-activity-footprint-inference-phosphoproteomics]]
- [[concepts/proteomic-signature-classifies-proinflammatory-tumor-associated]]
- [[concepts/m1-m2-polarization-paradigm]]
- [[concepts/tumor-associated-macrophage-immunosuppression]]
- [[foundations/pak2-kinase]]
- [[foundations/pkc-alpha-prkca]]
- [[foundations/pkac-alpha-prkaca]]
- [[foundations/ripk2-kinase]]
- [[foundations/lrrk2-kinase]]
- [[foundations/pdpk1-pdk1-kinase]]
- [[foundations/jak2-kinase]]
- [[foundations/fos-transcription-factor]]
- [[foundations/ncor2-nuclear-receptor-corepressor]]
- [[foundations/mafb-transcription-factor]]
- [[foundations/hsf1-heat-shock-factor]]
- [[foundations/pml-promyelocytic-leukemia-protein]]
- [[foundations/pparg-tf]]
- [[foundations/mapk1-3-erk1-2-kinases]]
- [[foundations/kinase-library-phosphosite-atlas]]
- [[foundations/kea3-kinase-enrichment-analysis]]
- [[foundations/netphorest-kinase-prediction]]
- [[foundations/maxquant-proteomics]]
- [[people/tiberiu-totu]]
- [[people/jonas-bossart]]
- [[people/marija-buljan]]
