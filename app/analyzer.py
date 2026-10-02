"""
analyzer.py — AI-powered resume analysis using Google Gemini.
"""

import os
import json
import google.generativeai as genai
from dotenv import load_dotenv

load_dotenv()


def _configure_model():
    """Configure and return the Gemini model."""
    api_key = os.getenv("GEMINI_API_KEY")
    if not api_key or api_key == "your_gemini_api_key_here":
        raise EnvironmentError(
            "GEMINI_API_KEY not set. Copy .env.example to .env and add your key."
        )
    genai.configure(api_key=api_key)
    return genai.GenerativeModel("gemini-1.5-flash")


def analyze_resume(resume_text: str, job_description: str) -> dict:
    """
    Analyze resume against job description using Gemini.

    Returns a dict with keys:
        - skills_in_resume: list[str]
        - skills_required: list[str]
        - matching_skills: list[str]
        - missing_skills: list[str]
        - suggestions: list[str]
        - summary: str
    """
    if not resume_text.strip():
        raise ValueError("Resume text cannot be empty.")
    if not job_description.strip():
        raise ValueError("Job description cannot be empty.")

    prompt = f"""
You are a professional career coach and resume expert.

Analyze the resume below against the provided job description.
Respond ONLY with valid JSON — no markdown, no extra text.

JSON format:
{{
  "skills_in_resume": ["skill1", "skill2"],
  "skills_required": ["skill1", "skill2"],
  "matching_skills": ["skill1"],
  "missing_skills": ["skill2"],
  "suggestions": [
    "Suggestion 1",
    "Suggestion 2"
  ],
  "summary": "One paragraph summary of job fit."
}}

RESUME:
{resume_text}

JOB DESCRIPTION:
{job_description}
"""

    model = _configure_model()
    response = model.generate_content(prompt)
    raw = response.text.strip()

    # Strip markdown code fences if present
    if raw.startswith("```"):
        raw = raw.split("```")[1]
        if raw.startswith("json"):
            raw = raw[4:]
        raw = raw.strip()

    try:
        return json.loads(raw)
    except json.JSONDecodeError:
        # Fallback: return raw text in summary field
        return {
            "skills_in_resume": [],
            "skills_required": [],
            "matching_skills": [],
            "missing_skills": [],
            "suggestions": [],
            "summary": raw,
        }
