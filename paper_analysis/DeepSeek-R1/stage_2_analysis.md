# DeepSeek R1: Karpathy-Style Analysis

> First-principles technical explanation

**TL;DR:** This work tackles the challenge of enhancing reasoning capabilities in large language models through reinforcement learning (RL). The key ideas are

---

### This work tackles the challenge of enhancing reasoning capabilities in large language models through reinforcement learning (RL). The key ideas are


- DeepSeek-R1-Zero: Applying pure RL without any supervised fine-tuning on a powerful base model (DeepSeek-V3-Base). This allowed the model to naturally discover powerful reasoning behaviors like self-verification, reflection, and generating long chains-of-thought. Remarkably, it achieved super-human performance on many reasoning benchmarks, validating that RL alone can incentivize strong reasoning skills.

- DeepSeek-R1: Building on R1-Zero by incorporating:
   - A cold-start phase using a small supervised dataset to provide a better starting point
   - Reasoning-oriented RL similar to R1-Zero 
   - Rejection sampling to collect new supervised examples leveraging the partially-trained model
   - Additional supervised fine-tuning on the aggregated data
   - Final RL stage incorporating prompts from all scenarios

This multi-stage process allowed DeepSeek-R1 to match the reasoning performance of OpenAI's flagship o1-1217 model while improving readability.

- Distillation: Demonstrating that the reasoning patterns discovered by large models like DeepSeek-R1 can be effectively distilled into smaller dense models like 14B-70B parameters, setting new state-of-the-art for open reasoning benchmarks.


### The key takeaways are

- RL alone can incentivize strong reasoning emergence without supervised examples 
- A curriculum combining RL and supervised phases unlocks further reasoning gains
- Distillation transfers the acquired reasoning skills to smaller, more efficient models

This systematic study provides insights into developing reasoning capabilities via different training paradigms, benchmarking progress, and highlights the potential of RL as a path towards more capable and general AI systems.
---

### Other Perspectives

[Precision Analysis](stage_1_analysis.md) · **Karpathy-Style Analysis** · [Builder's Perspective](stage_3_analysis.md) · [Strategic Analysis](stage_4_analysis.md) · [Pseudocode](pseudocode.md)

---

[← Back to DeepSeek R1](.) · [Original Paper](https://arxiv.org/pdf/2501.12948v1) · [All Papers](../)
