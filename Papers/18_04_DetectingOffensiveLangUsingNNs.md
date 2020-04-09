# Paper 18-04: [Detecting Offensive Language in Tweets Using Deep Learning](https://arxiv.org/abs/1801.04433)

- date: Jan 2018

## 0. Abstract

- detecting hateful content in tweets
- detection scheme: ensemble of RNNs 
- 16k tweet dataset
- scheme can successfully distinguish racism and sexism from notmal text

## 1. Introduction

- dealing with offensive speech on social media
	- so far (2016) relying on human annotation and reporting comments as offensive
		- huge effort needed
		- strong impact on response time
- NLP approaches tend to be complex and dependent on the language used in text
- new approach: neural networks
- majority of the existing automated approaches depend on using pre-trained vectors (e.g. Glove, Word2Vec) as word embeddings to achieve good performance from the classification model
	- the detection of hatred content unfeasible in cases where users have deliberately obfuscated their offensive terms with short slang words
- **a lot of unsupervised approaches dealing with hate speech**
- significant correlation between the user tendency in expressing opinions that
belong to some offensive class (Racism or Sexism), and the annotation labels associated
with that class

Main contributions: 
- DL arch for text classification in terms of hateful content
	- incorporates feats derived from the users' behavioural data
- language agnostic solution
	- due to no-use of pre-trained word embeddings
- experimental evaluation of the model on a Twitter dataset

--- 

## 2. Problem Statement

classes: 
- N - neutrality
- S - sexism
- R - racism

data: 
- p - unlabeled short sentence
- u - user who posted
	- has a history of posted messages

The Problem: to identify the class, which the unlabeled sentence p by user u belongs to
- *How to effectively identify the class of a new posting, given the identity of the
posting user and the history of postings related to that user?*


## 3. Related Work

- simple word-based approaches fail to identify subtle offensive content and affect the freedom of speech and expression
	- word can have different meaning in different contexts

Previous work: 
- LSTM works better than SVM on Hate/noHate data
- differentiate between hate speech and offensive language
	- naive bayes, decision tree, svm
- combining various linguistic and syntactic features in the text
- unsupervised approaches are common

---

## 4. Description of our Recurrent Neural Network-based Approach

- RNNs, LSTMs

### 4.1 Features

- 3 features t_na, t_ra, t_sa -> user's tendency towards posting neutral, racist, sexist
- model the input tweets in the form of vectors using wordbased frequency vectorization

### 4.2 Classification

- ensemble of LSTMs


---

## 5. Evaluation setup - Results

### 5.1 Data Preprocessing

- tokenization using Moses package


### 5.2 Deep Learning Model

**Layers:**
- Input (Embedding) Layer
- Hidden layer (LSTM) -> sigmoid
- Dense layer -> ReLU
- Output layer -> Softmax

### 5.3 Dataset

- 16k short messages from twitter

### 5.4 Experimental Setting

- 10 fold CV
- keras
- ADAM
- vocab size = 25000


### 5.5 Results

- eval: precision and recall, f-score

- table page 12 ... :) 

- the incorporation of features related to user’s behaviour into the
classification has provided a significant increase in the performance vs. using the textual content alone
	- this shouldn't be the case, right?
- deep learning can outperform any NLP-based approaches known so far in the task of abusive language detection


--- 

## 6. Conclusions and Future Work

- ensemble classifier that is detecting hate-speech in short text
-  input to the base-classifiers consists of not only the standard word uni-grams, but also a set of features describing each user’s historical tendency to post abusive messages
- future work: investigate other sources
