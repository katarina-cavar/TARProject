# [Transformers: Attention is All You Need](https://arxiv.org/abs/1706.03762)

---

## 0. Abstract 

- new simple network architecture, the Transformer, based solely on attention mechanisms, dispensing with recurrence and convolution entirely
	- dispense = izostaviti
- experiments on two machine translation tasks show these models to be superior in quality while being more parallelizable and requiring significantly less time to train


---

## 1. Introduction

- RNNs, LSTMs, Gated RNNs established as state-of-the-art
- RNN - sequential, precludes (sprječava) parallelization within training examples
- improvements:
	- factorization tricks
	- conditional computation
- attention mechianisms
	- became an integral part of compelling sequence modeling and transduction models
	- sometimes used with RNNs 
- **Transformer**
	- eschewing (izbjegavati) recurrence
	- relies entirely on attention mechanisms to draw global dependencies between input and output
	- significantly more parallelization
	- new state-of-the-art (SOTA) quality

--- 

## 2. Background

- goal: reducing sequential computation
	- Extended Neural GPU, ByteNet, ConvS2S
		-  number of operations required to relate signals from two arbitrary input or output positions grows in the distance between positions
		- more difficult to learn dependencies between distant position
- Transformer: 
	- constant num of operations
	- at the cost of reduced effective resolution due to averaging attention-weighted positions
	- solved: Multi-Head Attention
- self-attention
	- relating different positions of a single sequence to compute a representation of the sequence
	- tasks: 
		- reading comprehension
		- abstractive summarization
		- textual entailment
		- learning task-independent sentence representations
		- (all of these have references)
- end-to-end memory networks based on recurrent attention mechanisms (instead of sequence-aligned recurrence)
	- good for simple-language question answering and language modeling tasks
- Transformer
	- first model relying entirely on self-attention
	- without sequence-aligned RNNs or convolution

--- 

## 3. Model Architecture

- most competitive neural sequence transduction model have an **encoder-decoder** structure
- encoder: 
	- input sequence (symbols) to sequence of continuous representations **z**
- decoder: 
	- given z, generates an output sequence of symbols one element at a time
- model is [auto-regressive](https://www.google.com/search?q=autoregressive+model&oq=auto-regressi&aqs=chrome.1.69i57j0l7.2364j0j7&sourceid=chrome&ie=UTF-8)
- Transformer: 
	- stacked self-attention 
	- fully connected layers for both encoder and decoder

![Model Architecture](https://miro.medium.com/max/2880/1*BHzGVskWGS_3jEcYYi6miQ.png)

### 3.1 Encoder and Decoder Stacks

**Encoder**
- N=6 identical layers
- each layer 2 sub-layers
	- multi-head self-attention mechanism
	- position-wise fully connected feed-forward network
- residual connection around each of the two sub-layers, followed by feed-forward network
- `sub_output = LayerNorm(x + Sublayer(x))`



**Decoder**
- N=6 identical layers
- each layer 3 sublayers
	- multi-head self-attention
	- multi-head over output of encoder
	- position-wise fully connected feed-forward network
- predictions for position i can depend only on the known outputs at positions less than i

### 3.2 Attention

- attention function
	- mapping a query and a set of key-value pairs to an output
	- all variables are vectors
	- output = weighted sum of the values
	- weights - computed by a compatibility function of the query with the corresponding key

![Attention](https://pics.me.me/scaled-dot-product-attention-linear-matmul-concat-softmax-scaled-dot-product-h-50776120.png)

#### 3.2.1 Scaled Dot-Product Attention

- annotation: 
	- Q - query (dimenison d_k) - yes, same dimension as K
	- K - key (dimension d_k)
	- V - value (dimension d_v)
- formula: 

Attention(Q, K, V) = softmax( Q * K' / sqrt(d_k)) * V

- most common attentions: 
	- additive attentions
		- outperforms dot product without scaling for larger values of d_k
	- multiplicative attention (dot-product)
		- much faster and space-efficient in practice


#### 3.2.2. Multi-Head Attention

- linearly project the queries, keys and values h times with different, learned linear projections to dk, dk and dv dimensions
- perform the attention function in parallel
	- d_v-dimensional output values
- Multi-head attention allows the model to jointly attend to information from different representation subspaces at different positions


#### 3.2.3 Applications of Attention in our Model

- "enc-dec attention" layers
	- queries come from previous decoder layer
	- memory keys and values come from the output of enc
	- every position in dec can attend over all positions in input sequence
- enc
	- self-attention
	- K, V and Q come from the output of the previous layer in the encoder
	- each position in enc can attend to all positions in the previous layer of the encoder
- dec 
	- self-attention
	- each position in dec can attend to all positions in the decoder up to and including that position 
	- prevent leftward info flow to preserve auto-regressive property

### 3.3 Position-wise Feed-Forward Networks

- two lin transformations with a ReLU activation

FFN(x) = max(0, xW1 + b1) * W2 + b2

### 3.4 Embeddings and Softmax

- use learned embeddings to convert the input and output tokens to vectors of dimension d_model
- lin transformation and softmax to convert dec output to predicted next-token probabilities

### 3.5 Positional Encoding

- no recurrence, no convolution
- we must inject some info about relative or absolute position of the tokens in the sequence
	- **Positional Encodings**

---

## 4. Why Self-Attention

- comparing self-attention to RNN and CNN
	- total computational complexity per layer
	- amount of computation that can be parallelized (min # of sequential ops)
	- path length between long-range dependencies in the net
		- learning long-range dependencies is a key challenge
		- shorter paths -> easier to learn long-range dependencies
		- we compare max length between any two inp and out positions in the net
-  self-attention layers are faster than recurrent layers when the sequence length n is smaller than the representation dimensionality d
- self-attention could yield more interpretable models

---

## 5. Training

### 5.1 Training Data and Batching

- standard WMT 2014 English-German dataset
	- 4.5 mil sentence pairs
	- byte-pair encoding
	- 37k tokens vocab
- standard WMT 2014 English-German dataset
	- 36 mil sentence pairs
	- 32k word-piece vocab
- batch: approx 25k source and 25k target tokens

### 5.2 Hardware and schedule

- 8 NVIDIA p100 GPUs
- 100k steps for 12 hours
- big models 300k steps for 3.5 days

### 5.3 Optimizer

- adam optimizer

### 5.4 Regularization


**Residual Dropout**
- dropout to output of each sub-layer

**Label Smoothing**
- hurts perplexity, but improves accuracy and BLEU score


---

## 6. Results

### 6.1 Machine Translation

- big Transformer outperforms SOTA
- base model surpasses all previously published models and ensembles at a fraction of the training cost
- hyperparams... 

### 6.2 Model Variations

- variations... 
- determining compatibility is not easy and that a more sophisticated compatibility function than dot product may be beneficial
- bigger models are better, and dropout is very helpful in avoiding over-fitting
- replace our sinusoidal positional encoding with learned positional embeddings, and observe nearly identical results to the base model


### 6.3 English Constituency Parsing

- to evaluate if the Transformer can generalize to other tasks we performed experiments on English
constituency parsing
- challenges: 
	- output - strong structural constraints
	- output significantly longer than input
- configuration of the model... 
- model performs surprisingly well (even with the lack of task-specific tuning)


--- 

## 7. Conclusion

- the Transformer, the first sequence transduction model based entirely on attention
	- multi-headed self-attention
-  can be trained significantly faster than architectures based on recurrent or convolutional layers
- achieve new SOTA on WMT 2014 English-to-German and WMT 2014 English-to-French translation tasks


--- 

## Appendix: Attention Visualizations

- see for yourself :)