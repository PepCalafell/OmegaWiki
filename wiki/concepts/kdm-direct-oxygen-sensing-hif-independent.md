---
title: "KDM6A and KDM5A as direct oxygen sensors independent of HIF"
aliases:
  - "KDM6A oxygen sensing"
  - "KDM5A oxygen sensing"
  - "histone demethylase oxygen sensor"
  - "non-HIF oxygen sensor"
  - "H3K27me3 hypoxia"
  - "H3K4me3 hypoxia"
  - "Chakraborty 2019 KDM6A"
  - "histone modification oxygen"
  - "chromatin oxygen sensor"
  - "JmjC domain oxygen sensing"
  - "HIF-independent hypoxia signaling"
tags:
  - histone-demethylase
  - KDM6A
  - KDM5A
  - oxygen-sensor
  - chromatin
  - epigenetics
  - hypoxia
  - HIF-independent
  - JmjC-domain
maturity: emerging
key_papers:
  - hypoxia-driven-crosstalk-between-tumor-tumor
  - hypoxia-signaling-human-health-diseases-implications
first_introduced: "Chakraborty 2019 Science (KDM6A directly senses oxygen to control chromatin and cell fate); Gallipoli & Huntly 2019 Science perspective; Batie 2019 Science (KDM5A); reviewed Bai 2022"
date_updated: 2026-05-08
related_concepts:
  - tumor-hypoxia-classification-chronic-acute-cyclic
---

## Definition

A class of α-ketoglutarate-dependent dioxygenase histone demethylases — exemplified by KDM6A (UTX) and KDM5A — that act as *direct* oxygen sensors of the cell, regulating histone-tail methylation status (H3K27me3 and H3K4me3 respectively) and thereby chromatin accessibility and gene expression independently of the canonical HIF / PHD / VHL / FIH axis. Like the PHDs, these JmjC-domain enzymes require Fe(II), 2-oxoglutarate (2OG), and molecular oxygen for catalysis; their KM for O₂ is in the physiological pO₂ range, so they lose activity under hypoxia. Hypoxic inactivation of KDM6A → persistent H3K27me3 → blocked cell-fate programs (e.g. terminal differentiation); hypoxic inactivation of KDM5A → persistent H3K4me3 → altered transcriptional readiness. The discovery (Chakraborty 2019 *Science*) re-frames oxygen sensing as a *chromatin-level* process in addition to the well-known HIF transcriptional response, expanding the menu of cellular hypoxia outputs.

## Intuition

For two decades, "oxygen sensing" was nearly synonymous with the HIF-PHD-VHL axis: low O₂ → HIF stabilizes → transcriptional response. The 2019 Chakraborty + Batie work showed that *chromatin enzymes* themselves, with their O₂-dependent JmjC catalysis, are an independent oxygen-sensing layer. This makes biological sense: cells need to know oxygen levels for fate decisions (differentiation, stemness) that operate on epigenetic timescales, not just metabolic timescales. The HIF axis handles fast transcriptional responses; KDM oxygen sensing handles slower epigenetic programming. The two layers can interact (HIF target genes include some KDMs), but they are mechanistically distinct.

## Formal notation

Mechanism:
- KDMs are JmjC-domain α-KG-dependent dioxygenases.
- Co-substrates: Fe(II), 2-oxoglutarate, O₂.
- Catalytic cycle: KDM-Fe(II)-2OG-O₂ → KDM-Fe(IV)=O (ferryl intermediate) → demethylation of histone-tail Lys-Me / Lys-Me2 / Lys-Me3 → succinate + CO₂ + Fe(II).
- KM for O₂: in the physiological pO₂ range (~100-300 µM in normoxic cells), so substrate-limited under hypoxia.

Specific enzymes (Bai 2022 cites):
- **KDM6A (UTX)**: removes H3K27me2/me3 marks. Hypoxia inactivation → H3K27me3 persistence → blocked differentiation.
- **KDM5A**: removes H3K4me2/me3 marks. Hypoxia inactivation → H3K4me3 persistence → altered transcription.

Outputs:
- Cell-fate / differentiation control.
- Stemness modulation in hypoxic stem-cell niches.
- Cancer cell hypoxic adaptation independent of HIF transcription.
- Differential outcomes from chronic vs cyclic hypoxia (different exposure profiles to O₂-dependent demethylase).

Inhibitors:
- KDM-selective inhibitors are in development (GSK-J4 for KDM6A, others for KDM5A).
- Pharmacological mimicry of hypoxic KDM inactivation.

## Variants

- *KDM6A* (UTX) — H3K27me3 demethylase.
- *KDM5A* (RBP2/JARID1A) — H3K4me3 demethylase.
- Other JmjC-domain demethylases (KDM2, KDM3, KDM4, KDM7, KDM8 families) — variable O₂-sensitivity; ongoing research.
- *Cell-type-specific output*: the same hypoxic KDM inactivation drives different transcriptional consequences depending on which loci are H3K27me3-regulated in the cell type.

## Comparison

vs HIF axis: HIF responds via stabilization-and-translocation of a transcription factor; KDM responds via loss-of-catalysis on chromatin. HIF is fast (minutes-hours); KDM may be slower (hours-days for chromatin remodeling).
vs PHDs: structurally similar (Fe(II)/2OG-dependent dioxygenases), but PHDs hydroxylate HIF-α, KDMs demethylate histones. Both lose activity under hypoxia, but KDM loss does not drive HIF stabilization — they are parallel sensors.
vs FIH: FIH is also a JmjC-domain enzyme but acts on HIF-α asparagine, not histones; KDMs act on histones, not HIF. Different substrate specificity but same dioxygenase chemistry.
vs sirtuin / HDAC chromatin regulators: HDACs / sirtuins are not O₂-dependent and do not act as oxygen sensors.

## When to use

- When interpreting hypoxic cancer transcriptomes that include differentiation-blocked / stemness-elevated programs not predicted by HIF target genes alone.
- When designing hypoxia-mimicking compound screens: HIF-pathway-only readouts will miss KDM-axis hypoxic effects.
- For epigenetic-profiling experiments under hypoxia: H3K27me3 and H3K4me3 ChIP-seq are the direct readouts of KDM oxygen-sensor activity loss.
- For interpreting why some hypoxic phenotypes (de-differentiation, EMT-stem hybrid states) are *not* fully reproducible in HIF-overactivated normoxia (HIF-stabilizing compounds like CoCl₂).

## Known limitations

- The discovery is recent (2019); long-term replication and cancer-specific validation are still accumulating.
- KDM-axis oxygen sensing has been demonstrated in specific cell-fate / differentiation systems; broad cancer-cell evidence is more limited.
- Cross-talk with HIF axis is incompletely characterized — some KDMs are themselves HIF target genes (KDM3A, KDM4B, KDM6B).
- KDM-specific inhibitors are research tools, not yet clinically validated.

## Open problems

- A complete map of which KDMs are O₂-substrate-limited at physiological tumor hypoxia (pO₂ < 10 mmHg) — KMs vary across the family.
- Whether KDM oxygen sensing dominates or merely modulates the HIF transcriptional response in hypoxic cancer cells in vivo.
- Therapeutic exploitation: KDM inhibitors as hypoxia-mimetic compounds, or KDM activators as anti-hypoxia compounds.
- Cross-talk with the metabolic state: 2-OG and succinate are competing co-substrates / inhibitors of KDMs; oncometabolite states (SDH-deficient paragangliomas, IDH-mutant gliomas) overlap with KDM regulation.

## Key papers

- [[papers/hypoxia-driven-crosstalk-between-tumor-tumor]] — Bai et al. 2022 *Molecular Cancer*. The "Oxygen sensing mechanisms" section foregrounds KDM6A and KDM5A as direct O₂ sensors as a key 2019 advance, motivating that "the mechanisms of tumor hypoxic adaptation are more complex than currently envisaged."

## My understanding

For my thesis, the KDM-axis oxygen sensor is a complementary epigenetic lens on hypoxic macrophages. My NF-κB+TET2-driven DNA demethylation program operates on CpG methylation; the KDM axis operates on histone methylation. Both layers are relaxed under hypoxia and may co-cooperate to make chromatin more accessible. An interesting cross-cutting question: does hypoxia in macrophages drive H3K27me3 persistence (KDM6A inactivation) at the same loci where TET2-driven demethylation is occurring? If so, the chromatin would have an unusual signature — high accessibility (TET-driven 5mC removal) plus retained polycomb-repressive mark (H3K27me3) — testable in ChIP-seq + WGBS data.
