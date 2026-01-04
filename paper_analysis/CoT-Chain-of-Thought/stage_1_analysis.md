# CoT (Chain of Thought): Precision Analysis

> Key insights, surprising findings, and quotable moments

**TL;DR:** Based on the paper, here are the key insights, surprising elements, and notable quotes I've extracted

---

### Based on the paper, here are the key insights, surprising elements, and notable quotes I've extracted



### Key Insights


- Chain-of-thought prompting, where language models are prompted with examples containing a series of intermediate reasoning steps, significantly improves their ability to perform complex reasoning tasks like arithmetic, commonsense reasoning, and symbolic reasoning.

- This method enables large language models to learn reasoning abilities from just a few examples, without requiring extensive task-specific training data or fine-tuning.

- On the GSM8K math word problem benchmark, PaLM 540B with chain-of-thought prompting achieves new state-of-the-art performance, surpassing even fine-tuned GPT-3 with a verifier.

- Generating rationale-like chains of thought allows models to decompose multi-step problems and allocate more computation to harder problems requiring more reasoning steps.

- The chains of thought provide an interpretable window into the model's reasoning process, facilitating debugging and trust.


### Surprising Elements


- The striking performance gains from chain-of-thought prompting, with PaLM 540B outperforming standard prompting by a large margin on GSM8K (contrasting with poor few-shot prompting for reasoning in prior work).

- The ability of large language models to learn complex reasoning abilities from just a few chain-of-thought examples, without extensive task-specific training.

- The high performance achieved on challenging benchmarks like GSM8K via prompting, surpassing even heavily fine-tuned models.


### Notable Quotes


- "We show how such reasoning abilities emerge naturally in sufficiently large language models via a simple method called chain-of-thought prompting, where a few chain of thought demonstrations are provided as exemplars in prompting."

- "Experiments on three large language models show that chain-of-thought prompting improves performance on a range of arithmetic, commonsense, and symbolic reasoning tasks. The empirical gains can be striking."

- "For instance, prompting a PaLM 540B with just eight chain-of-thought exemplars achieves state-of-the-art accuracy on the GSM8K benchmark of math word problems, surpassing even finetuned GPT-3 with a verifier."

- "Chain-of-thought prompting has several attractive properties as an approach for facilitating reasoning in language models...a chain of thought provides an interpretable window into the behavior of the model, suggesting how it might have arrived at a particular answer and providing opportunities to debug where the reasoning path went wrong."
---

### Other Perspectives

**Precision Analysis** · [Karpathy-Style Analysis](stage_2_analysis.md) · [Builder's Perspective](stage_3_analysis.md) · [Strategic Analysis](stage_4_analysis.md) · [Pseudocode](pseudocode.md)

---

[← Back to CoT (Chain of Thought)](.) · [Original Paper](https://arxiv.org/pdf/2201.11903) · [All Papers](../)
