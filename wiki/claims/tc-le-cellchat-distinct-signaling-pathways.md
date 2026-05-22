---
title: "CellChat shows TC-exclusive (ANGPTL/GRN/NECTIN/EPHB) and LE-exclusive/enriched (CSPG4, Collagen, Tenascin, Laminin, FN1, MIF, CD99, Notch) signalling pathways"
slug: tc-le-cellchat-distinct-signaling-pathways
status: supported
confidence: 0.75
tags: [CellChat, ligand-receptor, OSCC, methodological]
domain: oncology/cell-cell-communication
source_papers:
  - spatial-transcriptomics-reveals-distinct-conserved-tumor
evidence:
  - source: spatial-transcriptomics-reveals-distinct-conserved-tumor
    type: supports
    strength: moderate
    detail: "TC-exclusive: ANGPTL, GRN, NECTIN, EPHB. LE-exclusive: CSPG4. LE-enriched (vs TC-TC): Collagen, Laminin, Tenascin, FN1, MIF, APP, CD99, Notch. Key ligand-receptor pairs include DSC2-DSG1 and ANGPTL4-SDC1 (TC), LAMB3-ITGA6_ITGB4 and MIF-CD74_CD44 (LE)."
conditions: "CellChat default databases; ST-spot ligand-receptor inference"
date_proposed: 2026-05-22
date_updated: 2026-05-22
---

## Statement
The TC and LE compartments engage in distinct ligand-receptor signalling: TC features adhesive desmosomal and growth-factor pathways, while LE is dominated by ECM remodelling and inflammatory pathways, including the oncogenic MIF-CD74_CD44 interaction.

## Evidence summary
CellChat aggregated signalling pathway analysis; circos plots of representative ligand-receptor pairs (Fig. 3e–h, Supplementary Fig. 3f).

## Conditions and scope
ST-derived spot-level inference; CellChat default thresholds.

## Counter-evidence
CellChat inference is correlative; pathway exclusivity may reflect detection sensitivity rather than absolute absence.

## Linked ideas

## Open questions
Whether MIF-CD74_CD44 disruption suffices to collapse LE state in vivo.
