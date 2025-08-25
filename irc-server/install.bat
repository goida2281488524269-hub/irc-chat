@echo off
cd /d "%~dp0"\src
pip install -r requirements.txt
echo Succesfully installed requirements
pause