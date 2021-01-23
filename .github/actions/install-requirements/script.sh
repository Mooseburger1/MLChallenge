#!/bin/bash
# DEFINES
WORKSPACE_FOLDER="$( cd "$( dirname "${BASH_SOURCE[0]}")/.." >/dev/null 2>&1 && pwd )"
PROJECT_NAME="${PWD##*/}"

# -----------------------------------START----------------------------------------


echo "pip install -r $1"
if [[ -f "$1" ]]; then
    pip install -r $1
else
    echo " $1 File not exist"
fi
