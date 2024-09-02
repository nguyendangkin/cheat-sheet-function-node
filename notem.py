import os
import sys
import pyperclip
import uuid
import subprocess

REPO_STATE_FILE = '.repo_state'
PENDING_FILES_FILE = '.pending_files'

def get_git_root():
    current_dir = os.getcwd()
    while current_dir != os.path.dirname(current_dir):  # Until we reach the root
        if os.path.isdir(os.path.join(current_dir, '.git')):
            return current_dir
        current_dir = os.path.dirname(current_dir)
    return None

def run_git_command(args):
    git_root = get_git_root()
    if git_root is None:
        print("Error: .git directory not found.")
        print(f"Current working directory: {os.getcwd()}")
        return None
    os.chdir(git_root)  # Change to the git root directory
    try:
        result = subprocess.run(['git'] + args, capture_output=True, text=True, check=True)
        return result.stdout.strip()
    except subprocess.CalledProcessError:
        print(f"Failed to run git {' '.join(args)}.")
        return None

def get_current_commit_hash():
    return run_git_command(['rev-parse', 'HEAD'])

def load_repo_state():
    if os.path.exists(REPO_STATE_FILE):
        with open(REPO_STATE_FILE, 'r') as f:
            return f.read().strip()
    return None

def save_repo_state(commit_hash):
    with open(REPO_STATE_FILE, 'w') as f:
        f.write(commit_hash)

def load_pending_files():
    if os.path.exists(PENDING_FILES_FILE):
        with open(PENDING_FILES_FILE, 'r') as f:
            return set(f.read().strip().split('\n'))
    return set()

def save_pending_files(pending_files):
    with open(PENDING_FILES_FILE, 'w') as f:
        f.write('\n'.join(pending_files))

def list_files():
    current_hash = get_current_commit_hash()
    if current_hash is None:
        return

    saved_hash = load_repo_state()
    if saved_hash != current_hash:
        if run_git_command(['pull']) is None:
            return
        save_repo_state(current_hash)

    txt_files = [f for f in os.listdir('.') if f.endswith('.txt')]
    if not txt_files:
        print("No .txt files found.")
        return

    for idx, file in enumerate(txt_files, start=1):
        print(f"{idx}. {file}")

def show_file_content(index):
    txt_files = [f for f in os.listdir('.') if f.endswith('.txt')]

    try:
        file_name = txt_files[index - 1]

        with open(file_name, 'r', encoding='utf-8') as file:
            content = file.read()
            print(content)
            pyperclip.copy(content)
            print("Code has been copied to clipboard.")
    except IndexError:
        print(f"No file found at index {index}.")

def create_file_with_code(base_name, code):
    unique_name = f"{base_name}{uuid.uuid4().hex}.txt"

    with open(unique_name, 'w', encoding='utf-8', newline='') as file:
        file.write(code)

    print(f"File '{unique_name}' has been created with the provided code.")

    pending_files = load_pending_files()
    pending_files.add(unique_name)
    save_pending_files(pending_files)

def delete_file(index):
    txt_files = [f for f in os.listdir('.') if f.endswith('.txt')]

    try:
        file_name = txt_files[index - 1]
        os.remove(file_name)
        print(f"File '{file_name}' has been deleted.")

        if run_git_command(['add', file_name]) is None:
            return
        if run_git_command(['commit', '-m', f'Delete {file_name}']) is None:
            return
        if run_git_command(['push']) is None:
            return
        print(f"File '{file_name}' deletion has been pushed to the repository.")

        pending_files = load_pending_files()
        if file_name in pending_files:
            pending_files.remove(file_name)
            save_pending_files(pending_files)

    except IndexError:
        print(f"No file found at index {index}.")
    except FileNotFoundError:
        print(f"File '{file_name}' does not exist.")

def get_code_from_clipboard():
    code = pyperclip.paste()
    return code

def push_pending_files():
    pending_files = load_pending_files()
    if not pending_files:
        print("No pending files to push.")
        return

    for file_name in pending_files:
        if run_git_command(['add', file_name]) is None:
            continue
        if run_git_command(['commit', '-m', f'Add {file_name}']) is None:
            continue
    
    if run_git_command(['push']) is None:
        return
    print("All pending files have been pushed to the repository.")
    os.remove(PENDING_FILES_FILE)  # Clear the pending files record

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: notem.py <command> [index] or notem.py up <name> or notem.py rm <index> or notem.py ups")
    else:
        command = sys.argv[1]

        if command == 'ls':
            list_files()
        elif command.isdigit():
            show_file_content(int(command))
        elif command == 'up' and len(sys.argv) == 3:
            file_name = sys.argv[2]
            code = get_code_from_clipboard()
            if code:
                create_file_with_code(file_name, code)
            else:
                print("Clipboard is empty. Please copy the code before running the command.")
        elif command == 'rm' and len(sys.argv) == 3 and sys.argv[2].isdigit():
            delete_file(int(sys.argv[2]))
        elif command == 'ups':
            push_pending_files()
        else:
            print(f"Unknown command or missing arguments: {command}")