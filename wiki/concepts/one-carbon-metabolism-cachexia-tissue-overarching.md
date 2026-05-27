---
title: "One-carbon metabolism as a tissue-overarching pathway in cancer cachexia"
aliases:
  - "tissue-overarching one-carbon activation cachexia"
  - "one-carbon signature of cancer cachexia"
tags:
  - one-carbon-metabolism
  - cachexia
  - methionine-cycle
  - folate-cycle
  - multi-tissue
  - methylation
maturity: emerging
key_papers:
  - multi-omics-profiling-cachexia-targeted-tissues
first_introduced: "Morigny et al. 2026 (Nat Metab) — formal cachexia framing; one-carbon pathway itself reviewed in Ducker & Rabinowitz 2017"
date_updated: 2026-05-27
related_concepts:
  - il6-driven-cachexia-one-carbon-reprogramming
  - methionine-cycle-myotube-atrophy-hypermetabolism
  - nnmt-mnam-liver-cachexia-axis
  - muscle-glucose-hypermetabolism-cachexia-tca-rewiring
  - multi-omics-coordinated-host-tissue-response-cachexia
---

## Definition

The concept that one-carbon metabolism (methionine cycle, folate cycle, polyamine and transsulfuration branches, including NNMT/MNAM, GNMT/sarcosine, KMT2A/B-methyllysines, SAT1-polyamines, GPX3/GSTA4-glutathione arms) is upregulated coordinately across multiple host tissues — liver, plasma, eWAT, iWAT, heart, GC muscle, soleus and tumour — during cancer cachexia, with substrate (glycine, serine) depletion and methylated-product (sarcosine, MNAM, di/tri-methyllysine, dimethylglycine, thymidine) accumulation as a unifying flux signature.

## Intuition

In cachexia each host tissue does *not* run an idiosyncratic metabolic program — they all reroute amino-acid-derived methyl flux through one-carbon metabolism, but with tissue-specific dominant methyl acceptors (MNAM in liver, sarcosine + methyllysines in muscle/adipose). This is what makes "one-carbon" the unifying axis: substrate depletion is global (plasma glycine/serine fall), product accumulation is global, but the consumer enzyme is tissue-typed.

## Formal notation

- Substrates depleted (plasma, multi-tissue): glycine, serine, methionine (relative).
- Products elevated (multi-tissue Cluster #1 of pseudo-time clustering): sarcosine, MNAM, di/tri-methyllysine, dimethylglycine, thymidine, ureidopropionic acid, glycyl-glutamate, aminoadipic acid.
- Activated KEGG pathways (Cax vs Ctrl + Non-cax): one-carbon pool by folate, pyrimidine metabolism, Gly/Ser/Thr metabolism, arginine biosynthesis.
- SAH/SAM ratio: trend ↑ in plasma, adipose, tumour. THF/5-methylTHF ratio: trend ↑ in liver.
- Enzyme upregulation (multi-tissue): Mat1a, Nnmt (liver); Mat2a, Kmt2a/b (muscle); Sat1, Gpx3, Gsta4 (multi-tissue).
- Conservation: documented in C26, Panc02, 8025, ApcMin, LLC, KPP and humanised SW480 mouse models; translates to human sarcopenic cancer patient liver/muscle.

## Variants

- Tissue-restricted variants:
  - **Liver one-carbon variant**: NNMT-MNAM dominant; MAT1A induction; detoxification framing.
  - **Muscle one-carbon variant**: methyllysine and sarcosine dominant; coupled to glucose hypermetabolism.
  - **Adipose one-carbon variant**: methyllysines + sarcosine; previously linked to phospholipid remodelling.
- Driver variants:
  - **IL6-driven** (this paper) — abolished by IL6 KO/neutralisation.
  - **Mitochondrial-dysfunction-driven** (refs 48-50 in paper) — one-carbon as a stress response to mitochondrial failure.

## Comparison

- Vs other proposed cachexia "unifying hubs" (cytokine-driven proteolysis, IL6-STAT3 muscle program, lipid-mobilisation programs): one-carbon is the first **metabolic** unifying axis across tissues, and is mechanistically downstream of inflammation rather than transcription-factor-mediated.
- Vs single-tissue methionine/SAM biology in macrophages ([[concepts/ac-derived-methionine-sam-macrophage-epigenetics]]): in macrophages SAM fuels DNMT3A for transient methylation; in cachexia the methyl flux runs through *multiple* writers (DNMT, KMT, NNMT, GNMT, PEMT, SAT1) and accumulates as products rather than ending on chromatin.

## When to use

- When designing biomarker panels for cachexia risk stratification across tumour entities (the pathway is conserved across six mouse models + patients).
- When considering therapeutic targets that act across tissues simultaneously rather than per-organ (e.g., systemic MAT inhibition, dietary methionine restriction).
- When interpreting tumour-bearing-host transcriptomes that show shared NNMT/MAT2A/Kmt2a/SAT1 upregulation as a coherent unit rather than independent hits.

## Known limitations

- Cause-or-consequence remains unresolved in vivo — only in vitro causality (methionine → atrophy; FIDAS-5 → rescue) shown.
- "Tissue-overarching" claim rests on bulk RNA-seq + bulk metabolomics — cell-type-resolved data missing.
- Tumour ↔ host directionality of one-carbon metabolite trafficking not isotopically resolved.

## Open problems

- Which downstream methylation marks (DNA / RNA / histone / small-molecule) are causally required for cachexia wasting?
- Is the IL6 → one-carbon axis recapitulated in human patients longitudinally (pre-cachexia → cachexia)?
- Does the one-carbon signature interact with hypoxia-driven metabolic rewiring in tumour-bearing host tissues?
- Can methylated products (MNAM, sarcosine, methyllysines) serve as routine clinical biomarkers for pre-cachexia detection?

## Key papers

- [[papers/multi-omics-profiling-cachexia-targeted-tissues]] — Morigny et al. 2026 *Nat Metab*; introduces the formal tissue-overarching framing.

## My understanding

This is a domain-defining concept for the cachexia branch of the wiki. It will likely become the anchor for downstream concepts (per-tissue variants, IL6 mechanism, FIDAS-5/methionine-restriction therapeutics, biomarker panels). The conceptual bridge to existing wiki content is via methionine-cycle macrophage biology — the same biochemistry (Met → SAM → methyltransferase → methylated product) is repurposed across very different contexts (efferocytosis resolution vs cachectic wasting), suggesting one-carbon metabolism is a generic adaptation node for inflammation-driven tissue reprogramming.
