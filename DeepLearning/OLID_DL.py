
# Imports

import numpy as np
import pandas as pd
import csv
from tqdm import tqdm
from sklearn.utils import shuffle
import argparse

import random
from textblob import TextBlob
from nltk.tokenize import TweetTokenizer

import tensorflow as tf 
from tensorflow.keras.preprocessing.text import Tokenizer
from tensorflow.keras.preprocessing.sequence import pad_sequences

import nltk
nltk.download("stopwords")


class DataReader:
    def __init__(self, task_a="../Dataset-OLID/OLIDv1.0/data_subtask_a.csv"):
        self.task_a = task_a
        
    def get_df_train_data(self):
        train_data = pd.read_csv(self.task_a)
        train_tweets = train_data.drop(["Unnamed: 0", "id", "subtask_a"], axis=1)
        return train_tweets
    
    def get_df_data(self, file="../Dataset-OLID/OLIDv1.0/data_subtask_a.csv"):
        data = pd.read_csv(file)
        train_tweets = data.drop(["Unnamed: 0", "id", "subtask_a"], axis=1)
        return train_tweets
    
    def get_np_data_and_labels(self, file="../Dataset-OLID/OLIDv1.0/data_subtask_a.csv"):
        tweets = self.get_df_data(file)
        data, labels = tweets.values[:,0], tweets.values[:,1]
        return data, labels
    
    # this creates copies
    def shuffle_np(self, data, labels):
        assert len(data) == len(labels)
        p = np.random.permutation(len(data))
        return data[p], labels[p]


class Preprocessor:

	def no_preprocessing(self, data, verbose=False):
		return data

	def remove_punctuation(self, data, verbose=False):
		for i in range(len(data)):
			if verbose:
				print(data[i])
            
			# Remove punctuation
			sentence_blob = TextBlob(data[i])
			sentence = " ".join(sentence_blob.words)
			data[i] = sentence
		return data
    
	def remove_stopwords_and_punctuation(self, data, verbose = False):
		from nltk.corpus import stopwords
		import re

		stop = stopwords.words("english")
		stop.append("’")
		stop.append("@user")

		tknzr = TweetTokenizer()

		if verbose:
			print(type(stop))
			print(stop)
		for i in range(len(data)):
			if verbose:
				print(data[i])

			# Remove punctuation
			#sentence_blob = TextBlob(data[i])
			sentence_blob = tknzr.tokenize(data[i])
			#print("Blob: ", sentence_blob)
			sentence = " ".join(sentence_blob) #.words)
			#print(sentence)
			words = sentence.split()
			#words = data[i].split()

			#Remove stopwords
			if verbose:
				print(words)
			clean_words = []

			for word in words:
				word = word.strip().lower()
				if verbose:
					print(word)
				if word not in stop: 
					clean_words.append(word)
				else: 
					if verbose:
						print("Remove: ", word)

			data[i] = " ".join(clean_words)
			if verbose:
				print(data[i])
				print("-"*20)
		return data

	def remove_stopwords_and_punctuation_textblob(self, data, verbose = False):
	    from nltk.corpus import stopwords
	    import re

	    stop = stopwords.words("english")
	    stop.append("’")
	    stop.append("user")
	    
	    if verbose:
	        print(type(stop))
	        print(stop)
	    for i in range(len(data)):
	        if verbose:
	            print(data[i])
	        
	        # Remove punctuation
	        sentence_blob = TextBlob(data[i])
	        sentence = " ".join(sentence_blob.words)
	        #print(sentence)
	        words = sentence.split()
	        
	        #Remove stopwords
	        if verbose:
	            print(words)
	        clean_words = []
	        
	        for word in words:
	            word = word.strip().lower()
	            if verbose:
	                print(word)
	            if word not in stop: 
	                clean_words.append(word)
	            else: 
	                if verbose:
	                    print("Remove: ", word)
	        
	        data[i] = " ".join(clean_words)
	        if verbose:
	            print(data[i])
	            print("-"*20)
	    return data

def get_train_val(messages, labels, args):

	VOCAB_SIZE = args.vocab_size
	MAX_LENGTH = args.max_len
	TRUNC_TYPE = args.trunc_type
	PADDING_TYPE = args.pad_type
	OOV_TOK = args.oov_tok
	TRAINING_PORTION = args.train_portion

	train_number = int(len(messages) * TRAINING_PORTION)

	train_msgs = messages[:train_number]
	train_labels = labels[:train_number]
	val_msgs = messages[train_number:]
	val_labels = labels[train_number:]

	tokenizer = Tokenizer(num_words = VOCAB_SIZE, oov_token = OOV_TOK)
	tokenizer.fit_on_texts(train_msgs)
	word_index = tokenizer.word_index

	print("len(msgs) = {}; len(labels) = {}".format(len(messages), len(labels)))
	print("TRAIN: len(x) = {}; len(y) = {}".format(len(train_msgs),len(train_labels)))
	print("TEST: len(x) = {}; len(y) = {}".format(len(val_msgs),len(val_labels)))


	print("\nlen(word_index) = {}\n".format(len(word_index))) 
	# Total number of words without stopwords = 8029
	#print(word_index)

	train_sequences = tokenizer.texts_to_sequences(train_msgs)
	train_padded = pad_sequences(train_sequences, maxlen = MAX_LENGTH, 
	                            padding = PADDING_TYPE, truncating = TRUNC_TYPE)

	val_sequences = tokenizer.texts_to_sequences(val_msgs)
	val_padded = pad_sequences(val_sequences, maxlen = MAX_LENGTH, 
	                            padding = PADDING_TYPE, truncating = TRUNC_TYPE)

	print(type(val_padded))

	return train_padded, train_labels, val_padded, val_labels

def basic_model(args):
	VOCAB_SIZE = args.vocab_size
	EMBEDDING_DIM = args.emb_dim
	MAX_LENGTH = args.max_len
	NUM_EPOCHS = args.num_epochs

	model = tf.keras.Sequential([
		tf.keras.layers.Embedding(VOCAB_SIZE, EMBEDDING_DIM, input_length=MAX_LENGTH),
		tf.keras.layers.GlobalAveragePooling1D(),
		tf.keras.layers.Dense(24, activation="relu"),
		tf.keras.layers.Dense(1, activation="sigmoid")
	])

	return model

def LSTM_model(args):
	# Source: https://www.kaggle.com/ngyptr/lstm-sentiment-analysis-keras
	VOCAB_SIZE = args.vocab_size
	EMBEDDING_DIM = args.emb_dim
	MAX_LENGTH = args.max_len
	NUM_EPOCHS = args.num_epochs
	LSTM_OUT = 32

	model = tf.keras.Sequential([
		tf.keras.layers.Embedding(VOCAB_SIZE, EMBEDDING_DIM, input_length=MAX_LENGTH),
		tf.keras.layers.SpatialDropout1D(0.4),
		tf.keras.layers.LSTM(LSTM_OUT, dropout=0.2, recurrent_dropout=0.2),
		tf.keras.layers.Dense(24, activation="relu"),
		tf.keras.layers.Dense(1, activation="sigmoid")
	])

	return model

def LSTM_model2(args):
	VOCAB_SIZE = args.vocab_size
	EMBEDDING_DIM = args.emb_dim
	MAX_LENGTH = args.max_len
	NUM_EPOCHS = args.num_epochs
	LSTM_OUT = 32

	model = tf.keras.Sequential([
		tf.keras.layers.Embedding(VOCAB_SIZE, EMBEDDING_DIM, input_length=MAX_LENGTH),
		tf.keras.layers.LSTM(LSTM_OUT, dropout=0.2, recurrent_dropout=0.2),
		tf.keras.layers.Dense(24, activation="relu"),
		tf.keras.layers.Dense(1, activation="sigmoid")
	])

	return model

def BiLSTM_model(args):
	VOCAB_SIZE = args.vocab_size
	EMBEDDING_DIM = args.emb_dim
	MAX_LENGTH = args.max_len
	NUM_EPOCHS = args.num_epochs
	LSTM_OUT = args.lstm_out
	DROPOUT = args.dropout

	model = tf.keras.Sequential([
		tf.keras.layers.Embedding(VOCAB_SIZE, EMBEDDING_DIM, input_length=MAX_LENGTH),
		tf.keras.layers.Dropout(DROPOUT),
		tf.keras.layers.Bidirectional(tf.keras.layers.LSTM(LSTM_OUT)),
		tf.keras.layers.Dense(64, activation="relu"),
		tf.keras.layers.Dense(32, activation="relu"),
		tf.keras.layers.Dense(1, activation="sigmoid")
	])

	return model

def BiLSTM_moreReg_model(args):
	VOCAB_SIZE = args.vocab_size
	EMBEDDING_DIM = args.emb_dim
	MAX_LENGTH = args.max_len
	NUM_EPOCHS = args.num_epochs
	LSTM_OUT = args.lstm_out
	DROPOUT = args.dropout

	model = tf.keras.Sequential([
		tf.keras.layers.Embedding(VOCAB_SIZE, EMBEDDING_DIM, input_length=MAX_LENGTH),
		tf.keras.layers.Dropout(DROPOUT),
		tf.keras.layers.Bidirectional(tf.keras.layers.LSTM(LSTM_OUT, dropout=0.2, recurrent_dropout=0.2)),
		tf.keras.layers.Dense(64, activation="relu"),
		tf.keras.layers.Dense(32, activation="relu"),
		tf.keras.layers.Dense(1, activation="sigmoid")
	])

	return model

def BiLSTM_moreReg_model2(args):
	VOCAB_SIZE = args.vocab_size
	EMBEDDING_DIM = args.emb_dim
	MAX_LENGTH = args.max_len
	NUM_EPOCHS = args.num_epochs
	LSTM_OUT = args.lstm_out
	DROPOUT = args.dropout

	model = tf.keras.Sequential([
		tf.keras.layers.Embedding(VOCAB_SIZE, EMBEDDING_DIM, input_length=MAX_LENGTH),
		tf.keras.layers.Dropout(DROPOUT),
		tf.keras.layers.Bidirectional(tf.keras.layers.LSTM(LSTM_OUT, dropout=0.2, recurrent_dropout=0.2)),
		tf.keras.layers.Dense(64, activation="relu"),
		tf.keras.layers.Dense(32, activation="relu"),
		tf.keras.layers.Dense(1, activation="sigmoid")
	])

	return model

def CNN_model(args):
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
		tf.keras.layers.Embedding(VOCAB_SIZE, EMBEDDING_DIM, input_length=MAX_LENGTH),
		tf.keras.layers.Dropout(DROPOUT),
		tf.keras.layers.Conv1D(FILTERS, KERNEL_SIZE, padding="valid", 
			activation="relu", strides=STRIDES),
		tf.keras.layers.GlobalMaxPooling1D(),
		tf.keras.layers.Dense(250),
		tf.keras.layers.Dropout(DROPOUT),
		tf.keras.layers.Activation("relu"),
		tf.keras.layers.Dense(1, activation="sigmoid")
	])

	return model

# Not finished
def BiLSTM_CNN_model(args):
	VOCAB_SIZE = args.vocab_size
	EMBEDDING_DIM = args.emb_dim
	MAX_LENGTH = args.max_len
	NUM_EPOCHS = args.num_epochs
	LSTM_OUT = args.lstm_out
	DROPOUT = args.dropout
	FILTERS = args.num_filters
	KERNEL_SIZE = args.kernel_size
	STRIDES = args.strides

	inp = tf.keras.layers.Input((MAX_LENGTH,))
	emb = tf.keras.layers.Embedding(VOCAB_SIZE, EMBEDDING_DIM, input_length=MAX_LENGTH)(inp)
	emb = tf.keras.layers.Dropout(DROPOUT)(emb)

	conv = tf.keras.layers.Conv1D(FILTERS, KERNEL_SIZE, padding="valid", 
			activation="relu", strides=STRIDES)(emb)
	pool = tf.keras.layers.GlobalMaxPooling1D()(conv)

	lstm = tf.keras.layers.Bidirectional(tf.keras.layers.LSTM(LSTM_OUT, 
		dropout=0.2, recurrent_dropout=0.2))(emb)

	combined = tf.keras.layers.concatenate([pool, lstm])
	dense1 = tf.keras.layers.Dense(128, activation="relu")(combined)
	dense2 = tf.keras.layers.Dense(32, activation="relu")(dense1)
	output = tf.keras.layers.Dense(1, activation="sigmoid")(dense2)


	return tf.keras.models.Model(inp, output)


def main():
	parser = argparse.ArgumentParser(description="Train a new model for OLID")
	parser.add_argument("data_file", metavar="DATAFILE")
	parser.add_argument("model_name", metavar="MODELNAME")
	parser.add_argument("model_type", metavar="MODEL_TYPE", 
		choices=['basic_model', 'LSTM_model', 'LSTM_model2', 'BiLSTM_model',
		'BiLSTM_moreReg_model', 'BiLSTM_moreReg_model2',
		'BiLSTM_CNN_model', 'CNN_model'])
	parser.add_argument("preproc", metavar="PREPROCESSING", 
		choices=['no_preprocessing', 'remove_punctuation', 
		'remove_stopwords_and_punctuation', 
		'remove_stopwords_and_punctuation_textblob'])
	
	parser.add_argument(
	    "--vocab_size",
	    default=None,
	    type=int,
	    required=True,
	)
	parser.add_argument(
	    "--emb_dim",
	    default=None,
	    type=int,
	    required=True,
	)
	parser.add_argument(
	    "--max_len",
	    default=None,
	    type=int,
	    required=True,
	)
	parser.add_argument(
	    "--trunc_type",
	    default=None,
	    type=str,
	    required=True,
	)
	parser.add_argument(
	    "--pad_type",
	    default=None,
	    type=str,
	    required=True,
	)
	parser.add_argument(
	    "--oov_tok",
	    default=None,
	    type=str,
	    required=True,
	)
	parser.add_argument(
	    "--train_portion",
	    default=None,
	    type=float,
	    required=True,
	)
	parser.add_argument(
	    "--num_epochs",
	    default=None,
	    type=int,
	    required=True,
	)
	parser.add_argument(
	    "--lstm_out",
	    default=None,
	    type=int,
	    required=True,
	)
	parser.add_argument(
	    "--num_filters",
	    default=None,
	    type=int,
	    required=True,
	)
	parser.add_argument(
	    "--dropout",
	    default=None,
	    type=float,
	    required=True,
	)
	parser.add_argument(
	    "--kernel_size",
	    default=None,
	    type=int,
	    required=True,
	)
	parser.add_argument(
	    "--strides",
	    default=None,
	    type=int,
	    required=True,
	)
	args = parser.parse_args()

	dr = DataReader()
	data, labels = dr.get_np_data_and_labels(args.data_file)

	pp = Preprocessor()

	if args.preproc == "no_preprocessing":
		proc_data = pp.no_preprocessing(data.copy(), verbose=False)
	elif args.preproc == "remove_punctuation":
		proc_data = pp.remove_punctuation(data.copy(), verbose=False)
	elif args.preproc == "remove_stopwords_and_punctuation":
		proc_data = pp.remove_stopwords_and_punctuation(data.copy(), verbose=False)
	else:
		proc_data = pp.remove_stopwords_and_punctuation_textblob(data.copy(), verbose=False)


	train_x, train_y, val_x, val_y = get_train_val(proc_data, labels, args)

	if args.model_type == "LSTM_model":
		model = LSTM_model(args)
	elif args.model_type == "LSTM_model2":
		model = LSTM_model2(args)
	elif args.model_type == "BiLSTM_model":
		model = BiLSTM_model(args)
	elif args.model_type == "BiLSTM_moreReg_model":
		model = BiLSTM_moreReg_model(args)
	elif args.model_type == "BiLSTM_moreReg_model2":
		model = BiLSTM_moreReg_model2(args)
	elif args.model_type == "BiLSTM_CNN_model":
		model = BiLSTM_CNN_model(args)
	else: 
		model = basic_model(args)

	model.compile(loss = "binary_crossentropy", optimizer = "adam", metrics = ["acc"])
	model.summary()

	history = model.fit(train_x, train_y,
	         epochs=args.num_epochs, validation_data=(val_x, val_y))

	scores = model.evaluate(val_x, val_y)

	print("\nSCORES:")
	print(scores)

	# Save model
	model_name = "{}_type={}_proc={}_epochs={}_emb_dim={}_vocab={}".format(args.model_name, 
		args.model_type, args.preproc, args.num_epochs, args.emb_dim, args.vocab_size)

	# serialize model to json
	model_json = model.to_json()
	with open("models/" + model_name+".json", "w") as json_file: 
	    json_file.write(model_json)

	# serialize weights to HDF5
	model.save_weights("models/" + model_name+".h5")
	print("\n--> Saved model to disk.")

	print(args)

main()