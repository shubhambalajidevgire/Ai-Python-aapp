import re
import json
import os
from difflib import get_close_matches


# =========================
# FILE PATH
# =========================
FILE_PATH = "ai_engine/learned.json"


# =========================
# LOAD & SAVE LEARNING
# =========================
def load_learned():
    if os.path.exists(FILE_PATH):
        with open(FILE_PATH, "r") as f:
            return json.load(f)
    return {}


def save_learned(data):
    with open(FILE_PATH, "w") as f:
        json.dump(data, f)


LEARNED_CORRECTIONS = load_learned()
LAST_UNKNOWN = None


# =========================
# COMMON MISTAKES
# =========================
COMMON_MISTAKES = {
    "lip": "loop",
    "lop": "loop",
    "lopp": "loop",
    "ad": "add",
    "aad": "add",
    "pritn": "print",
    "prnt": "print",
    "mutiply": "multiply",
    "mulitply": "multiply"
}


# =========================
# CLEAN INPUT
# =========================
def clean_prompt(prompt):
    return prompt.lower().strip()


# =========================
# REMOVE FILLER WORDS
# =========================
def remove_filler_words(prompt):
    fillers = [
        "please", "can", "you", "could", "would",
        "the", "a", "an", "to", "for", "me"
    ]

    words = prompt.split()
    filtered = [word for word in words if word not in fillers]

    return " ".join(filtered)


# =========================
# SPELLING CORRECTION
# =========================
def correct_word(word, keywords):

    # Protect important words
    protected_words = ["import"]
    if word in protected_words:
        return word

    # Learned corrections
    if word in LEARNED_CORRECTIONS:
        return LEARNED_CORRECTIONS[word]

    # Common mistakes
    if word in COMMON_MISTAKES:
        return COMMON_MISTAKES[word]

    # Fuzzy match (safe)
    match = get_close_matches(word, keywords, n=1, cutoff=0.5)

    return match[0] if match else word


def correct_prompt(prompt):
    keywords = [
        "add", "sum", "plus",
        "subtract", "minus",
        "multiply", "product",
        "loop", "repeat",
        "print",
        "class",
        "function",
        "even",
        "factorial",
        "list",
        "import"
    ]

    words = prompt.split()
    corrected = [correct_word(word, keywords) for word in words]

    return " ".join(corrected)


# =========================
# EXTRACT NUMBERS
# =========================
def extract_numbers(prompt):
    nums = re.findall(r'\d+', prompt)
    return list(map(int, nums))


# =========================
# EXTRACT LIBRARY
# =========================
def extract_library(prompt):
    words = prompt.split()

    if "import" in words:
        idx = words.index("import")
        if idx + 1 < len(words):
            return words[idx + 1]

    return None


# =========================
# DETECT INTENT
# =========================
def detect_intent(prompt):

    # Priority first
    if "import" in prompt:
        return "import"

    if any(word in prompt for word in ["add", "sum", "plus"]):
        return "addition"

    if any(word in prompt for word in ["subtract", "minus"]):
        return "subtraction"

    if any(word in prompt for word in ["multiply", "product"]):
        return "multiplication"

    if any(word in prompt for word in ["loop", "repeat"]):
        return "loop"

    if "even" in prompt:
        return "even_numbers"

    if "factorial" in prompt:
        return "factorial"

    if "list" in prompt:
        return "list"

    if "print" in prompt:
        return "print"

    if "class" in prompt:
        return "class"

    if "function" in prompt:
        return "function"

    return "unknown"


# =========================
# MAIN PROCESS FUNCTION
# =========================
def process_prompt(user_input):
    global LAST_UNKNOWN

    step1 = clean_prompt(user_input)
    step2 = correct_prompt(step1)
    step3 = remove_filler_words(step2)

    intent = detect_intent(step3)

    # Store unknown input for learning
    if intent == "unknown":
        LAST_UNKNOWN = step1

    data = {
        "intent": intent,
        "numbers": extract_numbers(step3),
        "library": extract_library(step3),
        "cleaned_prompt": step3,
        "raw": user_input
    }

    return data


# =========================
# LEARNING FUNCTION
# =========================
def learn_from_prompt(correct_prompt_text):
    global LAST_UNKNOWN

    if LAST_UNKNOWN:
        wrong_words = LAST_UNKNOWN.split()
        correct_words = correct_prompt_text.lower().split()

        for w in wrong_words:
            for c in correct_words:
                if w != c:
                    LEARNED_CORRECTIONS[w] = c

        save_learned(LEARNED_CORRECTIONS)

        print("✅ Learned:", LEARNED_CORRECTIONS)

        LAST_UNKNOWN = None
