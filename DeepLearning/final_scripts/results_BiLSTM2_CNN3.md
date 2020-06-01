
- 1
```
10560/10592 [============================>.] - ETA: 0s - loss: 0.0661 - acc: 0.9750 - rec: 0.9552 - prec: 0.9692 - f1: 0.9597
Epoch 00020: val_f1 did not improve from 0.65814

10592/10592 [==============================] - 63s 6ms/sample - loss: 0.0660 - acc: 0.9751 - rec: 0.9553 - prec: 0.9693 - f1: 0.9598 - val_loss: 1.0850 - val_acc: 0.7462 - val_rec: 0.5874 - val_prec: 0.6273 - val_f1: 0.5975
Epoch 00020: early stopping

2592/2648 [============================>.] - ETA: 0s - loss: 1.0879 - acc: 0.7458 - rec: 0.5839 - prec: 0.6223 - f1: 0.5922
2648/2648 [==============================] - 2s 935us/sample - loss: 1.0850 - acc: 0.7462 - rec: 0.5832 - prec: 0.6214 - f1: 0.5917

SCORES:
[1.0850487756585065, 0.74622357, 0.5832009, 0.6214002, 0.5916651]

Arguments:
----------
Namespace(LR=0.001, data_file='../../Dataset-OLID/OLIDv1.0/data_subtask_a.csv', dropout=0.5, emb_dim=300, emb_file='../../../0_embeddings/glove.6B/glove.6B.300d.txt', kernel_size=3, lstm_out=32, max_len=64, model_name='modelKeras', model_type='BiLSTM2_CNN3_model', num_epochs=50, num_filters=16, oov_tok='<OOV>', pad_type='post', pool_size=2, preproc='remove_stopwords_and_punctuation_textblob', strides=1, test_file='../../Dataset-OLID/OLIDv1.0/test_data_subtask_a.csv', train_portion=0.8, trunc_type='post', verbose=1, vocab_size=7500)

Scores on val:
2624/2648 [============================>.] - ETA: 0s - loss: 0.5142 - acc: 0.7748 - rec: 0.6796 - prec: 0.6550 - f1: 0.6582
2648/2648 [==============================] - 5s 2ms/sample - loss: 0.5116 - acc: 0.7761 - rec: 0.6835 - prec: 0.6562 - f1: 0.6606
[0.5115537531336268, 0.7760574, 0.68348515, 0.6561736, 0.6606434]

Scores on test:
832/860 [============================>.] - ETA: 0s - loss: 0.4316 - acc: 0.8065 - rec: 0.6323 - prec: 0.6427 - f1: 0.6282
860/860 [==============================] - 1s 2ms/sample - loss: 0.4250 - acc: 0.8070 - rec: 0.6367 - prec: 0.6436 - f1: 0.6311
[0.4250453504712083, 0.80697674, 0.6366677, 0.64359885, 0.63111985]
```


- 2: 
```
10560/10592 [============================>.] - ETA: 0s - loss: 0.2081 - acc: 0.9177 - rec: 0.8706 - prec: 0.8804 - f1: 0.8682
Epoch 00008: val_f1 did not improve from 0.67534

10592/10592 [==============================] - 117s 11ms/sample - loss: 0.2079 - acc: 0.9179 - rec: 0.8710 - prec: 0.8806 - f1: 0.8685 - val_loss: 0.6538 - val_acc: 0.7708 - val_rec: 0.6524 - val_prec: 0.6511 - val_f1: 0.6407
Epoch 00008: early stopping

2648/2648 [==============================] - 5s 2ms/sample - loss: 0.6538 - acc: 0.7708 - rec: 0.6578 - prec: 0.6525 - f1: 0.6471

SCORES:
[0.6538196526625365, 0.7707704, 0.65780216, 0.652484, 0.6471314]

Arguments:
----------
Namespace(LR=0.001, data_file='../../Dataset-OLID/OLIDv1.0/data_subtask_a.csv', dropout=0.5, emb_dim=300, emb_file='../../../0_embeddings/glove.6B/glove.6B.300d.txt', kernel_size=3, lstm_out=32, max_len=64, model_name='modelKeras2', model_type='BiLSTM2_CNN3_model', num_epochs=10, num_filters=16, oov_tok='<OOV>', pad_type='post', pool_size=2, preproc='remove_stopwords_and_punctuation_textblob', strides=1, test_file='../../Dataset-OLID/OLIDv1.0/test_data_subtask_a.csv', train_portion=0.8, trunc_type='post', verbose=1, vocab_size=7500)

Scores on val:
2648/2648 [==============================] - 6s 2ms/sample - loss: 0.4683 - acc: 0.7855 - rec: 0.6924 - prec: 0.6698 - f1: 0.6711
[0.46833498735442264, 0.7854985, 0.6923805, 0.6697642, 0.6711001]

Scores on test:
860/860 [==============================] - 2s 2ms/sample - loss: 0.4157 - acc: 0.8395 - rec: 0.6402 - prec: 0.7460 - f1: 0.6778
[0.41568076769972956, 0.8395349, 0.6401795, 0.7460131, 0.6777801]

```

- 3: 
```
10560/10592 [============================>.] - ETA: 0s - loss: 0.2065 - acc: 0.9172 - rec: 0.8674 - prec: 0.8833 - f1: 0.8689
Epoch 00008: val_f1 did not improve from 0.65006

10592/10592 [==============================] - 117s 11ms/sample - loss: 0.2061 - acc: 0.9175 - rec: 0.8678 - prec: 0.8836 - f1: 0.8693 - val_loss: 0.6638 - val_acc: 0.7719 - val_rec: 0.6197 - val_prec: 0.6671 - val_f1: 0.6311
Epoch 00008: early stopping

2648/2648 [==============================] - 4s 1ms/sample - loss: 0.6638 - acc: 0.7719 - rec: 0.6182 - prec: 0.6653 - f1: 0.6316

SCORES:
[0.6638426927011178, 0.77190334, 0.61817306, 0.66533697, 0.6315716]

Arguments:
----------
Namespace(LR=0.001, data_file='../../Dataset-OLID/OLIDv1.0/data_subtask_a.csv', dropout=0.5, emb_dim=300, emb_file='../../../0_embeddings/glove.6B/glove.6B.300d.txt', kernel_size=3, lstm_out=32, max_len=64, model_name='modelKeras3', model_type='BiLSTM2_CNN3_model', num_epochs=10, num_filters=16, oov_tok='<OOV>', pad_type='post', pool_size=2, preproc='remove_stopwords_and_punctuation_textblob', strides=1, test_file='../../Dataset-OLID/OLIDv1.0/test_data_subtask_a.csv', train_portion=0.8, trunc_type='post', verbose=1, vocab_size=7500)

Scores on val:
2648/2648 [==============================] - 6s 2ms/sample - loss: 0.4726 - acc: 0.7764 - rec: 0.6623 - prec: 0.6603 - f1: 0.6519
[0.472612017951343, 0.776435, 0.6622757, 0.66026396, 0.65193844]

Scores on test:
860/860 [==============================] - 2s 2ms/sample - loss: 0.4370 - acc: 0.7988 - rec: 0.6339 - prec: 0.6306 - f1: 0.6239
[0.4370402976523998, 0.7988372, 0.6339443, 0.6305977, 0.6238962]

```


- 4: 
```
10560/10592 [============================>.] - ETA: 0s - loss: 0.2050 - acc: 0.9181 - rec: 0.8733 - prec: 0.8836 - f1: 0.8711
Epoch 00008: val_f1 did not improve from 0.66801

10592/10592 [==============================] - 60s 6ms/sample - loss: 0.2050 - acc: 0.9181 - rec: 0.8734 - prec: 0.8835 - f1: 0.8712 - val_loss: 0.7017 - val_acc: 0.7640 - val_rec: 0.6616 - val_prec: 0.6426 - val_f1: 0.6384
Epoch 00008: early stopping

2648/2648 [==============================] - 2s 853us/sample - loss: 0.7017 - acc: 0.7640 - rec: 0.6486 - prec: 0.6428 - f1: 0.6340

SCORES:
[0.7017103718576835, 0.7639728, 0.64864415, 0.6427643, 0.63395333]

Arguments:
----------
Namespace(LR=0.001, data_file='../../Dataset-OLID/OLIDv1.0/data_subtask_a.csv', dropout=0.5, emb_dim=300, emb_file='../../../0_embeddings/glove.6B/glove.6B.300d.txt', kernel_size=3, lstm_out=32, max_len=64, model_name='modelKeras4', model_type='BiLSTM2_CNN3_model', num_epochs=10, num_filters=16, oov_tok='<OOV>', pad_type='post', pool_size=2, preproc='remove_stopwords_and_punctuation_textblob', strides=1, test_file='../../Dataset-OLID/OLIDv1.0/test_data_subtask_a.csv', train_portion=0.8, trunc_type='post', verbose=1, vocab_size=7500)

Scores on val:
2648/2648 [==============================] - 4s 2ms/sample - loss: 0.4802 - acc: 0.7761 - rec: 0.7222 - prec: 0.6461 - f1: 0.6717
[0.4802256796475263, 0.7760574, 0.72215664, 0.64612585, 0.67174774]

Scores on test:
860/860 [==============================] - 1s 1ms/sample - loss: 0.4500 - acc: 0.7965 - rec: 0.7184 - prec: 0.6057 - f1: 0.6447
[0.44995174227758894, 0.79651165, 0.718423, 0.6056611, 0.6447178]

```

- 5
```
10560/10592 [============================>.] - ETA: 0s - loss: 0.2471 - acc: 0.8990 - rec: 0.8449 - prec: 0.8522 - f1: 0.8404
Epoch 00007: val_f1 did not improve from 0.65223

10592/10592 [==============================] - 62s 6ms/sample - loss: 0.2469 - acc: 0.8991 - rec: 0.8454 - prec: 0.8521 - f1: 0.8406 - val_loss: 0.6213 - val_acc: 0.7662 - val_rec: 0.6704 - val_prec: 0.6464 - val_f1: 0.6476
Epoch 00007: early stopping

2648/2648 [==============================] - 3s 953us/sample - loss: 0.6213 - acc: 0.7662 - rec: 0.6697 - prec: 0.6383 - f1: 0.6440

SCORES:
[0.6212904421314372, 0.7662387, 0.66966134, 0.6383004, 0.6440029]

Arguments:
----------
Namespace(LR=0.001, data_file='../../Dataset-OLID/OLIDv1.0/data_subtask_a.csv', dropout=0.5, emb_dim=300, emb_file='../../../0_embeddings/glove.6B/glove.6B.300d.txt', kernel_size=3, lstm_out=32, max_len=64, model_name='modelKeras5', model_type='BiLSTM2_CNN3_model', num_epochs=10, num_filters=16, oov_tok='<OOV>', pad_type='post', pool_size=2, preproc='remove_stopwords_and_punctuation_textblob', strides=1, test_file='../../Dataset-OLID/OLIDv1.0/test_data_subtask_a.csv', train_portion=0.8, trunc_type='post', verbose=1, vocab_size=7500)

Scores on val:

2648/2648 [==============================] - 4s 2ms/sample - loss: 0.4609 - acc: 0.7980 - rec: 0.6037 - prec: 0.7390 - f1: 0.6532
[0.4609359178208152, 0.7979607, 0.6036898, 0.7389714, 0.65319073]

Scores on test:
860/860 [==============================] - 1s 1ms/sample - loss: 0.4168 - acc: 0.8349 - rec: 0.4923 - prec: 0.8356 - f1: 0.6028
[0.41679389851037846, 0.83488375, 0.49225098, 0.83561146, 0.60275805]

```

- 6: 
```
10560/10592 [============================>.] - ETA: 0s - loss: 0.2138 - acc: 0.9122 - rec: 0.8699 - prec: 0.8668 - f1: 0.8622
Epoch 00008: val_f1 did not improve from 0.66164

10592/10592 [==============================] - 58s 5ms/sample - loss: 0.2135 - acc: 0.9123 - rec: 0.8703 - prec: 0.8668 - f1: 0.8624 - val_loss: 0.6733 - val_acc: 0.7704 - val_rec: 0.6215 - val_prec: 0.6588 - val_f1: 0.6253
Epoch 00008: early stopping

2648/2648 [==============================] - 2s 821us/sample - loss: 0.6733 - acc: 0.7704 - rec: 0.6304 - prec: 0.6590 - f1: 0.6332

SCORES:
[0.6732884264604563, 0.7703928, 0.6304329, 0.65896577, 0.6332082]

Arguments:
----------
Namespace(LR=0.001, data_file='../../Dataset-OLID/OLIDv1.0/data_subtask_a.csv', dropout=0.5, emb_dim=300, emb_file='../../../0_embeddings/glove.6B/glove.6B.300d.txt', kernel_size=3, lstm_out=32, max_len=64, model_name='modelKeras6', model_type='BiLSTM2_CNN3_model', num_epochs=10, num_filters=16, oov_tok='<OOV>', pad_type='post', pool_size=2, preproc='remove_stopwords_and_punctuation_textblob', strides=1, test_file='../../Dataset-OLID/OLIDv1.0/test_data_subtask_a.csv', train_portion=0.8, trunc_type='post', verbose=1, vocab_size=7500)

Scores on val:
2648/2648 [==============================] - 5s 2ms/sample - loss: 0.4747 - acc: 0.7844 - rec: 0.6410 - prec: 0.6927 - f1: 0.6522
[0.4746896716403097, 0.78436553, 0.64104974, 0.69269633, 0.6522339]

Scores on test:
860/860 [==============================] - 1s 2ms/sample - loss: 0.4283 - acc: 0.8384 - rec: 0.5658 - prec: 0.7707 - f1: 0.6428
[0.42831006951110306, 0.8383721, 0.5657954, 0.77070045, 0.6428203]

```

- 7: 
```
Epoch 9/10
10560/10592 [============================>.] - ETA: 0s - loss: 0.1794 - acc: 0.9336 - rec: 0.9003 - prec: 0.9027 - f1: 0.8964
Epoch 00009: val_f1 did not improve from 0.65290

10592/10592 [==============================] - 61s 6ms/sample - loss: 0.1799 - acc: 0.9333 - rec: 0.8995 - prec: 0.9027 - f1: 0.8960 - val_loss: 0.7405 - val_acc: 0.7613 - val_rec: 0.6288 - val_prec: 0.6432 - val_f1: 0.6238
Epoch 00009: early stopping

2648/2648 [==============================] - 2s 858us/sample - loss: 0.7405 - acc: 0.7613 - rec: 0.6214 - prec: 0.6445 - f1: 0.6238

SCORES:
[0.7405295955450513, 0.7613293, 0.62137127, 0.6445255, 0.6237822]

Arguments:
----------
Namespace(LR=0.001, data_file='../../Dataset-OLID/OLIDv1.0/data_subtask_a.csv', dropout=0.5, emb_dim=300, emb_file='../../../0_embeddings/glove.6B/glove.6B.300d.txt', kernel_size=3, lstm_out=32, max_len=64, model_name='modelKeras7', model_type='BiLSTM2_CNN3_model', num_epochs=10, num_filters=16, oov_tok='<OOV>', pad_type='post', pool_size=2, preproc='remove_stopwords_and_punctuation_textblob', strides=1, test_file='../../Dataset-OLID/OLIDv1.0/test_data_subtask_a.csv', train_portion=0.8, trunc_type='post', verbose=1, vocab_size=7500)

Scores on val:
2648/2648 [==============================] - 4s 2ms/sample - loss: 0.5068 - acc: 0.7727 - rec: 0.6882 - prec: 0.6535 - f1: 0.6595
[0.5067592412233353, 0.7726586, 0.6881974, 0.6534644, 0.65949154]

Scores on test:
860/860 [==============================] - 2s 2ms/sample - loss: 0.4504 - acc: 0.7965 - rec: 0.6628 - prec: 0.6195 - f1: 0.6297
[0.4504350975502369, 0.79651165, 0.66279846, 0.6195279, 0.62969714]

```

- 8: 
```
10560/10592 [============================>.] - ETA: 0s - loss: 0.1871 - acc: 0.9266 - rec: 0.8819 - prec: 0.8947 - f1: 0.8825
Epoch 00009: val_f1 did not improve from 0.66055

10592/10592 [==============================] - 61s 6ms/sample - loss: 0.1872 - acc: 0.9265 - rec: 0.8814 - prec: 0.8951 - f1: 0.8823 - val_loss: 0.6931 - val_acc: 0.7632 - val_rec: 0.6332 - val_prec: 0.6464 - val_f1: 0.6297
Epoch 00009: early stopping

2648/2648 [==============================] - 2s 850us/sample - loss: 0.6931 - acc: 0.7632 - rec: 0.6326 - prec: 0.6448 - f1: 0.6292

SCORES:
[0.6931077311226248, 0.7632175, 0.63261044, 0.6448371, 0.6292006]

Arguments:
----------
Namespace(LR=0.001, data_file='../../Dataset-OLID/OLIDv1.0/data_subtask_a.csv', dropout=0.5, emb_dim=300, emb_file='../../../0_embeddings/glove.6B/glove.6B.300d.txt', kernel_size=3, lstm_out=32, max_len=64, model_name='modelKeras8', model_type='BiLSTM2_CNN3_model', num_epochs=10, num_filters=16, oov_tok='<OOV>', pad_type='post', pool_size=2, preproc='remove_stopwords_and_punctuation_textblob', strides=1, test_file='../../Dataset-OLID/OLIDv1.0/test_data_subtask_a.csv', train_portion=0.8, trunc_type='post', verbose=1, vocab_size=7500)

Scores on val:
2648/2648 [==============================] - 4s 2ms/sample - loss: 0.4903 - acc: 0.7874 - rec: 0.6494 - prec: 0.6880 - f1: 0.6575
[0.49034943645454243, 0.7873867, 0.6494256, 0.6880417, 0.65752524]

Scores on test:
860/860 [==============================] - 1s 2ms/sample - loss: 0.4229 - acc: 0.8279 - rec: 0.6158 - prec: 0.7122 - f1: 0.6483
[0.4228520486243936, 0.82790697, 0.6158101, 0.7122295, 0.6483007]

```