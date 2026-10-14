#!/bin/bash

# cd to the repository root
cd "$(dirname "$0")/../.."

python marble/environments/werewolf_env.py \
  --rounds "${ROUNDS:-10}" \
  --name "werewolf_engine_demo" \
  --config_path "marble/configs/test_config/werewolf_config/werewolf_config.yaml"
