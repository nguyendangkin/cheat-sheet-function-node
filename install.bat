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

:: Kiểm tra Python
where python >nul 2>&1
if %errorLevel% neq 0 (
    echo Python is not installed. Please download and install Python from:
    echo https://www.python.org/downloads/
    pause
    exit /b 1
)

:: Cài đặt pyperclip nếu Python đã có
echo Installing pyperclip...
pip install pyperclip

:: Tạo thư mục trong thư mục người dùng
set "install_dir=%USERPROFILE%\notem"
if not exist "%install_dir%" (
    mkdir "%install_dir%" 2>nul
)

:: In đường dẫn để kiểm tra
echo Source directory: "%~dp0"
echo Destination directory: "%install_dir%"

:: In danh sách file trong thư mục nguồn
echo Listing files in source directory:
dir /b "%~dp0"

:: Sao chép toàn bộ nội dung thư mục vào thư mục cài đặt bằng xcopy
echo Running xcopy...
xcopy "%~dp0" "%install_dir%" /E /H /I /Y

:: Tạo file batch cho lệnh 'notem'
(
    echo @echo off
    echo python "%install_dir%\notem.py" %%*
) > "%install_dir%\notem.bat"

:: Thêm thư mục vào PATH nếu chưa có
set "batch_path=%install_dir%"
for %%i in ("%PATH:;=";"%") do (
    if "%%~i"=="%batch_path%" set "found_path=true"
)
if not defined found_path (
    echo Adding %install_dir% to PATH...
    setx /M PATH "%PATH%;%install_dir%"
)

echo Installation completed successfully.
echo Please restart your command prompt to use 'notem' commands.
pause
