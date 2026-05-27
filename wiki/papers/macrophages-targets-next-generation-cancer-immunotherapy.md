---
# === Identification ===
title: "Macrophages: Targets for next-generation cancer immunotherapy"
slug: macrophages-targets-next-generation-cancer-immunotherapy
arxiv: ""
doi: "10.1016/j.ccell.2026.01.020"
pmid: ""
venue: "Cancer Cell"
year: 2026
authors:
  - "Xiaoqi Sun"
  - "Matthew D. Park"
  - "Miriam Merad"
  - "Brian D. Brown"
first_author: "Xiaoqi Sun"
corresponding_author: "Miriam Merad; Brian D. Brown"

# === Source & metadata ===
source_type: pdf
s2_id: ""
date_added: 2026-05-27
ingested_date: 2026-05-27
ingest_version: 1
last_reviewed:

# === Classification ===
importance: 5
tier: TIER_1
tags:
  - macrophage
  - tumor-associated-macrophage
  - cancer-immunotherapy
  - review
  - innate-checkpoint
  - car-m
  - mce
  - bioengineering
keywords:
  - TAM
  - macrophage reprogramming
  - phagocytosis checkpoint
  - CSF1R
  - CD47
  - TREM2
  - SPP1
  - CXCL9
  - LILRB
  - succinate-itaconate
  - 6D atlas
domain: "immunology"

# === Biomedical domain ===
tissue: [multi]
condition: [cancer]
disease_specific: []
species: [human, mouse]
hypoxia_relevant: true
contains_immune_cells: true
contains_myeloid: true

# === Technique ===
techniques: [review]
n_samples:
n_cells_total:
integration_method: ""

# === Biology captured ===
key_cell_types:
  - tumor-associated macrophage
  - TREM2⁺ TAM
  - SPP1⁺ TAM
  - CXCL9⁺ TAM
  - monocyte-derived macrophage
  - resident tissue macrophage
  - myeloid progenitor
key_markers:
  - CSF1R
  - CCL2
  - CCR2
  - CD47
  - SIRPα
  - TREM2
  - SPP1
  - CXCL9
  - LILRB2
  - LILRB4
  - MARCO
  - CLEVER-1
  - CD40
  - FOLR2
  - Arg1
  - IDO1
key_pathways:
  - CSF1-CSF1R signaling
  - CD47-SIRPα phagocytosis checkpoint
  - efferocytosis (TAM receptors)
  - PRR/STING/TLR myeloid activation
  - HIF-1α / succinate / IL-1β axis
  - itaconate / KEAP1 / NRF2 axis
  - kynurenine / AHR

# === User project membership ===
projects: [thesis, hypoxia]
priority: core
read_status: skimmed

# === HypoxiaVERSE-specific ===
hypoxiaverse_status: candidate
exclusion_reason:
data_availability: ""

# === Cross-references ===
code_url: ""
cited_by: []
---

## Problem

Tumor-associated macrophages (TAMs) are the most abundant immune cell type in many solid tumors and play paradoxical pro- and antitumor roles. Despite decades of work, clinical efforts targeting TAMs (CSF1R inhibitors, CCL2/CCR2 blockade, CD47 antagonists, TREM2 blockade) have largely failed. The review asks: what next-generation strategies can both *relieve* macrophage-driven immunosuppression and *unleash* macrophage tumoricidal potential, and what framework is needed to design them rationally?

## Key idea

Macrophage-targeted cancer therapy can be organized into three pillars — **depletion**, **effectorization**, and **reprogramming** — and the failure of first-generation single-axis interventions (CSF1R, CCL2, CD47, TREM2) argues for combination strategies that hit multiple axes. The authors propose a **6D characterization framework** (causal drivers, spatial niches, temporal dynamics, signaling state, metabolism, ontogeny) plus a 4D therapeutic design pipeline to escape the M1/M2 binary and enable subset- and niche-specific targeting.

## Method

Narrative review. Synthesizes:
- Single-cell and spatial atlases that identify TREM2⁺, SPP1⁺, CXCL9⁺ TAM states across tumor types
- Clinical-trial outcomes (Table 1, ~40 trials covering CSF1R, CCR2, CD47/SIRPα, TREM2, LILRB2/B4, CLEVER-1, IDO1, arginase, STING, TLR3/7/8/9, CD40, CAR-M)
- Mechanistic data on phagocytosis checkpoints, myeloid cell engagers, masked antibodies, lipid nanoparticles for myeloid delivery, IL-12-armored anti-TAM CAR T cells
- Functional genomics directions (Perturb-seq, Perturb-map, foundational models)

## Results

Major synthesized findings (see ## All claims for atomic statements):

- TAMs converge on three recurring transcriptional states across tumor types — TREM2⁺, SPP1⁺, CXCL9⁺ — with subset-specific prognostic implications that vary by tissue (e.g., TREM2 is suppressive in skin/lung/sarcoma but supportive of anti-PD-1 response in HCC).
- Tumors program myelopoiesis systemically: bone-marrow and splenic niches receive tumor-derived cues (IL-1, IL-6, IL-8, CCL2, CSF-1/2/3) and output already-imprinted myeloid progenitors.
- Three-pillar therapeutic taxonomy: depletion (CSF1R, CCR2 — clinically limited), effectorization (CD47-SIRPα, MCEs, PRR/CD40 agonists — partial responses, anti-inflammatory feedback), reprogramming (innate checkpoints, signaling/metabolism modulators, genetic engineering — most promising for durable benefit).
- Innate immune checkpoints (LILRB2, LILRB4, CLEVER-1, MARCO, LAIR-1, TREM2) define an emerging class of TAM-restricted targets, with LILRB2/B4 and CLEVER-1 showing partial clinical efficacy.
- TAM metabolic reprogramming: succinate↔itaconate set-point governs inflammatory output; Arg1 and IDO1/AHR axes drive amino-acid-mediated T-cell suppression.
- Bioengineering frontier: bispecific MCEs (DR-0201), masked antibodies (ADG153), TAM-targeted LNPs, genetically engineered HSCs (temferon), CAR-M (CT-0508), and IL-12-armored anti-TREM2/FOLR2 CAR T cells.

## All claims (exhaustive)

- `[c01]` TAMs converge on three conserved transcriptional states (TREM2⁺, SPP1⁺, CXCL9⁺) across diverse tumor types (p.2) "three subsets of TAMs—the TREM2-expressing, SPP1-expressing, and CXCL9/10-expressing—were shown to define the most commonly recurring states across tumors of different tissue types" — confidence: high — type: correlational — links: [[concepts/pan-cancer-tam-atlas-23-clusters]] [[concepts/momac-verse-mnp-verse-atlas]] [[claims/tam-converge-three-conserved-states-pan-cancer]]
- `[c02]` SPP1⁺ macrophages express immunosuppressive programs and associate with necrosis and poor prognosis (p.2) "SPP1+ macrophages express classical immunosuppressive gene programs and their enrichment is associated with necrosis and poor patient prognosis" — confidence: high — type: correlational — links: [[foundations/spp1-secreted-phosphoprotein-1]] [[concepts/cxcl9-spp1-tam-ratio-ici-biomarker]] [[claims/spp1-tam-poor-prognosis-necrosis]]
- `[c03]` TREM2⁺ macrophages associate with worse OS in skin/lung cancers and sarcomas (p.2) "TREM2+ macrophages were shown to dampen immunity in skin and lung cancers and sarcomas and are associated with worse overall survival" — confidence: high — type: correlational — links: [[concepts/trem2-tumor-associated-macrophage]] [[foundations/trem2-receptor]] [[claims/trem2-tam-worse-os-skin-lung-sarcoma]]
- `[c04]` In HCC, TREM2⁺ macrophages link to better PD-1 response and promote antitumor immunity (p.2) "in hepatocellular carcinoma (HCC), TREM2+ macrophages were linked to better patient response to PD-1 blockade, and in mouse models of HCC, TREM2+ macrophages promoted antitumor immunity" — confidence: medium — type: correlational — links: [[concepts/hepatic-trem2-protective-tam-program]] [[papers/trem2-macrophages-associated-enhanced-response-pd]] [[claims/trem2-tam-hcc-better-pd1-response]]
- `[c05]` Tumors systemically imprint myelopoiesis via IL-1/IL-6/IL-8/CCL2/CSF-1-2-3 cues sensed by BM and spleen (p.3) "Peripheral tumor cues, including soluble inflammatory molecules and chemokines (e.g., IL-1⍺/β, IL-6, IL-8, CCL2, and CSF-1/2/3), sensed by the bone marrow both mobilize immunosuppressive myeloid progenitors to tumors directly and imprint myeloid progenitors with epigenetic modifications" — confidence: high — type: mechanistic — links: [[concepts/tumor-imprinted-myelopoiesis]] [[foundations/ccl2-mcp1]] [[foundations/csf1r-receptor]] [[claims/tumor-systemic-myelopoiesis-imprinting]]
- `[c06]` Macrophage-targeted therapies fall into three categories: depletion, effectorization, reprogramming (p.4) "we classify these therapeutic strategies into three categories... (1) Depletion and reduced accumulation... (2) Effectorization... (3) Reprogramming" — confidence: high — type: methodological — links: [[concepts/tam-therapy-three-pillars]] [[claims/tam-therapy-three-categories-framework]]
- `[c07]` CSF1R blockade reduces TAMs preclinically but shows limited clinical efficacy and dose-limiting ocular edema and hepatotoxicity (p.4) "clinical trials that tested CSF1R inhibitors in various solid tumors have shown limited efficacy. There were also dose limiting side effects with CSF1R blockade in patients, including ocular edema and hepatotoxicity" — confidence: high — type: pharmacological — links: [[foundations/csf1r-receptor]] [[claims/csf1r-blockade-limited-clinical-efficacy]]
- `[c08]` Anti-CCL2 antibodies fail clinically; free CCL2 rebounds within 1 week of dosing (p.4) "free CCL2 levels rebound in patients as early as 1 week after the first infusion, irrespective of subsequent dosing" — confidence: high — type: pharmacological — links: [[foundations/ccl2-mcp1]] [[claims/anti-ccl2-rebound-clinical-failure]]
- `[c09]` First-generation CD47 antagonists fail due to "don't eat me" ligand redundancy; APMAP KO enhances anti-CD47 phagocytosis in lymphoma/breast/ovarian models (p.9) "CRISPR screening uncovered many different genes that negatively regulate ADCP, such as APMAP, and showed that knockout of this gene in different cancer cell types (lymphoma, breast, and ovarian) enhanced anti-CD47-triggered macrophage-mediated phagocytosis" — confidence: high — type: mechanistic — links: [[concepts/sirpa-cd47-don-t-eat-me-axis]] [[foundations/cd47-don-t-eat-me-receptor]] [[claims/cd47-first-gen-failure-eat-me-redundancy]]
- `[c10]` ADCP induces an anti-inflammatory, pro-angiogenic program in macrophages (p.9) "ADCP induced an anti-inflammatory, pro-angiogenic program in macrophages. This highlights a challenge of effectorization, since it can trigger pro-tumor programs" — confidence: medium — type: mechanistic — links: [[concepts/sirpa-cd47-don-t-eat-me-axis]] [[claims/adcp-induces-proangiogenic-tam-program]]
- `[c11]` PS sensing via TYRO3/AXL/MERTK with GAS6/PROS1 bridging biases macrophages toward anti-inflammatory output (p.9) "PS on apoptotic cells is recognized by TAM-family receptors (TYRO3, AXL, MERTK) via bridging ligands GAS6 and S1, often working with additional PS receptors... PS sensing biases macrophages toward anti-inflammatory outputs" — confidence: high — type: mechanistic — links: [[foundations/mertk-tam-receptors]] [[claims/ps-tam-receptors-anti-inflammatory-bias]]
- `[c12]` Myeloid cell engagers (DR-0201, CD20×Dectin-1) force SYK-coupled immunogenic phagocytosis and create an MHC-II antigen-transfer conduit (p.10) "Dren Bio's DR-0201, which targets CD20 on B cells and Dectin-1 on macrophages to force SYK-coupled, immunogenic phagocytosis" — confidence: medium — type: mechanistic — links: [[concepts/myeloid-cell-engager-mce]] [[claims/mce-syk-immunogenic-phagocytosis]]
- `[c13]` PRR/CD40 agonists activate TAMs preclinically but yield low or inconsistent clinical response rates (p.10) "TLR agonists, including TLR9 agents like tilsotolimod, TLR7/8 agonists like motolimod, and TLR3/dsRNA mimetics like BO-112, have shown only transient or limited benefit, with several phase 3 programs failing to meet primary endpoints" — confidence: high — type: pharmacological — links: [[foundations/cd40-co-stimulatory-receptor]] [[concepts/pattern-recognition-receptors-macrophage]] [[claims/prr-agonists-tam-activation-clinical-limited]]
- `[c14]` TREM2 antagonism (PY314) mono- or combo-PD-1 did not yield clinically significant antitumor efficacy (p.11) "TREM2 blockade—either as a monotherapy or in combination with PD-1 blockade—did not yield significant antitumor efficacy" — confidence: high — type: pharmacological — links: [[concepts/innate-immune-checkpoint-blockade]] [[foundations/trem2-receptor]] [[claims/trem2-antagonism-clinical-no-efficacy]]
- `[c15]` First-generation IDO1 inhibition (epacadostat) failed in phase 3 advanced melanoma (ECHO-301/KEYNOTE-252) (p.12) "Although first-generation IDO1 inhibition failed in phase 3 trials in melanoma (ECHO-301/KEYNOTE-252), extensive preclinical and correlative human data still support the pathway's immunoregulatory role" — confidence: high — type: pharmacological — links: [[foundations/ido1-indoleamine-dioxygenase]] [[foundations/ahr-ido1-tryptophan-axis]] [[claims/ido1-inhibition-phase3-melanoma-failure]]
- `[c16]` Succinate stabilizes HIF-1α and drives IL-1β; itaconate alkylates KEAP1 to activate NRF2 — opposing TAM metabolic set points (p.12) "succinate stabilizes HIF-1α and drives IL-1β, providing a direct link between mitochondrial metabolism and inflammation; conversely, the mitochondrial metabolite itaconate is anti-inflammatory, acting via KEAP1 alkylation to activate NRF2 and temper type-I IFN responses" — confidence: high — type: mechanistic — links: [[concepts/succinate-itaconate-metabolic-set-point]] [[concepts/m1-macrophage-tca-breaks-itaconate-succinate]] [[foundations/hif1a]] [[claims/succinate-itaconate-tam-set-point]]
- `[c17]` IL-12-armored anti-TREM2 or anti-FOLR2 CAR T cells deplete suppressive TAMs and enrich CXCL9⁺ macrophages, controlling ovarian/lung/CRC tumors preclinically (p.13) "armoring anti-TREM2 or anti-FOLR2 CAR T cells with IL-12 could result in more durable control of ovarian, lung, and colorectal tumors in preclinical models... led to enrichment of CXCL9+ TAMs" — confidence: high — type: pharmacological — links: [[concepts/il12-armored-anti-tam-car-t]] [[concepts/folr2-tissue-resident-macrophage]] [[concepts/ifng-mac-cxcl9-tam-ici-responder]] [[claims/il12-armored-anti-tam-cart-cxcl9-enrichment]]
- `[c18]` A 6D TAM atlas (drivers, niches, temporal, signaling, metabolism, ontogeny) is required for rational TAM-targeted therapy design (p.14) "we propose that an integrated 6D model with the following elements will introduce the first steps toward myeloid-targeting therapies with greater translational potential" — confidence: medium — type: methodological — links: [[concepts/6d-tam-translational-framework]] [[claims/6d-tam-atlas-rational-design]]
- `[c19]` HDAC inhibitors combine with CD47 blockade to enhance phagocytosis in glioblastoma models, with a low-to-medium dose window (p.12) "synergized with CD47 blockade by enhancing macrophage phagocytosis in glioblastoma models. These beneficial reprogramming effects appear to depend on low-to-medium dosing" — confidence: medium — type: pharmacological — links: [[concepts/sirpa-cd47-don-t-eat-me-axis]] [[claims/cd47-hdac-combo-glioblastoma-phagocytosis]]
- `[c20]` Arg1⁺ TAMs deplete arginine and blunt T cell proliferation; IDO1/TDO kynurenines act via AHR to promote immunosuppression (p.12) "Arg1-expressing TAMs deplete arginine and blunt T cell proliferation. In parallel, IDO1/TDO-mediated tryptophan catabolism generates kynurenines that act (in part via AHR) to promote immune suppression" — confidence: high — type: mechanistic — links: [[foundations/arg1-arginase-1]] [[foundations/ido1-indoleamine-dioxygenase]] [[foundations/aryl-hydrocarbon-receptor]] [[concepts/arginase-mdsc-arginine-depletion-tcell]] [[claims/arg1-ido-amino-acid-tcell-suppression]]

## Discussion captured

### Authors' interpretation

The authors interpret the recurrent clinical failures of single-axis TAM interventions (CSF1R, CCL2, CD47, TREM2 antagonism, IDO1 inhibition, STING/TLR agonists) as evidence that single-marker, single-mechanism strategies are insufficient. Their preferred model is that effective TAM therapy must (a) *remove* immunosuppressive TAMs, (b) *install* a CXCL9⁺-dominant repopulating compartment, and (c) account for systemic imprinting at the progenitor level. The IL-12-armored anti-TAM CAR T result is highlighted as proof-of-principle for this combined approach. They frame the 6D atlas as a "first step" framework rather than a validated predictive model.

### Comparisons with prior literature (made by authors)

- Park, Silvin, Ginhoux, Merad 2022 (Cell 185, 4259) — cited for the pan-cancer TAM state taxonomy
- Blériot, Dunsmore, Alonso-Curbelo, Ginhoux 2024 (Cancer Cell) — temporal perspective on TAMs
- Noy & Pollard 2014 (Immunity) — historical mechanisms-to-therapy framing
- DeNardo & Ruffell 2019 (Nat. Rev. Immunol.) — macrophages as regulators of tumor immunity
- Schol et al. 2024 (Cancer Cell) — myeloid effector cells
- Dunsmore et al. 2024 (Sci. Immunol.) — timing/location of monocyte→TAM transition

### Mechanistic hypotheses proposed

- "Universal TAM targets for tumor-agnostic therapies that reprogram them across diverse cancers" (p.2) — hypothesis that recurrent transcriptional states permit pan-cancer TAM-reprogramming therapy
- The succinate↔itaconate "set point" framework (p.12) — hypothesis that TAM function is governed by a tunable metabolic balance
- TREM2 better suited as an "anchor" for MCE/CAR-T/LNP delivery rather than as a pure antagonist target (p.11)

### Caveats and self-criticism

- "The limitations of 'binning' [TAMs] into discrete categories, as molecularly similar macrophages can have different roles in tumor biology depending on the cancer type, the stage, and even the therapy" (p.2)
- Translational gap: current TAM knowledge derives heavily from animal models and treatment-naive biopsies, with limited longitudinal/on-treatment human data
- Authors acknowledge that several proposed combination strategies (HDAC + CD47, IL-12-armored CAR-T) lack human data

### Future directions suggested

- Scaled functional genomics (Perturb-seq, Perturb-map) to nominate causal drivers
- High-resolution spatial atlases to define niche-specific TAM positioning
- Longitudinal sampling and on-treatment imaging for temporal dynamics
- Combination therapies that hit multiple axes (depletion + reprogramming)
- Targeted LNPs / viral vectors for tumor-enhanced delivery
- Foundational AI models that predict TAM control and adaptation across contexts

## Limitations

- Narrative review without systematic search criteria; potential selection bias toward Mount Sinai work (Brown lab IL-12-armored CAR T)
- Heavy reliance on preclinical mouse data for emerging modalities (MCEs, CAR-M, masked antibodies); human data are sparse
- Three-state (TREM2/SPP1/CXCL9) framework is acknowledged as reductive
- 6D framework is conceptual and not yet operationalized into validated quantitative biomarkers
- Clinical trial summary (Table 1) does not include outcomes from 2025-2026 cohorts still maturing

## Open questions

### Open questions raised by authors

- Which cytokines/cues are *non-redundant* drivers of pro-tumor vs antitumor TAM programs in different tumors?
- What are the molecular and cellular niches of SPP1⁺, TREM2⁺, and CXCL9⁺ TAMs outside of hypoxic/necrotic regions?
- How does TAM composition evolve during multimodal therapy (chemotherapy, checkpoint blockade, kinase inhibitors)?
- Can the succinate↔itaconate balance be measured non-invasively as a biomarker?
- How do human TAMs differ from mouse TAMs in the contexts most relevant to therapy?

### Open questions identified during ingest

- Whether the CXCL9⁺ TAM enrichment seen with IL-12-armored CAR T cells in mouse models will translate to humans is the key open question — Hamon et al. 2025 (in this wiki) provides correlative human evidence for the TREM2 side of this story in HCC.
- Whether innate-immune-checkpoint blockade (LILRB2/B4, CLEVER-1) is sufficient on its own, or always needs a T-cell-checkpoint partner.
- How tumor hypoxia interacts with the succinate↔itaconate set point — direct mechanistic relevance to the thesis's hypoxia-TAM line.

## My take

A comprehensive, current map of the TAM-targeting therapeutic landscape that converts a noisy literature into an organized three-pillar taxonomy plus a 6D characterization framework. The most useful contributions for this wiki are: (a) the integration of clinical-trial outcomes (Table 1) with mechanistic rationale, which separates "promising preclinical" from "validated in humans"; (b) the explicit framing of TAM therapy as inherently combinatorial (depletion *plus* reprogramming); and (c) the highlight that TREM2 should be repurposed from antagonist target to *anchor* for delivery — which aligns with the wiki's existing TREM2-HCC story (Hamon 2025) and the CXCL9/SPP1 ICI biomarker concept. The 6D framework is more aspirational than predictive but is a useful organizing scaffold.

## Related

- [[concepts/tumor-associated-macrophage-immunosuppression]]
- [[concepts/trem2-tumor-associated-macrophage]]
- [[concepts/pan-cancer-tam-atlas-23-clusters]]
- [[concepts/m1-m2-polarization-paradigm]]
- [[concepts/sirpa-cd47-don-t-eat-me-axis]]
- [[concepts/cxcl9-spp1-tam-ratio-ici-biomarker]]
- [[concepts/ifng-mac-cxcl9-tam-ici-responder]]
- [[concepts/macrophage-ontogeny-resident-vs-monocyte-derived]]
- [[concepts/tissue-resident-macrophage-tumor-niche]]
- [[concepts/folr2-tissue-resident-macrophage]]
- [[concepts/car-t-cell-therapy]]
- [[concepts/mononuclear-phagocyte-system]]
- [[concepts/pattern-recognition-receptors-macrophage]]
- [[concepts/m1-macrophage-tca-breaks-itaconate-succinate]]
- [[concepts/tam-therapy-three-pillars]]
- [[concepts/chimeric-antigen-receptor-macrophage]]
- [[concepts/myeloid-cell-engager-mce]]
- [[concepts/masked-antibody-tme-conditional]]
- [[concepts/innate-immune-checkpoint-blockade]]
- [[concepts/succinate-itaconate-metabolic-set-point]]
- [[concepts/6d-tam-translational-framework]]
- [[concepts/tumor-imprinted-myelopoiesis]]
- [[concepts/il12-armored-anti-tam-car-t]]
- [[papers/trem2-macrophages-associated-enhanced-response-pd]] — TREM2-PD1 context-dependence in HCC
- [[papers/pd-l1-expressing-tumor-associated-macrophages]] — TAM-expressed PD-L1
- [[papers/nf-kb-tet2-promote-macrophage-reprogramming]] — TAM reprogramming via NF-κB/TET2
