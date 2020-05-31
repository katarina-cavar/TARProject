- LSTM model: 
```
Epoch 20/20


10560/10592 [============================>.] - ETA: 0s - loss: 0.6352 - acc: 0.6684
10592/10592 [==============================] - 11s 1ms/sample - loss: 0.6353 - acc: 0.6682 - val_loss: 0.6355 - val_acc: 0.6681
0it [00:00, ?it/s]

2648/2648 [==============================] - 0s 157us/sample - loss: 0.6355 - acc: 0.6681
0it [00:00, ?it/s]

SCORES:
[0.635544828777947, 0.66805136]

```

- LSTM model 2: 
```
Epoch 20/20


10592/10592 [==============================] - 9s 841us/sample - loss: 0.5795 - acc: 0.6719 - val_loss: 0.5881 - val_acc: 0.7024


2648/2648 [==============================] - 0s 149us/sample - loss: 0.5881 - acc: 0.7024

SCORES:
[0.5880656010074558, 0.7024169]

```



- BiLSTM_model: (emb=16)

```
10528/10592 [============================>.] - ETA: 0s - loss: 0.3104 - acc: 0.8750
10560/10592 [============================>.] - ETA: 0s - loss: 0.3105 - acc: 0.8749
10592/10592 [==============================] - 55s 5ms/sample - loss: 0.3108 - acc: 0.8748 - val_loss: 0.6931 - val_acc: 0.7526



2464/2648 [==========================>...] - ETA: 0s - loss: 0.6925 - acc: 0.7508
2560/2648 [============================>.] - ETA: 0s - loss: 0.6949 - acc: 0.7508
2648/2648 [==============================] - 2s 736us/sample - loss: 0.6931 - acc: 0.7526

SCORES:
[0.693056226406933, 0.7526435]


```

- BiLSTM_model: (emb=128)
```
10528/10592 [============================>.] - ETA: 0s - loss: 0.1115 - acc: 0.9576
10560/10592 [============================>.] - ETA: 0s - loss: 0.1117 - acc: 0.9577
10592/10592 [==============================] - 53s 5ms/sample - loss: 0.1120 - acc: 0.9575 - val_loss: 1.3382 - val_acc: 0.7073


2592/2648 [============================>.] - ETA: 0s - loss: 1.3493 - acc: 0.7060
2648/2648 [==============================] - 2s 658us/sample - loss: 1.3382 - acc: 0.7073

SCORES:
[1.3381895150122687, 0.7073263]

```

- BiLSTM_model: (emb=128, remove "user" in preprocessing)
```
10560/10592 [============================>.] - ETA: 0s - loss: 0.1070 - acc: 0.9585
10592/10592 [==============================] - 53s 5ms/sample - loss: 0.1070 - acc: 0.9586 - val_loss: 1.3295 - val_acc: 0.7115


2624/2648 [============================>.] - ETA: 0s - loss: 1.3384 - acc: 0.7100
2648/2648 [==============================] - 2s 605us/sample - loss: 1.3295 - acc: 0.7115

SCORES:
[1.329469474870993, 0.7114804]

```

- BiLSTM_model: (emb=32, remove "user" in preprocessing)
```
10528/10592 [============================>.] - ETA: 0s - loss: 0.2064 - acc: 0.9146
10592/10592 [==============================] - 15s 1ms/sample - loss: 0.2062 - acc: 0.9147 - val_loss: 0.9119  val_acc: 0.7311



2528/2648 [===========================>..] - ETA: 0s - loss: 0.9227 - acc: 0.7275
2648/2648 [==============================] - 1s 276us/sample - loss: 0.9119 - acc: 0.7311

SCORES:
[0.9119464914424181, 0.73111784]

--> Saved model to disk.
Namespace(data_file='../Dataset-OLID/OLIDv1.0/data_subtask_a.csv', emb_dim=32, max_len=64, model_name='modelKeas_removeUser_emb128', model_type='BiLSTM_model', num_epochs=20, oov_tok='<OOV>', pad_type='post', preproc='reove_stopwords_and_punctuation_textblob', train_portion=0.8, trunc_type='post', vocab_size=2500)


```



- BiLSTM_model: (emb=32, remove "user" in preprocessing, vocab = 7500)
```
Epoch 8: 
10464/10592 [============================>.] - ETA: 0s - loss: 0.1812 - acc: 0.9284
10528/10592 [============================>.] - ETA: 0s - loss: 0.1814 - acc: 0.9284
10592/10592 [==============================] - 15s 1ms/sample - loss: 0.1818 - acc: 0.9282 - val_loss: 0.8531 - val_acc: 0.7300


Epoch 20: 

10528/10592 [============================>.] - ETA: 0s - loss: 0.0869 - acc: 0.9676
10592/10592 [==============================] - 16s 1ms/sample - loss: 0.0871 - acc: 0.9675 - val_loss: 1.2859 - val_acc: 0.7066


2528/2648 [===========================>..] - ETA: 0s - loss: 1.2989 - acc: 0.7033
2648/2648 [==============================] - 1s 270us/sample - loss: 1.2859 - acc: 0.7066

SCORES:
[1.2858698289740123, 0.706571]

--> Saved model to disk.
Namespace(data_file='../Dataset-OLID/OLIDv1.0/data_subtask_a.csv', emb_dim=32, max_len=64, model_name='modelKeras_removeUser_emb128', model_type='BiLSTM_model', num_epochs=20, oov_tok='<OOV>', pad_type='post', preproc='remove_stopwords_and_punctuation_textblob', train_portion=0.8, trunc_type='post', vocab_size=7500)



```



- BiLSTM_moreReg_model: (emb=32, remove "user" in preprocessing, vocab = 7500 + more reg)
```
Epoch 20: 

10560/10592 [============================>.] - ETA: 0s - loss: 0.1233 - acc: 0.9509
10592/10592 [==============================] - 18s 2ms/sample - loss: 0.1235 - acc: 0.9507 - val_loss: 1.1767 - val_acc: 0.7262


2528/2648 [===========================>..] - ETA: 0s - loss: 1.1913 - acc: 0.7235
2648/2648 [==============================] - 1s 287us/sample - loss: 1.1767 - acc: 0.7262

SCORES:
[1.1767321643152266, 0.72620845]

--> Saved model to disk.
Namespace(data_file='../Dataset-OLID/OLIDv1.0/data_subtask_a.csv', emb_dim=32, max_len=64, model_name='modelKeras_removeUser_emb128', model_type='BiLSTM_moreReg_model', num_epochs=20, oov_tok='<OOV>', pad_type='post', preproc='remove_stopwords_and_punctuation_textblob', train_portion=0.8, trunc_type='post', vocab_size=7500)


```

- BiLSTM_moreReg_model2: (emb=32, remove "user" in preprocessing, vocab = 7500 + more reg)
```
10464/10592 [============================>.] - ETA: 0s - loss: 0.1373 - acc: 0.9481
10528/10592 [============================>.] - ETA: 0s - loss: 0.1371 - acc: 0.9481
10592/10592 [==============================] - 10s 900us/sample - loss: 0.1371 - acc: 0.9482 - val_loss: 1.0971 - val_acc: 0.7213

2496/2648 [===========================>..] - ETA: 0s - loss: 1.0936 - acc: 0.7204
2648/2648 [==============================] - 0s 151us/sample - loss: 1.0971 - acc: 0.7213

SCORES:
[1.0970553147108533, 0.7212991]

--> Saved model to disk.
Namespace(data_file='../Dataset-OLID/OLIDv1.0/data_subtask_a.csv', emb_dim=32, max_len=32, model_name='modelKeras_removeUser_emb128', model_type='BiLST_moreReg_model2', num_epochs=20, oov_tok='<OOV>', pad_type='post', preproc='remove_stopwords_and_punctuation_textblob', train_portion=0.8, trunc_type='ost', vocab_size=7500)

```



- CNN model (Dense = 64, num_filters = 32)
```
10304/10592 [============================>.] - ETA: 0s - loss: 0.0915 - acc: 0.9696
10592/10592 [==============================] - 1s 55us/sample - loss: 0.0919 - acc: 0.9696 - val_loss: 1.5685 - val_acc: 0.7217

  32/2648 [..............................] - ETA: 0s - loss: 2.0649 - acc: 0.5938
2648/2648 [==============================] - 0s 15us/sample - loss: 1.5685 - acc: 0.7217

SCORES:
[1.5684637249056306, 0.72167677]

```

- CNN model (Dense = 250, num_filters = 250)
```
10080/10592 [===========================>..] - ETA: 0s - loss: 0.0874 - acc: 0.9717
10592/10592 [==============================] - 1s 61us/sample - loss: 0.0888 - acc: 0.9711 - val_loss: 1.5820 - val_acc: 0.7005

  32/2648 [..............................] - ETA: 0s - loss: 1.9929 - acc: 0.5312
2648/2648 [==============================] - 0s 15us/sample - loss: 1.5820 - acc: 0.7005

SCORES:
[1.5820012715647949, 0.7005287]

```

- BiLSTM_CNN_model: 
```
10560/10592 [============================>.] - ETA: 0s - loss: 0.0299 - acc: 0.9899
10592/10592 [==============================] - 20s 2ms/sample - loss: 0.0299 - acc: 0.9899 - val_loss: 1.7418 - val_acc: 0.7149


2624/2648 [============================>.] - ETA: 0s - loss: 1.7518 - acc: 0.7142
2648/2648 [==============================] - 1s 272us/sample - loss: 1.7418 - acc: 0.7149

SCORES:
[1.7418145663428524, 0.71487916]

--> Saved model to disk.
Namespace(data_file='../Dataset-OLID/OLIDv1.0/data_subtask_a.csv', dropout=0.2, emb_dim=32, kernel_size=3, lstm_out=64, max_len=32, model_name='modelKeras_removeUser_emb128', model_type='BiLSTM_CNN_model', num_epochs=20, num_filters=250, oov_tok='<OOV>', pad_type='post', preproc='remove_stopwords_and_punctuation_textblob', strides=1, train_portion=0.8, trunc_type='post', vocab_size=7500)

```

### PREPROC="remove_punctuation"

- LSTM_model2:
```
10528/10592 [============================>.] - ETA: 0s - loss: 0.5755 - acc: 0.7299
10592/10592 [==============================] - 10s 925us/sample - loss: 0.5751 - acc: 0.7303 - val_loss: 0.6082 - val_acc: 0.6975


2592/2648 [============================>.] - ETA: 0s - loss: 0.6090 - acc: 0.6968
2648/2648 [==============================] - 0s 166us/sample - loss: 0.6082 - acc: 0.6975



SCORES:
[0.6082250519101353, 0.69750756]

```


- BiLSTM_model: 

```
10528/10592 [============================>.] - ETA: 0s - loss: 0.3071 - acc: 0.8678
10560/10592 [============================>.] - ETA: 0s - loss: 0.3069 - acc: 0.8678
10592/10592 [==============================] - 55s 5ms/sample - loss: 0.3070 - acc: 0.8677 - val_loss: 0.6913 - val_acc: 0.7455


2528/2648 [===========================>..] - ETA: 0s - loss: 0.6954 - acc: 0.7441
2624/2648 [============================>.] - ETA: 0s - loss: 0.6946 - acc: 0.7443
2648/2648 [==============================] - 2s 716us/sample - loss: 0.6913 - acc: 0.7455


SCORES:
[0.6913014680057133, 0.74546826]

```
