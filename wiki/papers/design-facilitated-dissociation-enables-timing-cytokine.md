---
# === Identification ===
title: "Design of facilitated dissociation enables timing of cytokine signalling"
slug: "design-facilitated-dissociation-enables-timing-cytokine"
arxiv: ""
doi: "10.1038/s41586-025-09549-z"
pmid: "40993395"
venue: "Nature"
year: 2025
authors:
  - Adam J. Broerman
  - Christoph Pollmann
  - Yang Zhao
  - Mauriz A. Lichtenstein
  - Mark D. Jackson
  - Maxx H. Tessmer
  - Won Hee Ryu
  - Masato Ogishi
  - Mohamad H. Abedi
  - Danny D. Sahtoe
  - Aza Allen
  - Alex Kang
  - Joshmyn De La Cruz
  - Evans Brackenbrough
  - Banumathi Sankaran
  - Asim K. Bera
  - Daniel M. Zuckerman
  - Stefan Stoll
  - K. Christopher Garcia
  - Florian Praetorius
  - Jacob Piehler
  - David Baker
first_author: "Adam J. Broerman"
corresponding_author: "Adam J. Broerman; Florian Praetorius; David Baker"

# === Source & metadata ===
source_type: pdf
s2_id: "79372a68f322a9a713734d4c903d521a0b890d67"
date_added: 2026-06-10
ingested_date: 2026-06-10
ingest_version: 1
last_reviewed:

# === Classification ===
importance: 4
tier: TIER_1
tags:
  - protein-design
  - de-novo-design
  - facilitated-dissociation
  - conformational-switch
  - binding-kinetics
  - induced-fit
  - power-stroke
  - biosensor
  - cytokine-engineering
  - IL-2
keywords:
  - facilitated dissociation
  - excited states
  - structural frustration
  - allosteric switch
  - ASNeo2
  - IL-2 signalling dynamics
  - LOCKR / hinge switch
domain: protein design

# === Biomedical domain ===
tissue:
  - blood
  - in_vitro_only
condition:
  - healthy
disease_specific: []
species:
  - human
hypoxia_relevant: false
contains_immune_cells: true
contains_myeloid: false

# === Technique ===
techniques:
  - X-ray_crystallography
  - DEER_spectroscopy
  - surface_plasmon_resonance
  - MD_simulation
  - single-molecule_fluorescence
  - smFRET
  - NanoBiT_split_luciferase
  - flow_cytometry
  - bulk_RNA-seq
  - qPCR
n_samples:
n_cells_total:
integration_method: ""

# === Biology captured ===
key_cell_types:
  - primary human T cells
  - NK cells (YT-1)
key_markers:
  - IL-2
  - IL-2Rβ
  - γc (IL2RG)
  - STAT5
  - BCL2
  - caspase-3
  - SOCS2
  - CISH
  - CDKN2B
  - CDK6
key_pathways:
  - IL-2/IL-2Rβγc signalling
  - JAK-STAT5
  - apoptosis
  - cell-cycle (G1/S)
  - oxidative phosphorylation

# === User project membership ===
projects:
  - thesis
  - methods
priority: context
read_status: not_read

# === HypoxiaVERSE-specific ===
hypoxiaverse_status:
exclusion_reason:
data_availability: "PDB structures and design models deposited; details at https://doi.org/10.1038/s41586-025-09549-z (PMC12611780)."

# === Cross-references ===
code_url: ""
cited_by: []
---

## Problem

Protein interactions face a fundamental trade-off: high affinity (needed to respond to low concentrations and act potently) requires a slow off-rate, while rapid exchange (needed to respond quickly to changing stimuli) requires a fast off-rate. In a binary interaction these cannot be achieved simultaneously. Natural systems escape this via "facilitated dissociation" — an effector binds a target–host complex and accelerates target release — but there has been no general way to *design* kinetic control over arbitrary protein interactions. More broadly, protein design has focused on low-energy ground states; designing kinetics and dynamics additionally requires designing the strained excited (intermediate) states traversed between states.

## Key idea

Treat the strained intermediate as a designed object. Fuse an effector-responsive conformational switch (a de novo hinge / LOCKR-type protein, [[lockr-de-novo-conformational-switch-hinge]]) to an arbitrary binder so that, when the effector binds and flips the switch to state Y, it sterically clashes with the target. This creates a structurally frustrated, strained ternary complex (THE) — a designed excited state ([[designed-protein-excited-states-kinetic-control]]) — from which the target dissociates orders of magnitude faster than spontaneously ([[facilitated-dissociation-effector-induced]]). A flexible, disordered effector that folds upon binding provides an induced-fit "power stroke" that drives the switch through the strained transition faster than a rigid effector ([[induced-fit-power-stroke-flexible-effector]]). Applied to the IL-2 mimic Neo2, this yields ASNeo2, a cytokine whose signalling can be switched off within seconds ([[switchable-cytokine-mimic-signalling-timing]]).

## Method

De novo hinge switches (from cs221/3hb21) were re-engineered to keep an open effector cleft in state X (enabling induced-fit binding) while clashing with the target in state Y, then rigidly fused to binders at geometries sampled and rebuilt with AlphaFold2 ([[alphafold-multimer]]) to tune strain magnitude and direction. Binding kinetics (kon, koff, fold acceleration) were measured by surface plasmon resonance ([[surface-plasmon-resonance-spr]]); structures were solved by X-ray crystallography; ternary-complex dynamics probed by DEER spectroscopy and MD. Applications used NanoBiT split luciferase ([[nanobit-split-luciferase]]) for circuits/sensors, single-molecule fluorescence microscopy + smFRET for live-cell receptor dimerization, pSTAT5 assays in YT-1 NK cells (with ruxolitinib [[ruxolitinib-jak-inhibitor]] as control), and CFSE/survival/qPCR/RNA-seq in primary human T cells.

## Results

Designed allosteric switches achieved effector-induced target-dissociation accelerations from ~12-fold up to 5,700-fold. Kinetics and crystal structures (≤1.3 Å to design) confirmed the strained ternary intermediate and the register-shift X→Y conformational change. A flexible peptide effector outperformed a tighter-binding rigid 3hb effector via induced fit. Strain energy depended on both deformation magnitude and direction, with non-uniform strain giving kinetic asymmetry; variant AS117 reached 2,400-fold forward acceleration. Applications: a SARS-CoV-2 biosensor (30-fold signal, 30 s half-time, ~70× faster than a LOCKR sensor); chain-reaction circuits; rapid split-luciferase breakage; and ASNeo2, a switchable IL-2 mimic (1,500-fold γc off-rate increase) that reverses receptor dimerization in seconds on live cells and shuts down STAT5 nearly as well as ruxolitinib. Using ASNeo2 to time IL-2 signalling showed sustained signalling is required for proliferation while a brief pulse suffices for apoptosis protection, with distinct transcriptional programs.

## All claims (exhaustive)

- `[c1]` Designed strained excited states enable effector-induced dissociation-rate increases up to 5,700-fold (p.1, abstract) "incorporating excited states enables the design of effector-induced increases in dissociation rates as high as 5,700-fold" — confidence: high — type: quantitative — links: [[claims/fd-effector-induced-dissociation-up-to-5700-fold]] [[concepts/facilitated-dissociation-effector-induced]] [[concepts/designed-protein-excited-states-kinetic-control]]
- `[c2]` Facilitated dissociation proceeds through a strained ternary (THE) intermediate, faster than mutually exclusive competition (p.3) "the rate constant of facilitated target dissociation approaches koff,T:HE ... strongly suggesting that the ternary complex is an intermediate" — confidence: high — type: mechanistic — links: [[claims/strained-ternary-intermediate-faster-than-competition]] [[concepts/facilitated-dissociation-effector-induced]]
- `[c3]` The ternary-intermediate energy must lie in an optimal window for fast facilitated dissociation (p.2) "neither too high (otherwise the facilitated dissociation pathway would not be faster) nor too low (otherwise the target would not dissociate)" — confidence: high — type: mechanistic — links: [[claims/ternary-intermediate-energy-optimal-window]] [[concepts/designed-protein-excited-states-kinetic-control]] [[concepts/facilitated-dissociation-effector-induced]]
- `[c4]` A flexible peptide effector accelerates dissociation faster than a tighter-binding rigid effector, via an induced-fit power stroke (p.6) "a rigid effector provides reduced rate acceleration even though it binds more tightly" — confidence: high — type: mechanistic — links: [[claims/flexible-effector-faster-than-rigid-induced-fit]] [[concepts/induced-fit-power-stroke-flexible-effector]]
- `[c5]` Crystal structures match designed states to ≤1.3 Å and show effector binding drives a register-shift X→Y change (p.4) "closely match the design models (maximum 1.3 Å Cα root mean square deviation)" — confidence: high — type: methodological — links: [[claims/designed-states-match-crystal-register-shift]] [[foundations/alphafold-multimer]] [[foundations/lockr-de-novo-conformational-switch-hinge]]
- `[c6]` Strain in the ternary complex distributes across multiple sites — the binder bends, the target twists and partially disorders at its interface (p.4) "the binder fusion bends, the portion of the target that directly clashes with the switch becomes disordered and the target twists at its interface" — confidence: high — type: mechanistic — links: [[claims/ternary-strain-distributes-multiple-sites]] [[concepts/facilitated-dissociation-effector-induced]]
- `[c7]` The target dissociates 20-fold faster from AS1 than from an unhindered binder fusion (minor base-state strain) (p.4) "the target dissociates 20-fold faster from AS1 than from an unhindered binder fusion" — confidence: medium — type: quantitative — links: [[claims/target-dissociates-20-fold-faster-from-as1]] [[foundations/surface-plasmon-resonance-spr]]
- `[c8]` Tuning deformation geometry yields variant AS117 with 2,400-fold forward dissociation acceleration (p.4) "for the fastest variant (AS117), adding effector accelerated target dissociation by 2,400-fold" — confidence: high — type: quantitative — links: [[claims/as117-variant-2400-fold-forward-acceleration]] [[concepts/designed-protein-excited-states-kinetic-control]]
- `[c9]` Global strain energy depends on both magnitude and direction of deformation; non-uniform strain gives kinetic asymmetry (p.5) "the global strain energy of the ternary complex depends on both the magnitude and the direction of the deformation ... leading to kinetic asymmetry" — confidence: medium — type: mechanistic — links: [[claims/strain-energy-depends-magnitude-direction-kinetic-asymmetry]] [[concepts/designed-protein-excited-states-kinetic-control]]
- `[c10]` The allosteric switching-steric-clash mechanism is modular — the switch can be fused to almost any binder (p.6-7) "almost any binding interaction can be made to switch off rapidly in the presence of an effector" — confidence: high — type: methodological — links: [[claims/allosteric-clash-mechanism-modular-any-binder]] [[concepts/facilitated-dissociation-effector-induced]]
- `[c11]` A facilitated-dissociation SARS-CoV-2 biosensor gives 30-fold signal with a 30 s half-time, ~70× faster than a LOCKR sensor (p.6) "the best sensor shows a 30-fold increase in luciferase activity, with a half-time of 30 s—70 times faster than a previously designed LOCKR-based SARS-CoV-2 sensor" — confidence: high — type: quantitative — links: [[claims/ascov-biosensor-30s-70x-faster-than-lockr]] [[foundations/nanobit-split-luciferase]] [[concepts/facilitated-dissociation-effector-induced]]
- `[c12]` Facilitated dissociation enables effector-triggered chain-reaction circuits and rapid breakage of high-affinity split enzymes (p.5) "high luciferase activity that disappears much more rapidly upon addition of effector and excess untagged target than ... target alone" — confidence: medium — type: methodological — links: [[claims/facilitated-dissociation-breaks-circuits-split-enzymes]] [[foundations/nanobit-split-luciferase]] [[concepts/facilitated-dissociation-effector-induced]]
- `[c13]` ASNeo2, a switchable IL-2 mimic, shows a 1,500-fold effector-induced increase in γc off-rate (5,700-fold for an optimized variant) (p.6) "binding the effector induces a 1,500-fold increase in the γc off-rate" — confidence: high — type: quantitative — links: [[claims/asneo2-1500-fold-gc-off-rate-acceleration]] [[concepts/switchable-cytokine-mimic-signalling-timing]] [[foundations/neo2-designed-il-mimic]] [[foundations/il-2-cytokine]]
- `[c14]` The effector rapidly and completely reverses ASNeo2-induced IL-2Rβ/γc dimerization on live-cell membranes (p.6) "adding the effector reverses this association rapidly and completely, even at a high excess of γc" — confidence: high — type: mechanistic — links: [[claims/effector-reverses-asneo2-receptor-dimerization-live-cells]] [[concepts/switchable-cytokine-mimic-signalling-timing]] [[foundations/il-2-cytokine]]
- `[c15]` The effector blocks ASNeo2-driven STAT5 phosphorylation nearly as effectively as ruxolitinib (p.6) "The effector blocks ASNeo2 activity nearly as effectively as does ruxolitinib, a JAK1 inhibitor" — confidence: high — type: pharmacological — links: [[claims/effector-blocks-asneo2-stat5-like-ruxolitinib]] [[concepts/switchable-cytokine-mimic-signalling-timing]] [[foundations/stat5-tf]] [[foundations/ruxolitinib-jak-inhibitor]]
- `[c16]` Sustained IL-2 signalling is required for proliferation, but a brief transient pulse suffices to protect from apoptosis (p.7) "protection from apoptosis was evident after a short transient stimulation ... survived three days later at double the rate of an unstimulated control" — confidence: medium — type: correlational — links: [[claims/sustained-il2-proliferation-transient-apoptosis-protection]] [[concepts/switchable-cytokine-mimic-signalling-timing]]
- `[c17]` Transient IL-2 stimulation upregulates anti-apoptotic/early-cell-cycle/SOCS genes but not MYC/E2F/mTORC sustained-signalling programs (p.7) "IL-2 signalling must be sustained to pass the G1/S checkpoint" — confidence: medium — type: correlational — links: [[claims/transient-il2-upregulates-antiapoptotic-not-sustained-programs]] [[concepts/switchable-cytokine-mimic-signalling-timing]]
- `[c18]` Transient IL-2 stimulation downregulates oxidative-phosphorylation genes and activates mitotic-spindle genes before cell-cycle checkpoints (p.7) "preparations for mitosis are made immediately after T cell activation, before cell-cycle checkpoints" — confidence: medium — type: correlational — links: [[claims/transient-il2-downregulates-oxphos-activates-mitotic-spindle]] [[concepts/switchable-cytokine-mimic-signalling-timing]]

## Discussion captured

### Authors' interpretation

The authors argue that explicitly considering excited intermediate states when designing coupled protein systems unlocks a broad range of facilitated-dissociation behaviours, and that crystal structures throughout the process confirm the ability to design excited states and large register-shift conformational changes. They frame the flexible effector as folding upon binding to drive the conformational transition via a power-stroke mechanism, more efficiently than a ratchet, and note this is the energetic basis for the kinetic advantage of facilitated dissociation over mutually exclusive competition. They emphasize the modularity of the allosteric switching-steric-clash mechanism (no requirement on binder/target), evidenced by immediate transfer to IL-2 signalling (working designs on the first attempt among 24 tested).

### Comparisons with prior literature (made by authors)

Authors compare their allosteric mechanism to natural facilitated-dissociation systems that couple target and effector through direct steric overlap and intricate allostery (NF-κB·IκBα, transcription factors on DNA, myosin/dynein nucleotide exchange, GrpE/DnaK; refs 10–26). They draw an analogy to toehold-mediated strand displacement in DNA nanotechnology (refs 28,29). They contrast induced folding in the kinesin power stroke (ref 53) with their designed flexible effector, arguing their model system uniquely allows direct comparison of flexible vs rigid effectors. The biosensor is benchmarked against a prior LOCKR-based conformational-selection sensor (ref 41).

### Mechanistic hypotheses proposed

- The flexible effector folds upon binding, and the resulting interaction energy compensates uphill steps along the transition coordinate, lowering the barrier (power stroke) (p.6).
- The rigid 3hb effector can only bind the fully open state Y, so the THX→THY change becomes rate-limiting (conformational selection) (p.4).
- Disrupting signalling complexes at the cell surface versus later in the endosome could distinguish responses from each compartment (p.7).

### Caveats and self-criticism

- The ternary complex is dynamic (DEER/MD) rather than a single rigid strained state; strain magnitude varies by location.
- Strain energies are inferred from AF2 predictions and a simple spring model, not directly measured.
- Optimal fusion geometry is found by empirical sampling rather than prediction.

### Future directions suggested

- Local administration of switchable cytokine + systemic effector for site-restricted immune activation (any cytokine escaping into circulation is deactivated).
- Using switchable cytokines to dissect early signalling events and compartment-specific (surface vs endosome) responses.
- Designing the rates and pathways of protein motion toward complex, "lifelike" protein machinery.

## Limitations

- Mechanistic and kinetic characterization is largely in vitro (SPR, crystallography); cellular work is in cell lines (YT-1) and primary human T cells, not in vivo.
- IL-2 transcriptional analysis is a single 6 h RNA-seq timepoint; metabolic flux is inferred from transcripts.
- The switchable cytokine requires co-administered effector to turn off; pharmacokinetics and immunogenicity untested.
- Designs require per-binder geometry sampling; no a priori predictor of strain energy / acceleration.

## Open questions

### Open questions raised by authors

- Do cellular responses differ when IL-2 signalling complexes are disrupted at the cell surface versus in the endosome?
- How can switchable cytokines be deployed therapeutically for timing-controlled immune activation?
- Can the approach be extended to design directional motors and multi-step protein machines?

### Open questions identified during ingest

- Can ternary-complex strain energy and dissociation acceleration be predicted directly from structure, removing the empirical geometry search?
- How does the seconds-scale IL-2 off-switch interact with receptor internalization/endosomal signalling kinetics in vivo?
- Could the same temporal-control logic be applied to other γc-family cytokines (IL-15, IL-7) or to non-cytokine receptor systems relevant to immune regulation?

## My take

The reusable asset is twofold: (1) a *general design principle* — engineer strained excited states to control kinetics — validated crystallographically, and (2) a concrete immunology tool, ASNeo2, that turns IL-2 ligand residence time into an externally controllable variable with seconds resolution. For an immunology-focused vault this is most interesting as a complement to spatial cytokine-restriction strategies already present ([[mmp14-protease-activated-il2-prodrug]], [[trans-acting-immunocytokine]]): those control *where* a cytokine acts; this controls *when/how long*. The duration-dependence finding (proliferation needs sustained signalling; survival/BCL2 needs only a brief pulse) is a clean, hypothesis-generating result enabled entirely by the designed off-switch.

## Related

- [[facilitated-dissociation-effector-induced]] — core mechanism introduced here
- [[designed-protein-excited-states-kinetic-control]] — the underlying design principle
- [[induced-fit-power-stroke-flexible-effector]] — flexible-vs-rigid effector mechanism
- [[switchable-cytokine-mimic-signalling-timing]] — the ASNeo2 application (temporal control of IL-2)
- Complementary cytokine-engineering strategies in the vault (spatial vs temporal control): [[mmp14-protease-activated-il2-prodrug]], [[trans-acting-immunocytokine]], [[myeloid-targeted-immunocytokine-mite]]
- People: [[adam-j-broerman]], [[florian-praetorius]], [[david-baker]], [[k-christopher-garcia]], [[jacob-piehler]]
