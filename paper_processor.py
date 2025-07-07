#!/usr/bin/env python3
"""
AI Paper Analysis Pipeline
Fetches papers from README links and generates comprehensive analysis
"""

import os
import re
import json
import asyncio
import aiohttp
import aiofiles
from pathlib import Path
from typing import Dict, List, Tuple, Optional
from urllib.parse import urlparse
import markdown
from bs4 import BeautifulSoup
import PyPDF2
import requests
from datetime import datetime

class PaperProcessor:
    def __init__(self, output_dir: str = "paper_analysis"):
        self.output_dir = Path(output_dir)
        self.output_dir.mkdir(exist_ok=True)
        self.session = None
        
        # Load analysis prompts
        self.prompts = self._load_prompts()
        
    def _load_prompts(self) -> Dict[str, str]:
        """Load the 4-stage analysis prompts"""
        prompts_file = Path("document_analysis_prompts.md")
        if not prompts_file.exists():
            raise FileNotFoundError("document_analysis_prompts.md not found")
            
        with open(prompts_file, 'r', encoding='utf-8') as f:
            content = f.read()
            
        # Parse prompts from markdown
        prompts = {}
        sections = content.split('## Stage')
        
        for i, section in enumerate(sections[1:], 1):  # Skip header
            lines = section.strip().split('\n')
            title = lines[0].strip()
            prompt_content = '\n'.join(lines[1:]).strip()
            prompts[f"stage_{i}"] = {
                "title": title,
                "content": prompt_content
            }
            
        return prompts
    
    async def extract_papers_from_readme(self) -> List[Dict[str, str]]:
        """Extract paper links and metadata from README.md"""
        readme_path = Path("README.md")
        if not readme_path.exists():
            raise FileNotFoundError("README.md not found")
            
        with open(readme_path, 'r', encoding='utf-8') as f:
            content = f.read()
            
        papers = []
        lines = content.split('\n')
        
        current_section = "Unknown"
        for line in lines:
            # Track sections - improved pattern matching
            if (line.startswith('**') and (':**' in line or line.strip().endswith('**'))) or line.startswith('# '):
                section_clean = re.sub(r'\*+|#+|:', '', line).strip()
                if section_clean:
                    current_section = section_clean
                continue
                
            # Find paper links - improved to catch more patterns
            if 'arxiv.org' in line or '.pdf' in line or 'github.com' in line:
                # Extract paper info using regex - handle multiple link patterns
                link_patterns = [
                    r'\[([^\]]+)\]\(([^)]+)\)',  # Standard markdown links
                    r'\[([^\]]+)\*?\]\(([^)]+)\)',  # Links with trailing asterisks
                ]
                
                for pattern in link_patterns:
                    matches = re.findall(pattern, line)
                    
                    for title, url in matches:
                        if ('arxiv.org' in url or '.pdf' in url or 'github.com' in url) and title:
                            # Clean title - remove asterisks and extra whitespace
                            clean_title = re.sub(r'\*+', '', title).strip()
                            if not clean_title:
                                continue
                                
                            # Extract year - look for 4-digit years
                            year_match = re.search(r'(\d{4})', line)
                            year = year_match.group(1) if year_match else "Unknown"
                            
                            # Check if starred (priority) - more robust check
                            is_priority = ('**' in title and title.count('*') >= 3) or ('*' in title and title.count('*') >= 3)
                            
                            # Skip duplicates
                            if not any(p['url'] == url for p in papers):
                                papers.append({
                                    "title": clean_title,
                                    "url": url,
                                    "section": current_section,
                                    "year": year,
                                    "priority": is_priority,
                                    "raw_line": line.strip()
                                })
                        
        return papers
    
    async def fetch_paper_content(self, url: str) -> Optional[str]:
        """Fetch paper content from URL (PDF or HTML)"""
        try:
            if not self.session:
                self.session = aiohttp.ClientSession()
                
            async with self.session.get(url) as response:
                if response.status != 200:
                    return None
                    
                content_type = response.headers.get('content-type', '')
                content = await response.read()
                
                if 'pdf' in content_type.lower():
                    return self._extract_pdf_text(content)
                else:
                    return self._extract_html_text(content)
                    
        except Exception as e:
            print(f"Error fetching {url}: {e}")
            return None
    
    def _extract_pdf_text(self, pdf_content: bytes) -> str:
        """Extract text from PDF content"""
        try:
            # Save temporarily and extract
            temp_path = self.output_dir / "temp.pdf"
            with open(temp_path, 'wb') as f:
                f.write(pdf_content)
                
            text = ""
            with open(temp_path, 'rb') as f:
                reader = PyPDF2.PdfReader(f)
                for page in reader.pages:
                    text += page.extract_text() + "\n"
                    
            temp_path.unlink()  # Clean up
            return text
            
        except Exception as e:
            print(f"Error extracting PDF: {e}")
            return ""
    
    def _extract_html_text(self, html_content: bytes) -> str:
        """Extract text from HTML content"""
        try:
            soup = BeautifulSoup(html_content, 'html.parser')
            # Remove script and style elements
            for script in soup(["script", "style"]):
                script.decompose()
            return soup.get_text()
        except Exception as e:
            print(f"Error extracting HTML: {e}")
            return ""
    
    def generate_pseudocode(self, paper_title: str, content: str) -> str:
        """Generate pseudocode representation of the paper's core algorithm"""
        # This is a simplified version - in practice, you'd use LLM API
        pseudocode_template = f"""
# {paper_title} - Core Algorithm Pseudocode

## Main Algorithm
```
ALGORITHM {paper_title.replace(' ', '_').upper()}
INPUT: [Key inputs from paper]
OUTPUT: [Key outputs from paper]

PROCEDURE:
1. Initialize parameters
2. [Core process step 1]
3. [Core process step 2]
4. [Core process step 3]
5. Return results

COMPLEXITY: [Time/Space complexity if mentioned]
```

## Key Components
- **Input Processing**: [How input is handled]
- **Core Logic**: [Main algorithmic contribution]
- **Output Generation**: [How results are produced]

## Notable Optimizations
- [Optimization 1]
- [Optimization 2]

Generated on: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}
        """
        return pseudocode_template.strip()
    
    async def call_llm_api(self, content: str, prompt: str, stage_name: str) -> str:
        """Call LLM API for analysis (if configured)"""
        # Check for environment variables or config file
        openai_key = os.getenv('OPENAI_API_KEY')
        anthropic_key = os.getenv('ANTHROPIC_API_KEY')
        
        if openai_key:
            return await self._call_openai(content, prompt, stage_name, openai_key)
        elif anthropic_key:
            return await self._call_anthropic(content, prompt, stage_name, anthropic_key)
        else:
            # Return placeholder if no API keys available
            return self._generate_placeholder_analysis(stage_name, content[:500])
    
    async def _call_openai(self, content: str, prompt: str, stage_name: str, api_key: str) -> str:
        """Call OpenAI API"""
        try:
            headers = {
                'Authorization': f'Bearer {api_key}',
                'Content-Type': 'application/json'
            }
            
            data = {
                'model': 'gpt-4',
                'messages': [
                    {'role': 'system', 'content': prompt},
                    {'role': 'user', 'content': f"Analyze this paper:\n\n{content[:8000]}"}  # Limit content
                ],
                'max_tokens': 2000,
                'temperature': 0.3
            }
            
            if not self.session:
                self.session = aiohttp.ClientSession()
                
            async with self.session.post('https://api.openai.com/v1/chat/completions', 
                                       headers=headers, json=data) as response:
                if response.status == 200:
                    result = await response.json()
                    return result['choices'][0]['message']['content']
                else:
                    print(f"OpenAI API error: {response.status}")
                    return self._generate_placeholder_analysis(stage_name, content[:500])
                    
        except Exception as e:
            print(f"Error calling OpenAI API: {e}")
            return self._generate_placeholder_analysis(stage_name, content[:500])
    
    async def _call_anthropic(self, content: str, prompt: str, stage_name: str, api_key: str) -> str:
        """Call Anthropic API"""
        try:
            headers = {
                'x-api-key': api_key,
                'Content-Type': 'application/json',
                'anthropic-version': '2023-06-01'
            }
            
            data = {
                'model': 'claude-3-sonnet-20240229',
                'max_tokens': 2000,
                'messages': [
                    {'role': 'user', 'content': f"{prompt}\n\nPaper content:\n\n{content[:8000]}"}
                ]
            }
            
            if not self.session:
                self.session = aiohttp.ClientSession()
                
            async with self.session.post('https://api.anthropic.com/v1/messages', 
                                       headers=headers, json=data) as response:
                if response.status == 200:
                    result = await response.json()
                    return result['content'][0]['text']
                else:
                    print(f"Anthropic API error: {response.status}")
                    return self._generate_placeholder_analysis(stage_name, content[:500])
                    
        except Exception as e:
            print(f"Error calling Anthropic API: {e}")
            return self._generate_placeholder_analysis(stage_name, content[:500])
    
    def _generate_placeholder_analysis(self, stage_name: str, content_preview: str) -> str:
        """Generate placeholder analysis when no API is available"""
        return f"""
# {stage_name} Analysis

## Overview
This is a placeholder analysis. To generate real AI-powered insights, configure your API keys in the web viewer settings.

## Content Preview
```
{content_preview}...
```

## Next Steps
1. Start the web server: `python web_server.py`
2. Open the web viewer at http://localhost:8080
3. Click the settings gear icon (⚙️) in the top right
4. Configure your OpenAI or Anthropic API key
5. Click "Re-analyze Papers" button to update with real AI analysis

**Generated:** {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}
        """

    async def analyze_paper(self, paper: Dict[str, str]) -> Dict[str, str]:
        """Run 4-stage analysis on a paper"""
        print(f"Analyzing: {paper['title']}")
        
        # Create paper directory
        safe_title = re.sub(r'[^\w\s-]', '', paper['title']).strip()
        safe_title = re.sub(r'[-\s]+', '-', safe_title)
        paper_dir = self.output_dir / safe_title
        paper_dir.mkdir(exist_ok=True)
        
        # Fetch content
        content = await self.fetch_paper_content(paper['url'])
        if not content:
            print(f"Failed to fetch content for {paper['title']}")
            return {}
            
        # Save original content
        async with aiofiles.open(paper_dir / "original_content.txt", 'w', encoding='utf-8') as f:
            await f.write(content)
            
        # Generate analyses
        analyses = {}
        
        # Generate real or placeholder analyses for each stage
        for stage_key, prompt_data in self.prompts.items():
            print(f"  Generating {prompt_data['title']}...")
            analysis = await self.call_llm_api(content, prompt_data['content'], prompt_data['title'])
            analyses[stage_key] = analysis
            
            # Save individual analysis
            async with aiofiles.open(paper_dir / f"{stage_key}_analysis.md", 'w', encoding='utf-8') as f:
                await f.write(analysis)
        
        # Generate pseudocode
        pseudocode = self.generate_pseudocode(paper['title'], content)
        analyses['pseudocode'] = pseudocode
        
        async with aiofiles.open(paper_dir / "pseudocode.md", 'w', encoding='utf-8') as f:
            await f.write(pseudocode)
        
        # Save metadata
        metadata = {
            "paper": paper,
            "processed_at": datetime.now().isoformat(),
            "analyses_generated": list(analyses.keys()),
            "api_used": bool(os.getenv('OPENAI_API_KEY') or os.getenv('ANTHROPIC_API_KEY'))
        }
        
        async with aiofiles.open(paper_dir / "metadata.json", 'w', encoding='utf-8') as f:
            await f.write(json.dumps(metadata, indent=2))
        
        return analyses
    
    async def process_all_papers(self, limit: Optional[int] = None):
        """Process all papers from README"""
        papers = await self.extract_papers_from_readme()
        
        if limit:
            papers = papers[:limit]
            
        print(f"Found {len(papers)} papers to process")
        
        # Process priority papers first
        priority_papers = [p for p in papers if p['priority']]
        regular_papers = [p for p in papers if not p['priority']]
        
        all_papers = priority_papers + regular_papers
        
        # Process papers with concurrency limit
        semaphore = asyncio.Semaphore(3)  # Limit concurrent requests
        
        async def process_single_paper(paper):
            async with semaphore:
                return await self.analyze_paper(paper)
        
        tasks = [process_single_paper(paper) for paper in all_papers]
        await asyncio.gather(*tasks, return_exceptions=True)
        
        print(f"Completed processing {len(all_papers)} papers")
        
        # Generate index
        await self.generate_index(all_papers)
    
    async def generate_index(self, papers: List[Dict[str, str]]):
        """Generate index.json for the viewer"""
        index = {
            "generated_at": datetime.now().isoformat(),
            "total_papers": len(papers),
            "papers": []
        }
        
        for paper in papers:
            safe_title = re.sub(r'[^\w\s-]', '', paper['title']).strip()
            safe_title = re.sub(r'[-\s]+', '-', safe_title)
            
            index["papers"].append({
                "title": paper['title'],
                "section": paper['section'],
                "year": paper['year'],
                "priority": paper['priority'],
                "url": paper['url'],
                "directory": safe_title
            })
        
        async with aiofiles.open(self.output_dir / "index.json", 'w', encoding='utf-8') as f:
            await f.write(json.dumps(index, indent=2))
    
    async def cleanup(self):
        """Clean up resources"""
        if self.session:
            await self.session.close()

async def main():
    """Main execution function"""
    processor = PaperProcessor()
    
    try:
        # Process all papers from README
        await processor.process_all_papers()
    finally:
        await processor.cleanup()

if __name__ == "__main__":
    asyncio.run(main())