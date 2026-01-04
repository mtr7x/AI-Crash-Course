# RLHF: Builder's Perspective

> What this means for developers shipping products

**TL;DR:** TL;DR - OpenAI took GPT-3 and fine-tuned it on human feedback to better follow instructions. The resulting 1.3B InstructGPT model outperforms the 175B GPT-3 in evaluations, despite being 100x smaller.

---

TL;DR - OpenAI took GPT-3 and fine-tuned it on human feedback to better follow instructions. The resulting 1.3B InstructGPT model outperforms the 175B GPT-3 in evaluations, despite being 100x smaller.

The Trend 
Bigger models =/= better behaved. GPT-3's internet training leads to hallucinations, bias, and not following intent. This misalignment between training objective and desired behavior limits real-world apps. OpenAI's fix? Fine-tune on human preferences.

How They Did It
1) Collected demos of good behavior on API prompts 
2) Did supervised fine-tuning on demos
3) Got humans to rank model outputs 
4) Trained a reward model on the rankings
5) Used reinforcement learning to optimize the model for that reward signal


### The best 1.3B InstructGPT beats GPT-3 in

- Following instructions better 
- Reduced hallucinations and toxic outputs
- Better truthfulness (2x TruthfulQA)
- Minimal regressions on NLP tasks

Caveats
- Still makes simple mistakes
- Aligns to the values of their labelers, not broader "human values"
- Expensive human data collection

Implications
This is a promising direction to make LLMs safer and more controllable for real-world use. But scaling up human feedback pipelines is challenging. Techniques like InstructGPT could be part of a broader "constitutional AI" approach to baking in instructions.

The bigger picture is this democratizes some of GPT-3's power - a smaller, cheaper, and better-behaved model outperforms the larger one. Barriers to entry just got lower for devs building on LLMs.

So keep an 👁 on ethical LLM deployments, and think about ways to help models follow your intent. LLMs are becoming our co-pilots - we better learn how to give directions! Let's discuss in the comments 👇
---

### Other Perspectives

[Precision Analysis](stage_1_analysis.md) · [Karpathy-Style Analysis](stage_2_analysis.md) · **Builder's Perspective** · [Strategic Analysis](stage_4_analysis.md) · [Pseudocode](pseudocode.md)

---

[← Back to RLHF](.) · [Original Paper](https://arxiv.org/pdf/2203.02155) · [All Papers](../)
