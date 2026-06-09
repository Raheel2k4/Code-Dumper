import os
import sys

# Default extensions to include (can be overridden interactively)
DEFAULT_EXTENSIONS = {".py", ".js", ".html", ".css", ".json", ".md", ".txt", ".yml", ".yaml", ".xml", ".sh", ".bat", ".ps1"}

# Folders to skip
SKIP_DIRS = {".git", "node_modules", "__pycache__", ".venv", "venv", "env", "dist", "build", ".idea", ".vscode"}

def should_skip_dir(dirname):
    return any(skip in dirname.split(os.sep) for skip in SKIP_DIRS)

def is_text_file(filepath):
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            f.read(1024)
        return True
    except (UnicodeDecodeError, IOError):
        return False

def dump_folder(start_path, output_file, extensions):
    with open(output_file, 'w', encoding='utf-8') as out:
        # Write tree structure
        out.write("=== FOLDER STRUCTURE ===\n")
        for root, dirs, files in os.walk(start_path):
            # Skip unwanted directories
            dirs[:] = [d for d in dirs if d not in SKIP_DIRS]
            level = root.replace(start_path, "").count(os.sep)
            indent = "    " * level
            out.write(f"{indent}{os.path.basename(root)}/\n")
            sub_indent = "    " * (level + 1)
            for file in files:
                out.write(f"{sub_indent}{file}\n")
        out.write("\n=== FILE CONTENTS ===\n\n")

        # Write file contents
        for root, dirs, files in os.walk(start_path):
            dirs[:] = [d for d in dirs if d not in SKIP_DIRS]
            for file in files:
                filepath = os.path.join(root, file)
                ext = os.path.splitext(file)[1].lower()
                if extensions and ext not in extensions:
                    continue
                if not is_text_file(filepath):
                    continue
                rel_path = os.path.relpath(filepath, start_path)
                out.write(f"\n{'='*80}\nFILE: {rel_path}\n{'='*80}\n")
                try:
                    with open(filepath, 'r', encoding='utf-8') as f:
                        out.write(f.read())
                except Exception as e:
                    out.write(f"[ERROR reading file: {e}]\n")
                out.write("\n")

    print(f"Dump written to {output_file}")

def get_user_input():
    """Interactively ask for folder path and output file name."""
    # Folder path
    while True:
        folder = input("Enter the folder path to scan (leave empty for current directory): ").strip()
        if not folder:
            folder = os.getcwd()
        if os.path.isdir(folder):
            break
        print(f"Error: '{folder}' is not a valid directory. Please try again.")

    # Output file name
    default_out = "code_dump.txt"
    out_file = input(f"Enter output file name (default: {default_out}): ").strip()
    if not out_file:
        out_file = default_out

    # Optional: ask whether to filter by extensions
    use_filter = input(f"Filter by extensions {DEFAULT_EXTENSIONS}? (y/n, default y): ").strip().lower()
    extensions = DEFAULT_EXTENSIONS if use_filter != 'n' else None

    return folder, out_file, extensions

def main():
    # If command-line arguments are provided, use them (backward compatibility)
    if len(sys.argv) > 1:
        target_folder = sys.argv[1]
        output_file = sys.argv[2] if len(sys.argv) > 2 else "code_dump.txt"
        extensions = DEFAULT_EXTENSIONS
        if not os.path.isdir(target_folder):
            print(f"Error: '{target_folder}' is not a valid directory.")
            sys.exit(1)
    else:
        target_folder, output_file, extensions = get_user_input()

    print(f"Scanning: {target_folder}")
    print(f"Output file: {output_file}")
    if extensions:
        print(f"Including extensions: {', '.join(extensions)}")
    else:
        print("Including all text files (based on content detection)")

    dump_folder(target_folder, output_file, extensions)

if __name__ == "__main__":
    main()
