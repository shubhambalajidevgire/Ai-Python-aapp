import os

# =========================
# BASE DIRECTORY (USER STORAGE)
# =========================
BASE_DIR = "/storage/emulated/0/AI_Python_App"


# =========================
# INITIALIZE STORAGE
# =========================
def init_storage():
    if not os.path.exists(BASE_DIR):
        os.makedirs(BASE_DIR)


# =========================
# VALIDATE FILENAME
# =========================
def validate_filename(filename):
    filename = filename.strip()

    if not filename:
        return None

    if not filename.endswith(".py"):
        filename += ".py"

    return filename


# =========================
# GET FULL PATH
# =========================
def get_path(filename=None, folder=None):
    if folder:
        folder_path = os.path.join(BASE_DIR, folder)

        if not os.path.exists(folder_path):
            os.makedirs(folder_path)

        if filename:
            return os.path.join(folder_path, filename)

        return folder_path

    if filename:
        return os.path.join(BASE_DIR, filename)

    return BASE_DIR


# =========================
# CREATE FOLDER (PROJECT)
# =========================
def create_folder(folder_name):
    init_storage()

    try:
        path = get_path(folder=folder_name)
        os.makedirs(path, exist_ok=True)
        return True, f"Folder created: {folder_name}"

    except Exception as e:
        return False, str(e)


# =========================
# LIST FILES
# =========================
def list_files(folder=None):
    init_storage()

    try:
        path = get_path(folder=folder)
        files = os.listdir(path)

        return [f for f in files if f.endswith(".py")]

    except Exception:
        return []


# =========================
# LIST FOLDERS
# =========================
def list_folders():
    init_storage()

    try:
        items = os.listdir(BASE_DIR)

        return [
            item for item in items
            if os.path.isdir(os.path.join(BASE_DIR, item))
        ]

    except Exception:
        return []


# =========================
# SAVE FILE
# =========================
def save_file(filename, code, folder=None):
    init_storage()

    filename = validate_filename(filename)

    if not filename:
        return False, "Invalid filename"

    try:
        path = get_path(filename, folder)

        with open(path, "w") as file:
            file.write(code)

        return True, f"Saved: {path}"

    except Exception as e:
        return False, str(e)


# =========================
# LOAD FILE
# =========================
def load_file(filename, folder=None):
    filename = validate_filename(filename)

    if not filename:
        return False, "Invalid filename"

    try:
        path = get_path(filename, folder)

        with open(path, "r") as file:
            return True, file.read()

    except FileNotFoundError:
        return False, "File not found"

    except Exception as e:
        return False, str(e)


# =========================
# DELETE FILE
# =========================
def delete_file(filename, folder=None):
    filename = validate_filename(filename)

    if not filename:
        return False, "Invalid filename"

    try:
        path = get_path(filename, folder)

        if os.path.exists(path):
            os.remove(path)
            return True, "File deleted"

        return False, "File not found"

    except Exception as e:
        return False, str(e)


# =========================
# DELETE FOLDER
# =========================
def delete_folder(folder_name):
    try:
        path = get_path(folder=folder_name)

        if not os.path.exists(path):
            return False, "Folder not found"

        if os.listdir(path):
            return False, "Folder not empty"

        os.rmdir(path)
        return True, "Folder deleted"

    except Exception as e:
        return False, str(e)


# =========================
# FILE EXISTS
# =========================
def file_exists(filename, folder=None):
    filename = validate_filename(filename)

    if not filename:
        return False

    path = get_path(filename, folder)

    return os.path.exists(path)


# =========================
# RENAME FILE
# =========================
def rename_file(old_name, new_name, folder=None):
    old_name = validate_filename(old_name)
    new_name = validate_filename(new_name)

    if not old_name or not new_name:
        return False, "Invalid filename"

    try:
        old_path = get_path(old_name, folder)
        new_path = get_path(new_name, folder)

        if not os.path.exists(old_path):
            return False, "File not found"

        os.rename(old_path, new_path)
        return True, "File renamed"

    except Exception as e:
        return False, str(e)
