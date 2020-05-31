#!/bin/bash

export CUDA_VISIBLE_DEVICES=-1 #CPU
# OLID:
TEST_FILE="../../Dataset-OLID/OLIDv1.0/test_data_subtask_a.csv"

# MTSA: 
#TEST_FILE="../../Dataset-MTSA/tweets_50-50.csv"	

EMB_FILE="../../../0_embeddings/glove.6B/glove.6B.300d.txt" #options: {50,100,200,300}d
MODEL_NAME="saved_models/modelKeras_type=BiLSTM2_CNN3_supershort_model_proc=remove_stopwords_and_punctuation_textblob_epochs=50_emb_dim=300_vocab=7500"
TOKENIZER="tokenizers/tokenizer_maxlen=64.pickle"
PREPROC="remove_stopwords_and_punctuation_textblob"

VOCAB_SIZE=7500
EMBEDDING_DIM=300
MAX_LENGTH=64
TRUNC_TYPE="post"
PADDING_TYPE="post"
OOV_TOK="<OOV>"
TRAINING_PORTION=0.8
NUM_EPOCHS=50
LSTM_OUT=32
NUM_FILTERS=16
DROPOUT=0.5
KERNEL_SIZE=3
STRIDES=1
LEARNING_RATE=0.001 #0.001
VERBOSE=1
POOL_SIZE=2

python test_OLID.py $TEST_FILE $EMB_FILE $MODEL_NAME $TOKENIZER $PREPROC \
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
--strides $STRIDES \
--LR $LEARNING_RATE \
--verbose $VERBOSE \
--pool_size $POOL_SIZE