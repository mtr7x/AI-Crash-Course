# CoT (Chain of Thought): Karpathy-Style Analysis

> First-principles technical explanation

**TL;DR:** This paper explores an elegant and surprisingly effective technique to unlock the reasoning capabilities of large language models like PaLM. The core idea is simple yet powerful - provide the model with a few examples that demonstrate a chain of thought, which is essentially a series of intermedi...

---

This paper explores an elegant and surprisingly effective technique to unlock the reasoning capabilities of large language models like PaLM. The core idea is simple yet powerful - provide the model with a few examples that demonstrate a chain of thought, which is essentially a series of intermediate natural language steps that lead to the final answer. 

Let's break this down step-by-step. Large language models are trained on vast datasets and learn complex statistical patterns. However, directly prompting them to solve multi-step reasoning tasks often fails - the model doesn't know how to systematically break down the problem. The key insight is that by showing examples where the reasoning process is laid out explicitly, the model can learn to emulate this chain-of-thought approach.

The implementation is strikingly straightforward - just construct prompts containing input/chain-of-thought/output triples as exemplars. No complex fine-tuning pipelines or external systems required. The model figuring out how to do structured multi-step reasoning from just a handful of examples is quite remarkable and highlights the power of large models combined with prompting.

The empirical results are compelling. On the challenging GSM8K math word problem benchmark, PaLM 540B with chain-of-thought prompting hits a new state-of-the-art, outperforming even GPT-3 that was explicitly fine-tuned for this task! Gains are observed across arithmetic, commonsense, and symbolic reasoning benchmarks.

Of course, there are open questions and limitations. We don't fully understand why and how this approach works so well for such large models. Generating coherent multi-step reasoning chains can still fail for extremely difficult problems. But overall, chain-of-thought prompting is a conceptually clean, easy-to-implement, and surprisingly powerful technique.

It exemplifies the core strengths of large language models - the ability to rapidly acquire new skills from just a few examples, while combining and composing that knowledge in systematic ways. By providing the right prompting cues, we can unlock remarkable reasoning capabilities that were latent in these models all along. This promotes an interface where language models don't just regurgitate knowledge, but act as flexible reasoning engines following the chains of thought we demonstrate.
---

### Other Perspectives

[Precision Analysis](stage_1_analysis.md) · **Karpathy-Style Analysis** · [Builder's Perspective](stage_3_analysis.md) · [Strategic Analysis](stage_4_analysis.md) · [Pseudocode](pseudocode.md)

---

[← Back to CoT (Chain of Thought)](.) · [Original Paper](https://arxiv.org/pdf/2201.11903) · [All Papers](../)
