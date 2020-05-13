import string


def deEmojify(s):
    return s.encode('ascii', 'ignore').decode('ascii')


def main():
    offensive_words = set()
    with open('resources/offensive_words.csv') as fin:
        for line in fin:
            offensive_words.add(line.strip())

    stopwords = set()
    with open('resources/stopwords.csv') as fin:
        for line in fin:
            stopwords.add(line.strip())

    accuracy = 0
    with open('../Dataset-OLID/OLIDv1.0/olid-training-v1.0.tsv') as fin:
        for cnt, line in enumerate(fin):
            _, tweet, offensive, _, _ = line.strip().split('\t')

            # OFF - offensive
            # NOT - not offensive
            offensive = True if offensive == 'OFF' else False

            # remove punctuation
            table = str.maketrans(dict.fromkeys(string.punctuation))
            tweet = tweet.translate(table)

            # remove @USER
            tweet = tweet.replace('USER', '')

            # convert to lowercase
            tweet = tweet.lower()

            # remove emojis
            tweet = deEmojify(tweet)

            # remove stopwords
            tweet = [x for x in tweet.split() if x not in stopwords]

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
