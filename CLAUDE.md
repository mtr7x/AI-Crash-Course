# CLAUDE.md

Guidance for Claude Code when working with this repository.

## Overview

**AI Crash Course, Decoded** — 37 papers, 5 perspectives, plain English.

A GitHub-native learning resource. No installation required to browse.

## Structure

```
README.md                    # Home page - 8 essential papers
curriculum.md                # Full 2-week path - 37 papers

explanations/                # Plain English guides
├── zero-to-frontier.md      # Neural nets to frontier models
└── ai-coding-agents.md      # SWE-Bench and coding agents

paper_analysis/              # 37 papers, 5 analyses each
├── README.md                # Index by category
└── {Paper}/
    ├── README.md            # Landing page - choose perspective
    ├── stage_1_analysis.md  # Precision Analysis
    ├── stage_2_analysis.md  # Karpathy-Style
    ├── stage_3_analysis.md  # Builder's Perspective
    ├── stage_4_analysis.md  # Strategic Analysis
    └── pseudocode.md        # Core algorithm

tools/                       # Scripts (optional, for regeneration)
├── paper_processor.py       # Analyze papers with LLM
├── reimagine_analyses.py    # Reformat analysis files
└── generate_readme.py       # Generate navigation READMEs
```

## Key Files

| File | Purpose |
|------|---------|
| `README.md` | Minimal home - 8 essential papers, clear entry points |
| `curriculum.md` | Full 2-week curriculum with all 37 papers |
| `paper_analysis/README.md` | Index of all papers by category |
| `paper_analysis/{Paper}/README.md` | Landing page with perspective choices |
| `explanations/*.md` | Beginner-friendly plain English guides |

## Analysis Perspectives

Each paper has 5 analyses:

| File | Perspective | Focus |
|------|-------------|-------|
| `stage_1_analysis.md` | Precision | Key insights, quotes |
| `stage_2_analysis.md` | Karpathy-style | First-principles technical |
| `stage_3_analysis.md` | Builder's | Practical implications |
| `stage_4_analysis.md` | Strategic | Business/market view |
| `pseudocode.md` | Pseudocode | Core algorithm |

## Common Tasks

**Adding a new paper:**
1. Add to `curriculum.md` in appropriate section
2. Run `python tools/paper_processor.py` (requires API key)
3. Run `python tools/reimagine_analyses.py` to format

**Updating navigation:**
```bash
python tools/generate_readme.py
python tools/reimagine_analyses.py
```

**Regenerating analyses (optional):**
```bash
pip install -r requirements.txt
export OPENAI_API_KEY=...  # or ANTHROPIC_API_KEY
python tools/paper_processor.py
```

## Writing Style

- No emojis except star for priority papers
- Clean typography, clear hierarchy
- First-principles, conversational tone
- Balance technical depth with accessibility
- Every page has navigation links
