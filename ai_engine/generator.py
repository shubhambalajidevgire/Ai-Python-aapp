def generate_from_tasks(tasks):

    code = ""

    for task in tasks:

        # =========================
        # CALCULATOR
        # =========================
        if "create variables for two numbers" in task:
            code += "a = 5\nb = 3\n"

        elif "add the numbers" in task:
            code += "result = a + b\n"

        elif "print the result" in task:
            code += 'print("Result:", result)\n'

        # =========================
        # LOOP
        # =========================
        elif "create a loop" in task:
            code += "for i in range(5):\n"

        elif "print numbers in loop" in task:
            code += '    print("Number:", i)\n'

        # =========================
        # FACTORIAL
        # =========================
        elif "take input number" in task:
            code += "n = int(input('Enter number: '))\n"

        elif "initialize factorial" in task:
            code += "fact = 1\n"

        elif "loop and multiply" in task:
            code += "for i in range(1, n+1):\n"
            code += "    fact *= i\n"

        elif "print result" in task:
            code += 'print("Factorial:", fact)\n'

        # =========================
        # CLASS
        # =========================
        elif "create a class" in task:
            code += "class MyClass:\n"
            code += "    def __init__(self):\n"
            code += '        print("Object created")\n\n'

        elif "create an object" in task:
            code += "obj = MyClass()\n"

        elif "call a method" in task:
            code += 'print("Class example executed")\n'

    return code
