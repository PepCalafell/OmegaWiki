---
title: "In colon cancer, hypoxia decreases macrophage SIRPα while increasing tumor CD47, paradoxically enhancing phagocytosis"
slug: hypoxia-sirpa-cd47-paradox-colon-cancer-phagocytosis
status: supported
confidence: 0.65
tags:
  - SIRPα
  - SIRPA
  - CD47
  - hypoxia
  - phagocytosis
  - colon-cancer
  - paradoxical-effect
  - dual-edged-hypoxia
  - immune-checkpoint
domain: "immunology / oncology / phagocytosis"
source_papers:
  - hypoxia-driven-crosstalk-between-tumor-tumor
evidence:
  - source: hypoxia-driven-crosstalk-between-tumor-tumor
    type: supports
    strength: medium
    detail: "Bai 2022 (DOI 10.1186/s12943-022-01645-2, p.12) reviews the SIRPα-CD47 'don't eat me' axis under hypoxia: HIF activates CD47 in many cancers (eat-me signal up), BUT in colon cancer specifically, hypoxia decreases macrophage SIRPα expression while simultaneously increasing tumor CD47, with the net effect tilting toward enhanced phagocytosis. This may partly explain colon cancer's better prognosis with M2-rich / HIF-1α-high tumors than other cancers."
conditions: "Colon-cancer specific; documented in vitro and in human IHC studies (Qi 2020 Front Oncol)."
date_proposed: 2026-05-11
date_updated: 2026-05-11
---

## Statement

The SIRPα-CD47 axis is the major "don't eat me" checkpoint: CD47 on tumor cells engages SIRPα on macrophages, inhibiting phagocytosis. Hypoxia generally activates CD47 transcription via HIF, increasing the "don't eat me" signal. In colon cancer this expected directionality is paradoxically inverted: hypoxia *decreases* SIRPα on macrophages even as it *increases* CD47 on tumor cells. The net effect tilts toward *enhanced* (not suppressed) phagocytosis. This may explain why colon cancer — despite being M2-TAM-rich and HIF-1α-high — has a better prognosis than other cancers with the same hypoxic / TAM profile. Mechanistically, this means SIRPα-CD47 blockade may have *reduced* efficacy in colon cancer relative to other tumors, because the system is already tilted toward phagocytosis under hypoxia.

## Evidence summary

- [[papers/hypoxia-driven-crosstalk-between-tumor-tumor]] — Bai 2022 *Molecular Cancer*.
- Concept: [[concepts/sirpa-cd47-don-t-eat-me-axis]].
- Primary: Qi 2020 Front Oncol on hypoxic colorectal cancer and SIRPα-CD47.

## Conditions and scope

- Colon cancer specific; other cancers (NSCLC, breast, ovarian) show the canonical direction (CD47 up + SIRPα maintained → reduced phagocytosis).
- Translational implication: SIRPα-CD47 blockade clinical trials (e.g. magrolimab) should stratify colon cancer patients separately.

## Counter-evidence

- The colon-cancer prognosis benefit may be driven by other factors (microbiome, MSI status, immune-rich subtypes) rather than the SIRPα-CD47 paradox specifically.
- Some studies report intact SIRPα expression in hypoxic colon-cancer-associated macrophages; the SIRPα downregulation may be subtype-specific.

## Linked ideas

(none yet)

## Open questions

- Is the colon-cancer paradox tumor-cell-intrinsic (hypoxic colon tumors release a signal that downregulates SIRPα on TAMs) or TAM-cell-intrinsic (hypoxic colon-tumor TAMs lose SIRPα via mechanisms common to other tissues)?
- Does the paradox persist under cyclic hypoxia or only chronic hypoxia?
- Should magrolimab and other CD47-axis drugs avoid colon cancer specifically?
