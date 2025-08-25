#!/bin/bash

cd "$(dirname "$0")"/src
pip install -r requirements.txt
echo "Succesfully installed requirements"
read -p "Press enter to continue"