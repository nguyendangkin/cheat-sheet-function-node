import os
import sys
import pyperclip
import uuid
import subprocess

def list_files():
    # Kéo các file mới từ repo GitHub
    try:
        subprocess.run(['git', 'pull'], check=True)
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
    # Tạo tên file với dãy ký tự ngẫu nhiên
    unique_name = f"{base_name}_{uuid.uuid4().hex}.txt"
    
    # Ghi code vào file với mã hóa UTF-8
    with open(unique_name, 'w', encoding='utf-8', newline='') as file:
        file.write(code)
    
    print(f"File '{unique_name}' has been created with the provided code.")
    
    # Commit và push file mới lên repo GitHub
    try:
        subprocess.run(['git', 'add', unique_name], check=True)
        subprocess.run(['git', 'commit', '-m', f'Add {unique_name}'], check=True)
        subprocess.run(['git', 'push'], check=True)
        print(f"File '{unique_name}' has been pushed to the repository.")
    except subprocess.CalledProcessError:
        print("Failed to push the file to the repository.")

def delete_file(index):
    txt_files = [f for f in os.listdir('.') if f.endswith('.txt')]
    
    try:
        file_name = txt_files[index - 1]
        os.remove(file_name)
        print(f"File '{file_name}' has been deleted.")
        
        # Commit và push xóa file lên repo GitHub
        try:
            subprocess.run(['git', 'add', file_name], check=True)
            subprocess.run(['git', 'commit', '-m', f'Delete {file_name}'], check=True)
            subprocess.run(['git', 'push'], check=True)
            print(f"File '{file_name}' deletion has been pushed to the repository.")
        except subprocess.CalledProcessError:
            print("Failed to push the deletion to the repository.")
            
    except IndexError:
        print(f"No file found at index {index}.")
    except FileNotFoundError:
        print(f"File '{file_name}' does not exist.")

def get_code_from_clipboard():
    # Lấy đoạn mã từ clipboard
    code = pyperclip.paste()
    return code

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: notem.py <command> [index] or notem.py up <name> or notem.py rm <index>")
    else:
        command = sys.argv[1]
        
        if command == 'ls':
            list_files()
        elif command.isdigit():
            show_file_content(int(command))
        elif command == 'up' and len(sys.argv) == 3:
            file_name = sys.argv[2]
            # Lấy code từ clipboard
            code = get_code_from_clipboard()
            if code:
                create_file_with_code(file_name, code)
            else:
                print("Clipboard is empty. Please copy the code before running the command.")
        elif command == 'rm' and len(sys.argv) == 3 and sys.argv[2].isdigit():
            delete_file(int(sys.argv[2]))
        else:
            print(f"Unknown command or missing arguments: {command}")
