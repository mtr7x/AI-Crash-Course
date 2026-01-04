# LLM Survey: Karpathy-Style Analysis

> First-principles technical explanation

**TL;DR:** Large language models (LLMs) represent a major milestone in the pursuit of artificial general intelligence (AGI). At their core, LLMs are massively scaled transformer models trained on vast datasets to predict the next token in a sequence.

---

Large language models (LLMs) represent a major milestone in the pursuit of artificial general intelligence (AGI). At their core, LLMs are massively scaled transformer models trained on vast datasets to predict the next token in a sequence. While conceptually simple, this self-supervised objective allows LLMs to acquire broad knowledge and capabilities that emerge at scale.


### The key factors behind LLMs' remarkable performance are

1) Model scale - With billions of parameters, LLMs can memorize and generalize from vast amounts of data.
2) Data scale - Training on web-crawled datasets of unprecedented size imbues LLMs with broad grounding.
3) Inductive biases - Transformers' attention mechanisms prove remarkably effective for modeling long-range dependencies in language.


### However, simply scaling up language modeling is insufficient for unlocking LLMs' full potential. Several complementary techniques are crucial


In-context learning allows LLMs to rapidly adapt to new tasks from just a few examples at inference time. Prompting LLMs with task descriptions and exemplars provides strong few-shot learning signals.

Instruction tuning optimizes LLMs to follow complex prompts involving reasoning over multiple steps. This bridges scripting and model capabilities for open-ended task-solving.

External knowledge & tools can augment an LLM's capabilities far beyond what is present in its training data. APIs, databases, coding environments and more can be integrated into the model's loop.

While incredibly capable, LLMs still have key limitations. Their knowledge is static, frozen at training time. They lack robust world grounding and common sense. And scaling alone will eventually run into fundamental limits of the deep learning paradigm.

Looking ahead, LLMs are just the beginning. Marrying their broad capabilities with techniques for open-ended learning, knowledge acquisition and reasoning could finally realize long-standing goals of artificial general intelligence. But getting there will require a careful balance of ambition and honesty about the path's challenges.
---

### Other Perspectives

[Precision Analysis](stage_1_analysis.md) · **Karpathy-Style Analysis** · [Builder's Perspective](stage_3_analysis.md) · [Strategic Analysis](stage_4_analysis.md) · [Pseudocode](pseudocode.md)

---

[← Back to LLM Survey](.) · [Original Paper](https://arxiv.org/pdf/2402.06196v2) · [All Papers](../)
