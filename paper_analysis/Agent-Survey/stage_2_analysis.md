# Agent Survey: Karpathy-Style Analysis

> First-principles technical explanation

**TL;DR:** Large language models (LLMs) have shown remarkable potential for achieving human-level intelligence by learning from vast datasets. This has sparked growing research interest in using LLMs as the core component to build autonomous agents that can make human-like decisions.

---

Large language models (LLMs) have shown remarkable potential for achieving human-level intelligence by learning from vast datasets. This has sparked growing research interest in using LLMs as the core component to build autonomous agents that can make human-like decisions.


### At a high level, constructing an LLM-based agent involves two key aspects


1) Designing the agent architecture to effectively leverage the LLM
2) Enabling the agent to acquire necessary capabilities for target tasks


### Let's break these down through a unified conceptual framework


The agent architecture typically consists of an LLM at the core, combined with other components like memory, planners, external tools etc. The LLM provides broad knowledge and language understanding. Memory allows tracking conversation/task state. Planners break down complex goals into subtasks. External tools give access to APIs, sensors etc.

All these components interact in a loop - the LLM comprehends the current state from memory/observations, forms a plan, takes actions by calling tools/APIs or outputting text, and the loop continues based on new state. Different architectural choices explore various ways to compose and orchestrate these pieces.

To acquire capabilities, one approach is prompting - providing instructions that steer the LLM towards target behaviors without updating its parameters. Alternatively, the LLM can be fine-tuned on datasets of task demonstrations. Reinforcement learning can shape behaviors through reward modeling.

While extremely powerful, LLM-based agents have limitations. Factual errors and hallucinations remain an issue inherited from LLM training data. Safety and alignment challenges arise from the black-box nature of large models. Resource constraints limit real-world sensory grounding.

Despite these challenges, LLM-based agents have already shown promise across diverse applications in science, engineering, interactive assistants and more. As this field rapidly evolves, we can expect increasingly capable agents that synergistically combine the strengths of LLMs with other AI components in novel ways.

Rigorously evaluating these agents requires a combination of objective metrics for capability benchmarks as well as subjective human evaluation of factors like coherence, safety, and user experience. Overall, this area crystallizes some of the most exciting directions towards artificial general intelligence.
---

### Other Perspectives

[Precision Analysis](stage_1_analysis.md) · **Karpathy-Style Analysis** · [Builder's Perspective](stage_3_analysis.md) · [Strategic Analysis](stage_4_analysis.md) · [Pseudocode](pseudocode.md)

---

[← Back to Agent Survey](.) · [Original Paper](https://arxiv.org/pdf/2308.11432) · [All Papers](../)
