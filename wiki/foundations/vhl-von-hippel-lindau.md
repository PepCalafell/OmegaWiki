---
title: "VHL — Von Hippel-Lindau tumor suppressor / E3 ubiquitin ligase"
slug: vhl-von-hippel-lindau
domain: "molecular-biology / hypoxia-signaling / oncology"
status: mainstream
aliases:
  - "VHL"
  - "pVHL"
  - "Von Hippel-Lindau protein"
  - "Von Hippel-Lindau tumor suppressor"
  - "VHL E3 ubiquitin ligase"
  - "VHL gene"
  - "VHL disease gene"
  - "VBC complex"
  - "VHL/Elongin B/C/Cul2 complex"
  - "HIF-α ubiquitin ligase"
first_introduced: "Latif et al. 1993 Science (positional cloning of VHL); Maxwell, Wiesener et al. 1999 Nature (VHL targets HIF-1α for ubiquitination)"
date_updated: 2026-05-08
source_url: "https://www.uniprot.org/uniprot/P40337"
---

## Definition

VHL is the tumor-suppressor protein encoded by the VHL gene (chr3p25.3 in human) and the substrate-recognition subunit of an E3 ubiquitin-ligase complex (VBC: VHL / Elongin B / Elongin C / Cul2 / Rbx1) that targets prolyl-hydroxylated HIF-α subunits for proteasomal degradation under normoxia. Loss of VHL function — by germline mutation in Von Hippel-Lindau disease, by somatic mutation/deletion in clear cell renal cell carcinoma (ccRCC), or by epigenetic silencing — results in constitutive HIF-α stabilization (especially HIF-2α) and a "pseudohypoxia" transcriptional state. VHL has additional non-HIF substrates and structural roles, but the HIF-α axis is its dominant mechanism of tumor suppression.

## Intuition

VHL is the gatekeeper that disposes of HIF-α whenever oxygen is plentiful. Under normoxia, PHD enzymes hydroxylate HIF-α at specific proline residues; pVHL recognizes the hydroxylated proline as a degron, recruits the rest of the VBC complex, polyubiquitinates HIF-α, and ships it to the proteasome. Under hypoxia, PHDs cannot hydroxylate HIF-α, so VHL cannot recognize it, and HIF-α accumulates. Loss-of-function mutations in VHL break this disposal at the protein-recognition step, locking HIF-α in a stabilized state regardless of O₂ — the chronic-pseudohypoxia hallmark of VHL disease and ccRCC.

## Formal notation

- Gene: VHL, chr3p25.3, human protein 213 aa (long isoform pVHL30) or 160 aa (short isoform pVHL19).
- Protein structure: α-domain binds Elongin B/C; β-domain binds hydroxyproline-containing HIF-α.
- VBC complex: pVHL + Elongin B (EloB) + Elongin C (EloC) + Cullin 2 (Cul2) + RING-finger Rbx1.
- Substrate: HIF-1α / HIF-2α / HIF-3α with hydroxyproline at Pro402 / Pro564 (HIF-1α) or Pro405 / Pro531 (HIF-2α) — recognized by pVHL β-domain.
- Mechanism: VBC complex polyubiquitinates K-residues on HIF-α → 26S proteasomal degradation.
- HIF-1α has stronger affinity for VHL than HIF-2α — different proline-hydroxylation sites contribute to differential recognition (Bai 2022 cites this distinction).

VHL disease:
- Autosomal-dominant inherited tumor syndrome.
- Germline VHL mutation/deletion + somatic second hit → multi-organ tumors.
- Tumor spectrum: ccRCC, CNS hemangioblastomas, retinal angiomas, pheochromocytomas, pancreatic neuroendocrine tumors (pNET), endolymphatic-sac tumors, epididymal cystadenomas.
- Therapy: HIF-2α inhibitor Belzutifan (FDA-approved 2021) for VHL-RCC, hemangioblastoma, pNET.

ccRCC connection:
- ~90% of sporadic ccRCC have VHL inactivation (mutation, deletion, or hypermethylation).
- pVHL loss → HIF-2α dominance → ccRCC.

Pacak-Zhuang syndrome:
- Activating somatic-mosaic EPAS1 mutation bypasses VHL (HIF-2α gain-of-function).
- Polycythemia + multiple paragangliomas.
- Belzutifan candidate per Bai 2022.

## Key variants

- *VHL Type 1*: deletions / null mutations; high RCC and hemangioblastoma risk, low pheochromocytoma risk.
- *VHL Type 2A*: missense mutations; lower RCC risk, higher pheochromocytoma risk.
- *VHL Type 2B*: missense; both RCC and pheochromocytoma.
- *VHL Type 2C*: missense; only pheochromocytoma.
- *Chuvash polycythemia* (VHL R200W homozygous): mild VHL hypomorph → HIF-2α-driven erythropoiesis.

## Known limitations

- VHL has non-HIF substrates (atypical PKC, fibronectin, RNA-pol II) whose contribution to tumor suppression is less clear.
- VHL-loss mouse models often have embryonic lethality; conditional alleles required.
- The therapeutic upside of HIF-2α inhibition (Belzutifan) does not fully reverse VHL-loss phenotypes — non-HIF VHL functions may be relevant.

## Open problems

- Comprehensive map of non-HIF VHL substrates and their contribution to tumor suppression vs cancer dependency.
- Why HIF-2α dominates ccRCC while HIF-1α dominates many other VHL-loss-related processes — substrate preference at the protein level vs transcriptional rewiring.
- Predictive value of VHL mutation type for Belzutifan response.

## Relevance to active research

VHL is foundational to cancer-relevant hypoxia biology. In [[papers/hypoxia-driven-crosstalk-between-tumor-tumor]] (Bai 2022), VHL's role in the canonical HIF-α degradation pathway is the textbook anchor for why HIF-2α-PAS-B small molecules (Belzutifan, PT2385) are clinically meaningful: they pharmacologically mimic the loss of HIF-2α activity that pVHL would normally enforce. The iASPP-VHL interaction (Zhao 2022 *Oncogene*) is also a hot area: oncogenic iASPP binds pVHL to prevent HIF-1α degradation without blocking PHD-mediated hydroxylation.
