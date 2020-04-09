# Combining Shallow and Deep Learning for Aggressive Text Detection

#### __<div align="center"> Viktor Golem, Mladen Karan, Jan Šnajder</div>__

### 1.Intro
- TRAC1 workshop for English
- task was to distinguish between:
  - open aggression
  - covert aggression
  - non-aggression
- dataset: social media text (Facebook and Tweeter)
    - cca 15,000 FB messages, tested on Tweeter

### 2.Related work
- __very exhaustive overview of models used for this problem__

### 3. Models
- model evaluation: 5-fold cross-validation

#### 3.1 Shallow models
- __logistic regression__ - bigrams, unigrams, char-ngrams
- __SVM__

- testing with features:
  - bad word occurrences (bool)
  - POS tags (NLTK)
  - text length
  - capitalization features (number of capitalized words, number of __all caps__)
  - numerical tokens
  - named entities (person, organization, location)
  - __sentiment polarity__ - single numerical feature indicating sentiment polarity of the text (VADER)

#### 3.2 Deep models
- __CNN__
- __BiLSTM__

-inputs:
  - GloVe 300-dimensional word embeddings
  - 200-dimensional word embeddings trained on 20 mil tweets

#### 3.3 Ensembles
- voting (hard vote)
- SVM metaclassifier, RBF kernel

### 4.Results
- __BiLSTM and logistic regression (bigrams)__ - had comparable results (<60%), best performance
- BiLSTM - "...this model is considered by many to be the state of the art"
- combinations of the models (deep and shallow) yield somewhat better results than any of the models standalone

- __error analyses done__
- idea to approach: tree kernels combined with word embedding
