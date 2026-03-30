def split_task(data):

    # =========================
    # HANDLE INPUT TYPE
    # =========================
    if isinstance(data, dict):
        intent = data.get("intent", "")
    else:
        intent = str(data)

    intent = intent.lower().strip()

    tasks = []

    # =========================
    # CALCULATOR / ADDITION
    # =========================
    if "calculator" in intent or "add" in intent:
        tasks = [
            "create variables for two numbers",
            "add the numbers",
            "print the result"
        ]

    # =========================
    # LOOP
    # =========================
    elif "loop" in intent:
        tasks = [
            "create a loop",
            "print numbers in loop"
        ]

    # =========================
    # FACTORIAL
    # =========================
    elif "factorial" in intent:
        tasks = [
            "take input number",
            "initialize factorial",
            "loop and multiply",
            "print result"
        ]

    # =========================
    # CLASS
    # =========================
    elif "class" in intent:
        tasks = [
            "create a class",
            "create an object",
            "call a method"
        ]

    # =========================
    # DEFAULT (UNKNOWN)
    # =========================
    else:
        tasks = [intent]

    return tasks
