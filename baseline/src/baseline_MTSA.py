from Preprocessor import Preprocessor


def main():
    preprocessor = Preprocessor()

    offensive_words = set()
    with open('../resources/offensive_words.csv') as fin:
        for line in fin:
            offensive_words.add(line.strip())

    accuracy = 0
    with open('../../Dataset-MTSA/extracted_tweets.tsv') as fin:
        for cnt, line in enumerate(fin):
            if cnt == 0:
                continue

            id, offensive, tweet = line.strip().split('\t')

            # POS - positive
            # NEG - negative
            offensive = True if offensive == 'NEG' else False

            # perform preprocessing
            tweet = preprocessor.preprocess(tweet)

            # check if a word in tweet is in the offensive words dataset
            isOffensive = False
            for word in tweet:
                if word in offensive_words:
                    isOffensive = True
                    break

            # if our estimation is equal to official annotation increase accuracy
            if offensive == isOffensive:
                accuracy += 1

        accuracy = accuracy / cnt * 100
        print('Accuracy: {}%'.format(str(round(accuracy, 4))))


if __name__ == '__main__':
    main()
