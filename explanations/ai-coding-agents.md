# AI Coding Agents

> How AI learned to fix real GitHub issues, not just write toy functions.

**TL;DR:** SWE-Bench tests whether AI can fix real bugs in real codebases. SWE-Agent is an agent architecture that thinks, searches files, edits code, and verifies fixes. With good scaffolding, models go from 2% to 49% accuracy.

[Back to Home](../README.md) · [Paper Analyses](../paper_analysis/)

---

## The Problem

Here's the thing: we had all these benchmarks for code - HumanEval, MBPP, whatever. They're all basically:

```
"Write a function that reverses a string"
→ Model writes 5 lines
→ We check if it passes tests
→ Done
```

Cool. But that's not what software engineering actually is.

**Real software engineering is:**
- Clone a massive repo you've never seen
- Read a GitHub issue: "Button doesn't work on Safari"
- Figure out which of 10,000 files is relevant
- Understand the existing code
- Make a surgical fix
- Not break anything else

That's *hard*. That's what SWE-Bench tests.

---

## SWE-Bench: The Benchmark

They took **2,294 real GitHub issues** from popular Python repos (Django, Flask, scikit-learn, etc.) with:

1. The issue description (bug report / feature request)
2. The codebase at that point in time
3. The actual human fix (ground truth)
4. Tests that verify the fix works

```
Input:  GitHub issue + entire codebase
Output: A patch that fixes the issue
Eval:   Run the test suite. Did it pass?
```

**Why this is brutal:**

- Average repo has 100K+ lines of code
- Model must *find* the relevant files (needle in haystack)
- Must understand existing architecture
- Must write code that integrates cleanly
- Must not break existing tests

Early models scored like **2-3%**. Humans found these issues genuinely challenging.

---

## SWE-Agent: The Agent

SWE-Agent is the "how do we actually solve this?" part.

It's a **ReAct-style agent** specialized for coding:

```
┌─────────────────────────────────────────┐
│  GitHub Issue: "Fix timezone bug"       │
└─────────────────────────────────────────┘
                    ↓
┌─────────────────────────────────────────┐
│  SWE-Agent                              │
│                                         │
│  Thought: Need to find timezone code    │
│  Action:  find_file("timezone")         │
│  Obs:     Found utils/timezone.py       │
│                                         │
│  Thought: Let me read this file         │
│  Action:  open_file("utils/timezone.py")│
│  Obs:     [file contents]               │
│                                         │
│  Thought: Bug is on line 47, wrong tz   │
│  Action:  edit_file(line=47, ...)       │
│  Obs:     File updated                  │
│                                         │
│  Thought: Let me verify with tests      │
│  Action:  run_tests()                   │
│  Obs:     All tests pass              │
└─────────────────────────────────────────┘
                    ↓
┌─────────────────────────────────────────┐
│  Output: Git patch with the fix         │
└─────────────────────────────────────────┘
```

**Key insight:** They designed a custom **Agent-Computer Interface (ACI)**.

Instead of raw bash, the agent gets clean commands:

| Command | What it does |
|---------|--------------|
| `find_file` | Search for files by name |
| `search_dir` | Grep through directory |
| `open_file` | View file with line numbers |
| `goto` | Jump to specific line |
| `edit` | Make surgical edits |
| `submit` | Submit the patch |

This interface design matters enormously. Raw bash = agent gets lost. Clean ACI = agent stays on track.

---

## OpenHands (formerly OpenDevin)

Same idea, open source, more general:

```
┌──────────────────────────────────┐
│         OpenHands Agent          │
├──────────────────────────────────┤
│  - Browse the web                │
│  - Write/edit code               │
│  - Run terminal commands         │
│  - Interact with any software    │
└──────────────────────────────────┘
```

It's not just code fixing - it's a general-purpose computer-using agent. But SWE-Bench is a key benchmark.

---

## Current Scores (as of late 2024)

| System | SWE-Bench Score |
|--------|-----------------|
| Claude 3.5 Sonnet + agent | ~49% |
| GPT-4 + SWE-Agent | ~18% |
| Raw GPT-4 (no agent) | ~2% |

The gap between "raw model" and "model + good agent scaffolding" is massive. **The scaffolding matters as much as the model.**

---

## Why This Matters

This is the path to AI that actually helps you code:

```
Today:     "Write me a function"     (toy problems)
SWE-Agent: "Fix this bug in Django"  (real work)
Future:    "Build me this feature"   (end-to-end)
```

The agent needs to:
1. **Navigate** - Find relevant code in huge repos
2. **Understand** - Grok existing architecture
3. **Plan** - Figure out what changes to make
4. **Execute** - Write correct, clean code
5. **Verify** - Test that it works

We're getting there. Not perfect yet. But the trajectory is clear.

---

## The Takeaway

SWE-Bench showed us the gap between "can write code snippets" and "can do software engineering."

SWE-Agent showed us that **agents + good interfaces + frontier models** can start closing that gap.

This is why everyone's building coding agents now. It's one of the clearest paths to useful AI.

---

## Key Papers

| Paper | Analysis | Year |
|-------|----------|------|
| [SWE-Bench](https://arxiv.org/pdf/2310.06770) | [5 perspectives](../paper_analysis/SWE-Bench/) | 2023 |
| [SWE-Agent](https://arxiv.org/pdf/2405.15793) | [5 perspectives](../paper_analysis/SWE-Agent/) | 2024 |
| [OpenHands](https://arxiv.org/pdf/2407.16741) | [5 perspectives](../paper_analysis/OpenHands/) | 2024 |
| [ReAct](https://arxiv.org/pdf/2210.03629) | [5 perspectives](../paper_analysis/ReACT/) | 2022 |

---

The future is agents that can navigate real codebases and ship real fixes. We're maybe 1-2 years from this being genuinely useful day-to-day.

---

[Back to Home](../README.md) · [Full Curriculum](../curriculum.md) · [All Paper Analyses](../paper_analysis/)
