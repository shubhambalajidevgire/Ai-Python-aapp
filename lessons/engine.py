import json


def load_lesson(filename):

    with open("lessons/" + filename, "r") as file:
        lesson = json.load(file)

    return lesson


def show_lesson(lesson):

    print("\n=== Lesson ===")

    print("\nTitle:")
    print(lesson["title"])

    print("\nExplanation:")
    print(lesson["explanation"])

    print("\nExample Code:")
    print(lesson["example"])

    print("\nExercise:")
    print(lesson["exercise"])
