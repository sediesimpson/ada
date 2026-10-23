# The whole world is a dictionary: full path -> file contents.
FILES = {
    "/home/guest/readme.txt": "Deletion scheduled at midnight. Admin keeps the exit code somewhere safe.",
    "/home/guest/.diary": "Admin's password is my dog's name. Rex would be proud.",
    "/admin/exit_code.txt": "7731",
    "/home/guest/notes/todo.txt": "1. Feed Rex\n2. Back up the server"
}

HOME = "/home/guest"

def resolve(path):
    """Turn a relative path like '.diary' into a full one like '/home/guest/.diary'."""
    if path.startswith("/"):
        return path
    return HOME + "/" + path

def ls(path=HOME, all=False):
    """List what's directly inside a folder."""
    folder = resolve(path).rstrip("/") + "/"
    names = set()

    for full_path in FILES:
        if not full_path.startswith(folder):
            continue
        rest = full_path[len(folder):]          # e.g. "readme.txt" or "guest/readme.txt"
        if "/" in rest:
            names.add(rest.split("/")[0] + "/")  # it's inside a subfolder: show the folder
        elif rest.startswith(".") and not all:
            continue                             # hidden file, and we weren't asked for hidden ones
        else:
            names.add(rest)

    if not names:
        return f"ls: {path}: nothing here"
    return "    ".join(sorted(names))

def is_folder(full):
    """A path is a folder if some file lives underneath it."""
    folder = full.rstrip("/") + "/"
    return any(p.startswith(folder) for p in FILES)

def cat(path):
    """Read a file."""
    full = resolve(path)
    if full in FILES:
        return FILES[full]
    if is_folder(full):
        return f"cat: {path}: is a directory"
    return f"cat: {path}: No such file"