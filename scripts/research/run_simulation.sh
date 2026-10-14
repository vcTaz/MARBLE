#!/bin/bash

# Config path for the research scenario. An argument is resolved against the
# current directory; the default is relative to the marble/ directory.
if [ -n "$1" ]; then
    CONFIG_FILE="$(cd "$(dirname "$1")" && pwd)/$(basename "$1")"
else
    CONFIG_FILE="./configs/test_config_research/profile_1.yaml"
fi

# cd to marble directory
cd "$(dirname "$0")/../../marble"

# Execute the simulation engine with the specified configuration
python main.py --config_path "$CONFIG_FILE"
