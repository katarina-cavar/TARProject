import random


# e.g. fraction = 0.8 -> train set: 80%
#                     -> validation set: 20%
def partition(ldata, fraction):
    # ldata = list(data)
    random.shuffle(ldata)
    breakPoint = int(len(ldata) * fraction)
    return ldata[:breakPoint], ldata[breakPoint:]


data = []
with open('../../Dataset-MTSA/extracted_tweets.tsv', encoding='utf-8') as fin:
    for cnt, line in enumerate(fin):
        if cnt == 0:
            header = line
        data.append(line)

train, test = partition(data, 0.935)

with open('../../Dataset-MTSA/tweets_train.tsv', 'w', encoding='utf-8') as fout:
    fout.write(header)
    [fout.write(t) for t in train]

with open('../../Dataset-MTSA/tweets_test.tsv', 'w', encoding='utf-8') as fout:
    fout.write(header)
    [fout.write(t) for t in test]
