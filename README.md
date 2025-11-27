# AI Resume Analyzer

Lightweight Flask service to analyze resume text and return simple insights:
- word & character count
- skills detected (rule-based)
- top terms
- brief summary
- simple readability score

## Usage
POST /analyze
Body: {"text": "paste resume text here"}

Run locally:
pip install -r requirements.txt
python app.py
