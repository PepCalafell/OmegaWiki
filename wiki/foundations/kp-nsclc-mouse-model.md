---
title: "KP NSCLC mouse model (KrasG12D / Trp53fl/fl lung adenocarcinoma)"
slug: kp-nsclc-mouse-model
domain: "oncology / immunology / mouse genetics"
status: mainstream
aliases:
  - "KP model"
  - "KP NSCLC"
  - "KP lung adenocarcinoma"
  - "KrasG12D Trp53 mouse model"
  - "K-rasG12D p53fl/fl"
  - "LSL-KrasG12D Trp53fl/fl"
  - "KP orthotopic tumor model"
  - "DuPage KP model"
  - "KP-GFP cell line"
  - "tail-vein KP injection"
  - "SPC-Cre KP genetic NSCLC"
first_introduced: "Jackson et al. *Nature* 2001 (LSL-KrasG12D); DuPage, Dooley & Jacks *Nature Protocols* 2009 (Cre-recombinase delivery); Sutherland et al. *PNAS* 2014 (cell-of-origin)"
date_updated: 2026-05-06
source_url: "https://doi.org/10.1038/nprot.2009.95"
---

## Definition

The KP NSCLC mouse model uses lung epithelial cells carrying conditional alleles of oncogenic K-Ras (LSL-KrasG12D, Jackson Lab 008179) and floxed Trp53 (Trp53fl/fl, Jackson Lab 008462). Cre-recombinase delivery — by adenovirus (SPC-Cre intratracheal instillation, autochthonous model) or by genetic crossing followed by ex vivo recombination and orthotopic transplantation — drives Kras activation and p53 deletion specifically in lung type II pneumocytes, generating lung adenocarcinomas histologically and molecularly resembling human NSCLC. The transplantable variant uses GFP-labelled KP cell lines injected via tail vein (5×10⁵ cells per mouse) to seed tumour foci in the lungs over 5–30 days.

## Intuition

KP is the mouse genetic standard for NSCLC: it pairs the most common driver oncogene in human NSCLC (KRAS-G12D, ~30%) with the most common tumour-suppressor loss (TP53, ~50%). The model captures both the molecular initiation and the histological progression of human lung adenocarcinoma, and its orthotopic transplantable form provides reproducible kinetics for studying immune-tumour interactions over a defined timeline.

## Key variants

- **Autochthonous KP** (SPC-Cre adenovirus / lentivirus): Cre delivered intratracheally to LSL-KrasG12D Trp53fl/fl mice; tumours form spontaneously in lung type II pneumocytes; closer to human disease but slower and less synchronous
- **Orthotopic KP-GFP transplant** (Casanova-Acebes 2021 use): KP cells genetically labelled with GFP, expanded in vitro, injected via tail vein; rapid reproducible tumour seeding (day 5–30 timeline)
- **KrasG12D-only model**: less aggressive, slower progression
- **KP + immune-checkpoint variants**: KP crossed with PD-L1-KO or other immune modulators
- **B16-F10/OVA syngeneic melanoma**: companion model for non-lung cancer comparison (used in Casanova-Acebes 2021 to validate TRM depletion phenotype across tumour types)

## Known limitations

- Pure C57BL/6 background limits MHC haplotype diversity and clinical translation
- Orthotopic transplant model bypasses early epithelial transformation events (already-transformed cells)
- Mouse lung anatomy and immune compartment differ from human (e.g., bronchial-associated lymphoid tissue, alveolar macrophage density)
- Tumour cells in transplant models are clonal; intratumour heterogeneity is reduced
- Lacks the smoking/inflammation context of most human NSCLC

## Open problems

- Better integration of lung-microbiome and inflammation context
- Humanised KP variants for testing human-targeted therapeutics
- Models that recapitulate the slow progression and field cancerisation of human disease

## Relevance to active research

[[papers/tissue-resident-macrophages-provide-pro-tumorigenic]] uses orthotopic KP-GFP injection (5×10⁵ cells, tail vein) to establish a tractable day-5-to-day-30 NSCLC progression timeline, enabling spatial imaging of TRM-tumour contact, longitudinal scRNA-seq, and CD169-DTR-mediated TRM depletion before tumour engraftment. The model is the workhorse for studying early-stage TRM niche function in lung cancer.
