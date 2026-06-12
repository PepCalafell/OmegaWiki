---
title: "mini-SWE-agent harness"
slug: mini-swe-agent-harness
domain: methods
status: mainstream
aliases:
  - mini-SWE-agent
  - mini SWE agent
first_introduced: "2024"
date_updated: 2026-06-12
source_url: "https://github.com/SWE-agent/mini-SWE-agent"
---

## Definition

mini-SWE-agent is an open-source minimal agent harness that implements a simple
action loop for LLM-driven tool use: the model generates a free-form response,
the harness extracts the first fenced code block (markdown triple-backtick), executes
it in a local bash shell, and returns stdout/stderr to the model as the next
observation. It is the harness under which `scBench` evaluates all frontier models.

## Intuition

The harness deliberately keeps the scaffold thin so that measured performance
reflects the underlying model's capability rather than elaborate prompt
engineering. The only affordance is "write code → run it → read the output",
iterated until the agent writes an answer file or exhausts its step budget.

## Formal notation

Each step is the triple (LLM turn → code extraction → execution → observation).
In scBench, each evaluation is capped at 100 action steps; if the agent never
writes `eval_answer.json`, the run scores zero.

## Key variants

- Plain mini-SWE-agent bash loop (as used by scBench and SpatialBench).
- Pluggable `agent_function` interface, enabling custom agents to be compared
  against published results.

## Known limitations

- Single fenced-block extraction per turn constrains the action space to one
  command at a time.
- No built-in retry logic; in scBench each replicate is a single attempt.
- Bash-only execution with no GUI/interactive tooling (no Jupyter, no plot display).

## Open problems

- How much of measured model performance is attributable to harness design
  versus model capability remains an open question that the authors raise as a
  target for "harness engineering".

## Relevance to active research

mini-SWE-agent is the standard evaluation substrate for agentic benchmarks on
scientific data analysis, including scBench (scRNA-seq) and SpatialBench
(spatial transcriptomics). Bounded by two timeout layers (300 s per bash
command, 600 s per evaluation via `SIGALRM`), it provides reproducible,
trajectory-logged execution for post-hoc analysis of agent behaviour.
