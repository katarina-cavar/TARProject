from nltk.tokenize import TweetTokenizer
from nltk.corpus import stopwords
import string


def tweetTokenizer(tweet):
    # preserve_case=False -> convert to lowercase
    # strip_handles=True  -> strip '@sth'
    # reduce_len=True     -> reduce > 3 consecutive letters to 3, e.g. 'yeeeees' to 'yeees'
    tweet_tokenizer = TweetTokenizer(preserve_case=False, strip_handles=True, reduce_len=True)
    return tweet_tokenizer.tokenize(tweet)


def customTokenizer(tweet):
    table = str.maketrans(dict.fromkeys(string.punctuation))
    tweet_new = []

    for word in tweet:
        if word == '' or word == '?' or word == '?' or word == '..' or word == '...':
            continue
        if len(word) == 1:
            if word.translate(table) == '':
                continue
        if word.startswith('#'):
            tweet_new.append(word[1:])
            continue
        tweet_new.append(word)

    return tweet_new


def main():
    with open('/home/sanja/Desktop/TARProject/Dataset-OLID/OLIDv1.0/olid-training-v1.0.tsv') as fin:
        for cnt, line1 in enumerate(fin):
            _, tweet, offensive, _, _ = line1.strip().split('\t')

            # apply nltk tweet tokenizer
            tweet = tweetTokenizer(tweet)

            # additional improvements
            tweet = customTokenizer(tweet)

            # remove stopwords
            stop_words = set(stopwords.words('english'))
            tweet = [word for word in tweet if word not in stop_words]

            print(tweet)


if __name__ == '__main__':
    main()
