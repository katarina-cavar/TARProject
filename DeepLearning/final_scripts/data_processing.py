import numpy as np
import pandas as pd

from textblob import TextBlob
from nltk.tokenize import TweetTokenizer

class DataReader:
    def __init__(self, task_a="../../Dataset-OLID/OLIDv1.0/data_subtask_a.csv"):
        self.task_a = task_a
        
    def get_df_train_data(self):
        train_data = pd.read_csv(self.task_a)
        train_tweets = train_data.drop(["Unnamed: 0", "id", "subtask_a"], axis=1)
        return train_tweets
    
    def get_df_data(self, file="../../Dataset-OLID/OLIDv1.0/data_subtask_a.csv"):
        data = pd.read_csv(file)
        train_tweets = data.drop(["Unnamed: 0", "id", "subtask_a"], axis=1)
        return train_tweets
    
    def get_np_data_and_labels(self, file="../../Dataset-OLID/OLIDv1.0/data_subtask_a.csv"):
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


