#!/bin/bash

# cd to the repository root
cd "$(dirname "$0")/../.."

python marble/evaluator/werewolf_evaluator.py \
  --top_level_dir "werewolf_log" \
  --config_path "marble/configs/test_config/werewolf_config/werewolf_config.yaml" \
  --snapshot_folder "placeholder" \
  --base_log_dir "${BASE_LOG_DIR:-path/to/your/output/dir}"
