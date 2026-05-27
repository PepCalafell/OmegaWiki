---
# === Identification ===
title: "A sympathetic-eosinophil axis orchestrates psychological stress to exacerbate skin inflammation"
slug: sympathetic-eosinophil-axis-orchestrates-psychological-stress
arxiv: ""
doi: "10.1126/science.adv5974"
pmid: ""
venue: "Science"
year: 2026
authors:
  - "Jiahe Tian"
  - "Yudian Cao"
  - "Yilei Li"
  - "Junlong Sun"
  - "Cheng Zhan"
  - "Wei Ni"
  - "Yongjun Zheng"
  - "Yanqing Wang"
  - "Shenbin Liu"
first_author: "Jiahe Tian"
corresponding_author: "Shenbin Liu"

# === Source & metadata ===
source_type: pdf
s2_id: ""
date_added: 2026-05-27
ingested_date: 2026-05-27
ingest_version: 1
last_reviewed: null

# === Classification ===
importance: 5
tier: TIER_1
tags:
  - atopic-dermatitis
  - psychological-stress
  - sympathetic-nervous-system
  - eosinophil
  - prodynorphin
  - Pdyn
  - CCL11
  - eotaxin
  - CCR3
  - Adrb2
  - neuroimmunology
  - optogenetics
  - chemogenetics
  - DREADD
  - intersectional-genetics
  - sNuc-seq
  - retrograde-tracing
  - hairy-skin
  - MC903
  - RHS
  - itch
  - degranulation
keywords:
  - sympathetic-eosinophil axis
  - Pdyn+ sympathetic neurons
  - stress-aggravated atopic dermatitis
  - CCL11-CCR3 eosinophil recruitment
  - Adrb2-mediated eosinophil degranulation
  - psychological stress dermatitis
  - HPA axis vs sympathetic nervous system
  - hairy-skin sympathetic innervation
  - sNuc-seq stellate ganglion
  - context-dependent β2-adrenergic signalling
domain: "neuroimmunology / dermatology / sympathetic nervous system"

# === Biomedical domain ===
tissue:
  - skin_hairy
  - blood
  - bone_marrow
  - stellate_ganglion
  - thoracic_ganglion_T2
condition:
  - atopic_dermatitis
  - psychological_stress
disease_specific:
  - atopic_dermatitis
species:
  - mouse
  - human
hypoxia_relevant: false
contains_immune_cells: true
contains_myeloid: false

# === Technique ===
techniques:
  - scRNA-seq_10x
  - snRNA-seq
  - bulk_RNA-seq
  - flow_cytometry
  - optogenetics_CatCh
  - chemogenetics_DREADD_hM3Dq
  - chemogenetics_DREADD_hM4Di
  - immunohistochemistry
  - retrograde_tracing_CTB
  - pseudorabies_PRV_tracing
  - transwell_migration
  - multiplex_chemokine_assay
  - chemical_sympathectomy_6OHDA
  - conditional_Cre_loxP
  - intersectional_Cre_Flp
n_samples: null
n_cells_total: 25877
integration_method: ""

# === Biology captured ===
key_cell_types:
  - eosinophil
  - sympathetic_neuron_Pdyn
  - sympathetic_neuron_Npy
  - mast_cell
  - CD45_leukocyte
  - keratinocyte
  - dermal_fibroblast
key_markers:
  - Pdyn
  - Npy
  - Th
  - Slc18a2_Net
  - Dbh
  - Snap25
  - Tubb3
  - Adrb2
  - Ccl11
  - Ccr3
  - Epx
  - Mbp
  - Il31
  - Siglec-F
  - CD45
  - CD11b
  - Oprk1
  - VIP
  - CGRP
key_pathways:
  - sympathetic_noradrenergic_signaling
  - CCL11_CCR3_chemotaxis
  - Adrb2_Gs_cAMP_vs_beta_arrestin2
  - HPA_axis_corticosterone
  - eosinophil_degranulation
  - itch_scratch_neuroimmune_cycle

# === User project membership ===
projects:
  - thesis
  - skin
priority: useful
read_status: read

# === HypoxiaVERSE-specific ===
hypoxiaverse_status: not_included
exclusion_reason: "neuroimmune skin AD axis; not hypoxia-relevant — kept for thesis skin/dermatology and AHR-AD intersection"
data_availability: "GEO GSE302016; Zenodo 10.5281/zenodo.17694111 (sc/snuc-seq); 10.5281/zenodo.17696528 (bulk RNA-seq)"

# === Cross-references ===
code_url: ""
cited_by: []
---

## Problem

Psychological stress is a clinically established aggravating factor in atopic dermatitis (AD), yet the cellular and molecular pathway by which stress signals in the brain are converted into worsened skin inflammation has remained underspecified. Traditional models pin the link on either HPA-axis cortisol or generalised systemic immune dysfunction, both of which fail to explain the specificity (skin-targeted) and severity (eosinophil-dominant) of stress-aggravated AD. Eosinophilic infiltration is a hallmark of AD, but the recruitment and activation logic of eosinophils under stress — and the contribution of subtype-specific peripheral sympathetic neurons to that logic — has not been mapped.

## Key idea

Acute psychological stress engages a specific subset of paravertebral noradrenergic sympathetic neurons defined by Prodynorphin (Pdyn) expression that selectively innervate hairy skin. These neurons drive eosinophil-dependent exacerbation of AD-like inflammation through a two-arm mechanism: (i) local release of the chemokine CCL11, which recruits eosinophils via CCR3, and (ii) local noradrenaline release, which activates the recruited eosinophils via β2-adrenergic receptors (Adrb2) to drive degranulation and inflammation. The HPA axis is not the driver of stress-aggravated AD — adrenalectomy worsens, rather than improves, the phenotype. The companion sympathetic subset (Npy+) handles vasomotor reflexes, not dermatitis. Pharmacological CCR3 blockade (SB297006) and eosinophil-specific Adrb2 knockout are independently sufficient to abolish stress-driven worsening of AD.

## Method

**Human cohort**: Retrospective study of 51 AD patients with Perceived Stress Scale (PSS), SCORAD, NRS scores, paired CBC, and skin biopsy (MBP-IHC for eosinophils, tryptase for mast cells).

**Mouse model**: MC903 (calcipotriol) topical induction of AD-like dermatitis ([[foundations/mc903-calcipotriol-ad-model]]); ~10 days; day-10 peak. Validation in HDM + SEB AD model.

**Stress paradigms**: Repeated high-platform stress (RHS) ([[foundations/repeated-high-platform-stress-rhs]]), restraint stress (PPR), cage-change stress; plasma corticosterone + noradrenaline read-out.

**Endocrine and sympathetic dissection**: Bilateral adrenalectomy (blocks HPA-axis corticosterone); peripheral 6-OHDA chemical sympathectomy ([[foundations/6-hydroxydopamine-chemical-sympathectomy]]).

**Single-cell readouts**: scRNA-seq of skin CD45+ leukocytes (25,877 cells, 20 immune types); sNuc-seq of stellate ganglia + T2 thoracic ganglia (~30 mice, 198 neurons, 4 Th+ subtypes); FosCreER-H2b-EGFP activity tagging.

**Intersectional genetic lines (Cre × Flp)**:
- **PdynNet-TD** = PdynCre × NetFlpo × loxP-stop-loxP-frt-stop-frt-tdTomato-DTR (visualises and conditionally depletes Pdyn+ noradrenergic sympathetic neurons).
- **PdynNet-Abl** = PdynNet-TD + DTx i.p. (ablation).
- **PdynNet-CatCh** ([[foundations/catch-channelrhodopsin-optogenetics]]) — optogenetic activation.
- **PdynNet-hM4Di** ([[foundations/hm3dq-hm4di-dreadd-chemogenetics]]) — chemogenetic silencing.
- **NpyNet-TD / NpyNet-Abl** — parallel for Npy+ neurons.

**Eosinophil perturbations**:
- **Epx^iCre-DTA** (ablation), **Epx^iCre-hM3Dq** (chemogenetic activation), **Epx^iCre-Adrb2^fl/fl** (conditional Adrb2 KO), **Epx^iCre-oprk1^fl/fl** (conditional Oprk1 KO).
- Anti-CCR3 mAb (Grimaldi 1999 clone).
- SB297006 ([[foundations/sb297006-ccr3-antagonist]]).

**Anatomical tools**: CTB-488 retrograde tracing of skin-projecting sympathetic neurons; Cre-dependent PRV-Bartha transsynaptic retrograde tracing from intradermal injection ([[foundations/pseudorabies-virus-retrograde-tracing]]).

**Ex vivo assays**: Transwell migration of Siglec-F-sorted blood eosinophils co-cultured with optogenetically activated CatCh sympathetic neurons; multiplexed chemokine profiling; Adrb2-agonist (salmeterol, tulobuterol) degranulation assays (Epx supernatant).

**Bulk RNA-seq**: Siglec-F-sorted eosinophils ([[foundations/siglec-f-eosinophil-marker]]) from EtOH vs MC903 mice for adrenergic/Npy/opioid receptor expression.

## Results

### 1. Stress correlates with eosinophilia and AD severity in humans (Fig. 1)
- PSS↔SCORAD r=0.665 ***P<0.001; PSS↔NRS r=0.637 ***P<0.001.
- PSS↔blood eosinophils r=0.439, P=0.004.
- High-PSS dermal MBP+ eosinophils increased vs low/moderate (t4=2.883, P=0.045).
- Neutrophils, basophils, monocytes, T/B cells, skin mast cells unaffected by PSS.

### 2. RHS is the only stressor that exacerbates MC903 AD (Fig. 2A–F, fig. S2)
- RHS produces the largest plasma NA increase among RHS / PPR / cage-change.
- Day-10 RHS: TEWL F5,60=9.058 ***P<0.001; scratching F5,60=8.887 ***P<0.001; CD45+ t12=7.363 ***P<0.001; eosinophils t12=5.765 ***P<0.001.
- PPR weak; cage-change null. Effect requires pre-established inflammation.

### 3. Eosinophils are required for stress exacerbation (Fig. 2G–J, fig. S5)
- Epx^iCre-DTA eosinophil depletion (>16-fold blood reduction) protects from RHS-driven worsening of TEWL, scratching, dermal thickness, CD45+ infiltration.
- Baseline AD pathology unaffected by eosinophil depletion.
- Acute chemogenetic eosinophil activation (Epx^iCre-hM3Dq + CNO) is sufficient to trigger itch flare-ups.

### 4. Peripheral sympathetic — not HPA — drives the effect (fig. S6)
- Adrenalectomy worsens RHS dermatitis ⇒ HPA axis is a brake, not a driver.
- 6-OHDA chemical sympathectomy abolishes RHS-induced worsening; baseline AD unaffected.

### 5. sNuc-seq identifies stress-activated sympathetic subtypes (Fig. 3A–B, fig. S7)
- 4 Th+ subtypes (Snap25/Tubb3/Slc18a2/Dbh).
- 2 stress-recruited subtypes: Pdyn+ (cluster 3, 32% of activated) and Npy+ (clusters 1/2/4, 25% of activated).
- Pdyn also highly expressed in human stellate ganglia.

### 6. Pdyn+ neurons selectively innervate hairy skin (Fig. 3C–H, fig. S8)
- PdynNet-TD labels ~30% of paravertebral sympathetic neurons.
- 89.5% Pdyn-mRNA+ neurons are tdTomato+; 88.2% tdTomato+ are TH+; <1% VIP+ or Npy+.
- tdTomato+ fibres: abundant in hairy-skin dermis; absent from glabrous skin, lung, kidney, spleen, BAT.
- 32% of hairy-skin-innervating sympathetic somata are tdTomato+ (CTB-488).
- tdTomato+ fibres in close apposition to Siglec-F+ eosinophils in inflamed dermis (movie S2).
- PRV-Bartha traces skin-Pdyn+ neurons back to paraventricular nucleus and locus ceruleus.

### 7. Pdyn+ neurons necessary for stress exacerbation (Fig. 3I–L, fig. S9, S12)
- PdynNet-Abl (DTx) abolishes RHS-driven worsening of TEWL, scratching, dermal thickness, eosinophilia in MC903 model.
- Vasoconstriction reflex preserved.
- Baseline AD unaffected.
- Acute hM4Di silencing during RHS recapitulates the ablation phenotype.
- Replicated in HDM + SEB AD model (fig. S13).

### 8. Npy+ neurons mediate vasoconstriction, not dermatitis (fig. S10–S11)
- NpyNet fibres encircle cutaneous blood vessels.
- NpyNet-Abl reverses RHS tail-skin-temperature drop but does not protect against dermatitis exacerbation.

### 9. Pdyn+ activation is sufficient via eosinophils (Fig. 4)
- 473-nm optogenetic stimulation of PdynNet-CatCh skin fibres exacerbates AD: ↑TEWL, ↑scratching, ↑dermal thickness, ↑CD45+, 1.4-fold ↑ eosinophil proportion, 2.5-fold ↑ absolute eosinophils.
- Anti-CCR3 mAb eosinophil depletion abolishes optogenetic effect on dermatitis and acute scratching.

### 10. CCL11 is the chemoattractant; SB297006 blocks chemotaxis (Fig. 5A–E, fig. S15)
- Blue-light-activated CatCh sympathetic neurons drive eosinophil migration in Transwell (P=0.002).
- CCL11 is the most abundant chemotactic factor in conditioned medium (t8=2.401, P=0.043).
- CCL11 upregulated within Pdyn+ neurons after MC903 (fig. S15H).
- SB297006 (20 μM) eliminates Transwell migration.
- Systemic SB297006 alleviates RHS skin inflammation (TEWL t8=5.521 ***P<0.001) without affecting baseline AD.

### 11. Adrb2 is the eosinophil-side noradrenergic integrator (Fig. 5F–K, fig. S16)
- Bulk RNA-seq of MC903 eosinophils: Adrb2 most highly expressed adrenergic/Npy/opioid receptor and upregulated.
- Oprk1 (κ-opioid; Pdyn receptor) unchanged; Epx^iCre-oprk1^fl/fl shows no AD or RHS phenotype.
- Adrb2 agonists salmeterol (F3,16=8.195 P=0.002) and tulobuterol (F3,16=3.992 P=0.027) dose-dependently increase Epx release ex vivo.
- Epx^iCre-Adrb2^fl/fl reduces RHS-evoked TEWL (t9=2.707 P=0.024), scratching (P=0.009), dermal thickness (t9=5.236 ***P<0.001) without affecting baseline AD or eosinophil biology.

## All claims (exhaustive)

- `[c01]` In AD patients (n=51), perceived stress (PSS) correlates positively with SCORAD (r=0.665), NRS (r=0.637), and blood (r=0.439) / skin eosinophil counts; other immune cells unchanged (p.1270, Fig. 1B–J) "Elevated stress levels showed a strong correlation with increased severity of skin inflammation… A positive association was observed between stress and eosinophil counts in both blood and skin tissues" — confidence: high — type: correlational — links: [[foundations/atopic-dermatitis]] [[concepts/sympathetic-eosinophil-axis-skin-inflammation]] [[claims/stress-eosinophilia-correlation-ad-severity-human]]
- `[c02]` RHS — but not PPR or cage-change — exacerbates pre-established MC903 AD-like inflammation in mice (TEWL, scratching, dermal thickness, CD45+ infiltration all up at day 10) (p.1271-1272, Fig. 2A–F, fig. S2) "RHS markedly exacerbated skin inflammation, as evidenced by increased TEWL, heightened spontaneous scratching bouts, dermal thickness, and CD45+ leukocyte infiltration" — confidence: high — type: quantitative — links: [[foundations/repeated-high-platform-stress-rhs]] [[foundations/mc903-calcipotriol-ad-model]] [[concepts/stress-paradigm-specific-sympathetic-circuit]] [[claims/rhs-stress-exacerbates-ad-mouse-mc903]]
- `[c03]` Eosinophil ablation (Epx^iCre-DTA) abolishes RHS-induced AD exacerbation without affecting baseline MC903 disease (p.1272, Fig. 2G–J, fig. S5G–H) "Eosinophil depletion protected against RHS-induced exacerbation of skin inflammation… without affecting baseline inflammation" — confidence: high — type: mechanistic — links: [[foundations/eosinophil-peroxidase-epx]] [[concepts/sympathetic-eosinophil-axis-skin-inflammation]] [[claims/eosinophil-depletion-protects-stress-exacerbated-dermatitis]]
- `[c04]` Acute chemogenetic eosinophil activation (Epx^iCre-hM3Dq + CNO) is sufficient to trigger itch flare-up in AD-like mice (p.1272, fig. S5A–D, movie S1) "eosinophil activation alone was sufficient to trigger acute itch flare-ups in AD-like mice" — confidence: medium — type: mechanistic — links: [[foundations/hm3dq-hm4di-dreadd-chemogenetics]] [[foundations/il-31-cytokine]] [[claims/chemogenetic-eosinophil-activation-triggers-acute-itch]]
- `[c05]` Peripheral 6-OHDA chemical sympathectomy abolishes RHS-induced inflammation and eosinophilia but does not affect baseline MC903 AD (p.1272, fig. S6D–L) "Chemical sympathectomy did not alter MC903-induced skin inflammation or eosinophil accumulation… However, it rendered mice resistant to RHS-induced inflammation and eosinophilia" — confidence: high — type: mechanistic — links: [[foundations/6-hydroxydopamine-chemical-sympathectomy]] [[claims/sympathectomy-blocks-stress-induced-dermatitis-not-baseline]]
- `[c06]` Bilateral adrenalectomy worsens RHS-induced skin inflammation — HPA axis activation counteracts rather than drives stress-aggravated AD (p.1272, fig. S6A–C) "Adrenalectomy worsened skin inflammation in stressed mice, indicating that HPA axis activation may counteract, rather than enhance, stress-induced skin inflammation" — confidence: medium — type: mechanistic — links: [[claims/adrenalectomy-worsens-stress-dermatitis-hpa-not-driver]]
- `[c07]` sNuc-seq (stellate + T2 ganglia, 198 neurons, 4 Th+ subtypes) plus FosCreER labelling identifies Pdyn+ (32%) and Npy+ (25%) as the stress-activated noradrenergic sympathetic subtypes; Pdyn also highly expressed in human stellate ganglia (p.1272-1273, Fig. 3A–B, fig. S7) "two major types of noradrenergic sympathetic neurons were identified: a Pdyn (Prodynorphin) subpopulation (cluster 3), and a broader Npy (Neuropeptide Y) population… Pdyn was also highly expressed in human stellate sympathetic ganglia" — confidence: high — type: methodological — links: [[foundations/snrna-seq-single-nucleus]] [[foundations/prodynorphin-pdyn-neuropeptide]] [[concepts/pdyn-sympathetic-neurons-hairy-skin-innervation]] [[claims/pdyn-and-npy-sympathetic-neurons-activated-by-stress]]
- `[c08]` PdynNet intersectional line labels Pdyn+ noradrenergic sympathetic neurons that selectively innervate hairy skin (32% of hairy-skin-innervating sympathetic somata), are absent from glabrous skin / lung / kidney / spleen / BAT, and lie in close apposition to dermal eosinophils; PRV-Bartha tracing maps back to paraventricular nucleus and locus ceruleus (p.1273-1274, Fig. 3C–H, fig. S8) "tdTomato+ fibres were... abundant in the dermis of hairy skin... ~32% of hairy skin–innervating sympathetic neurons were tdTomato+" — confidence: high — type: methodological — links: [[foundations/prodynorphin-pdyn-neuropeptide]] [[foundations/pseudorabies-virus-retrograde-tracing]] [[concepts/pdyn-sympathetic-neurons-hairy-skin-innervation]] [[claims/pdyn-sympathetic-neurons-innervate-hairy-skin-specifically]]
- `[c09]` DTx-mediated ablation of Pdyn+ neurons (PdynNet-Abl) abolishes RHS-induced exacerbation of dermatitis and eosinophilia without affecting baseline AD; replicated in HDM+SEB model (p.1273-1274, Fig. 3I–L, fig. S9, S13L–O) "MC903-treated PdynNet-Abl mice did not exhibit RHS-induced exacerbation of dermatitis or eosinophilia" — confidence: high — type: mechanistic — links: [[foundations/cre-loxp-recombinase-system]] [[concepts/pdyn-sympathetic-neurons-hairy-skin-innervation]] [[claims/pdyn-neuron-ablation-protects-stress-exacerbated-dermatitis]]
- `[c10]` NpyNet sympathetic neurons mediate the RHS-induced vasoconstriction reflex (tail-skin temperature) but not stress-aggravated dermatitis (p.1274, fig. S10–S11) "Npy+ neurons formed a dense network around cutaneous blood vessels… these neurons… did not contribute to aggravated skin inflammation" — confidence: high — type: mechanistic — links: [[concepts/pdyn-sympathetic-neurons-hairy-skin-innervation]] [[claims/npy-neurons-vasoconstriction-not-dermatitis]]
- `[c11]` Acute chemogenetic silencing of Pdyn+ neurons (PdynNet-hM4Di + CNO) during RHS eliminates stress-induced AD exacerbation, recapitulating the ablation phenotype without injury confounds (p.1274, fig. S12) "Silencing PdynNet neurons during RHS through intraperitoneal CNO injection did not affect the baseline dermatitis but did eliminate the RHS-evoked exacerbation" — confidence: high — type: mechanistic — links: [[foundations/hm3dq-hm4di-dreadd-chemogenetics]] [[claims/pdyn-acute-silencing-hm4di-blocks-stress-exacerbation]]
- `[c12]` Optogenetic activation of skin-innervating Pdyn+ fibres (PdynNet-CatCh, 473 nm) is sufficient to exacerbate AD: ↑TEWL, ↑scratching, ↑dermal thickness, 1.4× ↑ eosinophil proportion, 2.5× ↑ absolute eosinophils (p.1274-1275, Fig. 4A–G, fig. S14) "CatCh mice exhibited increased spontaneous scratching bouts, elevated TEWL, skin thickening, and greater CD45+ leukocyte infiltration compared with controls" — confidence: high — type: mechanistic — links: [[foundations/catch-channelrhodopsin-optogenetics]] [[concepts/pdyn-sympathetic-neurons-hairy-skin-innervation]] [[claims/optogenetic-pdyn-activation-mimics-stress-induced-skin-inflammation]]
- `[c13]` Anti-CCR3 mAb-mediated eosinophil depletion abolishes optogenetic-Pdyn-driven dermatitis exacerbation and acute scratching, placing eosinophils downstream of Pdyn+ neuron firing (p.1275, Fig. 4H–L) "This treatment alleviated the enhanced skin inflammation… triggered by blue-light stimulation in CatCh mice" — confidence: high — type: mechanistic — links: [[foundations/ccr3-chemokine-receptor]] [[concepts/ccl11-ccr3-eosinophil-chemotaxis-skin]] [[claims/anti-ccr3-blocks-optogenetic-pdyn-dermatitis-exacerbation]]
- `[c14]` Activated Pdyn+ sympathetic neurons release CCL11 as the most abundant chemotactic factor in conditioned medium; SB297006 (CCR3 antagonist) abolishes Transwell eosinophil migration; CCL11 is upregulated within Pdyn+ sympathetic neurons after MC903 (p.1275, Fig. 5A–D, fig. S15) "CCL11 (Eotaxin-1) was identified as the most abundant factor… Pharmacological inhibition of CCR3 with SB297006 eliminated eosinophil migration toward blue-light–stimulated CatCh neurons" — confidence: high — type: mechanistic — links: [[foundations/ccl11-eotaxin-1]] [[foundations/ccr3-chemokine-receptor]] [[concepts/ccl11-ccr3-eosinophil-chemotaxis-skin]] [[claims/pdyn-neurons-release-ccl11-recruit-eosinophils-via-ccr3]]
- `[c15]` Systemic SB297006 alleviates RHS-induced TEWL, scratching, and dermal thickening in MC903 AD-like mice without altering baseline disease (p.1275, Fig. 5E, fig. S15I–K) "SB297006 treatment significantly reduced lesional TEWL, spontaneous scratching bouts, and dermal thickness of lesional skin in RHS-treated AD-like mice" — confidence: high — type: pharmacological — links: [[foundations/sb297006-ccr3-antagonist]] [[concepts/ccl11-ccr3-eosinophil-chemotaxis-skin]] [[claims/sb297006-ccr3-antagonist-alleviates-rhs-skin-inflammation]]
- `[c16]` Bulk RNA-seq of MC903-mouse blood eosinophils: Adrb2 is the most highly expressed adrenergic/Npy/opioid receptor and is upregulated in MC903; Oprk1 (κ-opioid; Pdyn receptor) is unchanged (p.1275, Fig. 5F–G) "The adrenergic receptor beta2 (Adrb2) was expressed abundantly in eosinophils and up-regulated in eosinophils of AD-like mice, surpassing all other adrenergic, Npy, and opioid receptors" — confidence: high — type: quantitative — links: [[foundations/adrb2-beta2-adrenergic-receptor]] [[concepts/adrb2-eosinophil-context-dependent-degranulation]] [[claims/adrb2-most-expressed-adrenergic-receptor-eosinophils-ad]]
- `[c17]` Adrb2 agonists salmeterol and tulobuterol drive dose-dependent Epx release from AD-mouse blood eosinophils ex vivo (p.1275, Fig. 5H–I) "Treatment of eosinophils with the Adrb2 agonist salmeterol or tulobuterol induced a dose-dependent release of cationic granule proteins" — confidence: high — type: pharmacological — links: [[foundations/adrb2-beta2-adrenergic-receptor]] [[foundations/eosinophil-peroxidase-epx]] [[concepts/adrb2-eosinophil-context-dependent-degranulation]] [[claims/adrb2-agonist-degranulates-eosinophils-dose-dependent]]
- `[c18]` Eosinophil-specific Adrb2 deletion (Epx^iCre-Adrb2^fl/fl) reduces RHS-induced TEWL, scratching, dermal thickness without altering baseline AD or eosinophil biology (p.1275, Fig. 5J–K, fig. S16G–K) "eosinophil-specific Adrb2 knockout mitigated stress-induced exacerbation of dermatitis" — confidence: high — type: mechanistic — links: [[foundations/adrb2-beta2-adrenergic-receptor]] [[concepts/adrb2-eosinophil-context-dependent-degranulation]] [[claims/eosinophil-specific-adrb2-knockout-protects-stress-dermatitis]]
- `[c19]` Eosinophil-specific Oprk1 deletion (Epx^iCre-oprk1^fl/fl) does not affect AD pathology or RHS-induced exacerbation, ruling out a κ-opioid (dynorphin) arm in eosinophils (p.1275, fig. S16A–F) "Oprk1 does not contribute to AD-like pathology or RHS-induced AD exacerbation" — confidence: medium — type: mechanistic — links: [[foundations/prodynorphin-pdyn-neuropeptide]] [[claims/oprk1-knockout-eosinophils-not-required-stress-ad]]

## Discussion captured

### Authors' interpretation

The authors position the Pdyn+ sympathetic-eosinophil axis as the missing mechanistic link between psychological stress and AD severity. They emphasize that stress paradigms are not interchangeable — different stressors recruit different sympathetic subtypes and imprint distinct peripheral immune signatures, even when overall corticosterone elevation is similar. They reframe the long-standing clinical disappointment of IL-5 / IL-5Rα blockade in AD (which depletes eosinophils systemically) as consistent with their finding that eosinophils are dispensable for baseline AD but critical specifically for the stress-aggravated arm — and therefore the relevant clinical-trial design must stratify by patient stress state. They argue that Adrb2 signalling on eosinophils is context-dependent, branching through Gs–cAMP (anti-inflammatory in cytokine-primed eosinophils, as in classical asthma data) vs β-arrestin-2 (proinflammatory in AD-context dermal eosinophils), reconciling decades of conflicting β2-agonist clinical observations.

### Comparisons with prior literature (made by authors)

- **Furlan et al. 2016 (Nat. Neurosci.)** — label-line organisation of sympathetic neurons; conceptual basis for subtype-specificity.
- **Wang et al. Nature 2025** — target-tissue-specific sympathetic outflow; extended here to skin/immune target.
- **Zhang et al. Nature 2020** — segregated stress neural circuits.
- **Poller et al. Nature 2022** — sympathetic-leukocyte specificity (heart/bone marrow context).
- **Pellefigues et al. 2021 (JACI)** — MC903 AD model reference.
- **Shinkai 1993; Grimbaldeston 2005** — Rag2⁻/⁻ and Sash⁻/⁻ mice show T/B cells and mast cells are not crucial for stress-aggravated AD.
- **Fulkerson 2006 (PNAS); White 2000 (JBC)** — CCL11–CCR3 axis biology; SB297006 antagonist pharmacology.
- **Moriyama 2018 (Science); Tamura 2012 (Allergol. Int.)** — Adrb2 in immune cells; salmeterol / tulobuterol pharmacology.
- **Whetstone 2025; Kang 2020** — limited efficacy of IL-5 / IL-5Rα blockade in AD trials.
- **Pedersen 1993; Aldridge 2002** — conflicting β2-agonist clinical data in eosinophilic disease.
- **Nash 2018; Nguyen 2017** — Gs–cAMP vs β-arrestin-2 branching of β2-adrenergic signalling.
- **Duan 2014 (Cell)** — Pdyn-Cre line used for intersectional labelling.
- **Kleinlogel 2011** — CatCh optogenetic actuator.

### Mechanistic hypotheses proposed

- The Pdyn+ subtype's "giant soma" + Pdyn / NetFlpo signature defines a category of sympathetic neurons that selectively innervate piloerector muscles in hairy skin and may evolutionarily serve piloerection — but is co-opted under pathological stress for eosinophil recruitment.
- Adrb2 signalling outcome (anti- vs proinflammatory) is determined by cellular and pathological context via the Gs-cAMP / β-arrestin-2 branchpoint.
- Bone marrow eosinopoiesis is governed by another, distinct sympathetic subtype (since sympathectomy reduces eosinophils systemically); only Pdyn+ governs *local skin* recruitment.

### Caveats and self-criticism

- The clinical cohort is retrospective and small (n=51).
- Causal manipulation is restricted to mouse.
- Mouse Pdyn+ neuron-driven CCL11 release may not directly translate to human stellate-ganglion biology even though human stellate Pdyn expression is confirmed.
- Whether and how Adrb2 modulates eosinophil function in primary cells from AD patients remains unresolved.
- The HDM+SEB AD model validation is restricted to selected readouts.

### Future directions suggested

- Test whether mental-health interventions reduce dermal eosinophil burden in AD patients.
- Develop subtype-selective blockers (e.g. CCR3 antagonists, eosinophil-Adrb2 modulators) for stress-aggravated AD.
- Map analogous circuit specificity in human stellate ganglia using human sNuc-seq.
- Probe Adrb2 Gs-cAMP vs β-arrestin-2 bias in human AD eosinophils.
- Define which sympathetic subtype governs bone-marrow eosinopoiesis (the systemic eosinophil reduction after sympathectomy is currently unassigned to a subtype).

## Limitations

- Mouse-centric perturbation logic; human evidence is correlational.
- Single AD-induction model (MC903) as the primary system; HDM+SEB validation is partial.
- Acute stress paradigms; chronic-stress translation untested.
- Single sympathetic ganglion-level transcriptomic dataset; no cross-strain or human sNuc-seq replication.
- No direct in vivo measurement of intra-skin CCL11 or noradrenaline kinetics.
- Receptor-bias model (Gs vs β-arrestin-2) is interpretive, not directly tested with biased ligands.

## Open questions

### Open questions raised by authors

- Whether Adrb2 modulates eosinophil function the same way in primary cells from AD patients.
- Which sympathetic subtype controls bone-marrow eosinopoiesis.
- Whether stress management interventions reduce dermal eosinophilia clinically.
- Whether IL-5/IL-5Rα blockade plus stress-axis modulation outperforms either alone.

### Open questions identified during ingest

- Whether psoriasis, chronic urticaria, or other neurally-rich skin conditions share the Pdyn+ sympathetic-eosinophil axis.
- Whether CCL11 release from Pdyn+ neurons is activity-coupled (vesicular) or transcription-coupled (constitutive ramp).
- The relationship between hair-follicle stem-cell stress signalling and Pdyn+ neuron firing.
- Whether the same axis drives stress-aggravated alopecia areata or pruritus in dermatologic-immune comorbidities.
- Whether AHR modulators ([[foundations/atopic-dermatitis]] / [[papers/aryl-hydrocarbon-receptor-rehabilitated-target-therapeutic]]) intersect with the sympathetic-eosinophil arm — both target AD but via distinct cellular routes.

## My take

This is the cleanest neuroimmune-circuit dissection of stress-aggravated atopic dermatitis I have seen, and it is positioned at exactly the granularity that matters clinically: a specific sympathetic *subtype* (Pdyn+), a specific chemokine (CCL11), a specific receptor on a specific immune cell (Adrb2 on eosinophils), and three independent perturbation strategies (DTx ablation, hM4Di silencing, optogenetic activation) converging on the same conclusion. The HPA-axis-as-brake-not-driver result is genuinely surprising and worth flagging — it overturns a textbook narrative.

For thesis-adjacent skin work, the operative concept is **stressor-specific sympathetic recruitment**: not all "stress" engages the same circuit. If AHR-dependent AD therapeutics (tapinarof, etc.) are eventually combined with stress-axis modulation, the question becomes whether AHR signalling intersects with Pdyn+ neuron firing, eosinophil Adrb2 signalling, or the CCL11–CCR3 chemotactic arm — none of which have been mapped.

The biggest practical limitation is that the receptor-bias model (Adrb2 Gs-cAMP vs β-arrestin-2) is inferred, not tested. A biased-agonist experiment would close the loop; the paper does not deliver this. The clinical-cohort sample is also small for a strong human-correlational claim.

## Related

- [[foundations/atopic-dermatitis]] — disease background and AHR-therapeutic intersection.
- [[foundations/mc903-calcipotriol-ad-model]] — mouse model used throughout.
- [[foundations/repeated-high-platform-stress-rhs]] — sympathetic-dominant stress paradigm.
- [[foundations/prodynorphin-pdyn-neuropeptide]] — Pdyn marker and Pdyn-Cre driver.
- [[foundations/ccl11-eotaxin-1]] — chemoattractant.
- [[foundations/ccr3-chemokine-receptor]] — eosinophil receptor.
- [[foundations/adrb2-beta2-adrenergic-receptor]] — eosinophil noradrenergic integrator.
- [[foundations/eosinophil-peroxidase-epx]] — granule protein and Epx^iCre driver.
- [[foundations/il-31-cytokine]] — itch-inducing eosinophil-released mediator.
- [[foundations/catch-channelrhodopsin-optogenetics]] — optogenetic actuator.
- [[foundations/hm3dq-hm4di-dreadd-chemogenetics]] — chemogenetic activators / silencers.
- [[foundations/6-hydroxydopamine-chemical-sympathectomy]] — sympathectomy reagent.
- [[foundations/pseudorabies-virus-retrograde-tracing]] — central tracing of Pdyn+ projections.
- [[foundations/sb297006-ccr3-antagonist]] — CCR3 antagonist.
- [[foundations/siglec-f-eosinophil-marker]] — eosinophil identification marker.
- [[foundations/snrna-seq-single-nucleus]] — sNuc-seq of sympathetic ganglia.
- [[foundations/cre-loxp-recombinase-system]] — intersectional Cre/Flp lines.
- [[concepts/sympathetic-eosinophil-axis-skin-inflammation]] — central organising concept.
- [[concepts/pdyn-sympathetic-neurons-hairy-skin-innervation]] — subtype identity.
- [[concepts/ccl11-ccr3-eosinophil-chemotaxis-skin]] — chemotactic arm.
- [[concepts/adrb2-eosinophil-context-dependent-degranulation]] — effector arm.
- [[concepts/stress-paradigm-specific-sympathetic-circuit]] — stressor specificity principle.
