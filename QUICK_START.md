# Quick Start

**AI Crash Course, Decoded** — 37 papers, 5 perspectives, plain English.

---

## Option 1: Plain English First

Start here if papers feel intimidating:

| Guide | What It Covers |
|-------|----------------|
| [From Neural Nets to Frontier Models](explanations/zero-to-frontier.md) | Transformers → GPT → RLHF → Reasoning |
| [AI Coding Agents](explanations/ai-coding-agents.md) | SWE-Bench, SWE-Agent, future of AI coding |

---

## Option 2: Follow the 2-Week Path

See [README.md](README.md) for the structured curriculum:
- **Week 1**: Foundations (Transformers, Scaling, Alignment)
- **Week 2**: Frontier (Reasoning, Agents, State of the Art)

---

## Option 3: Interactive Viewer

```bash
pip install -r requirements.txt
python web_server.py
# Open http://localhost:8080
```

Browse 37 papers with 5 analysis perspectives each.

---

## Option 4: Re-analyze with Your API

```bash
export OPENAI_API_KEY="sk-..."
python paper_processor.py
```

---

## What's Here

| Folder | Contents |
|--------|----------|
| `explanations/` | Plain English guides |
| `paper_analysis/` | 37 papers × 5 analyses |
| `web_server.py` | Interactive viewer |
