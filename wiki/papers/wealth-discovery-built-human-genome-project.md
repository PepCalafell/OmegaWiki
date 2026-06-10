---
# === Identification ===
title: "A wealth of discovery built on the Human Genome Project — by the numbers"
slug: wealth-discovery-built-human-genome-project
arxiv: ""
doi: "10.1038/d41586-021-00314-6"
pmid: "33568828"
venue: "Nature"
year: 2021
authors: ["Alexander J. Gates", "Deisy Morselli Gysi", "Manolis Kellis", "Albert-László Barabási"]
first_author: "Alexander J. Gates"
corresponding_author: "Albert-László Barabási"

# === Source & metadata ===
source_type: pdf
s2_id: "58c2fde0686bbbcf11025123f304d05c0d350f93"
date_added: 2026-06-10
ingested_date: 2026-06-10
ingest_version: 1
last_reviewed:

# === Classification ===
importance: 4
tier: TIER_1
tags: [network-science, network-medicine, bibliometrics, genomics, science-of-science, drug-discovery, HGP]
keywords: [Human Genome Project, preferential attachment, superstar genes, non-coding genome, druggable genome, GWAS, interactome]
domain: genomics

# === Biomedical domain ===
tissue: [multi]
condition: [healthy, cancer]
disease_specific: []
species: [human]
hypoxia_relevant: false
contains_immune_cells: false
contains_myeloid: false

# === Technique ===
techniques: [bibliometric_analysis, network_analysis]
n_samples:
n_cells_total:
integration_method: ""

# === Biology captured ===
key_cell_types: []
key_markers: [TP53, TNF, EGFR, IL6, VEGFA, APOE, TGFB1, MTHFR, CD4, HBA1, ADRA1A, SCT]
key_pathways: [gene-regulatory-networks, drug-target-interactome]

# === User project membership ===
projects: [methods]
priority: reference
read_status: not_read

# === HypoxiaVERSE-specific ===
hypoxiaverse_status:
exclusion_reason:
data_availability: "Supplementary information at go.nature.com/39qgndf"

# === Cross-references ===
code_url: ""
cited_by: []
---

## Problem

Twenty years after the 2001 draft human genome, what did the Human Genome Project (HGP) actually change about how biology is done? The authors quantify the HGP's impact on gene discovery, research attention, drug discovery, and the shift from a single-gene to a network/systems view of biology — using bibliometric and network analysis rather than new wet-lab data.

## Key idea

The HGP's enduring value is not the ~20,000-protein parts catalogue itself but the *network era* of genomics it enabled. A comprehensive components list is necessary but not sufficient to understand a complex system; biology's complexity arises from interactions between components. Along the way, research attention on genes follows a "rich-gets-richer" (preferential attachment) dynamic, producing a small set of intensely studied "superstar" genes and leaving most of the genome — and the proteome as drug-target space — under-explored.

## Method

A bibliometric/network analysis linking several data sets: 38,546 RNA transcripts; ~1 million SNPs; 1,660 human diseases with documented genetic roots; 7,712 approved and experimental pharmaceuticals; and 704,515 scientific publications (1900–2017). The team mapped genes to publications, diseases, and drug targets, and tracked temporal trends, controlling for overall growth in biology publications. Methods derive from the authors' network-science toolkit — see [[preferential-attachment]] and [[network-medicine]].

## Results

- Protein-coding gene discovery plateaued at ~20,000 in the mid-2000s, far below the long-assumed 100,000.
- Attention is extremely skewed: 22% of gene-related publications referenced just 1% of genes; ~3% of genes had no publications. Superstar genes: TP53, TNF, EGFR, IL6, VEGFA, …
- Discovery of non-coding elements outpaced protein-coding gene discovery ~5×; >30,000 SNP–trait papers/year, many associations in non-coding regions; >300,000 regulatory interactions charted.
- Drug targets: ~10% (2,149) of proteins targeted by approved drugs (3,119 incl. experimental); 90% of the proteome untargeted; ADRA1A targeted by 99 drugs (5% of approved) despite ~130 publications.
- Most successful drugs act on network neighbours of disease genes; COVID-19 repurposing screens found ~99% of candidates modulate human (not viral) proteins.

## All claims (exhaustive)

- `[c01]` Protein-coding gene count plateaued ~20,000, far below the earlier 100,000 estimate (p.1) "It levelled out suddenly in the mid-2000s at about 20,000 protein-coding genes … far short of the 100,000-strong estimate" — confidence: high — type: quantitative — links: [[foundations/human-genome-project]] [[claims/protein-coding-gene-count-plateaued-20000]]
- `[c02]` By 2017, 22% of gene-related publications referenced just 1% of genes (p.1) "by 2017, 22% of gene-related publications referenced just 1% of genes" — confidence: high — type: quantitative — links: [[concepts/superstar-gene-attention-skew]] [[claims/gene-research-attention-concentrated-superstars]]
- `[c03]` Yearly new publications on a gene are linearly proportional to its existing literature — preferential attachment (p.3) "the number of new yearly publications focusing on a given gene is linearly proportional to the size of previous literature on it" — confidence: medium — type: mechanistic — links: [[foundations/preferential-attachment]] [[concepts/superstar-gene-attention-skew]] [[claims/gene-study-follows-preferential-attachment]]
- `[c04]` Non-coding element discovery has outstripped protein-coding gene discovery ~5× (p.3) "that growth has outstripped the discovery of protein-coding genes by a factor of five" — confidence: high — type: quantitative — links: [[foundations/long-non-coding-rna]] [[foundations/human-genome-project]] [[claims/noncoding-element-discovery-outpaces-coding-5x]]
- `[c05]` The majority of functional sequences in the human genome do not encode proteins (p.3) "the majority of functional sequences in the human genome do not encode proteins" — confidence: high — type: mechanistic — links: [[foundations/long-non-coding-rna]] [[claims/majority-functional-sequences-noncoding]]
- `[c06]` Only ~10% of proteins (2,149) targeted by approved drugs; ~90% of proteome untargeted (p.3) "only about 10% — 2,149 — have so far been targeted by approved drugs … That leaves 90% of the proteome untouched" — confidence: high — type: quantitative — links: [[concepts/druggable-genome]] [[claims/only-10-percent-proteome-drug-targeted]]
- `[c07]` Since 2001 nearly 100% of US-licensed drugs/year have all protein targets identified (vs <50% before) (p.3) "Until 2001, the probability of knowing all of a drug's protein targets was less than 50% … Now, the targets are known for almost all drugs licensed in the United States each year" — confidence: medium — type: correlational — links: [[concepts/druggable-genome]] [[foundations/human-genome-project]] [[claims/hgp-enabled-near-complete-drug-target-identification]]
- `[c08]` Most successful drugs target proteins 1–2 interactions from the disease gene (p.3) "they target proteins one or two interactions away, modulating the consequences of faulty components" — confidence: medium — type: mechanistic — links: [[concepts/network-medicine]] [[claims/successful-drugs-target-network-neighbors]]
- `[c09]` In COVID-19 repurposing screens only ~1% of candidates targeted a viral protein (p.3-4) "only 1% of promising candidates targeted a viral protein — the majority were drugs that modulated human proteins" — confidence: medium — type: correlational — links: [[concepts/network-medicine]] [[claims/covid-repurposing-candidates-target-human-proteins]]
- `[c10]` TP53 is the most-studied gene (9,232 publications) and altered in >50% of tumour sequences (p.1-3) "it is mentioned in 9,232 publications between 1976 and 2017"; "found in more than 50% of tumour sequences" — confidence: high — type: quantitative — links: [[foundations/tp53-tumor-suppressor]] [[concepts/superstar-gene-attention-skew]] [[claims/tp53-most-studied-superstar-gene]]
- `[c11]` TNF is associated with 160 known diseases, the most of any gene (p.2) "TNF is associated with 160 known diseases, the most of any gene" — confidence: high — type: quantitative — links: [[foundations/tnf-tumor-necrosis-factor]] [[claims/tnf-associated-most-diseases]]
- `[c12]` ADRA1A targeted by 99 approved drugs (5% of all) despite only ~130 publications (p.2-3) "Five per cent of all approved drugs … (99 distinct molecules) target the protein ADRA1A"; "It is the subject of just 130 publications" — confidence: high — type: quantitative — links: [[foundations/adra1a-adrenergic-receptor]] [[concepts/druggable-genome]] [[claims/drug-target-attention-skewed-adra1a]]
- `[c13]` >30,000 SNP–trait papers/year, large fraction of associations in non-coding regions (p.3) "more than 30,000 papers per year linking SNPs and traits. A large fraction of these associations are in the once-dismissed non-coding regions" — confidence: high — type: correlational — links: [[foundations/gwas-genome-wide-association-study]] [[foundations/hapmap-project]] [[foundations/1000-genomes-project]] [[claims/gwas-associations-concentrated-noncoding]]
- `[c14]` More than 300,000 regulatory network interactions have been charted (p.3) "more than 300,000 regulatory network interactions have been charted — proteins binding with non-coding regions or with other proteins" — confidence: medium — type: quantitative — links: [[concepts/network-medicine]] [[claims/regulatory-network-interactions-charted-300k]]
- `[c15]` The HGP's lasting value is the network era it enabled, not the protein catalogue itself (p.4) "the HGP is more notable for the new era of genomics it ushered in, than for the protein catalogue itself" — confidence: medium — type: mechanistic — links: [[concepts/network-medicine]] [[foundations/human-genome-project]] [[claims/hgp-value-is-network-era-not-catalogue]]
- `[c16]` Biology team sizes grew steadily since the 1950s; the HGP did not mark a step change (p.3) "team sizes in biology have grown consistently since the 1950s" — confidence: medium — type: correlational — links: [[foundations/human-genome-project]] [[claims/biology-team-size-growth-not-hgp-step-change]]

## Discussion captured

### Authors' interpretation

The authors interpret the gene-attention skew through their own network-science lens: the imbalance reflects a "rich-gets-richer" dynamic (preferential attachment) rooted in social factors — heavily studied genes are safer bets for funding, mentorship, tools, and citations. They frame drug discovery similarly, arguing that the network neighbourhood of disease genes, not the genes themselves, is where most therapeutics act ("network drugs").

### Comparisons with prior literature (made by authors)

- Cite the two 2001 draft-genome papers: Venter et al., Science 291, 1304–1351 (2001) and IHGSC, Nature 409, 860–921 (2001).
- Preferential attachment / scale-free networks: Barabási & Albert, Science 286, 509–512 (1999); fitness variant Bianconi & Barabási, Europhys. Lett. 54, 436 (2001).
- Attention-skew problem previously flagged: Edwards et al., Nature 470, 163–165 (2011).
- Network drugs / disease-gene targeting: Yildirim et al., Nature Biotechnol. 25, 1119–1126 (2007).
- COVID-19 network repurposing: Gysi et al., arXiv:2004.07229 (2020).
- Enabling variation catalogues: HapMap (Nature 426, 789–796, 2003); 1000 Genomes (Nature 526, 68–74, 2015).
- Drug-target database: Wishart et al., Nucleic Acids Res. 46, D1074–D1082 (2018).

### Mechanistic hypotheses proposed

- "this vast imbalance can be explained by a 'rich-gets-richer' dynamic rooted in social factors" (preferential attachment) (p.3).
- Network-drug hypothesis: therapeutics modulate the consequences of faulty components via network neighbours rather than the disease gene directly (p.3).

### Caveats and self-criticism

- No consensus on where a gene starts/ends or what exactly encodes some genes; multiple naming conventions break some publication–element links (p.1).
- Graphs end in 2017 due to database time lag; did not control for time since gene discovery (but estimate it would not change conclusions) (p.1).
- "There is no world without an HGP for comparison," so causal attribution of the trends to the HGP is impossible; other factors (computing power, sequencing methods) also contributed (p.1).

### Future directions suggested

- Disentangle whether research effort goes to what is most important/urgent versus "more of the same" that reliably wins grants.
- Explore the untargeted 90% of the proteome as potential drug targets if the field were less risk-averse.

## Limitations

- Bibliometric/database-derived; subject to naming and annotation inconsistencies.
- Counterfactual (no-HGP world) is untestable, so trends cannot be causally attributed to the HGP alone.
- Analysis window ends in 2017.

## Open questions

### Open questions raised by authors

- What drives the choice of "what gets studied next" — importance/urgency or grant-safe repetition?
- Could the untargeted majority of the proteome yield many viable drug targets?

### Open questions identified during ingest

- How much of the gene-attention skew is genuine biological importance versus self-reinforcing momentum, and can it be measured?
- How far from complete is the human interactome relative to the >300,000 charted interactions?

## My take

A high-level, widely-read Nature commentary (Barabási + Kellis) that reframes the HGP as the launchpad of network/systems genomics. Tangential to the hypoxia/skin/immune thesis work directly, but useful as a conceptual anchor: it cautions that literature-derived priors (curated pathways, marker lists) inherit the superstar-gene attention skew, and it supplies the [[network-medicine]] and [[preferential-attachment]] vocabulary. Importance 4 for influence/venue, not for methodological depth — it is interpretive bibliometrics, not original wet-lab science.

## Related

- [[concepts/network-medicine]] — central framing of drug action on the interactome.
- [[concepts/superstar-gene-attention-skew]] — the core bibliometric finding.
- [[concepts/druggable-genome]] — proteome drug-target coverage.
- [[foundations/preferential-attachment]], [[foundations/human-genome-project]], [[foundations/long-non-coding-rna]], [[foundations/gwas-genome-wide-association-study]], [[foundations/hapmap-project]], [[foundations/1000-genomes-project]], [[foundations/adra1a-adrenergic-receptor]], [[foundations/tp53-tumor-suppressor]], [[foundations/tnf-tumor-necrosis-factor]]
