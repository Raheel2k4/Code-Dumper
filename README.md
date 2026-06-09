# 📁 Code Dumper

A simple yet powerful **Python script** that recursively walks through a folder, skips binary files and common build/version control directories, and writes **every text/code file** plus the **folder structure** into a single `.txt` file. Perfect for sharing complete codebases with LLMs, performing manual security audits, or creating quick backups of source code.

[![Python 3.6+](https://img.shields.io/badge/python-3.6+-blue.svg)](https://www.python.org/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)

---

## ✨ Features

- ✅ **Interactive prompts** – asks for source folder and output file name (or use command‑line arguments)
- ✅ **Folder tree preview** – writes a clean tree of all files/directories at the top of the output
- ✅ **File content concatenation** – appends the full content of each text/code file, clearly delimited with its path
- ✅ **Smart filtering** – skips binary files (by reading first 1024 bytes) and common unwanted directories (`.git`, `node_modules`, `__pycache__`, `.venv`, `dist`, etc.)
- ✅ **Extension whitelist** – only includes common code extensions: `.py`, `.js`, `.html`, `.css`, `.json`, `.md`, `.txt`, `.yml`, `.yaml`, `.xml`, `.sh`, `.bat`, `.ps1` (optional – you can turn filtering off)
- ✅ **Command‑line or interactive** – use `python dumper.py /path/to/folder out.txt` or just `python dumper.py` and answer the prompts
- ✅ **UTF‑8 encoding** – handles international characters gracefully

---

## 🚀 Usage

### 1. Prerequisites
- Python 3.6 or higher (no external dependencies required)

### 2. Download the script
Save the following code as `code_dumper.py` (or download from the repo).

### 3. Run it

#### Interactive mode (recommended)
```bash
python code_dumper.py
```
You will be asked:
- Folder path (press Enter to use current directory)
- Output file name (default: `code_dump.txt`)
- Filter by extensions? (y/n – default y)

#### Command‑line mode (for scripting)
```bash
python code_dumper.py "C:\my\project" output.txt
```
- The second argument (output file) is optional – defaults to `code_dump.txt`.
- The script still uses the default extension whitelist in this mode.

---

## 📂 Example output
`code_dump.txt` will look like:

```text
=== FOLDER STRUCTURE ===
my_project/
    src/
        main.py
        utils.js
    README.md

=== FILE CONTENTS ===

================================================================================
FILE: src/main.py
================================================================================
print("Hello world")

================================================================================
FILE: src/utils.js
================================================================================
function add(a,b) { return a+b; }

================================================================================
FILE: README.md
================================================================================
# My Project
...
```

---

## ⚙️ Customisation
You can modify the following variables inside the script:

| Variable | Description | Default |
| :--- | :--- | :--- |
| `DEFAULT_EXTENSIONS` | Set of file extensions to include | `.py`, `.js`, `.html`, `.css`, `.json`, `.md`, `.txt`, `.yml`, `.yaml`, `.xml`, `.sh`, `.bat`, `.ps1` |
| `SKIP_DIRS` | Directory names (or parts) to skip entirely | `.git`, `node_modules`, `__pycache__`, `.venv`, `venv`, `env`, `dist`, `build`, `.idea`, `.vscode` |

- To include all text files regardless of extension, answer `n` when prompted *“Filter by extensions?”*.
- The script will then rely solely on the `is_text_file()` heuristic (reads first 1024 bytes as UTF‑8).

---

## 🧪 Use cases

* **Sharing code with LLMs** – paste the entire `code_dump.txt` into a chat context for analysis.
* **Codebase review** – manually search for secrets, hardcoded credentials, or anti‑patterns across many files.
* **Offline backup of source** – create a single, easily searchable snapshot of a project.
* **Documentation generation** – quickly produce a combined text file for documentation tools.

---

## 📄 License
MIT – do whatever you like with it, but please keep the original copyright notice if you redistribute.

---

## 🤝 Contributing
Suggestions and pull requests are welcome! Areas for improvement:
* Add more intelligent binary detection
* Allow excluding specific files via `.gitignore`‑style patterns
* Compress output (e.g., `.zip` or `.gz`) for very large projects

---

Made with ❤️ for developers who need a quick, no‑fuss code dumper.
