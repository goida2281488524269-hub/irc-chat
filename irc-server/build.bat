@echo off
cd /d "%~dp0"\src
echo Starting build in %CD%
python -m PyInstaller --onefile server.py
echo Succesfully builded!
echo Exe file in %CD%\dist\
pause