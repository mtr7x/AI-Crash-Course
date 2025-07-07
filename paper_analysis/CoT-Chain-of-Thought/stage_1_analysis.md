Based on the paper, here are the key insights, surprising elements, and notable quotes I've extracted:

Key Insights:

1. Chain-of-thought prompting, where language models are prompted with examples containing a series of intermediate reasoning steps, significantly improves their ability to perform complex reasoning tasks like arithmetic, commonsense reasoning, and symbolic reasoning.

2. This method enables large language models to learn reasoning abilities from just a few examples, without requiring extensive task-specific training data or fine-tuning.

3. On the GSM8K math word problem benchmark, PaLM 540B with chain-of-thought prompting achieves new state-of-the-art performance, surpassing even fine-tuned GPT-3 with a verifier.

4. Generating rationale-like chains of thought allows models to decompose multi-step problems and allocate more computation to harder problems requiring more reasoning steps.

5. The chains of thought provide an interpretable window into the model's reasoning process, facilitating debugging and trust.

Surprising Elements:

1. The striking performance gains from chain-of-thought prompting, with PaLM 540B outperforming standard prompting by a large margin on GSM8K (contrasting with poor few-shot prompting for reasoning in prior work).

2. The ability of large language models to learn complex reasoning abilities from just a few chain-of-thought examples, without extensive task-specific training.

3. The high performance achieved on challenging benchmarks like GSM8K via prompting, surpassing even heavily fine-tuned models.

Notable Quotes:

1. "We show how such reasoning abilities emerge naturally in sufficiently large language models via a simple method called chain-of-thought prompting, where a few chain of thought demonstrations are provided as exemplars in prompting."

2. "Experiments on three large language models show that chain-of-thought prompting improves performance on a range of arithmetic, commonsense, and symbolic reasoning tasks. The empirical gains can be striking."

3. "For instance, prompting a PaLM 540B with just eight chain-of-thought exemplars achieves state-of-the-art accuracy on the GSM8K benchmark of math word problems, surpassing even finetuned GPT-3 with a verifier."

4. "Chain-of-thought prompting has several attractive properties as an approach for facilitating reasoning in language models...a chain of thought provides an interpretable window into the behavior of the model, suggesting how it might have arrived at a particular answer and providing opportunities to debug where the reasoning path went wrong."