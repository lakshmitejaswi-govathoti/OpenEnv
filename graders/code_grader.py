def grade_code(output, expected):
    return len(set(output) & set(expected)) / len(expected)