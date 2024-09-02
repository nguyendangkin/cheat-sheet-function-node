import os
import sys
import pyperclip
import uuid
import subprocess

REPO_STATE_FILE = '.repo_state'
PENDING_FILES_FILE = '.pending_files'

def get_current_commit_hash():
    try:
        result = subprocess.run(['git', 'rev-parse', 'HEAD'], capture_output=True, text=True, check=True)
        return result.stdout.strip()
    except subprocess.CalledProcessError:
        print("Failed to get current commit hash.")
        return None

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
        try:
            subprocess.run(['git', 'pull'], check=True)
            save_repo_state(current_hash)
        except subprocess.CalledProcessError:
            print("Failed to pull files from the repository.")
            return

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

        try:
            subprocess.run(['git', 'add', file_name], check=True)
            subprocess.run(['git', 'commit', '-m', f'Delete {file_name}'], check=True)
            subprocess.run(['git', 'push'], check=True)
            print(f"File '{file_name}' deletion has been pushed to the repository.")
        except subprocess.CalledProcessError:
            print("Failed to push the deletion to the repository.")

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
        try:
            subprocess.run(['git', 'add', file_name], check=True)
            subprocess.run(['git', 'commit', '-m', f'Add {file_name}'], check=True)
        except subprocess.CalledProcessError:
            print(f"Failed to commit the file {file_name}.")
    
    try:
        subprocess.run(['git', 'push'], check=True)
        print("All pending files have been pushed to the repository.")
        os.remove(PENDING_FILES_FILE)  # Clear the pending files record
    except subprocess.CalledProcessError:
        print("Failed to push files to the repository.")

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
