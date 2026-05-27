---
# === Identification ===
title: "HIF-1 regulates mitochondrial function in bone marrow-derived macrophages but not in tissue-resident alveolar macrophages"
slug: hif-regulates-mitochondrial-function-bone-marrow
arxiv: ""
doi: "10.1038/s41598-025-95962-3"
pmid: "40185846"
venue: "Scientific Reports"
year: 2025
authors:
  - "Parker S. Woods"
  - "Rengül Cetin-Atalay"
  - "Angelo Y. Meliton"
  - "Kaitlyn A. Sun"
  - "Obada R. Shamaa"
  - "Kun Woo D. Shin"
  - "Yufeng Tian"
  - "Benjamin Haugen"
  - "Robert B. Hamanaka"
  - "Gökhan M. Mutlu"
first_author: "Parker S. Woods"
corresponding_author: "Gökhan M. Mutlu"

# === Source & metadata ===
source_type: pdf
s2_id: "9bcf5a1c49064ade44de7caae6e744a7aa579413"
date_added: 2026-05-27
ingested_date: 2026-05-27
ingest_version: 1
last_reviewed: null

# === Classification ===
importance: 3
tier: TIER_2
tags:
  - HIF1A
  - BMDM
  - tissue-resident-alveolar-macrophage
  - macrophage-ontogeny
  - immunometabolism
  - glycolysis
  - oxidative-phosphorylation
  - FG-4592
  - roxadustat
  - prolyl-hydroxylase-inhibitor
  - c-Myc
  - DoRothEA
  - ribosomal-biogenesis
  - TCA-cycle
  - itaconate
  - succinate
  - LPS
  - inflammation
  - LysM-CreERT2
  - Seahorse
  - GC-MS
  - ETC-inhibitor
keywords:
  - ontogeny-divergent HIF-1α macrophage function
  - HIF-1α Myc reciprocal regulation BMDM
  - alveolar macrophage HIF-1α dispensability
  - bone marrow-derived macrophage glycolytic HIF dependence
  - prolyl hydroxylase inhibitor FG-4592 macrophage
  - inducible myeloid HIF-1α deletion mouse
  - c-Myc compensatory mitochondrial axis HIF-deficient macrophage
domain: "immunology / immunometabolism / hypoxia-signaling / macrophage-biology"

# === Biomedical domain ===
tissue:
  - lung
  - bone_marrow
  - in_vitro_only
condition:
  - healthy
disease_specific: []
species:
  - mouse
hypoxia_relevant: true
contains_immune_cells: true
contains_myeloid: true

# === Technique ===
techniques:
  - bulk_RNA-seq
  - western_blot
  - seahorse_extracellular_flux
  - GC-MS_metabolomics
  - qPCR
  - ELISA
  - immunofluorescence
  - siRNA_knockdown
  - inducible_LysM-CreERT2
  - DoRothEA_TF_inference
  - GO-BP_enrichment
  - CHEA_target_heatmap
n_samples: null
n_cells_total: null
integration_method: ""

# === Biology captured ===
key_cell_types:
  - bone_marrow_derived_macrophage_BMDM
  - tissue_resident_alveolar_macrophage_TR_AM
key_markers:
  - HIF1A
  - MYC
  - HK2
  - LDHA
  - PFKFB3
  - PKM2
  - MCT4
  - PHD2
  - TNF
  - IL6
  - IL1B
  - KC_CXCL1
  - succinate
  - citrate
  - itaconate
  - lactate
key_pathways:
  - HIF1A_target_transcription
  - glycolysis
  - oxidative_phosphorylation_ETC
  - TCA_cycle
  - Myc_regulon_ribosomal_biogenesis
  - LPS_TLR4_NFKB_cytokine_axis

# === User project membership ===
projects:
  - thesis
  - hypoxia
priority: useful
read_status: read

# === HypoxiaVERSE-specific ===
hypoxiaverse_status: candidate
exclusion_reason: ""
data_availability: "RNA-seq data: GEO accession in supplementary; mouse strains Hif1a^fl/fl^ (JAX 007561) and Lyz2^tm1(cre/ERT2)Grtn^ (JAX 031674)"

# === Cross-references ===
code_url: ""
cited_by: []
---

## Problem

It is widely accepted that HIF-1α is a master regulator of macrophage glycolytic metabolism and pro-inflammatory effector function, an inference largely built on bone-marrow-derived macrophages (BMDMs) and peritoneal macrophages. Yet tissue-resident alveolar macrophages (TR-AMs) live in an oxygen-rich, glucose-poor airspace, are predominantly oxidative-phosphorylation-dependent at baseline, and progressively silence HIF-1α target genes during postnatal maturation. Whether HIF-1α is functionally required in mature TR-AMs — and whether HIF-1α's roles in glycolysis and inflammation are decomposable in BMDMs — has remained unclear. Resolving this matters clinically because acute respiratory distress syndrome (ARDS) outcomes depend on the survival of TR-AMs versus the activity of recruited monocyte-derived macrophages, and HIF-stabilising drugs (FG-4592/roxadustat) are increasingly considered for pulmonary contexts.

## Key idea

HIF-1α exerts ontogeny-divergent functions in macrophages. In BMDMs (monocyte-derived), HIF-1α is required at baseline for glycolytic capacity, ETC-inhibitor resistance, and full pro-inflammatory cytokine output, and its loss derepresses a c-Myc–driven mitochondrial / ribosomal-biogenesis / proliferation program. In TR-AMs, HIF-1α is functionally silent at steady state and during LPS exposure — load-bearing only under hypoxia or pharmacological PHD inhibition, where it drives a glycolytic rescue against ETC failure. Using tamoxifen-inducible myeloid-lineage Hif1a deletion (Hif1a^fl/fl^:LysM-CreERT2^+/−^), the authors map the BMDM-vs-TR-AM dichotomy and identify Myc as the causal compensatory driver in HIF-1α-deficient BMDMs.

## Method

**Mouse model**: Hif1a^fl/fl^ (B6.129-Hif1a^tm3Rsjo^/J, JAX 007561) × Lyz2^tm1(cre/ERT2)Grtn^ (JAX 031674) — tamoxifen-inducible myeloid-lineage Hif1a deletion. Tamoxifen (80 mg/kg/day × 5 days in corn oil). Deletion verified by Hif1a exon-2 qPCR.

**Macrophage isolation and culture**: TR-AMs by bronchoalveolar lavage (>95% pure); BMDMs differentiated from bone marrow over 7 days in M-CSF (~100% pure). Cultured ± FG-4592 (25 µM, 16 h overnight) ([[foundations/fg-4592-roxadustat]]).

**Bulk RNA-seq**: HIF-1α target genes interrogated via CHEA ChIP-X enrichment heatmaps; DEGs at logFC ≥ 1, p ≤ 0.05.

**Bioenergetic phenotyping** ([[foundations/seahorse-extracellular-flux-analyzer]]): Seahorse XF24 — Glycolysis Stress Test (glucose / oligomycin / 2-DG) and Mito Stress Test (oligomycin / FCCP / rotenone + antimycin A).

**Metabolomics**: GC-MS for TCA-cycle metabolites (lactate, pyruvate, succinate, citrate, itaconate, malate, etc.).

**Protein expression**: Western blot — HIF-1α nuclear localisation, glycolytic enzymes (HK2, LDHA, PFKFB3, PKM2, MCT4, PHD2), ETC complex I-IV cocktail; immunofluorescence for HIF-1α nuclear localisation.

**Cytokine quantification**: ELISA for TNFα, IL-6, IL-1β, KC (CXCL1) after LPS ± ETC inhibitors (rotenone 20 nM, antimycin A 20 nM) ± FG-4592 preconditioning.

**Cell death**: Sulforhodamine B assay after rotenone or antimycin A ± FG-4592 preconditioning.

**TF activity inference** ([[foundations/dorothea-tf-regulon-analysis]]): DoRothEA mouse-regulon enrichment on Hif1a^−/−^ vs Hif1a^+/+^ BMDM DEGs; GO-BP enrichment; CHEA HIF-1α and c-Myc target heatmaps.

**Causal Myc rescue**: siRNA electroporation of Myc into Hif1a^−/−^ BMDMs (48 h rest) followed by Mito Stress Test + western blot validation.

**Validation**: siRNA Hif1a knockdown in BMDMs as a kinetic counterpoint to genetic deletion; Poly(I:C) challenge in TR-AMs as a TLR3 control.

## Results

### 1. HIF-1α deletion remodels BMDM but not TR-AM transcriptome at baseline (Fig. 1)
- TR-AM Hif1a^−/−^ vs Hif1a^+/+^ baseline: 10 DEGs (8 up, 2 down).
- BMDM Hif1a^−/−^ vs Hif1a^+/+^ baseline: 305 DEGs (121 up, 184 down).
- FG-4592 response is greatly diminished in Hif1a^−/−^ macrophages of both types — HIF-1α target heatmaps confirm specificity.

### 2. HIF-1α deletion broadly impairs BMDM glycolysis; TR-AM glycolysis only after FG-4592 (Fig. 2)
- FG-4592 increases TR-AM ECAR ~4-fold in Hif1a^+/+^ but not Hif1a^−/−^.
- Hif1a^−/−^ BMDMs have lower baseline ECAR and lower HK2/LDHA expression; FG-4592 cannot rescue.
- Hif1a^−/−^ BMDMs become susceptible to ETC-inhibitor (rotenone, antimycin A) cell death — phenocopying control TR-AMs.

### 3. HIF-1α deletion boosts mitochondrial function in BMDMs but not TR-AMs (Fig. 3)
- Hif1a^−/−^ BMDMs show higher basal OCR, ATP production; less inhibitable by FG-4592.
- GC-MS: elevated TCA-cycle metabolites in Hif1a^−/−^ BMDMs.
- TR-AMs: only mild elevation in spare respiratory capacity; no functional change in basal respiration.

### 4. ETC complex protein/gene expression elevated in Hif1a⁻/⁻ BMDMs only (Fig. 4)
- ETC complexes I-IV ↑ at protein and gene level in Hif1a^−/−^ BMDMs.
- FG-4592 reduces ETC gene expression in Hif1a^+/+^ TR-AMs and BMDMs (HIF-1α-dependent suppression of ETC genes under pseudohypoxia) but does not alter ETC protein levels in short term.

### 5. HIF-1α dispensable for LPS-induced glycolytic flux; required for cytokine output (Fig. 5A-E)
- LPS-induced ECAR rise in BMDMs is HIF-1α-independent (genetic KO + siRNA concordant) when normalised to baseline.
- Hif1a^−/−^ BMDMs secrete less TNFα, IL-6, IL-1β after LPS; ETC inhibition worsens this.
- HIF-1α stabilisation in TR-AMs occurs only under FG-4592, not under LPS or Poly(I:C).

### 6. Hif1a⁻/⁻ BMDMs show LPS-driven elevation of immunoregulatory TCA metabolites (Fig. 5F)
- Reduced lactate; elevated succinate, citrate, itaconate; pyruvate unchanged.
- TR-AMs: only minor malate elevation in Hif1a^−/−^.

### 7. c-Myc is the most positively enriched regulon in Hif1a⁻/⁻ BMDMs (Fig. 6A-D)
- DoRothEA: HIF1A most negative; MYC most positive NES.
- Pro-growth regulons up: E2F1-4, LEF1, GIL2, TFDP1.
- Cell-cycle-arrest / glucose-homeostasis regulons down: FOXO, TCF12, MAF, ONECUT.
- Shared HIF/Myc target genes: only the glycolytic subset is downregulated, confirming HIF-1α as the dominant glycolytic driver.

### 8. Myc siRNA rescues mitochondrial elevation in Hif1a⁻/⁻ BMDMs (Fig. 6E-G)
- Myc knockdown returns basal OCR and ATP production to Hif1a^+/+^ control levels — establishing causal Myc-dependence of the mitochondrial compensation.

## All claims (exhaustive)

- `[c01]` HIF-1α deletion produces 305 baseline DEGs in BMDMs vs only 10 in TR-AMs — ontogeny-asymmetric transcriptional dependence (p.2-3, Fig. 1B,E; Suppl. Fig. S3) "loss of HIF-1α in TR-AMs resulted in minimal changes in gene expression at baseline with only 10 observed significantly differentially expressed genes... HIF-1α deletion resulted in significant alterations at baseline in BMDMs with 305 DEGs" — confidence: high — type: quantitative — links: [[foundations/hif1a]] [[foundations/bone-marrow-derived-macrophage-bmdm]] [[foundations/tissue-resident-alveolar-macrophage]] [[concepts/ontogeny-divergent-hif1a-macrophage-metabolism]] [[claims/hif1a-deletion-asymmetric-transcriptome-bmdm-vs-tram]]
- `[c02]` TR-AM HIF-1α is required for the FG-4592-induced glycolytic shift and for ETC-inhibitor cytoprotection — Hif1a⁻/⁻ TR-AMs fail to upregulate ECAR and die under rotenone/antimycin A (p.3-4, Fig. 2A,B,E) "after treatment with FG-4592, Hif1a−/− TR-AMs had significantly lower glycolysis compared to treated TR-AM controls... FG-4592 became ineffective in rescuing Hif1a−/− TR-AMs from ETC inhibitor-induced cell death" — confidence: high — type: pharmacological — links: [[foundations/fg-4592-roxadustat]] [[foundations/tissue-resident-alveolar-macrophage]] [[foundations/phd-prolyl-hydroxylases]] [[concepts/ontogeny-divergent-hif1a-macrophage-metabolism]] [[claims/tram-hif1a-required-fg4592-glycolytic-shift]]
- `[c03]` HIF-1α deletion in BMDMs collapses baseline glycolytic capacity and ETC-inhibitor resistance — Hif1a⁻/⁻ BMDMs phenocopy control TR-AMs (p.4-5, Fig. 2F-J; Suppl. Fig. 4B) "Glycolytic rates were significantly lower in Hif1a−/− BMDMs... BMDMs are resistant to ETC inhibition-induced death at baseline but they became sensitized after the loss of HIF-1α" — confidence: high — type: mechanistic — links: [[foundations/hif1a]] [[foundations/bone-marrow-derived-macrophage-bmdm]] [[foundations/hk2-hexokinase-2]] [[foundations/ldh-lactate-dehydrogenase]] [[concepts/warburg-effect-hif1a-glycolytic-reprogramming]] [[concepts/hif-dependent-glycolysis-immune-cell-differentiation]] [[claims/bmdm-hif1a-required-baseline-glycolysis]]
- `[c04]` HIF-1α deletion enhances mitochondrial OXPHOS, ETC complex I-IV protein expression, and TCA cycle metabolite pools in BMDMs — HIF-1α acts as a negative regulator of mitochondrial function (p.5-6, Fig. 3C-E; Fig. 4C,D; Suppl. Fig. 6) "Hif1a−/− BMDMs maintained higher basal oxygen consumption rates and ATP production... HIF-1α deletion in BMDMs led to significant increases in protein expression for ETC complexes I-IV" — confidence: high — type: mechanistic — links: [[foundations/bone-marrow-derived-macrophage-bmdm]] [[foundations/seahorse-extracellular-flux-analyzer]] [[concepts/ontogeny-divergent-hif1a-macrophage-metabolism]] [[concepts/c-myc-compensatory-mitochondrial-axis-hif-deficient-bmdm]] [[claims/bmdm-hif1a-loss-enhances-mitochondrial-oxphos]]
- `[c05]` LPS-induced acute glycolytic flux in BMDMs is HIF-1α-independent — concordant in genetic KO and siRNA knockdown — supporting post-translational (PFKFB3/PKM2) rather than HIF-transcriptional control of acute LPS glycolysis (p.7-8, Fig. 5A,B; Suppl. Fig. 7A-C) "Hif1a−/− BMDMs still respond to LPS by immediately upregulating glycolysis... when the ECAR was normalized to percent change... no change in the magnitude of glycolytic induction" — confidence: high — type: mechanistic — links: [[foundations/lps-toll-like-receptor-signaling]] [[foundations/bone-marrow-derived-macrophage-bmdm]] [[claims/bmdm-lps-glycolytic-flux-hif1a-independent]]
- `[c06]` Hif1a⁻/⁻ BMDMs secrete less TNFα, IL-6, and IL-1β after LPS; TR-AM cytokine output is HIF-1α-independent unless preconditioned with FG-4592 (p.8-9, Fig. 5E; Suppl. Fig. S11A) "Hif1a−/− BMDMs secreted less TNFα, IL-6, and IL-1β in response to LPS and exhibited reduced cytokine secretion in the presence of an ETC inhibitor" — confidence: high — type: pharmacological — links: [[foundations/tnf-tumor-necrosis-factor]] [[foundations/il-6-cytokine]] [[foundations/lps-toll-like-receptor-signaling]] [[concepts/ontogeny-divergent-hif1a-macrophage-metabolism]] [[claims/bmdm-hif1a-loss-reduces-cytokine-secretion]]
- `[c07]` HIF-1α is not stabilised in TR-AMs by LPS or Poly(I:C), only by hypoxia or FG-4592; in BMDMs LPS-induced HIF-1α peaks at ~4 h then returns to baseline by 24 h — challenges prior reports of TLR-driven HIF-1α induction in TR-AMs (p.8, Fig. 5C,D; Suppl. Fig. S8-S10) "nuclear stabilization of HIF-1α in BMDMs occurs early in exposure, peaks around 4 h, and returns to near baseline levels by 24 h... HIF-1α was only observed in the presence of FG-4592 in TR-AMs, but not in the presence of LPS" — confidence: medium — type: mechanistic — links: [[foundations/hif1a]] [[foundations/tissue-resident-alveolar-macrophage]] [[claims/tram-hif1a-not-stabilized-by-lps-only-by-hypoxia]]
- `[c08]` Hif1a⁻/⁻ BMDMs after LPS accumulate immunoregulatory TCA metabolites — succinate, citrate, itaconate — while lactate falls (p.9, Fig. 5F) "Hif1a−/− BMDMs had reduced lactate production in response to LPS... succinate, citrate, and itaconate, which are known regulators of macrophage inflammation, were robustly elevated in Hif1a−/− BMDMs" — confidence: high — type: quantitative — links: [[foundations/itaconate-metabolite]] [[foundations/sucnr1-succinate-receptor]] [[concepts/m1-macrophage-tca-breaks-itaconate-succinate]] [[claims/bmdm-hif1a-loss-elevates-tca-itaconate-succinate-citrate]]
- `[c09]` DoRothEA TF inference identifies c-Myc as the most positively enriched regulon in Hif1a⁻/⁻ BMDMs (HIF-1α most negative); concordant pro-growth program (E2F1-4, LEF1, GIL2, TFDP1) up, FOXO/TCF12/MAF/ONECUT down (p.9-10, Fig. 6A-D) "Not surprisingly, the HIF-1α regulon genes had the most negative enrichment score in our Hif1a−/− BMDMs. In contrast, Myc was the most positively enriched regulatory interaction" — confidence: high — type: methodological — links: [[foundations/dorothea-tf-regulon-analysis]] [[foundations/myc-oncogene]] [[concepts/c-myc-compensatory-mitochondrial-axis-hif-deficient-bmdm]] [[claims/bmdm-hif1a-loss-derepresses-myc-regulon-dorothea]]
- `[c10]` Myc siRNA in Hif1a⁻/⁻ BMDMs rescues elevated basal OCR and ATP production back to control levels — establishing Myc as causal mediator of mitochondrial compensation (p.10, Fig. 6E-G) "Myc knockdown in Hif1a−/− BMDMs reduced basal respiration and ATP production to levels comparable to control BMDMs. This suggests that Myc is responsible for increased mitochondrial activity in the absence of HIF-1α" — confidence: high — type: mechanistic — links: [[foundations/myc-oncogene]] [[concepts/c-myc-compensatory-mitochondrial-axis-hif-deficient-bmdm]] [[claims/myc-sirna-reverses-mitochondrial-elevation-hif1a-ko-bmdm]]

## Discussion captured

### Authors' interpretation

The authors frame their findings as a refinement, not a reversal, of the canonical view of HIF-1α as a master macrophage regulator: HIF-1α is indeed central in BMDMs, but its role is shaped by macrophage ontogeny. In TR-AMs, postnatal silencing of HIF-1α target genes leaves the cell baseline-independent of HIF-1α, with HIF-1α only re-engaging under hypoxic/PHD-inhibited stress to drive a glycolytic emergency program. In BMDMs, HIF-1α and c-Myc act in mutual antagonism — HIF-1α loss removes the brake on Myc, which then drives a mitochondrial-dominant, ribosomal-biogenic, proliferative state at the expense of pro-inflammatory output. They highlight that this resembles the long-known cancer-cell HIF-1α–Myc antagonism, now extended to inflammatory macrophages. Therapeutically, they argue HIF-1α-targeting in ARDS may be useful because it can rescue TR-AMs from ETC failure while simultaneously dampening recruited-macrophage pro-inflammatory output.

### Comparisons with prior literature (made by authors)

- **Cramer et al. 2003 (Cell)** — original HIF-1α as a key regulator of myeloid inflammation; framework the present paper refines.
- **Tannahill et al. 2013 (Nature)** — succinate-driven HIF-1α/IL-1β axis in LPS-BMDMs; consistent with HIF-1α involvement in BMDM cytokine output.
- **Wang et al. 2017 / Woods 2022** — TR-AM low glycolytic capacity baseline; FG-4592-driven glycolytic adaptation; previous work from the group that motivated this study.
- **Soucek 2019** — postnatal silencing of HIF-1α target genes during TR-AM maturation; supports steady-state dispensability.
- **Daniel 2018 (Cell)** — Myc upregulation in MCSF-restimulated BMDMs drives proliferative-mitochondrial phenotype; mirrors the present Myc rescue.
- **Koshiji et al. 2004; Gordan et al. 2007** — HIF-1α displaces c-Myc to induce cell-cycle arrest under hypoxia in tumor cells; opposite directionality but supports the antagonism framework.
- **Zhu et al. 2018, 2020** — Poly(I:C) / influenza induces HIF-1α in TR-AMs; present authors fail to replicate and attribute to GM-CSF culture conditions.

### Mechanistic hypotheses proposed

- "It may be that in the absence of HIF-1α other transcription factors aid in the basal maintenance of BMDM glycolysis, but that HIF-1α is required for a fully functional glycolytic phenotype" (p.11).
- "Without HIF-1α, c-Myc can serve a larger role in shaping BMDM metabolism, which fundamentally changes how BMDMs respond to immune stimulus" (p.12).
- "Elevated citrate... can be exported from the mitochondria to generate acetyl-CoA, which can be used for de novo fatty acid synthesis or epigenetic modifications" — proposed link between metabolic reshaping and downstream gene-expression alterations (p.11-12).

### Caveats and self-criticism

- "This system may not delete HIF-1α in 100% of cells upon tamoxifen exposure" — Lyz2-CreERT2 partial-deletion caveat acknowledged.
- "Lyz2^CreERT2^ allele results in Lyz2 heterozygosity in our cells" — possible secondary phenotypic confound.
- "BMDMs derived in CSF-1 may not perfectly recapitulate the phenotype of recruited macrophages" — translational caveat for in-vivo extrapolation.
- "While hypoxia is a more physiological activator of HIF-1α, we chose to use a chemical prolyl hydroxylase inhibitor" — acknowledged that HIF-independent hypoxic responses are missed in the FG-4592 design.

### Future directions suggested

- Dissecting how chronic in-vivo conditions (ARDS, infection) engage the HIF-1α-Myc axis in resident vs recruited lung macrophages.
- Testing whether other tissue-resident macrophages (Kupffer, microglia, peritoneal) show the same ontogeny-divergent HIF-1α dependence.
- Translational use of FG-4592 / roxadustat in ARDS — preserving TR-AMs against ETC failure while suppressing recruited-macrophage inflammation.

## Limitations

- **Partial deletion**: LysM-CreERT2 may not delete HIF-1α in 100% of cells.
- **Heterozygosity confound**: Lyz2^CreERT2^ allele creates lysozyme heterozygosity (mitigated by Suppl. Fig. S12).
- **Pharmacological vs physiological hypoxia**: FG-4592 misses HIF-independent hypoxic effects (mitochondrial ROS, lipid changes).
- **In vitro only**: no in-vivo confirmation of the BMDM-vs-TR-AM phenotype in disease models.
- **Myc-rescue scope**: causal Myc-dependence demonstrated only for basal OCR/ATP; cytokine and ribosomal-biogenesis phenotypes not formally rescued.
- **DoRothEA inference**: regulon-footprint inference, not direct ChIP — Myc activity is inferred rather than measured.
- **Mouse-only**: human MDM analogue and human alveolar macrophages not tested.

## Open questions

### Open questions raised by authors

- Does HIF-1α-Myc antagonism explain mitochondrial-OXPHOS / cytokine phenotypes in other macrophage ontogenies?
- Does in-vivo FG-4592 / roxadustat administration in ARDS models recapitulate the ontogeny-divergent effect?
- Why does culture with GM-CSF apparently confer HIF-1α inducibility on TR-AMs (Zhu et al.) — is it proliferation-coupled HIF biology?

### Open questions identified during ingest

- Whether ontogeny-divergent HIF-1α function extends to tumor-associated macrophages of mixed ontogeny — directly relevant to the hypoxia/macrophage thesis.
- Whether scRNA-seq "HIF activity scores" used in pan-cancer macrophage atlases need to be re-interpreted per macrophage cluster's ontogenic origin.
- Whether the c-Myc compensatory axis is exploitable therapeutically (e.g. combined HIF-1α + Myc inhibition to fully suppress recruited-macrophage pro-inflammation in ARDS).

## My take

A focused, mechanistically clean Scientific Reports paper that breaks the "HIF-1α is a generic macrophage master regulator" narrative by explicitly contrasting two macrophage ontogenies in the same paradigm. The causal Myc-rescue is particularly important — it elevates the c-Myc compensation from correlative inference to mechanism. Direct relevance to my thesis hypoxia/macrophage chapters: any inference about HIF-1α activity from scRNA-seq TAM clusters must be stratified by ontogeny, and HIF-stabilising drugs in tumor settings will have ontogeny-asymmetric macrophage effects. Caveat: ScientificReports + Lyz2-CreERT2 partial-deletion model + in-vitro-only — the *direction* of the findings is convincing, the *magnitude* in vivo will need confirmation.

## Related

- [[concepts/ontogeny-divergent-hif1a-macrophage-metabolism]] — central concept introduced.
- [[concepts/c-myc-compensatory-mitochondrial-axis-hif-deficient-bmdm]] — central concept introduced.
- [[concepts/macrophage-ontogeny-resident-vs-monocyte-derived]] — broader ontogeny framework.
- [[concepts/hif-dependent-glycolysis-immune-cell-differentiation]] — refined by this paper.
- [[concepts/warburg-effect-hif1a-glycolytic-reprogramming]] — HIF-1α–Myc axis in cancer cells, analogue.
- [[concepts/tissue-specific-metabolic-programming-macrophages]] — TR-AM niche context.
- [[concepts/m1-macrophage-tca-breaks-itaconate-succinate]] — TCA-cycle metabolite reshaping in inflammatory macrophages.
- [[foundations/hif1a]] / [[foundations/myc-oncogene]] / [[foundations/fg-4592-roxadustat]] / [[foundations/phd-prolyl-hydroxylases]] / [[foundations/dorothea-tf-regulon-analysis]] / [[foundations/seahorse-extracellular-flux-analyzer]] / [[foundations/bone-marrow-derived-macrophage-bmdm]] / [[foundations/tissue-resident-alveolar-macrophage]] / [[foundations/cre-loxp-recombinase-system]] / [[foundations/lps-toll-like-receptor-signaling]] / [[foundations/tnf-tumor-necrosis-factor]] / [[foundations/il-6-cytokine]] / [[foundations/itaconate-metabolite]] / [[foundations/sucnr1-succinate-receptor]] / [[foundations/hk2-hexokinase-2]] / [[foundations/ldh-lactate-dehydrogenase]]
- [[papers/hypoxia-signaling-human-health-diseases-implications]] — broader HIF immunology review.
- [[papers/metabolism-tissue-macrophages-homeostasis-pathology]] — tissue-macrophage metabolism review.
- [[papers/nf-kb-tet2-promote-macrophage-reprogramming]] — HIF1A vs NF-κB in hypoxic BMDMs.
