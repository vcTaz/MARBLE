#!/bin/bash

# Define the path to the configuration file (relative to the marble/ directory)
CONFIG_FILE="./configs/test_config_database/gpt-3.5-turbo_E_COMMERCE_FETCH_LARGE_DATA_INSERT_LARGE_DATA.yaml" #config path for the database scenario

# cd to marble directory
cd "$(dirname "$0")/../../marble"

# Execute the simulation engine with the specified configuration
python main.py --config_path "$CONFIG_FILE"
