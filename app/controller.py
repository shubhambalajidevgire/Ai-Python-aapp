# =========================
# CONTROLLER CLASS
# =========================

from database import save_log

class Controller:

    def __init__(self):
        pass

    def process_prompt(self, user_input):

        is_simple = any(word in text for word in simple_keywords)
        text = user_input.lower()

        # Intent detection
        if "loop" in text:
            intent = "loop"
        elif "add" in text or "sum" in text:
            intent = "addition"
        else:
            intent = "unknown"

        if is_simple:
            save_log(user_input, "simple")
        else:
            save_log(user_input, "complex")


        # Generate code
        if intent == "loop":
            code = "for i in range(5):\n    print(i)"
        elif intent == "addition":
            code = "a = 5\nb = 3\nprint(a + b)"
        else:
            code = "# Could not understand request"

        return {
            "status": "success",
            "message": f"Generated code for: {intent}",
            "code": code,
            "tasks": []
        }
