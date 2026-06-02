---
# === Identification ===
title: "Chemokine-defined macrophage niches establish spatial organization of tumor immunity"
slug: chemokine-defined-macrophage-niches-establish-spatial
arxiv: ""
doi: "10.1038/s41590-026-02445-2"
pmid: ""
venue: "Nature Immunology"
year: 2026
authors:
  - Soubhik Ghosh
  - Xin Li
  - Kavita Rawat
  - Aishwarya Dighal
  - Stephanie Kalinowski
  - Reza Hosseini
  - Fred W. Kolling
  - Carol S. Ringelberg
  - Claudia V. Jakubzick
first_author: "Soubhik Ghosh"
corresponding_author: "Claudia V. Jakubzick"

# === Source & metadata ===
source_type: pdf
s2_id: ""
date_added: 2026-06-02
ingested_date: 2026-06-02
ingest_version: 1
last_reviewed:

# === Classification ===
importance: 4
tier: TIER_1
tags:
  - macrophage
  - interstitial-macrophage
  - chemokine
  - tertiary-lymphoid-structure
  - spatial-transcriptomics
  - tumor-immunology
  - lung-cancer
  - monocyte-derived-dc
keywords:
  - CD206hi interstitial macrophage
  - recruited macrophage
  - CXCL13
  - CCL2
  - CCR5
  - maraviroc
  - tertiary lymphoid structure
  - Xenium spatial transcriptomics
domain: immunology

# === Biomedical domain ===
tissue:
  - lung
condition:
  - cancer
disease_specific:
  - lung_adenocarcinoma
  - melanoma_lung_metastasis
species:
  - mouse
hypoxia_relevant: false
contains_immune_cells: true
contains_myeloid: true

# === Technique ===
techniques:
  - scRNA-seq_10x
  - spatial_xenium
  - flow_cytometry
  - immunohistochemistry
  - ELISA
n_samples: 4
n_cells_total:
integration_method: ""

# === Biology captured ===
key_cell_types:
  - CD206hi interstitial macrophage
  - CD206lo interstitial macrophage
  - recruited macrophage (recMac)
  - alveolar macrophage
  - monocyte-derived dendritic cell (moDC)
  - B cell
  - T cell
key_markers:
  - Mrc1 (CD206)
  - Folr2
  - Cd163
  - Mmp9
  - Mmp12
  - Cxcl13
  - Cxcl9
  - Cxcl10
  - Ccl2
  - Fn1
  - Vcan
  - Spp1
  - Arg1
  - Cd274 (PD-L1)
  - Ccr5
  - Ccr2
  - Pf4
key_pathways:
  - CCL2-CCR2 monocyte recruitment
  - CCR5-CCL5 moDC migration
  - CXCL13/CXCL9/CXCL10 lymphocyte recruitment
  - tertiary lymphoid structure formation

# === User project membership ===
projects:
  - thesis
priority: context
read_status: read

# === HypoxiaVERSE-specific ===
hypoxiaverse_status:
exclusion_reason:
data_availability: ""

# === Cross-references ===
code_url: ""
cited_by: []
---

## Problem

Macrophages are among the most abundant immune cells in solid tumors, yet how macrophage **lineage** and **spatial organization** shape antitumor immunity is unclear. Canonical surface markers (CD11c, CD11b, CD64, CD88, CD206, MHCII) are shared across interstitial macrophages (IMs) and monocyte-derived recruited macrophages (recMacs), and CD206 (Mrc1) — widely used as an "M2-like" pro-tumor marker — is neither macrophage-restricted nor predictive of function. This makes it hard to assign pro- vs antitumor roles to specific macrophage states in vivo.

## Key idea

In lung cancer there is a **spatially organized division of labor** among chemokine-defined macrophage subsets. Tissue-resident **CD206hi IMs** (Folr2⁺Cd163⁺Mmp9⁺), positioned along bronchovascular and pleural regions, produce **CXCL13/CXCL9/CXCL10** to recruit lymphocytes and build **tertiary lymphoid structures (TLS)** that control tumors. **CD206lo IMs** and **Ly6c2⁺Fn1⁺Vcan⁺ recMacs**, positioned within tumor regions, express protumor programs; **IM-derived CCL2** recruits recMacs, and Ly6C⁺ **moDCs** migrate to draining lymph nodes via **CCR5** to suppress antitumor immunity. Function is best predicted by **anatomical niche + transcriptional state**, not surface markers.

## Method

- **scRNA-seq** of flow-sorted extravascular CD64⁺CD11b⁺ mononuclear phagocytes from B16F10 melanoma-bearing lungs (two datasets; 23 immune populations) to resolve AMs, CD206hi/CD206lo IMs, recMacs and DCs.
- **Genetic depletion** of CD206hi IMs with **Pf4Cre Cx3cr1DTR** mice (intersectional DT-receptor expression) across B16F10 melanoma, KPAR1.3 transplanted adenocarcinoma, and **AgerCreERT2KP** spontaneous lung adenocarcinoma (with BM chimeras for hematopoietic-restricted depletion).
- **10x Xenium** subcellular spatial transcriptomics (targeted panel) on melanoma- and adenocarcinoma-bearing lungs + a draining lymph node internal control.
- **Compartment-resolved chimeras**: irradiation vs **busulfan** conditioning with WT or **Ccl2⁻ᐟ⁻** BM to separate resident-IM CCL2 from recruited/endothelial CCL2; competitive **Ccr2⁻ᐟ⁻:Ccr5⁻ᐟ⁻ (80:20)** chimeras to remove CCR5 selectively from monocyte-derived cells.
- **Pharmacology**: transient CCR5 blockade with **maraviroc** during DC-based neoantigen (peptide + poly(I:C)) vaccination; ELISA and IHC readouts.

## Results

- CD206hi IMs express Cxcl13/Cxcl9/Cxcl10; CD206lo IMs and recMacs express Ccl2, with recMacs enriched for Spp1/Vegfa/Arg1/Cd274 (PD-L1).
- Depleting CD206hi IMs increased tumor burden ~3.7× (melanoma), 7.2× (KPAR1.3), 2.3× (spontaneous), reduced B/T aggregates ~80%, abolished TLS, and lowered lung CXCL9/CXCL10/CXCL13 protein.
- Xenium: CD206hi IMs line airways/pleura with Cxcl13; CD206lo IMs and recMacs (≈60–71% of tumor macrophages) fill tumor cores/margins; AMs are excluded from tumors.
- IM-derived CCL2 (not endothelial/recMac/DC) is the dominant, nonredundant driver of recMac recruitment (busulfan vs irradiation Ccl2⁻ᐟ⁻ chimeras; ~10.8× tumor reduction with Ccl2⁻ᐟ⁻ BM).
- CCR5 loss in monocyte-derived cells reduced metastases 6.8× (melanoma) / 9.3× (adenocarcinoma); maraviroc selectively/transiently blocked antigen-bearing moDC migration (~76%) and boosted neoantigen-vaccine efficacy (7.5× vs unvaccinated; 3.1× vs vaccine alone).

## All claims (exhaustive)

- `[c01]` CD206hi IMs, CD206lo IMs and recMacs form a functional division of labor in lung cancer (p.2) "we uncovered a division of labor between tissue-resident CD206hi and CD206lo interstitial macrophage (IM) subsets and Ly6c2+Fn1+Vcan+ recruited macrophages (recMacs) in lung cancer" — confidence: high — type: mechanistic — links: [[concepts/chemokine-defined-interstitial-macrophage-division-of-labor]] [[claims/cd206hi-ims-cd206lo-ims-recmacs-form]]
- `[c02]` CD206hi IMs express antitumorigenic chemokines CXCL13, CXCL9, CXCL10 (p.2) "CD206hi IMs predominantly expressed antitumorigenic chemokines, including Cxcl13, Cxcl9 and Cxcl10" — confidence: high — type: correlational — links: [[foundations/cxcl13-chemokine]] [[concepts/cd206hi-im-bronchovascular-chemokine-tls-niche]] [[claims/cd206hi-interstitial-macrophages-express-antitumorigenic-chemokines]]
- `[c03]` recMacs express protumorigenic Spp1, Vegfa, Arg1, PD-L1 and CCL2 (p.2) "Fn1+Vcan+ recMacs were further enriched for canonical tumor-promoting transcripts, such as Spp1, Vegfa, Arg1 and Cd274 (which encodes PD-L1)" — confidence: high — type: correlational — links: [[foundations/ccl2-mcp1]] [[concepts/im-derived-ccl2-recmac-recruitment-loop]] [[claims/recmacs-express-protumorigenic-spp1-vegfa-arg1]]
- `[c04]` CD206hi IMs are Folr2/Cd163/Mmp9⁺ while CD206lo IMs are Tmem119/Mmp12/Ccr2⁺ (p.1-2) "CD206hi IMs ... expressed Folr2, Cd163, Mmp9 ... whereas CD206lo IMs expressed Ccr2, Mmp12, Mmp13 and Tmem119" — confidence: high — type: methodological — links: [[concepts/folr2-tissue-resident-macrophage]] [[concepts/chemokine-defined-interstitial-macrophage-division-of-labor]] [[claims/cd206hi-ims-folr2-cd163-mmp9-positive]]
- `[c05]` Pf4Cre Cx3cr1DTR mice selectively deplete CD206hi IMs without altering lung structure (p.2) "only IMs coexpress Cx3cr1 and therefore selectively express the diphtheria toxin (DT) receptor ... resulting in preferential depletion of CD206hi IMs" — confidence: high — type: methodological — links: [[foundations/pf4cre-cx3cr1dtr-im-depletion]] [[claims/pf4cre-cx3cr1dtr-mice-selectively-deplete-cd206hi]]
- `[c06]` CD206hi IM depletion increases lung tumor burden across three models (p.2-3) "DT administration in the Pf4CreCx3cr1DTR mice led to marked increased tumor burden (~3.7-fold in melanoma B16F10, 7.2-fold in ... KPAR1.3 and 2.3-fold in the spontaneous ... AgerCreERT2KP mice)" — confidence: high — type: quantitative — links: [[foundations/pf4cre-cx3cr1dtr-im-depletion]] [[claims/depletion-cd206hi-ims-increases-lung-tumor]]
- `[c07]` Transient CD206hi IM depletion after tumor seeding is sufficient to promote tumor growth (p.3) "a single intravenous DT dose administered on day 4 reproduced the phenotype ... indicating that transient depletion of CD206hi IM after tumor seeding was sufficient to promote tumor growth" — confidence: medium — type: mechanistic — links: [[claims/transient-cd206hi-im-depletion-after-tumor]]
- `[c08]` CD206hi IM depletion abolishes TLS formation and reduces lymphocyte aggregates (p.3) "TLS were completely lost ... B cell and T cell aggregates were markedly reduced (~80% reduction)" — confidence: high — type: mechanistic — links: [[concepts/cd206hi-im-bronchovascular-chemokine-tls-niche]] [[concepts/tertiary-lymphoid-structure]] [[claims/cd206hi-im-depletion-abolishes-tertiary-lymphoid]]
- `[c09]` CD206hi IM depletion reduces lung CXCL9/CXCL10/CXCL13 protein (p.3) "substantial reduction in CXCL9, CXCL10 and CXCL13 protein levels (~2.7-fold, 2.6-fold and 1.5-fold, respectively) in CD206hi IM-deficient ... mice" — confidence: high — type: quantitative — links: [[foundations/cxcl13-chemokine]] [[claims/cd206hi-im-depletion-reduces-lung-cxcl9]]
- `[c10]` CD206hi IMs occupy bronchovascular/pleural niches while CD206lo IMs and recMacs occupy tumor regions (p.4) "CD206hi IMs (Folr2, Cd163 and Mmp9) localized preferentially adjacent to the bronchial airways and the visceral pleura, whereas CD206lo IMs (Mmp12) and Fn1+Vcan+ recMacs predominated in tumor-dense regions" — confidence: high — type: correlational — links: [[concepts/anatomical-niche-predicts-macrophage-function]] [[foundations/xenium-in-situ-spatial-transcriptomics]] [[claims/cd206hi-ims-occupy-bronchovascular-pleural-niches]]
- `[c11]` Cxcl13 is produced by Cd163⁺Folr2⁺ CD206hi IMs lining bronchial airways (p.4) "CD163⁺Folr2⁺ CD206hi IMs lining Epcam⁺ bronchial epithelial airways coexpressed Cxcl13 in both the melanoma and adenocarcinoma models" — confidence: high — type: correlational — links: [[concepts/cd206hi-im-bronchovascular-chemokine-tls-niche]] [[claims/cxcl13-produced-cd163-folr2-cd206hi-ims]]
- `[c12]` AMs are excluded from tumor regions while recMacs dominate tumor cores (p.4) "AMs ... were largely excluded from tumor regions ... ~60–71% Vcan+Cx3cr1+Mafb+ recMacs and ~19–25% Mmp12+C5ar1+Mafb+CD206lo IMs of the total lung macrophages preferentially populated the tumor cores and margins" — confidence: high — type: quantitative — links: [[concepts/anatomical-niche-predicts-macrophage-function]] [[claims/alveolar-macrophages-excluded-tumor-regions-while]]
- `[c13]` CD206lo IMs and recMacs within the TME coexpress Ccl2 (p.5) "CD206lo IMs (Mmp12) and recMacs (Vcan) in the TME ... coexpressed Ccl2" — confidence: high — type: correlational — links: [[foundations/ccl2-mcp1]] [[concepts/im-derived-ccl2-recmac-recruitment-loop]] [[claims/cd206lo-ims-recmacs-within-tumor-microenvironment]]
- `[c14]` IM-derived CCL2 is the dominant nonredundant source for recMac recruitment (p.5-6) "IM-derived CCL2, rather than endothelial, recMac or DC derived CCL2, was required for recMac recruitment and the progression of B16F10 melanoma lung metastasis" — confidence: high — type: mechanistic — links: [[concepts/im-derived-ccl2-recmac-recruitment-loop]] [[foundations/busulfan-conditioning-myeloid-sparing]] [[claims/im-derived-ccl2-dominant-nonredundant-source]]
- `[c15]` Ccl2 deficiency in BM reduces tumor burden and recMac accumulation (p.5) "BM chimeric Ccl2−/− mice showed an approximately 10.8-fold reduction in lung tumor burden and a 2.7-fold decrease in Ly6C+CD11b+ recMacs accumulation" — confidence: high — type: quantitative — links: [[foundations/ccl2-mcp1]] [[claims/ccl2-deficiency-bone-marrow-reduces-tumor]]
- `[c16]` Busulfan vs irradiation conditioning isolates IM-derived CCL2 function (p.5-6) "irradiated BM chimeric mice reconstituted with Ccl2−/− BM exhibited a 7.0-fold reduction in lung metastatic burden compared to busulfan-treated BM chimeric mice reconstituted with Ccl2−/− BM" — confidence: high — type: methodological — links: [[foundations/busulfan-conditioning-myeloid-sparing]] [[claims/busulfan-versus-irradiation-conditioning-isolates-im]]
- `[c17]` Ly6C⁺ recMacs become moDCs that migrate via CCR5 and immunosuppress in draining lymph nodes (p.6) "Ly6C+CD11b+ recMacs migrate to the draining lymph nodes, where they differentiate into moDCs ... and induce antigen-specific regulatory T cells ... moDCs depend on CCR5-CCL5 signaling, rather than on CCR7" — confidence: high — type: mechanistic — links: [[concepts/ccr5-modc-immunosuppressive-lymph-node-axis]] [[foundations/ccr5-chemokine-receptor]] [[claims/ly6c-recmacs-become-modcs-migrate-ccr5]]
- `[c18]` CCR5 loss in monocyte-derived cells reduces lung metastatic burden (p.6) "Chimeric mice reconstituted with 80% Ccr2−/− to 20% Ccr5−/− BM ... had a 6.8-fold reduction in lung metastatic melanoma burden and a 9.3-fold reduction in lung adenocarcinoma burden" — confidence: high — type: quantitative — links: [[foundations/ccr5-chemokine-receptor]] [[concepts/ccr5-modc-immunosuppressive-lymph-node-axis]] [[claims/ccr5-loss-monocyte-derived-cells-reduces]]
- `[c19]` Maraviroc selectively and transiently blocks antigen-bearing moDC migration to draining lymph nodes (p.6) "mice treated with maraviroc exhibited an approximately 76% reduction in antigen-bearing Ly6C⁺ moDCs ... Inhibition ... was observed only when maraviroc was administered 3 h before antigen delivery" — confidence: high — type: pharmacological — links: [[foundations/maraviroc]] [[claims/maraviroc-selectively-transiently-blocks-antigen-bearing]]
- `[c20]` Maraviroc enhances neoantigen vaccine antitumor immunity (p.6-7) "Mice that received neoantigen peptides+ poly(I:C) together with maraviroc exhibited a 7.5-fold reduction in metastatic burden compared to unvaccinated mice and a 3.1-fold reduction compared to mice vaccinated ... without maraviroc" — confidence: high — type: pharmacological — links: [[foundations/maraviroc]] [[concepts/ccr5-modc-immunosuppressive-lymph-node-axis]] [[claims/maraviroc-enhances-neoantigen-vaccine-antitumor-immunity]]
- `[c21]` Macrophage function in tumors is best predicted by anatomical niche, not surface markers (p.7) "macrophage function in vivo is best understood by integrating spatial context with transcriptional state rather than relying on surface markers alone" — confidence: high — type: mechanistic — links: [[concepts/anatomical-niche-predicts-macrophage-function]] [[claims/macrophage-function-tumors-best-predicted-anatomical]]

## Discussion captured

### Authors' interpretation

The authors interpret tissue-resident macrophage function as **best predicted by anatomical niche**: distinct chemokine programs organize either protective immunity (bronchovascular/pleural CD206hi IMs producing CXCL13/9/10 → TLS) or tumor-promoting circuits (intratumoral CD206lo IMs/recMacs producing CCL2). They argue removal of CD206hi IMs "dismantled this immunologic scaffold." They identify tissue-resident **Ccl2⁺ IMs** as key, previously underappreciated contributors to the suppressive myeloid environment, refining models that emphasize stromal/endothelial/cancer-cell CCL2.

### Comparisons with prior literature (made by authors)

- Builds directly on Li et al., *Nat. Immunol.* 2024 (coordinated chemokine expression defines macrophage subsets / IMck0–9) and Rawat et al., *JEM* 2023 (CCL5⁺ migratory DCs guide CCR5⁺ monocytes into draining lymph nodes).
- CCL2-monocyte-metastasis framing from Qian et al., *Nature* 2011 and Kitamura et al., *JEM* 2015.
- Contrasts transient maraviroc with prolonged systemic CCR5 blockade trials (Haag et al. PICCASSO, *Eur. J. Cancer* 2022; Jiao et al., *Cancer Res.* 2019).
- Notes CD206/FOLR2 macrophage associations (Nalio Ramos et al., *Cell* 2022; Ray et al., *JEM* 2025) and TREM2 macrophages (Park et al., *Nat. Immunol.* 2023).

### Mechanistic hypotheses proposed

- Both CD206hi and CD206lo IM subsets produce Ccl2 and may both contribute to the protumor loop "likely with distinct timing and context" (p.7).
- Early monocyte-derived antigen presentation constrains protective immunity; temporary disruption favors DC-mediated priming (p.7).

### Caveats and self-criticism

- "No current genetic model selectively targets a single macrophage subset, with the exception of Ccl24Cre" — individual chemokine-defined IM subsets cannot be resolved functionally.
- Recruited monocytes are immunosuppressive in these cancer models, but scRNA-seq also identified inflammatory monocyte clusters that in infection contexts support protective T cell priming — function is context-dependent.

### Future directions suggested

- New experimental models to selectively interrogate individual chemokine-defined IM subsets.
- Therapeutics that **selectively disrupt suppressive monocyte-driven pathways while preserving resident macrophage programs** that coordinate protective immune architecture.

## Limitations

- Mouse-only functional experiments (melanoma + lung adenocarcinoma); human relevance argued from conserved macrophage programs, not tested at subset/spatial resolution here.
- Targeted Xenium gene panel rather than whole-transcriptome spatial profiling; small spatial n (2 melanoma + 2 adenocarcinoma).
- CD206hi IM depletion and CCL2/CCR5 perturbations act on compartments, not single chemokine-defined subsets.
- Causality between spatial position and function inferred from depletion/chimera experiments, not from spatial perturbation.

## Open questions

### Open questions raised by authors

- Which individual chemokine-defined IM subset (Cxcl13⁺ vs Cxcl9⁺ vs Cxcl10⁺) drives which protective function?
- What sets the timing/context of CD206hi vs CD206lo IM CCL2 output?
- Can monocyte-selective, transient CCR5 blockade be translated to human vaccination/immunotherapy schedules?

### Open questions identified during ingest

- Is niche assignment instructive (niche programs the macrophage) or selective (programmed macrophages home to niches)?
- Does preserving the CD206hi IM bronchovascular–TLS niche synergize with checkpoint blockade?
- How does this division of labor intersect with hypoxia in tumor cores (relevant to the broader corpus, though not addressed here)?

## My take

A clean, mechanism-first integration of scRNA-seq, Xenium spatial transcriptomics and compartment-resolved genetics that converts a confusing macrophage-marker landscape into a spatially organized, chemokine-defined division of labor. The two most actionable insights: (1) tissue-resident IM-derived CCL2 — not stromal/endothelial CCL2 — drives the protumor recMac loop, and (2) brief, windowed maraviroc during vaccination flips a suppressive moDC step into enhanced DC priming. The CD206-as-near-neutral-marker reframing is a useful corrective for the wider TAM literature.

## Related

- [[concepts/chemokine-defined-interstitial-macrophage-division-of-labor]]
- [[concepts/anatomical-niche-predicts-macrophage-function]]
- [[concepts/cd206hi-im-bronchovascular-chemokine-tls-niche]]
- [[concepts/im-derived-ccl2-recmac-recruitment-loop]]
- [[concepts/ccr5-modc-immunosuppressive-lymph-node-axis]]
- [[concepts/cxcl13-cxcr5-tls-recruitment]]
- [[concepts/tertiary-lymphoid-structure]]
- [[concepts/tam-recruitment-hypoxic-niche-chemokines]]
- [[concepts/tissue-resident-macrophage-tumor-niche]]
- [[concepts/macrophage-ontogeny-resident-vs-monocyte-derived]]
- [[people/soubhik-ghosh]]
- [[people/claudia-jakubzick]]
