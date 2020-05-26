from nltk.tokenize import TweetTokenizer
import string


def tweetTokenizer(tweet):
    # preserve_case=False -> convert to lowercase
    # strip_handles=True  -> strip '@sth'
    # reduce_len=True     -> reduce > 3 consecutive letters to 3, e.g. 'yeeeees' to 'yeees'
    tweet_tokenizer = TweetTokenizer(preserve_case=False, strip_handles=True, reduce_len=True)
    return tweet_tokenizer.tokenize(tweet)


def main():
    with open('Dataset-OLID/OLIDv1.0/olid-training-v1.0.tsv') as fin:
        for cnt, line1 in enumerate(fin):
            _, tweet, offensive, _, _ = line1.strip().split('\t')

            # OFF - offensive
            # NOT - not offensive
            offensive = True if offensive == 'OFF' else False

            # apply nltk tweet tokenizer
            tweet = tweetTokenizer(tweet)

            # additional improvements
            table = str.maketrans(dict.fromkeys(string.punctuation))
            tweet2 = tweet.copy()
            tweet = []
            for word in tweet2:
                if word == '' or word == '“' or word == '’' or word == '..' or word == '...':
                    continue
                if len(word) == 1:
                    if word.translate(table) == '':
                        continue
                if word.startswith('#'):
                    tweet.append(word[1:])
                    continue
                tweet.append(word)

            # remove stopwords
            stopwords = set()
            with open('baseline/resources/stopwords.csv') as fin:
                for line in fin:
                    stopwords.add(line.strip())
            tweet = [x for x in tweet if x not in stopwords]

            print(tweet)


if __name__ == '__main__':
    main()
