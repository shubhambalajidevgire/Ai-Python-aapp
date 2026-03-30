def combine_code(code_blocks):
    """
    Combines multiple code blocks into one final code
    """

    final_lines = []

    for code in code_blocks:
        if not code:
            continue

        lines = code.split("\n")

        for line in lines:
            # Skip empty duplicate lines
            if line.strip() == "":
                continue

            final_lines.append(line)

    # Remove duplicate imports (important)
    unique_lines = []
    seen_imports = set()

    for line in final_lines:
        if line.startswith("import"):
            if line not in seen_imports:
                seen_imports.add(line)
                unique_lines.append(line)
        else:
            unique_lines.append(line)

    return "\n".join(unique_lines)
