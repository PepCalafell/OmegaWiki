---
# === Identification ===
title: "Effector–host interactome map links type III secretion systems in healthy gut microbiomes to immune modulation"
slug: effector-host-interactome-map-links-type
arxiv: ""
doi: "10.1038/s41564-025-02241-y"
pmid: "41588163"
venue: "Nature Microbiology"
year: 2026
authors: ["Veronika Young", "B. Dohai", "Hridi Halder", "Jaime Fernandez-Macgregor", "Niels S. van Heusden", "Thomas C. A. Hitch", "Benjamin Weller", "Patrick Hyden", "Deeya Saha", "D. Pieren", "Sonja Rittchen", "L. Lambourne", "Sibusiso B. Maseko", "Chung-Wen Lin", "Ye Min Tun", "Jonas Bibus", "Luisa Pletschacher", "Mégane Boujeant", "Sebastien A. Choteau", "Lou Bergogne", "J. Perrin", "Franziska Ober", "Patrick Schwehn", "Simin T. Rothballer", "Melina Altmann", "Stefan Altmann", "A. Strobel", "Michael Rothballer", "Marie J. Tofaute", "Daniel Kotlarz", "Matthias Heinig", "Thomas Clavel", "Michael A. Calderwood", "Marc Vidal", "Jean-Claude Twizere", "Renaud Vincentelli", "Daniel Krappmann", "M. Boes", "C. Falter", "T. Rattei", "Christine Brun", "Andreas Zanzoni", "Pascal Falter-Braun"]
first_author: "Veronika Young"
corresponding_author: "Andreas Zanzoni; Pascal Falter-Braun"

# === Source & metadata ===
source_type: pdf
s2_id: "39d768bfe83ed5e2707d2f1ec9d36a2f0a562356"
date_added: 2026-05-28
ingested_date: 2026-05-28
ingest_version: 1
last_reviewed:

# === Classification ===
importance: 4
tier: TIER_1
tags: [t3ss, microbiome, interactome, immune-modulation, gut, ibd, nf-kb, effectors]
keywords: [type III secretion system, commensal effectors, meta-interactome, HuMMI, Crohn's disease, ulcerative colitis, NF-κB, PDZ domain, Pseudomonadota]
domain: microbiology

# === Biomedical domain ===
tissue: [colon, skin, in_vitro_only]
condition: [healthy, autoimmune]
disease_specific: [crohns_disease, ulcerative_colitis]
species: [human]
hypoxia_relevant: false
contains_immune_cells: false
contains_myeloid: false

# === Technique ===
techniques: [yeast_two_hybrid, co-IP, metagenomics, comparative_genomics, AlphaFold-Multimer, FoldSeek, holdup_assay, NanoLuc_HiBiT_injection, dual_luciferase_reporter]
n_samples:
n_cells_total:
integration_method: ""

# === Biology captured ===
key_cell_types: [intestinal_epithelial_cells, HeLa, HEK293, Caco-2]
key_markers: [NF-κB, TNF, NOD2, COG6, TNIP1, TCF4, REL, TRAF2, IL-6, IL-8]
key_pathways: [NF-κB_signalling, SAPK_JNK, muramyl_dipeptide_NOD2, TLR1_2_signalling, c-di-GMP_signalling]

# === User project membership ===
projects: [thesis]
priority: reference
read_status: read

# === HypoxiaVERSE-specific ===
hypoxiaverse_status:
exclusion_reason:
data_availability: "Supplementary Data 1-26; HuMEOme_v1 ORFeome; HuMMI interactome"

# === Cross-references ===
code_url: ""
cited_by: []
---

## Problem

The human gut microbiome influences health in genotype-dependent ways, but the molecular
mechanisms are incompletely understood. Most work has focused on metabolites, MAMPs and
community-level properties; direct intracellular bacteria–host *protein* interactions are
largely unexplored. Type III secretion systems (T3SS), the "needle-and-syringe"
machineries that inject effectors into host cells, have been studied almost exclusively
in pathogens and framed as virulence determinants. Whether commensal Pseudomonadota of
the healthy human gut deploy T3SS, and what host functions their effectors engage, was
unknown.

## Key idea

Treat commensal T3SS as a route of direct protein-mediated microorganism–host
communication. The authors (1) survey T3SS prevalence across thousands of gut genomes and
MAGs, (2) machine-learning-predict candidate effectors and show they are sequence/structurally
distinct from pathogen effectors, (3) experimentally build HuMMI — a verified
effector–human protein meta-interactome — and (4) link the targeted host network to
disease genetics and to functional immune modulation (NF-κB, cytokines), culminating in
an IBD metagenomic signal that diverges between Crohn's disease and ulcerative colitis.

## Method

- **Comparative genomics**: EffectiveDB T3SS detection across 77 HMP-derived reference
  genomes, 4,752 culture-collection strains (HiBC/BIO-ML/GMC) and 16,179 MAGs.
- **Effector prediction**: three ML models; comparison to 1,195 pathogen effectors via
  sequence (jackhmmer/UniRef90) and structure (AlphaFold + FoldSeek clustering).
- **Injection assays**: NanoLuc HiBiT split-luciferase translocation via heterologous
  Salmonella Typhimurium (ΔsctV control) and native strains (e.g. Edwardsiella tarda).
- **Interactome mapping**: cloned HuMEOme_v1 (910 ORFs) screened against human ORFeome
  9.1 by multi-assay Y2H; validation by yN2H and co-IP in HEK293.
- **Interface analysis**: AlphaFold-Multimer (globular interfaces), mimicINT
  (SLiM-domain), holdup assay (PDZ–PBM Kd).
- **Disease genetics**: GO/Recon3D enrichment, Open Targets/EFO GWAS mapping, HuRI
  random-walk neighbourhoods.
- **Functional**: dual-luciferase NF-κB reporter (HEK293), cytokine secretion (Caco-2),
  IBD metagenomics (504 CD, 302 UC, 334 healthy).

## Results

~79% of gut Pseudomonadota reference genomes (92% with any host-directed secretion
system) encode complete T3SS, restricted to Gammaproteobacteria. 3,002 candidate strain
effectors are largely novel vs pathogens in sequence and structure, carrying
commensal-specific c-di-GMP (GGDEF/EAL) and PAS domains. 32 candidate effectors were
specifically injected into HeLa; E. tarda's native T3SS injected 3/4 effectors. HuMMI
comprises 1,255 verified interactions (286 effectors × 426 human proteins), biophysically
on par with literature interactions. Effectors converge on ~60 host hub proteins
(including the NF-κB module). Interaction profiles are sequence-independent; SLiM-domain
(notably PDZ–PBM) interfaces are enriched and holdup-validated. Targeted proteins/
neighbourhoods are enriched for MDP/NOD2 response, NF-κB, and GWAS variation for immune
and metabolic disease — Crohn's disease specifically, not UC. Functionally, effectors
bidirectionally modulate NF-κB and stimulus-specifically modulate IL-6/IL-8. In IBD
metagenomes, 64 effectors are enriched in Crohn's disease but depleted in ulcerative
colitis, with network links to CD/UC susceptibility proteins (COG6, TNIP1).

## All claims (exhaustive)

- `[c01]` ~79% of gut-commensal Pseudomonadota reference genomes encode a complete T3SS (p.444) "449 (79%) have complete T3SS" — confidence: high — type: quantitative — links: [[claims/79-percent-gut-pseudomonadota-encode-complete-t3ss]] [[concepts/commensal-t3ss-host-directed-secretion]] [[foundations/type-iii-secretion-system]] [[foundations/effectivedb-t3ss-prediction]]
- `[c02]` 92% of gut Pseudomonadota genomes encode ≥1 host-directed secretion system (p.444) "527 of the 568 Pseudomonatoda genomes (92%) have at least one host-directed secretion system" — confidence: high — type: quantitative — links: [[claims/92-percent-gut-pseudomonadota-have-host-directed-secretion-system]] [[concepts/commensal-t3ss-host-directed-secretion]]
- `[c03]` Commensal T3SS are restricted to Gammaproteobacteria, especially Escherichia (p.444) "T3SS were only detected in Gammaproteobacteria... especially common among Escherichia" — confidence: high — type: correlational — links: [[claims/commensal-t3ss-restricted-to-gammaproteobacteria-escherichia]] [[concepts/commensal-t3ss-host-directed-secretion]]
- `[c04]` Commensal effectors rarely share sequence similarity with pathogen effectors (p.443) "Only 17 out of 3,002 (0.5%) strain effectors... showed high sequence similarity" — confidence: high — type: quantitative — links: [[claims/commensal-effectors-rarely-share-sequence-with-pathogen-effectors]] [[concepts/commensal-pathogen-effector-divergence]]
- `[c05]` Commensal and pathogen effector structures form mostly homogeneous clusters; mixed clusters depleted (p.443) "homogeneous clusters... were highly overrepresented, whereas mixed clusters... were depleted (P << 0.0001)" — confidence: high — type: methodological — links: [[claims/commensal-pathogen-effector-structures-cluster-homogeneously]] [[concepts/commensal-pathogen-effector-divergence]] [[foundations/foldseek]] [[foundations/alphafold-multimer]]
- `[c06]` GGDEF, EAL and PAS domains are enriched in commensal effectors but absent from pathogen effectors (p.443) "the diguanylate cyclase, GGDEF domain... and EAL domain... none of which was found in pathogen effectors" — confidence: medium — type: correlational — links: [[claims/ggdef-eal-pas-domains-enriched-commensal-effectors-absent-pathogens]] [[concepts/commensal-pathogen-effector-divergence]] [[foundations/cyclic-di-gmp]]
- `[c07]` 32 commensal candidate effectors are specifically T3SS-injected into human cells (p.443) "Among 97 tested candidate effectors from 11 strains, 32 were specifically and significantly injected" — confidence: high — type: methodological — links: [[claims/32-commensal-effectors-t3ss-injected-into-hela-via-salmonella]] [[concepts/commensal-t3ss-host-directed-secretion]] [[foundations/nanoluc-hibit-injection-assay]] [[foundations/salmonella-typhimurium]]
- `[c08]` Edwardsiella tarda uses its native T3SS to inject effectors into human cells (p.443) "Edwardsiella tarda reproducibly and significantly injected three out of four tested effectors into HeLa cells" — confidence: medium — type: methodological — links: [[claims/edwardsiella-tarda-native-t3ss-injects-effectors-into-hela]] [[foundations/edwardsiella-tarda]] [[concepts/commensal-t3ss-host-directed-secretion]]
- `[c09]` HuMMI maps 1,255 verified interactions between 286 effectors and 426 human proteins (p.446) "HuMMI contains 1,255 unique verified interactions between 286 effectors and 426 human proteins" — confidence: high — type: quantitative — links: [[claims/hummi-1255-interactions-286-effectors-426-human-proteins]] [[concepts/microbiome-host-meta-interactome-hummi]] [[foundations/yeast-two-hybrid-y2h]]
- `[c10]` HuMMI interactions are biophysically reliable and detectable in human cells (p.447) "the biophysical quality of HuMMI is on par with well-documented literature interactions" — confidence: medium — type: methodological — links: [[claims/hummi-biophysical-quality-on-par-with-literature-interactions]] [[concepts/microbiome-host-meta-interactome-hummi]]
- `[c11]` Effectors from multiple strains converge on ~60 host hub proteins more than expected by chance (p.446) "60 human proteins are subject to effector convergence" — confidence: high — type: quantitative — links: [[claims/effectors-converge-on-60-host-hub-proteins-more-than-random]] [[concepts/effector-convergence-host-hub-proteins]] [[foundations/nf-kb-p65-rela]]
- `[c12]` Commensal and pathogen effectors share a small but significant set of human targets (p.446) "12 human proteins targeted by both groups (P = 0.014... odds ratio = 2.26)" — confidence: medium — type: correlational — links: [[claims/commensal-pathogen-effectors-share-12-human-targets]] [[concepts/effector-convergence-host-hub-proteins]]
- `[c13]` Effector host-interaction profiles are largely independent of overall sequence similarity (p.447) "host effector function as measured by protein-interaction profiles is largely independent of overall sequence similarity" — confidence: high — type: mechanistic — links: [[claims/effector-interaction-profile-independent-of-sequence-similarity]] [[concepts/effector-interaction-sequence-independence]]
- `[c14]` SLiM–domain interfaces are enriched among commensal effector–host interactions (p.447) "51 passed at least one (P = 0.0137)... 22 passed two stringency criteria (P = 0.0005)" — confidence: medium — type: methodological — links: [[claims/slim-domain-interfaces-enriched-in-hummi]] [[concepts/slim-pdz-effector-host-interface]] [[foundations/mimicint-slim-domain-inference]] [[foundations/alphafold-multimer]]
- `[c15]` Bacterial C-terminal PBMs bind human PDZ domains, validated by holdup assay (p.447) "Of 23 Y2H pairs, 16 (70%) showed at least one PDZ–peptide interaction" — confidence: high — type: methodological — links: [[claims/pdz-pbm-effector-interfaces-validated-by-holdup-assay]] [[concepts/slim-pdz-effector-host-interface]] [[foundations/holdup-assay]] [[foundations/pdz-domain]]
- `[c16]` Effector-targeted human proteins are enriched for MDP response, NF-κB and SAPK/JNK signalling (p.448) "Among the most enriched functions was 'response to muramyl dipeptide'... Central immune signalling pathways are also enriched, namely, the NF-κB and the SAPK/JNK pathways" — confidence: medium — type: correlational — links: [[claims/effector-targets-enriched-muramyl-dipeptide-nfkb-sapk-jnk]] [[foundations/nod2]] [[foundations/muramyl-dipeptide]] [[foundations/nf-kb-p65-rela]]
- `[c17]` Effector-targeted human genes are enriched for GWAS variation in immune and metabolic diseases (p.448) "Effector targets are also associated with cancers and immune diseases, such as psoriasis, asthma, allergies and systemic lupus erythematosus" — confidence: medium — type: correlational — links: [[claims/effector-targets-enriched-gwas-immune-metabolic-disease-variation]] [[concepts/effector-prevalence-crohns-vs-uc-divergence]] [[foundations/huri-human-reference-interactome]]
- `[c18]` Effector-targeted network neighbourhoods are enriched for Crohn's disease but not ulcerative colitis (p.450) "inflammatory bowel disease (IBD) was enriched... particularly Crohn's disease (nominal P = 8.5 × 10−5)... but not ulcerative colitis" — confidence: medium — type: correlational — links: [[claims/effector-neighbourhoods-enriched-crohns-not-uc]] [[concepts/effector-prevalence-crohns-vs-uc-divergence]] [[foundations/inflammatory-bowel-disease]]
- `[c19]` Commensal effectors bidirectionally modulate NF-κB activity in human cells (p.450) "5 out of 26 commensal effectors significantly activated NF-κB activity... 3 effectors reduced NF-κB activity under strong TNF stimulation" — confidence: medium — type: pharmacological — links: [[claims/commensal-effectors-bidirectionally-modulate-nfkb-activity]] [[foundations/nf-kb-p65-rela]] [[foundations/tnf-tumor-necrosis-factor]]
- `[c20]` Commensal effectors modulate cytokine secretion in a stimulus-dependent manner (p.450) "Cpa_12... reduced secretion of several cytokines... Other effectors enhanced cytokine responses, particularly IL-6 and IL-8, only after Pam3CSK4 stimulation" — confidence: medium — type: pharmacological — links: [[claims/commensal-effectors-modulate-cytokine-secretion-tlr-dependent]] [[foundations/pam3csk4-tlr12-agonist]] [[foundations/il-6-cytokine]] [[foundations/cxcl8-il8]]
- `[c21]` T3SS effectors are enriched in Crohn's disease but depleted in ulcerative colitis metagenomes (p.450) "64 effectors were significantly more prevalent in individuals with Crohn's disease... whereas effectors were less common in individuals with ulcerative colitis" — confidence: medium — type: correlational — links: [[claims/t3ss-effectors-enriched-crohns-depleted-uc-metagenomes]] [[concepts/effector-prevalence-crohns-vs-uc-divergence]] [[foundations/inflammatory-bowel-disease]]
- `[c22]` Crohn's-prevalent effectors physically target Crohn's susceptibility proteins COG6 and TNIP1 (p.450) "effectors from K. pneumonia, E. coli and E. fergusonii... interact with the Crohn's disease susceptibility protein COG6... Efe_13... binds the Crohn's disease susceptibility protein TNIP1" — confidence: low — type: mechanistic — links: [[claims/cd-prevalent-effectors-target-cd-susceptibility-proteins-cog6-tnip1]] [[concepts/effector-prevalence-crohns-vs-uc-divergence]]
- `[c23]` 26% of HuMMI effectors are detectable in skin microbiome samples (p.450) "26% of HuMMI effectors are detectable in skin microbiome samples, suggesting that commensal effectors are shared across ecological niches" — confidence: medium — type: quantitative — links: [[claims/26-percent-hummi-effectors-detectable-in-skin-microbiome]]

## Discussion captured

### Authors' interpretation

The authors interpret high T3SS prevalence and the distinctness of commensal effectors as
evidence that commensal T3SS are adapted for cooperative rather than pathogenic
interactions ("a model in which commensal T3SS are adapted for cooperative rather than
pathogenic interactions"). They argue species-level labels ("commensal"/"pathogenic")
obscure within-species diversity and that convergence proteins are key host–microorganism
nodes. They position host-directed secretion as an under-appreciated mode of
microbiota–host communication.

### Comparisons with prior literature (made by authors)

- Plant/insect symbiosis systems where T3SS mediate beneficial interactions (refs 10–14).
- Plant effector–host interactome convergence on central host nodes (ref 13, 40).
- Human reference interactome HuRI (ref 36) and assay reference sets (refs 35,37,38).
- H. pylori CagA as a paradigm of host-modified effectors (ref 60).
- Differential clinical anti-TNF response in CD vs UC.

### Mechanistic hypotheses proposed

- Commensal effectors may modulate host responses to Gram-positive Bacteroidetes
  (via TLR1/2 potentiation), influencing interphyla competition.
- A "homeostatic shift" model: effectors increase Crohn's disease risk while decreasing
  ulcerative colitis risk.
- c-di-GMP signalling (GGDEF/EAL/PAS domains) may participate in interkingdom
  communication.

### Caveats and self-criticism

- Some false effector identifications cannot be excluded; heterologous-host assays may
  lack cofactors (false negatives).
- Pathogen interaction data are non-systematic (IntAct) and limited in size.
- mimicINT found essentially no effector-enzymatic-domain engagement of host substrate
  motifs (only one LxVP/Efe_1–VAC14 example) — possibly a real difference, functional
  mimicry without sequence similarity, or a method limitation.

### Future directions suggested

- Determine whether host cells signal to induce commensal T3SS (as plant hosts do).
- Mechanistic studies of whether effectors causally affect CD risk / UC protection.
- Explore convergence proteins in commensal vs pathogenic contexts as entry points to
  understanding emergence of pathogenicity.

## Limitations

- T3SS detection tools may miss divergent systems (prevalence underestimate).
- Y2H assay sensitivity (~13–17.5%) and ~32% sampling sensitivity; network is incomplete.
- AlphaFold-Multimer confident for only ~10% of pairs.
- Disease associations are statistical (GWAS/Open Targets), not causal.
- IBD metagenomic signal is observational.

## Open questions

### Open questions raised by authors

- What host/environmental cues activate commensal T3SS in vivo?
- Do commensal effectors causally contribute to Crohn's disease or protect against UC?
- Are convergence proteins differentially manipulated in commensal vs pathogenic contexts?

### Open questions identified during ingest

- How much of the skin-microbiome effector detection reflects active injection in skin?
- Could effector content (not taxon abundance) become an IBD biomarker or therapy
  stratifier?

## My take

A landmark systems-microbiology paper that reframes T3SS as a normal feature of gut
commensals and delivers the first commensal effector–human interactome (HuMMI). The
genomic and interactome scaffolding is strong; the disease links (Crohn's vs UC) are
suggestive and honestly framed as hypotheses. The skin-microbiome detection (26%) is a
small but interesting hook connecting to broader barrier-tissue immunology. Of most
reuse value here: HuMMI as a resource, the convergence-on-NF-κB finding, and the
sequence-independence-of-interaction-profiles caution.

## Related

### Concepts
- [[commensal-t3ss-host-directed-secretion]]
- [[commensal-pathogen-effector-divergence]]
- [[microbiome-host-meta-interactome-hummi]]
- [[effector-convergence-host-hub-proteins]]
- [[effector-interaction-sequence-independence]]
- [[slim-pdz-effector-host-interface]]
- [[effector-prevalence-crohns-vs-uc-divergence]]

### Claims
- [[claims/79-percent-gut-pseudomonadota-encode-complete-t3ss]]
- [[claims/92-percent-gut-pseudomonadota-have-host-directed-secretion-system]]
- [[claims/commensal-t3ss-restricted-to-gammaproteobacteria-escherichia]]
- [[claims/commensal-effectors-rarely-share-sequence-with-pathogen-effectors]]
- [[claims/commensal-pathogen-effector-structures-cluster-homogeneously]]
- [[claims/ggdef-eal-pas-domains-enriched-commensal-effectors-absent-pathogens]]
- [[claims/32-commensal-effectors-t3ss-injected-into-hela-via-salmonella]]
- [[claims/edwardsiella-tarda-native-t3ss-injects-effectors-into-hela]]
- [[claims/hummi-1255-interactions-286-effectors-426-human-proteins]]
- [[claims/hummi-biophysical-quality-on-par-with-literature-interactions]]
- [[claims/effectors-converge-on-60-host-hub-proteins-more-than-random]]
- [[claims/commensal-pathogen-effectors-share-12-human-targets]]
- [[claims/effector-interaction-profile-independent-of-sequence-similarity]]
- [[claims/slim-domain-interfaces-enriched-in-hummi]]
- [[claims/pdz-pbm-effector-interfaces-validated-by-holdup-assay]]
- [[claims/effector-targets-enriched-muramyl-dipeptide-nfkb-sapk-jnk]]
- [[claims/effector-targets-enriched-gwas-immune-metabolic-disease-variation]]
- [[claims/effector-neighbourhoods-enriched-crohns-not-uc]]
- [[claims/commensal-effectors-bidirectionally-modulate-nfkb-activity]]
- [[claims/commensal-effectors-modulate-cytokine-secretion-tlr-dependent]]
- [[claims/t3ss-effectors-enriched-crohns-depleted-uc-metagenomes]]
- [[claims/cd-prevalent-effectors-target-cd-susceptibility-proteins-cog6-tnip1]]
- [[claims/26-percent-hummi-effectors-detectable-in-skin-microbiome]]

### People
- [[veronika-young]] · [[andreas-zanzoni]] · [[pascal-falter-braun]] · [[michael-rothballer]] · [[michael-calderwood]] · [[jean-claude-twizere]] · [[renaud-vincentelli]]

### Foundations
- [[type-iii-secretion-system]] · [[effectivedb-t3ss-prediction]] · [[foldseek]] · [[alphafold-multimer]] · [[yeast-two-hybrid-y2h]] · [[mimicint-slim-domain-inference]] · [[holdup-assay]] · [[huri-human-reference-interactome]] · [[nanoluc-hibit-injection-assay]] · [[pdz-domain]] · [[cyclic-di-gmp]] · [[nod2]] · [[muramyl-dipeptide]] · [[pam3csk4-tlr12-agonist]] · [[salmonella-typhimurium]] · [[edwardsiella-tarda]] · [[nf-kb-p65-rela]] · [[inflammatory-bowel-disease]] · [[tnf-tumor-necrosis-factor]] · [[il-6-cytokine]] · [[cxcl8-il8]]
