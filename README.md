# Module 5 — AI Resume Analyzer

An AI-powered resume analyzer that compares a resume against a job description to identify matching skills, missing skills, and improvement suggestions using the Google Gemini API.

## Features
- Extract skills from resume text
- Extract requirements from job description
- Identify matching and missing skills
- Generate improvement suggestions
- Clean structured output
- Handles empty input, API errors, and missing config gracefully

## Setup

1. Install dependencies:
```bash
pip install -r requirements.txt
```

2. Configure API key:
```bash
copy .env.example .env
# Edit .env and add your Gemini API key
```

Get a free API key at: https://aistudio.google.com/app/apikey

3. Run:
```bash
python app/main.py
```

## Project Structure
```
Module-5-AI-Mini-Project/
├── app/
│   ├── main.py         # Entry point
│   ├── analyzer.py     # AI analysis logic
│   └── utils.py        # Input helpers
├── screenshots/
├── README.md
├── requirements.txt
├── .env.example
└── .gitignore
```

## Security
- API key stored in `.env` only — never committed to Git
- `.env` is in `.gitignore`
