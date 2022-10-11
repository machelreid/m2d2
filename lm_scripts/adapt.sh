#!/bin/bash
# Parameters
PYTHON=python #path to python executable to use
PATH_TO_TRANSFORMERS= #path to transformers `git clone git@github.com:huggingface/transformers`
TOPDIR= #directory with all domains
GRAD_ACCUM_STEPS= #change to adjust batch size
MAX_STEPS= #Max tuning steps
CACHE_DIR= #set a cache dir, when running on many domains it is advised to place this somewhere with enough storage
LR= #learning rate
MODEL=gpt2 #change for L1 model by specifying path to checkpoint instead of GPT-2
### 
DATA=$TOPDIR/__FILL__

PROGRAM_ARGS=($PATH_TO_TRANSFORMERS/examples/pytorch/language-modeling/run_clm.py --fp16 \
--model_name_or_path $MODEL --per_device_train_batch_size 7 --gradient_accumulation_steps $GRAD_ACCUM_STEPS \
--seed 1234 \
--train_file $DATA/train.txt \
--validation_file $DATA/valid.txt \
--preprocessing_num_workers 60 \
--do_eval \
--do_train \
--warmup_ratio 0.1 \
--eval_steps 1000 \
--evaluation_strategy steps \
--save_strategy steps \
--save_steps 1000 \
--learning_rate $LR \
--max_steps $MAX_STEPS \
--load_best_model_at_end \
--overwrite_output_dir \
--save_total_limit 3 \
--cache_dir $CACHE_DIR \
--output_dir $DATA/models)


$PYTHON  "${PROGRAM_ARGS[@]}"
