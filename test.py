from app.controller import Controller
from app.editor import Editor
from ai_engine.debugger import Debugger
from interface.display import show_full_response

ctrl = Controller()
editor = Editor(ctrl.memory)
debugger = Debugger(ctrl.memory)

# Generate code
response = ctrl.process_prompt("addition")
show_full_response(response)

# Break code manually
editor.replace_line(2, '    print("Updated Number:", i)')

print("\n--- BROKEN CODE ---")
show_full_response({"status": "success", "code": ctrl.memory.get_current_code()})

# Debug it
print("\n--- DEBUGGING ---")
result = debugger.debug_code()
show_full_response(result)
