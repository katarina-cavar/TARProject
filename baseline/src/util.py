import random


# e.g. fraction = 0.8 -> train set: 80%
#                     -> validation set: 20%
def partition(data, fraction):
    ldata = list(data)
    random.shuffle(ldata)
    breakPoint = int(len(ldata) * fraction)
    return ldata[:breakPoint], ldata[breakPoint:]
