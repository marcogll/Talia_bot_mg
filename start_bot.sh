#!/bin/bash
# Script to start the Talia Bot with correct PYTHONPATH

# Get the directory of the script
DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )"

# Ensure the project root is on PYTHONPATH so absolute imports resolve
export PYTHONPATH="$DIR:${PYTHONPATH}"

# Run the bot using the package entrypoint
python3 -m bot.main
