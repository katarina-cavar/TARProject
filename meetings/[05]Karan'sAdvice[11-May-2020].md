## Karanovi savjeti

UNSUPERVISED PRETRAINING NA SLOBODNOM TEKSTU I POTOM FINE-TUNING NA OFFENSEVAL PODATCIMA
- moguće koristiti DBN (Deep Belief Network)
- međutim, bolje koristiti modele poput word2vec ili BERT u tu svrhu

FEED-FORWARD NEURAL NETWORK (BOTH SINGLE- AND MULTI-LAYER PERCEPTRON)
- napraviti reprezentaciju svakog komentara tako da uprosječimo word embeddinge (word2vec, glove, fasttext i sl.), riječi svakog teksta
- na taj način dobijemo jedan npr. 300-dim vektor značajki za svaki tekst i onda nam je to ulaz u FFNN s jednim skrivenim slojem

LSTM, BiLSTM, CNN, RNN, GRU, BERT itd.
- radit će bolje od FFNN zato što svi ovi modeli u biti imaju feedforward komponentu na samom kraju mreže, samo način na koji se dobije ulaz u taj feedforward bude sofisticiraniji od jednostavnog prosjeka word2vec vektora
- npr. LSTM "prošeće" lstm cell po svim riječima i gleda zadnje stanje cella kao ulaz u FFNN (znači gleda vektore jedan po jedan po redu umjesto da ih uprosječi, a tako izgubi puno manje informacija)
- CNN radi slično, ali s konvolucijskim maskama
- koristiti Keras library (postoje svi osim BERT-a) -> jednostavan, najviše out-of-the-box, sve tehnikalije se dogode ispod haube
- također, moguće koristiti Pytorch i Tensorflow -> ako želimo malo više kontrole nad time što se događa, ima i tamo gotovih lstm/cnn/gru layera za iskoristiti

BERT
- malo teže fine-tunati model, teško bez grafičke, a i s GPU je užasno sporo
- ako ipak želimo probati, dobar library za to je tu: https://github.com/huggingface/transformers 
- s ovime bi moglo možda raditi dobro i bez fine-tunanja: https://github.com/UKPLab/sentence-transformers
	* samo generiramo reprezentaciju za tekst i koristimo to kao fiksni vektor za taj tekst (zapravo slično kao da smo uprosječili word embeddinge, ali puno moćnije)
