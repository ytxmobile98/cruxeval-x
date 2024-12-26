#!/usr/bin/env bash

MODEL_NAME=Qwen2.5-Coder-7B
MODEL_DIR="/data/models"

# LANGS="['java', 'cpp', 'cs', 'd', 'go', 'jl', 'js', 'lua', 'php', 'pl', 'py', 'r', 'rb', 'rkt', 'rs', 'scala', 'sh', 'swift', 'ts']"
# LANGS="['cpp', 'go', 'java', 'js', 'py']"
LANGS="['py']"

python inference/infer_vllm.py \
    --langs "$LANGS" \
    --model_name "$MODEL_NAME" \
    --model_dir "$MODEL_DIR" \
    --tot_data_num 800 \
    --data_root ./datasets/cruxeval-x \
    --data_input_output ./datasets/cruxeval_preprocessed \
    --example_root ./datasets/examples \
    --example_input_output ./datasets/examples_preprocessed \
    --output_dir ./infer_results