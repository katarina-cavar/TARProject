import pandas as pd
from collections import defaultdict, Counter


def find_sentiment(ratings):
    count = Counter(ratings)

    # if negative and positive have the same frequency, positive has the advantage
    if count['negative'] > 0 and count['negative'] > count['positive']:
        return 'NEG'

    return 'POS'


def main():
    df = pd.read_csv('annotated_tweets.csv',
                     usecols=['is_the_sentiment_expressed_positive_or_negative_', 'text', 'tweet_id'], dtype=object)
    df = df.applymap(str)

    tweet_id = df['tweet_id'].to_list()
    tweet = df['text'].to_list()
    is_pos_neg = df['is_the_sentiment_expressed_positive_or_negative_'].to_list()

    tweet_dict = {}
    for i in range(len(tweet_id)):
        tweet_dict[tweet_id[i]] = tweet[i]

    rating_dict = defaultdict(list)
    for i in range(len(tweet_id)):
        rating_dict[tweet_id[i]].append(is_pos_neg[i])

    with open('extracted_tweets.tsv', 'a') as fout:
        fout.write("{}\t{}\t{}\n".format('id', 'sentiment', 'tweet'))
        i = 0
        for id, ratings in rating_dict.items():
            fout.write('{}\t{}\t{}\n'.format(i, find_sentiment(ratings), tweet_dict[id]))
            i += 1


if __name__ == '__main__':
    main()
