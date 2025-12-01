# write_setup_and_hook.py
import os
from pathlib import Path

PROJECT_ROOT = Path(__file__).parent
VENV_DIR = PROJECT_ROOT / "venv"
REQ_FILE = PROJECT_ROOT / "requirements.txt"
GIT_HOOKS_DIR = PROJECT_ROOT / ".git" / "hooks"
PRE_COMMIT_HOOK = GIT_HOOKS_DIR / "pre-commit"
GITIGNORE_FILE = PROJECT_ROOT / ".gitignore"

# --- 1. Write setup_venv.py ---
setup_venv_content = f'''\
import os
import sys
import subprocess
from pathlib import Path
import shutil

PROJECT_ROOT = Path(__file__).parent
VENV_DIR = PROJECT_ROOT / "venv"
REQ_FILE = PROJECT_ROOT / "requirements.txt"

CHECK_MODE = "--check" in sys.argv
blocking_errors = 0
warnings = 0

def log_warning(msg):
    global warnings
    warnings += 1
    print(f"[WARNING] {{msg}}")

def log_error(msg):
    global blocking_errors
    blocking_errors += 1
    print(f"[ERROR] {{msg}}")

def remove_old_venv():
    if VENV_DIR.exists():
        try:
            shutil.rmtree(VENV_DIR)
            print(f"Removed existing venv at {{VENV_DIR}}")
        except PermissionError:
            log_error(f"Permission denied removing {{VENV_DIR}}. Close any running Python processes and retry.")
            if CHECK_MODE:
                sys.exit(1)

def create_venv():
    print(f"Creating venv at {{VENV_DIR}}...")
    subprocess.check_call([sys.executable, "-m", "venv", str(VENV_DIR)])

def generate_requirements():
    print("Generating requirements.txt from current venv...")
    pip_path = VENV_DIR / "Scripts" / "pip.exe"
    if not pip_path.exists():
        log_error(f"pip not found at {{pip_path}}")
        if CHECK_MODE:
            sys.exit(1)
    else:
        subprocess.check_call([str(pip_path), "freeze", "--exclude-editable"], stdout=open(REQ_FILE, "w", encoding="utf-8"))
        print(f"requirements.txt written to {{REQ_FILE}}")

def main():
    if CHECK_MODE:
        if not VENV_DIR.exists():
            log_error(f"Virtual environment not found at {{VENV_DIR}}")
        if not REQ_FILE.exists():
            log_error(f"requirements.txt missing at {{REQ_FILE}}")
        print(f"Check complete: {{blocking_errors}} errors, {{warnings}} warnings.")
        sys.exit(1 if blocking_errors > 0 else 0)

    # Normal run: recreate venv
    remove_old_venv()
    create_venv()
    generate_requirements()
    print("Setup complete.")

if __name__ == "__main__":
    main()
'''

setup_venv_path = PROJECT_ROOT / "setup_venv.py"
setup_venv_path.write_text(setup_venv_content, encoding="utf-8")
print(f"Wrote {setup_venv_path}")

# --- 2. Write pre-commit hook ---
GIT_HOOKS_DIR.mkdir(parents=True, exist_ok=True)
pre_commit_content = f'''@echo off
REM Pre-commit hook to check venv and requirements

python "{setup_venv_path}" --check

IF %ERRORLEVEL% NEQ 0 (
    echo.
    echo "Pre-commit check failed. Resolve blocking issues before committing."
    exit /b 1
)
exit /b 0
'''

PRE_COMMIT_HOOK.write_text(pre_commit_content, encoding="utf-8")
# Make it executable (Windows should run .bat content)
os.chmod(PRE_COMMIT_HOOK, 0o755)
print(f"Wrote {PRE_COMMIT_HOOK}")

# --- 3. Update .gitignore for venv ---
gitignore_entry = "\n# Ignore virtual environment\nvenv/\n"
if GITIGNORE_FILE.exists():
    current_content = GITIGNORE_FILE.read_text(encoding="utf-8")
    if "venv/" not in current_content:
        GITIGNORE_FILE.write_text(current_content + gitignore_entry, encoding="utf-8")
        print("Updated .gitignore to include venv/")
else:
    GITIGNORE_FILE.write_text(gitignore_entry, encoding="utf-8")
    print("Created .gitignore with venv/ entry")
