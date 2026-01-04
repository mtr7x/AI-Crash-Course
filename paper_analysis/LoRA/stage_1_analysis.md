# LoRA: Precision Analysis

> Key insights, surprising findings, and quotable moments

**TL;DR:** LoRA proposes a novel parameter-efficient way to adapt large pre-trained language models to downstream tasks by injecting trainable low-rank matrices into each Transformer layer. This challenges the conventional full fine-tuning approach.

---

- LoRA proposes a novel parameter-efficient way to adapt large pre-trained language models to downstream tasks by injecting trainable low-rank matrices into each Transformer layer. This challenges the conventional full fine-tuning approach.

- LoRA achieves comparable or better performance than full fine-tuning across multiple large models (RoBERTa, DeBERTa, GPT-2, GPT-3) while using 10,000x fewer trainable parameters and requiring 3x less GPU memory during training.

- The efficacy of LoRA suggests that language model adaptation exhibits a high degree of rank-deficiency, meaning the update to the original pre-trained weights can be compressed into low-rank matrices.

- LoRA enables efficient deployment of large adapted models by avoiding storing full fine-tuned copies, which has major cost and scalability implications.

- LoRA maintains the same inference speed as the base pre-trained model, unlike adapter methods which incur inference latency.


### Surprising/Shocking Elements


- The drastic 10,000x reduction in trainable parameters compared to full fine-tuning while maintaining performance is very surprising and contradicts expectations.

- The finding that large pre-trained models can be efficiently adapted by just injecting low-rank updates challenges the notion that fine-tuning all parameters is necessary.

- The stark contrast between LoRA's minimal parameter overhead and adapter methods which add many parameters is unexpected.


### Notable Quotes


"Compared to GPT-3 175B fine-tuned with Adam, LoRA can reduce the number of trainable parameters by 10,000 times and the GPU memory requirement by 3 times."

"LoRA performs on-par or better than fine-tuning in model quality on RoBERTa, DeBERTa, GPT-2, and GPT-3, despite having fewer trainable parameters, a higher training throughput, and, unlike adapters, no additional inference latency."

"We also provide an empirical investigation into rank-deficiency in language model adaptation, which sheds light on the efficacy of LoRA."
---

### Other Perspectives

**Precision Analysis** · [Karpathy-Style Analysis](stage_2_analysis.md) · [Builder's Perspective](stage_3_analysis.md) · [Strategic Analysis](stage_4_analysis.md) · [Pseudocode](pseudocode.md)

---

[← Back to LoRA](.) · [Original Paper](https://arxiv.org/abs/2106.09685) · [All Papers](../)
