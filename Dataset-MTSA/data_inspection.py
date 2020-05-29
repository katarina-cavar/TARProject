def inspect(data_file):
    neg = 0
    pos = 0

    with open(data_file, encoding='utf-8') as fin:
        for cnt, line in enumerate(fin):
            if cnt == 0:
                continue
            if line.split('\t')[1] == 'NEG':
                neg += 1
            else:
                pos += 1

    print('Negative data: ', neg)
    print('Positive data: ', pos)
    print('Total data: ', cnt)
    print('-' * 50)


def main():
    # training set
    print('TRAINING SET')
    inspect('tweets_train.tsv')

    # test set
    print('TEST SET')
    inspect('tweets_test.tsv')


if __name__ == '__main__':
    main()
