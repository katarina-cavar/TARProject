from nltk.tokenize import TweetTokenizer, RegexpTokenizer
from nltk.corpus import stopwords
import string


class Preprocessor
    # Possible modes
    #   (1) tweet  - only tweet tokenizer
    #   (2) custom - tweet and custom tokenizer
    #   (3) strict - tweet and match tokenizer
    def __init__(self, mode='tweet')
        self.mode = mode

    # preserve_case=False - convert to lowercase
    # strip_handles=True  - strip '@sth'
    # reduce_len=True     - reduce  3 consecutive letters to 3, e.g. 'yeeeees' to 'yeees'
    def tweetTokenizer(self, tweet)
        tweet_tokenizer = TweetTokenizer(preserve_case=False, strip_handles=True, reduce_len=True)
        return tweet_tokenizer.tokenize(tweet)

    # removes everything except word, numbers and '-'
    def matchTokenizer(self, tweet)
        match_tokenizer = RegexpTokenizer([w-]+)
        return match_tokenizer.tokenize(tweet)

    def removeStopwords(self, tweet, remove_dash=False)
        stop_words = set(stopwords.words('english'))
        if remove_dash
            return [word for word in tweet if word not in stop_words and word != '-']
        return [word for word in tweet if word not in stop_words]

    # additional improvements
    def customTokenizer(self, tweet)
        table = str.maketrans(dict.fromkeys(string.punctuation))
        tweet_new = []

        for word in tweet
            if word == '' or word == '..' or word == '...'
                continue
            if len(word) == 1
                if word.translate(table) == ''
                    continue
            if word.startswith('#')
                tweet_new.append(word[1])
                continue
            tweet_new.append(word)

        return tweet_new

    def preprocess(self, tweet)
        tweet = self.tweetTokenizer(tweet)

        if self.mode == 'tweet'
            tweet = self.removeStopwords(tweet)

        elif self.mode == 'custom'
            tweet = self.customTokenizer(tweet)
            tweet = self.removeStopwords(tweet)

        else
            tweet = self.matchTokenizer(' '.join(tweet))
            tweet = self.removeStopwords(tweet, remove_dash=True)

        return tweet
