# Paper 08: [BERT: Pre-training of Deep Bidirectional Transformers for Language Understanding](https://arxiv.org/abs/1810.04805)

## 0. Abstract

- BERT - Bidirectional Encoder Representations from Transformers
- BERT is designed to pretrain deep bidirectional representations from unlabeled text by jointly conditioning on both left and right context in all layers
- can be finetuned with just one additional output layer to create SOTA models for a wide range of tasks
	- question answering
	- language inference
	- ... 

--- 

## 1. Introduction

- LM (language model) pretraining is effective for improving many NLP tasks
	- NL inference
	- paraphrasing
	- named entity recognition
	- question answering
	- ... 
- are two existing strategies for applying pre-trained language representations to downstream tasks: *feature-based* and *fine-tuning*

**feature-based**
- ELMo
- task-specific architectures
- pre-trained representations as additional features

**fine-tuning**
- minimal task-specific params
- trained on the downstream tasks by simply fine-tuning all pretrained parameters


Approaches
- share the same objective function during pre-training
- unidirectional LMs to learn general language representations
- major limitation is that standard language models are unidirectional
	- such restrictions are sub-optimal for sentence-level tasks,
and could be very harmful when applying finetuning based approaches to token-level tasks

**BERT**
- we improve the fine-tuning based approaches by proposing BERT: Bidirectional Encoder Representations from Transformers
- MLM (Masked Language Model)
	- masked language model randomly masks some of the tokens from the input, and the objective is to predict the original vocabulary based only on its context
	- MLM objective enables the representation to fuse the left and the right context
		- pretraining a deep bidirectional Transformer
- next sentence prediction

**Paper contributions:**
- demonstrate the importance of bidirectional pre-training for language representations
- pre-trained representations reduce the need for many heavily-engineered taskspecific architectures
	- BERT is the first finetuning based representation model that achieves state-of-the-art performance on a large suite of sentence-level and token-level tasks, outperforming many task-specific architectures
- [BERT - code and pre-trained models](https://github.com/google-research/bert)


--- 

## 2. Related Work

### 2.1 Unsupervised Feature-based Approaches

- pre-trained word embeddings are an integral part of modern NLP systems
	- significant improvements over embeddings learned from scratch
- word embeddings, sentence embeddings, paragraph embeddings
	- **REALNETWORKS COULD BE INTERESTED IN SENTENCE / PARAGRAPH EMBEDDINGS**
	- Paper: [An efficient framework for learning sentence representations](https://openreview.net/forum?id=rJvJXZb0W)
- ELMo
	- generalize traditional word embedding research along a different dimension
	- extract *context-sensitive* features from L-to-R and R-to-L LMs
	- question answering, sentiment analysis and named entity recognition

### 2.2 Unsupervised Fine-tuning Approaches

- sentence or document encoders which produce contextual token representations have been pre-trained from unlabeled text and fine-tuned for a supervised downstream task
- advantage: few parameters need to be learned from scratch

### 2.3 Transfer Learning from Supervised Data

- effective transfer from supervised tasks with large datasets, such as natural language inference and machine translation
- cool in computer vision also

--- 

## 3. BERT

- two steps: pre-training and fine-tuning
- pre-training
	- model trained on unlabeled data over different pre-training tasks
- fine-tuning
	- initialized with pre-trained params
	- params fine-tuned using labeled data from the downstream tasks
	- each downstream task has spearate fine-tuned models
- a distinctive feature of BERT is its unified architecture across different tasks
	- minimal difference between pre-trained arch and the final downstream arch

**Model Architecture**
- multi-layer bidirectional Transformer encoder
- *annotation*
	- L - number of layers
	- H - hidden size
	- A - number of self-attention heads
- BERT_base (L=12, H=768, A=12, total_params=110M)
- BERT_base (L=24, H=1024, A=16, total_params=340M)

**Input/Output Representations**
- input repr can unambiguously represent both a single sentence and a pair of sentences in one token sequence
- WordPiece embeddings with 30k token vocab
- first token of a sequence: `[CLS]`
- separator token: `[SEP]`
- we denote: 
	- input embedding as *E*
	- final hidden vector of the `[CLS]` token as *C*
	- final hidden vector for the i_th input token as *T_i*
- for a token: 
	- input repr = corresponding token + segment + position embeddings

### 3.1 Pre-training BERT

- pre-training BERT using 2 unsupervised tasks

**Task #1: Masked LM**
- bidirectional models should be more powerful than unidirectional
- to train bidir, we mask some percentage of the input tokens and random and then predict those masked tokens
	- -> *Masked LM* or *Cloze* (in the literature)
	- 15% tokens masked
	- only predict masked words (rather than reconstructing the entire input)
- downside: creating a mismatch between pre-training and fine-tuning
	- `[MASK]` token doens't appear during fine-tuning
	- to mitigate this, we don't always replace masked words with `[MASK]` token
- masking tokens replaced with: 
	- `[MASK]` token 80%
	- random token 10%
	- unchanged token 10% 

**Task #2: Next Sentence Prediction (NSP)**
- tasks based on understanding the relationship between two sentences: 
	- Question Answering (QA)
	- Natural Language Inference (NLI)
- relationship between two sentences not directly captured by language modeling
- pre-train for binarized *next sentence prediction* task
	- labels "isNext", "notNext"
- NSP task closely related to representation-learning objectives
	- in prior work, only sentence embeddings are transferred to down-stream tasks, where BERT transfers all parameters to initialize end-task model parameters

**Pre-training data**
- corpus: BooksCorpus (800M words), English Wikipedia (2500M words)

### 3.2 Fine-tuning BERT

- for text pairs, BERT encodes a concatenated pair with self-attention -> bidirectional cross attention between the two sentences
- for each specific task: 
	- plug in task specific inputs and outputs into BERT
	- finetune all params end-to-end
- output: token reps fed into an output layer for token-level tasks: 
	- sequence tagging, question answering, ... 
- output: [CLS] rep fed into an output layer for classification: 
	- entailment, sentiment analysis...
- compared to pre-training, fine-tuning is relatively inexpensive
	- few hours on a GPU

---

## 4. Experiments

- BERT fine-tuning results on 11 NLP tasks

### 4.1 GLUE

- GLUE = The General Language Understanding Evaluation


(From **Appendix B.1**:)
- GLUE (The General Language Understanding Evaluation)
	- MNLI (Multi-Genre Natural Language Inference)
		- pair of sentences -> entailment / contradiction / neutral
	- QQP (Quora Question Pairs)
		- if two Qs are semantically equivalent
	- QNLI (Question NL Inference)
		- version of Stanfort QA Dataset
		- (question, sentence) -> correct answer / no answer
	- SST-2 (Stanford Sentiment Treebank)
		- movie review -> sentiment
	- CoLA (The Corpus of Linguistic Acceptability)
		- english sentence -> linguistically acceptable / not
	- STS-B (The Semantic Textual Similarity Benchmark)
		- sentence pairs (from headlines, ...) -> 1-5 similarity score
	- MRPC (Microsoft Research Paraphrase Corpus)
		- sentence pairs (from news) -> semnatically equivalent / not
	- RTE (Recognizing Textual Entailment)
		- similar to MNLI, less training data
	- WNLI (Winograd NL Inference)
		- there are issues with construction of this dataset

**Back to 4.1 GLUE**
- for finetuning: 
	- input sequence (sentence or sent-pair)
	- final hidden vector
	- new parameters: classification layer weights (W e R - dim = KxH)
		- K - number of labels
- compute standard classification loss with C and W  ( *log(softmax(CW'))* ) 
- hyperparams
	- batch_size = 32
	- epochs = 3
	- learning rate = best one on dev set (among 5e-5, 4e-5, 3e-5, and 2e-5)
- bert_large sometimes unstable on small datasets -> random restarts
- bert_base and bert_large outperform all systems on all tasks
	- bert_large outperforms bert_base

### 4.2 SQuAD v1.1

- Stanford Question Answering Dataset 
	- 100k crowdsourced q/a pairs
	- (question, passage - odlomak) -> answer
- bert: question with A embedding, passage with B embedding

### 4.3 SQuAD v2.0

- extension: possibility that no short answer exists in the paragraph


### 4.4 SWAG

- SWAG = Situations With Adversarial Generations
	- 113k sentence-pair completion examples that evaluate grounded commonsense inference
	- given a sentence, choose the most plausible continuation among four choices
- BERT: 
	- 4 input sequences: one for each continuations 
	- beginnings marked with A, continuations with B

## 5. Ablation Studies 

- ablation = amputacija
- ablation experiments over a number of facets of BERT
	- to better understand relative importance

### 5.1 Effect of Pre-training Tasks

- evaluating 2 pre-training objectives using exactly the same pre-training data, fine-tuning scheme and hyperparams as BERT_base

1. **No NSP**
- bidirectional model trained using masked LM, without NSP

2. **LTR & No NSP**
- left-context only trained using a standard LTR (left-to-right) model rather than MLM
- no NSP
- comparable to OpenAI GPT, using a larger training dataset, their input representation and fine-tuning scheme

3. **LTR & No NSP + BiLSTM**
- good faith attempt at strengthening LTR system
- added randomly initialized BiLSTM on top


**Discussion**
- no NSP hurts performance significantly on QNLI, MNLI, SQuAD 1.1
- LTR performs worse than MLM on all tasks (especially MRPC, SQuAD)
	- adding BiLSTM helps, but still worse than bidirectional models
	- adding BiLISTM hurts performance on GLUE tasks

### 5.2 Effect Of Model Size

- BERTs with different num of layers, hidden units, attention heads
- same hyperparameters and training procedure
- results in table 6: 	
	- #L - num of layers
	- #H - hidden size
	- #A - num of attention heads
	- LM (ppl) - masked LM perplexity of held-out training data
- scaling to extreme model sizes leads to large improvements on very small scale tasks (provided that the model has been sufficiently pre-trained)
- we hypothesize that when the model is fine-tuned directly on the downstream tasks and uses only a very small number of randomly initialized additional parameters, the taskspecific models can benefit from the larger, more expressive pre-trained representations even when downstream task data is very small


### 5.3 Feature-based Approach with BERT

- fine-tuning approach: simple classification layer is added to the pre-trained model, all params jointly fine-tuned on a downstream task
- feature-based approach has some advantages
	- not all tasks can be easily represented by a Transformer encoder arch, they require some task-specific model arch to be added
	- major computational benefits to pre-compute an expensive representation of the training data once and run many experiments with cheaper models on top of this repr
- BERT for CoNLL-2003 Named Entity Recognition (NER) task
- BERT_large performs competitively with SOTA methods
- BERT is effective for both fine-tuning and feature-based approaches

---


## 6. Conclusion

- rich, unsupervised pre-training is an integral part of many understanding systems
- these results enable even low-resource tasks to benefit from deep unidirectional architectures
- our major contribution: deep bidirectional architectures
	- to tackle a broad set of NLP tasks