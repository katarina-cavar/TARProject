
# Imports

import argparse

import numpy as np
import tensorflow as tf 
from tensorflow.keras.preprocessing.text import Tokenizer
from tensorflow.keras.preprocessing.sequence import pad_sequences
from tensorflow.keras.callbacks import EarlyStopping, ModelCheckpoint
from tensorflow.keras.models import model_from_json, load_model

from new_prints import line_print, title_print
import pickle

import nltk
nltk.download("stopwords")

#import gensim
#from gensim.models import Word2Vec 

from data_processing import DataReader, Preprocessor, rec, prec, f1
from dl_models import basic_model, LSTM_model, LSTM_model2, BiLSTM_model, \
BiLSTM_moreReg_model, BiLSTM_moreReg_model2, CNN_model, BiLSTM_CNN_model, BiLSTM2_model, \
BiLSTM2_CNN_model, BiLSTM2_CNN3_model, BiLSTM_short_model, BiLSTM2_CNN3_short_model, \
BiLSTM2_CNN3_supershort_model


def get_arguments():
	parser = argparse.ArgumentParser(description="Train a new model for OLID")
	#parser.add_argument("data_file", metavar="DATAFILE")
	parser.add_argument("test_file", metavar="TESTFILE")
	parser.add_argument("emb_file", metavar="EMBFILE")
	parser.add_argument("model_name", metavar="MODELNAME")
	parser.add_argument("tokenizer_file", metavar="TOKENIZERFILE")
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
	parser.add_argument(
	    "--LR",
	    default=None,
	    type=float,
	    required=True,
	)
	parser.add_argument(
	    "--verbose",
	    default=1,
	    type=int,
	    required=True,
	)
	parser.add_argument(
	    "--pool_size",
	    default=2,
	    type=int,
	    required=True,
	)
	args = parser.parse_args()

	return args


def main():

	"""
		Loading Arguments
	"""

	args = get_arguments()

	title_print(args.test_file)

	"""
		Data Reading + Preprocessing 
	"""

	dr = DataReader()
	test_data, test_labels = dr.get_np_data_and_labels(args.test_file)

	print("\n\n\n")
	print(type(test_data), type(test_labels))
	print(test_data.shape, test_labels.shape)
	print(type(test_data[0]), type(test_labels[0]))
	print(test_data.encode('utf-8'),test_labels)
	print("\n\n\n")

	pp = Preprocessor()

	if args.preproc == "no_preprocessing":
		proc_data = pp.no_preprocessing(test_data.copy(), verbose=False)
	elif args.preproc == "remove_punctuation":
		proc_data = pp.remove_punctuation(test_data.copy(), verbose=False)
	elif args.preproc == "remove_stopwords_and_punctuation":
		proc_data = pp.remove_stopwords_and_punctuation(test_data.copy(), verbose=False)
	else:
		proc_data = pp.remove_stopwords_and_punctuation_textblob(test_data.copy(), verbose=False)


	"""
		Tokenize
	"""

	VOCAB_SIZE = args.vocab_size
	MAX_LENGTH = args.max_len
	TRUNC_TYPE = args.trunc_type
	PADDING_TYPE = args.pad_type
	OOV_TOK = args.oov_tok

	handle = open(args.tokenizer_file, "rb")
	tokenizer = pickle.load(handle)
	handle.close()

	test_sequences = tokenizer.texts_to_sequences(test_data)
	test_padded = pad_sequences(test_sequences, maxlen=MAX_LENGTH, 
								padding=PADDING_TYPE, truncating=TRUNC_TYPE)


	no_proc_test_sequences = tokenizer.texts_to_sequences(proc_data)
	no_proc_test_padded = pad_sequences(no_proc_test_sequences, maxlen=MAX_LENGTH, 
								padding=PADDING_TYPE, truncating=TRUNC_TYPE)

	test_x, test_y = test_padded, test_labels
	no_proc_test_x, no_proc_test_y = no_proc_test_padded, test_labels

	"""
		Models
	"""

	model = load_model(args.model_name, custom_objects={"prec": prec, 
		"rec": rec, "f1": f1})
	model.summary()

	adam_optimizer = tf.keras.optimizers.Adam(learning_rate=args.LR)
	model.compile(loss = "binary_crossentropy", optimizer = adam_optimizer, 
		metrics = ["acc", rec, prec, f1])

	line_print(args.model_name)


	print("\nScores on test:")
	scores = model.evaluate(test_x, test_y)
	print(scores)

	print("\nScores on no proc test:")
	scores = model.evaluate(no_proc_test_x, no_proc_test_y)
	print(scores)

	"""

	y_pred = model.predict(no_proc_test_x)
	line_print("y_pred")
	#print(y_pred[:50])

	for i in range(len(y_pred)):
		#print(y_pred[i][0])
		if (y_pred[i][0] > 0.9):
			print("-> NEG 1 -> {} true - ({:.3f}):\n\t  {}".format(test_labels[i], 
			y_pred[i][0],  test_data[i].encode('utf-8'))) #.encode('utf-8'))
		if (y_pred[i][0] < 0.1):
			print("-> POS 0 -> {} true - ({:.3f}):\n\t {}".format(test_labels[i], 
			y_pred[i][0], test_data[i].encode('utf-8'))) #.encode('utf-8'))


	line_print("y_true")
	#print(no_proc_test_y[:50])
	"""


main()