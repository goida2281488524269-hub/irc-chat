#!/bin/bash

cd "$(dirname "$0")"/src
echo "Starting build in $(pwd)"
python -m PyInstaller --onefile server.py
echo "Succesfully builded!"
echo "File in $(pwd)/dist/"
read -p "Press enter to continue"