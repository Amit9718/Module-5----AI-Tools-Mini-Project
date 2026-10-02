"""
main.py — AI Resume Analyzer entry point.
"""

from analyzer import analyze_resume
from utils import get_multiline_input, print_results


def main():
    print("=" * 50)
    print("   AI RESUME ANALYZER — Module 5")
    print("   Powered by Google Gemini")
    print("=" * 50)

    resume_text = get_multiline_input("\nPaste your RESUME text below:")
    if not resume_text:
        print("Error: Resume cannot be empty.")
        return

    job_description = get_multiline_input("\nPaste the JOB DESCRIPTION below:")
    if not job_description:
        print("Error: Job description cannot be empty.")
        return

    print("\nAnalyzing your resume... please wait.")

    try:
        result = analyze_resume(resume_text, job_description)
        print_results(result)
    except EnvironmentError as e:
        print(f"\nConfiguration Error: {e}")
    except ValueError as e:
        print(f"\nInput Error: {e}")
    except Exception as e:
        print(f"\nError during analysis: {e}")
        print("Please check your API key and internet connection.")

    print("\nAnalysis complete.")


if __name__ == "__main__":
    main()
