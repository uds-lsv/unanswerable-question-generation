#!/bin/bash

# arguments
BS=24
GA_STEPS=2
LR=5e-5
EPOCH=2
SEED=42

MODEL=bert-large-cased

TRAIN_FILE=squad_all.json
VAL_FILE=valid.json

OUTPUT_DIR=checkpoints/

python run_qa.py \
    --model_name_or_path ${MODEL} \
    --output_dir $OUTPUT_DIR  \
    --train_file  ${TRAIN_FILE} \
    --validation_file ${VAL_FILE}  \
    --do_train \
    --do_eval \
    --per_device_train_batch_size $BS \
    --gradient_accumulation_steps ${GA_STEPS}  \
    --learning_rate $LR \
    --num_train_epochs $EPOCH \
    --max_seq_length 384 \
    --doc_stride 128 \
    --version_2_with_negative \
    --save_steps 5000 \
    --seed $SEED  \
    --overwrite_output_dir

