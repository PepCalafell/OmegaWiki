---
title: "Benjamini–Hochberg FDR — step-up false discovery rate control"
slug: benjamini-hochberg-fdr
domain: "statistics / methods"
status: mainstream
aliases:
  - "Benjamini-Hochberg"
  - "BH procedure"
  - "BH FDR"
first_introduced: "Benjamini & Hochberg 1995 *JRSS-B*"
date_updated: 2026-06-03
source_url: "https://doi.org/10.1111/j.2517-6161.1995.tb02031.x"
---

## Definition

The Benjamini–Hochberg (BH) procedure controls the false discovery rate — the expected proportion of false positives among rejected hypotheses — when performing many simultaneous tests. P-values are ranked, and the largest rank \(j\) whose p-value satisfies \(p_{(j)} \le \frac{j}{N}\alpha\) (equivalently adjusted \(Q_{(j)}=\frac{N}{j}p_{(j)}\le\alpha\)) sets the rejection threshold.

## Intuition

Unlike Bonferroni, which controls the family-wise error rate by dividing \(\alpha\) by \(N\), BH allows more discoveries by tolerating a controlled fraction of false positives. It is DESeq2's native multiple-testing correction.

## Formal notation

Reject \(H_{(1)},\dots,H_{(k)}\) where \(k=\max\{j: p_{(j)}\le \frac{j}{N}\alpha\}\). Adjusted value \(Q_{(j)}=\frac{N}{j}p_{(j)}\).

## Key variants

- Bonferroni correction: \(p^* = p/N\) (FWER control, more conservative).
- Benjamini–Yekutieli: FDR control under arbitrary dependence.

## Known limitations

- The adjusted value depends on the full p-value distribution, so it cannot be computed for a single hypothesis a priori — it must be approximated (e.g. by assuming a p-value quantile \(q\)) for power analysis.
- Standard BH assumes independence or positive dependence among tests.

## Open problems

- Choosing realistic non-null fractions \(q\) for prospective power calculations.

## Relevance to active research

- [[papers/depower-approximate-power-analysis-deseq2]] approximates BH for prospective sample-size estimation via \(p^*=qp\), contrasting it with the conservative Bonferroni case.
