import sys
import os

sys.path.append(os.path.dirname(os.path.dirname(__file__)))

from ai_engine.splitter import split_task
from ai_engine.generator import generate_from_tasks
from validator.syntax import check_syntax
from executor.runner import run_code

from lessons.engine import load_lesson, show_lesson


def learning_mode():

    lesson = load_lesson("variables.json")
    show_lesson(lesson)


def coding_mode():

    prompt = input("\nAsk AI to create program: ")

    tasks = split_task(prompt)

    print("\nTasks:")
    for t in tasks:
        print("-", t)

    code = generate_from_tasks(tasks)

    print("\nGenerated Code:\n")
    print(code)

    valid, error = check_syntax(code)

    if valid:
        print("\nSyntax OK")
        run_code(code)
    else:
        print("\nSyntax Error:")
        print(error)


def main():

    print("=== AI Python Learning App ===")

    print("\n1 - Learn Python")
    print("2 - AI Code Generator")

    choice = input("\nSelect option: ")

    if choice == "1":
        learning_mode()

    elif choice == "2":
        coding_mode()

    else:
        print("Invalid choice")


if __name__ == "__main__":
    main()
