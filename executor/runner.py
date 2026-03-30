def run_code(code):

    print("\n--- Running Program ---\n")

    try:
        exec(code)
    except Exception as error:
        print("\nProgram Error:")
        print(error)

    print("\n--- Program Finished ---\n")
