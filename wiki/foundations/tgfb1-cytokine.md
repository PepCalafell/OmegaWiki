---
title: "TGFβ — transforming growth factor β"
slug: tgfb1-cytokine
domain: cell biology / immunology / developmental biology
status: mainstream
aliases:
  - "TGFβ"
  - "TGF-β"
  - "TGFβ1"
  - "TGFB1"
  - "transforming growth factor beta"
  - "TGFβ family"
  - "TGFβ2"
  - "TGFβ3"
  - "latent TGFβ complex"
  - "TGFβ-SMAD signaling"
  - "anti-inflammatory cytokine TGFβ"
first_introduced: "Roberts & Sporn 1981 (TGFβ purification); reviewed in Massagué 2012 Cell"
date_updated: 2026-05-06
source_url: ""
---

## Definition

TGFβ (transforming growth factor β) is a master pleiotropic cytokine with three mammalian isoforms (TGFβ1, TGFβ2, TGFβ3) that signals via heterodimeric type I/II serine-threonine kinase receptors (TGFBR1/2 = ALK5/TβRII) to drive SMAD2/3 phosphorylation and SMAD4-coupled nuclear translocation. TGFβ controls developmental specification (including macrophage tissue-specific identity in the niche), tissue repair, immune suppression, fibrosis, and tumour progression. Its outputs are highly context-dependent: pro-tumour in late cancer, anti-inflammatory in homeostasis, pro-fibrotic when chronic.

## Intuition

TGFβ is one of the body's most context-sensitive cytokines — it can suppress inflammation in homeostasis, drive fibrosis when chronic, instruct macrophage tissue identity in development, support tumour progression in late cancer, and act as tumour suppressor in early epithelium. Its biology is regulated at multiple layers: latent secretion, integrin-mediated activation, dose dependence, and downstream SMAD vs non-SMAD signalling. TGFβ is the canonical *niche signal* for several TRM identities — it instructs PPARγ in alveolar macrophages (with CSF2), SALL1 in microglia, ID3 in Kupffer cells.

## Formal notation

- Genes: *TGFB1*, *TGFB2*, *TGFB3*
- Receptor complex: TβRII (TGFBR2; binds ligand) + TβRI/ALK5 (TGFBR1; downstream kinase)
- Canonical signalling: SMAD2/3 phosphorylation → SMAD4 complex → nuclear translocation → TGFβ-target gene transcription
- Non-canonical signalling: TAK1 → MAPK; PI3K-AKT; Rho-ROCK
- Latency: secreted as latent complex bound to LAP (latency-associated peptide) and LTBP; activated by integrins (αVβ6, αVβ8), proteases, ROS, mechanical stress
- Macrophage context:
  - Niche-derived TGFβ instructs LDF expression (PPARγ in alveolar mac, SALL1 in microglia, ID3 in Kupffer)
  - Anti-inflammatory output of efferocytosis includes TGFβ secretion
  - Driver of macrophage M2-polarization (with IL-4, IL-13)
  - Pro-fibrotic in BMDM-driven tissue fibrosis
- Disease:
  - Marfan syndrome (FBN1 mutations dysregulate TGFβ)
  - Loeys-Dietz syndrome (TGFBR1/2 mutations)
  - Pulmonary, hepatic, renal fibrosis
  - Cancer: late-stage tumour progression, immunosuppression, EMT
  - Autoimmunity: regulatory T-cell maintenance defects (Treg-TGFβ axis)

## Key variants

- TGFβ1 — most abundant, broadly expressed
- TGFβ2 — eye, heart, embryo
- TGFβ3 — palate, lung
- LAP (latency-associated peptide) — non-covalent association with mature TGFβ
- LTBP1-4 — latent TGFβ-binding proteins; matrix anchoring
- BMP family (BMP2/4/7) — related TGFβ-superfamily ligands; SMAD1/5/8 downstream

## Known limitations

- Pleiotropy makes systemic TGFβ blockade unsafe (cardiac, autoimmunity side effects).
- Latent vs active TGFβ measurement is technically difficult; many "TGFβ" studies measure total without activation status.
- Mouse-to-human translation incomplete — TGFβ isoform usage differs.

## Open problems

- Targeted TGFβ blockade for cancer immunotherapy (anti-TGFβ + anti-PD-1 combinations) — clinical signal mixed.
- The integrin-dependent activation step in fibrosis — whether αVβ6 / αVβ8 inhibitors can selectively block pathological TGFβ.
- Role of TGFβ in maintaining vs disrupting TRM identity during chronic disease.

## Relevance to active research

For my hypoxia-NF-κB work: TGFβ is a *competing* signal — hypoxia + NF-κB drives pro-inflammatory output (TNF, IL-6); TGFβ drives anti-inflammatory and fibrotic output. The two pathways cross-talk extensively (SMAD-NF-κB cross-regulation, HIF-SMAD interactions). Tumour macrophages often experience both signals simultaneously, and the integration logic is poorly understood. TGFβ is also the canonical "homeostatic" signal that hypoxic NF-κB likely *displaces* in our experimental system; framing my findings explicitly in TGFβ-vs-NF-κB terms could sharpen the interpretation.
