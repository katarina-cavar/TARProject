dictionary = set()

with open('resources/offensive_datasets/offensive') as fin:
    for line in fin:
        dictionary.add(line.strip())

with open('resources/offensive_datasets/bad-words.csv') as fin:
    for line in fin:
        dictionary.add(line.strip())

with open('resources/offensive_datasets/google_twunter') as fin:
    for cnt, line in enumerate(fin):
        if cnt == 0 or line.strip() == '}':
            continue

        line = line.replace('"', '').split(':')[0].strip()
        dictionary.add(line)

with open('resources/offensive_words.csv', 'w') as fout:
    for word in sorted(list(dictionary)):
        fout.write(word + '\n')
