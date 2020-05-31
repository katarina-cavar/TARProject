
# Imports

import argparse

import numpy as np
import tensorflow as tf 
from tensorflow.keras.preprocessing.text import Tokenizer
from tensorflow.keras.preprocessing.sequence import pad_sequences
from tensorflow.keras.callbacks import EarlyStopping, ModelCheckpoint
from tensorflow.keras.models import model_from_json, load_model

from new_prints import line_print, title_print

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
	parser.add_argument("data_file", metavar="DATAFILE")
	parser.add_argument("test_file", metavar="TESTFILE")
	parser.add_argument("emb_file", metavar="EMBFILE")
	parser.add_argument("model_name", metavar="MODELNAME")
	parser.add_argument("model_type", metavar="MODEL_TYPE", 
		choices=['basic_model', 'LSTM_model', 'LSTM_model2', 
		'BiLSTM_model', 'BiLSTM_short_model',
		'BiLSTM_moreReg_model', 'BiLSTM_moreReg_model2',
		'BiLSTM_CNN_model', 'CNN_model', 'BiLSTM2_model',
		'BiLSTM2_CNN_model', 'BiLSTM2_CNN3_model', 
		'BiLSTM2_CNN3_short_model', 'BiLSTM2_CNN3_supershort_model'])
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


"""
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


	print("\nTYPES")
	print(type(train_padded), type(train_labels), type(val_padded), type(val_labels))
	print(train_padded.shape, train_labels.shape, val_padded.shape, val_labels.shape)

	return train_padded, train_labels, val_padded, val_labels

"""

def get_embedding_matrix(args, word_index):
	EMB_FILE = args.emb_file
	EMB_DIM = args.emb_dim
	VOCAB_SIZE = args.vocab_size

	embeddings_index = {}
	print(EMB_FILE)

	f = open(EMB_FILE, "r", encoding="utf8")
	lines = f.readlines()
	for line in lines: 
		values = line.split()
		word = values[0]
		coefs = np.asarray(values[1:], dtype="float32")
		embeddings_index[word] = coefs
	f.close()

	print("Found %s word vectors." % len(embeddings_index))

	#embedding_matrix = np.zeros((len(word_index) + 1, EMB_DIM))
	embedding_matrix = np.zeros((VOCAB_SIZE, EMB_DIM))

	print(len(word_index))
	for word, i in word_index.items():
		if i == VOCAB_SIZE: 
			print("Vocab size reached.")
			break
		emb_vector = embeddings_index.get(word)
		if emb_vector is not None:
			embedding_matrix[i] = emb_vector

	return embedding_matrix


def main():

	"""
		Loading Arguments
	"""

	args = get_arguments()

	"""
		Data Reading + Preprocessing 
	"""

	dr = DataReader()
	data, labels = dr.get_np_data_and_labels(args.data_file)
	test_data, test_labels = dr.get_np_data_and_labels(args.test_file)

	pp = Preprocessor()

	if args.preproc == "no_preprocessing":
		proc_data = pp.no_preprocessing(data.copy(), verbose=False)
	elif args.preproc == "remove_punctuation":
		proc_data = pp.remove_punctuation(data.copy(), verbose=False)
	elif args.preproc == "remove_stopwords_and_punctuation":
		proc_data = pp.remove_stopwords_and_punctuation(data.copy(), verbose=False)
	else:
		proc_data = pp.remove_stopwords_and_punctuation_textblob(data.copy(), verbose=False)


	"""
		Tokenize
	"""

	VOCAB_SIZE = args.vocab_size
	MAX_LENGTH = args.max_len
	TRUNC_TYPE = args.trunc_type
	PADDING_TYPE = args.pad_type
	OOV_TOK = args.oov_tok
	TRAINING_PORTION = args.train_portion

	train_number = int(len(proc_data) * TRAINING_PORTION)

	train_msgs = proc_data[:train_number]
	train_labels = labels[:train_number]
	val_msgs = proc_data[train_number:]
	val_labels = labels[train_number:]

	tokenizer = Tokenizer(num_words = VOCAB_SIZE, oov_token = OOV_TOK)
	tokenizer.fit_on_texts(train_msgs)
	word_index = tokenizer.word_index

	print("len(msgs) = {}; len(labels) = {}".format(len(proc_data), len(labels)))
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


	print("\nTYPES")
	print(type(train_padded), type(train_labels), type(val_padded), type(val_labels))
	print(train_padded.shape, train_labels.shape, val_padded.shape, val_labels.shape)


	#train_x, train_y, val_x, val_y = get_train_val(proc_data, labels, args)
	train_x, train_y, val_x, val_y = train_padded, train_labels, val_padded, val_labels

	test_sequences = tokenizer.texts_to_sequences(test_data)
	test_padded = pad_sequences(test_sequences, maxlen=MAX_LENGTH, 
								padding=PADDING_TYPE, truncating=TRUNC_TYPE)

	test_x, test_y = test_padded, test_labels


	"""
		Preparing the Embedding Layer 
		(src: https://blog.keras.io/using-pre-trained-word-embeddings-in-a-keras-model.html)
	"""

	embedding_matrix = get_embedding_matrix(args, tokenizer.word_index)


	"""
		Models
	"""

	if args.model_type == "LSTM_model":
		model = LSTM_model(args, embedding_matrix)
	elif args.model_type == "LSTM_model2":
		model = LSTM_model2(args, embedding_matrix)
	elif args.model_type == "BiLSTM_model":
		model = BiLSTM_model(args, embedding_matrix)
	elif args.model_type == "BiLSTM_short_model":
		model = BiLSTM_short_model(args, embedding_matrix)
	elif args.model_type == "BiLSTM2_model":
		model = BiLSTM2_model(args, embedding_matrix)
	elif args.model_type == "BiLSTM_moreReg_model":
		model = BiLSTM_moreReg_model(args, embedding_matrix)
	elif args.model_type == "BiLSTM_moreReg_model2":
		model = BiLSTM_moreReg_model2(args, embedding_matrix)
	elif args.model_type == "BiLSTM_CNN_model":
		model = BiLSTM_CNN_model(args, embedding_matrix)
	elif args.model_type == "BiLSTM2_CNN_model":
		model = BiLSTM2_CNN_model(args, embedding_matrix)
	elif args.model_type == "BiLSTM2_CNN3_model":
		model = BiLSTM2_CNN3_model(args, embedding_matrix)
	elif args.model_type == "BiLSTM2_CNN3_short_model":
		model = BiLSTM2_CNN3_short_model(args, embedding_matrix)
	elif args.model_type == "BiLSTM2_CNN3_supershort_model":
		model = BiLSTM2_CNN3_supershort_model(args, embedding_matrix)
	else: 
		model = basic_model(args, embedding_matrix)


	title_print(args.model_type)

	adam_optimizer = tf.keras.optimizers.Adam(learning_rate=args.LR)
	model.compile(loss = "binary_crossentropy", optimizer = adam_optimizer, 
		metrics = ["acc", rec, prec, f1])
	model.summary()

	"""
		Callbacks
	"""

	model_name = "{}_type={}_proc={}_epochs={}_emb_dim={}_vocab={}".format(args.model_name, 
		args.model_type, args.preproc, args.num_epochs, args.emb_dim, args.vocab_size)

	callback_list = []

	monitor = "val_f1"
	monitor_mode = "max"
	mc = ModelCheckpoint(filepath="models/" + model_name, verbose=1, save_best_only=True, 
		monitor=monitor, mode=monitor_mode)
	callback_list.append(mc)

	patience = 15

	es = EarlyStopping(monitor=monitor, mode=monitor_mode, patience=patience, verbose=1)
	callback_list.append(es)

	history = model.fit(train_x, train_y,
	         epochs=args.num_epochs, validation_data=(val_x, val_y),
	         callbacks=callback_list, verbose=args.verbose)

	scores = model.evaluate(val_x, val_y)
	#scores = model.evaluate(test_x, test_y)

	print("\nSCORES:")
	print(scores)

	line_print("Arguments:")
	print(args)

	# Save model
	
	"""
	# serialize model to json
	model_json = model.to_json()
	with open("models/" + model_name+".json", "w") as json_file: 
	    json_file.write(model_json)

	# serialize weights to HDF5
	model.save_weights("models/" + model_name+".h5")
	print("\n--> Saved model to disk.")

	line_print("Load model")
	json_file = open("models/" + model_name + ".json", "r")
	loaded_model_json = json_file.read()
	json_file.close()
	model = model_from_json(loaded_model_json)
	model.load_weights("models/" + model_name + ".h5")
	"""

	model = load_model("models/" + model_name, custom_objects={"prec": prec, 
		"rec": rec, "f1": f1})

	model.compile(loss = "binary_crossentropy", optimizer = adam_optimizer, 
		metrics = ["acc", rec, prec, f1])
	

	print("\nScores on val:")
	scores = model.evaluate(val_x, val_y)
	print(scores)

	print("\nScores on test:")
	scores = model.evaluate(test_x, test_y)
	print(scores)





main()