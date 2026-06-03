---
title: "A finite-sample-size solution exists only above a dispersion-dependent threshold"
slug: deseq2-sample-size-solution-exists-only
status: supported
confidence: 0.85
tags: [deseq2, dispersion, power-analysis, statistics, edge-case]
domain: "statistics / methods"
source_papers:
  - depower-approximate-power-analysis-deseq2
evidence:
  - source: depower-approximate-power-analysis-deseq2
    type: supports
    strength: moderate
    detail: "Eq. 4 yields a real σ_LFC solution only when σ_LFC > √2; threshold only binds at d+ ≈ 10 or μ̄ ≈ 1 (qPCR-like regime)."
conditions: "Dispersion constrained to upper bound max(n,10); relevant only at very low μ̄ / very high dispersion."
date_proposed: 2026-06-03
date_updated: 2026-06-03
---

## Statement

When the dispersion is constrained to its default upper limit \(\max(n,10)\), solving for \(\sigma_{\mathrm{LFC}}\) (Eq. 4) gives a real-valued solution only if \(\sigma_{\mathrm{LFC}}>\sqrt{2}\); if \(\mathrm{LFC}\sqrt{W}\) is below this, the target significance cannot be met at any finite sample size. This edge case only becomes relevant at \(d_+ \approx 10\) or \(\bar\mu \approx 1\) — a regime more appropriate for targeted assays like qPCR than genome-wide RNA-seq.

## Evidence summary

Algebraic consequence of the dispersion upper bound in the DESeq2 model (Eq. 4).

## Conditions and scope

Only binds in the very-low-expression / very-high-dispersion corner; not a practical concern for typical genome-wide assays.

## Counter-evidence

None mathematically; practically the regime is rarely encountered in RNA-seq.

## Linked ideas

- [[concepts/analytical-power-analysis-deseq2-model]]

## Open questions

- Whether targeted-assay (qPCR) design should use a different dispersion model entirely.
