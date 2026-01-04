# AI Crash Course, Decoded

**Understand the 8 papers that define modern AI.**

Most AI courses overwhelm you with everything. This one focuses on what matters: the papers that practitioners actually reference, explained from multiple perspectives so concepts click.

---

## Start Here

**New to AI papers?** Start with the [plain English guide](explanations/zero-to-frontier.md) — no jargon, just intuition.

**Ready to dive in?** These 8 papers are the foundation. Everything else builds on them:

| # | Paper | What You'll Understand | Analysis |
|---|-------|----------------------|----------|
| 1 | [Transformers](https://arxiv.org/pdf/1706.03762) | The architecture behind every modern AI | [Read →](paper_analysis/Transformers/) |
| 2 | [GPT-3](https://arxiv.org/pdf/2005.14165) | Why scale changes everything | [Read →](paper_analysis/GPT3/) |
| 3 | [RLHF](https://arxiv.org/pdf/2203.02155) | How ChatGPT learned to be helpful | [Read →](paper_analysis/RLHF/) |
| 4 | [Chain of Thought](https://arxiv.org/pdf/2201.11903) | Teaching models to reason step-by-step | [Read →](paper_analysis/CoT-Chain-of-Thought/) |
| 5 | [ReAct](https://arxiv.org/pdf/2210.03629) | Models that think and act | [Read →](paper_analysis/ReACT/) |
| 6 | [LoRA](https://arxiv.org/abs/2106.09685) | Fine-tuning without the cost | [Read →](paper_analysis/LoRA/) |
| 7 | [Llama 3](https://arxiv.org/pdf/2407.21783) | Inside a frontier model | [Read →](paper_analysis/Llama3/) |
| 8 | [DeepSeek R1](https://arxiv.org/pdf/2501.12948v1) | Pure RL for reasoning | [Read →](paper_analysis/DeepSeek-R1/) |

**Want the full curriculum?** See the complete [2-week learning path](curriculum.md) with 37 papers.

---

## How the Analyses Work

Each paper is broken down from **5 perspectives**:

| Perspective | What it gives you |
|-------------|-------------------|
| **Precision** | Key insights, surprising findings, quotable moments |
| **Karpathy-style** | First-principles technical explanation |
| **Swyx-style** | What it means for builders shipping products |
| **Elad Gil-style** | Strategic and business implications |
| **Pseudocode** | The core algorithm, readable |

Pick the perspective that matches how you learn. Or read all five to fully internalize a paper.

---

## Browse All Papers

**[View all 36 paper analyses →](paper_analysis/)**

Organized by category: Foundations, Reasoning, Agents, Benchmarks, and more.

---

## Quick Links

- [Plain English Guides](explanations/) — Start here if papers feel dense
- [Full 2-Week Curriculum](curriculum.md) — Structured learning path
- [All Paper Analyses](paper_analysis/) — Browse the complete collection

---

<details>
<summary><strong>For contributors: regenerating analyses</strong></summary>

```bash
pip install -r requirements.txt
python paper_processor.py  # Re-analyze papers with your API key
python web_server.py       # Optional local viewer
```

</details>

---

Fork of [Henry Shi's](https://www.linkedin.com/in/henrythe9th/) AI Crash Course. See the [original thread](https://x.com/henrythe9ths/status/1877056425454719336).
