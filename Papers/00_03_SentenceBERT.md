# Paper 08: [Sentence-BERT: Sentence Embeddings using Siamese BERT-Networks](https://arxiv.org/abs/1908.10084)

## 0. Abstract

- BERT and RoBERTa set new SOTA on semantic text similarity (STS)
	- requires both sentences being fed -> massive computational overhead
- BERT unsuitable for semantic similarity search and clustering

Sentence-BERT (SBERT)
- modification of BERT
- uses siamese and triplet network structures
- goal: derive semantically meaningful sentence embeddings
	- compared using cosine similarity
- reduces cost for finding most similar pair from 65 hours (BERT) to 5 seconds (SBERT), while maintaining accuracy


--- 


## 1. Introduction

- SentenceBERT
	- modified BERT: uses siamese and triplet networks to derive semantically meaningful sentence embeddings
- enable new tasks: 
	- large-scale semantic similarity comparison, clustering, information retrieval via semantic search 
BERT uses cross encoder: two sentences are passed to the transformer and the target value is predicted
	- unsuitable for various pair regression tasks (too many combinations)
- common method for clustering and semantic search: 
	- map each sentence to a vector space such that semantically similar sentences are close
- researchers: trying to get sentence embeddings out of BERT by inputing only one sentence and do some processing and hacks
	- yield rather bad sentence embeddings, often worse than averaging GloVe embeddings


SentenceBERT
- siamese net arch enables deriving fixed-size vectors for input sentences
- semantically similar sentences with cosine-similarity of Manhatten / Euclidean distance
- fine-tune on NLI data
	- outperform SOTA sentence embedding methods like InferSent and Universal Sentence Encoder
- can be adapted to a specific task

--- 

## 2. Related Work

**BERT**
- pre-trained transformer net
- input: sentence-pair
- multi-head attention
- disadvantage: no independent sentence embeddings are computed -> hard to derive sentence embeddings from BERT

**Sentence embeddings**
- well studied area, dozens of proposed methods
	- Skip-Thought -> predict surrounding sentences
	- InferSent
	- Universal Sentence Encoder 
		- task on which sentence embeddings are trained significantly impacts their quality
		- SNLI datasets suitable for training sentence embeddings
- ... 


--- 

## 3. Model

- SBERT adds a pooling operation to the output of BERT / RoBERTa to derive a fixed sized sentence embedding
- 3 pooling strategies: 
	- using the output of `CLS` token
	- computing the mean of all output vectors (`MEAN`-Strategy)
		- default! 
	- computing max-over-time of the output vectors (`MAX`-Strategy)
- fine-tuning BERT (and RoBERTa)
	- siamese and triplet networks to update the weights, so the sent embeddings are semantically meaningful and can be compared with cosine-similarity
- experiment with different structures and objective functions

**Classification Objective Function**
- concatenate sentence embeddings u and v with element-wise difference
- ...
- cross-entropy loss

**Regression Objective Function**
- cosine-similarity between two sentence embeddings 
- mean-squared-error loss

**Triplet Objective Function**
- anchor sentence a, positive sentence p, negative sentence n
- triplet loss tunes the network: distance between a and p is smaller than the distance between a and n
- euclidean distance


### 3.1 Training Details

- SNLI (570k sentence pairs -> entailment / contradiction / neutral) and MultiNLI (430k sentence pairs) datasets
- fine-tune SBERT with 3-way softmay classifier objective function for 1 epoch
- batch_size = 16
- adam optimizer with LR = 2e-5
	- linear learning rate warm-up over 10% of the training data
- default pooling strategy: MEAN


## 4. Evaluation - Semantic Textual Similarity

- evaluate performance for STS (Semantic Textual Similarity) tasks
- SOTA methods often learn a complex regression function that maps sentence embeddings to a similarity score
	- work pair-wise -> combinatorial explosion
- we use cosine-similarity

### 4.1 Unsupervised STS

- evaluate performance of SBERT on STS without using any STS specific training data
- we compute the Spearman’s rank correlation between the cosine-similarity of the sentence embeddings and the gold labels
- directly using the output of BERT -> poor performance
- SBERT outperforms InferSent and Universal Sentence Encoder substantially

### 4.2 Supervised STS

- STSb (STS benchmark) dataset
- training set to fine-tune SBERT using the regression objective function
- prediction time: compute cosine-similarity between the sentence embeddings


### 4.3 Argument Facet Similarity

- AFS (Argument Facet Similarity) corpus
	- 6k argument pairs on topics: gun control, gay marriage, death penalty
	- annotation: 0 (different topic) - 5 (completely equivalent)
- STS data usually descriptive, AFS data are argumentative excerpts (izvadci) from dialogs
	- similar arguments: similar claims + similar reasoning
- 2 topic in training set, 1 topic in testing
- not so good results, right?

### 4.4 Wikipedia Sections Distinction

- for train,dev,test
- articles separated into distinct sections focusing on certain aspects
- [Dor et al.] assumes that sentences in the same section are thematically closer than sentences in different sections
	- -> large dataset of weakly labeled sentence triplets: anchor, positive (same section), negative (different section)
- Triplet Objective

---

## 5. Evaluation - SentEval

- the purpose of SBERT sentence embeddings are not to be used for transfer learning for other tasks
- here BERT is more suitable
-  appears that the sentence embeddings from SBERT capture well sentiment information

--- 

## 6. Ablation Study

- ablation = amputacija
- evaluated different pooling strategies
- for classification objective function, we evaluate different concatenation methods
- for each possible configuration, we train SBERT with 10 different random seeds and average the performances
- the objective function depends on the annotated dataset
- classification objective: 
	- pooling strategy -> minor impact
	- concatenation mode -> much larger impact
- regression objective: 
	- pooling strategy -> large impact

---

## 7. Computational Efficiency

- Sentence embeddings need potentially be computed for Millions of sentences, hence, a high computation speed is desired
- Performances were measured on a server with Intel i7-5820K CPU @ 3.30GHz, Nvidia Tesla V100 GPU, CUDA 9.2 and cuDNN

--- 

## 8. Conclusion

- BERT out-of-the-box maps sentences to a vector space that is rather unsuitable to be used with common similarity measures like cosine-similarity
- SentenceBERT!
	- fine-tunes BERT in a siamese / triplet network architecture
	- evaluated the quality on various common benchmarks
- Replacing BERT with RoBERTa did not yield a significant improvement in our experiments
- SBERT is computationally efficient

