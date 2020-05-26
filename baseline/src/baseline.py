from nltk.tokenize import TweetTokenizer, word_tokenize, WordPunctTokenizer, RegexpTokenizer
import string


def customTokenizer(tweet, lowercase=False, remove_emojis=False):
    # remove punctuation
    table = str.maketrans(dict.fromkeys(string.punctuation))
    tweet = tweet.translate(table)

    if lowercase:
        # convert to lowercase
        tweet = tweet.lower()

    if remove_emojis:
        # remove emojis
        tweet = tweet.encode('ascii', 'ignore').decode('ascii')

    # remove stopwords
    stopwords = set()
    with open('resources/stopwords.csv') as fin:
        for line in fin:
            stopwords.add(line.strip())
    tweet = [x for x in tweet.split() if x not in stopwords]

    return tweet


def tweetTokenizer(tweet):
    tweet_tokenizer = TweetTokenizer()
    return tweet_tokenizer.tokenize(tweet)


def wordTokenizer(tweet):
    return word_tokenize(tweet)


def punctTokenizer(tweet):
    punct_tokenizer = WordPunctTokenizer()
    return punct_tokenizer.tokenize(tweet)


def matchTokenizer(tweet):
    match_tokenizer = RegexpTokenizer("[\w']+")
    return match_tokenizer.tokenize(tweet)


def spaceTokenizer(tweet):
    space_tokenizer = RegexpTokenizer("\s+", gaps=True)
    return space_tokenizer.tokenize(tweet)


def main():
    offensive_words = set()
    with open('resources/offensive_words.csv') as fin:
        for line in fin:
            offensive_words.add(line.strip())

    accuracy = 0
    with open('../Dataset-OLID/OLIDv1.0/olid-training-v1.0.tsv') as fin:
        for cnt, line in enumerate(fin):
            _, tweet, offensive, _, _ = line.strip().split('\t')

            # OFF - offensive
            # NOT - not offensive
            offensive = True if offensive == 'OFF' else False

            # remove @USER
            tweet = tweet.replace('@USER', '')

            # TODO choose tokenizer function
            tweet = customTokenizer(tweet)

            # check if a word in tweet is in the offensive words dataset
            isOffensive = False
            for word in tweet:
                if word in offensive_words:
                    isOffensive = True
                    break

            # if our estimation is equal to official annotation increase accuracy
            if offensive == isOffensive:
                accuracy += 1

        accuracy = accuracy / (cnt + 1) * 100
        print('Accuracy: {}%'.format(str(round(accuracy, 4))))


if __name__ == '__main__':
    main()
