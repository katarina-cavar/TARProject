from Preprocessor import Preprocessor


def main():
    preprocessor = Preprocessor()

    offensive_words = set()
    with open('../resources/offensive_words.csv') as fin:
        for line in fin:
            offensive_words.add(line.strip())

    accuracy = 0
    with open('../../Dataset-OLID/OLIDv1.0/olid-training-v1.0.tsv') as fin:
        for cnt, line in enumerate(fin):
            if cnt == 0:
                continue

            _, tweet, offensive, _, _ = line.strip().split('\t')

            # OFF - offensive
            # NOT - not offensive
            offensive = True if offensive == 'OFF' else False

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
