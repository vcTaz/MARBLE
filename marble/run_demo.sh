#!/bin/bash

# Define the path to the configuration file
CONFIG_FILE="./configs/coding_config/coding_config.yaml"

# cd to marble directory
cd "$(dirname "$0")"

# Execute the simulation engine with the specified configuration
python main.py --config_path "$CONFIG_FILE"
