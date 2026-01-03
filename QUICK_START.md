# Quick Start

## Option 1: Read the Papers

Follow the 2-week learning path in [README.md](README.md):
- **Week 1**: Foundations (Transformers, Scaling, Alignment)
- **Week 2**: Frontier (Reasoning, Agents, State of the Art)

## Option 2: Start with Plain English

If papers feel dense, start with the explanations:

```
explanations/
├── zero-to-frontier.md    # Complete AI journey explained simply
└── ai-coding-agents.md    # SWE-Bench & coding agents explained
```

## Option 3: Launch the Interactive Viewer

```bash
# Install dependencies
pip install -r requirements.txt

# Start the web server
python web_server.py

# Open http://localhost:8080
```

Browse 37 pre-analyzed papers with 5 perspectives each:
- Precision Analysis
- Educational Breakdown
- Developer Perspective
- Strategic Analysis
- Pseudocode

## Option 4: Re-analyze with Your Own API

```bash
# Configure API
export OPENAI_API_KEY="sk-..."
# or
export ANTHROPIC_API_KEY="..."

# Run analysis
python paper_processor.py
```

---

## What's in This Repo

| Folder/File | What It Contains |
|-------------|------------------|
| `paper_analysis/` | 37 papers, 5 analyses each (185 files) |
| `explanations/` | Plain English guides |
| `web_server.py` | Interactive viewer server |
| `viewer.html` | Web interface |
| `paper_processor.py` | Analysis pipeline |

---

**Start here**: Read `explanations/zero-to-frontier.md`, then follow the 2-week path.
