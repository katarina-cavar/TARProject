

# Paper 11-01: [Kashfia SailunazEmail authorManmeet DhaliwalJon RokneReda Alhajj. Emotion detection from text and speech: a survey](https://link.springer.com/article/10.1007/s13278-018-0505-2)

- different sources to analyze emotions
- extracting emotions - immense and complicated task
- to achieve better accuracy: 
  - word-based techniques
  - sentence-based techniques
  - ML
  - NLP
- this article has to be bought!! :O  

## 1. Introduction

- emotion detection - hard task due to versatility, ambiguity and other params
  - harder from sentiment detection
  - ‘Emotion’ is “a strong feeling deriving from one’s circumstances, mood, or relationships with others”
  - ‘Sentiment’ is “a view or opinion that is held or expressed"
  - sentiments - effects of emotions

## 2. Emotion Analysis

- expressing emotions in multiD ways
  - facial expression, body language, gesture, text, speech

### 2.1 Evolution of Emotion

- Darwin: humans and animals express emotions in similar circumstances
- some emotional expression universal for people all over the world

### 2.2 Emotion models

- emotions can be identified and grouped based on emotion type, intensity, duration, synchronization, rapidity of change, event focus, ... 

Emotion models: 
1. *Categorical*
  - define list of categories of emotions
2. *Dimensional*
  - define a few dimenisons with some parameters
  - usual dimensions:
    - valence - positivity / negativity of emotion
    - arousal - excitement level of an emotion
    - dominance - level of control over an emotion

### 2.3 Emotion detection
    
- table of emotion models


## 3. Emotion Analysis from Text

- most people use text for communication
- extracting emotions from text is harder
  - easier if words representing a particular emotion were explicit in the text
- usually - emotion expressed in a subtle way
  - multiple meanings, multiple emotions, ambiguous words, sarcasm, slang, spelling mistakes, multilingual test, acronyms... 
- research on emotion extraction from text is very popular
- overview of exitsing work in tables..

### 3.1 Emotion detection methods

- *affective computing* -  study and development of systems and devices that can recognize, interpret, process, and simulate human affects
- categories: 
  - keyword-based method
  - lexicon-based method
  - machine learning method
  - hybrid method
- existing work utilized the following as features for emotion detection task: 
  - unigrams
  - n-grams
  - emoticons
  - hashtag words
  - punctuations
  - negations

#### 3.1.1 Keyword-based method

- most intuitive and straightforward
- find patterns similar to emotion keywords and match them
- tag words with Parts-Of-Speech tagger and extract NAVA words (Noun, Adjective, Verb, Adverb)
  - most probable emotion carrying words
- match words with emotion-connected words
- WordNet - find synonyms and antonyms of words

#### 3.1.2 Lexicon-based method

- classifies text using a lexicon
- similar to 3.1.1

#### 3.1.3. Machine learning method

- supervised
  - most common: Naive Bayes, SVM, Decision tree
- unsupervised
  - start with several seed words which are cross-referenced to sentences
- unsup more generalized, but sup usually has better acc

#### 3.1.4 Hybrid method

- combines any two or more methods
- benefit of multiple methods
- better acc

### 3.2 Datasets

- small num of emotion labeled datasets available
- most used datasets in table 13

### 3.3 Discussions

- lot of unturned stones and possibilities

#### 3.3.1 Emotion Intensity Detection

- different intensities
- normal sadness vs severe depression

#### 3.3.2 Sarcasm Detection

- very complex task
- max acc achieved so far is not the best
- correct sarcasm detection depends on correctly using sentence structure,  accurate emotion behind the sentence, understanding context, .. 

#### 3.3.3 Multiple emotion detection

- recognizing emotions with temporal and/or spatial dimension

#### 3.3.4 Emotion-cause detection

- cause of emotions
- likes and dislikes of a person

#### 3.3.5 Personality or mood detection

- for making personalized suggestions
- if a person is angry, we could suggest going to her fav restaurant

#### 3.3.6 Emotion vs individual or social parameters

- emotions can be related to their age, gender, time, location, ethnicity, political views, ... 
- individual, social, temporal and spatial parameters
- example: older people can be more concerned with political issues


## 4. Emotion recognition from speech

- let's skip this

## 5. Conclusions

- sum up