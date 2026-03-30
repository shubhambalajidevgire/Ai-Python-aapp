class Debugger:

    def __init__(self, memory):
        self.memory = memory

    # =========================
    # SYNTAX CHECK
    # =========================
    def check_syntax(self, code):
        try:
            compile(code, "<string>", "exec")
            return True, None
        except SyntaxError as e:
            return False, str(e)

    # =========================
    # FIND VARIABLES
    # =========================
    def extract_variables(self, code):

        defined = set()
        used = set()

        lines = code.split("\n")

        for line in lines:

            # Detect assignments
            if "=" in line:
                var = line.split("=")[0].strip()
                if var.isidentifier():
                    defined.add(var)

            # Detect usage
            words = line.replace("(", " ").replace(")", " ").split()

            for word in words:
                if word.isidentifier():
                    used.add(word)

        return defined, used

    # =========================
    # FIX UNDEFINED VARIABLES
    # =========================
    def fix_variables(self, code):

        defined, used = self.extract_variables(code)

        missing = used - defined

        fix_lines = []

        for var in missing:
            if var not in ["print", "range", "int", "input"]:
                fix_lines.append(f"{var} = 0")

        if fix_lines:
            code = "\n".join(fix_lines) + "\n" + code

        return code, missing

    # =========================
    # FIX INDENTATION
    # =========================
    def fix_indentation(self, code):

        lines = code.split("\n")
        fixed = []

        for line in lines:

            # Remove random leading spaces
            if not line.startswith("    ") and line.startswith(" "):
                line = line.lstrip()

            fixed.append(line)

        return "\n".join(fixed)

    # =========================
    # MAIN DEBUG FUNCTION
    # =========================
    def debug_code(self):

        code = self.memory.get_current_code()

        if not code:
            return {
                "status": "error",
                "message": "No code to debug"
            }

        messages = []

        # Step 1: Fix indentation
        code = self.fix_indentation(code)

        # Step 2: Fix variables
        code, missing_vars = self.fix_variables(code)

        if missing_vars:
            messages.append(f"Added missing variables: {', '.join(missing_vars)}")

        # Step 3: Syntax check
        valid, error = self.check_syntax(code)

        if valid:
            self.memory.set_code(code)

            return {
                "status": "success",
                "message": " | ".join(messages) if messages else "Code is clean",
                "code": code
            }

        else:
            return {
                "status": "error",
                "message": error,
                "code": code
            }
