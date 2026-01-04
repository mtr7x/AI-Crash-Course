# Prompt Engineering Survey: Karpathy-Style Analysis

> First-principles technical explanation

**TL;DR:** Prompting allows us to interact with large language models (LLMs) by providing an input "prompt" to which the model generates an output response. Effective prompting is critical for getting good results from LLMs across a wide range of tasks.

---

Prompting allows us to interact with large language models (LLMs) by providing an input "prompt" to which the model generates an output response. Effective prompting is critical for getting good results from LLMs across a wide range of tasks. 

At its core, a prompt is simply a sequence of tokens (words) fed into the LLM before generation begins. By carefully crafting this input sequence, we can steer the model's predictions in desired directions. This process of designing good prompts is referred to as "prompt engineering."


### There are many prompting techniques that can improve performance on different tasks. Some key ones


- In-context learning: Provide example input-output pairs in the prompt to demonstrate the task.
- Chain-of-thought prompting: Instruct the model to show its step-by-step reasoning process.
- Decomposition: Break a complex task into subtasks with separate prompts.

However, prompting is a relatively new field with inconsistent terminology and little established theory. We lack a unified framework for understanding what makes an effective prompt across domains. Prompts can be brittle and models can exhibit issues like overconfidence, bias, and insensitivity to small prompt changes.

While prompting unlocks new capabilities, we must approach it with clear eyes - understanding both the potential and current limitations. Sustained research is needed to develop principled prompt engineering methods and benchmarks for rigorously evaluating prompting approaches.

Ultimately, prompting provides a powerful interface for leveraging large language models in practice. But realizing its full potential will require thinking from first principles about what we're actually doing when we prompt these models.
---

### Other Perspectives

[Precision Analysis](stage_1_analysis.md) · **Karpathy-Style Analysis** · [Builder's Perspective](stage_3_analysis.md) · [Strategic Analysis](stage_4_analysis.md) · [Pseudocode](pseudocode.md)

---

[← Back to Prompt Engineering Survey](.) · [Original Paper](https://arxiv.org/pdf/2406.06608) · [All Papers](../)
