import re

def search_tool(word):
    mapping = {
        "meeting": "important",
        "win": "spam",
        "sale": "promotions"
    }
    return mapping.get(word, "unknown")

def code_analysis_tool(code):
    issues = []
    if "1/0" in code:
        issues.append("division_by_zero")
    if re.search(r"print\s+\w+", code):
        issues.append("syntax_error")
    return issues