# 2-Week AI Paper Curriculum

A structured path through 37 papers that matter. Each paper links to both the original PDF and our multi-perspective analysis.

[← Back to Home](README.md)

---

## Week 1: Foundations

### Day 1-2: Build Intuition

Before papers, build visual intuition:

| Resource | What You'll Learn |
|----------|-------------------|
| [3Blue1Brown Neural Networks](https://www.youtube.com/watch?v=aircAruvnKk&list=PLZHQObOWTQDNU6R1_67000Dx_ZCJB-3pi) | How neural nets actually work |
| [Andrej Karpathy: Zero to Hero](https://www.youtube.com/playlist?list=PLAqhIrjkxbuWI23v9cThsA9GvCAUhRvKZ) | Build intuition through code |

### Day 3-4: The Transformer

Everything builds on this.

| Paper | Analysis | Why It Matters |
|-------|----------|----------------|
| [Transformers](https://arxiv.org/pdf/1706.03762) ⭐ | [Read →](paper_analysis/Transformers/) | The architecture behind GPT, Claude, Gemini |

### Day 5-6: Scaling

The insight that drove the AI explosion.

| Paper | Analysis | Why It Matters |
|-------|----------|----------------|
| [Scaling Laws](https://arxiv.org/pdf/2001.08361) | [Read →](paper_analysis/Scaling-Laws/) | Why bigger models keep getting better |
| [GPT-3](https://arxiv.org/pdf/2005.14165) ⭐ | [Read →](paper_analysis/GPT3/) | The paper that proved scaling works |
| [Training Compute-Optimal LLMs](https://arxiv.org/pdf/2203.15556) | [Read →](paper_analysis/Training-Compute-Optimal-LLMs/) | Chinchilla - training efficiently |

### Day 7: Alignment

Making models helpful, not just capable.

| Paper | Analysis | Why It Matters |
|-------|----------|----------------|
| [RLHF](https://arxiv.org/pdf/2203.02155) ⭐ | [Read →](paper_analysis/RLHF/) | How ChatGPT became ChatGPT |
| [DPO](https://arxiv.org/pdf/2305.18290) | [Read →](paper_analysis/DPO/) | Simpler alternative to RLHF |

---

## Week 2: The Frontier

### Day 8-9: Reasoning

Teaching models to think.

| Paper | Analysis | Why It Matters |
|-------|----------|----------------|
| [Chain of Thought](https://arxiv.org/pdf/2201.11903) ⭐ | [Read →](paper_analysis/CoT-Chain-of-Thought/) | "Let's think step by step" |
| [Tree of Thoughts](https://arxiv.org/pdf/2305.10601) | [Read →](paper_analysis/ToT-Tree-of-Thoughts/) | Exploring multiple reasoning paths |
| [Graph of Thoughts](https://arxiv.org/pdf/2308.09687) | [Read →](paper_analysis/GoT-Graph-of-Thoughts/) | Network-based reasoning |
| [Meta-CoT](https://arxiv.org/pdf/2304.04487) | [Read →](paper_analysis/Meta-CoT/) | Meta-learning for chain of thought |
| [Self-Refine](https://arxiv.org/pdf/2303.17651) | [Read →](paper_analysis/SELF-REFINE-Iterative-Refinement-with-Self-Feedback/) | Iterative self-improvement |
| [Let's Verify Step by Step](https://arxiv.org/pdf/2305.20050) | [Read →](paper_analysis/Lets-Verify-Step-by-Step/) | Process beats outcome |
| [DeepSeek R1](https://arxiv.org/pdf/2501.12948v1) ⭐ | [Read →](paper_analysis/DeepSeek-R1/) | Pure RL for reasoning |

### Day 10-11: Agents

Models that take action.

| Paper | Analysis | Why It Matters |
|-------|----------|----------------|
| [ReAct](https://arxiv.org/pdf/2210.03629) | [Read →](paper_analysis/ReACT/) | Reasoning + Acting interleaved |
| [Toolformer](https://arxiv.org/pdf/2302.04761) | [Read →](paper_analysis/Toolformer/) | Teaching LLMs to use tools |
| [SWE-Agent](https://arxiv.org/pdf/2405.15793) | [Read →](paper_analysis/SWE-Agent/) | AI that fixes real GitHub issues |
| [OpenHands](https://arxiv.org/pdf/2407.16741) | [Read →](paper_analysis/OpenHands/) | Open-source coding agent |

### Day 12-13: State of the Art

Inside frontier models.

| Paper | Analysis | Why It Matters |
|-------|----------|----------------|
| [GPT-4](https://arxiv.org/pdf/2303.08774) | [Read →](paper_analysis/GPT4/) | OpenAI's multimodal flagship |
| [Llama 3](https://arxiv.org/pdf/2407.21783) ⭐ | [Read →](paper_analysis/Llama3/) | Most transparent frontier model |
| [Gemini 1.5](https://arxiv.org/pdf/2403.05530) | [Read →](paper_analysis/Gemini15/) | 10M context, multimodal |
| [MoE](https://arxiv.org/pdf/2401.04088) | [Read →](paper_analysis/MoE/) | Mixture of Experts architecture |

### Day 14: Benchmarks

How we measure progress.

| Paper | Analysis | Why It Matters |
|-------|----------|----------------|
| [BIG-Bench](https://arxiv.org/pdf/2206.04615) | [Read →](paper_analysis/BIG-Bench/) | 200+ diverse capability tasks |
| [SWE-Bench](https://arxiv.org/pdf/2310.06770) | [Read →](paper_analysis/SWE-Bench/) | Real-world software engineering |
| [Chatbot Arena](https://arxiv.org/pdf/2403.04132) | [Read →](paper_analysis/Chatbot-Arena/) | Live human preference rankings |
| [ARC-Prize](https://arxiv.org/pdf/2412.04604) | [Read →](paper_analysis/ARC-Prize/) | Testing general reasoning |

---

## Deep Dives

### Survey Papers

| Survey | Analysis | Coverage |
|--------|----------|----------|
| [Foundations of LLMs](https://arxiv.org/pdf/2501.09223) | [Read →](paper_analysis/Foundations-of-LLMs/) | Comprehensive theoretical foundations |
| [LLM Survey](https://arxiv.org/pdf/2402.06196v2) | [Read →](paper_analysis/LLM-Survey/) | Complete landscape of LLMs |
| [Agent Survey](https://arxiv.org/pdf/2308.11432) | [Read →](paper_analysis/Agent-Survey/) | Autonomous AI agents |
| [Prompt Engineering Survey](https://arxiv.org/pdf/2406.06608) | [Read →](paper_analysis/Prompt-Engineering-Survey/) | Every prompting technique |

### Planning & Search

| Paper | Analysis | Why It Matters |
|-------|----------|----------------|
| [AlphaZero](https://arxiv.org/pdf/1712.01815) | [Read →](paper_analysis/AlphaZero/) | Self-play mastery |
| [MuZero](https://arxiv.org/pdf/1911.08265) ⭐ | [Read →](paper_analysis/MuZero/) | Learning without rules |

### Fine-Tuning

| Paper | Analysis | Why It Matters |
|-------|----------|----------------|
| [LoRA](https://arxiv.org/abs/2106.09685) | [Read →](paper_analysis/LoRA/) | Efficient fine-tuning |
| [LLM-as-Judge](https://arxiv.org/pdf/2306.05685) | [Read →](paper_analysis/LLM-as-Judge/) | AI evaluating AI |

### Beyond Text

| Paper | Analysis | Why It Matters |
|-------|----------|----------------|
| [Vision Transformer](https://arxiv.org/pdf/2010.11929) | [Read →](paper_analysis/Vision-Transformer/) | Transformers for images |
| [Latent Diffusion](https://arxiv.org/pdf/2112.10752) | [Read →](paper_analysis/Latent-Diffusion/) | Foundation of Stable Diffusion |

---

## Additional Resources

### Reference

| Resource | Analysis | What It Offers |
|----------|----------|----------------|
| [History of Deep Learning](https://github.com/adam-maj/deep-learning) | [Read →](paper_analysis/History-of-Deep-Learning/) | Timeline of breakthroughs |

### Video Lectures

| Resource | Best For |
|----------|----------|
| [Yannic Kilcher](https://www.youtube.com/@YannicKilcher) | Paper walkthroughs |
| [Stanford: Building LLMs](https://www.youtube.com/watch?v=9vM4p9NN0Ts) | Academic depth |
| [Noam Brown on Planning](https://www.youtube.com/watch?v=eaAonE58sLU) | o1 founder on AI planning |

### Books

| Resource | Best For |
|----------|----------|
| [Build an LLM from Scratch](https://www.amazon.com/Build-Large-Language-Model-Scratch/dp/1633437167) | Hands-on understanding |
| [Full Stack Deep Learning](https://fullstackdeeplearning.com/) | Production AI systems |

---

[← Back to Home](README.md) · [Browse All Papers →](paper_analysis/)
