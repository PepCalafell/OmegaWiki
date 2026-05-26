---
title: "Recurrent malignant metaprograms (NMF-derived)"
aliases:
  - metaprogram
  - MP
  - malignant metaprogram
  - tumor metaprogram
  - recurrent expression program
  - recurrent ITH program
  - NMF metaprogram
  - Tirosh metaprogram
  - 3CA metaprogram
  - hallmarks of ITH
  - pan-cancer malignant programs
  - recurrent transcriptional state
tags: [scrna-seq, nmf, ith, metaprograms, malignant-cells, pan-cancer]
maturity: stable
key_papers:
  - curated-cancer-cell-atlas-provides-comprehensive
first_introduced: "2023 (Gavish et al.); refined 2025 (Tyler et al.)"
date_updated: 2026-05-26
related_concepts: [curated-cancer-cell-atlas-3ca, tumor-hypoxia-intratumoral-heterogeneity, crc-stemness-metaprogram, snrna-vs-scrna-metaprogram-differences]
---

## Definition

Recurrent malignant metaprograms (MPs) are clusters of NMF-derived gene programs that recur across tumours and patients, summarising the dominant axes of transcriptional intratumour heterogeneity (ITH) in malignant cells. Each MP is represented by its top-50 genes ranked by dataset recurrence.

## Intuition

Run NMF per tumour with K=4–9 to extract latent programs; keep programs that are (i) robust within the tumour (overlap across K), and (ii) robust across tumours (overlap with programs from other samples); cluster these robust programs by Jaccard overlap into MPs. The result captures shared "themes" of ITH — cell cycle, EMT, hypoxia, interferon/MHC-II, EpiSen, MYC, secreted, NPC, etc. — that recur across patients and cancer types.

## 3CA v2 program inventory (67 MPs)

Cell cycle (G1/S, G2/M, HMG-rich, single-nucleus variant), Chromatin, Stress (1, 2, in vitro), Hypoxia, Unfolded protein response (1, 2), Proteasomal degradation, Protein maturation, Translation initiation, EMT-I to EMT-VI, Mesenchymal (glioma), Interferon/MHC-II (I, II, III), EpiSen (Epithelial Senescence, plus HNSCC-specific), MYC, Respiration (1, 2, HNSCC), Secreted (I, II), Cilia (1, 2 — snRNA-seq variant), Astrocytes, NPC glioma, Oligo Progenitor, Oligo normal, NPC/OPC (and snRNA-seq variant), PDAC classical and PDAC-related (1–5), Alveolar, Skin pigmentation, RBCs, Platelet activation, Hemato-related (I–IV), IG, Glutathione, Metal-response, NRF2 targets, P53, Adherens, Cholesterol homeostasis, Complement and coagulation (liver), CRC stemness, Colon-related, Androgen response (prostate), Unassigned (1, 2).

## Variants

- **Single-nucleus-specific MPs** ([[concepts/snrna-vs-scrna-metaprogram-differences]]) — cell-cycle and cilia variants that appear mostly in snRNA-seq samples.
- **Tumour-type-specific MPs** — e.g. [[concepts/crc-stemness-metaprogram|CRC stemness]], PDAC classical, NPC glioma, Skin pigmentation.

## When to use

- To score each malignant cell against a panel of pan-cancer states.
- To quantify the diversity of intratumour heterogeneity in a new dataset.
- To compare programs identified in a new study against an established compendium of recurrent states.

## Known limitations

- The MP set is biased by the cancer-type composition of the input atlas.
- snRNA-seq contributes disproportionately to some MPs (e.g. cell cycle, cilia variant).
- Statistical thresholds for "robust" NMF programs are heuristic.
- Some MPs near borders may be merged or split depending on clustering parameters.

## Key papers

- [[curated-cancer-cell-atlas-provides-comprehensive]] — 67 MPs, 3CA v2.

## My understanding

The malignant-cell MP framework has become the de facto vocabulary for pan-cancer scRNA-seq ITH. For the thesis, the hypoxia MP and the new NRF2-targets MP are the obvious entry points; the cell-cycle MPs anchor the proliferation/phase-bias story.
