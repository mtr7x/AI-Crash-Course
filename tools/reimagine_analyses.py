#!/usr/bin/env python3
"""
Reimagine the paper analysis reading experience.

Transforms raw analysis text into beautifully structured, navigable documents
following Julie Zhou / Jonathan Ive design principles:
- Clear hierarchy
- Scannable structure
- Consistent navigation
- Every element earns its place
"""

import json
import os
import re
from pathlib import Path

PAPER_ANALYSIS_DIR = Path("paper_analysis")

# Perspective metadata
PERSPECTIVES = {
    "stage_1_analysis.md": {
        "name": "Precision Analysis",
        "tagline": "Key insights, surprising findings, and quotable moments",
        "sections": ["Key Insights", "Surprising Findings", "Notable Quotes"],
    },
    "stage_2_analysis.md": {
        "name": "Karpathy-Style Analysis",
        "tagline": "First-principles technical explanation",
        "sections": ["Core Idea", "How It Works", "Why It Matters", "Technical Details"],
    },
    "stage_3_analysis.md": {
        "name": "Builder's Perspective",
        "tagline": "What this means for developers shipping products",
        "sections": ["The Trend", "Practical Implications", "What to Build", "Watch Out For"],
    },
    "stage_4_analysis.md": {
        "name": "Strategic Analysis",
        "tagline": "Business implications and market dynamics",
        "sections": ["Market Impact", "Strategic Implications", "Investment Thesis", "Key Risks"],
    },
    "pseudocode.md": {
        "name": "Pseudocode",
        "tagline": "The core algorithm, readable",
        "sections": ["Algorithm", "Key Functions", "Implementation Notes"],
    },
}

STAGE_ORDER = [
    "stage_1_analysis.md",
    "stage_2_analysis.md",
    "stage_3_analysis.md",
    "stage_4_analysis.md",
    "pseudocode.md",
]


def get_paper_title(paper_dir: Path) -> tuple[str, str]:
    """Get paper title and URL from metadata."""
    metadata_path = paper_dir / "metadata.json"
    if metadata_path.exists():
        with open(metadata_path) as f:
            data = json.load(f)
            paper = data.get("paper", {})
            title = paper.get("title", paper_dir.name).replace("\\", "").strip()
            url = paper.get("url", "")
            return title, url
    return paper_dir.name, ""


def structure_content(content: str, perspective_info: dict) -> str:
    """
    Add structure to raw analysis content.

    Tries to identify natural sections and add headers.
    """
    lines = content.strip().split("\n")

    # Remove the "Here is a summary in the style of..." opener if present
    if lines and lines[0].lower().startswith("here"):
        # Skip intro lines until we hit actual content
        for i, line in enumerate(lines):
            if line.strip() and not line.lower().startswith("here") and ":" not in line[:50]:
                lines = lines[i:]
                break

    # Check if content already has structure (headers)
    has_headers = any(line.strip().startswith("#") for line in lines)

    if has_headers:
        return "\n".join(lines)

    # Try to identify numbered lists and convert to sections
    structured = []
    current_section = []

    for line in lines:
        # Check for numbered section starters like "1. Key Insights:" or "Key Insights:"
        section_match = re.match(r'^(?:\d+\.\s*)?([A-Z][^:]+):\s*$', line.strip())
        if section_match:
            if current_section:
                structured.extend(current_section)
                structured.append("")
            section_name = section_match.group(1)
            structured.append(f"### {section_name}")
            structured.append("")
            current_section = []
        # Check for numbered items like "1. The Transformer..."
        elif re.match(r'^\d+\.\s+', line.strip()):
            item = re.sub(r'^\d+\.\s+', '- ', line.strip())
            current_section.append(item)
        else:
            current_section.append(line)

    if current_section:
        structured.extend(current_section)

    return "\n".join(structured)


def create_navigation(paper_dir: Path, current_file: str, paper_title: str, paper_url: str) -> str:
    """Create navigation footer for an analysis file."""
    nav_parts = []

    for stage_file in STAGE_ORDER:
        if stage_file == current_file:
            # Current perspective - no link
            nav_parts.append(f"**{PERSPECTIVES[stage_file]['name']}**")
        elif (paper_dir / stage_file).exists():
            nav_parts.append(f"[{PERSPECTIVES[stage_file]['name']}]({stage_file})")

    nav_line = " · ".join(nav_parts)

    footer = f"""
---

### Other Perspectives

{nav_line}

---

[← Back to {paper_title}](.) · [Original Paper]({paper_url}) · [All Papers](../)
"""
    return footer


def extract_tldr(content: str, max_sentences: int = 2) -> str:
    """Extract a TL;DR from the content."""
    # Find first substantive paragraph
    paragraphs = [p.strip() for p in content.split("\n\n") if p.strip() and len(p.strip()) > 50]

    if not paragraphs:
        return ""

    first_para = paragraphs[0]

    # Clean up any markdown artifacts
    first_para = re.sub(r'^#+\s*', '', first_para)
    first_para = re.sub(r'^\*+\s*', '', first_para)
    first_para = re.sub(r'^-\s*', '', first_para)

    # Get first N sentences
    sentences = re.split(r'(?<=[.!?])\s+', first_para)
    tldr = " ".join(sentences[:max_sentences])

    # Ensure it's not too long
    if len(tldr) > 300:
        tldr = tldr[:297] + "..."

    return tldr


def reimagine_analysis(paper_dir: Path, analysis_file: str) -> bool:
    """Reimagine a single analysis file."""
    file_path = paper_dir / analysis_file

    if not file_path.exists():
        return False

    perspective = PERSPECTIVES.get(analysis_file)
    if not perspective:
        return False

    paper_title, paper_url = get_paper_title(paper_dir)

    with open(file_path) as f:
        original_content = f.read()

    # Skip if already reimagined (has our header format with perspective name)
    if f": {perspective['name']}" in original_content.split('\n')[0]:
        return False

    # Structure the content
    structured_content = structure_content(original_content, perspective)

    # Extract TL;DR
    tldr = extract_tldr(structured_content)

    # Build the reimagined document
    header = f"""# {paper_title}: {perspective['name']}

> {perspective['tagline']}

"""

    if tldr:
        header += f"""**TL;DR:** {tldr}

---

"""

    navigation = create_navigation(paper_dir, analysis_file, paper_title, paper_url)

    reimagined = header + structured_content + navigation

    with open(file_path, "w") as f:
        f.write(reimagined)

    return True


def reimagine_paper_readme(paper_dir: Path):
    """Create a beautiful landing page for each paper."""
    paper_title, paper_url = get_paper_title(paper_dir)

    # Get metadata for more context
    metadata_path = paper_dir / "metadata.json"
    section = ""
    year = ""
    if metadata_path.exists():
        with open(metadata_path) as f:
            data = json.load(f)
            paper = data.get("paper", {})
            section = paper.get("section", "")
            year_raw = paper.get("year", "")
            if year_raw and len(year_raw) == 4:
                yy = int(year_raw[:2])
                year = f"20{year_raw[:2]}" if yy < 90 else f"19{year_raw[:2]}"

    # Build perspective cards
    perspectives_section = []
    for stage_file in STAGE_ORDER:
        if (paper_dir / stage_file).exists():
            p = PERSPECTIVES[stage_file]
            perspectives_section.append(
                f"**[{p['name']}]({stage_file})**  \n{p['tagline']}\n"
            )

    readme_content = f"""# {paper_title}

"""

    if section or year:
        meta_parts = []
        if year:
            meta_parts.append(f"**Year:** {year}")
        if section:
            meta_parts.append(f"**Category:** {section}")
        readme_content += " · ".join(meta_parts) + "\n\n"

    if paper_url:
        readme_content += f"[Read the original paper]({paper_url})\n\n"

    readme_content += """---

## Choose Your Perspective

"""

    readme_content += "\n".join(perspectives_section)

    readme_content += f"""
---

[← All Papers](../) · [Home](../../README.md)
"""

    readme_path = paper_dir / "README.md"
    with open(readme_path, "w") as f:
        f.write(readme_content)


def reimagine_index():
    """Create a curated, beautiful index page."""

    # Collect all papers with metadata
    papers_by_category = {}
    priority_papers = []

    for paper_dir in sorted(PAPER_ANALYSIS_DIR.iterdir()):
        if not paper_dir.is_dir() or paper_dir.name.startswith("."):
            continue

        metadata_path = paper_dir / "metadata.json"
        if not metadata_path.exists():
            continue

        with open(metadata_path) as f:
            data = json.load(f)
            paper = data.get("paper", {})

        title = paper.get("title", paper_dir.name).replace("\\", "").strip()
        section = paper.get("section", "Other")
        priority = paper.get("priority", False)
        year_raw = paper.get("year", "")

        if year_raw and len(year_raw) == 4:
            yy = int(year_raw[:2])
            year = f"20{year_raw[:2]}" if yy < 90 else f"19{year_raw[:2]}"
        else:
            year = ""

        paper_info = {
            "dir": paper_dir.name,
            "title": title,
            "year": year,
            "priority": priority,
        }

        if section not in papers_by_category:
            papers_by_category[section] = []
        papers_by_category[section].append(paper_info)

        if priority:
            priority_papers.append(paper_info)

    # Build the index
    content = """# Paper Analyses

**36 papers. 5 perspectives each. Browse directly on GitHub.**

[← Back to Home](../README.md)

---

## Start With These

The foundational papers that everything else builds on:

| Paper | Year | What You'll Learn |
|-------|------|-------------------|
"""

    # Curated order for priority papers
    priority_order = ["Transformers", "GPT3", "RLHF", "CoT-Chain-of-Thought", "Llama3", "DeepSeek-R1", "MuZero"]

    for dir_name in priority_order:
        for p in priority_papers:
            if p["dir"] == dir_name:
                content += f"| [{p['title']}]({p['dir']}/) | {p['year']} | Core concept |\n"
                break

    content += """
---

## Browse by Category

"""

    # Preferred category order
    category_order = [
        "Foundational Modelling",
        "Planning/Reasoning",
        "Applications",
        "Benchmarks",
        "Surveys",
        "Others (non LLMs)",
    ]

    # Add categories in order, then remaining
    seen_categories = set()
    for category in category_order:
        if category in papers_by_category:
            seen_categories.add(category)
            papers = sorted(papers_by_category[category], key=lambda x: x.get("year", ""))
            content += f"### {category}\n\n"
            for p in papers:
                priority_mark = " ⭐" if p["priority"] else ""
                content += f"- [{p['title']}{priority_mark}]({p['dir']}/) ({p['year']})\n"
            content += "\n"

    # Add remaining categories
    for category, papers in sorted(papers_by_category.items()):
        if category in seen_categories:
            continue
        papers = sorted(papers, key=lambda x: x.get("year", ""))
        content += f"### {category}\n\n"
        for p in papers:
            priority_mark = " ⭐" if p["priority"] else ""
            content += f"- [{p['title']}{priority_mark}]({p['dir']}/) ({p['year']})\n"
        content += "\n"

    content += """---

## How to Read

Each paper has 5 analysis perspectives. Pick based on what you need:

| If you want... | Read this |
|----------------|-----------|
| Quick key takeaways | Precision Analysis |
| Deep technical understanding | Karpathy-Style |
| Practical builder implications | Builder's Perspective |
| Business/strategic view | Strategic Analysis |
| Implementation details | Pseudocode |

---

[← Back to Home](../README.md) · [Full Curriculum](../curriculum.md)
"""

    index_path = PAPER_ANALYSIS_DIR / "README.md"
    with open(index_path, "w") as f:
        f.write(content)


def main():
    print("Reimagining the reading experience...")
    print()

    papers_processed = 0
    files_updated = 0

    for paper_dir in sorted(PAPER_ANALYSIS_DIR.iterdir()):
        if not paper_dir.is_dir() or paper_dir.name.startswith("."):
            continue

        if not (paper_dir / "metadata.json").exists():
            continue

        print(f"  {paper_dir.name}/")
        papers_processed += 1

        # Reimagine each analysis file
        for stage_file in STAGE_ORDER:
            if reimagine_analysis(paper_dir, stage_file):
                files_updated += 1
                print(f"    ✓ {stage_file}")

        # Reimagine the paper landing page
        reimagine_paper_readme(paper_dir)
        print(f"    ✓ README.md")

    print()
    print("Reimagining index...")
    reimagine_index()
    print("  ✓ paper_analysis/README.md")

    print()
    print(f"Done! Processed {papers_processed} papers, updated {files_updated} analysis files.")
    print()
    print("The reading experience is now:")
    print("  • Clear headers with paper title + perspective")
    print("  • TL;DR at the top of each analysis")
    print("  • Navigation between perspectives")
    print("  • Beautiful paper landing pages")
    print("  • Curated index page")


if __name__ == "__main__":
    main()
