# AI Paper Analysis System

A comprehensive system for analyzing AI research papers with multiple analytical perspectives and an intuitive viewing interface.

## Overview

This system automatically:
1. Extracts paper links from the AI Crash Course README
2. Fetches paper content (PDF/HTML)
3. Generates 4 different analysis perspectives:
   - **Precision Analysis**: Key insights, surprises, and quotes
   - **Karpathy Style**: Technical depth with first-principles thinking
   - **Swyx Style**: Developer-focused community insights
   - **Elad Gil Style**: Strategic business implications
4. Creates implementation pseudocode
5. Provides an intuitive web viewer

## Quick Start

### 1. Install Dependencies
```bash
pip install -r requirements.txt
```

### 2. Configure API Keys (Optional)
```bash
# Interactive setup
python setup_api.py

# Or set environment variables manually
export OPENAI_API_KEY="sk-your-key-here"
export ANTHROPIC_API_KEY="your-anthropic-key"
```

### 3. Run Paper Analysis
```bash
python paper_processor.py
```

### 4. View Results
```bash
# Start web server
python -m http.server 8000
# Then visit: http://localhost:8000/viewer.html
```

## System Architecture

### Paper Processing Pipeline
```
README.md → Extract Links → Fetch Content → 4-Stage Analysis → Generate Pseudocode → Save to Directories
```

### Directory Structure
```
paper_analysis/
├── index.json                 # Master index of all papers
├── attention-is-all-you-need/
│   ├── metadata.json         # Paper metadata
│   ├── original_content.txt  # Raw paper content
│   ├── stage_1_analysis.md   # Precision analysis
│   ├── stage_2_analysis.md   # Karpathy style
│   ├── stage_3_analysis.md   # Swyx style
│   ├── stage_4_analysis.md   # Elad Gil style
│   └── pseudocode.md         # Implementation pseudocode
└── [other-papers]/
    └── [same structure]
```

## Analysis Stages

### Stage 1: Precision Analysis
- 5-7 key insights that challenge conventional thinking
- Surprising/shocking elements that contradict expectations
- 3-5 impactful direct quotes
- Focus on actionable takeaways

### Stage 2: Karpathy Style
- Technical precision with clear language
- First-principles breakdown of concepts
- Practical implementation insights
- Systems thinking approach

### Stage 3: Swyx Style
- Developer-centric perspective
- Community and ecosystem implications
- Actionable next steps for builders
- Trend synthesis and pattern recognition

### Stage 4: Elad Gil Style
- Strategic business focus
- Market timing and competitive analysis
- Investment and scaling considerations
- Long-term value creation insights

### Stage 5: Pseudocode
- Core algorithm representation
- Key components and optimizations
- Complexity analysis
- Implementation structure

## Viewer Features

### API Configuration
- **Settings Modal**: Click ⚙️ icon in top-right corner
- **Multiple Providers**: OpenAI, Anthropic, or Local LLM support
- **Secure Storage**: Keys stored locally in browser only
- **Privacy First**: Keys never transmitted to our servers
- **Easy Setup**: Interactive configuration with validation

### Design Principles (Julie Zhou Inspired)
- **Content-driven layout**: Typography and spacing build trust
- **Thoughtful defaults**: Reduced decision fatigue
- **First-class states**: Zero, loading, error, success states
- **Accessibility**: WCAG AA compliance
- **Invisible design**: Users focus on content, not UI

### Key Features
- **Smart filtering**: By category, priority, or search
- **Keyboard navigation**: Full accessibility support
- **Responsive design**: Works on all devices
- **State management**: Proper loading and error states
- **Performance**: Efficient content loading
- **API Integration**: Real-time analysis with your API keys

### Navigation
- **Search**: Type to filter papers by title or section
- **Filters**: All, Priority, Foundational, Applications, Benchmarks
- **Tabs**: Switch between analysis perspectives
- **Settings**: Click ⚙️ to configure API keys
- **Keyboard**: Arrow keys for tab navigation, Escape to clear

## Customization

### Adding New Analysis Stages
1. Update `document_analysis_prompts.md`
2. Modify `paper_processor.py` to include new stage
3. Update viewer tabs in `viewer.html`

### Styling
- Modify CSS custom properties in `viewer.html`
- All colors, spacing, and typography controlled via CSS variables
- Supports dark mode and high contrast

### Processing Options
```python
# Process specific number of papers
await processor.process_all_papers(limit=10)

# Process only priority papers
priority_papers = [p for p in papers if p['priority']]
```

## LLM Integration

To enable actual AI analysis (currently uses placeholders):

1. Add your preferred LLM API (OpenAI, Anthropic, etc.)
2. Update the `analyze_paper` method in `paper_processor.py`
3. Replace placeholder analysis with actual LLM calls

Example OpenAI integration:
```python
import openai

async def generate_analysis(content, prompt):
    response = await openai.ChatCompletion.acreate(
        model="gpt-4",
        messages=[
            {"role": "system", "content": prompt},
            {"role": "user", "content": content}
        ]
    )
    return response.choices[0].message.content
```

## Performance Considerations

- **Concurrent processing**: Limited to 3 simultaneous requests
- **Caching**: Results saved to disk for reuse
- **Incremental updates**: Only process new/updated papers
- **Content limits**: Large papers truncated for processing

## Error Handling

- **Network failures**: Graceful fallback and retry
- **PDF parsing errors**: Alternative text extraction
- **Missing content**: Clear error states in viewer
- **API limits**: Rate limiting and backoff

## Development

### Running Tests
```bash
python -m pytest tests/
```

### Code Style
```bash
black paper_processor.py
flake8 paper_processor.py
```

### Contributing
1. Fork the repository
2. Create feature branch
3. Follow existing code style
4. Add tests for new features
5. Submit pull request

## License

MIT License - see LICENSE file for details.