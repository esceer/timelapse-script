#!/bin/bash
cd `dirname $0`
VENV_PYTHON_INTERPRETER=../venv/bin/python3

TIMELAPSE_OUTPUT_DIRECTORY=../timelapse-photos

$VENV_PYTHON_INTERPRETER ../src/timelapse.py `readlink --canonicalize $TIMELAPSE_OUTPUT_DIRECTORY`
