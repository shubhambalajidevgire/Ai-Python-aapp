# =========================
# CONTROLLER CLASS
# =========================

class Controller:

    def __init__(self):
        pass

    def process_prompt(self, user_input):

        text = user_input.lower()

        # Intent detection
        if "loop" in text:
            intent = "loop"
        elif "add" in text or "sum" in text:
            intent = "addition"
        else:
            intent = "unknown"

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
