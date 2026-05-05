---
title: "Cluster C2 (403 CpGs) is hypomethylated specifically in hypoxic LPS-activated MACs"
slug: c2-cluster-cpg-demethylation-specific-hypoxic
status: supported
confidence: 0.9
tags:
  - DNA-methylation
  - hypoxia
  - macrophage
  - NF-kB
  - epigenetics
domain: "epigenetics"
source_papers:
  - nf-kb-tet2-promote-macrophage-reprogramming
evidence:
  - source: nf-kb-tet2-promote-macrophage-reprogramming
    type: supports
    strength: strong
    detail: "EPIC array DMP analysis, FDR<0.05, |Δβ|>0.2; HOMER NF-κB motif enrichment; ChIP-seq p65 cobinding; in vivo recapitulation in IL4I1 MACs from primary OC."
conditions: "Human monocyte-derived M-CSF MACs at 1% O2 + LPS 48h. CpGs are EPIC-array detectable; signature not yet validated outside MACs."
date_proposed: 2026-05-05
date_updated: 2026-05-05
---

## Statement

A specific cluster of 403 CpG sites (cluster C2) is hypomethylated only in mature hypoxic LPS-activated macrophages (mMAC1), not in mMAC21, iMAC21, iMAC1, or monocytes. C2 CpGs are enriched in NF-κB motifs, located at LPS-induced de novo enhancers (gain H3K4me1 and H3K27ac), and associated with proinflammatory genes including IL6 and TNF.

## Evidence summary

- EPIC array differential methylation analysis (FDR<0.05, |Δβ|>0.2) defines C2 = 403 CpGs.
- HOMER motif enrichment shows NF-κB family motif as most significantly enriched (Fig. 1F).
- C2 regions enriched in intergenic and open-sea genomic context (Fig. S1D).
- Reanalysis of MAC histone-mark ChIP-seq shows H3K4me1 + H3K27ac gain at C2 after LPS (Fig. S1E).
- C2 regions exclusively associated with p65-specific ChIP-seq peaks (P1 cluster), not HIF1α (Fig. 4I-J).
- Sorted IL4I1 MACs from primary ovarian carcinoma recapitulate the C2 hypomethylation pattern (Fig. 5J).

## Conditions and scope

- In vitro M-CSF MACs at 1% O₂ + LPS 48 h.
- Confirmed in vivo in IL4I1 MACs sorted from human ovarian tumors.
- Not yet tested in non-LPS NF-κB activators or in non-myeloid cells.

## Counter-evidence

(none in the present paper; contradiction would require a hypoxic LPS-activated MAC system showing different DMP topology)

## Linked ideas

(none yet)

## Open questions

- Generalizability across different NF-κB-activating stimuli at the same CpGs.
- Persistence of C2 demethylation upon return to normoxia (memory).
- Whether C2 expansion (more CpGs) defines deeper mMAC1 phenotypes.
