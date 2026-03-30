def check_syntax(code):

    try:
        compile(code, "<string>", "exec")
        return True, None

    except SyntaxError as error:
        return False, error
