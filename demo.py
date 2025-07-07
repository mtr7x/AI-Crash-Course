#!/usr/bin/env python3
"""
Demo script to show the AI Paper Analysis System
"""

import json
import os
from pathlib import Path

def show_system_demo():
    """Demonstrate the AI Paper Analysis System"""
    
    print("🤖 AI Paper Analysis System Demo")
    print("=" * 50)
    
    # Check if analysis exists
    analysis_dir = Path("paper_analysis")
    if not analysis_dir.exists():
        print("❌ No analysis found. Run 'python paper_processor.py' first.")
        return
    
    # Load index
    index_file = analysis_dir / "index.json"
    if not index_file.exists():
        print("❌ No index.json found.")
        return
    
    with open(index_file, 'r') as f:
        data = json.load(f)
    
    print(f"📊 System Status:")
    print(f"   Generated: {data['generated_at']}")
    print(f"   Total Papers: {data['total_papers']}")
    print()
    
    print("📄 Analyzed Papers:")
    for i, paper in enumerate(data['papers'], 1):
        priority = "⭐" if paper['priority'] else "  "
        print(f"{priority} {i}. {paper['title']}")
        print(f"      Year: {paper['year']}")
        print(f"      Section: {paper['section']}")
        print(f"      Directory: {paper['directory']}")
        print()
    
    # Show sample analysis structure
    if data['papers']:
        sample_paper = data['papers'][0]
        sample_dir = analysis_dir / sample_paper['directory']
        
        print(f"🔍 Sample Analysis Structure ({sample_paper['title']}):")
        if sample_dir.exists():
            files = list(sample_dir.iterdir())
            for file in sorted(files):
                size = file.stat().st_size
                print(f"   📄 {file.name} ({size:,} bytes)")
        print()
    
    # Show viewer access
    print("🌐 Web Viewer:")
    print("   1. Start web server: python web_server.py")
    print("   2. Open: http://localhost:8080")
    print("   3. Click ⚙️ icon to configure API keys")
    print("   4. Click 'Re-analyze Papers' for real AI analysis")
    print("   5. View updated results in real-time")
    print()
    
    print("✨ Features:")
    print("   🔍 Search papers by title/section")
    print("   🏷️  Filter by category or priority")
    print("   📖 4 different analysis perspectives")
    print("   🔧 Implementation pseudocode")
    print("   ⚙️  API key configuration (OpenAI/Anthropic/Local)")
    print("   🔒 Secure local storage of credentials")
    print("   🔄 One-click re-analysis with real AI")
    print("   📡 Real-time progress tracking")
    print("   ♿ Full keyboard navigation")
    print("   📱 Responsive design")
    print()
    
    print("🎨 Design Principles (Julie Zhou):")
    print("   ✅ Content drives layout")
    print("   ✅ Clarity over cleverness")
    print("   ✅ Thoughtful defaults")
    print("   ✅ First-class states (zero, loading, error)")
    print("   ✅ WCAG AA accessibility")
    print("   ✅ Invisible design - focus on content")
    print()
    
    # Show sample content
    print("📝 Sample Analysis Preview:")
    sample_analysis = sample_dir / "stage_1_analysis.md"
    if sample_analysis.exists():
        print("   Stage 1 (Precision Analysis):")
        with open(sample_analysis, 'r') as f:
            lines = f.readlines()[:10]
            for line in lines:
                print(f"   {line.rstrip()}")
        print("   ... (truncated)")
    print()
    
    print("🚀 Next Steps:")
    print("   • Run 'python web_server.py' to start the web interface")
    print("   • Open http://localhost:8080 in your browser")
    print("   • Click ⚙️ to configure your API keys")
    print("   • Click 'Re-analyze Papers' for real AI insights")
    print("   • Explore the updated analyses with real AI content!")

if __name__ == "__main__":
    show_system_demo()