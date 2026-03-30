class SessionMemory:

    def __init__(self):
        # 🔹 Current state
        self.current_prompt = None
        self.current_tasks = []
        self.current_code = None
        self.current_file = None

        # 🔹 History
        self.prompts = []
        self.tasks = []
        self.codes = []

        # 🔹 Learning (basic for now)
        self.learned_patterns = {}

    # =========================
    # CURRENT STATE SETTERS
    # =========================
    def set_prompt(self, prompt):
        self.current_prompt = prompt
        self.prompts.append(prompt)

    def set_tasks(self, tasks):
        self.current_tasks = tasks
        self.tasks.extend(tasks)

    def set_code(self, code):
        self.current_code = code
        self.codes.append(code)

    def set_file(self, filename):
        self.current_file = filename

    # =========================
    # GET CURRENT STATE
    # =========================
    def get_current_code(self):
        return self.current_code

    def get_current_prompt(self):
        return self.current_prompt

    def get_current_tasks(self):
        return self.current_tasks

    def get_current_file(self):
        return self.current_file

    # =========================
    # HISTORY
    # =========================
    def get_history(self):
        return {
            "prompts": self.prompts,
            "tasks": self.tasks,
            "codes": self.codes
        }

    # =========================
    # LEARNING SYSTEM (BASIC)
    # =========================
    def learn_pattern(self, wrong, correct):
        self.learned_patterns[wrong] = correct

    def get_learned_pattern(self, word):
        return self.learned_patterns.get(word, None)

    def show_learned_patterns(self):
        print("\n--- Learned Patterns ---")
        for k, v in self.learned_patterns.items():
            print(f"{k} → {v}")

    # =========================
    # CLEAR SESSION
    # =========================
    def clear_current(self):
        self.current_prompt = None
        self.current_tasks = []
        self.current_code = None
        self.current_file = None

    def reset_all(self):
        self.clear_current()
        self.prompts = []
        self.tasks = []
        self.codes = []
        self.learned_patterns = {}

    # =========================
    # DEBUG / DISPLAY
    # =========================
    def show_current(self):
        print("\n--- Current Session ---")
        print("Prompt:", self.current_prompt)
        print("Tasks:", self.current_tasks)
        print("Code:\n", self.current_code)
        print("File:", self.current_file)

    def show_history(self):
        print("\n--- History ---")

        print("\nPrompts:")
        for p in self.prompts:
            print("-", p)

        print("\nTasks:")
        for t in self.tasks:
            print("-", t)

        print("\nCodes:")
        for c in self.codes:
            print(c)
