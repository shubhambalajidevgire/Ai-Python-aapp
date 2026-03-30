# =========================
# DISPLAY MODULE
# =========================

def show_message(message):
    print("\n=== AI MESSAGE ===")
    print(message)


def show_code(code):
    print("\n=== GENERATED CODE ===")

    lines = code.split("\n")

    for i, line in enumerate(lines, start=1):
        print(f"{i:02d} | {line}")


def show_tasks(tasks):
    print("\n=== TASKS ===")

    for i, task in enumerate(tasks, start=1):
        print(f"{i}. {task}")


def show_error(error):
    print("\n=== ERROR ===")
    print(error)


def show_success(message):
    print("\n=== SUCCESS ===")
    print(message)


# =========================
# MAIN DISPLAY FUNCTION
# =========================
def show_full_response(response):

    status = response.get("status")

    if status == "error":
        show_error(response.get("message"))
        return

    # Show message
    show_message(response.get("message", ""))

    # Show tasks (if present)
    tasks = response.get("tasks")
    if tasks:
        show_tasks(tasks)

    # Show code (if present)
    code = response.get("code")
    if code:
        show_code(code)
