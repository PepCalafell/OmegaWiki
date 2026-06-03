---
# === Identification ===
title: "DEPower: approximate power analysis with DESeq2"
slug: depower-approximate-power-analysis-deseq2
arxiv: ""
doi: "10.64898/2026.02.05.704084"
pmid: ""
venue: "bioRxiv"
year: 2026
authors: [Gennady Gorin, Deek Guruge, Linda Goodman]
first_author: "Gennady Gorin"
corresponding_author: "Linda Goodman"

# === Source & metadata ===
source_type: pdf
s2_id: ""
date_added: 2026-06-03
ingested_date: 2026-06-03
ingest_version: 1
last_reviewed:

# === Classification ===
importance: 3
tier: TIER_2
tags: [power-analysis, sample-size, rna-seq, deseq2, experimental-design, single-cell, statistics, methods]
keywords: [DESeq2, power analysis, sample size, Wald test, dispersion, PyDESeq2, false discovery rate, single-cell RNA-seq]
domain: "methods"

# === Biomedical domain (fill if applicable, else leave empty list/null) ===
tissue: [liver]
condition: []
disease_specific: []
species: []
hypoxia_relevant: false
contains_immune_cells: false
contains_myeloid: false

# === Technique ===
techniques: [bulk_RNA-seq, scRNA-seq_10x, snRNA-seq]
n_samples: 16
n_cells_total:
integration_method: ""

# === Biology captured (extracted from paper) ===
key_cell_types: []
key_markers: []
key_pathways: []

# === User project membership (multi-valued) ===
projects: [methods, thesis]
priority: context
read_status: read

# === HypoxiaVERSE-specific ===
hypoxiaverse_status:
exclusion_reason:
data_availability: "GSE254223 (demonstration dataset); code at https://github.com/Fauna-Bio/GGG_2026; web app https://poweranalysis-fb.streamlit.app/"

# === Cross-references ===
code_url: "https://github.com/Fauna-Bio/GGG_2026"
cited_by: []
---

## Problem

Rigorous RNA-seq experimental design requires formal power analysis — computing the minimum number of samples needed to detect an effect of a given size at a target significance level. Ideally the test used for sample-size determination matches the test used for analysis, but few tools use the assumptions of DESeq2, the dominant differential-expression framework, and most existing tools are simulation-based rather than analytical. There is no widely available closed-form power analysis grounded specifically in the DESeq2 model.

## Key idea

Because DESeq2 significance reduces to a Wald test (\(\sqrt{W}=\mathrm{LFC}/\sigma_{\mathrm{LFC}}\)) and the standard error \(\sigma_{\mathrm{LFC}}\) has an approximate closed form in the fitted means, gene-specific dispersion, and replicate count, one can invert the significance condition to solve directly for the required sample size — an elementary analytical consequence of the DESeq2 model. The authors package this as a Streamlit web calculator, DEPower.

## Method

Starting from the two-sided Wald test, the test statistic is \(\sqrt{W}=\mathrm{LFC}/\sigma_{\mathrm{LFC}}\) and significance requires \(\sqrt{W}=z_{1-\alpha/2}\) (Eq. 1). The LFC standard error is \(\sigma_{\mathrm{LFC}}^2=\frac{1}{n}(\frac{1}{W_0}+\frac{1}{W_1})\) with per-sample Fisher information \(W_i=\mu_i/(1+\mu_i d)\) and \(\mu_1=e^{\mathrm{LFC}}\mu_0\) (Eq. 2); an unbalanced generalization is given (Eqs. 6–7). Dispersion is supplied by a data-free heuristic band on the mean-dispersion curve \(d(\bar\mu)=a_0+a_1/\bar\mu\) (Eq. 3): a logarithmic-midpoint "typical" curve plus optimistic/pessimistic bounds at \(\times 10^{\mp 1/2}\). Multiple testing is handled by Bonferroni (\(p^*=p/N\)) or an approximate Benjamini–Hochberg (\(p^*=qp\)). The six-step recipe solves for the minimal \(n\). Validation uses the "forward" estimation problem on PyDESeq2 0.4.8 as a baseline.

## Results

On mitochondrial-microRNA counts from thirteen-lined ground squirrel liver (Robichaud et al., GSE254223; summer TSL vs. torpid TTL, 8 animals/group), the heuristic intermediate statistics and p-values are broadly concordant with full PyDESeq2 (Fig. 1b–d). The dispersion heuristic agrees with the PyDESeq2 trend although individual genes fall outside the band; the deviations in p-value are overwhelmingly attributable to the ad hoc dispersion — substituting the true PyDESeq2 dispersion gives near-identical p-values. A worked single-cell example shows that a rare cell type (1% of 10,000 cells) needs ~6 samples/condition (nominal) but 28 (Bonferroni) or 22 (BH) once genome-wide correction is applied — dozens of samples even optimistically.

## All claims (exhaustive)

- `[c01]` Square-root Wald statistic equals LFC over its standard error (p.2) "√W = θ̂/σθ̂ = LFC/σLFC" — confidence: high — type: methodological — links: [[foundations/wald-test]] [[foundations/deseq2-differential-expression]] [[claims/square-root-wald-statistic-equals-lfc]]
- `[c02]` LFC standard error scales as (1/n)(1/W0+1/W1) with per-sample Fisher information W_i=μ_i/(1+μ_i d) (p.2) "σ²LFC = 1/n (1/W0 + 1/W1), such that Wi = μi/(1 + μi d)" — confidence: high — type: methodological — links: [[concepts/analytical-power-analysis-deseq2-model]] [[claims/lfc-standard-error-scales-inversely-sample]]
- `[c03]` A finite-sample-size solution exists only when σ_LFC>√2; edge case only binds at d+≈10 or μ̄≈1 (qPCR regime) (p.2-4) "which only provides a real-valued solution for σLFC > √2 ... only becomes relevant at d+ = 10 or μ̄ ≈ 1" — confidence: high — type: quantitative — links: [[concepts/analytical-power-analysis-deseq2-model]] [[claims/deseq2-sample-size-solution-exists-only]]
- `[c04]` The DESeq2 mean-dispersion curve is approximated by a data-free order-of-magnitude band (typical ã0=10^-3/2, ã1=10^1/2; ±10^1/2 bounds) (p.2) "a somewhat arbitrary but reasonable choice is the logarithmic midpoint ... optimistic low-dispersion case ... pessimistic high-dispersion case" — confidence: medium — type: methodological — links: [[concepts/heuristic-dispersion-band-mean-expression]] [[claims/deseq2-mean-dispersion-curve-approximated-heuristic]]
- `[c05]` Heuristic p-values are broadly concordant with full PyDESeq2; deviations explained by the ad hoc dispersion (p.5-6) "deviations from the p-value obtained through the full procedure are overwhelmingly explained by the ad hoc dispersion estimate: if the PyDESeq2 estimate is used, the results agree" — confidence: medium — type: correlational — links: [[concepts/heuristic-dispersion-band-mean-expression]] [[foundations/pydeseq2]] [[claims/heuristic-deseq2-power-analysis-values-concordant]]
- `[c06]` A rare cell type (1% of 10,000 cells) needs ~6 samples/condition to detect log2FC=1 at nominal p=0.05 (3/14 low/high dispersion) (p.4) "would require 6 samples per condition (3/14 for the low-/high-dispersion cases)" — confidence: medium — type: quantitative — links: [[concepts/rare-cell-type-single-cell-enrichment]] [[claims/rare-cell-type-log2-fold-change]]
- `[c07]` Genome-wide correction sharply increases required n: 28 (Bonferroni, 14/74) or 22 (BH q=0.1, 11/58) over ~10,000 genes (p.4-5) "under the Bonferroni correction would require 28 samples (14/74) ... under the Benjamini–Hochberg procedure ... would require 22 (11/58) samples" — confidence: medium — type: quantitative — links: [[foundations/benjamini-hochberg-fdr]] [[claims/genome-wide-fdr-correction-sharply-increases]]
- `[c08]` Standard unbiased single-cell RNA-seq is statistically insufficient for rare cell types; enrichment is mandatory (p.5) "standard 'unbiased' single-cell RNA sequencing is insufficient to investigate this cell population at the specified significance, and cell type enrichment is mandatory" — confidence: medium — type: methodological — links: [[concepts/rare-cell-type-single-cell-enrichment]] [[claims/unbiased-single-cell-rna-seq-insufficient]]
- `[c09]` The same mathematics can flag implausible published results (e.g. p=10^-200 at log2FC=1, n=3) but is impractical as a scalable fraud detector (p.6-7) "it is possible to scrutinize published experiments and check whether extreme results ... are mathematically plausible ... However, this approach is unlikely to be broadly fruitful" — confidence: low — type: methodological — links: [[concepts/power-analysis-research-fraud-detector]] [[claims/power-analysis-flag-implausible-published-results]]
- `[c10]` Sample-size estimates should be treated as a lower bound under ideal assumptions (p.4) "the results of the sample size analysis should be seen as a lower bound under the ideal-case scenario" — confidence: high — type: methodological — links: [[concepts/analytical-power-analysis-deseq2-model]] [[claims/deseq2-sample-size-estimates-lower-bound]]

## Discussion captured

### Authors' interpretation

The authors frame the approximate relationship between sample size, effect size, and significance as an elementary consequence of the DESeq2 model that fills a gap in the literature (analytical rather than simulation-based, and DESeq2-specific). They emphasize the method is sufficient for "order-of-magnitude, back-of-the-envelope calculations" and that the dominant source of inaccuracy is the ad hoc dispersion estimate, which pilot data can replace.

### Comparisons with prior literature (made by authors)

- DESeq2 itself: Love, Huber & Anders 2014 (doi:10.1186/s13059-014-0550-8).
- PyDESeq2 baseline: Muzellec et al. 2023 (doi:10.1093/bioinformatics/btad547).
- Prior power/sample-size tools, mostly simulation-based: Ching et al. 2014, Bi & Liu 2016, Li & Shyr 2016, Poplawski & Binder 2018, scDesign (Li & Li 2019), Su et al. 2020, scPower (Schmid et al. 2021), Jeon et al. 2023; few analytical treatments (Bi & Liu 2016; Hart et al. 2013).
- Benjamini & Hochberg 1995 for FDR control.
- Pseudoreplication / false discoveries in single-cell DE: Squair et al. 2021, Zimmerman et al. 2021, Mukamel & Yu 2025, Lee & Han 2024.
- Fraud/metascience context: Richardson et al. 2025 (PNAS), Bik et al. 2016, GRIM (Brown & Heathers 2017), and others.

### Mechanistic hypotheses proposed

- Not a mechanistic biology paper; the central "hypothesis" is mathematical — that DESeq2 power can be derived in closed form by inverting the Wald-test significance condition.

### Caveats and self-criticism

- Neglecting between-condition read-depth variability is an oversimplification (claimed minor).
- The ad hoc dispersion estimate incurs the most severe errors; individual genes fall outside the band.
- The Wald test relies on asymptotic chi-square convergence, less reliable at small n.
- Estimates assume the negative-binomial model holds; batches/outliers raise the needed n.
- For fraud detection: laborious, suggestive not conclusive, confounded with tool misuse, and bypassed by data fabrication or large public datasets.

### Future directions suggested

- Use pilot data to replace the heuristic dispersion when available.
- Adapt the procedure to specific experimental circumstances.

## Limitations

- Single, small, qualitative validation dataset (ground squirrel liver miRNA); no systematic accuracy benchmark.
- Heuristic dispersion is data-free and the dominant error source.
- Closed form omits covariates/batches and assumes balanced depth.
- Small-sample Wald non-asymptotics not corrected.

## Open questions

### Open questions raised by authors

- How to choose the BH non-null quantile \(q\) defensibly for prospective design.
- When pilot data are unavailable, how tight can a purely heuristic dispersion band be made?

### Open questions identified during ingest

- How well does heuristic-vs-full concordance hold across larger, heterogeneous, unbalanced designs?
- What empirical inflation factor converts the "lower bound" into a realistic target n?
- Quantitative power/cost trade-off of specific cell-type enrichment strategies.

## My take

A short, honest, and practically useful methods note. The value is less in mathematical novelty (it is "elementary") than in giving a fast, DESeq2-consistent, transparent sample-size calculator that matches the test people actually run — directly relevant to designing my own RNA-seq / single-nucleus experiments. The rare-cell-type conclusion (enrichment is effectively mandatory for stringent DE) is a concrete design rule worth remembering. The dispersion heuristic is the obvious weak point, and the authors say so; with pilot data the method tightens considerably. The fraud-detection aside is intriguing but the authors themselves deflate it.

## Related

- [[concepts/analytical-power-analysis-deseq2-model]]
- [[concepts/heuristic-dispersion-band-mean-expression]]
- [[concepts/rare-cell-type-single-cell-enrichment]]
- [[concepts/power-analysis-research-fraud-detector]]
- [[foundations/deseq2-differential-expression]]
- [[foundations/pydeseq2]]
- [[foundations/wald-test]]
- [[foundations/benjamini-hochberg-fdr]]
- [[people/gennady-gorin]]
- [[people/linda-goodman]]
