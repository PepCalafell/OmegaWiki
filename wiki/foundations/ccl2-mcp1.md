---
title: "CCL2 / MCP-1 — monocyte chemoattractant protein-1"
slug: ccl2-mcp1
domain: "molecular-biology / immunology / chemokine"
status: mainstream
aliases:
  - "CCL2"
  - "MCP-1"
  - "MCP1"
  - "monocyte chemoattractant protein-1"
  - "monocyte chemotactic protein-1"
  - "JE chemokine"
  - "small inducible cytokine A2"
  - "SCYA2"
  - "CCR2 ligand"
  - "monocyte chemoattractant"
  - "MCAF"
  - "macrophage recruitment chemokine"
first_introduced: "Yoshimura, Robinson, Tanaka et al. 1989 J Exp Med (purified MCAF/MCP-1); Charo et al. 1994 PNAS (CCR2 cloning)"
date_updated: 2026-05-08
source_url: "https://www.uniprot.org/uniprot/P13500"
---

## Definition

CCL2 (also known as MCP-1, monocyte chemoattractant protein-1) is the prototypic CC chemokine for monocyte and macrophage recruitment to inflammatory and tumor sites. It is produced by tumor cells, stromal cells, and existing macrophages, and binds primarily to CCR2 (Gαi-coupled GPCR) on classical monocytes (Ly6C^high in mouse, CD14+CD16− in human) to drive their egress from bone marrow and recruitment to target tissues. Under hypoxia, CCL2 is induced via NF-κB and HIF-1α and is a major contributor to the accumulation of tumor-associated macrophages in the hypoxic-niche TME. CCL2-CCR2 axis blockade (carlumab, BMS-813160, PF-04136309) has been tested in oncology with mixed results.

## Intuition

If you want to bring monocytes / macrophages from circulation into a tumor, you make CCL2. Tumors do this constitutively (and more under hypoxia and NF-κB activation) to recruit the monocyte pool that will become TAMs. CCL2 is the dominant monocyte recruitment signal in many cancers (lung, breast, prostate, ovarian). Its therapeutic blockade is mechanistically appealing — fewer monocytes recruited → fewer TAMs → less protumor support — but clinical trials have been disappointing because of redundant chemokine signals (CCL3, CCL4, CCL5, CXCL12 all have macrophage chemoattractant activity).

## Formal notation

Receptor-ligand:
- CCL2 → CCR2 (high affinity) and CCR4 (lower affinity).
- CCR2 also binds CCL7, CCL8, CCL13.

Hypoxic regulation (Bai 2022):
- "Under hypoxic stress, NF-κB/HIF-1α activation encourages lung cancer cells to secrete MCP-1, which furthers the accumulation of macrophages."
- HIF-1α and NF-κB jointly drive CCL2 transcription under hypoxia.

Tumor-TAM crosstalk:
- Tumor-derived CCL2 → CCR2+ monocytes → recruitment to TME → differentiation into TAMs.
- TAM-derived CCL2 → autocrine and paracrine recruitment of more monocytes.
- Inflammatory monocytes (Ly6C^high in mouse) are the principal CCR2+ recruits.

Therapeutics:
- **Carlumab (CNTO 888)**: anti-CCL2 mAb; oncology trials (ovarian, prostate, mCRPC) — limited efficacy.
- **BMS-813160**: dual CCR2/CCR5 antagonist; oncology and inflammation trials.
- **PF-04136309**: CCR2 antagonist; tested in pancreatic cancer with FOLFIRINOX combination.
- **Cenicriviroc**: CCR2/CCR5 antagonist; tested in NASH.

## Key variants

- *CCL2 (MCP-1)*: prototypic, dominant in many tumors.
- *CCL7 (MCP-3)*: related, broader CCR2/CCR1/CCR3 binding.
- *CCL8 (MCP-2)*: see Bai 2022 cervical cancer mechanism (Zeb1-driven, CCR2-NF-κB, TAM infiltration).
- *CCL13 (MCP-4)*: CCR2 ligand, allergic inflammation enrichment.

## Known limitations

- Anti-CCL2 monotherapy has shown limited clinical efficacy due to redundant chemokines and rebound CCL2 elevation after antibody clearance.
- CCR2 antagonists have variable bioavailability and PD effects.
- Mouse-human translation: mouse "JE" is the CCL2 ortholog, with some species differences.
- TAM-derived autocrine CCL2 makes blockade harder than tumor-cell CCL2 blockade alone.

## Open problems

- Optimal combination of CCR2 antagonism with checkpoint blockade in TAM-rich tumors.
- Whether intermittent vs sustained CCL2 blockade gives better TAM depletion.
- Predictive biomarker (CCL2 plasma, CCR2+ monocyte frequency).

## Relevance to active research

CCL2/MCP-1 is foundational for TAM recruitment biology. In [[papers/hypoxia-driven-crosstalk-between-tumor-tumor]] (Bai 2022), CCL2 appears in the TAM recruitment section as a hypoxia-driven NF-κB/HIF-1α target in lung cancer that drives macrophage accumulation in the hypoxic niche. For my hypoxia-NF-κB-macrophage thesis, CCL2 is both an upstream signal that recruits TAMs into hypoxic regions and a downstream output of hypoxic NF-κB activation in macrophages — relevant on both sides.
