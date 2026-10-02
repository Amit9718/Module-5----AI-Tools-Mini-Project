"""
utils.py — Input helpers for the resume analyzer.
"""


def get_multiline_input(prompt: str) -> str:
    """
    Prompt user for multi-line input.
    User types content and enters 'END' on a new line to finish.
    """
    print(prompt)
    print("(Enter your text. Type 'END' on a new line when done.)\n")
    lines = []
    while True:
        line = input()
        if line.strip().upper() == "END":
            break
        lines.append(line)
    return "\n".join(lines).strip()


def print_section(title: str, items: list, empty_msg: str = "None identified."):
    """Print a named list section."""
    print(f"\n{'='*50}")
    print(f"  {title}")
    print(f"{'='*50}")
    if items:
        for item in items:
            print(f"  • {item}")
    else:
        print(f"  {empty_msg}")


def print_results(result: dict):
    """Pretty-print the analysis results."""
    print("\n" + "=" * 50)
    print("  RESUME ANALYSIS RESULTS")
    print("=" * 50)

    print_section("Skills Found in Resume", result.get("skills_in_resume", []))
    print_section("Skills Required by Job", result.get("skills_required", []))
    print_section("Matching Skills ✓", result.get("matching_skills", []))
    print_section("Missing Skills ✗", result.get("missing_skills", []))
    print_section("Improvement Suggestions", result.get("suggestions", []))

    summary = result.get("summary", "")
    if summary:
        print(f"\n{'='*50}")
        print("  OVERALL SUMMARY")
        print(f"{'='*50}")
        # Wrap at ~80 chars
        words = summary.split()
        line, output = [], []
        for w in words:
            line.append(w)
            if sum(len(x) + 1 for x in line) > 78:
                output.append("  " + " ".join(line[:-1]))
                line = [w]
        if line:
            output.append("  " + " ".join(line))
        print("\n".join(output))
