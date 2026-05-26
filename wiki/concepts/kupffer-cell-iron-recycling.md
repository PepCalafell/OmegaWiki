---
title: "Kupffer cell iron recycling and erythrophagocytosis"
aliases:
  - "Kupffer cell iron metabolism"
  - "iron recycling macrophage"
  - "ferroportin macrophage iron export"
  - "senescent erythrocyte clearance liver"
  - "RBC erythrophagocytosis"
  - "haem catabolism Kupffer"
  - "iron homeostasis liver"
  - "Kupffer cell ferroportin"
  - "stressed erythrocyte phagocytosis"
tags:
  - kupffer-cell
  - liver
  - iron-metabolism
  - ferroportin
  - macrophage
  - homeostasis
maturity: stable
key_papers:
  - physiology-diseases-tissue-resident-macrophages
  - metabolism-tissue-macrophages-homeostasis-pathology
first_introduced: "Knutson 2003 (ferroportin in macrophage iron export); Kohyama 2009 Nature (SPI-C in red pulp); reviewed in Lazarov & Geissmann 2023"
date_updated: 2026-05-06
related_concepts:
  - macrophage-ontogeny-resident-vs-monocyte-derived
  - tissue-specific-lineage-determining-factors-macrophage
---

## Definition

Kupffer cells — the resident liver macrophages — phagocytose circulating senescent or damaged red blood cells (RBCs), digest them within phagolysosomes, and recycle the released iron back into systemic circulation via the ferroportin transporter. The iron is then bound to transferrin in plasma, supplying erythropoiesis in bone marrow. Kupffer-cell-mediated iron recycling is the dominant pathway for daily iron turnover in mammals (~25 mg/day in humans, vs ~1–2 mg/day from dietary absorption).

## Intuition

The body cannot afford to lose iron — it is biologically expensive. Senescent RBCs (~120-day lifespan in humans) are recognized by Kupffer cells via "eat-me" signals (PtdSer flip, decreased CD47). Phagocytosed RBCs are processed in phagolysosomes; haem is degraded by haem oxygenase to release Fe²⁺; ferritin stores excess intracellular iron; ferroportin (the only known iron exporter) transports Fe out of the macrophage to plasma transferrin. Hepcidin (liver-derived peptide) regulates ferroportin levels by ubiquitinating and internalizing it — coupling iron status to release.

## Formal notation

- **Substrate**: senescent or damaged RBCs (CD47-low, PtdSer-high)
- **Recognition**: macrophage receptors include SIRPα (CD47 sensor), TAM receptors (PtdSer via bridging ligands), scavenger receptors
- **Processing**: phagolysosomal haem degradation via haem oxygenase 1 (HMOX1)
- **Storage**: ferritin (intracellular iron storage)
- **Export**: ferroportin (SLC40A1) — sole iron exporter
- **Plasma carrier**: transferrin
- **Regulation**: hepcidin → ferroportin internalization/degradation
- **Diseases**:
  - Hereditary haemochromatosis (HFE / HJV / TFR2 / SLC40A1 mutations) — failure of hepcidin-ferroportin axis → iron overload
  - Anaemia of chronic inflammation — IL-6-driven hepcidin upregulation → ferroportin loss → iron sequestration in macrophages
  - SPI-C deficiency (mouse Kohyama 2009) — loss of red pulp macrophages and splenic iron homeostasis defect

## Variants

- *Kupffer cell iron recycling* (steady state) — primary pathway.
- *Splenic red pulp macrophage iron recycling* — parallel pathway; SPI-C-dependent; haem-induced LDF.
- *BMDM-mediated iron recycling under stress* — high-demand erythrophagocytosis recruits ferroportin-expressing BMDMs to liver; transient population that disappears when demand subsides (Theurl et al. 2016 *Nat Med*).

## Comparison

vs other Kupffer functions: iron recycling is one of several Kupffer functions; others include LPS clearance, anti-tumour cytotoxicity, hepatocyte trophic support via WNT and HGF. Iron recycling is distinguished by its quantitative dominance and direct organ-physiology coupling.
vs gut iron absorption: gut absorbs ~1–2 mg/day; Kupffer recycling delivers ~25 mg/day. The two are complementary; Kupffer dysfunction is not compensated by dietary iron.

## When to use

- Interpreting iron-overload phenotypes in macrophage-conditional knockouts.
- Designing inflammation-induced anaemia therapies (target hepcidin / ferroportin).
- Predicting which haematological diseases stress the Kupffer iron-recycling axis (haemolytic anaemias, malaria, transfusion overload).

## Known limitations

- Most quantitative kinetics derive from rodent studies; human throughput is estimated, not directly measured.
- The split between Kupffer-cell vs splenic red pulp iron recycling under various physiological states is not cleanly resolved.
- Aged Kupffer cells lose efficiency — relevance to age-related anaemia is underexplored.

## Open problems

- Whether BMDM-derived ferroportin-expressing iron-recyclers persist long enough to acquire Kupffer-like programmes.
- Cross-talk between Kupffer iron handling and lipid-droplet biology in MASH/NAFLD livers.
- Tumour-context iron recycling — whether liver tumours sequester or scavenge iron via Kupffer subversion.

## Key papers

- [[papers/physiology-diseases-tissue-resident-macrophages]] — Lazarov & Geissmann 2023 *Nature* — section on liver Kupffer cells covering RBC phagocytosis, ferroportin export, and the BMDM-takeover under high iron demand

## My understanding

Iron recycling is canonical "ancillary cell" biology — Kupffer cells exist to support hepatocyte and erythropoietic demand. For my hypoxia work this is tangentially relevant: hypoxia upregulates HIF1α/HIF2α, which interact with iron homeostasis (HIF2α is iron-regulated; haem-binding regulates HIF stability via PHD enzymes). Whether hypoxic Kupffer cells redistribute their iron-handling vs inflammatory functions is not well covered in the Lazarov review and could be a productive integrative question.
