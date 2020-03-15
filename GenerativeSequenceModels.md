# Generative Sequence Models

- the goal of this file is to do research on what Generative Sequence Models are and how to build them


## TL; DR

Summary of this file:
- topic proposal
- (summed up) suggestions by Mladen Karan
- research on the Topic
	- useful links
	- tutorials on building generative sequence models
	- different paper propositions
	- paper I started with ([The Secret Sharer : Evaluating and Testing Unintended Memorization in Neural Networks](https://www.usenix.org/system/files/sec19-carlini.pdf) )

**Short topic proposal**
- compare different generative models
- research different evaluation metrics
- build an attack (if you guys want to)
- see what gets our interest during the project and go in that direction 

---

## Topic proposal

Reminder:
- Idea is to create multiple segments of our topic. We should be **happy with finishing any of these segments** as our project. **If we have time, we can do more** or all of the segments.
- segments **don't** have to be done in the order they are explained below

Segment 1:
- compare n-gram models with LSTMs, RNNs, word-level and/or character-level Models
- if we have enough computational power, it would be cool to compare it to transformers also (BERT, ALBERT, Sentence-BERT, ...)
	- i can add links to papers or articles for BERT, ALBERT and similar, I'm currently working with transformers
- compare speed, quality, ...
- possibly try a hybrid n-gram LM + neural LM to get both speed and performance
- **Katarina: I propose this as our base segment, we could build lots of things on it**


Segment 2:
- explore evaluation metrics
- compare quality and perplexity metrics of the model
- see other metrics?
- think of our own metric?
	- this could be too hard?

Segment 3:
- build attacks on top of these models, as described in [The Secret Sharer : Evaluating and Testing Unintended Memorization in Neural Networks](https://www.usenix.org/system/files/sec19-carlini.pdf)
	- or any other paper

Segment 4:
- Mystery Segment
	- we can add here whatever we want :)

---

## Suggestion by Mladen Karan

1. **je li tema dovoljno povezana s gradivom predmeta?**
- keywords:
  - n-gram language models (LM)
    - jednostavni statisticki modeli
  - neural language models
    - ogromne DL mreze (**transformers**)
    - bolje modeliraju kontext
    - [BERT](https://arxiv.org/abs/1810.04805)


2. **da li je preteška ili možda prejednostavna za projekt?**

- sloziti pricu koju zelimo ispricati / pitanja na koja zelimo odgovoriti
- slozenost po:
  - a) kolicini i slozenosti implementiranih modela
  - b) broju datasetova na kojima isprobavamo modele
  - c) sofisticiranosti i broju eksperimenata koje cemo vrtiti
- TO DO:
  - napraviti svoj prijedlog, oni ce pogledati i po potrebi jos malo razraditi
- na checkpointovima mozemo dodatno suziti / prosiriti opseg

**Ogledni primjeri:**
- **vanilla (n-gram) LM vs neural LM** usporedba performansi, analiza pogresaka, da li grijese u istim slucajevima
- ako mora biti real time mozda je neural presporo pa se moze napraviti neki **hibrid n-gram LM + neural LM** da se dobije i brzina i performanse
- ako imate skup tekstova neke vrlo uske domene na kojem treba raditi autocomplete, moze li se nekako iskoristiti podaci iz druge domene u kojoj imate jako puno tekstova za popravljanje rezultata na ovoj prvoj domeni (**pretrain na general domain pa finetune** dodatno, kao neki domain adaptation)
- **istrazivanje postupaka evaluacije**, da li je **preplexity** prikladna mjera, npr. evaluirati sve modele kvalitativno i sa perplexity, odrediti da li ljudske ocjene kvalitete dobro koreliraju sa perplexity, **razmotriti druge mjere evaluacije** (blue score npr.), mozda **izmisliti vlastitu**?
- **customizacija predvidjanja sa dodatnim podacima o korisniku** ako ih mozete nabaviti (npr. ako znate dob ili spol osobe koja pise to vec ta informacija sama po sebi moze mozda dosta utjecati na to koje rijeci bi bili prikladniji autocomplete kandidati, a mozda i nece, to je pitanje)


3. **mislite li da postoji prikladan dataset na kojem bi se ovo moglo obavljati?**

- datasetovi:
  - https://ilps.science.uva.nl/wp-content/papercite-data/pdf/cai-survey-2016.pdf
  - googlati druge
  - automatski generirati dataset?
  - ljudi ocjenjuju? skupo!
- moja ideja:
  - pogledati dataset na kojem je radio Google Smart Complete? (trebalo bi nesto bit javno buduci da je to clanak?)


---

## Research on the topic


Googled term: `how to make generative sequence models`

### [Gentle Introduction on Generative LSTM Networks ](https://machinelearningmastery.com/gentle-introduction-generative-long-short-term-memory-networks/)

August 2017.

- LSTM models can be designed to learn the general structural properties of the corpus, and when given a seed input, **can generate new sequences** that are representative of the original corpus
	- may work word level or character Level

**Generative LSTM**
- a Generative LSTM is not really architecture, it is more a change in perspective about what an LSTM predictive model learns and how the model is used
- Vanilla LSTM: input -> LSTM -> Dense -> Output

**Papers proposed:**
- [Generating Text with Recurrent Neural Networks, 2011.](http://www.cs.utoronto.ca/~ilya/pubs/2011/LANG-RNN.pdf)
	- Abstract:
```
Recurrent Neural Networks (RNNs) are very powerful sequence models that do not enjoy
widespread use because it is extremely difficult to train them properly. Fortunately,
recent advances in Hessian-free optimization have been able to overcome the difficulties
associated with training RNNs, making it possible to apply them successfully to
challenging sequence problems. In this paper we demonstrate the power of RNNs trained
with the new Hessian-Free optimizer (HF) by applying them to character-level
language modeling tasks. The standard RNN architecture, while effective, is not ideally
suited for such tasks, so we introduce a new RNN variant that uses multiplicative
(or “gated”) connections which allow the current input character to determine the
transition matrix from one hidden state vector to the next. After training
the multiplicative RNN with the HF optimizer for five days on 8 high-end
Graphics Processing Units, we were able to surpass the performance of the best
previous single method for character-level language modeling – a hierarchical
nonparametric sequence model. To our knowledge this represents the largest recurrent neural network application to date.
```
- [Generating Sequences With Recurrent Neural Networks, 2013.](https://arxiv.org/abs/1308.0850)
	- handwriting
	- Abstract:
```
This paper shows how Long Short-term Memory recurrent neural networks can be used to
generate complex sequences with long-range structure, simply by predicting one data point at
a time. The approach is demonstrated for text (where the data are discrete) and online
handwriting (where the data are real-valued). It is then extended to handwriting synthesis
by allowing the network to condition its predictions on a text sequence. The resulting
system is able to generate highly realistic cursive handwriting in a wide variety of styles.
```
- [TTS Synthesis with Bidirectional LSTM based Recurrent Neural Networks, 2014.]
	- text to speech
- [A First Look at Music Composition using LSTM Recurrent Neural Networks, 2002
	- music generation
- [Jazz Melody Generation from Recurrent Network Learning of Several Human Melodies, 2005.]
	- music generation


### [Gentle introduction to Statistical Language Modeling and Neural Language Models](https://machinelearningmastery.com/statistical-language-modeling-and-neural-language-models/)

Explains briefly the following:
- Problem of Modeling Language
- Statistical Language Modeling
- Neural Language Models
	- steps:
		- associate each word in the vocab with a distributed word feature vector
		- express the joint probability function of word sequences in terms of the feature vectors of these words in the sequence
		- learn simultaniously the word feature vector and the parameters of the probability function
	- outperforms the classical statistical approaches
	- heuristics:
		- size matters (bigger models -> better results, usually)
		- regularization matters
		- CNNs vs Embeddings - Char level CNNs can sometimes achieve better results than word embeddings
		- Ensembles matter


Tutorials:
- [How to Develop a Word-Level Neural Language Model and Use it to Generate Text](https://machinelearningmastery.com/how-to-develop-a-word-level-neural-language-model-in-keras/)
	- has code! :D (Keras!)
	- how to prepare text for developing a word-based language model
	- how to design and fit a neural language model with a learned embedding and an LSTM hidden layer
	- how to use the learned **language model to generate new text** with similar statistical properties as the source text
- [How to Develop Word-Based Neural Language Models in Python with Keras](https://machinelearningmastery.com/develop-word-based-neural-language-models-python-keras/)
	- Framing Language Modeling
	- Jack and Jill Nursery Rhyme
	- Model 1: One-Word-In, One-Word-Out Sequences
	- Model 2: Line-By-Line Sequence
	- Model 3: Two-Words-In, One-Word-Out Sequence
- [How to Develop a Character-Based Neural Language Model in Keras](https://machinelearningmastery.com/develop-character-based-neural-language-model-keras/)
	- How to prepare text for character-based language modeling
	- How to develop a character-based language model using LSTMs
	- How to use a trained **character-based language model to generate text**


---

The paper I got introduced in with this topic:

### Paper | [The Secret Sharer : Evaluating and Testing Unintended Memorization in Neural Networks](https://www.usenix.org/system/files/sec19-carlini.pdf)

Abstract:
```
This paper describes a testing methodology for quantitatively assessing the risk
that rare or unique training-data sequences are unintentionally memorized by
generative sequence models—a common type of machine-learning model.
Because such models are sometimes trained on sensitive data
(e.g., the text of users’ private messages), this methodology
can benefit privacy by allowing deep-learning practitioners to
select means of training that minimize such memorization.
In experiments, we show that unintended memorization is
a persistent, hard-to-avoid issue that can have serious consequences.
Specifically, for models trained without consideration of memorization,
we describe new, efficient procedures that can extract unique, secret sequences,
such as credit card numbers. We show that our testing strategy is a practical and
easy-to-use first line of defense, e.g., by describing its application to quantitatively
limit data exposure in Google’s Smart Compose, a commercial text-completion
neural network trained on millions of users’ email messages.
```
