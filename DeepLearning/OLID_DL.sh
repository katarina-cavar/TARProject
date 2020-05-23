#!/bin/bash

export CUDA_VISIBLE_DEVICES=-1 #CPU
DATA_FILE="../Dataset-OLID/OLIDv1.0/data_subtask_a.csv"
MODEL_NAME="modelKeras_removeUser_emb128"
MODEL_TYPE='basic_model'
PREPROC="remove_stopwords_and_punctuation_textblob"

VOCAB_SIZE=7500
EMBEDDING_DIM=32
MAX_LENGTH=32
TRUNC_TYPE="post"
PADDING_TYPE="post"
OOV_TOK="<OOV>"
TRAINING_PORTION=0.8
NUM_EPOCHS=20
LSTM_OUT=64
NUM_FILTERS=250
DROPOUT=0.2
KERNEL_SIZE=3
STRIDES=1

python OLID_DL.py $DATA_FILE $MODEL_NAME $MODEL_TYPE $PREPROC \
--vocab_size $VOCAB_SIZE \
--emb_dim $EMBEDDING_DIM \
--max_len $MAX_LENGTH \
--trunc_type $TRUNC_TYPE \
--pad_type $PADDING_TYPE \
--oov_tok $OOV_TOK \
--train_portion $TRAINING_PORTION \
--num_epochs $NUM_EPOCHS \
--lstm_out $LSTM_OUT \
--num_filters $NUM_FILTERS \
--dropout $DROPOUT \
--kernel_size $KERNEL_SIZE \
--strides $STRIDES