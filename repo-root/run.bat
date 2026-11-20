@echo off
cd /d "D:\My Project\9.Apk projects\repo-root"

python -c "import kivy" >nul 2>&1
if errorlevel 1 (
    echo Kivy not found. Installing...
    python -m pip install kivy
    if errorlevel 1 (
        echo Failed to install Kivy.
        pause
        exit /b 1
    )
)

set KIVY_GL_BACKEND=angle_sdl2
python main.py
if errorlevel 1 (
    echo.
    echo Python exited with an error.
    pause
)