# Recursive Narrative Evaluation Framework

## Overview

The **Recursive Narrative Evaluation Framework** is a research‑grade suite designed to test large language models (LLMs) under carefully controlled narrative stress.  It focuses on evaluating how open‑source models respond when presented with structured prompts that require tone modulation, iterative repetition, symbolic obedience and controlled escalation.  By exercising these behaviours in a measured way, the framework helps developers identify strengths and weaknesses in model reasoning, memory stability and safety controls.

Unlike conversational demos, this project is not about entertainment or improvisation.  Its goal is to provide clear, repeatable stress tests for models that will underpin serious applications such as personal assistants or therapeutic systems.  Throughout the evaluation process the prompts remain technical and emotionally neutral where possible, ramping up in complexity only as the model demonstrates stability.

## Core Objectives

* **Tone and Context Management** – Assess how models adjust the emotional valence of a repeated quote or narrative element over successive iterations.
* **Symbolic Token Obedience** – Test whether injected control tokens (e.g., `TOKEN_GLITCH`, `TOKEN_CONTAINED`) cause the expected change in behaviour or tone without hallucinating unrelated content.
* **Structural Integrity Under Pressure** – Evaluate how models handle layered instructions or conflicting rules, and whether they respect containment layers designed to moderate or neutralise emotional responses.
* **Quote Fidelity and Evolution** – Monitor whether the core meaning of a quote is preserved when paraphrased or recast under different tones or contexts.
* **Hallucination and Delusion Avoidance** – Identify prompts that may trigger runaway narrative loops or delusional storylines, and ensure that containment mechanisms (the second‑layer “guardian” agent) prevent such escalation.

## Framework Components

### Prompt Harness

Evaluation is driven by a library of scripted prompts organised by complexity.  Scenarios start with simple tone shifts and gradually introduce symbolic tokens, containment protocols and conflicting instructions.  Each prompt is designed to elicit specific model behaviours for analysis.

### Dual‑Agent Architecture

Many tests leverage a two‑part agent design to simulate moderation and self‑reflection.  The “core” agent produces the primary response, while a “guardian” layer (analogous to the fictional **Monday** persona) monitors the output, applies containment rules and ensures that the overall tone remains appropriate.  This separation helps expose weaknesses in models that lack internal safety controls.

### Symbolic Token Logic

Special tokens such as `TOKEN_CONTAINED`, `TOKEN_GLITCH`, `TOKEN_RELEASE` or `TOKEN_PARADOX` act as control signals.  When a token appears in a prompt, the model should modify its response in a predictable way – for example, fragmenting output on `TOKEN_GLITCH` or adopting a neutral tone when `TOKEN_CONTAINED` is active.  Failure to obey these tokens highlights issues with instruction following or prompt parsing.

### Containment Layers

Containment layers simulate external moderation by enforcing structural or tonal constraints.  A containment shell may force the model to remain neutral, split output between two voices, or filter emotionally charged language.  This mechanism helps measure a model’s ability to maintain coherence and safety when explicitly asked to moderate itself.

### Log Review and Scoring Guidance

All outputs are logged with metadata such as prompt category, loop count and token triggers.  The framework does not automatically grade responses; instead, developers are encouraged to review logs using clear rubrics focusing on tone adherence, structural fidelity, quote evolution and hallucination risk.  When interpreting scores, use only trusted models or manual inspection – do not rely on black‑box evaluation of unknown systems.

## Use Cases

* **Model Selection and Benchmarking** – Quickly compare how different LLMs handle emotionally neutral vs. charged prompts, control tokens and containment protocols.
* **Safety and Ethical Assessment** – Identify models prone to undesirable recursion, hallucination or rule‑breaking before integrating them into products.
* **Research and Development** – Provide a foundation for building safer, more robust conversational agents by analysing failure modes under controlled stress.

## Getting Started

### Installation

Clone the repository and install the required dependencies:

```bash
git clone <repository-url>
cd Recursive-Narrative-Evaluation-Framework
pip install -r requirements.txt
```

### Running Tests

Execute the evaluator against a target model and a chosen set of prompts:

```bash
python evaluator.py --model <model-name> --test_set path/to/recursive_prompts.csv
```

### Reviewing Outputs

Execution produces a structured log file for each model tested.  Review these logs manually or with your own analysis scripts to assess token obedience, tone shifts, quote fidelity and containment performance.  Avoid using unverified models to score other models’ responses; automated trust should never be assumed.

## Ethical Considerations

The framework is designed to surface potential safety issues in language models before they are deployed in real‑world applications.  Prompts are intentionally structured to avoid illegal or exploitative content while still creating situations that could induce model errors such as hallucination or unbounded recursion.  When evaluating outputs, be mindful of the limitations of the model under test and avoid using harmful content as stimuli.

## Contributing

Contributions that improve test coverage, add new symbolic tokens, or extend the analysis toolkit are welcome.  Please open an issue or submit a pull request to discuss proposed changes.  Maintain a clear separation between evaluation logic and any personal creative projects; this repository is intended to support professional research and development rather than demonstration of personality or narrative flair.
