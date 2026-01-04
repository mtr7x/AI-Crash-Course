# DeepSeek R1: Builder's Perspective

> What this means for developers shipping products

**TL;DR:** Developers, listen up! DeepSeek has dropped a bombshell with DeepSeek-R1, their first reasoning model trained via pure reinforcement learning (RL).

---

Developers, listen up! DeepSeek has dropped a bombshell with DeepSeek-R1, their first reasoning model trained via pure reinforcement learning (RL). This is a milestone for the community exploring LLM reasoning capabilities without relying on supervised fine-tuning.

The origin story is wild - DeepSeek-R1-Zero, the zero-shot RL model, naturally emerged with mind-blowing behaviors like self-verification, reflection and generating long chains-of-thought. It crushed reasoning benchmarks, scoring 71% on AIME 2024 from just 15.6% initially! 

But readability was an issue, so they leveled up with DeepSeek-R1. A cold start with curated data, multi-stage RL training with rejection sampling - this model is an RL juggernaut, matching OpenAI's best on reasoning tasks.

The real power move? Distilling DeepSeek-R1 to smaller dense models like 14B, 32B and even 70B parameter count. Their 14B model blows away previous 32B state-of-the-art, proving the reasoning patterns from the teacher are priceless. 💎

For devs craving reasoning AI, these open-source models are a gamechanger. RL has unlocked a new frontier, incentivizing capabilities we could only dream of before. The takeaway? Strap in and watch the reasoning revolution unfold! 

The path ahead has challenges, but with this community's ingenuity, the possibilities are limitless. Let's dive in, discuss the implications, and push the boundaries of what AI can reason!
---

### Other Perspectives

[Precision Analysis](stage_1_analysis.md) · [Karpathy-Style Analysis](stage_2_analysis.md) · **Builder's Perspective** · [Strategic Analysis](stage_4_analysis.md) · [Pseudocode](pseudocode.md)

---

[← Back to DeepSeek R1](.) · [Original Paper](https://arxiv.org/pdf/2501.12948v1) · [All Papers](../)
