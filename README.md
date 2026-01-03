# AI Crash Course, Decoded

**37 papers. 5 perspectives. Plain English.**

Whether you're a developer, researcher, or builder - this guide takes you from foundational concepts to the cutting edge of AI research. Every paper has been analyzed from multiple perspectives to accelerate your understanding.

---

## Learning Path

### Week 1: Foundations

**Day 1-2: Neural Network Intuition**

Start here. Build visual intuition before diving into papers.

| Resource | What You'll Learn |
|----------|-------------------|
| [Neural Network → LLM Series](https://www.youtube.com/watch?v=aircAruvnKk&list=PLZHQObOWTQDNU6R1_67000Dx_ZCJB-3pi) | Visual intuition for how neural nets actually work |
| [3Blue1Brown](https://www.youtube.com/@3blue1brown) | The math behind deep learning, made beautiful |

**Day 3-4: The Transformer**

Everything in modern AI builds on this. Learn it cold.

| Paper | Year | Why It Matters |
|-------|------|----------------|
| [Transformers](https://arxiv.org/pdf/1706.03762) ⭐ | 2017 | The architecture behind GPT, Claude, Gemini - everything |

**Day 5-6: Scaling & Training**

The insight that drove the AI explosion.

| Paper | Year | Why It Matters |
|-------|------|----------------|
| [Scaling Laws](https://arxiv.org/pdf/2001.08361) | 2020 | Why bigger models keep getting better |
| [GPT-3](https://arxiv.org/pdf/2005.14165) ⭐ | 2020 | The paper that proved scaling works |
| [Training Compute-Optimal LLMs](https://arxiv.org/pdf/2203.15556) | 2022 | Chinchilla - how to train efficiently |

**Day 7: Alignment**

Making models helpful, not just capable.

| Paper | Year | Why It Matters |
|-------|------|----------------|
| [RLHF / InstructGPT](https://arxiv.org/pdf/2203.02155) ⭐ | 2022 | How ChatGPT became ChatGPT |
| [DPO](https://arxiv.org/pdf/2305.18290) | 2023 | Simpler alternative to RLHF |

---

### Week 2: The Frontier

**Day 8-9: Reasoning**

Teaching models to think.

| Paper | Year | Why It Matters |
|-------|------|----------------|
| [Chain of Thought](https://arxiv.org/pdf/2201.11903) ⭐ | 2022 | "Let's think step by step" |
| [Tree of Thoughts](https://arxiv.org/pdf/2305.10601) | 2023 | Exploring multiple reasoning paths |
| [Let's Verify Step by Step](https://arxiv.org/pdf/2305.20050) | 2023 | Process beats outcome |
| [DeepSeek R1](https://arxiv.org/pdf/2501.12948v1) ⭐ | 2025 | Pure RL for reasoning - the AlphaZero moment |

**Day 10-11: Agents**

Models that take action.

| Paper | Year | Why It Matters |
|-------|------|----------------|
| [ReAct](https://arxiv.org/pdf/2210.03629) | 2022 | Reasoning + Acting interleaved |
| [Toolformer](https://arxiv.org/pdf/2302.04761) | 2023 | Teaching LLMs to use tools |
| [SWE-Agent](https://arxiv.org/pdf/2405.15793) | 2024 | AI that fixes real GitHub issues |
| [OpenHands](https://arxiv.org/pdf/2407.16741) | 2024 | Open-source coding agent |

**Day 12-13: State of the Art**

What frontier models look like inside.

| Paper | Year | Why It Matters |
|-------|------|----------------|
| [Llama 3](https://arxiv.org/pdf/2407.21783) ⭐ | 2024 | Most transparent look at building a frontier model |
| [Gemini 1.5](https://arxiv.org/pdf/2403.05530) | 2024 | 10M context window, multimodal |
| [DeepSeek V3](https://github.com/deepseek-ai/DeepSeek-V3/blob/main/DeepSeek_V3.pdf) | 2024 | Frontier OSS model at fraction of cost |
| [MoE](https://arxiv.org/pdf/2401.04088) | 2024 | Mixture of Experts architecture |

**Day 14: Benchmarks & Evaluation**

How we measure progress.

| Paper | Year | Why It Matters |
|-------|------|----------------|
| [SWE-Bench](https://arxiv.org/pdf/2310.06770) | 2023 | Real-world software engineering |
| [Chatbot Arena](https://arxiv.org/pdf/2403.04132) | 2024 | Live human preference rankings |
| [ARC-Prize](https://arxiv.org/pdf/2412.04604) | 2024 | Testing general reasoning |

---

## Deep Dives

### Survey Papers

For comprehensive overviews:

| Survey | Year | Coverage |
|--------|------|----------|
| [LLM Survey](https://arxiv.org/pdf/2402.06196v2) | 2024 | Complete landscape of LLMs |
| [Agent Survey](https://arxiv.org/pdf/2308.11432) | 2023 | Autonomous AI agents |
| [Prompt Engineering Survey](https://arxiv.org/pdf/2406.06608) | 2024 | Every prompting technique |

### Planning & Search

The AlphaGo lineage:

| Paper | Year | Why It Matters |
|-------|------|----------------|
| [AlphaZero](https://arxiv.org/pdf/1712.01815) | 2017 | Self-play mastery |
| [MuZero](https://arxiv.org/pdf/1911.08265) ⭐ | 2019 | Learning without knowing the rules |

### Fine-Tuning

Making models your own:

| Paper | Year | Why It Matters |
|-------|------|----------------|
| [LoRA](https://arxiv.org/abs/2106.09685) | 2021 | Efficient fine-tuning |
| [LLM-as-Judge](https://arxiv.org/pdf/2306.05685) | 2023 | AI evaluating AI |

### Beyond Text

| Paper | Year | Why It Matters |
|-------|------|----------------|
| [Vision Transformer](https://arxiv.org/pdf/2010.11929) | 2021 | Transformers for images |
| [Latent Diffusion](https://arxiv.org/pdf/2112.10752) | 2021 | Foundation of Stable Diffusion |

---

## Plain English Explanations

Start here if papers feel intimidating:

| Guide | What It Covers |
|-------|----------------|
| [From Neural Nets to Frontier Models](explanations/zero-to-frontier.md) | Complete journey from basics to DeepSeek R1 |
| [AI Coding Agents](explanations/ai-coding-agents.md) | SWE-Bench, SWE-Agent, and the future of AI coding |

---

## Interactive Paper Analysis

This repo includes a **full analysis system** with 37 papers pre-analyzed.

### Quick Start

```bash
# Install dependencies
pip install -r requirements.txt

# Launch the web viewer
python web_server.py

# Open http://localhost:8080
```

### What You Get

Every paper analyzed from **5 perspectives**:

| Analysis | Focus |
|----------|-------|
| Precision Analysis | Technical deep-dive, key insights |
| Educational Breakdown | First-principles explanation |
| Developer Perspective | Practical implications for builders |
| Strategic Analysis | Business and market implications |
| Pseudocode | Implementation algorithms |

### Project Structure

```
paper_analysis/          # 37 papers, 5 analyses each
├── Transformers/
├── GPT3/
├── DeepSeek-R1/
└── ...

explanations/            # Plain English guides
├── zero-to-frontier.md
└── ai-coding-agents.md

web_server.py           # Interactive viewer
viewer.html             # Web interface
paper_processor.py      # Analysis pipeline
```

---

## Additional Resources

### Video Lectures

| Resource | Best For |
|----------|----------|
| [Andrej Karpathy: Zero to Hero](https://www.youtube.com/playlist?list=PLAqhIrjkxbuWI23v9cThsA9GvCAUhRvKZ) | Building intuition through code |
| [Yannic Kilcher](https://www.youtube.com/@YannicKilcher) | Paper walkthroughs |
| [Stanford: Building LLMs](https://www.youtube.com/watch?v=9vM4p9NN0Ts) | Academic depth |
| [Noam Brown on Planning](https://www.youtube.com/watch?v=eaAonE58sLU) | o1 founder on AI planning |

### Books & Courses

| Resource | Best For |
|----------|----------|
| [Build an LLM from Scratch](https://www.amazon.com/Build-Large-Language-Model-Scratch/dp/1633437167) | Hands-on understanding |
| [Full Stack Deep Learning](https://fullstackdeeplearning.com/) | Production AI systems |
| [Prompting Guide](https://www.promptingguide.ai/) | Prompting techniques |

### Staying Current

| Resource | What It Offers |
|----------|----------------|
| [History of Deep Learning](https://github.com/adam-maj/deep-learning) | Timeline of breakthroughs |
| [2025 AI Engineer Reading List](https://www.latent.space/p/2025-papers) | Extended reading |
| [State of Generative Models](https://nrehiew.github.io/blog/2024/) | Current landscape |

---

## How to Use This Guide

1. **Start with plain English** - Read `explanations/` first if papers feel dense
2. **Follow the 2-week path** - Papers are ordered intentionally
3. **Prioritize starred papers (⭐)** - These are load-bearing
4. **Use the web viewer** - Browse all 37 papers with 5 analysis perspectives
5. **Build something** - Understanding comes from implementation

---

## Credits

Fork of [Henry Shi's](https://www.linkedin.com/in/henrythe9th/) original AI Crash Course.

See the [original Twitter thread](https://x.com/henrythe9ths/status/1877056425454719336) for context.

---

**The best way to learn is to build.** Start with the Transformer paper. Implement it. Break things. That's how you develop intuition.
