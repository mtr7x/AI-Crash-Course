# Training Compute-Optimal LLMs: Karpathy-Style Analysis

> First-principles technical explanation

**TL;DR:** Large language models have grown massively in recent years, with dense transformer models now exceeding 500 billion parameters. The motivation is clear - increasing model size has consistently improved performance across many language tasks.

---

Large language models have grown massively in recent years, with dense transformer models now exceeding 500 billion parameters. The motivation is clear - increasing model size has consistently improved performance across many language tasks. However, training these enormous models requires staggering compute resources. 

Given a fixed compute budget, determined by factors like available hardware and training time, a key question arises: How should we optimally allocate that budget between model size and number of training tokens? Scaling only model size while keeping token count fixed, as recent models have done, may be sub-optimal.

To investigate this, we trained over 400 language models ranging from 70M to 16B parameters on 5B to 400B tokens. Modeling the pre-training loss as a function of model size and token count, we found that the optimal allocation scales model size and token count equally for a fixed compute budget. In other words, if you double the model size, you should also double the number of training tokens.

This contrasts with previous recommendations to prioritize scaling model size over token count. It also contradicts the approach taken by recent large models like GPT-3 and Gopher, which were undertrained relative to their size given the compute used.

To validate our findings, we trained a 70B parameter "Chinchilla" model on 1.4 trillion tokens - 4x more than GPT-3/Gopher - using the same compute budget as the 280B Gopher. Despite being 4x smaller, Chinchilla outperformed Gopher and other larger models across a wide range of tasks.

The implications are significant. By better allocating compute between size and tokens, we can train more performant yet substantially smaller models. This reduces inference costs and energy usage, facilitating broader downstream applications.

Ultimately, we need to think about language model training in a holistic, systems-minded way. Focusing just on scaling model size while undertrained is sub-optimal. By taking a balanced, first-principles approach, we can more efficiently utilize compute to push forward capabilities.
---

### Other Perspectives

[Precision Analysis](stage_1_analysis.md) · **Karpathy-Style Analysis** · [Builder's Perspective](stage_3_analysis.md) · [Strategic Analysis](stage_4_analysis.md) · [Pseudocode](pseudocode.md)

---

[← Back to Training Compute-Optimal LLMs](.) · [Original Paper](https://arxiv.org/pdf/2203.15556) · [All Papers](../)
