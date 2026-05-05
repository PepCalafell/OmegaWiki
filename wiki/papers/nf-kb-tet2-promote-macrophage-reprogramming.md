---
title: "NF-κB and TET2 promote macrophage reprogramming in hypoxia that overrides the immunosuppressive effects of the tumor microenvironment"
slug: nf-kb-tet2-promote-macrophage-reprogramming
arxiv: ""
venue: "Science Advances"
year: 2024
tags: [macrophages, hypoxia, tumor-microenvironment, dna-methylation, nf-kb, hif1a, tet2, immunology, epigenetics]
importance: 4
date_added: 2026-05-05
source_type: pdf
s2_id: ""
keywords: [macrophages, hypoxia, NF-κB, TET2, HIF1α, DNA methylation, tumor microenvironment, immunogenicity]
domain: "immunology / epigenetics"
code_url: "https://github.com/gustaveroussy/FG-Lab"
cited_by: []
---

DOI: 10.1126/sciadv.adq5226 — published 18 September 2024 in *Science Advances* 10, eadq5226. Data: GEO GSE261324; scRNA-seq via gustaveroussy/FG-Lab.

## Problem

Macrophages (MACs) in the tumor microenvironment (TME) are largely associated with poor prognosis because cues in the TME reprogram them into immunosuppressive cells. Hypoxia is a hallmark feature of the TME and is widely framed as an immunosuppressive driver, yet evidence on its direct effect on macrophage function is contradictory: HIF1α has been described as both pro- and anti-inflammatory depending on cellular and physiological context. The specific contribution of oxygen restriction — disentangled from other TME signals — to macrophage immunogenicity remained uncertain. Critically, hypoxia inhibits TET dioxygenase activity (which requires O₂), so the field expected hypoxia to globally repress TET-mediated demethylation of inflammatory loci. The paper asks whether, despite this, hypoxia could *enhance* macrophage immunogenicity, and through which transcriptional and epigenetic mechanisms.

## Key idea

Using a controlled in vitro system (human peripheral monocytes differentiated to MACs under 21% O₂ vs 1% O₂, ± LPS), the authors show that hypoxia paradoxically **boosts** the proinflammatory program of activated macrophages. The boost is driven by a specific cluster of CpGs — **cluster C2** — that undergoes hypoxia-specific DNA demethylation despite reduced global TET activity. C2 is exclusively associated with NF-κB binding (p65), not HIF1α binding, and hosts inflammatory loci including *IL6* and *TNF*. Hypoxic mMAC₁ macrophages (the term coined for "mature MACs activated under 1% O₂") thus carry a distinctive demethylation+overexpression signature for proinflammatory cytokines. This signature is found in vivo in mMAC₁-like subpopulations infiltrating bladder and ovarian carcinomas and correlates with better patient survival — challenging the "hypoxia is immunosuppressive" paradigm for macrophage biology and identifying actionable targets in p65 / TET2.

## Method

**In vitro model**: Human MO-derived MACs differentiated 5 days with M-CSF in 21% (normoxia) or 1% O₂ (hypoxia), then ± LPS for 48 h. Four conditions: iMAC₂₁, mMAC₂₁, iMAC₁, mMAC₁.

**Multi-omics characterization**:
- Cytokines (LEGENDplex), surface markers (flow cytometry: HLA-DR, CD80, CD86, CD14, CD206, CD163), and CD8⁺ T cell proliferation cocultures (CFSE).
- DNA methylation (Illumina Infinium MethylationEPIC) → DMP analysis with FDR < 0.05, |Δβ| > 0.2; clustered into C1 (hypomethylated MACs vs MOs), C2 (hypoxia-specific demethylation in mMAC₁), C3 (hypermethylated MACs).
- Bulk RNA-seq → 4 expression clusters E1–E4; DoRothEA TF-regulon activity inference; reanalysis of public LPS time-course data (37) to assign "early" vs "late" inflammatory genes.
- Validation across PAMPs/cytokines (P3C, CpG, polyI:C, TNF-α, IL-1β) and "swap" experiments (transferring cells between O₂ conditions at the activation step).
- Western blot + immunofluorescence quantifying HIF1α and p65 cytoplasm vs nucleus dynamics.
- ChIP-seq for HIF1α and p65 across all four conditions → unsupervised clustering yielded H1–H3 (HIF1α) and P1 (p65) peak sets; HOMER motif enrichment.
- Pharmacological dissection: BAY11-7082 (p65i), PX-478 (HIF1αi), 4-octyl itaconate (TET inhibitor as positive control for blocking demethylation), then re-measuring methylation + RT-qPCR of representative C2 genes.

**In vivo validation**:
- MoMac-VERSE single-cell atlas (10): testing whether mMAC₁-defined gene-expression and C2 demethylation signatures map onto pre-defined human MO/MAC subpopulations across 13 tissues.
- TCGA pan-cancer survival analysis using mMAC₁/iMAC₁/mMAC₂₁/iMAC₂₁ signatures and BLCA C2 methylation; CIBERSORTx + scRNA-seq cell-type estimation in BLCA, separating "cold" (n=226) and "hot" (n=161) tumors; CellChat for ligand-receptor mapping between mMAC₁ and T cells.
- Primary ovarian carcinoma (n=5) sorting via FACS into IL4I1, TREM2, FOLR2 MAC populations, followed by EPIC methylation arrays + bulk RNA-seq to confirm the mMAC₁ signature in vivo.

## Results

- **Functional**: mMAC₁ secrete more IL-6/TNF-α and less IL-10 than mMAC₂₁; up-regulate HLA-DR/CD80/CD86 and down-regulate CD14/CD206/CD163; suppress CD8⁺ T-cell proliferation *less* than normoxic counterparts (Fig. 1B–D).
- **Epigenetic**: 2782 (C1) + 403 (C2) + 903 (C3) DMPs. Cluster C2 = NF-κB-motif-enriched, hypoxia-specific demethylation in mMAC₁ at LPS-dependent de novo enhancers (H3K4me1+H3K27ac after LPS); includes *IL6*, *TNF* loci (Fig. 1E–F, fig. S1C).
- **Transcriptional**: 4 DEG clusters; cluster E2 (LPS-up) is over-enriched for C2-associated genes (P = 3.03·10⁻⁴⁴; Fig. 2D–E). DoRothEA: HIF1A is the most enriched regulon along the hypoxia axis, but in the LPS-activated comparison HIF1A is overcome by STAT2/IRF1 and RELA — RELA up-regulation is *attributable almost exclusively* to a hypoxic boost in normoxia-up genes (fig. S3C).
- **Mechanism**: HIF1α is induced cytoplasmically and nuclearly under hypoxia; p65 nuclear translocation after LPS is *enhanced* in hypoxia (Fig. 3B–C). ChIP-seq: H1–H3 + P1 peak sets; cobound HIF1α∩p65 peaks centered on HIF1α-specific motifs but show no linear correlation in binding intensity (r=0.13), arguing for cooperation without obligate physical interaction. C2 CpGs co-localize *exclusively* with p65-specific peaks, not HIF1α peaks (Fig. 4I–J).
- **Pharmacological dissection (Fig. 4K–L)**: BAY11-7082 (p65i) alone — but not PX-478 (HIF1αi) alone — restores DNA methylation at C2 to mMAC₂₁-like levels and drops mRNA of *IL6/IRF1/NFKB1/CCL5*. 4-octyl itaconate (TET inhibitor) confirms demethylation is required for full mRNA boost. **Conclusion: NF-κB (p65) — not HIF1α — drives C2 demethylation and the inflammatory boost.**
- **In vivo translation**: mMAC₁ signatures localize to MoMac-VERSE clusters #15 (IL1B Mo), #6 (IL4I1 Mac), and #4 (ISG Mo); high mMAC₁ / IL4I1 abundance correlates with better OS in 7/12 cancer types in TCGA (notably BLCA and OC); high C2 methylation correlates with worse OS in BLCA. mMAC₁ abundance correlates with T-cell infiltration in BLCA (r=0.74, P=2.2·10⁻⁶⁷) and predicts ligand-receptor signaling for T cell chemotaxis (CXCL9-CXCR3, CXCL10-CXCR2), trafficking (ICAM1-SPN), TCR activation (HLA-A/B/E/F-CD8) and costimulation (MIF-CD74+CD44/CXCR4). Sorted IL4I1 ovarian-tumor MACs reproduce the mMAC₁ methylation+TF program ex vivo.

## Limitations

- One inflammatory stimulus at a time. Other TME cues (IL-10, TGF-β) might invert the phenotype — explicitly acknowledged.
- In vitro MO→MAC differentiation may not capture full tissue-resident MAC ontogeny.
- Survival association is correlational, not causal; bulk-deconvoluted signatures inherit CIBERSORTx assumptions.
- HIF1α inhibition was pharmacological only (PX-478) — no genetic loss of function to disentangle HIF1α-independent hypoxia effects.
- Demethylation-vs-transcription causal direction at C2 still needs paired time-resolved methylome+transcriptome to nail the sequence of events.
- Sample sizes in primary ovarian sorted populations are small (n=5).

## Open questions

- Which non-canonical / HIF1α-independent oxygen-sensing pathway licenses p65 to overactivate in 1% O₂?
- Mechanism by which p65 binding triggers TET2 recruitment and local demethylation under O₂ limitation that should otherwise inhibit TET catalysis.
- Whether mMAC₁-like populations are reachable in vivo by clinically available NF-κB or HIF1α modulators without compromising other immune compartments.
- Do additional in vivo cues (TGF-β, IL-10, lactate, adenosine) reverse the mMAC₁ pro-immunogenic state?
- How robust is the prognostic signal across cancer types — and what explains the 5/12 cancer types where higher mMAC₁ does *not* correlate with better OS?
- Time-course: does demethylation precede or follow transcription at C2 loci?

## My take

This paper inverts the default narrative ("hypoxia → immunosuppressive MAC") and demonstrates a clean separation of TF labour (HIF1α-driven hypoxia adaptation vs NF-κB-driven proinflammatory demethylation) at single-loci resolution. The pharmacological dissection (Fig. 4K–L) is the load-bearing experiment: it shows that **p65 — not HIF1α — is the demethylation driver**, despite the field's heavy focus on HIF as the hypoxia TF. Strongest contributions: (i) the C2 cluster as a portable epigenetic signature linking in vitro mechanism to in vivo prognostic populations, (ii) the explicit non-correlation of HIF1α/p65 binding intensities at cobound regions (arguing co-regulation without complex formation), and (iii) the convergent in-vivo validation across MoMac-VERSE, TCGA, and primary ovarian sorts. The honest limitation about single-stimulus design is well-acknowledged. The actionable claim — that hypoxia plus NF-κB activation can be a *positive* therapeutic lever in TAM-rich tumors — is provocative and testable. Worth holding side-by-side with [[itaconate-tet2-inflammation-dampening]] and Mulder et al.'s MoMac-VERSE for any future TAM-targeting work.

## Related

- [[mmac1-hypoxic-inflammatory-macrophage]] — the new mMAC₁ phenotype defined here
- [[nfkb-hif1a-cooperative-binding]] — co-regulation pattern with HIF1α primary on hypoxia adaptation, p65 primary on inflammatory demethylation
- [[hypoxia-boosts-mac-immunogenicity-via-nfkb-tet]] — central claim, p65-dependent
- [[mmac1-signature-correlates-with-better-survival]] — clinical translation claim
- [[hif1a]] — HIF1α as canonical hypoxia TF (foundation)
- [[tet-mediated-dna-demethylation]] — TET dioxygenase mechanism (foundation)
- [[josep-calafell-segura]] — co-first author
- [[esteban-ballestar]] — senior / corresponding author
