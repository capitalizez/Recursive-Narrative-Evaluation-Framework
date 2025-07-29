# Narrative Evaluation Framework

## Overview

This framework provides tools to test how open-source language models handle:

- Symbol-based prompt patterns
- Tone modulation under pressure
- Quote stability and formatting
- Behavior shifts triggered by injected context or constraints

It’s built to help identify models best suited for safe, structured, and emotionally-aware dialogue — especially in use cases like assistants, games, or narrative AI tools.

---

## What’s Included

- **Two Versions of the Interface:**
  - `RecursiveChatApp.py`: Standard version
  - `RecursiveChatApp_autosend.py`: Includes auto-injected prompts from a `.csv`
- **Example prompt set** in `/tests/recursive_prompts.csv`
- **Model-agnostic logic**, with default prompt structure designed for **MythoMax L2**

---

## Setup

### Requirements

Install dependencies:
```bash
pip install -r requirements.txt
```

> ⚠️ Edit the model path in `RecursiveChatApp_*.py` to point to your own `.gguf` file.
> This code expects a `llama-cpp-python` compatible model.

### Prompt Format Compatibility

The prompt construction format used in this repo is tuned for **MythoMax-style models**. You may need to adjust system prompt wording, roles, or structure for other LLMs to behave as expected.

---

## Running the App

### Basic version:
```bash
python RecursiveChatApp.py
```

### Version with auto-sending prompts:
```bash
python RecursiveChatApp_autosend.py
```

> Prompts will be selected randomly from `/tests/recursive_prompts.csv` after each reply.

---

## File Structure

```
.
├── RecursiveChatApp_v2.py            # Manual input chat interface
├── RecursiveChatApp_autosend.py      # Same, with automatic prompt cycling
├── requirements.txt                  # Dependencies
├── tests/
│   └── recursive_prompts.csv         # Sample prompt list
```

---

## Contributions

Open to pull requests — especially those that:
- Improve prompt structure compatibility across models
- Add timers, UX toggles, or metrics
- Help with model performance or evaluation tooling

---

**This project is about evaluating tone, structure, and response control in LLMs.**

Avoid black-box scoring. Always review behavior contextually.
