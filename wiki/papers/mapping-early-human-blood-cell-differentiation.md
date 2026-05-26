---
# === Identification ===
title: "Mapping early human blood cell differentiation using single-cell proteomics and transcriptomics"
slug: mapping-early-human-blood-cell-differentiation
arxiv: ""
doi: "10.1126/science.adr8785"
pmid: "40839704"
venue: "Science"
year: 2025
authors:
  - "Benjamin Furtwängler"
  - "Nil Üresin"
  - "Sabrina Richter"
  - "Mikkel Bruhn Schuster"
  - "Despoina Barmpouri"
  - "Henrietta Holze"
  - "Anne Wenzel"
  - "Kirsten Grønbæk"
  - "Kim Theilgaard-Mönch"
  - "Fabian J. Theis"
  - "Erwin M. Schoof"
  - "Bo T. Porse"
first_author: "Furtwängler"
corresponding_author: "Bo T. Porse; Erwin M. Schoof; Fabian J. Theis"

# === Source & metadata ===
source_type: pdf
s2_id: "b6bb52db76c97923f9e0dc8a3325cf71c60438a0"
date_added: 2026-05-26
ingested_date: 2026-05-26
ingest_version: 1
last_reviewed:

# === Classification ===
importance: 5
tier: TIER_1
tags:
  - single-cell-proteomics
  - scp-MS
  - SCoPE-MS
  - scRNA-seq
  - CITE-seq
  - multi-omics
  - hematopoiesis
  - HSPC
  - HSC
  - translation-dynamics
  - RNA-velocity
  - trajectory-inference
  - mass-spectrometry
  - TMT
  - mRNA-protein-discordance
keywords:
  - scp-MS
  - scProtVelo
  - SCeptre
  - GLUE
  - cellRank
  - CD34+
  - LTC-IC
  - SOD1
  - TALDO1
  - H1F0
domain: "single-cell methods / hematology / proteomics"

# === Biomedical domain ===
tissue: [bone_marrow, blood]
condition: [healthy]
disease_specific: []
species: [human]
hypoxia_relevant: false
contains_immune_cells: true
contains_myeloid: true

# === Technique ===
techniques: [scp-MS, SCoPE-MS, TMTpro_multiplexing, scRNA-seq_10x, CITE-seq, FACS, CRISPR_Cas9_KO, LTC-IC_assay, CFU_assay]
n_samples: 6
n_cells_total: 2500
integration_method: "GLUE (variational autoencoder, unpaired)"

# === Biology captured ===
key_cell_types:
  - HSC
  - MPP
  - LMPP
  - GMP
  - CLP
  - MEP
  - BaEoMa-progenitor
  - GMDP
  - MDP
  - pre-pDC
  - pre-mDC
  - early-erythroid
  - late-erythroid
  - CD34+ HSPC
key_markers:
  - CD34
  - CD38
  - CD45RA
  - CD123
  - CD71
  - BAH-1 (CD110)
  - Endomucin
  - H1F0
  - SOD1
  - SOD2
  - TALDO1
  - PRDX1
  - HMGA1
  - HP1BP3
  - macroH2A1
  - B2M
  - HLA-A
  - HLA-B
  - HLA-DRB1
  - ATF3
  - KLF2
  - SOX4
  - CDK6
  - APEX1
  - ELANE
  - MPO
  - AZU1
  - PRTN3
  - CTSG
  - S100A4
  - RAP1B
  - PRG2
  - CLC
  - LYZ
  - LGALS1
  - PLD4
  - TOP2B
  - CD10
  - LMNB2
  - ALDH1A1
key_pathways:
  - oxidative-stress-response
  - glycolysis
  - oxidative-phosphorylation
  - pentose-phosphate
  - MHC-class-I-assembly
  - MHC-class-II-presentation
  - prostaglandin-metabolism
  - chromatin-remodeling
  - ribosomal-translation
  - nucleocytoplasmic-export

# === User project membership ===
projects: [thesis, methods]
priority: core
read_status: read

# === HypoxiaVERSE-specific ===
hypoxiaverse_status: excluded
exclusion_reason: "healthy bone marrow only; no hypoxia perturbation or hypoxic niche focus"
data_availability: "BM samples from Rigshospitalet Department of Hematology; methods describe ethics approval 1705391"

# === Cross-references ===
code_url: ""
cited_by: []
---

## Problem

Single-cell transcriptomics (scRNA-seq) has driven the modern understanding of the human hematopoietic stem and progenitor cell (HSPC) compartment, but mRNA is an imperfect proxy for protein abundance — the actual workhorse of cell function. Targeted antibody methods (CITE-seq, scADT) profile only pre-selected surface epitopes. Until recently, untargeted, high-throughput single-cell proteomics by mass spectrometry (scp-MS) was unavailable at the scale needed to recapitulate an in vivo differentiation hierarchy. The paper asks: (i) can scp-MS resolve the human HSPC compartment at single-cell resolution, (ii) what protein-level information is missed by scRNA-seq, and (iii) can the temporal delay between transcription and translation be modeled to infer trajectories more accurately than RNA velocity alone.

## Key idea

Generate a >2500-cell scp-MS dataset of human CD34+ HSPCs by combining SCoPE-MS-style isobaric multiplexing (TMTpro 16-plex with a peptide carrier), RETICLE real-time search-assisted acquisition, and a 384-well plate workflow. Process the data with SCeptre (extends Scanpy for scp-MS). Integrate scp-MS with a matched CITE-seq dataset via GLUE (a VAE for unpaired multimodal data) to obtain a joint latent space. Run cellRank on this latent space for trajectory inference. Introduce scProtVelo, a latent-variable model that simultaneously fits transcription, translation, and degradation rates, to model temporal lag between mRNA and protein and quantify how much protein variance is genuinely captured by mRNA.

## Method

**Sample prep.** CD34+ BM HSPCs from six healthy adult donors. Two FACS strategies: classical gating into enriched populations, and total HSPC random sampling. Real-time computational gating revisited the GMP/MEP/CMP/BaEoMa boundaries; CD71 and BAH-1 (CD110) added to refine MEP purity. Cells were single-sorted into 384-well plates with a peptide carrier well (TMTpro-126), TMT-labeled, and pooled into 14-cell MS sets.

**Mass spec.** RETICLE real-time search-assisted acquisition; TMTpro 16-plex. SCeptre processing pipeline (Scanpy-based) with cell filtering, batch correction (via SCeptre's internal model), and median-ratio normalization. PCA regression confirmed donor/plate variance was largely removed.

**Multi-omics.** Companion CITE-seq dataset of Lin-CD34+ HSPCs from four donors (~9086 cells) integrated via totalVI. scp-MS + CITE-seq integrated unpaired via GLUE — silhouette score 0.03 indicated successful joint latent space. cellRank with the pseudotime kernel computed terminal states and fate probabilities on the joint embedding.

**Translation-dynamics model.** scProtVelo: a latent-variable model that learns gene-specific transcription, translation, mRNA-degradation, and protein-degradation rates, taking pseudotime annotations as a prior. Inferred protein velocity vectors aggregated over top 100 genes to recover cell-progression direction.

**Functional validation.** CRISPR/Cas9 KO of SOD1, TALDO1, and H1F0 in primary CD34+ BM cells. Readouts: LTC-IC limiting dilution (HSC surrogate), CFU assays, and 3-week stromal co-culture.

## Results

- 2500+ cells × ~2900 proteins; ~68% missing values per cell.
- 11 unsupervised clusters mapped onto the HSPC hierarchy (HSC, Prog1, Prog2, LMPP, GMDP, MDP, pre-pDC, CLP/pre-pDC, pB, MEP, BaEoMa).
- CD123+PRG2/CLC marks BaEoMa progenitors; CD71+BAH-1+ separates true MEPs from false-MEP GMP-like cells.
- Endomucin proposed as alternative LT-HSC marker; CD90 and CD49f showed lower specificity in this dataset.
- GLUE integration yielded a joint latent space combining scp-MS and CITE-seq with silhouette 0.03; cellRank on the joint space outperformed single-modality models (CLP, pre-pDC, MDP, pre-mDC assignments improved from 86% to 91% on RNA cells and from 65% to 95% on protein cells).
- HSC quiescence and chromatin signatures (H1F0, HP1BP3, macroH2A1, HMGA1, ATF3, KLF2) were visible on protein but weakly or not on mRNA.
- Differentiation away from HSCs upregulated ATP synthase and oxidative phosphorylation; HSCs were enriched in glycolysis and oxidative-stress response (SOD1, SOD2, PRDX1, TALDO1).
- Overall mRNA-protein correlation vector <0.25 across HSPC differentiation.
- CRISPR/Cas9 KO: SOD1 (LTC-IC frequency 1/153 vs 1/14 control), TALDO1 (1/42), H1F0 (1/80) — all reduce long-term hematopoietic potential; SOD1 KO additionally blocked granulocytic colony formation.
- B2M protein covaries with HLA-A/B (MHC-I complex) even when mRNA correlations are absent — example of post-transcriptional protein-protein covariation.
- scProtVelo explains ~50% of protein variance vs ~36% under the linear mRNA-protein assumption (40% relative improvement); fixes the spurious Late→Early erythroid backflow seen with standard scVelo on this trajectory.

## All claims (exhaustive)

- `[c01]` scp-MS captures >2900 proteins across 2500+ CD34+ HSPCs from 6 healthy donors with ~68% missing values per cell (p.2) "SCeptre processing yielded a dataset with over 2900 proteins quantified across 2500 cells, albeit with variable data completeness… on average 68% missing values per cell" — confidence: high — type: quantitative — links: [[concepts/single-cell-proteomics-mass-spec]] [[foundations/sceptre-scp-ms-processing]] [[foundations/tmtpro-isobaric-multiplexing]] [[claims/scp-ms-2500-hspcs-2900-proteins]]
- `[c02]` SCeptre batch correction removes donor, plate, and TMT-channel variance without residual technical clustering (p.2) "we did not observe any batch effects based on the TMTpro channel, individual donors or plates… PCA regression… revealed that only very low fractions of the variance could be explained by MS run, TMTpro label, donor or age" — confidence: high — type: methodological — links: [[foundations/sceptre-scp-ms-processing]] [[claims/sceptre-removes-scp-ms-batch-effects]]
- `[c03]` scp-MS UMAP recapitulates the human HSPC hierarchy (HSC/MPP → LMPP → GMP/CLP/MEP branches) (p.2) "Overlaying the cell identities derived from the two different cell-sorting strategies onto the UMAP embedding revealed clustering and branching of the sorted (en-riched) populations based on the HSPC differentiation hierarchy" — confidence: high — type: correlational — links: [[concepts/hspc-differentiation-multiomics]] [[claims/scp-ms-umap-recapitulates-hspc-hierarchy]]
- `[c04]` CD71 and BAH-1 (CD110) together delineate true MEPs from GMP-clustered false MEPs (p.3) "the combination of CD71 and BAH-1 clearly delineated MEPs, allowing the separation of those MEPs that clustered with GMPs… proteins associated with MEP differentiation, such as S100A4 and RAP1B, to be highly abundant in the BAH-1 positive MEPs, and proteins associated with granulocytic differentiation, such as ELANE and MPO, to have high levels in some of the putative false MEPs" — confidence: high — type: methodological — links: [[concepts/hspc-differentiation-multiomics]] [[claims/cd71-bah1-true-meps]]
- `[c05]` CD123 surface expression with high PRG2 and CLC protein marks BaEoMa progenitors (p.3) "Basophil-eosinophil-mast progenitors (BaEoMa) were marked by CD123 surface expression and high protein levels of Proteoglycan 2 (PRG2) and Charcot-Leyden Crystal Galec-tin (CLC), components of eosinophil granules" — confidence: high — type: methodological — links: [[concepts/hspc-differentiation-multiomics]] [[claims/cd123-prg2-clc-mark-baeoma]]
- `[c06]` Endomucin is proposed as a new LT-HSC surface marker because CD90 and CD49f showed lower specificity in this scp-MS dataset (p.2, fig S2B) "our data suggest that Endomucin might serve as an alternative surface marker for enriching LT-HSCs, since commonly used markers CD90 and CD49f exhibited lower or no specificity in our dataset" — confidence: medium — type: methodological — links: [[concepts/hspc-differentiation-multiomics]] [[claims/endomucin-alternative-lt-hsc-marker]]
- `[c07]` scp-MS and CITE-seq are successfully integrated unpaired via GLUE into a joint latent space (silhouette 0.03) (p.4) "The resulting joint latent space successfully integrated 'mRNA' cells from the CITE-seq dataset and 'protein' cells from the scp-MS dataset, with a silhouette score of 0.03" — confidence: high — type: methodological — links: [[concepts/joint-multimodal-latent-space]] [[foundations/glue-multiomics-integration]] [[claims/glue-integrates-scpms-citeseq-joint-latent]]
- `[c08]` cellRank on the joint latent space outperforms single-modality cellRank for lineage assignment (CLP/pre-pDC/MDP/pre-mDC: 86%→91% RNA, 65%→95% protein) (p.5) "correct lineage assignments of CLP, pre-pDC, MDP, and pre-mDC improved from 86% to 91% on the RNA cells and from 65% to 95% on the protein cells" — confidence: high — type: quantitative — links: [[concepts/joint-multimodal-latent-space]] [[foundations/cellrank-fate-mapping]] [[claims/joint-latent-cellrank-outperforms-single-modality]]
- `[c09]` HSC quiescence signature on protein level includes H1F0, ATF3 and KLF2 — driving exit from quiescence are CDK6, SOX4, APEX1 (p.5-6) "genes associated with HSCs like the transcription factors ATF3… or KLF2… genes associated with cell differentiation were CDK6… the transcription factor SOX4… and the endonuclease APEX1" — confidence: high — type: mechanistic — links: [[foundations/h1f0-linker-histone]] [[claims/hsc-quiescence-protein-signature-h1f0-atf3-klf2]]
- `[c10]` HSC differentiation shifts cellular metabolism from glycolysis to oxidative phosphorylation, with ATP synthase upregulation (p.3, 6) "HSCs… showed enrichment in glycolysis, likely reflecting their reliance on glycolysis instead of oxidative phosphorylation… Processes enriched during HSC differentiation included nucleosome organization and increased expression of the ATP synthase, required for the switch from glycolysis to oxidative phosphorylation" — confidence: high — type: mechanistic — links: [[claims/hsc-differentiation-glycolysis-to-oxphos]]
- `[c11]` Across HSPC differentiation the overall mRNA-protein correlation vector is below 0.25 (p.6) "Comparison between the full correlation vectors on mRNA and protein level revealed an overall weak correlation below 0.25 between these vectors" — confidence: high — type: quantitative — links: [[concepts/mrna-protein-discordance]] [[claims/mrna-protein-vector-correlation-below-025]]
- `[c12]` CRISPR/Cas9 KO of SOD1, TALDO1, or H1F0 in CD34+ BM HSPCs reduces LTC-IC frequency (SOD1 1/153, TALDO1 1/42, H1F0 1/80 vs AAVS1 1/14) (p.6-7) "LTC-IC limiting dilution analysis revealed a reduction in LTC-IC frequency of TALDO1 and H1F0 deficient cells (1 in 42 and 1 in 80, respectively) compared to the AAVS1 control (1 in 14)… a dramatic reduction in LTC-IC frequency (1 in 153; Fig. 5F)" — confidence: high — type: pharmacological — links: [[foundations/h1f0-linker-histone]] [[foundations/sod1-superoxide-dismutase]] [[foundations/taldo1-transaldolase]] [[claims/sod1-taldo1-h1f0-ko-reduces-ltc-ic]]
- `[c13]` SOD1-deficient HSPCs nearly fail to form colonies and show a block in granulocytic differentiation (p.7) "SOD1-deficient HSPCs… were largely unable to form colonies (only yielding small CFU-Gs)… a block in especially granulocytic differentiation in the stromal co-culture assay" — confidence: high — type: pharmacological — links: [[foundations/sod1-superoxide-dismutase]] [[claims/sod1-ko-blocks-granulocytic-differentiation]]
- `[c14]` B2M protein abundance covaries with HLA-A/B even when their mRNA does not — example of post-transcriptional regulation via MHC-I complex stabilization (p.7-8) "B2M protein abundance profile corresponded well to its complex part-ners, HLA-A and HLA-B in the major histocompatibility complex (MHC) class I… the abundance of Beta-2 microglobulin (B2M) could be regulated on the protein level by protection from degradation via stabilization in the MHC I complex" — confidence: high — type: mechanistic — links: [[concepts/mrna-protein-discordance]] [[claims/b2m-protein-covaries-with-mhc-i-complex]]
- `[c15]` scProtVelo explains ~50% of protein variance vs ~36% under a linear mRNA-protein assumption (40% relative improvement) (p.8) "scProtVelo resulted in more accurate modeling for almost all genes… a 40% increase in explained protein variance as compared to the simple assumption of a linear relationship (median R2 values of 36% for the linear model and 50% for scProtVelo, respectively)" — confidence: high — type: quantitative — links: [[concepts/scprotvelo-translation-dynamics]] [[claims/scprotvelo-40pct-improvement-over-linear]]
- `[c16]` Standard scVelo on erythroid scRNA-seq produces the previously reported erroneous Late→Early Eryth backflow; scProtVelo recovers the correct direction (p.8) "applying the standard RNA velocity workflow to the scRNA-seq cells of the erythroid trajectory resulted in the previously reported erroneous backflow in velocity vectors from Late to Early Erythroid progenitors" — confidence: high — type: methodological — links: [[concepts/scprotvelo-translation-dynamics]] [[concepts/scvelo-rna-velocity]] [[claims/scprotvelo-fixes-erythroid-backflow]]
- `[c17]` Chromatin regulators HMGA1, HP1BP3, and macroH2A1 (H2AFY) decrease during early HSC differentiation — visible on protein but not mRNA (p.6) "many proteins involved in chromatin structure among HSC-correlating factors, including… histone H1F0, the H1-like protein HP1BP3, which is required for HSC self-renewal, the histone macroH2A1 (H2AFY), associated with HSC homeo-stasis, and the chromatin regulator HMGA1… the decrease of these chromatin regulators during early HSC differentiation was better described via scp-MS" — confidence: high — type: mechanistic — links: [[concepts/mrna-protein-discordance]] [[claims/chromatin-regulators-decrease-on-protein-during-hsc-differentiation]]

## Discussion captured

### Authors' interpretation

The authors argue that scp-MS, while still limited in throughput and coverage, already captures complementary information to scRNA-seq about cell state and translation dynamics. They interpret the low mRNA-protein concordance during HSC quiescence as evidence that post-transcriptional regulation dominates in immature cells; during lineage specification, increased signal-to-noise from larger effect sizes drives higher mRNA-protein concordance. They also interpret scProtVelo's success as a proof-of-concept that integrated mRNA+protein single-cell data unlocks the study of gene expression dynamics — transcription, translation, and degradation rates — that splicing-kinetics-based RNA velocity cannot reach.

### Comparisons with prior literature (made by authors)

- Cite prior SCoPE-MS / SCoPE2 work (refs 25-28) as the technical foundation.
- Compare against bulk HSPC proteomics (ref 42) to validate scp-MS fold-changes (Pearson on log2 fold-changes high for matching populations).
- Compare against an external bulk mRNA+protein dataset of 59 breast cancer cell lines (refs 74-76) to confirm that low mRNA-protein concordance is a system-spanning rather than dataset-specific phenomenon (mRNA rank vs protein rank correlation = 0.35).
- Discuss the immunophenotypic CMP population as historically heterogeneous (refs 34-39) and reframe their observation that CMPs split between BaEoMa and myeloid as functional confirmation.

### Mechanistic hypotheses proposed

- "B2M could be regulated on the protein level by protection from degradation via stabilization in the MHC I complex" (p.8) — a hypothesis that protein-protein interactions stabilize otherwise low-mRNA-correlated proteins.
- The post-transcriptional regulation of chromatin regulators (HMGA1, HP1BP3, macroH2A1) is proposed to explain why HSC quiescence is captured only on the protein layer.

### Caveats and self-criticism

- "scp-MS is still associated with relatively low throughput and coverage" — the authors explicitly acknowledge this.
- scVI-modeled mRNA values may smooth out distributions; authors note "the scVI-modeled values should be used with caution as they represent only the mean of a modeled distribution with potentially high uncertainty".
- Difficulty in mass-spec at the most immature HSC subset (small protein amounts, small effect sizes) is acknowledged as limiting absolute statistical sensitivity at the HSC end.

### Future directions suggested

- Extend scp-MS multi-omics to other in vivo differentiation systems, normal development, and disease (cancer).
- Use scProtVelo as a starting point for simultaneously inferring multiple trajectories — currently limited by model complexity.
- Better methods for protein measurement depth at the immature HSC compartment.

## Limitations

- Healthy donors only (no disease, no perturbation other than 3-gene CRISPR KO).
- ~68% missing values per cell on the protein layer; many proteins quantified intermittently.
- GLUE integration is unpaired; the same physical cells were not measured by both modalities, so per-cell mRNA-protein correlations are inferred via the joint latent space rather than directly observed.
- Cluster-based annotation must be interpreted alongside the joint-space label transfer; some progenitor classes (Progenitors 1, Progenitors 2) span FACS gates and are intrinsically heterogeneous.
- scProtVelo, as deployed, requires a pseudotime prior — circular reasoning risk if pseudotime is itself derived from the same data.

## Open questions

### Open questions raised by authors

- Can scp-MS be scaled to in vivo systems with rarer cell types and to disease states?
- Can simultaneous inference of multiple trajectories be made tractable in scProtVelo?
- Which post-transcriptional mechanisms beyond complex-mediated stabilization (e.g., B2M↔MHC-I) explain the broader mRNA-protein discordance during quiescence?

### Open questions identified during ingest

- Does the SOD1-KO granulocytic block reflect a redox-specific requirement, or is it a general HSPC stress phenotype? The SOD1/SOD2 contrast (SOD2 KO replicates much of the phenotype but without proliferation arrest) is suggestive but unresolved.
- How sensitive are scProtVelo's translation-rate inferences to mis-specified pseudotime priors?
- Would the same conclusions hold under sparser TMT channels (e.g., 8-plex) or shotgun-DIA workflows that bypass isobaric labeling entirely?

## My take

The strongest contribution is the dataset itself — a 2500-cell scp-MS atlas of human HSPCs paired with a matched CITE-seq layer — plus the SCeptre processing pipeline, which transposes Scanpy idioms onto mass-spec data and is reusable for future scp-MS studies. scProtVelo is a thoughtful generalization of RNA velocity to a third axis (translation), and the 40% variance-explanation improvement over linear mRNA→protein is non-trivial. The CRISPR KO validation of SOD1/TALDO1/H1F0 elevates the work from descriptive to causal for at least three protein hits. Caveat: GLUE-based unpaired integration adds a layer of inference; future work pairing both modalities per-cell (e.g., dogma-seq variants for proteins) would tighten the per-gene mRNA-protein correlations the authors quantify.

For my thesis (hypoxia / oxidative stress / myeloid identity): SOD1 and TALDO1 emerge here as functional regulators of HSPC long-term potential — a hypoxia-redox link worth tracking even though the paper is on healthy BM. The protein-level visibility of chromatin regulators (HMGA1, macroH2A1) is also directly relevant to how I should interpret epigenetic-state changes in scRNA-seq-only datasets.

## Related

- [[concepts/single-cell-proteomics-mass-spec]] — primary methodological framing
- [[concepts/scprotvelo-translation-dynamics]] — new latent-variable model introduced here
- [[concepts/mrna-protein-discordance]] — central interpretive concept
- [[concepts/joint-multimodal-latent-space]] — integration strategy
- [[concepts/hspc-differentiation-multiomics]] — biological scaffold
- [[foundations/sceptre-scp-ms-processing]]
- [[foundations/tmtpro-isobaric-multiplexing]]
- [[foundations/reticle-realtime-search-acquisition]]
- [[foundations/glue-multiomics-integration]]
- [[foundations/totalvi-cite-seq-modeling]]
- [[foundations/cellrank-fate-mapping]]
- [[foundations/h1f0-linker-histone]]
- [[foundations/sod1-superoxide-dismutase]]
- [[foundations/taldo1-transaldolase]]
- [[foundations/scvelo-rna-velocity]]
- [[foundations/scrna-seq-10x-chromium]]
- [[foundations/scvi-deep-generative-model]]
- [[foundations/harmony-integration]]
- [[people/benjamin-furtwangler]]
- [[people/nil-uresin]]
- [[people/erwin-schoof]]
- [[people/bo-porse]]
- [[people/fabian-theis]]
