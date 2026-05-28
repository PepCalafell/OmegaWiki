---
title: "Single-cell spatial transcriptomic analysis of human skin anatomy"
slug: single-cell-spatial-transcriptomic-analysis-human
arxiv: ""
doi: "10.1038/s41588-026-02552-8"
pmid: "41872488"
venue: "Nature Genetics"
year: 2026
authors:
  - Paula Restrepo
  - Alexis Wilder
  - Aubrey E. Houser
  - Harkirat Singh Sandhu
  - Angie Ramirez
  - M. Grace Hren
  - Raman Gill
  - Abiha Kazmi
  - Larry Chen
  - Alexandra Nigro
  - Ichiro Imanishi
  - Deniz Demircioglu
  - Dan Hasson
  - Alan Soto
  - Stephanie McQuillan
  - Edgar Gonzalez-Kozlova
  - Rachel Brody
  - Benjamin Ungar
  - Maria Kasper
  - Catherine P. Lu
  - Philip Torina
  - Jesse M. Lewin
  - Sacha Gnjatic
  - Sai Ma
  - Andrew L. Ji
first_author: "Paula Restrepo"
corresponding_author: "Andrew L. Ji"

source_type: pdf
s2_id: "2698bf5d8e85b13f417c8f2931fb94cd52dbecfb"
date_added: 2026-05-27
ingested_date: 2026-05-27
ingest_version: 1
last_reviewed:

importance: 4
tier: TIER_1
tags: [skin, MERFISH, spatial-transcriptomics, atlas, perivascular, CCL19, TNF, SALT, multicellular-neighborhood, aging, atopic-dermatitis, psoriasis, hidradenitis-suppurativa, SCC, BCC]
keywords: [skin atlas, MERFISH, multicellular neighborhood, PERIVASC I, CCL19, TNF, perivascular fibroblast, SALT, Visium, scRNA-seq integration, crumblr]
domain: cell biology / dermatology / immunology

tissue: [skin]
condition: [healthy, autoimmune, cancer]
disease_specific: [atopic_dermatitis, psoriasis, hidradenitis_suppurativa, squamous_cell_carcinoma_cutaneous, basal_cell_carcinoma, prurigo_nodularis]
species: [human]
hypoxia_relevant: false
contains_immune_cells: true
contains_myeloid: true

techniques: [MERFISH, scRNA-seq_10x, spatial_visium, CellChat, crumblr, variancePartition, dreamlet, Harmony]
n_samples: 114
n_cells_total: 1201886
integration_method: "Harmony / Seurat-style integration of 14 public scRNA-seq studies + simulated PERIVASC I CellChat"

key_cell_types: [Papil_Fib, Retic_Fib_I, Retic_Fib_II, Perivasc_Fib_I_CCL19, Perivasc_Fib_II, perineural_Fib, dermal_papilla, dermal_sheath, pericyte, VEC, HEC, LEC, smooth_muscle, Schwann, adipocyte, Bas_KC, Spn_KC_I, Spn_KC_II, Grn_KC, ORS_basal, ORS_suprabasal, bulge, IRS_HS, melanocyte, Langerhans_cell, CD4_TH, CD4_Treg, CD8_TC, naive_T, mast_cell, macrophage, monocyte, CD1C_DC, CCR7_DC, CLEC9A_DC, plasma_cell, eccrine_gland, eccrine_duct, eccrine_myoepi]
key_markers: [CCL19, CXCL12, CXCR4, CCR7, TNF, TNFRSF1A, MIF, CD74, MDK, PTN, NCL, S100A8, SOX9, GJB2, GJB6, ANGPTL7, PRG4, COMP, APOE, C3, CXCL13, MMP1, MMP3, POSTN, TNC]
key_pathways: [TNF-CCL19_perivascular_axis, CXCL12-CXCR4, MIF-CD74, MDK-CD74, PTN-NCL, TNF-TNFRSF1A, IL-17_inflammatory_program, MHC_class_I_II_antecubital]

projects: [thesis, skin]
priority: core
read_status: deep_read

hypoxiaverse_status:
exclusion_reason:
data_availability: "MERFISH and Visium data released alongside Nat Genet 2026 publication (see paper supplement for accession identifiers)."

code_url: ""
cited_by: []
---

## Problem

The skin is the largest human organ and a major site of disease burden, yet how its ~45 cell types are spatially organised across the body plan, how that organisation changes with age, and how it is disrupted in disease has remained poorly characterised. Earlier scRNA-seq studies provided cell-type catalogues without spatial context; bulk transcriptomics could not resolve cellular composition; positional-memory studies in cultured fibroblasts were hard to interpret in vivo. A coherent, organ-wide spatial reference of human skin was missing.

## Key idea

Build an organ-wide MERFISH atlas of normal adult skin spanning 15 anatomic sites, integrate it with a 14-study public scRNA-seq reference and a multi-disease Visium ST cohort, and use this to (i) catalogue 45 cell types in situ, (ii) define ten reproducible multicellular spatial neighborhoods, (iii) discover stereotyped centrifugal and flexural compositional gradients, (iv) reveal a perivascular CCL19+ niche (PERIVASC I) as the physical correlate of SALT, sustained by a TNF→CCL19 stromal-immune loop, and (v) demonstrate pan-disease PERIVASC I expansion and remodeling across AD, psoriasis, HS, BCC and SCC.

## Method

- **MERFISH atlas**: 1,201,886 cells from 114 samples / 22 donors / 15 anatomic sites profiled on Vizgen [[foundations/merscope-vizgen]] [[foundations/merfish-imaging-spatial]] using a 500-gene panel; baysor-style segmentation; cell-type calling cross-referenced with an integrated scRNA-seq reference.
- **Integrated scRNA-seq reference**: 286,000 cells from 14 public studies (93 samples / 85 donors) harmonised via [[foundations/harmony-integration]] and Seurat-style integration to define a 45-cell-type label set, including 8 fibroblast subsets.
- **Multicellular neighborhood discovery**: cells clustered by neighbor-cell-type composition yielding 10 reproducible neighborhoods (N0 DEJ, N1 PERIVASC I, N2 DIFF IFE, N3 PERIVASC II, N4 STROMA, N5 UPPER HF, N6 ECCRINE, N7 SEB GLAND, N8 SUBCUTIS, N9 LOWER HF).
- **Compositional statistics**: cell-type abundance shifts modelled via [[foundations/crumblr-cell-composition]] mixed linear models with variance partitioning over site, donor, sex, age and technical factors.
- **Cell-cell communication**: [[foundations/cellchat-cell-cell-communication]] L-R inference on (a) MERFISH PERIVASC I cells directly and (b) simulated PERIVASC I composition derived from the integrated scRNA-seq reference for transcriptome breadth.
- **Disease integration**: [[foundations/10x-visium-spatial-transcriptomics]] datasets from 5 skin diseases (AD, psoriasis, HS, BCC, SCC) + normal scar; 142,515 spots over 63 donors. Visium spots labelled by reference-based neighborhood prediction using the MERFISH atlas as anchor.
- **Aging analysis**: site-restricted abdomen subset (n=13 donors) used to remove site confounding; Spearman correlation of neighborhood proportions and cell-type abundances with donor age.

## Results

1. MERFISH resolves 45 cell types across 15 anatomic sites, including 8 fibroblast subsets (papillary, reticular I/II, perivascular I/II, perineural, DP-like, dermal sheath) and identifies CCL19+ Perivasc Fib I localising specifically to perivascular space.
2. Spinous keratinocyte cluster II is enriched in scalp and sole with an infundibular-like S100A8/SOX9/GJB2/GJB6 program.
3. Cellular diversity and density rise centrifugally from trunk toward extremities; flexural sites exceed neighboring extensor sites; face and sole are compositional outliers.
4. Anatomic sites cluster into compositional families (flexural / extensor / trunk / scalp / face / sole) with site explaining the dominant share of cell-type-abundance variance.
5. Innate immune cells (Mono, Mac, DCs) enrich in extremities; T cells enrich specifically in antecubital fossa (and to a lesser extent popliteal fossa).
6. Ten reproducible multicellular neighborhoods (N0–N9) define skin spatial architecture across all sites; PERIVASC I has highest diversity and most immune content.
7. In abdominal skin (n=13), age correlates with STROMA decline (ρ = −0.70, P = 0.0083) and PERIVASC II expansion (ρ = 0.70, P = 0.0076); Retic Fib I declines while HEC, VEC, pericytes and SM increase.
8. CellChat: PERIVASC I has the highest interaction volume and most unique pathways (MIF, MK, CXCL/CCL, TNF). Top stromal→immune pairs: CXCL12-CXCR4, MDK-CD74, MIF-CD74, PTN-NCL. Top immune→stromal: PPIA-BSG, NAMPT-ITGA5+ITGB1, TNF-TNFRSF1A.
9. TNF is proposed as the keystone immune-derived signal maintaining CCL19 expression in perivascular fibroblasts, closing a homeostatic FRC-like loop.
10. Visium ST integration of 5 skin diseases reveals pan-disease PERIVASC I expansion; CCL19+ pro-inflammatory disease-fibroblasts map to PERIVASC I; disease-specific sub-states (TLS, TLS-like, KC stress, HS tunnel, BCC tumor) emerge alongside the homeostatic ten-neighborhood scheme.
11. Papillary fibroblast abundance correlates with epidermal thickness (ρ = 0.26, P = 0.012); Retic Fib II distributes diffusely through sole dermis.

## All claims (exhaustive)

- `[c01]` MERFISH atlas of ~1.2M cells across 15 sites, 114 samples, 22 donors (p.1) "an organ-wide single-cell spatial atlas of ~1.2 million cells from normal adult human skin, resolving the location of 45 cell types across 114 samples encompassing 15 anatomic sites" — confidence: high — type: quantitative — links: [[foundations/merfish-imaging-spatial]] [[concepts/organ-wide-merfish-skin-atlas]] [[claims/skin-atlas-12m-cells-15-sites-merfish]]
- `[c02]` Integrated scRNA-seq reference of 286k cells from 14 public studies (Fig.1a) "Public data scRNA-seq 286,000 cells (14 studies) 93 samples (85 donors)" — confidence: high — type: methodological — links: [[foundations/harmony-integration]] [[concepts/organ-wide-merfish-skin-atlas]] [[claims/integrated-scrnaseq-skin-reference-286k-cells]]
- `[c03]` 45 cell types resolved spatially including 8 fibroblast subpopulations (p.2) "we characterized 15 stromal subpopulations ... We identified eight fibroblast subpopulations—papillary (Papil Fib), two reticular (Retic Fib I and Retic Fib II), two perivascular (Perivasc Fib I and Perivasc Fib II), perineural, dermal papilla (DP)-like and dermal sheath (DS) subsets" — confidence: high — type: correlational — links: [[concepts/organ-wide-merfish-skin-atlas]] [[claims/skin-45-cell-types-resolved-spatially]]
- `[c04]` Spn KC II enriched in scalp and sole, infundibular-like signature (p.2) "Spn KC II was most prominent in the scalp and sole and displayed an elevated infundibular-like (S100A8, SOX9, GJB2 and GJB6) gene expression profile" — confidence: medium — type: correlational — links: [[claims/spn-kc-ii-scalp-sole-infundibular-like]]
- `[c05]` CCL19+ Perivasc Fib I localises near vasculature (p.2) "MERFISH localized all fibroblast groups, including previously described CCL19+ Perivasc Fib I fibroblasts near vasculature" — confidence: high — type: mechanistic — links: [[foundations/ccl19-chemokine]] [[concepts/perivascular-immune-stromal-niche-skin-salt]] [[claims/ccl19-perivasc-fib-i-near-vasculature-skin]]
- `[c06]` Centrifugal diversity and density gradient across the body plan (p.3) "centrally located body sites (buttocks, abdomen and back) were low in diversity, suggesting diversity increases centrifugally from central to peripheral sites" — confidence: high — type: correlational — links: [[concepts/centrifugal-cellular-diversity-gradient-skin]] [[claims/centrifugal-diversity-density-skin]]
- `[c07]` Sites cluster into compositional families (flexural / extensor / trunk / scalp); face and sole are unique (p.5) "anatomic sites exhibited similar compositional patterns within flexural ... extensor ... trunk ... or scalp sites, while face and sole were unique" — confidence: high — type: correlational — links: [[concepts/centrifugal-cellular-diversity-gradient-skin]] [[claims/anatomic-site-categories-similar-composition]]
- `[c08]` Innate immune cells enriched in extremities (p.5) "innate immune cells such as monocytes, macrophages and DC subsets appeared strongly enriched in the extremities" — confidence: medium — type: correlational — links: [[claims/innate-immune-extremity-enrichment-skin]]
- `[c09]` T-cell enrichment in antecubital (and weakly popliteal) fossa (p.5) "T cell subsets were distinctly enriched in antecubital fossa and to a lesser extent the popliteal fossa, divergent from elbow and knee patterns" — confidence: medium — type: correlational — links: [[claims/tcell-antecubital-fossa-enrichment-skin]]
- `[c10]` Ten multicellular neighborhoods define skin architecture (Fig. 3, p.6) "Multicellular spatial neighborhoods define cell composition and localization ... N0: DEJ, N1: PERIVASC I, N2: DIFF IFE, N3: PERIVASC II, N4: STROMA, N5: UPPER HF, N6: ECCRINE, N7: SEB GLAND, N8: SUBCUTIS, N9: LOWER HF" — confidence: high — type: methodological — links: [[concepts/skin-multicellular-spatial-neighborhoods]] [[claims/ten-multicellular-neighborhoods-skin]]
- `[c11]` PERIVASC I has highest diversity and immune enrichment (p.8) "focusing on PERIVASC I, given its high diversity and immune enrichment (Fig. 3c,d)" — confidence: high — type: correlational — links: [[concepts/perivascular-immune-stromal-niche-skin-salt]] [[claims/perivasc-i-highest-diversity-immune-enriched]]
- `[c12]` STROMA declines with age in abdomen (Spearman = −0.70, P = 0.0083) (p.8) "Age was associated with decreased STROMA (Spearman = −0.70) and increased PERIVASC II (Spearman = 0.70) abundance" — confidence: high — type: quantitative — links: [[concepts/age-stroma-to-perivasc-fibroblast-shift]] [[claims/age-stroma-decreases-abdomen-skin]]
- `[c13]` PERIVASC II rises with age in abdomen (Spearman = 0.70, P = 0.0076) (p.8) "Age was associated with decreased STROMA (Spearman = −0.70) and increased PERIVASC II (Spearman = 0.70) abundance" — confidence: high — type: quantitative — links: [[concepts/age-stroma-to-perivasc-fibroblast-shift]] [[claims/age-perivasc-ii-increases-abdomen-skin]]
- `[c14]` Retic Fib I declines and vascular cells expand with age (p.8) "Retic Fib I—the major STROMA constituent—declined with age, whereas HEC, VEC, pericytes and smooth muscle cells, which define PERIVASC II, increased" — confidence: medium — type: correlational — links: [[concepts/age-stroma-to-perivasc-fibroblast-shift]] [[claims/retic-fib-i-declines-age-abdomen]]
- `[c15]` TNF maintains CCL19 in perivascular fibroblasts (p.11) "Within, we show that TNF is key to sustaining CCL19 expression in perivascular fibroblasts" — confidence: medium — type: mechanistic — links: [[foundations/tnf-tumor-necrosis-factor]] [[foundations/ccl19-chemokine]] [[concepts/tnf-ccl19-perivascular-fibroblast-axis]] [[claims/tnf-sustains-ccl19-perivasc-fibroblast]]
- `[c16]` Top stromal→immune PERIVASC I L-R pairs CXCL12-CXCR4, MDK-CD74, MIF-CD74, PTN-NCL (p.8) "Top stromal-to-immune L–R pairs in PERIVASC I included CXCL12–CXCR4, MDK–CD74, MIF–CD74 and PTN–NCL (Fig. 5c)" — confidence: medium — type: methodological — links: [[foundations/cellchat-cell-cell-communication]] [[foundations/cxcl12-chemokine]] [[claims/perivasc-i-stromal-immune-lr-pairs]]
- `[c17]` Top immune→stromal PERIVASC I L-R pairs PPIA-BSG, NAMPT-ITGA5+ITGB1, TNF-TNFRSF1A (p.8) "Conversely, immune-to-stromal interactions involved PPIA-BSG, NAMPT-ITGA5 + ITGB1 and TNF–TNFRSF1A (Fig. 5d)" — confidence: medium — type: methodological — links: [[foundations/tnf-tumor-necrosis-factor]] [[foundations/cellchat-cell-cell-communication]] [[claims/perivasc-i-immune-stromal-lr-pairs]]
- `[c18]` Visium integration of 142,515 spots across 5 skin diseases (Fig. 6, p.10) "Integration of Visium ST n = 63 donors 5 skin diseases k = 142,515 spots" — confidence: high — type: methodological — links: [[foundations/10x-visium-spatial-transcriptomics]] [[foundations/atopic-dermatitis]] [[foundations/psoriasis-disease]] [[foundations/hidradenitis-suppurativa-disease]] [[claims/visium-skin-5-diseases-143k-spots]]
- `[c19]` PERIVASC I expands in inflammatory and neoplastic skin disease (Fig. 6, p.10–11) "Perivascular I neighborhood expansion in disease" — confidence: high — type: correlational — links: [[concepts/cross-disease-perivasc-immune-remodeling-skin]] [[claims/perivasc-i-expansion-inflammatory-skin-disease]]
- `[c20]` Disease CCL19+ fibroblasts map to PERIVASC I (p.11) "CCL19+ 'pro-inflammatory' fibroblasts in inflammatory skin disease mapped primarily to PERIVASC I, which exhibited pathogenic immune expansion and architectural disruption" — confidence: high — type: correlational — links: [[concepts/cross-disease-perivasc-immune-remodeling-skin]] [[foundations/ccl19-chemokine]] [[claims/ccl19-fibroblasts-disease-map-perivasc-i]]
- `[c21]` Disease-enriched spot sub-states TLS, TLS-like, KC stress, HS tunnel, BCC tumor (Fig. 6c-d, p.10) "Disease-enriched spots ... KC stress, BCC tumor, TLS, HS tunnel, TLS-like, NS-mapped" — confidence: medium — type: correlational — links: [[concepts/cross-disease-perivasc-immune-remodeling-skin]] [[claims/disease-enriched-spot-substates-skin]]
- `[c22]` Papil Fib abundance correlates with epidermal thickness (ρ=0.26, P=0.012) (Fig. 4) "Papil Fib abundance ... Epidermis thickness Spearman = 0.26, P = 0.012" — confidence: medium — type: quantitative — links: [[claims/papil-fib-correlates-epidermal-thickness]]
- `[c23]` PERIVASC I = physical correlate of SALT (p.11) "The PERIVASC I neighborhood provides a physical correlate for the conceptual framework of SALT" — confidence: medium — type: mechanistic — links: [[foundations/skin-associated-lymphoid-tissue-salt]] [[concepts/perivascular-immune-stromal-niche-skin-salt]] [[claims/perivasc-i-physical-correlate-salt]]
- `[c24]` Site dominates variance partitioning of cell-type abundance (p.5) "Variance partitioning of demographic and technical covariates confirmed that the cell-type abundances largely varied by anatomic site, while quantifying other sources of variance" — confidence: high — type: methodological — links: [[foundations/crumblr-cell-composition]] [[claims/site-dominates-variance-cell-abundance-skin]]
- `[c25]` Most interactive PERIVASC I cell types: VEC, CD4+ TC, CD8+ TC, Perivasc Fib I/II (p.8) "Within PERIVASC I, the most interactive cell types were VECs, CD4+ cytotoxic T cells, CD8+ cytotoxic T cells and Perivasc Fib I/Perivasc Fib II (Fig. 5a)" — confidence: medium — type: methodological — links: [[foundations/cellchat-cell-cell-communication]] [[claims/perivasc-i-most-interactive-cell-types]]
- `[c26]` PERIVASC I has highest interaction volume and most unique pathways (MIF, MK, CXCL/CCL, TNF) (p.8) "MIF, midkine (MK), CXCL/CCL chemokines and TNF as top PERIVASC I pathways (Fig. 5b) and PERIVASC I and ECCRINE as having the highest interaction volume" — confidence: high — type: methodological — links: [[foundations/tnf-tumor-necrosis-factor]] [[claims/perivasc-i-pathway-volume-leadership]]
- `[c27]` Site-specific MHC class I/II and CD4/CD8 elevation in antecubital fossa (p.11) "increased MHC class I/class II and CD4/CD8 in the antecubital fossa, suggests adaptive inflammatory setpoints at distinct body sites" — confidence: low — type: correlational — links: [[claims/site-specific-lr-mhc-cd4-cd8-antecubital]]
- `[c28]` Disease-associated PERIVASC I shows chemokine/cytokine/ECM remodeling (Fig. 6h-j) "disease-associated increases in chemokines, cytokines and ECM factors, highlighting a key spatial domain for immune recruitment and activity" — confidence: high — type: correlational — links: [[concepts/cross-disease-perivasc-immune-remodeling-skin]] [[claims/disease-perivasc-i-chemokine-cytokine-ecm-remodel]]
- `[c29]` Perivasc Fib I may maintain immune residence via CCL19-CCR7 and CXCL12-CXCR4 (p.11) "Reciprocally, Perivasc Fib I may help maintain immune recruitment and residence (for example, through CCL19–CCR7 and CXCL12–CXCR4), analogous to fibroblastic reticular cells in secondary lymph nodes" — confidence: medium — type: mechanistic — links: [[foundations/ccl19-chemokine]] [[foundations/cxcl12-chemokine]] [[concepts/tnf-ccl19-perivascular-fibroblast-axis]] [[claims/perivasc-fib-i-immune-recruitment-ccl19-cxcl12]]
- `[c30]` Retic Fib II (ANGPTL7+/PRG4+/COMP+) diffuse in sole dermis (p.2) "Retic Fib II (ANGPTL7+/PRG4+/COMP+) previously observed in palmoplantar skin, which localized diffusely throughout the sole dermis" — confidence: medium — type: correlational — links: [[claims/retic-fib-ii-sole-dermis-localization]]

## Discussion captured

### Authors' interpretation

The authors interpret the ten neighborhoods as the architectural units of skin: anatomic site differences and disease phenotypes are best framed as redistribution and remodeling of these neighborhoods, rather than as the appearance of fundamentally new cell types. PERIVASC I is presented as the long-missing physical substrate of the 1983 SALT concept, with a TNF→CCL19 fibroblast axis providing a homeostatic blueprint that disease subsequently amplifies.

### Comparisons with prior literature (made by authors)

- Steele et al. 2025 (Nat Immunol, ref 32) — six-fibroblast taxonomy; the present 8-subset MERFISH catalogue refines and spatially localises that scheme.
- Yu et al. 2024 (Immunity, ref 28) — CCL19+ fibroblasts in HS TLS, here generalised to a pan-disease PERIVASC I expansion.
- Streilein 1983 (ref 38) — SALT proposal, here given a cellular substrate.
- Solé-Boldo et al. 2020 (ref 12) — age-related fibroblast gene-expression decline in inguinal skin; the present work adds numerical Retic Fib I depletion.
- Varani et al. (ref 41) — collagen-production decline with age, now linked to Retic Fib I numerical loss.
- Volar-fibroblast intradermal therapy (ref 6) — motivates dissecting Papil Fib vs Retic Fib II contribution to epidermal thickening.
- CellCharter (ref 37) — analogous spatial-neighborhood methodology in tumours.

### Mechanistic hypotheses proposed

- "TNF is key to sustaining CCL19 expression in perivascular fibroblasts" (p.11).
- "Perivasc Fib I may help maintain immune recruitment and residence (for example, through CCL19–CCR7 and CXCL12–CXCR4), analogous to fibroblastic reticular cells in secondary lymph nodes" (p.11).
- "Additional anatomic site variation of immune-stromal crosstalk molecules ... suggests adaptive inflammatory setpoints at distinct body sites ... potentially lower the threshold for chronic inflammation and disease susceptibility" (p.11).

### Caveats and self-criticism

- MERFISH provides sparse transcriptomes; future work is required to resolve cell-state differences across anatomic sites within a fibroblast subset.
- Lack of donor-matched scalp and sole datasets complicates distinguishing site-specific from donor-specific expression in Spn KC II.
- Age-correlation analysis is restricted to abdomen (n=13) to remove site confounding — extension to other sites is needed.
- Disease integration uses Visium spot resolution rather than MERFISH; therefore neighborhood mapping in disease is reference-based, not direct.

### Future directions suggested

- Dissect Papil Fib vs Retic Fib II contribution to epidermal thickening for refined cellular therapies.
- Test whether anti-TNF biologics reduce CCL19+ perivascular fibroblast abundance.
- Use ten-neighborhood scheme as a template for ex vivo skin organoid reconstruction including adnexa and immune components.
- Investigate adaptive inflammatory setpoints at specific anatomic sites as drivers of site-specific disease predilection.

## Limitations

- 22-donor MERFISH cohort, 500-gene panel — limited transcriptomic depth per cell.
- Cross-sectional aging design; no longitudinal data.
- Visium spot resolution (~55 µm) aggregates cells; PERIVASC I mapping in disease relies on reference inference.
- Causal claims (e.g. TNF→CCL19) rest on CellChat L-R inference, not perturbation.
- Demographic and ethnic representativeness not exhaustive.
- Sole-fibroblast functional contribution unresolved (Papil Fib vs Retic Fib II).

## Open questions

### Open questions raised by authors

- Do site-specific inflammatory setpoints (e.g. antecubital MHC II/CD4 elevation) drive site-specific disease predilection?
- Which fibroblast subset mediates volar-fibroblast-driven epidermal thickening?
- Can anti-TNF therapy reshape CCL19+ perivascular fibroblast biology?
- Can the ten-neighborhood blueprint guide ex vivo skin organoid construction?

### Open questions identified during ingest

- Is PERIVASC I expansion reversible by current biologics (anti-TNF, anti-IL-17, JAK inhibitors) across skin diseases?
- Does PERIVASC I score serve as a transversal disease-activity biomarker for trials?
- How does the centrifugal diversity gradient interact with UV exposure history and ageing?
- Are the ten neighborhoods conserved in mouse skin and across species, enabling animal-model translation?
- Does Retic Fib I loss precede or follow basement-membrane changes with age?

## My take

For my thesis (skin / hypoxia / single-cell context), this paper is a foundational reference. Three things make it immediately useful: (i) the ten-neighborhood vocabulary becomes a shared spatial coordinate system for any future skin study I touch; (ii) PERIVASC I + the TNF→CCL19 axis give a concrete cellular substrate for "skin immunity" that lets me phrase questions about therapy mechanism more precisely; (iii) the centrifugal and flexural compositional gradients impose biopsy-site matching as a rigour requirement for any future lesional/non-lesional analysis I do. The TNF→CCL19 claim is causally underdetermined (inferential CellChat, not perturbational), which makes it a natural target for downstream functional follow-up. The age-related Retic Fib I depletion connects neatly to broader fibroblast-loss themes in tumours and chronic inflammation, opening cross-tissue comparisons.

## Related

- [[foundations/merfish-imaging-spatial]] — primary spatial platform
- [[foundations/10x-visium-spatial-transcriptomics]] — disease arm
- [[foundations/cellchat-cell-cell-communication]] — L-R inference
- [[foundations/harmony-integration]] — scRNA-seq integration
- [[foundations/crumblr-cell-composition]] — compositional statistics
- [[foundations/ccl19-chemokine]]
- [[foundations/cxcl12-chemokine]]
- [[foundations/tnf-tumor-necrosis-factor]]
- [[foundations/skin-associated-lymphoid-tissue-salt]]
- [[foundations/hidradenitis-suppurativa-disease]]
- [[foundations/psoriasis-disease]]
- [[foundations/atopic-dermatitis]]
- [[concepts/organ-wide-merfish-skin-atlas]]
- [[concepts/skin-multicellular-spatial-neighborhoods]]
- [[concepts/perivascular-immune-stromal-niche-skin-salt]]
- [[concepts/tnf-ccl19-perivascular-fibroblast-axis]]
- [[concepts/centrifugal-cellular-diversity-gradient-skin]]
- [[concepts/age-stroma-to-perivasc-fibroblast-shift]]
- [[concepts/cross-disease-perivasc-immune-remodeling-skin]]
- [[papers/spatial-joint-profiling-dna-methylome-transcriptome]] — Sai Ma co-senior, related spatial multi-omics
- [[papers/cellcharter-reveals-spatial-cell-niches-associated]] — neighborhood-discovery methodology in tumours
- [[papers/nico-identifies-extrinsic-drivers-cell-state]] — neighborhood-based cell-state inference
- [[papers/single-cell-spatial-genomics-atlas-human]] — same problem (human skin fibroblast atlas; this paper cites it)
