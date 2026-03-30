# =========================
# EDITOR MODULE
# =========================

class Editor:

    def __init__(self, memory):
        self.memory = memory

    # =========================
    # SET CODE
    # =========================
    def set_code(self, code):
        self.memory.set_code(code)

        return {
            "status": "success",
            "message": "Code updated",
            "code": code
        }

    # =========================
    # GET CODE
    # =========================
    def get_code(self):
        code = self.memory.get_current_code()

        return {
            "status": "success",
            "code": code
        }

    # =========================
    # APPEND CODE
    # =========================
    def append_code(self, new_code):

        current = self.memory.get_current_code()

        if not current:
            updated = new_code
        else:
            updated = current + "\n" + new_code

        self.memory.set_code(updated)

        return {
            "status": "success",
            "message": "Code appended",
            "code": updated
        }

    # =========================
    # REPLACE LINE
    # =========================
    def replace_line(self, line_no, new_line):

        code = self.memory.get_current_code()

        if not code:
            return {"status": "error", "message": "No code available"}

        lines = code.split("\n")

        if line_no < 1 or line_no > len(lines):
            return {"status": "error", "message": "Invalid line number"}

        lines[line_no - 1] = new_line
        updated = "\n".join(lines)

        self.memory.set_code(updated)

        return {
            "status": "success",
            "message": f"Line {line_no} replaced",
            "code": updated
        }

    # =========================
    # DELETE LINE
    # =========================
    def delete_line(self, line_no):

        code = self.memory.get_current_code()

        if not code:
            return {"status": "error", "message": "No code available"}

        lines = code.split("\n")

        if line_no < 1 or line_no > len(lines):
            return {"status": "error", "message": "Invalid line number"}

        lines.pop(line_no - 1)
        updated = "\n".join(lines)

        self.memory.set_code(updated)

        return {
            "status": "success",
            "message": f"Line {line_no} deleted",
            "code": updated
        }
