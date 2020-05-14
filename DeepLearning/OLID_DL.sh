#!/bin/bash

export CUDA_VISIBLE_DEVICES=-1 #CPU
DATA_FILE="../Dataset-OLID/OLIDv1.0/data_subtask_a.csv"
MODEL_NAME="modelKeras_emb128"
MODEL_TYPE="BiLSTM_model"
PREPROC="remove_stopwords_and_punctuation_textblob"

VOCAB_SIZE=2500
EMBEDDING_DIM=128
MAX_LENGTH=64
TRUNC_TYPE="post"
PADDING_TYPE="post"
OOV_TOK="<OOV>"
TRAINING_PORTION=0.8
NUM_EPOCHS=20

python OLID_DL.py $DATA_FILE $MODEL_NAME $MODEL_TYPE $PREPROC \
--vocab_size $VOCAB_SIZE \
--emb_dim $EMBEDDING_DIM \
--max_len $MAX_LENGTH \
--trunc_type $TRUNC_TYPE \
--pad_type $PADDING_TYPE \
--oov_tok $OOV_TOK \
--train_portion $TRAINING_PORTION \
--num_epochs $NUM_EPOCHS