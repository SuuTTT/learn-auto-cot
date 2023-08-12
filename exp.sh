#!/bin/bash
datasets=( "aqua" "addsub" "last_letters" "coin_flip")

for dataset in "${datasets[@]}"; do
    # Step 1: Running the demo
    python run_demo.py \
    --task "$dataset" \
    --pred_file "log/${dataset}_zero_shot_cot.log" \
    --clustering_method hierarchical \
    --demo_save_dir "demos/${dataset}_clustering_method=hierarchical"

    # Step 2: Running the inference
    python run_inference.py \
    --dataset "$dataset" \
    --demo_path "demos/${dataset}_clustering_method=hierarchical" \
    --output_dir "experiment/${dataset}_clustering_method=hierarchical"
done
