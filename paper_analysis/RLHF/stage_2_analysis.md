# RLHF: Karpathy-Style Analysis

> First-principles technical explanation

**TL;DR:** Large language models like GPT-3 are trained on a vast corpus of internet data to predict the next word in a sequence. However, this language modeling objective does not inherently make them good at following a user's explicit instructions or implicit intentions like being truthful, unbiased and ...

---

Large language models like GPT-3 are trained on a vast corpus of internet data to predict the next word in a sequence. However, this language modeling objective does not inherently make them good at following a user's explicit instructions or implicit intentions like being truthful, unbiased and harmless. We want models that are helpful, honest and safe when assisting humans.

The Approach: Fine-tuning with Human Feedback


### We can move towards aligning language models with human intentions by fine-tuning them on human feedback signals


1) Supervised fine-tuning on demonstrations 
- Collect written prompts and human-written ideal outputs 
- Fine-tune GPT-3 to mimic these demonstrations

2) Reward modeling
- Gather human preferences comparing model outputs
- Train a reward model to predict the preferred output

3) Reinforcement Learning 
- Use the reward model as the reward function
- Fine-tune the supervised model via PPO to maximize this reward

We call the resulting models "InstructGPT" - they aim to follow instructions from the training distribution.


### Key Results


- 1.3B InstructGPT outputs are preferred over 175B GPT-3 by humans, despite 100x fewer parameters
- InstructGPT shows improvements in truthfulness on benchmarks like TruthfulQA
- It reduces hallucinations on closed-domain tasks like summarization
- But it still makes simple mistakes and has flaws

While limited to the preferences of the particular labelers, this demonstrates fine-tuning with human feedback as a promising direction for aligning powerful language models with the user's true intent and values.

The technique breaks down the hard problem of specifying human values into an iterative process of providing demonstrations, comparing outputs, and fine-tuning towards the aggregate feedback signal. However, careful thought is needed on whose feedback to incorporate as this shapes what the model optimizes for.

Human in the loop fine-tuning allows us to distill helpful capabilities from large pretrained models, while mitigating misalignment from pretraining. But the resulting systems are still narrow and imperfect - we must keep iterating while maintaining robustness and oversight.
---

### Other Perspectives

[Precision Analysis](stage_1_analysis.md) · **Karpathy-Style Analysis** · [Builder's Perspective](stage_3_analysis.md) · [Strategic Analysis](stage_4_analysis.md) · [Pseudocode](pseudocode.md)

---

[← Back to RLHF](.) · [Original Paper](https://arxiv.org/pdf/2203.02155) · [All Papers](../)
