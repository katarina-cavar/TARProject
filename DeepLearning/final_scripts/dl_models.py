

import tensorflow as tf
from tensorflow.keras.layers import Embedding, GlobalAveragePooling1D, \
Dense, SpatialDropout1D, LSTM, Bidirectional, Dropout, Activation, Conv1D, \
GlobalMaxPooling1D, Input, concatenate
from tensorflow.keras.models import Model


def basic_model(args, embedding_matrix):
	VOCAB_SIZE = args.vocab_size
	EMBEDDING_DIM = args.emb_dim
	MAX_LENGTH = args.max_len
	NUM_EPOCHS = args.num_epochs

	model = tf.keras.Sequential([
		Embedding(VOCAB_SIZE, EMBEDDING_DIM, weights=[embedding_matrix], 
			input_length=MAX_LENGTH),
		GlobalAveragePooling1D(),
		Dense(24, activation="relu"),
		Dense(1, activation="sigmoid")
	])

	return model

def basic_no_emb_model(args, embedding_matrix):
	VOCAB_SIZE = args.vocab_size
	EMBEDDING_DIM = args.emb_dim
	MAX_LENGTH = args.max_len
	NUM_EPOCHS = args.num_epochs

	model = tf.keras.Sequential([
		Embedding(VOCAB_SIZE, EMBEDDING_DIM, 
			input_length=MAX_LENGTH),
		GlobalAveragePooling1D(),
		Dense(24, activation="relu"),
		Dense(1, activation="sigmoid")
	])

	return model

def LSTM_model(args, embedding_matrix):
	# Source: https://www.kaggle.com/ngyptr/lstm-sentiment-analysis-keras
	VOCAB_SIZE = args.vocab_size
	EMBEDDING_DIM = args.emb_dim
	MAX_LENGTH = args.max_len
	NUM_EPOCHS = args.num_epochs
	LSTM_OUT = 32

	model = tf.keras.Sequential([
		Embedding(VOCAB_SIZE, EMBEDDING_DIM, weights=[embedding_matrix], 
			input_length=MAX_LENGTH),
		SpatialDropout1D(0.4),
		LSTM(LSTM_OUT, dropout=0.2, recurrent_dropout=0.2),
		Dense(24, activation="relu"),
		Dense(1, activation="sigmoid")
	])

	return model

def LSTM_model2(args, embedding_matrix):
	VOCAB_SIZE = args.vocab_size
	EMBEDDING_DIM = args.emb_dim
	MAX_LENGTH = args.max_len
	NUM_EPOCHS = args.num_epochs
	LSTM_OUT = 32

	model = tf.keras.Sequential([
		Embedding(VOCAB_SIZE, EMBEDDING_DIM, weights=[embedding_matrix], 
			input_length=MAX_LENGTH),
		LSTM(LSTM_OUT, dropout=0.2, recurrent_dropout=0.2),
		Dense(24, activation="relu"),
		Dense(1, activation="sigmoid")
	])

	return model

def BiLSTM_model(args, embedding_matrix):
	VOCAB_SIZE = args.vocab_size
	EMBEDDING_DIM = args.emb_dim
	MAX_LENGTH = args.max_len
	NUM_EPOCHS = args.num_epochs
	LSTM_OUT = args.lstm_out
	DROPOUT = args.dropout

	model = tf.keras.Sequential([
		Embedding(VOCAB_SIZE, EMBEDDING_DIM, weights=[embedding_matrix], 
			input_length=MAX_LENGTH),
		Dropout(DROPOUT),
		Bidirectional(LSTM(LSTM_OUT)),
		Dense(64, activation="relu"),
		Dense(32, activation="relu"),
		Dense(1, activation="sigmoid")
	])

	return model

def BiLSTM_short_model(args, embedding_matrix):
	VOCAB_SIZE = args.vocab_size
	EMBEDDING_DIM = args.emb_dim
	MAX_LENGTH = args.max_len
	NUM_EPOCHS = args.num_epochs
	LSTM_OUT = args.lstm_out
	DROPOUT = args.dropout

	model = tf.keras.Sequential([
		Embedding(VOCAB_SIZE, EMBEDDING_DIM, weights=[embedding_matrix], 
			input_length=MAX_LENGTH),
		Dropout(DROPOUT),
		Bidirectional(LSTM(LSTM_OUT)),
		Dense(1, activation="sigmoid")
	])

	return model

def BiLSTM_moreReg_model(args, embedding_matrix):
	VOCAB_SIZE = args.vocab_size
	EMBEDDING_DIM = args.emb_dim
	MAX_LENGTH = args.max_len
	NUM_EPOCHS = args.num_epochs
	LSTM_OUT = args.lstm_out
	DROPOUT = args.dropout

	model = tf.keras.Sequential([
		Embedding(VOCAB_SIZE, EMBEDDING_DIM, weights=[embedding_matrix], 
			input_length=MAX_LENGTH),
		Dropout(DROPOUT),
		Bidirectional(LSTM(LSTM_OUT, dropout=0.2, recurrent_dropout=0.2)),
		Dense(64, activation="relu"),
		Dense(32, activation="relu"),
		Dense(1, activation="sigmoid")
	])

	return model

def BiLSTM_moreReg_model2(args, embedding_matrix):
	VOCAB_SIZE = args.vocab_size
	EMBEDDING_DIM = args.emb_dim
	MAX_LENGTH = args.max_len
	NUM_EPOCHS = args.num_epochs
	LSTM_OUT = args.lstm_out
	DROPOUT = args.dropout

	model = tf.keras.Sequential([
		Embedding(VOCAB_SIZE, EMBEDDING_DIM, weights=[embedding_matrix], 
			input_length=MAX_LENGTH),
		Dropout(DROPOUT),
		Bidirectional(LSTM(LSTM_OUT, dropout=0.2, recurrent_dropout=0.2)),
		Dense(64, activation="relu"),
		Dense(32, activation="relu"),
		Dense(1, activation="sigmoid")
	])

	return model

def CNN_model(args, embedding_matrix):
	# Source: https://keras.io/examples/imdb_cnn/
	VOCAB_SIZE = args.vocab_size
	EMBEDDING_DIM = args.emb_dim
	MAX_LENGTH = args.max_len
	NUM_EPOCHS = args.num_epochs
	LSTM_OUT = args.lstm_out
	DROPOUT = args.dropout
	FILTERS = args.num_filters
	KERNEL_SIZE = args.kernel_size
	STRIDES = args.strides

	model = tf.keras.Sequential([
		Embedding(VOCAB_SIZE, EMBEDDING_DIM, weights=[embedding_matrix], input_length=MAX_LENGTH),
		Dropout(DROPOUT),
		Conv1D(FILTERS, KERNEL_SIZE, padding="valid", 
			activation="relu", strides=STRIDES),
		GlobalMaxPooling1D(),
		Dense(250),
		Dropout(DROPOUT),
		Activation("relu"),
		Dense(1, activation="sigmoid")
	])

	return model


def BiLSTM_CNN_model(args, embedding_matrix):
	VOCAB_SIZE = args.vocab_size
	EMBEDDING_DIM = args.emb_dim
	MAX_LENGTH = args.max_len
	NUM_EPOCHS = args.num_epochs
	LSTM_OUT = args.lstm_out
	DROPOUT = args.dropout
	FILTERS = args.num_filters
	KERNEL_SIZE = args.kernel_size
	STRIDES = args.strides

	inp = Input((MAX_LENGTH,))
	emb = Embedding(VOCAB_SIZE, EMBEDDING_DIM, weights=[embedding_matrix], 
		input_length=MAX_LENGTH)(inp)
	emb = Dropout(DROPOUT)(emb)

	conv = Conv1D(FILTERS, KERNEL_SIZE, padding="valid", 
			activation="relu", strides=STRIDES)(emb)
	pool = GlobalMaxPooling1D()(conv)

	lstm = Bidirectional(LSTM(LSTM_OUT, 
		dropout=0.2, recurrent_dropout=0.2))(emb)

	combined = concatenate([pool, lstm])
	dense1 = Dense(128, activation="relu")(combined)
	dense2 = Dense(32, activation="relu")(dense1)
	output = Dense(1, activation="sigmoid")(dense2)


	return Model(inp, output)

def BiLSTM2_model(args, embedding_matrix):
	VOCAB_SIZE = args.vocab_size
	EMBEDDING_DIM = args.emb_dim
	MAX_LENGTH = args.max_len
	NUM_EPOCHS = args.num_epochs
	LSTM_OUT = args.lstm_out
	DROPOUT = args.dropout

	model = tf.keras.Sequential([
		Embedding(VOCAB_SIZE, EMBEDDING_DIM, weights=[embedding_matrix], 
			input_length=MAX_LENGTH),
		Dropout(DROPOUT),
		Bidirectional(LSTM(LSTM_OUT*2, return_sequences=True, dropout=0.2, recurrent_dropout=0.2)),
		Dropout(DROPOUT),
		Bidirectional(LSTM(LSTM_OUT, dropout=0.2, recurrent_dropout=0.2)),
		Dense(64, activation="relu"),
		Dense(32, activation="relu"),
		Dense(1, activation="sigmoid")
	])

	return model



def BiLSTM2_CNN_model(args, embedding_matrix):
	VOCAB_SIZE = args.vocab_size
	EMBEDDING_DIM = args.emb_dim
	MAX_LENGTH = args.max_len
	NUM_EPOCHS = args.num_epochs
	LSTM_OUT = args.lstm_out
	DROPOUT = args.dropout
	FILTERS = args.num_filters
	KERNEL_SIZE = args.kernel_size
	STRIDES = args.strides

	inp = Input((MAX_LENGTH,))
	emb = Embedding(VOCAB_SIZE, EMBEDDING_DIM, weights=[embedding_matrix], 
		input_length=MAX_LENGTH)(inp)
	emb = Dropout(DROPOUT)(emb)
	conv = Conv1D(FILTERS, KERNEL_SIZE, padding="valid", 
			activation="relu", strides=STRIDES)(emb)
	pool = GlobalMaxPooling1D()(conv)

	lstm = Bidirectional(LSTM(LSTM_OUT, return_sequences=True,
		dropout=0.2, recurrent_dropout=0.2))(emb)
	drop = Dropout(DROPOUT)(lstm)
	lstm2 = Bidirectional(LSTM(LSTM_OUT, dropout=0.2, recurrent_dropout=0.2))(drop)

	combined = concatenate([pool, lstm2])
	dense1 = Dense(128, activation="relu")(combined)
	dense2 = Dense(32, activation="relu")(dense1)
	output = Dense(1, activation="sigmoid")(dense2)


	return Model(inp, output)

def BiLSTM2_CNN3_model(args, embedding_matrix):
	VOCAB_SIZE = args.vocab_size
	EMBEDDING_DIM = args.emb_dim
	MAX_LENGTH = args.max_len
	NUM_EPOCHS = args.num_epochs
	LSTM_OUT = args.lstm_out
	DROPOUT = args.dropout
	FILTERS = args.num_filters
	KERNEL_SIZE = args.kernel_size
	STRIDES = args.strides

	inp = Input((MAX_LENGTH,))
	emb = Embedding(VOCAB_SIZE, EMBEDDING_DIM, weights=[embedding_matrix], 
		input_length=MAX_LENGTH)(inp)
	emb = Dropout(DROPOUT)(emb)

	conv1 = Conv1D(FILTERS, KERNEL_SIZE, padding="valid", 
			activation="relu", strides=STRIDES)(emb)
	pool1 = GlobalMaxPooling1D()(conv1)

	conv2 = Conv1D(FILTERS, KERNEL_SIZE+1, padding="valid", 
			activation="relu", strides=STRIDES)(emb)
	pool2 = GlobalMaxPooling1D()(conv2)

	conv3 = Conv1D(FILTERS, KERNEL_SIZE+2, padding="valid", 
			activation="relu", strides=STRIDES)(emb)
	pool3 = GlobalMaxPooling1D()(conv3)



	lstm = Bidirectional(LSTM(LSTM_OUT, return_sequences=True,
		dropout=0.2, recurrent_dropout=0.2))(emb)
	drop = Dropout(DROPOUT)(lstm)
	lstm2 = Bidirectional(LSTM(LSTM_OUT, dropout=0.2, recurrent_dropout=0.2))(drop)

	combined = concatenate([pool1, pool2, pool3, lstm2])
	dense1 = Dense(512, activation="relu")(combined)
	drop1 = Dropout(DROPOUT)(dense1)
	dense2 = Dense(128, activation="relu")(drop1)
	drop2 = Dropout(DROPOUT/2)(dense2)
	dense3 = Dense(32, activation="relu")(drop2)
	output = Dense(1, activation="sigmoid")(dense3)


	return Model(inp, output)

def BiLSTM2_CNN3_short_model(args, embedding_matrix):
	VOCAB_SIZE = args.vocab_size
	EMBEDDING_DIM = args.emb_dim
	MAX_LENGTH = args.max_len
	NUM_EPOCHS = args.num_epochs
	LSTM_OUT = args.lstm_out
	DROPOUT = args.dropout
	FILTERS = args.num_filters
	KERNEL_SIZE = args.kernel_size
	STRIDES = args.strides

	inp = Input((MAX_LENGTH,))
	emb = Embedding(VOCAB_SIZE, EMBEDDING_DIM, weights=[embedding_matrix], 
		input_length=MAX_LENGTH)(inp)
	emb = Dropout(DROPOUT)(emb)

	conv1 = Conv1D(FILTERS, KERNEL_SIZE, padding="valid", 
			activation="relu", strides=STRIDES)(emb)
	pool1 = GlobalMaxPooling1D()(conv1)

	conv2 = Conv1D(FILTERS, KERNEL_SIZE+1, padding="valid", 
			activation="relu", strides=STRIDES)(emb)
	pool2 = GlobalMaxPooling1D()(conv2)

	conv3 = Conv1D(FILTERS, KERNEL_SIZE+2, padding="valid", 
			activation="relu", strides=STRIDES)(emb)
	pool3 = GlobalMaxPooling1D()(conv3)



	lstm = Bidirectional(LSTM(LSTM_OUT, return_sequences=True,
		dropout=0.2, recurrent_dropout=0.2))(emb)
	drop = Dropout(DROPOUT)(lstm)
	lstm2 = Bidirectional(LSTM(LSTM_OUT, dropout=0.2, recurrent_dropout=0.2))(drop)

	combined = concatenate([pool1, pool2, pool3, lstm2])
	drop1 = Dropout(DROPOUT)(combined)
	dense3 = Dense(32, activation="relu")(drop1)
	output = Dense(1, activation="sigmoid")(dense3)


	return Model(inp, output)

def BiLSTM2_CNN3_supershort_model(args, embedding_matrix):
	VOCAB_SIZE = args.vocab_size
	EMBEDDING_DIM = args.emb_dim
	MAX_LENGTH = args.max_len
	NUM_EPOCHS = args.num_epochs
	LSTM_OUT = args.lstm_out
	DROPOUT = args.dropout
	FILTERS = args.num_filters
	KERNEL_SIZE = args.kernel_size
	STRIDES = args.strides
	POOL_SIZE = args.pool_size

	inp = Input((MAX_LENGTH,))
	emb = Embedding(VOCAB_SIZE, EMBEDDING_DIM, weights=[embedding_matrix], 
		input_length=MAX_LENGTH)(inp)
	#emb = Dropout(DROPOUT)(emb)

	conv1 = Conv1D(FILTERS, KERNEL_SIZE, padding="valid", 
			activation="relu", strides=STRIDES)(emb)
	pool1 = GlobalMaxPooling1D()(conv1)

	conv2 = Conv1D(FILTERS, KERNEL_SIZE+1, padding="valid", 
			activation="relu", strides=STRIDES)(emb)
	pool2 = GlobalMaxPooling1D()(conv2)

	conv3 = Conv1D(FILTERS, KERNEL_SIZE+2, padding="valid", 
			activation="relu", strides=STRIDES)(emb)
	pool3 = GlobalMaxPooling1D()(conv3)



	lstm = Bidirectional(LSTM(LSTM_OUT, return_sequences=True,
		dropout=0.2, recurrent_dropout=0.2))(emb)
	drop = Dropout(DROPOUT)(lstm)
	lstm2 = Bidirectional(LSTM(LSTM_OUT, dropout=0.2, recurrent_dropout=0.2))(drop)

	combined = concatenate([pool1, pool2, pool3, lstm2])
	drop1 = Dropout(DROPOUT)(combined)
	#dense3 = Dense(32, activation="relu")(drop1)
	output = Dense(1, activation="sigmoid")(drop1)


	return Model(inp, output)

"""
def BiLSTM2_CNN3_supershort_d_model(args, embedding_matrix):
	VOCAB_SIZE = args.vocab_size
	EMBEDDING_DIM = args.emb_dim
	MAX_LENGTH = args.max_len
	NUM_EPOCHS = args.num_epochs
	LSTM_OUT = args.lstm_out
	DROPOUT = args.dropout
	FILTERS = args.num_filters
	KERNEL_SIZE = args.kernel_size
	STRIDES = args.strides

	inp = Input((MAX_LENGTH,))
	emb = Embedding(VOCAB_SIZE, EMBEDDING_DIM, weights=[embedding_matrix], 
		input_length=MAX_LENGTH)(inp)
	emb = Dropout(DROPOUT)(emb)

	conv1 = Conv1D(FILTERS, KERNEL_SIZE, padding="valid", 
			activation="relu", strides=STRIDES)(emb)
	pool1 = GlobalMaxPooling1D()(conv1)

	conv2 = Conv1D(FILTERS, KERNEL_SIZE+1, padding="valid", 
			activation="relu", strides=STRIDES)(emb)
	pool2 = GlobalMaxPooling1D()(conv2)

	conv3 = Conv1D(FILTERS, KERNEL_SIZE+2, padding="valid", 
			activation="relu", strides=STRIDES)(emb)
	pool3 = GlobalMaxPooling1D()(conv3)



	lstm = Bidirectional(LSTM(LSTM_OUT, return_sequences=True,
		dropout=0.2, recurrent_dropout=0.2))(emb)
	drop = Dropout(DROPOUT)(lstm)
	lstm2 = Bidirectional(LSTM(LSTM_OUT, dropout=0.2, recurrent_dropout=0.2))(drop)

	combined = concatenate([pool1, pool2, pool3, lstm2])
	drop1 = Dropout(DROPOUT)(combined)
	#dense3 = Dense(32, activation="relu")(drop1)
	output = Dense(1, activation="sigmoid")(drop1)


	return Model(inp, output)
"""

def char_cnn_word_blstm(args, embedding_matrix):
	VOCAB_SIZE = args.vocab_size
	EMBEDDING_DIM = args.emb_dim
	MAX_LENGTH = args.max_len
	NUM_EPOCHS = args.num_epochs
	LSTM_OUT = args.lstm_out
	DROPOUT = args.dropout
	FILTERS = args.num_filters
	KERNEL_SIZE = args.kernel_size
	STRIDES = args.strides
	POOL_SIZE = args.pool_size

	inp = Input((MAX_LENGTH,))
	emb = Embedding(VOCAB_SIZE, EMBEDDING_DIM, weights=[embedding_matrix], 
		input_length=MAX_LENGTH)(inp)
	#emb = Dropout(DROPOUT)(emb)

	conv1 = Conv1D(FILTERS, KERNEL_SIZE, padding="valid", 
			activation="relu", strides=STRIDES)(emb)
	pool1 = GlobalMaxPooling1D()(conv1)

	conv2 = Conv1D(FILTERS, KERNEL_SIZE+1, padding="valid", 
			activation="relu", strides=STRIDES)(emb)
	pool2 = GlobalMaxPooling1D()(conv2)

	conv3 = Conv1D(FILTERS, KERNEL_SIZE+2, padding="valid", 
			activation="relu", strides=STRIDES)(emb)
	pool3 = GlobalMaxPooling1D()(conv3)



	lstm = Bidirectional(LSTM(LSTM_OUT, return_sequences=True,
		dropout=0.2, recurrent_dropout=0.2))(emb)
	drop = Dropout(DROPOUT)(lstm)
	lstm2 = Bidirectional(LSTM(LSTM_OUT, dropout=0.2, recurrent_dropout=0.2))(drop)

	combined = concatenate([pool1, pool2, pool3, lstm2])
	drop1 = Dropout(DROPOUT)(combined)
	#dense3 = Dense(32, activation="relu")(drop1)
	output = Dense(1, activation="sigmoid")(drop1)


	return Model(inp, output)