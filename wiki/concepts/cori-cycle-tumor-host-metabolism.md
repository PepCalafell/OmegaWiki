---
title: "Cori cycle and tumour-driven host metabolic rewiring"
aliases:
  - "Cori cycle hypermetabolism cancer"
  - "tumor lactate hepatic gluconeogenesis"
tags:
  - cachexia
  - oncology
  - metabolism
  - cori-cycle
maturity: active
key_papers:
  - cancer-associated-cachexia-bridging-clinical-findings
first_introduced: "Cori 1929 (Cori cycle); Faubert et al. 2017 Cell; Hensley et al. 2016 Cell (NSCLC isotope tracing)"
date_updated: 2026-05-27
related_concepts: []
---

## Definition

The Cori cycle is the inter-organ recycling of lactate produced by tissues (here, the tumour) back to glucose via hepatic gluconeogenesis. In cancer, this loop is hijacked: tumour-derived lactate is converted to glucose by the liver at the cost of ATP, and the tumour re-imports the glucose — net result is an energetically expensive futile cycle that elevates host resting energy expenditure (REE) and contributes to cachexia. Modern in-vivo isotope tracing reveals that, in NSCLC, lactate is ALSO used by the tumour to fuel the TCA cycle directly — refining (not replacing) the classical Warburg/Cori picture.

## Intuition

Tumour hypermetabolism does not require the tumour itself to burn vast amounts of ATP; it can drain the host by forcing the liver to spend ATP regenerating glucose from the tumour's lactate output, while also using lactate as a TCA substrate. Tumour burden then maps to host REE via this loop and explains why metastatic spread to liver (large metabolic mass) further amplifies CAC.

## Formal notation

- Cori cycle ATP balance: ~6 ATP consumed in hepatic gluconeogenesis to regenerate glucose from 2 lactate → tumour consumes ~2 ATP via glycolysis → net loss of ~4 ATP per cycle, paid by the host.
- Modern isotope tracing (in vivo [13C]-glucose, [13C]-lactate): quantifies tumour vs adjacent-tissue glucose oxidation and lactate utilization.
- PET-FDG: indirect uptake measure correlating with energy expenditure and weight loss in esophageal and NSCLC cohorts.

## Variants

- Cori cycle (lactate-glucose, classical).
- Glutamine-glutamate Cahill-cycle analogue (amino acid - based futile cycling).
- Tumour-direct lactate-TCA oxidation (Faubert et al.) — not a futile cycle per se, but adds to tumour nutrient demand.

## Comparison

vs the Warburg effect: Warburg posits the tumour itself favours aerobic glycolysis over OXPHOS, generating lactate locally — but the Warburg effect alone is insufficient to explain host hypermetabolism. The Cori-cycle reframing shifts emphasis from tumour-intrinsic to inter-organ tumour-host metabolic coupling.

vs simple gluconeogenesis (starvation): in CAC, hepatic gluconeogenesis is increased even in the fed state and persists despite adequate dietary intake.

## When to use

When discussing host hypermetabolism in CAC, the role of liver metastases in amplifying REE, or the rationale for in-vivo metabolic-flux tracing in patients.

## Known limitations

- Direct quantification of Cori-cycle flux in human cancer patients remains rare and challenging (requires multi-tracer studies).
- The relative contribution of Cori cycle vs other futile cycles (e.g., triglyceride-FFA cycling) to host REE elevation is unclear.
- PET-FDG-based ML models for CAC detection have only retrospective single-centre validation.

## Open problems

- Can targeting hepatic gluconeogenesis (metformin? specific GP inhibitors?) reduce host REE without harming tumour control?
- Are lactate-shuttle inhibitors (MCT1/MCT4 antagonists) viable CAC therapeutics?
- How does the Cori cycle interact with the IL-6/NNMT one-carbon-metabolism axis described in [[papers/multi-omics-profiling-cachexia-targeted-tissues]]?

## Key papers

- [[papers/cancer-associated-cachexia-bridging-clinical-findings]] — review framing.

## My understanding

The Cori cycle is a useful organizing concept but probably one of several inter-organ futile cycles that collectively explain host hypermetabolism. The therapeutic angle is appealing (target an inter-organ loop without targeting the tumour itself) but pharmacologically immature.
