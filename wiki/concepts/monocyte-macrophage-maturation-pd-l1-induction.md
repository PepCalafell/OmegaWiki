---
title: "PD-L1 upregulation during monocyte-to-macrophage maturation is IFN-γ-independent and ERK-dependent"
aliases:
  - "monocyte-macrophage PD-L1 maturation"
  - "IFN-gamma independent PD-L1"
  - "ERK-driven PD-L1 induction"
  - "PD-L1 as maturation marker"
  - "monocyte differentiation PD-L1"
  - "adherent monocyte PD-L1"
  - "ex vivo monocyte PD-L1"
  - "MAPK PD-L1 monocyte"
  - "IFN-gR1 PD-L1+ monocyte"
  - "PD-L1 maturation axis"
tags:
  - PD-L1
  - monocyte
  - macrophage
  - maturation
  - ERK
  - MAPK
  - IFN-gamma
  - differentiation
maturity: emerging
key_papers:
  - pd-l1-expressing-tumor-associated-macrophages
first_introduced: "Wang et al. 2024 Cell Reports Medicine — direct demonstration that PD-L1 is upregulated during monocyte→macrophage differentiation in serum-free, IFN-γ-blocked conditions; ERK inhibition specifically blocks induction"
date_updated: 2026-05-12
related_concepts:
  - pd-l1-immunostimulatory-tam-phenotype
  - macrophage-ontogeny-resident-vs-monocyte-derived
---

## Definition

PD-L1 is upregulated on peripheral blood monocytes during their differentiation/maturation into macrophages independent of IFN-γ — the canonical inducer of PD-L1. This contradicts the textbook framing of PD-L1 as a JAK-STAT1-IRF1 inflammatory response gene and re-positions PD-L1 as a *maturation marker* in the monocyte-macrophage lineage. The induction is partially ERK1/2-dependent (blocked by SCH772984) and does not require external IFN-γ stimulus, as PD-L1 upregulation persists when monocytes are rested in serum-free medium with IFN-γ and IFN-γR blocking antibodies.

## Mechanistic features (Wang 2024)

1. Fresh peripheral blood monocytes from breast cancer patients show low surface PD-L1; 8h ex vivo resting (RPMI 1640 + 10% FBS) is sufficient to upregulate PD-L1.
2. PD-L1 is higher on adherent monocytes/macrophages than on suspension monocytes after resting — consistent with adhesion-coupled maturation.
3. In vitro M-CSF-driven differentiation yields uniformly PD-L1+ macrophages.
4. PD-L1 upregulation persists in serum-free medium with anti-IFN-γ + anti-IFN-γR blocking antibodies → IFN-γ-independent.
5. PD-L1+ monocytes/macrophages co-upregulate maturation markers (CD54, CD69, CD83), MHC-II (HLA-DR), co-stimulatory ligands (CD40, CD80, CD86), co-inhibitory ligands (PD-L2, B7-H3, B7-H4), Fcγ receptors (CD16, CD32, CD64), and chemokine receptors (CSF1R, CCR5).
6. PD-L1+ monocytes show elevated phosphorylation of STAT1, STAT3, mTOR, and Akt by phosflow.
7. Small-molecule inhibitor screen: ERK1/2 (SCH772984, 0.5 μM) significantly suppresses PD-L1 upregulation; STAT1, Akt, PI3K, NF-κB, mTOR inhibitors do not.
8. PD-L1+ monocytes/macrophages have higher IFN-γR1 surface levels and respond more strongly to subsequent IFN-γ stimulation (higher ΔpSTAT1+%) — i.e., they are primed for IFN-γ response, but IFN-γ is not required for the initial induction.

## Counterpoint: cancer cells

In contrast to TAMs, PD-L1−/lo *cancer cells* show stronger IFN-γ-induced pSTAT1 response than PD-L1+/hi cancer cells (opposite direction). This dissociates the IFN-γ→PD-L1 pathway in cancer cells from the IFN-γ-independent maturation pathway in monocyte-derived macrophages.

## Therapeutic implications

- PD-L1 quantification on monocytes/macrophages may misrepresent inflammatory state if interpreted only as an IFN-γ response.
- Modulating monocyte maturation (e.g., ERK pathway) may alter PD-L1+ TAM abundance independently of inflammatory cytokine context.
- The IFN-γ-independent route may explain why intratumoral PD-L1 IHC has limited prognostic value: TAM PD-L1 reflects maturation, not necessarily an active anti-tumor immune response.

## Known limitations

- ERK inhibition only partially suppresses PD-L1; additional pathways (e.g., chromatin-state changes during differentiation) are likely co-active.
- In vitro M-CSF differentiation may not capture tumor-niche-specific maturation cues.
- Whether this maturation-driven PD-L1 is functionally equivalent (immunostimulatory) to PD-L1 induced by IFN-γ is not directly tested.

## Open problems

- The transcriptional regulators downstream of ERK driving PD-L1 in maturing monocytes (FOS, JUNB, CEBPD candidates).
- Whether adhesion (integrin signaling) is causal upstream of ERK→PD-L1.
- The role of monocyte-extrinsic cues (tumor-derived chemokines, ECM stiffness) in vivo.
- Whether GM-CSF-differentiated MoDMs (e.g., DC-like) show the same maturation-driven PD-L1 induction.

## Key papers

- [[papers/pd-l1-expressing-tumor-associated-macrophages]] — Wang et al. 2024 Cell Reports Medicine. Direct demonstration of IFN-γ-independent and ERK-dependent PD-L1 induction during monocyte-to-macrophage maturation.
