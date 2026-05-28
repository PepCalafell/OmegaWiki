---
title: "Transferred adversarial training removes batch effects between train-tissue and target-tissue"
slug: transferred-adversarial-training-removes-batch-effects
status: supported
confidence: 0.8
tags: [batch-effect, adversarial, deconvolution]
domain: methods
source_papers:
  - decode-deep-learning-based-common-deconvolution
evidence:
  - source: decode-deep-learning-based-common-deconvolution
    type: supports
    strength: moderate
    detail: "Stage 2 forces the discriminator to fail at identifying feature origin, mitigating batch effects across platforms, health states and sample types while preserving biological signal (Supplementary Fig. 16a–d)."
conditions: "Demonstrated via supplementary batch-effect analyses; main-text evidence is qualitative."
date_proposed: 2026-05-28
date_updated: 2026-05-28
---

## Statement

DECODE's stage-2 transferred adversarial training aligns train-tissue and target-tissue features, removing batch effects across platforms, health states and sample types while preserving deconvolution-relevant biological signal.

## Evidence summary

"force the discriminator to fail in identifying the origin of the features, thereby effectively mitigating batch effects" (p.597). Effectiveness shown in Supplementary Fig. 16a–d. Encoder parameters are frozen after stage 2 and passed to stage 3.

## Conditions and scope

A specific instance of [[adversarial-domain-adaptation-dann]] applied to deconvolution; balance between batch removal and signal preservation is the operative risk.

## Counter-evidence

None reported; adversarial alignment can in principle over-correct and erase biology.

## Linked ideas

## Open questions

How much biological signal is lost at high alignment strength.
