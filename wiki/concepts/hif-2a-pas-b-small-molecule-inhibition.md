---
title: "HIF-2α PAS-B-pocket allosteric small-molecule inhibition"
aliases:
  - "Belzutifan mechanism"
  - "PT2385 mechanism"
  - "MK-6482 HIF-2α inhibitor"
  - "PAS-B pocket HIF-2α antagonist"
  - "HIF-2α / ARNT dimerization blocker"
  - "selective HIF-2α inhibitor"
  - "VHL disease HIF-2α drug"
  - "ccRCC HIF-2α inhibitor"
  - "DFF332 HIF-2α inhibitor"
  - "NKT2152 HIF-2α inhibitor"
  - "first FDA-approved HIF inhibitor"
tags:
  - HIF-2α
  - HIF2A
  - EPAS1
  - small-molecule
  - allosteric-inhibitor
  - PAS-B-pocket
  - VHL-disease
  - clear-cell-renal-cell-carcinoma
  - drug-discovery
  - clinical-trial
maturity: active
key_papers:
  - hypoxia-driven-crosstalk-between-tumor-tumor
first_introduced: "Scheuermann 2013 PNAS / Wehn 2018 J Med Chem (PAS-B allosteric HIF-2α antagonists); first-in-class clinical candidate PT2385 (Chen 2016 Nature); FDA approval Belzutifan 2021"
date_updated: 2026-05-08
related_concepts:
  - tumor-hypoxia-classification-chronic-acute-cyclic
related_topics: []
---

## Definition

A class of small-molecule allosteric inhibitors that bind the Per-ARNT-Sim B (PAS-B) hydrophilic pocket of HIF-2α (EPAS1), inducing a conformational change that disrupts HIF-2α / ARNT (HIF-1β) heterodimerization and abolishes downstream target-gene transcription. Despite the high sequence identity between HIF-1α and HIF-2α PAS-B domains, the PAS-B pocket of HIF-2α is uniquely druggable, and the inhibitors are highly selective for HIF-2α/ARNT dissociation with no measurable activity against HIF-1. The class includes Belzutifan (MK-6482, Welireg) — the first FDA-approved HIF inhibitor, indicated for VHL-disease-associated tumors — PT2385 (the first-in-class clinical candidate), DFF332, and NKT2152.

## Intuition

HIF-1α and HIF-2α share the same dimerization partner (ARNT/HIF-1β), the same DNA-binding HRE consensus, and overlapping target-gene programs — yet they are not redundant. HIF-2α dominates clear cell renal cell carcinoma (ccRCC) and VHL disease where the canonical pVHL-mediated degradation is lost. The chemical breakthrough was finding that the HIF-2α PAS-B domain — a protein-protein-interaction interface, not a classical enzyme active site — has an unexpectedly druggable internal cavity that, when occupied by a small molecule, allosterically blocks dimerization with ARNT. This was the cleanest example of "drugging a protein-protein interaction at an allosteric pocket" in oncology drug discovery, and it has now translated into FDA approval (Belzutifan, 2021) for the VHL-disease indication.

## Formal notation

Mechanism:
- HIF-2α has a PAS-B domain with a unique hydrophilic internal cavity (~290 Å³).
- Small molecule (Belzutifan, PT2385) occupies the cavity → conformational change → HIF-2α / ARNT dimerization blocked → no HIF-2α HRE binding → target genes not transcribed.
- Selectivity: high — HIF-1 function unaffected.
- Notable: the same general PAS-B pocket on HIF-3α can bind oleoylethanolamide (OEA) as an *agonist* — the pocket is thus a multi-state ligand-binding site whose functional consequence depends on molecule and isoform.

Approved / clinical molecules:
- **Belzutifan (MK-6482, Welireg)**: oral; first-in-class FDA approval (Aug 2021) for VHL-disease-associated RCC, CNS hemangioblastoma, pNET.
- **PT2385**: first clinical HIF-2α antagonist; ccRCC and recurrent GBM trials. Can mitigate sorafenib adverse effects through HIF-2α / AR / pSTAT3 / pAKT / pERK suppression.
- **DFF332** (Novartis): NCT04895748 phase I in advanced/relapsed renal cancer.
- **NKT2152**: NCT05119335 phase I/II in advanced ccRCC.

VHL disease background:
- Autosomal dominant tumor syndrome from VHL gene germline mutation/deletion.
- Loss of pVHL → constitutive HIF-α stabilization (especially HIF-2α) → multi-organ tumors (RCC, hemangioblastoma, pNET, pheochromocytoma).
- Belzutifan blocks the HIF-2α activity that pVHL would normally restrain.

Combination directions (per Bai 2022):
- Belzutifan + pembrolizumab (NCT04976634)
- Belzutifan + Lenvatinib (NCT05239728)
- Belzutifan + cabozantinib (NCT03634540, NCT04736706)
- Multiple other combinations at NCT05030506, NCT04626518, NCT04586231, NCT04626479

Special indications:
- Pacak-Zhuang syndrome (somatic-mosaic activating EPAS1 mutation): polycythemia + multiple paragangliomas; Belzutifan candidate per Bai 2022.

## Variants

- *Belzutifan vs PT2385*: similar mechanism; Belzutifan has improved PK/half-life and is the first FDA-approved member.
- *Selectivity profile*: all members of this class are HIF-2α-selective; HIF-1 is not targeted.
- *Allosteric mode*: distinct from competitive inhibitors targeting HIF-1α active sites (e.g. PX-478) or from translational inhibitors (digoxin, melatonin via SPHK1).
- *Pacak-Zhuang activating mutation* (EPAS1 / HIF-2α): direct mechanistic indication for HIF-2α-selective therapy.

## Comparison

vs HIF-1α inhibition (PX-478): different isoform, different pocket, different target-gene profile, different cancer-type specificity (HIF-2α dominates ccRCC; HIF-1α dominates many other cancers). The two are largely complementary, not redundant.
vs nucleic-acid-based HIF inhibition (ARO-HIF2 RNAi, RO7070179 ASO): the small molecule acts post-translationally on protein function; nucleic-acid drugs act on mRNA. Different PK/PD, different toxicity profile, different drug-delivery requirements.
vs blocking pVHL-HIF interaction directly: would reverse HIF-2α stabilization, but no clinical molecule targets this.
vs OEA-driven HIF-3α PAS-B agonism (Diao 2022): same general structural pocket, opposite outcome — illustrates that the PAS-B class is a conformational switch.

## When to use

- VHL-disease-associated tumors with active or progressive lesions where surgery is undesirable.
- Sporadic ccRCC after first-line failure (Belzutifan trials ongoing).
- Pacak-Zhuang syndrome (Bai 2022 prediction).
- Combination with checkpoint inhibitor or TKI in renal and CNS tumors.

## Known limitations

- The HIF-2α inhibitors have NO effect on HIF-1α-driven malignancies — therapeutic scope is limited to HIF-2α-dominant cancers (ccRCC and VHL setting principally).
- Resistance: tumors may evolve to use HIF-1α as a bypass (suspected in some ccRCC progressors).
- Anemia is a class side effect (HIF-2α drives erythropoietin; blocking HIF-2α reduces EPO).
- Pulmonary hypertension and metabolic effects observed in animal models with HIF-2α loss-of-function.
- Clinical trials have shown variable response durability; real-world effectiveness in non-VHL ccRCC is being established.

## Open problems

- Predictive biomarker for response (beyond VHL mutation): is there a transcriptomic signature that identifies HIF-2α-dependent tumors better than VHL status alone?
- Optimal combination partner: pembrolizumab vs Lenvatinib vs cabozantinib — head-to-head trials needed.
- Dose-response and chronic toxicity: long-term Belzutifan safety in young VHL patients (lifelong therapy).
- Whether the same mechanism can be extended to HIF-3α (where OEA is an endogenous agonist) for inverse-direction indications.

## Key papers

- [[papers/hypoxia-driven-crosstalk-between-tumor-tumor]] — Bai et al. 2022 *Molecular Cancer*. Section "HIF-1α/2α inhibitors for cancer treatment in clinical studies" is the latest review-level summary of the class, with NCT identifiers and combination strategies.

## My understanding

For my hypoxia thesis, the HIF-2α inhibitor class is a *therapeutic anchor* — it proves that HIF-axis intervention is clinically tractable. The mechanism (PAS-B dimerization block) is orthogonal to the cell-intrinsic NF-κB / TET2 reprogramming I study. An interesting cross-cutting question is whether Belzutifan's TAM-side effect (reducing HIF-2α-driven Spint1 secretion in TAMs, per Bai 2022 mechanism) partially offsets its tumor-restraining effect by releasing pro-HGF cleavage — a counterintuitive prediction worth flagging.
