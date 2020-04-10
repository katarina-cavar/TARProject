## Project Checkpoint - Alpha

PRETPROCESIRANJE
- normalizing the tokens, hashtags, URLs, retweets (RT), dates, elongated words (e.g., “Hiiiii” to “Hi”, partially hidden words (“c00l” to “cool”)
- converting emojis to text, removing uncommon words
- Twitter-specific tokenizers (e.g. Ark Tokenizer, NLTK TweetTokenizer)
- standard tokenizers (e.g. Stanford Core NLP, the one from Keras)

DATASET
- dodatni datasetovi možda
- same dodati par primjera

ALATI I METODE
- bigram, Bayes ili nešto jednostavnije kao base model (usporedba s već postojećim popisom riječi)
- ML metode (više basic pristup) - SVM i/ili logistička regresija
- neuronske mreže
- deep learning (e.g. LSTM, BiLSTM)
- ensemble više deep learning metoda
- BERT (LSTM, izgradnja attention-a)
	* bazično razumijevanje jezika (Google)
	* fine-tuning za našu primjenu
	* potrebni resursi (Đerek, Šikić ?) 
- word embedding specifično za tweetove (200 dim, 20M tweetova)
- sentiment polarity - single numerical feature indicating sentiment polarity of the text (VADER)

ANALIZA
- F1 score (average, macro)
- grafovi (precision, recall)
- confusion matrix

OPCIJE
- primijeniti više metoda na a) pa usporediti (zadatke b) i c) ako stignemo)
- primijeniti jednu ili dvije metode na a), b) i c)

PITATI
- za rokove vezane uz projekt
- treba li naš članak opisati nešto novo i kako to ostvariti
- prokomemtirati gore navedene opcije, treba li možda nešto drugačije
