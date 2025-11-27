"""
ai_resume_analyzer.app
Simple Flask API to analyze resume text and return insights.
"""
from flask import Flask, request, jsonify
from utils.analyzer import analyze_resume

app = Flask(__name__)

@app.route("/", methods=["GET"])
def index():
    return jsonify({"message": "AI Resume Analyzer - POST /analyze with JSON {'text': '...'}"}), 200

@app.route("/analyze", methods=["POST"])
def analyze():
    data = request.get_json(silent=True) or {}
    text = data.get("text", "").strip()

    if not text:
        return jsonify({"error": "Please provide resume text in 'text' field."}), 400

    result = analyze_resume(text)
    return jsonify(result), 200

if __name__ == "__main__":
    # For local testing only. Use a WSGI server for production.
    app.run(host="0.0.0.0", port=5000, debug=False)
