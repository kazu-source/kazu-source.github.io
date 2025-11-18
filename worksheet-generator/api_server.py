"""
API Server for Worksheet Generator GUI
Provides REST API endpoints for the web interface
"""

from flask import Flask, request, jsonify, send_file
from flask_cors import CORS
import sys
import os
from pathlib import Path
from datetime import datetime

# Add worksheet-generator to path
sys.path.insert(0, os.path.dirname(__file__))

from topic_registry import get_registry, register_all_generators
from pdf_generator import PDFWorksheetGenerator
from practice_test_generator import PracticeTestGenerator

app = Flask(__name__)
CORS(app)  # Enable CORS for development

# Initialize generators
register_all_generators()
registry = get_registry()
pdf_gen = PDFWorksheetGenerator()
practice_gen = PracticeTestGenerator()


@app.route('/api/generate-worksheet', methods=['POST'])
def generate_worksheet():
    """Generate a standard worksheet."""
    try:
        data = request.json
        unit = data.get('unit')
        topic = data.get('topic')
        topic_type = data.get('topicType', 'Intro')
        difficulty = data.get('difficulty', 'medium')
        num_problems = data.get('numProblems', 10)
        custom_title = data.get('customTitle')

        # Get generator
        generator = registry.get_generator(unit, topic_type, topic)
        if not generator:
            return jsonify({
                'success': False,
                'error': f'Generator not found for {topic}'
            }), 404

        # Generate problems
        problems = generator.generate_worksheet(difficulty, num_problems)

        # Create output path
        date_str = datetime.now().strftime("%Y%m%d")
        topic_clean = topic.replace(" ", "_").replace("/", "_").replace("(", "").replace(")", "").replace("?", "")
        output_dir = Path("output") / f"Unit{int(unit)}" / topic_type
        output_dir.mkdir(parents=True, exist_ok=True)

        if custom_title:
            title_clean = custom_title.replace(" ", "_")
            filename = f"{title_clean}_{date_str}.pdf"
            pdf_title = custom_title
        else:
            filename = f"{topic_clean}_{difficulty}_{date_str}.pdf"
            pdf_title = f"Algebra 1 - Unit {int(unit)} - {topic} ({difficulty.capitalize()})"

        output_path = output_dir / filename

        # Generate PDF
        pdf_gen.generate_worksheet(problems, str(output_path), title=pdf_title)

        return jsonify({
            'success': True,
            'path': str(output_path),
            'downloadUrl': f'/api/download/{output_path.name}'
        })

    except Exception as e:
        return jsonify({
            'success': False,
            'error': str(e)
        }), 500


@app.route('/api/generate-practice-test', methods=['POST'])
def generate_practice_test():
    """Generate a practice test."""
    try:
        data = request.json
        test_type = data.get('testType')
        difficulty_mix = data.get('difficultyMix', 'balanced')

        if test_type == 'unit':
            # Unit review
            unit = data.get('unit')
            num_problems = data.get('numProblems', 20)

            path = practice_gen.generate_unit_review(
                unit=unit,
                num_problems=num_problems,
                difficulty_mix=difficulty_mix
            )

        elif test_type == 'cumulative':
            # Cumulative test
            units = data.get('units', [])
            num_problems = data.get('numProblems', 30)

            path = practice_gen.generate_cumulative_test(
                units=units,
                num_problems=num_problems,
                difficulty_mix=difficulty_mix
            )

        elif test_type == 'spiral':
            # Spiral review
            unit = data.get('unit')
            topic = data.get('topic')
            topic_type = data.get('topicType', 'Intro')
            problems_per_level = data.get('problemsPerLevel', 5)

            path = practice_gen.generate_topic_spiral(
                topic=(unit, topic_type, topic),
                num_problems_per_level=problems_per_level
            )

        else:
            return jsonify({
                'success': False,
                'error': f'Invalid test type: {test_type}'
            }), 400

        filename = Path(path).name
        return jsonify({
            'success': True,
            'path': path,
            'downloadUrl': f'/api/download/{filename}'
        })

    except Exception as e:
        return jsonify({
            'success': False,
            'error': str(e)
        }), 500


@app.route('/api/generate-custom', methods=['POST'])
def generate_custom():
    """Generate a custom worksheet with multiple topics."""
    try:
        data = request.json
        title = data.get('title', 'Custom Worksheet')
        specs = data.get('specs', [])

        if not specs:
            return jsonify({
                'success': False,
                'error': 'No topics specified'
            }), 400

        # Generate problems for each spec
        all_problems = []
        for spec in specs:
            unit = spec['unit']
            topic = spec['topic']
            topic_type = spec.get('topicType', 'Intro')
            difficulty = spec['difficulty']
            num_problems = spec['numProblems']

            generator = registry.get_generator(unit, topic_type, topic)
            if generator:
                problems = generator.generate_worksheet(difficulty, num_problems)
                all_problems.extend(problems)

        # Shuffle for mixed practice
        import random
        random.shuffle(all_problems)

        # Create output path
        date_str = datetime.now().strftime("%Y%m%d")
        title_clean = title.replace(" ", "_")
        output_dir = Path("output") / "Custom"
        output_dir.mkdir(parents=True, exist_ok=True)
        filename = f"{title_clean}_{date_str}.pdf"
        output_path = output_dir / filename

        # Generate PDF
        pdf_title = f"Algebra 1 - {title}"
        pdf_gen.generate_worksheet(all_problems, str(output_path), title=pdf_title)

        return jsonify({
            'success': True,
            'path': str(output_path),
            'downloadUrl': f'/api/download/{filename}'
        })

    except Exception as e:
        return jsonify({
            'success': False,
            'error': str(e)
        }), 500


@app.route('/api/download/<filename>')
def download_file(filename):
    """Download a generated worksheet."""
    try:
        # Search for file in output directory
        output_dir = Path("output")

        # Search recursively for the file
        for file_path in output_dir.rglob(filename):
            return send_file(
                str(file_path),
                as_attachment=True,
                download_name=filename,
                mimetype='application/pdf'
            )

        return jsonify({
            'success': False,
            'error': 'File not found'
        }), 404

    except Exception as e:
        return jsonify({
            'success': False,
            'error': str(e)
        }), 500


@app.route('/api/topics/<unit>')
def get_topics(unit):
    """Get all topics for a unit."""
    try:
        unit_float = float(unit)
        topics = [t for t in registry.get_implemented_topics() if t.unit == unit_float]

        return jsonify({
            'success': True,
            'topics': [
                {
                    'topic': t.topic,
                    'type': t.type.value
                }
                for t in topics
            ]
        })

    except Exception as e:
        return jsonify({
            'success': False,
            'error': str(e)
        }), 500


@app.route('/api/stats')
def get_stats():
    """Get worksheet generator statistics."""
    try:
        stats = registry.get_coverage_stats()

        return jsonify({
            'success': True,
            'stats': {
                'totalTopics': stats['implemented'],
                'totalWorksheets': stats['implemented'] * 4,  # 4 difficulty levels
                'units': len(registry.get_units()),
                'difficultyLevels': 4
            }
        })

    except Exception as e:
        return jsonify({
            'success': False,
            'error': str(e)
        }), 500


if __name__ == '__main__':
    print("=" * 80)
    print("WORKSHEET GENERATOR API SERVER")
    print("=" * 80)
    print("\nServer starting on http://localhost:5000")
    print("\nAPI Endpoints:")
    print("  POST /api/generate-worksheet     - Generate standard worksheet")
    print("  POST /api/generate-practice-test - Generate practice test")
    print("  POST /api/generate-custom        - Generate custom worksheet")
    print("  GET  /api/download/<filename>    - Download generated file")
    print("  GET  /api/topics/<unit>          - Get topics for unit")
    print("  GET  /api/stats                  - Get generator statistics")
    print("\n" + "=" * 80)
    print()

    app.run(debug=True, port=5000)
