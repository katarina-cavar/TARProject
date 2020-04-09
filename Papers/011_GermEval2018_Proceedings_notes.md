# Offensive Language Detection with Neural Networks for Germeval Task 2018

### INTRO
- 2 tasks:
  - __binnary classification of offensive tweets__ in German
  - classification of offensive tweets into: profanity, insult and abuse (not done because of ill distribution of classes)
  - evaluation: macro-averaged F1 score
  - __CNNs and RNNs__

### Preprocessing
- dataset: 5009 tweets
- tokenization
- punctuation removal
- removal of non-alphanumerical characters
- lowercased words
- hashtags used without #-sign
- @SIGN removed
- __pre-trained embeddings used__ (NB words in th embeddings are true-cased)
- tweets vectorized using words IDs

### Models
1. __CNN__
  - very fast
  - few trainable parameters
  - can only consider local information

2. __RNN__
  - bidirectional gated recurrent units (GRUs)
  - LSTMs performed worse than GRUs
  - cross-entropy as loss
  - Adam optimizer
  - cross validation
  - grid search for hiperparameters

### Results
  - shot given to:
    - __lowercase__ outperforms true-cased words
    - __swear word dictionary__ (when words were not found in embeddings vocabulary) - result better for true-cased case but not for lowercase
    - issue with __out-of-vocabulary (OOV)__ words (misspelling etc.)
      - solution: character embedding - bad performance

  - winner: CNN model with a bi- and trigram filter
  - __ensambles of CNN better (1% diff) than RNN - 78.6%__
