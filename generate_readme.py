#!/usr/bin/env python3
"""Generate README.md files for each paper folder and a master index.

This makes the paper analyses browsable directly on GitHub without
needing to run the web server.
"""

import json
import os
from pathlib import Path

PAPER_ANALYSIS_DIR = Path("paper_analysis")

# Mapping of stage files to human-readable names
ANALYSIS_PERSPECTIVES = [
    ("stage_1_analysis.md", "Precision Analysis", "Technical deep-dive, key insights, notable quotes"),
    ("stage_2_analysis.md", "Karpathy Style", "First-principles explanation, balanced technical depth"),
    ("stage_3_analysis.md", "Developer Perspective (Swyx)", "Practical implications for builders, trends"),
    ("stage_4_analysis.md", "Strategic Analysis (Elad Gil)", "Business implications, investment perspective"),
    ("pseudocode.md", "Pseudocode", "Core algorithm implementation"),
]


def generate_paper_readme(paper_dir: Path) -> dict | None:
    """Generate README.md for a single paper folder."""
    metadata_path = paper_dir / "metadata.json"

    if not metadata_path.exists():
        print(f"  Skipping {paper_dir.name} - no metadata.json")
        return None

    with open(metadata_path) as f:
        metadata = json.load(f)

    paper = metadata.get("paper", {})
    title = paper.get("title", paper_dir.name).rstrip("\\")
    url = paper.get("url", "")
    section = paper.get("section", "")
    year = paper.get("year", "")
    priority = paper.get("priority", False)

    # Fix year parsing - arxiv IDs look like YYMM (e.g., 1706 = 2017, 2305 = 2023)
    if year and len(year) == 4:
        yy = int(year[:2])
        if yy >= 90:  # 90-99 -> 1990-1999
            year = f"19{year[:2]}"
        else:  # 00-89 -> 2000-2089
            year = f"20{year[:2]}"

    # Clean title artifacts
    title = title.replace("\\", "").strip()

    # Build README content
    priority_badge = " ⭐" if priority else ""

    lines = [
        f"# {title}{priority_badge}",
        "",
    ]

    if section:
        lines.append(f"**Category:** {section}")
    if year:
        lines.append(f"**Year:** {year}")
    if url:
        lines.append(f"**Original:** [{url}]({url})")

    lines.extend([
        "",
        "---",
        "",
        "## Analysis Perspectives",
        "",
        "| Perspective | Focus |",
        "|-------------|-------|",
    ])

    for filename, name, description in ANALYSIS_PERSPECTIVES:
        if (paper_dir / filename).exists():
            lines.append(f"| [{name}]({filename}) | {description} |")

    lines.extend([
        "",
        "---",
        "",
        f"[Back to Paper Index](../README.md)",
    ])

    readme_content = "\n".join(lines)

    readme_path = paper_dir / "README.md"
    with open(readme_path, "w") as f:
        f.write(readme_content)

    print(f"  Created {paper_dir.name}/README.md")

    return {
        "name": paper_dir.name,
        "title": title,
        "url": url,
        "section": section,
        "year": year,
        "priority": priority,
    }


def generate_master_index(papers: list[dict]):
    """Generate the master index README.md for paper_analysis/."""

    # Group by section
    sections = {}
    for paper in papers:
        section = paper.get("section", "Other")
        if section not in sections:
            sections[section] = []
        sections[section].append(paper)

    lines = [
        "# Paper Analysis Index",
        "",
        f"**{len(papers)} papers analyzed from 5 perspectives each.**",
        "",
        "Browse any paper directly on GitHub - no server required.",
        "",
        "---",
        "",
    ]

    # Add quick links to priority papers first
    priority_papers = [p for p in papers if p.get("priority")]
    if priority_papers:
        lines.extend([
            "## Priority Papers ⭐",
            "",
            "Start here for the most impactful papers:",
            "",
            "| Paper | Year | Category |",
            "|-------|------|----------|",
        ])
        for paper in sorted(priority_papers, key=lambda x: x.get("year", "")):
            name = paper["name"]
            title = paper["title"]
            year = paper.get("year", "")
            section = paper.get("section", "")
            lines.append(f"| [{title}]({name}/) | {year} | {section} |")
        lines.extend(["", "---", ""])

    # Add all papers by section
    lines.append("## All Papers by Category")
    lines.append("")

    for section in sorted(sections.keys()):
        section_papers = sections[section]
        lines.extend([
            f"### {section}",
            "",
            "| Paper | Year |",
            "|-------|------|",
        ])
        for paper in sorted(section_papers, key=lambda x: x.get("year", "")):
            name = paper["name"]
            title = paper["title"]
            year = paper.get("year", "")
            priority_mark = " ⭐" if paper.get("priority") else ""
            lines.append(f"| [{title}{priority_mark}]({name}/) | {year} |")
        lines.append("")

    lines.extend([
        "---",
        "",
        "## What Each Perspective Offers",
        "",
        "| Perspective | Focus | Best For |",
        "|-------------|-------|----------|",
        "| Precision Analysis | Key insights, surprising elements, notable quotes | Quick understanding |",
        "| Karpathy Style | First-principles, technical depth | Deep learning |",
        "| Developer Perspective | Practical implications, trends | Building things |",
        "| Strategic Analysis | Business implications, market impact | Investment/strategy |",
        "| Pseudocode | Core algorithms | Implementation |",
        "",
        "---",
        "",
        "[Back to Main Curriculum](../README.md)",
    ])

    content = "\n".join(lines)

    index_path = PAPER_ANALYSIS_DIR / "README.md"
    with open(index_path, "w") as f:
        f.write(content)

    print(f"\nCreated paper_analysis/README.md with {len(papers)} papers")


def main():
    print("Generating paper README files...")
    print()

    papers = []

    for paper_dir in sorted(PAPER_ANALYSIS_DIR.iterdir()):
        if paper_dir.is_dir() and not paper_dir.name.startswith("."):
            result = generate_paper_readme(paper_dir)
            if result:
                papers.append(result)

    print()
    generate_master_index(papers)

    print(f"\nDone! Generated {len(papers)} paper READMEs + master index.")
    print("\nPapers are now browsable directly on GitHub:")
    print("  - paper_analysis/README.md (index)")
    print("  - paper_analysis/{Paper}/README.md (navigation)")


if __name__ == "__main__":
    main()
