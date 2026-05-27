---
title: "WNN modality weights differ by spatial cluster: cardiac tissue (W6) is RNA-defined, craniofacial region (W11) is DNA-methylation-defined in E11 embryo"
slug: modality-weights-differ-cardiac-rna-craniofacial-dnam-defined
status: supported
confidence: 0.85
tags: [WNN, modality-weight, spatial-omics, epigenetic-priming]
domain: spatial omics / multi-omics integration
source_papers:
  - spatial-joint-profiling-dna-methylome-transcriptome
evidence:
  - source: spatial-joint-profiling-dna-methylome-transcriptome
    type: supports
    strength: moderate
    detail: "Quote (p.3-4): 'we computed modality weights for individual spatial pixels (Extended Data Fig. 4g). This analysis revealed that some clusters were defined predominantly by gene expression (for example, W6, cardiac tissue), whereas others by DNA methylation (for example, W11, craniofacial region)'."
conditions: "E11 mouse embryo, 50 μm pixel size; WNN modality weights computed per pixel."
date_proposed: 2026-05-27
date_updated: 2026-05-27
---

## Statement

Per-pixel WNN modality weights are non-uniform across tissue: some spatial clusters are defined predominantly by gene expression (cardiac tissue, W6), others predominantly by DNA methylation (craniofacial region, W11). This implies regulatory modality-dominance varies by anatomical context.

## Evidence summary

Reported in [[papers/spatial-joint-profiling-dna-methylome-transcriptome]], Extended Data Fig. 4g.

## Conditions and scope

E11 mouse embryo; single biological stage tested in the paper.

## Counter-evidence

Modality dominance could reflect technical artefact (modality-specific coverage / dynamic-range differences) rather than biology; the paper acknowledges RNA's "broader dynamic range" as a confound.

## Linked ideas

## Open questions

- Whether DNAm-dominant regions (W11) represent epigenetically-primed states with not-yet-divergent transcription.
- Genome-wide attribution of which features carry the per-cluster modality dominance.
