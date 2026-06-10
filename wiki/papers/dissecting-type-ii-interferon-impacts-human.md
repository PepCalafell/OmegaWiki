---
# === Identification ===
title: "Dissecting type I and II interferon impacts on human immune cells in disease by a cell type-specific interferon response atlas"
slug: "dissecting-type-ii-interferon-impacts-human"
arxiv: ""
doi: "10.64898/2025.12.02.691676"
pmid: ""
venue: "bioRxiv"
year: 2025
authors:
  - Nicholas Moss
  - Catalina Sakai
  - Saransh N. Kaul
  - Lucas T. Graybuck
  - Samir Rachid Zaim
  - Melinda L. Angus-Hill
  - Yudong D. He
  - Erik D. Layton
  - Paige Bouvatte
  - Peter J. Wittig
  - Christian M. La France
  - Tao Peng
  - Marla C. Glass
  - Upaasana Krishnan
  - Aishwarya Chander
  - Erin K. Kawelo
  - Jessica Garber
  - Julian Reading
  - Stephanie D. Anover-Sombke
  - Mary Kwok
  - Damian J. Green
  - Ananda W. Goldrath
  - Mikael Sigvardsson
  - Peter J. Skene
  - Xiao-jun Li
  - Troy R. Torgerson
  - Emma L. Kuan
first_author: "Nicholas Moss"
corresponding_author: "Emma L. Kuan"

# === Source & metadata ===
source_type: pdf
s2_id: ""
date_added: 2026-06-10
ingested_date: 2026-06-10
ingest_version: 1
last_reviewed:

# === Classification ===
importance: 4
tier: TIER_1
tags:
  - interferon
  - ISG
  - single-cell
  - immune-atlas
  - IFN-I
  - IFN-II
  - multiple-myeloma
  - SLE
  - deconvolution
keywords:
  - HIRISA
  - interferon-stimulated genes
  - IFN-α
  - IFN-γ
  - CD14 monocytes
  - NMF scoring
domain: immunology

# === Biomedical domain ===
tissue:
  - blood
  - bone_marrow
condition:
  - healthy
  - cancer
  - autoimmune
disease_specific:
  - multiple_myeloma
  - SLE
  - rheumatoid_arthritis
  - long_COVID
species:
  - human
hypoxia_relevant: false
contains_immune_cells: true
contains_myeloid: true

# === Technique ===
techniques:
  - scRNA-seq_10x
  - CITE-seq
  - flow_cytometry
n_samples: 100
n_cells_total: 1236656
integration_method: ""

# === Biology captured ===
key_cell_types:
  - CD14 monocytes
  - T cells
  - B cells
  - NK cells
  - plasma cells
key_markers:
  - IFI44L
  - ISG15
  - MX1
  - OAS3
  - CXCL9
  - IDO1
  - GBP1
  - STAT1
  - CD300e
key_pathways:
  - type I IFN signaling
  - type II IFN signaling
  - ISGF3
  - GAF/STAT1

# === User project membership ===
projects:
  - thesis
priority: context
read_status: not_read

# === HypoxiaVERSE-specific ===
hypoxiaverse_status:
exclusion_reason:
data_availability: "Interactive web portal: https://apps.allenimmunology.org/aifi/resources/ifn-response/"

# === Cross-references ===
code_url: ""
cited_by: []
---

## Problem

Interferons (IFN-I, IFN-II, IFN-III) orchestrate immune responses, but distinguishing the individual contribution of each IFN type from human transcriptomic data is hard: IFN-I and IFN-III converge on [[isgf3-complex]] to induce overlapping antiviral ISGs (MX, IFIT, OAS), and IFN-γ-driven GAF/STAT1 programs partly overlap as well, especially when IFN-I and IFN-II are co-induced (as in SLE). Existing references aggregate mixed cell types and few datasets span all IFN types across all major immune subsets.

## Key idea

Build a cell-type- and IFN-type-resolved single-cell atlas — HIRISA — by stimulating purified human immune lineages separately with IFN-α2A, IFN-β, IFN-γ, and IFN-λ1, then use the resulting cell-type-specific ISG dictionaries as the basis for an NMF scoring algorithm that deconvolves IFN-I and IFN-II activity per cell type in disease datasets. See [[hirisa-human-interferon-response-immune-subsets]], [[ifn-ifn-ii-activity-deconvolution-scoring]].

## Method

PBMCs from 5 healthy donors were negatively selected into CD14 monocytes, T, B, and NK cells (>90% purity), each stimulated for 21h with IFN-α2A, IFN-β, IFN-γ, or IFN-λ1, or left unstimulated. ~1.23M cells from 100 samples on the 10x Flex platform passed QC, resolving 13 L2 subsets ([[scrna-seq-10x-chromium]], [[umap-dimensionality-reduction]]). Per-donor unstimulated cells served as the baseline in a bootstrapped N-of-1 differential-expression framework; shared DEGs across donors gave mean fold changes per IFN. Whole-PBMC IFN-α stimulation (4 donors) was annotated by [[seurat-v3-integration]] label transfer to assess bystander effects. Flow cytometry validated protein-level changes. A scoring algorithm computed FCs of ~1,174 HIRISA ISGs vs controls and applied [[nmf-non-negative-matrix-factorization]] to derive per-cell-type IFN-α and IFN-γ scores, applied to NDMM cohorts and seven public disease datasets, and exposed via an interactive web tool.

## Results

HIRISA resolves conserved core and subset-specific ISG programs across 13 subsets. CD14 monocytes show the most extensive remodeling for both IFN-I and IFN-II. IFN-α and IFN-β are nearly interchangeable; circulating IFN-λ1 responses are a restricted subset of the IFN-I program confined to B cells and select T cells. IFN-γ responses are largely monocyte- and B-cell-restricted (tracking IFNGR2), with IDO1/CXCL9 as monocyte biomarkers. The NMF scoring framework distinguishes IFN-I from IFN-II activity in NDMM (both elevated; VRd suppresses IFN-I only), and across diseases ranks autoimmune > myeloma > infection > aging for IFN-α; SLE flare shows T-cell IFN-γ elevation and disrupted IFN-I/IFN-II coordination; long COVID is IFN-γ-dominant/IFN-α-suppressed.

## All claims (exhaustive)

- `[c1]` HIRISA is a single-cell atlas of IFN-α/β/γ/λ1 responses across 13 human immune subsets (~1.23M cells, 5 donors) (p.4) "1,236,656 cells from 100 samples passed quality control" — confidence: high — type: methodological — links: [[claims/hirisa-single-cell-atlas-ifn-responses]] [[concepts/hirisa-human-interferon-response-immune-subsets]] [[foundations/scrna-seq-10x-chromium]]
- `[c2]` CD14 monocytes show the most extensive transcriptional remodeling to interferon among circulating subsets (p.3, p.6) "CD14 monocytes exhibiting the most extensive transcriptional remodeling" — confidence: high — type: correlational — links: [[claims/cd14-monocytes-show-most-extensive-transcriptional]] [[concepts/core-versus-subset-specific-isg-programs]]
- `[c3]` A conserved IFN-I antiviral ISG signature is induced across all immune cell types (p.4) "a conserved IFN-I signature (IFI44L, ISG15, LY6E, TAP1) was strongly induced across cell types" — confidence: high — type: mechanistic — links: [[claims/conserved-ifn-antiviral-isg-signature-induced]] [[foundations/type-interferon-ifna-ifnb]] [[foundations/isgf3-complex]]
- `[c4]` IFN-α and IFN-β induce near-identical transcriptomic programs across all 13 subsets (p.5) "FCs of shared genes were nearly identical between IFN-α and IFN-β across all 13 subsets" — confidence: high — type: quantitative — links: [[claims/ifn-alpha-ifn-beta-induce-near]] [[foundations/type-interferon-ifna-ifnb]]
- `[c5]` Circulating IFN-λ1 responses are restricted to B cells and select T cells, with no uniquely IFN-λ1-induced genes (p.5) "no genes uniquely induced by IFN-λ1" — confidence: high — type: correlational — links: [[claims/circulating-ifn-lambda1-response-restricted-cells]]
- `[c6]` IFN-γ transcriptomic responses are restricted to CD14 monocytes and B cells, tracking IFNGR2 (p.6) "IFN-γ–driven transcriptomic changes were largely restricted to CD14 monocytes and B cells" — confidence: high — type: correlational — links: [[claims/ifn-gamma-response-restricted-cd14-monocytes]] [[foundations/ifn-gamma-cytokine]]
- `[c7]` CD14 monocytes are the dominant IFN-γ responder with 792 DEGs (600 unique) (p.6) "CD14 monocytes exhibited the most extensive response, with 792 DEGs, including 600 unique to this subset" — confidence: high — type: quantitative — links: [[claims/cd14-monocytes-dominant-ifn-gamma-responder]] [[foundations/stat1-tf]]
- `[c8]` IFN-γ drives M1-like polarization in CD14 monocytes (p.6) "upregulated genes associated with proinflammatory and anti-tumor functions (CXCL9, CD40, FCGR1A, SLAMF7) ... downregulating M2-like and tumor-promoting markers (THBS1, CD163, CD36, FN1)" — confidence: medium — type: mechanistic — links: [[claims/ifn-gamma-drives-m1-like-polarization]] [[foundations/ifn-gamma-cytokine]] [[foundations/cxcl9-chemokine]]
- `[c9]` IDO1 and CXCL9 are monocyte-specific biomarkers of IFN-γ activity (p.6-7) "IDO1 and CXCL9 were among the top IFN-γ–induced genes and were uniquely upregulated in CD14 monocytes, identifying them as robust biomarkers of IFN-γ activity" — confidence: high — type: methodological — links: [[claims/ido1-cxcl9-monocyte-biomarkers-ifn-gamma]] [[foundations/cxcl9-chemokine]] [[foundations/cxcl10-chemokine]]
- `[c10]` CD300e is upregulated by IFN-α but downregulated by IFN-γ at RNA and protein levels (p.7) "CD300e ... was upregulated by IFN-α but downregulated by IFN-γ at both RNA and protein levels ... suggesting antagonistic regulation" — confidence: medium — type: mechanistic — links: [[claims/cd300e-antagonistic-regulation-ifn-versus-ifn]]
- `[c11]` IFNAR abundance does not predict IFN-I response magnitude, unlike IFNGR2/IFNLR1 for IFN-II/III (p.4) "receptor abundance did not predict IFN-I response magnitude. IFN-γ responses correlated with IFNGR2 expression and IFN-λ1 responses with IFNLR1" — confidence: medium — type: correlational — links: [[claims/ifn-receptor-abundance-does-predict-ifn]] [[foundations/type-interferon-ifna-ifnb]]
- `[c12]` Enriched-population stimulation yields more consistent IFN-α signatures by minimizing bystander activation (p.4) "independent stimulation of enriched populations yields more consistent and physiologically relevant IFN-α signatures by minimizing bystander activation" — confidence: medium — type: methodological — links: [[claims/enriched-stimulation-reduces-bystander-activation-ifn]]
- `[c13]` An NMF scoring algorithm built on HIRISA separates IFN-I and IFN-II activity per cell type (p.7-8) "non-negative matrix factorization was used to derive IFN-α and IFN-γ coefficients, referred to as IFN-α and IFN-γ scores per cell type" — confidence: high — type: methodological — links: [[claims/nmf-scoring-algorithm-separates-ifn-ifn]] [[concepts/ifn-ifn-ii-activity-deconvolution-scoring]] [[foundations/nmf-non-negative-matrix-factorization]]
- `[c14]` NDMM shows systemic and bone-marrow elevation of both IFN-I and IFN-II responses (p.7, p.9) "broad elevation of IFN-I scores across B, T, NK, and CD14 monocytes ... Both IFN-I and IFN-II responses were increased across all major immune cell subsets" — confidence: medium — type: correlational — links: [[claims/newly-diagnosed-multiple-myeloma-shows-systemic]]
- `[c15]` Induction therapy (VRd) selectively suppresses IFN-I but not IFN-II in myeloma (p.8) "induction therapy, particularly VRd, attenuates systemic IFN-I activity ... IFN-γ scores ... remained unchanged after VRd and DVRd" — confidence: medium — type: pharmacological — links: [[claims/induction-therapy-vrd-suppresses-ifn-ifn]]
- `[c16]` Autoimmune cohorts show the strongest IFN-α responses across the disease atlas (p.8-9) "Autoimmune diseases showed the strongest IFN-α responses, followed by myeloma, infection, and aging" — confidence: medium — type: correlational — links: [[claims/autoimmune-diseases-show-strongest-ifn-alpha]] [[concepts/ifn-ifn-ii-activity-deconvolution-scoring]]
- `[c17]` SLE flare shows elevated IFN-γ scores in T cells versus managed disease (p.9) "flare cases (n = 14) exhibited higher IFN-γ scores in T cells than managed cases (n = 10; p = 0.001)" — confidence: medium — type: quantitative — links: [[claims/sle-flare-shows-elevated-ifn-gamma]] [[foundations/ifn-gamma-cytokine]]
- `[c18]` SLE flare disrupts coordination between IFN-I and IFN-II responses (p.9) "significant negative correlations were detected in B cells, monocytes, and T cells during SLE flare ... indicating disrupted coordination between IFN-I and IFN-II responses" — confidence: medium — type: correlational — links: [[claims/sle-flare-disrupts-coordination-between-ifn]]
- `[c19]` Long COVID shows IFN-γ-dominant but IFN-α-suppressed signaling (p.9) "Long COVID patients (n = 8) showed elevated IFN-γ scores in B cells (p = 0.04) and CD14 monocytes (p = 0.02) ... markedly reduced IFN-α activity" — confidence: medium — type: quantitative — links: [[claims/long-covid-shows-ifn-gamma-dominant]]

## Discussion captured

### Authors' interpretation

The authors argue HIRISA confirms canonical core ISGs (OAS3, IFI44L, ISG15) while revealing extensive, previously underappreciated cell-type-specific IFN responses with lower fold changes, and that the full transcriptomic landscape refines the long-standing problem of distinguishing IFN-I from IFN-II in human data. CD14 monocytes are highlighted as the strongest IFN-I/IFN-II responders with many unique ISGs linked to antigen presentation and inflammation. They interpret declining IFN-I after myeloma induction therapy as reflecting reduced IFN-α production with tumor regression, and low IFN-I in MGUS as evidence that IFN-α upregulation arises during malignant transformation (supporting IFN-based stratification).

### Comparisons with prior literature (made by authors)

Authors contrast HIRISA with MSigDB-style aggregate references that mix cell types. They compare their NDMM bone-marrow findings to Zavidij et al. (ref 36), confirming similar IFN scores but higher monocyte IFN-γ in their data, and use Zavidij's MGUS/SMM/MM cohort for progression analysis. SLE/RA (refs 37, 38), infection datasets (influenza, SARS-CoV-2, long COVID, malaria; refs 39–41), and aging (ref 31) anchor the cross-disease comparison. They note IFN-α's prior discontinued use in MM therapy due to toxicity (ref 43).

### Mechanistic hypotheses proposed

- Chronic or spatially restricted IFN-γ signaling in the marrow may contribute to immune dysregulation and treatment resistance in myeloma (p.10).
- Impaired balance between IFN-I and IFN-II pathways, particularly in memory T and B cells, may underlie immune dysregulation during SLE flare (p.9).
- TBX21 (T-bet) induction by IFN-γ in memory B cells suggests IFN-γ-driven atypical memory B-cell differentiation (p.6).

### Caveats and self-criticism

Authors note IFN-γ scores correlate only weakly/non-significantly with circulating IFN-γ (likely low systemic abundance), considerable inter-donor heterogeneity (especially monocytes), small disease cohort sizes, and that concordance between IFN-regulated genes and proteins was assessed mainly in monocytes — extension to other cell types is needed.

### Future directions suggested

Spatial transcriptomic and proteomic studies of bone marrow to define IFN-γ dynamics in the myeloma niche; longitudinal profiling to delineate stage-specific IFN contributions to autoimmunity; extension to tissue-resident populations (macrophages, fibroblasts, memory T cells).

## Limitations

- Circulating immune cells only; no tissue-resident populations.
- In-vitro stimulation at fixed concentrations and a single 21h timepoint.
- Healthy donors only for the atlas (n=5); disease applications rely on small, heterogeneous public cohorts.
- RNA–protein concordance validated mainly in CD14 monocytes.
- Cross-cohort batch effects only partially mitigated.

## Open questions

### Open questions raised by authors

- How does IFN signaling behave in tissue-resident immune and non-immune cells?
- What is the functional role of persistent/marrow IFN-γ in myeloma progression and treatment resistance?
- Can stage-specific IFN-I/IFN-II contributions to autoimmune pathogenesis be resolved longitudinally?

### Open questions identified during ingest

- How robust is the NMF deconvolution on bulk-only data lacking cell-type resolution?
- Do the monocyte-unique IFN-γ programs (e.g., IDO1/CXCL9, M1-like) map onto tumor-resident IFN-γ macrophage states described elsewhere in the vault?
- What sets IFN-I response magnitude if not receptor abundance?

## My take

The reusable asset here is the cell-type-resolved ISG dictionaries plus the NMF deconvolution that turns them into a standardized IFN-I-vs-IFN-II measurement instrument across diseases — directly relevant to interpreting monocyte/macrophage IFN states. The disease findings (selective IFN-I suppression by myeloma induction therapy; IFN-γ-driven lupus flare; IFN-γ-dominant long COVID) are intriguing but rest on small cohorts and should be treated as hypothesis-generating.

## Related

- [[hirisa-human-interferon-response-immune-subsets]] — the atlas resource introduced here
- [[ifn-ifn-ii-activity-deconvolution-scoring]] — the NMF scoring framework
- [[core-versus-subset-specific-isg-programs]] — conceptual framing of the ISG response
- [[donor-baseline-interferon-signaling-heterogeneity]] — inter-donor IFN baseline variation observed here
- Related tumor biology: the IFN-γ-driven CXCL9+ monocyte/M1 program here parallels the IFN-γ CXCL9+ TAM state described in tumor atlases (see concepts/ifng-mac-cxcl9-tam-ici-responder), connected via [[foundations/cxcl9-chemokine]] and [[foundations/ifn-gamma-cytokine]]
- People: [[nicholas-moss]], [[emma-kuan]], [[ananda-goldrath]]
