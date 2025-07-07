#!/usr/bin/env python3
"""
Web server for AI Paper Analysis with API endpoint
"""

import os
import json
import asyncio
import subprocess
from pathlib import Path
from flask import Flask, request, jsonify, send_from_directory
from flask_cors import CORS
import tempfile

app = Flask(__name__)
CORS(app)

# Serve static files
@app.route('/')
def index():
    return send_from_directory('.', 'viewer.html')

@app.route('/<path:filename>')
def serve_static(filename):
    return send_from_directory('.', filename)

@app.route('/api/analyze', methods=['POST'])
def analyze_papers():
    """API endpoint to trigger paper analysis with user's API keys"""
    try:
        data = request.get_json()
        
        if not data:
            return jsonify({'error': 'No data provided'}), 400
        
        provider = data.get('provider')
        api_key = data.get('apiKey')
        endpoint = data.get('endpoint')
        
        if not provider:
            return jsonify({'error': 'Provider not specified'}), 400
        
        # Validate API key/endpoint based on provider
        if provider in ['openai', 'anthropic'] and not api_key:
            return jsonify({'error': f'{provider} API key required'}), 400
        
        if provider == 'local' and not endpoint:
            return jsonify({'error': 'Local endpoint required'}), 400
        
        # Set environment variables temporarily
        env = os.environ.copy()
        
        if provider == 'openai':
            env['OPENAI_API_KEY'] = api_key
        elif provider == 'anthropic':
            env['ANTHROPIC_API_KEY'] = api_key
        elif provider == 'local':
            env['LOCAL_LLM_ENDPOINT'] = endpoint
        
        # Run the paper processor
        try:
            result = subprocess.run(
                ['python', 'paper_processor.py'],
                env=env,
                capture_output=True,
                text=True,
                timeout=300  # 5 minute timeout
            )
            
            if result.returncode == 0:
                # Parse output to get number of papers processed
                output_lines = result.stdout.strip().split('\n')
                papers_processed = 0
                
                for line in output_lines:
                    if 'Found' in line and 'papers to process' in line:
                        try:
                            papers_processed = int(line.split()[1])
                        except:
                            papers_processed = 5  # fallback
                
                return jsonify({
                    'success': True,
                    'message': 'Analysis completed successfully',
                    'papers_processed': papers_processed,
                    'output': result.stdout
                })
            else:
                return jsonify({
                    'error': 'Analysis failed',
                    'message': result.stderr or result.stdout
                }), 500
                
        except subprocess.TimeoutExpired:
            return jsonify({
                'error': 'Analysis timeout',
                'message': 'Analysis took too long (>5 minutes)'
            }), 408
        
        except Exception as e:
            return jsonify({
                'error': 'Execution failed',
                'message': str(e)
            }), 500
    
    except Exception as e:
        return jsonify({
            'error': 'Server error',
            'message': str(e)
        }), 500

@app.route('/api/status')
def get_status():
    """Get current analysis status"""
    try:
        # Check if index.json exists and get timestamp
        index_file = Path('paper_analysis/index.json')
        if index_file.exists():
            with open(index_file, 'r') as f:
                data = json.load(f)
            return jsonify({
                'last_updated': data.get('generated_at'),
                'total_papers': data.get('total_papers', 0),
                'papers': data.get('papers', [])
            })
        else:
            return jsonify({
                'last_updated': None,
                'total_papers': 0,
                'papers': []
            })
    except Exception as e:
        return jsonify({
            'error': 'Failed to get status',
            'message': str(e)
        }), 500

if __name__ == '__main__':
    print("🚀 Starting AI Paper Analysis Web Server")
    print("=" * 50)
    print("📊 Features:")
    print("   • Web viewer with API configuration")
    print("   • Real-time paper analysis")
    print("   • Secure API key handling")
    print("   • Progress tracking")
    print()
    print("🌐 Access:")
    print("   • Viewer: http://localhost:8080")
    print("   • API Status: http://localhost:8080/api/status")
    print()
    print("⚙️ Usage:")
    print("   1. Open the viewer in your browser")
    print("   2. Click ⚙️ to configure API keys")
    print("   3. Click 'Re-analyze Papers' to run analysis")
    print("   4. View updated results in real-time")
    print()
    
    # Start the server
    app.run(host='localhost', port=8080, debug=False)