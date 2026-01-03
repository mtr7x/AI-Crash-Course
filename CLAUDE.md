# CLAUDE.md

This file provides guidance to Claude Code when working with this repository.

## Repository Overview

**AI Crash Course, Decoded** — 37 papers, 5 perspectives, plain English.

A fork of Henry Shi's AI Crash Course, expanded with:
- **37 papers** analyzed from 5 perspectives
- **Plain English guides** for beginners
- **Interactive web viewer** for exploration
- **2-week structured curriculum**

## Repository Structure

```
├── README.md                # Main curriculum (2-week learning path)
├── QUICK_START.md           # Quick start guide
├── explanations/            # Plain English guides
│   ├── zero-to-frontier.md  # Neural nets → frontier models
│   └── ai-coding-agents.md  # SWE-Bench & coding agents
├── paper_analysis/          # 37 papers × 5 analyses each
│   ├── Transformers/
│   ├── GPT3/
│   ├── DeepSeek-R1/
│   └── ...
├── web_server.py            # Interactive viewer server
├── viewer.html              # Web interface
├── paper_processor.py       # Analysis pipeline
└── requirements.txt         # Python dependencies
```

## Key Files

| File | Purpose |
|------|---------|
| `README.md` | 2-week curriculum with paper links |
| `explanations/*.md` | Beginner-friendly guides |
| `paper_analysis/*/stage_1_analysis.md` | Technical deep-dive |
| `paper_analysis/*/stage_2_analysis.md` | Educational breakdown |
| `paper_analysis/*/stage_3_analysis.md` | Developer perspective |
| `paper_analysis/*/stage_4_analysis.md` | Strategic analysis |
| `paper_analysis/*/pseudocode.md` | Implementation algorithms |

## Common Tasks

**Adding new papers:**
1. Add paper link to README.md in appropriate section
2. Run `python paper_processor.py`
3. New analysis appears in `paper_analysis/`

**Adding explanations:**
1. Create new `.md` file in `explanations/`
2. Update README.md to link to it

**Running the viewer:**
```bash
pip install -r requirements.txt
python web_server.py
# Open http://localhost:8080
```

## Writing Style

- Papers use star (⭐) for priority marking
- Explanations use first-principles, conversational tone
- Keep content accessible to builders with varying backgrounds
- Balance technical depth with clarity
