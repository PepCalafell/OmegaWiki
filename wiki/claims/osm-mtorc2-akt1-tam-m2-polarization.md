---
title: "OSM (oncostatin M) from hypoxic cancer cells drives TAM M2 polarization via mTORC2-AKT1 (not PKCα)"
slug: osm-mtorc2-akt1-tam-m2-polarization
status: supported
confidence: 0.80
tags:
  - OSM
  - oncostatin-M
  - mTORC2
  - AKT1
  - PKCα
  - TAM
  - M2-polarization
  - hypoxia
  - IL-6-family
  - CD206
  - CD163
  - Arg-1
  - COX-2
domain: "immunology / oncology / signaling"
source_papers:
  - hypoxia-driven-crosstalk-between-tumor-tumor
evidence:
  - source: hypoxia-driven-crosstalk-between-tumor-tumor
    type: supports
    strength: medium
    detail: "Bai 2022 (DOI 10.1186/s12943-022-01645-2, p.10) summarizes that OSM (IL-6 family cytokine) secreted by hypoxic cancer cells engages OSMR on macrophages and activates mTORC2 → AKT1 (not PKCα), driving upregulation of M2 surface markers CD206, CD163, Arg-1, and COX-2."
conditions: "Demonstrated primarily in breast, lung, and hepatocellular cancer models; in vitro co-culture and macrophage stimulation experiments."
date_proposed: 2026-05-11
date_updated: 2026-05-11
---

## Statement

Oncostatin M (OSM) is an IL-6 family cytokine secreted by hypoxic cancer cells. OSM binds the OSMR-LIFR or OSMR-gp130 heterodimer on macrophages and triggers a signaling cascade in which mTORC2 — not PKCα as initially assumed — phosphorylates AKT1 specifically (not AKT2 or AKT3), driving M2 polarization. The output is upregulation of canonical M2 surface markers CD206 (MRC1), CD163, Arg-1 (Arginase-1), and the inflammation/prostaglandin enzyme COX-2 (PTGS2). This is one of the cytokine-driven hypoxic tumor→TAM channels, parallel to CCL2/CCL8/CXCL8 chemokine recruitment.

## Evidence summary

- [[papers/hypoxia-driven-crosstalk-between-tumor-tumor]] — Bai 2022 *Molecular Cancer*.
- Foundation: [[foundations/oncostatin-m-osm]].
- Concept linkage: [[concepts/tumor-associated-macrophage-immunosuppression]].

## Conditions and scope

- Hypoxic cancer-cell origin of OSM has been documented in breast, lung, and HCC.
- The mTORC2-AKT1 specificity (not PKCα, not AKT2/3) is a recent refinement (2019-2021 literature) of earlier "OSM → PI3K-AKT → M2" framing.

## Counter-evidence

- Some macrophage contexts (LPS-driven) show OSM signaling through PKCα in addition to mTORC2.
- OSM also has tumor-cell-intrinsic effects (EMT, stemness) that confound interpretation of mixed cancer-immune effects.

## Linked ideas

(none yet)

## Open questions

- Is the mTORC2 → AKT1 specificity preserved under cyclic vs chronic hypoxia, given mTORC2 is itself oxygen-sensitive?
- Does the COX-2 induction by OSM in TAMs contribute to PGE2-mediated T-cell exclusion, providing a mechanistic link between OSM and immune evasion?
