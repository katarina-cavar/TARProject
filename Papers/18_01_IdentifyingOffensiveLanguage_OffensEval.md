# Paper 18-01: [SemEval-2019 Task 6: Identifying and Categorizing Offensive Language in Social Media (OffensEval)](https://arxiv.org/pdf/1903.08983.pdf)

- OLID dataset (Offensive Language Identification Dataset)
	- 14k tweets
- sub-task A: 
	- offensive vs non-offensive
- sub-task B: 
	- type of offensive content
- sub-task C: 
	- detect target
- 800 teams assigned, 115 submitted results - presented in this paper

---

## 1. Introduction

- task usually modeled as supervised classification problem
- related topics: 
	- hate speech
	- cyberbulling
	- aggression

---

## 2. Related work

- different abusive and offense language identification problems

**Aggresion identification**
- 15k FB posts and comments
- classes: non-aggressive, covertly aggressive, overtly aggressive
- best systems: DL, CNN, RNN, LSTM

**Bullying detection**
- related

**Hate speech identification**
- most studied abusive language detection task
- dataset: 24k tweets (non-offensive, hate speech, profanity)

**Offensive language**
- GermEval - german tweets, 8k tweets, offensive / non-offensive; profanity, insult, abuse

**Toxic comments**
- challenge at Kaggle
- comments from wikipedia
- toxic, severe toxic, obscene, threat, insult, identity hate

---

## 3. Task description and Evaluation

- OLID dataset built for this task
- hierarchical three-level annotation model

### 3.1 Sub-task A: Offensive language identification

- categories: 
	- NOT - not offensive
	- OFF - offensive (if it contains any form of non-acceptable language (profanity) or a targeted offense)

### 3.2 Sub-task B: Automatic categorization of offense types

- only OFF are here
- categories: 
	- TIN - targeted insult (to an individual, group or others)
	- UNT - untargeted (with general profanity)

### 3.3 Sub-task C: Offense target identification

- only TIN are here
- categories: 
	- IND - individual
	- GRP - group
	- OTH - other (example: an organization, a situation, an event, an issue...)

### 3.4 Task evaluation

- imbalance between the number of instances
- macro-averaged F1 score as evaluation for all three sub-tasks

### 3.5 Participation

- 800 teams, 115 submitted results
	- list of teams' papers

---

## 4. Data

**OLID**
- hierarchical 3-layer annotation
- 14,1k tweets: 13 240 train, 860 test
	- + 320 trial dataset

---

## 5. Results

- techniques: SVM, log-reg, DL, CNN, RNN, BiLSTM, attention, ELMo, BERT
- some used 
	- additional training data
	- sentiment lexicons or sentiment analysis model for prediction
	- offensive word list
	- pre-trained word embeddings (FastText, GloVe, word2vec)
	- pre-processing: 
		- normalizing tokens, hashtags, URLs, retweets, dates, elongated words, partially hidden words, converting emoji to text, ... 
- results: table 4

### 5.1 Sub-task A

- top 10 teams: 
	- 7 BERTs
	- top non-BERT: ensamble of CNN and BLSTM+BGRU

### 5.2 Sub-task B

- top 10 teams: 
	- 5 ensembles
	- some ensembles: DL (including BERT) + non-neural ML models
- BERT works as well 


### 5.3 Sub-task C

- best: BERT
- 2nd best: ensemble of DL (OpenAI Finetune, LSTM, Transformer, non-neural ML: SVM, Random Forest)

### 5.4 Description of the Top Teams

- who cares


---

## 6. Conclusion

-  The evaluation results have shown that the best systems used ensembles and state-of-the-art deep learning models such as BERT. Overall, both deep learning and traditional machine learning classifiers were widely used.





















---