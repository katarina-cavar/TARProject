from nltk.tokenize import TweetTokenizer, RegexpTokenizer


def tweetTokenizer(tweet):
    # preserve_case=False -> convert to lowercase
    # strip_handles=True  -> strip '@sth'
    # reduce_len=True     -> reduce > 3 consecutive letters to 3, e.g. 'yeeeees' to 'yeees'
    tweet_tokenizer = TweetTokenizer(preserve_case=False, strip_handles=True, reduce_len=True)
    return tweet_tokenizer.tokenize(tweet)


def matchTokenizer(tweet):
    # removes everything except word, numbers and '-'
    match_tokenizer = RegexpTokenizer("[\w-]+")
    return match_tokenizer.tokenize(tweet)


def main():
    with open('Dataset-OLID/OLIDv1.0/olid-training-v1.0.tsv') as fin:
        for cnt, line1 in enumerate(fin):
            _, tweet, offensive, _, _ = line1.strip().split('\t')

            # apply nltk tokenizers
            tweet = tweetTokenizer(tweet)
            tweet = matchTokenizer(' '.join(tweet))

            # remove stopwords and single '-'
            stopwords = set()
            with open('baseline/resources/stopwords.csv') as fin:
                for line in fin:
                    stopwords.add(line.strip())
            tweet = [x for x in tweet if x not in stopwords and x != '-']

            print(tweet)


if __name__ == '__main__':
    main()
