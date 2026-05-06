---
title: "TRMs and MDMs are ontogenically distinct populations in NSCLC"
slug: trm-mdm-distinct-ontogeny-nsclc
status: supported
confidence: 0.9
tags:
  - TRM
  - MDM
  - macrophage-ontogeny
  - NSCLC
  - lineage-tracing
  - fate-mapping
domain: "immunology / oncology"
source_papers:
  - tissue-resident-macrophages-provide-pro-tumorigenic
evidence:
  - source: tissue-resident-macrophages-provide-pro-tumorigenic
    type: supports
    strength: strong
    detail: "Map17(Pdzk1ip1)-creER × R26-tdTom and Cx3cr1-creER × R26-YFP fate mapping in KP NSCLC mice show that group I (PPARG⁺/MARCO⁺/SIGLEC1⁺) is depleted of label-positive cells (TRM lineage, embryonic origin), while group II (TREM2⁺/SPP1⁺/APOE⁺/GPNMB⁺), III (CD14⁺ monocytes), and IV (CD16⁺/CX3CR1⁺ monocytes) are heavily labelled (adult-HSC progeny). Cross-species conservation confirmed in human NSCLC scRNA-seq (Mount Sinai 35-patient cohort)."
conditions: "Mouse KP orthotopic NSCLC; tamoxifen-pulsed lineage tracing 6 months before tumour injection; cross-species validation in human NSCLC scRNA-seq."
date_proposed: 2026-05-06
date_updated: 2026-05-06
---

## Statement

In NSCLC, the four conserved myeloid groups identified by scRNA-seq (group I: TRMs, alveolar-like, PPARG⁺/MARCO⁺/SIGLEC1⁺/STMN1⁺; group II: MDMs, TREM2⁺/SPP1⁺/APOE⁺/GPNMB⁺; group III: CD14⁺ classical monocytes; group IV: CD16⁺/CX3CR1⁺ non-classical monocytes) are ontogenically distinct: group I derives from embryonic/self-renewing TRM lineage independent of adult HSCs, while groups II–IV derive from adult HSCs through a monocyte intermediate.

## Evidence summary

- Map17-creER × R26-tdTom labelling: 6 months after tamoxifen, group I cluster strongly depleted of Tomato⁺ cells (resident lineage); other groups heavily Tomato⁺
- Cx3cr1-creER × R26-YFP continuous labelling: same pattern, YFP-negative group I, YFP-positive groups II-IV
- Cross-species conservation: PPARG/MARCO/SIGLEC1/STMN1 (group I) and TREM2/SPP1/APOE/GPNMB (group II) gene modules conserved between human and mouse NSCLC
- Independent validation via signature similarity to bulk-RNA-seq of purified human alveolar macrophages (Leach 2020) and an inDrop NSCLC scRNA-seq dataset (Zilionis 2019)

## Conditions and scope

- Established in mouse KP orthotopic NSCLC and validated in human NSCLC scRNA-seq (35-patient cohort from Mount Sinai); cross-species signature similarity supports the dichotomy in human disease
- Lineage tracing is mouse-only; human ontogeny is inferred from signature conservation
- Pertains to early and intermediate stages of tumour growth (days 5-30 post KP injection in mouse)

## Counter-evidence

- Plasticity literature: monocytes may acquire TRM-like states given long enough residency, blurring the dichotomy in late-stage tumours
- Some skin / colon TRMs are partially replaced by MDMs over time, suggesting tissue-specific exceptions to embryonic-origin maintenance

## Linked ideas

(none yet)

## Open questions

- Whether monocyte-derived group II MDMs in chronic NSCLC eventually acquire TRM-like self-renewal
- Single-cell-resolution lineage tracing in human NSCLC to confirm cross-species inference
- Whether subpopulations within group I (alveolar TRM diversity) have distinct origins
