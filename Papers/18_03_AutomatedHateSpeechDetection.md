# Paper 18-03: [Automated Hate Speech Detection and the Problem of Offensive Language∗](https://arxiv.org/pdf/1703.04009.pdf)

## 0. Abstract

- key challenge: separation of hate speech from other offensive language
- multiclass classifier for different categories

--- 

## 1. Introduction

- hate speech 
	- targets disadvantaged social groups
	- s language that is used to expresses hatred towards a targeted group or is intended to be derogatory, to humiliate, or to insult the members of the group
- sometimes people use offensive language but not as hate speech ("b\*tch" or "n\*gga" quoting some lyrics)
- this paper has 3 categories: 
	- hate speech
	- offensive language
	- neither

---

## 2. Related work

- bag-of-words approach
	- high recall, but high rates of false positives
	- presence of offensive words leads to misclassification
- leveraging syntactic features to better identify the targets and intensity of hate speech
	- I \*intensity\* - \*user intent\* - \*hate target\* (*I f\*cking hate white people*)

---

## 3. Data

- hate speech lexicon (by Hatebase.org)
- searched for tweets containing lexicon
	- 85M tweets from 33k users
- labeling blabla

--- 

## 4. Features

- lowercased stemmed tweets
- unigram, bigram, trigram features
	- each weighted by TF-IDF
- to capture information about the syntactic structure, we use *NLTK* (Bird, Loper, Klein 2009) to construct Penn Part-of-Speech tag 
-  To capture the quality of each tweet we use modified Flesch-Kincaid Grade Level and Flesch Reading Ease scores, where the number of sentences is fixed at one
 sentiment lexicon designed for social media to assign sentiment scores to each tweet
- include binary and count indicators for hashtags, mentions, retweets, and URLs, as well as features for the number of characters, words, and syllables in each tweet


---


## 5. Model

- log reg + L1 reg 
	- to reduce dimensionality of the data
- models: 
	- logreg
	- naive bayes
	- decision trees
	- random forests
	- linear SVMs
- test with 5 fold CV
- logreg and linear SVM performed better than others
- final model: logreg + L2 reg
- 1 vs rest 
- modeling using `scikit-learn`

--- 

## 6. Results

- best model: precision = 0.91, recall = 0.90, F1-score = 0.90
	- but almost 40% of hate speech is misclassified: precision = 0.44, recall = 0.61
- model is biased towards classifying tweets as less hateful than humans

A look into the data
- highest probability for hate speech - contain multiple racial or homophobic parts
- correct classification whe strongly racist or homophobic terms are used
- tweets labeled as offensive
	- generally less hateful
	- perhaps mislabeled ("curiosity is a b\*tch #curiosityKilledMe")
- hate speech misclassified as offensive
	- perhaps lack some terms strongly associated with hate speech
- hate speech misclassified as neither
	- tend to not contain hate or curse words
	- rare tiypes of hate speech tend to be misclassified (anti-Chinese, ... )
- key flaw: offensive language being mislabeled as hate speech due to an overly broad definition
	- they solved it
- Human coders appear to consider racists or homophobic terms to be hateful but consider words that are sexist and derogatory towards women to be only offensive
- neither misclassified as hate or offensive tend to mention race, sexuality and other social categories targeted by hate speakers
	- importance of taking context into account


---

## 7. 

- conflating (mixing) hate speech and offensive language makes lots of people look like hate speakers
	- fail to differentiate between commonplace offensive language and serious hate speech
- lexical methods: good for identifying offensive terms, inaccurate for identifying hate speech
- Hate speech is a difficult phenomenon to define and is not monolithic
