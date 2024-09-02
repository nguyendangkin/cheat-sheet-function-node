@echo off
setlocal enabledelayedexpansion

:: Kiểm tra quyền admin
net session >nul 2>&1
if %errorLevel% neq 0 (
    echo This script requires administrator privileges.
    echo Please run this script as an administrator.
    pause
    exit /b 1
)

:: Cài đặt Python nếu chưa có
where python >nul 2>&1
if %errorLevel% neq 0 (
    echo Python is not installed. Installing Python...
    powershell -Command "Invoke-WebRequest -Uri https://www.python.org/ftp/python/3.9.7/python-3.9.7-amd64.exe -OutFile python-installer.exe"
    python-installer.exe /quiet InstallAllUsers=1 PrependPath=1
    del python-installer.exe
)

:: Cài đặt pyperclip
pip install pyperclip

:: Tạo thư mục trong Program Files
set "install_dir=%ProgramFiles%\notem"
mkdir "%install_dir%" 2>nul

:: Sao chép toàn bộ nội dung thư mục vào thư mục cài đặt
robocopy "%~dp0" "%install_dir%" /E /COPYALL /R:3 /W:5

:: Tạo file batch cho lệnh 'notem'
(
    echo @echo off
    echo python "%install_dir%\notem.py" %%*
) > "%install_dir%\notem.bat"

:: Thêm thư mục vào PATH
for /f "tokens=2*" %%a in ('reg query "HKLM\SYSTEM\CurrentControlSet\Control\Session Manager\Environment" /v Path') do set "current_path=%%b"
setx /M PATH "%current_path%;%install_dir%"

echo Installation completed successfully.
echo Please restart your command prompt to use 'notem' commands.
pause
