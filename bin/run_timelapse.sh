#!/bin/bash
cd `dirname $0`
VENV_PYTHON_INTERPRETER=../venv/bin/python3

TIMELAPSE_OUTPUT_DIRECTORY=../timelapse-photos

OPTIONAL_RESOLUTION_WIDTH=$1
OPTIONAL_RESOLUTION_HEIGHT=$2

$VENV_PYTHON_INTERPRETER ../src/utils/timelapse.py `readlink --canonicalize $TIMELAPSE_OUTPUT_DIRECTORY` $OPTIONAL_RESOLUTION_WIDTH $OPTIONAL_RESOLUTION_HEIGHT
