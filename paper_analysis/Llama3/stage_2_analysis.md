# Llama3: Karpathy-Style Analysis

> First-principles technical explanation

**TL;DR:** The Llama 3 herd represents a new set of large language models that aim to advance the state-of-the-art in foundation models. At their core, they are fundamentally dense Transformer architectures pre-trained on massive multilingual text corpora.

---

The Llama 3 herd represents a new set of large language models that aim to advance the state-of-the-art in foundation models. At their core, they are fundamentally dense Transformer architectures pre-trained on massive multilingual text corpora. However, the key innovation lies in the thoughtful decisions made around data, scale, and system design to maximize performance.

On the data front, the team curated over 15T tokens of higher quality multilingual training data compared to 1.8T for Llama 2. Careful filtering, deduplication, and quality assurance pipelines were implemented.

For scale, the flagship 405B parameter model was pre-trained using a staggering 3.8x10^25 FLOPs - nearly 50x more compute than Llama 2. Following scaling laws, this massive scale boosts performance commensurately. Smaller 8B and 70B models were also trained for longer than theoretically optimal to eke out more quality.

From a systems perspective, the team favored relatively simple but scalable algorithms like supervised finetuning and preference optimization over complex reinforcement learning. The dense model also sidesteps potential instabilities with mixture-of-experts.

The result is a family of models - 8B, 70B, and 405B in size - that achieve state-of-the-art performance across benchmarks like MMLU, coding, reasoning, and tool use tasks. Human evaluations suggest the 405B flagship model is competitive with models like GPT-4 while offering a better safety profile than previous Llamas.

Notably, the team has also extended Llama 3 to multimodal domains like vision and speech through a compositional approach. Initial results are promising but models are still in development.

Overall, Llama 3 showcases the potential of very large language models realized through careful data curation, massive scale, and pragmatic system design choices. The open release offers opportunities for further research while responsibly pushing the boundaries of what's possible.
---

### Other Perspectives

[Precision Analysis](stage_1_analysis.md) · **Karpathy-Style Analysis** · [Builder's Perspective](stage_3_analysis.md) · [Strategic Analysis](stage_4_analysis.md) · [Pseudocode](pseudocode.md)

---

[← Back to Llama3](.) · [Original Paper](https://arxiv.org/pdf/2407.21783) · [All Papers](../)
