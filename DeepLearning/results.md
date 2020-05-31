- BiLSTM + CNN, dropout = 0.2
```
2592/2648 [============================>.] - ETA: 0s - loss: 0.8748 - acc: 0.7157 - rec: 0.7142 - prec: 0.5548 - f1: 0.6147
2648/2648 [==============================] - 1s 452us/sample - loss: 0.8726 - acc: 0.7160 - rec: 0.7164 - prec: 0.5537 - f1: 0.6150

SCORES:
[0.8725939700970837, 0.71601206, 0.71642405, 0.553717, 0.61497176]

Arguments:
----------
Namespace(LR=0.001, data_file='../../Dataset-OLID/OLIDv1.0/data_subtask_a.csv', dropout=0.2, emb_dim=300, emb_file='../../../0_embeddings/glove.6B/glove.6B.300d.txt', kernel_size=3, lstm_out=64, max_len=32, model_name='modelKeras', model_type='BiLSTM_CNN_model', num_epochs=5, num_filters=250, oov_tok='<OOV>', pad_type='post', preproc='remove_stopwords_and_punctuation_textblob', strides=1, test_file='../../Dataset-OLID/OLIDv1.0/test_data_subtask_a.csv', train_portion=0.8, trunc_type='post', verbose=1, vocab_size=7500)

Scores on val:

2648/2648 [==============================] - 2s 653us/sample - loss: 0.4681 - acc: 0.7881 - rec: 0.5997 - prec: 0.7206 - f1: 0.6455
[0.4680842542036062, 0.78814197, 0.59974986, 0.7206372, 0.64554024]

Scores on test:

860/860 [==============================] - 0s 556us/sample - loss: 0.4481 - acc: 0.8128 - rec: 0.5181 - prec: 0.6952 - f1: 0.5833
[0.44809937380081, 0.8127907, 0.51806104, 0.69519264, 0.58328027]

```

- BiLSTM2, dropout = 0.2
```
10528/10592 [============================>.] - ETA: 0s - loss: 0.2617 - acc: 0.8914 - rec: 0.8234 - prec: 0.8430 - f1: 0.8256
10560/10592 [============================>.] - ETA: 0s - loss: 0.2616 - acc: 0.8914 - rec: 0.8230 - prec: 0.8431 - f1: 0.8254
Epoch 00005: val_f1 did not improve from 0.64101

10592/10592 [==============================] - 72s 7ms/sample - loss: 0.2618 - acc: 0.8911 - rec: 0.8219 - prec: 0.8429 - f1: 0.8247 - val_loss: 0.6315 - val_acc: 0.7787 - val_rec: 0.5795 - val_prec: 0.6972 - val_f1: 0.6207
2592/2648 [============================>.] - ETA: 0s - loss: 0.6348 - acc: 0.7774 - rec: 0.5759 - prec: 0.6932 - f1: 0.6178
2648/2648 [==============================] - 3s 1ms/sample - loss: 0.6315 - acc: 0.7787 - rec: 0.5801 - prec: 0.6931 - f1: 0.6203

SCORES:
[0.6314637004608834, 0.7787009, 0.5800945, 0.6931429, 0.620253]

Arguments:
----------
Namespace(LR=0.001, data_file='../../Dataset-OLID/OLIDv1.0/data_subtask_a.csv', dropout=0.2, emb_dim=300, emb_file='../../../0_embeddings/glove.6B/glove.6B.300d.txt', kernel_size=3, lstm_out=64, max_len=32, model_name='modelKeras', model_type='BiLSTM2_model', num_epochs=5, num_filters=250, oov_tok='<OOV>', pad_type='post', preproc='remove_stopwords_and_punctuation_textblob', strides=1, test_file='../../Dataset-OLID/OLIDv1.0/test_data_subtask_a.csv', train_portion=0.8, trunc_type='post', verbose=1, vocab_size=7500)

Scores on val:
2624/2648 [============================>.] - ETA: 0s - loss: 0.5476 - acc: 0.7774 - rec: 0.6174 - prec: 0.6800 - f1: 0.6354
2648/2648 [==============================] - 7s 3ms/sample - loss: 0.5454 - acc: 0.7779 - rec: 0.6180 - prec: 0.6798 - f1: 0.6358
[0.5453694936372002, 0.77794564, 0.61797315, 0.6798401, 0.6358169]

Scores on test:
832/860 [============================>.] - ETA: 0s - loss: 0.5222 - acc: 0.8137 - rec: 0.5497 - prec: 0.7100 - f1: 0.6020
860/860 [==============================] - 2s 2ms/sample - loss: 0.5115 - acc: 0.8186 - rec: 0.5618 - prec: 0.7208 - f1: 0.6142
[0.5114860612292622, 0.81860465, 0.56175554, 0.72078055, 0.61424327]

```

- BiLSTM2, dropout = 0.5
```
10528/10592 [============================>.] - ETA: 0s - loss: 0.3476 - acc: 0.8527 - rec: 0.7280 - prec: 0.8154 - f1: 0.7586
10560/10592 [============================>.] - ETA: 0s - loss: 0.3472 - acc: 0.8528 - rec: 0.7283 - prec: 0.8156 - f1: 0.7589
Epoch 00005: val_f1 did not improve from 0.64999

10592/10592 [==============================] - 67s 6ms/sample - loss: 0.3471 - acc: 0.8529 - rec: 0.7284 - prec: 0.8162 - f1: 0.7592 - val_ls: 0.5756 - val_acc: 0.7874 - val_rec: 0.6072 - val_prec: 0.7143 - val_f1: 0.6440

2592/2648 [============================>.] - ETA: 0s - loss: 0.5795 - acc: 0.7859 - rec: 0.5930 - prec: 0.7082 - f1: 0.6340
2648/2648 [==============================] - 3s 1ms/sample - loss: 0.5756 - acc: 0.7874 - rec: 0.5968 - prec: 0.7088 - f1: 0.6365

SCORES:
[0.5755601013895248, 0.7873867, 0.59679914, 0.7088182, 0.6364951]

Arguments:
----------
Namespace(LR=0.001, data_file='../../Dataset-OLID/OLIDv1.0/data_subtask_a.csv', dropout=0.5, emb_dim=300, emb_file='../../../0_embeddings/gle.6B/glove.6B.300d.txt', kernel_size=3, lstm_out=64, max_len=32, model_name='modelKeras', model_type='BiLSTM2_model', num_epochs=5, num_filts=250, oov_tok='<OOV>', pad_type='post', preproc='remove_stopwords_and_punctuation_textblob', strides=1, test_file='../../Dataset-OLID/OLIDv0/test_data_subtask_a.csv', train_portion=0.8, trunc_type='post', verbose=1, vocab_size=7500)

Scores on val:
2624/2648 [============================>.] - ETA: 0s - loss: 0.4668 - acc: 0.7893 - rec: 0.6263 - prec: 0.7088 - f1: 0.6528
2648/2648 [==============================] - 7s 3ms/sample - loss: 0.4647 - acc: 0.7904 - rec: 0.6308 - prec: 0.7093 - f1: 0.6553
[0.46467545241387587, 0.79040784, 0.63082093, 0.70929545, 0.6553019]

Scores on test:
832/860 [============================>.] - ETA: 0s - loss: 0.4504 - acc: 0.8089 - rec: 0.5284 - prec: 0.6956 - f1: 0.5888
860/860 [==============================] - 2s 2ms/sample - loss: 0.4441 - acc: 0.8140 - rec: 0.5459 - prec: 0.7028 - f1: 0.6018
[0.44407594231672065, 0.81395346, 0.54589725, 0.70278984, 0.60183686]

```

- BiLSTM2 + CNN, dropout = 0.5
```
10528/10592 [============================>.] - ETA: 0s - loss: 0.2998 - acc: 0.8731 - rec: 0.7923 - prec: 0.8246 - f1: 0.7990
10560/10592 [============================>.] - ETA: 0s - loss: 0.2997 - acc: 0.8731 - rec: 0.7922 - prec: 0.8249 - f1: 0.7991
Epoch 00005: val_f1 did not improve from 0.66276

10592/10592 [==============================] - 48s 5ms/sample - loss: 0.3002 - acc: 0.8729 - rec: 0.7919 - prec: 0.8245 - f1: 0.7988 - val_loss: 0.5323 - val_acc: 0.7768 - val_rec: 0.6024 - val_prec: 0.6886 - val_f1: 0.6327

2592/2648 [============================>.] - ETA: 0s - loss: 0.5343 - acc: 0.7766 - rec: 0.6014 - prec: 0.6809 - f1: 0.6268
2648/2648 [==============================] - 2s 804us/sample - loss: 0.5323 - acc: 0.7768 - rec: 0.6016 - prec: 0.6802 - f1: 0.6268

SCORES:
[0.5323300512895843, 0.7768127, 0.6016353, 0.6801989, 0.6268024]

Arguments:
----------
Namespace(LR=0.001, data_file='../../Dataset-OLID/OLIDv1.0/data_subtask_a.csv', dropout=0.5, emb_dim=300, emb_file='../../../0_embeddings/glove.6B/glove.6B.300d.txt', kernel_size=3, lstm_out=64, max_len=32, model_name='modelKeras', model_type='BiLSTM2_CNN_model', num_epochs=5, num_filters=250, oov_tok='<OOV>', pad_type='post', preproc='remove_stopwords_and_punctuation_textblob', strides=1, test_file='../../Dataset-OLID/OLIDv1.0/test_data_subtask_a.csv', train_portion=0.8, trunc_type='post', verbose=1, vocab_size=7500)

Scores on val:
2592/2648 [============================>.] - ETA: 0s - loss: 0.4568 - acc: 0.8005 - rec: 0.6214 - prec: 0.7332 - f1: 0.6606
2648/2648 [==============================] - 3s 1ms/sample - loss: 0.4543 - acc: 0.8021 - rec: 0.6258 - prec: 0.7335 - f1: 0.6633
[0.45427784467751886, 0.8021148, 0.6258343, 0.7334866, 0.66327494]

Scores on test:
800/860 [==========================>...] - ETA: 0s - loss: 0.4254 - acc: 0.8275 - rec: 0.4947 - prec: 0.7902 - f1: 0.5952
860/860 [==============================] - 1s 1ms/sample - loss: 0.4165 - acc: 0.8337 - rec: 0.5116 - prec: 0.8011 - f1: 0.6105
[0.4164896349574244, 0.8337209, 0.51162326, 0.8010982, 0.61048555]

```


- BiLSTM2 + CNN, dropout = 0.5, epochs = 30
```
10496/10592 [============================>.] - ETA: 0s - loss: 0.0622 - acc: 0.9770 - rec: 0.9598 - prec: 0.9718 - f1: 0.9640
10528/10592 [============================>.] - ETA: 0s - loss: 0.0621 - acc: 0.9771 - rec: 0.9599 - prec: 0.9719 - f1: 0.9641
10560/10592 [============================>.] - ETA: 0s - loss: 0.0620 - acc: 0.9772 - rec: 0.9601 - prec: 0.9719 - f1: 0.9642
Epoch 00018: val_f1 did not improve from 0.65706

10592/10592 [==============================] - 53s 5ms/sample - loss: 0.0619 - acc: 0.9772 - rec: 0.9602 - prec: 0.9718 - f1: 0.9642 - val_loss: 1.2032 - val_acc: 0.7458 - val_rec: 0.5806 - val_prec: 0.6264 - val_f1: 0.5893
Epoch 00018: early stopping

2592/2648 [============================>.] - ETA: 0s - loss: 1.2044 - acc: 0.7450 - rec: 0.5768 - prec: 0.6223 - f1: 0.5889
2648/2648 [==============================] - 3s 1ms/sample - loss: 1.2032 - acc: 0.7458 - rec: 0.5763 - prec: 0.6229 - f1: 0.5891

SCORES:
[1.203189299726054, 0.7458459, 0.57630926, 0.62294126, 0.58911484]

Arguments:
----------
Namespace(LR=0.001, data_file='../../Dataset-OLID/OLIDv1.0/data_subtask_a.csv', dropout=0.5, emb_dim=300, emb_file='../../../0_embeddings/glove.6B/glove.6B.300d.txt', kernel_size=3, lstm_out=64, max_len=32, model_name='modelKeras', model_type='BiLSTM2_CNN_model', num_epochs=30, num_filters=250, oov_tok='<OOV>', pad_type='post', preproc='remove_stopwords_and_punctuation_textblob', strides=1, test_file='../../Dataset-OLID/OLIDv1.0/test_data_subtask_a.csv', train_portion=0.8, trunc_type='post', verbose=1, vocab_size=7500)

Scores on val:
2624/2648 [============================>.] - ETA: 0s - loss: 0.4749 - acc: 0.7782 - rec: 0.6711 - prec: 0.6613 - f1: 0.6567
2648/2648 [==============================] - 4s 2ms/sample - loss: 0.4731 - acc: 0.7791 - rec: 0.6751 - prec: 0.6614 - f1: 0.6584
[0.4730728546838386, 0.77907854, 0.67510617, 0.6613604, 0.6583817]

Scores on test:
832/860 [============================>.] - ETA: 0s - loss: 0.4524 - acc: 0.7921 - rec: 0.6133 - prec: 0.6164 - f1: 0.6041
860/860 [==============================] - 1s 2ms/sample - loss: 0.4490 - acc: 0.7942 - rec: 0.6230 - prec: 0.6195 - f1: 0.6105
[0.4490047181761542, 0.79418606, 0.62299484, 0.61947393, 0.61052346]

```

- BiLSTM3 + CNN3, max_len = 32
```
10528/10592 [============================>.] - ETA: 0s - loss: 0.3145 - acc: 0.8665 - rec: 0.7918 - prec: 0.8062 - f1: 0.7892
10560/10592 [============================>.] - ETA: 0s - loss: 0.3144 - acc: 0.8666 - rec: 0.7920 - prec: 0.8066 - f1: 0.7896
Epoch 00005: val_f1 did not improve from 0.66985

10592/10592 [==============================] - 67s 6ms/sample - loss: 0.3144 - acc: 0.8666 - rec: 0.7920 - prec: 0.8069 - f1: 0.7898 - val_loss: 0.5477 - val_acc: 0.7806 - val_rec: 0.6252 - val_prec: 0.6815 - val_f1: 0.6417

2592/2648 [============================>.] - ETA: 0s - loss: 0.5516 - acc: 0.7797 - rec: 0.6253 - prec: 0.6802 - f1: 0.6422
2648/2648 [==============================] - 2s 927us/sample - loss: 0.5477 - acc: 0.7806 - rec: 0.6263 - prec: 0.6799 - f1: 0.6428

SCORES:
[0.5476927190028649, 0.7805891, 0.62630713, 0.6798762, 0.64278525]

Arguments:
----------
Namespace(LR=0.001, data_file='../../Dataset-OLID/OLIDv1.0/data_subtask_a.csv', dropout=0.5, emb_dim=300, emb_file='../../../0_embeddings/glove.6B/glove.6B.300d.txt', kernel_size=3, lstm_out=64, max_len=32, model_name='modelKeras', model_type='BiLSTM2_CNN3_model', num_epochs=5, num_filters=250, oov_tok='<OOV>', pad_type='post', preproc='remove_stopwords_and_punctuation_textblob', strides=1, test_file='../../Dataset-OLID/OLIDv1.0/test_data_subtask_a.csv', train_portion=0.8, trunc_type='post', verbose=1, vocab_size=7500)

Scores on val:
2592/2648 [============================>.] - ETA: 0s - loss: 0.4791 - acc: 0.7708 - rec: 0.7267 - prec: 0.6347 - f1: 0.6691
2648/2648 [==============================] - 4s 1ms/sample - loss: 0.4763 - acc: 0.7723 - rec: 0.7293 - prec: 0.6357 - f1: 0.6710
[0.47625026890158295, 0.772281, 0.72925436, 0.6357136, 0.6709505]

Scores on test:
800/860 [==========================>...] - ETA: 0s - loss: 0.4704 - acc: 0.7912 - rec: 0.6489 - prec: 0.6086 - f1: 0.6173
860/860 [==============================] - 1s 1ms/sample - loss: 0.4660 - acc: 0.7977 - rec: 0.6597 - prec: 0.6187 - f1: 0.6285
[0.46596271257067834, 0.7976744, 0.6597085, 0.61874306, 0.6285067]

```

- BiLSTM3 + CNN3, max_len = 64
```
10528/10592 [============================>.] - ETA: 0s - loss: 0.3128 - acc: 0.8692 - rec: 0.8011 - prec: 0.8101 - f1: 0.7940
10560/10592 [============================>.] - ETA: 0s - loss: 0.3128 - acc: 0.8692 - rec: 0.8008 - prec: 0.8103 - f1: 0.7939
Epoch 00005: val_f1 did not improve from 0.66342

10592/10592 [==============================] - 132s 12ms/sample - loss: 0.3130 - acc: 0.8693 - rec: 0.8007 - prec: 0.8105 - f1: 0.7940 - val_loss: 0.5291 - val_acc: 0.7817 - val_rec: 0.6332 - val_prec: 0.6836 - val_f1: 0.6452

2624/2648 [============================>.] - ETA: 0s - loss: 0.5322 - acc: 0.7801 - rec: 0.6217 - prec: 0.6825 - f1: 0.6404
2648/2648 [==============================] - 5s 2ms/sample - loss: 0.5291 - acc: 0.7817 - rec: 0.6262 - prec: 0.6846 - f1: 0.6438

SCORES:
[0.5290813417233009, 0.78172207, 0.6262245, 0.68457043, 0.64380836]

Arguments:
----------
Namespace(LR=0.001, data_file='../../Dataset-OLID/OLIDv1.0/data_subtask_a.csv', dropout=0.5, emb_dim=300, emb_file='../../../0_embeddings/glove.6B/glove.6B.300d.txt', kernel_size=3, lstm_out=64, max_len=64, model_name='modelKeras', model_type='BiLSTM2_CNN3_model', num_epochs=5, num_filters=250, oov_tok='<OOV>', pad_type='post', preproc='remove_stopwords_and_punctuation_textblob', strides=1, test_file='../../Dataset-OLID/OLIDv1.0/test_data_subtask_a.csv', train_portion=0.8, trunc_type='post', verbose=1, vocab_size=7500)

Scores on val:
2624/2648 [============================>.] - ETA: 0s - loss: 0.4818 - acc: 0.7839 - rec: 0.6709 - prec: 0.6756 - f1: 0.6640
2648/2648 [==============================] - 7s 2ms/sample - loss: 0.4795 - acc: 0.7855 - rec: 0.6748 - prec: 0.6777 - f1: 0.6671
[0.47946390928278515, 0.7854985, 0.6748334, 0.6777437, 0.66709137]

Scores on test:
832/860 [============================>.] - ETA: 0s - loss: 0.4319 - acc: 0.8149 - rec: 0.6113 - prec: 0.6744 - f1: 0.6289
860/860 [==============================] - 2s 2ms/sample - loss: 0.4268 - acc: 0.8174 - rec: 0.6211 - prec: 0.6782 - f1: 0.6361
[0.42684167484904445, 0.8174419, 0.6210593, 0.67818147, 0.6361277]
```

- BiLSTM3 + CNN3 short, max_len = 64
```
10528/10592 [============================>.] - ETA: 0s - loss: 0.3371 - acc: 0.8560 - rec: 0.7578 - prec: 0.7963 - f1: 0.7669
10560/10592 [============================>.] - ETA: 0s - loss: 0.3370 - acc: 0.8559 - rec: 0.7575 - prec: 0.7963 - f1: 0.7668
Epoch 00005: val_f1 did not improve from 0.67232

10592/10592 [==============================] - 115s 11ms/sample - loss: 0.3378 - acc: 0.8557 - rec: 0.7572 - prec: 0.7962 - f1: 0.7666 - val_loss: 0.5061 - val_acc: 0.7851 - val_rec: 0.6359 - val_prec: 0.6845 - val_f1: 0.6502

2624/2648 [============================>.] - ETA: 0s - loss: 0.5084 - acc: 0.7847 - rec: 0.6307 - prec: 0.6881 - f1: 0.6486
2648/2648 [==============================] - 5s 2ms/sample - loss: 0.5061 - acc: 0.7851 - rec: 0.6312 - prec: 0.6879 - f1: 0.6489

SCORES:
[0.5060553217582472, 0.78512084, 0.6311755, 0.68788075, 0.6488502]

Arguments:
----------
Namespace(LR=0.001, data_file='../../Dataset-OLID/OLIDv1.0/data_subtask_a.csv', dropout=0.5, emb_dim=300, emb_file='../../../0_embeddings/glove.6B/glove.6B.300d.txt', kernel_size=3, lstm_out=64, max_len=64, model_name='modelKeras', model_type='BiLSTM2_CNN3_short_model', num_epochs=5, num_filters=250, oov_tok='<OOV>', pad_type='post', preproc='remove_stopwords_and_punctuation_textblob', strides=1, test_file='../../Dataset-OLID/OLIDv1.0/test_data_subtask_a.csv', train_portion=0.8, trunc_type='post', verbose=1, vocab_size=7500)

Scores on val:
2624/2648 [============================>.] - ETA: 0s - loss: 0.4624 - acc: 0.7854 - rec: 0.6868 - prec: 0.6731 - f1: 0.6689
2648/2648 [==============================] - 6s 2ms/sample - loss: 0.4611 - acc: 0.7859 - rec: 0.6906 - prec: 0.6723 - f1: 0.6699
[0.4610898313745631, 0.78587615, 0.69059163, 0.67226005, 0.66991043]

Scores on test:
832/860 [============================>.] - ETA: 0s - loss: 0.4086 - acc: 0.8329 - rec: 0.5493 - prec: 0.7599 - f1: 0.6235
860/860 [==============================] - 2s 2ms/sample - loss: 0.4038 - acc: 0.8360 - rec: 0.5614 - prec: 0.7642 - f1: 0.6328
[0.40383757255798164, 0.8360465, 0.5613987, 0.7641641, 0.6327991]

```


- BiLSTM, maxlen = 64
```
10528/10592 [============================>.] - ETA: 0s - loss: 0.2972 - acc: 0.8735 - rec: 0.7866 - prec: 0.8277 - f1: 0.7979
10560/10592 [============================>.] - ETA: 0s - loss: 0.2972 - acc: 0.8735 - rec: 0.7866 - prec: 0.8276 - f1: 0.7979
Epoch 00005: val_f1 did not improve from 0.64005

10592/10592 [==============================] - 40s 4ms/sample - loss: 0.2977 - acc: 0.8731 - rec: 0.7855 - prec: 0.8276 - f1: 0.7972 - val_loss: 0.5673 - val_acc: 0.7870 - val_rec: 0.6029 - val_prec: 0.7150 - val_f1: 0.6387

2560/2648 [============================>.] - ETA: 0s - loss: 0.5690 - acc: 0.7867 - rec: 0.5988 - prec: 0.7059 - f1: 0.6388
2648/2648 [==============================] - 1s 505us/sample - loss: 0.5673 - acc: 0.7870 - rec: 0.6009 - prec: 0.7076 - f1: 0.6408

SCORES:
[0.5673418174697553, 0.78700906, 0.6009426, 0.7076302, 0.6407899]

Arguments:
----------
Namespace(LR=0.001, data_file='../../Dataset-OLID/OLIDv1.0/data_subtask_a.csv', dropout=0.5, emb_dim=300, emb_file='../../../0_embeddings/glove.6B/glove.6B.300d.txt', kernel_size=3, lstm_out=64, max_len=64, model_name='modelKeras', model_type='BiLSTM_model', num_epochs=5, num_filters=250, oov_tok='<OOV>', pad_type='post', preproc='remove_stopwords_and_punctuation_textblob', strides=1, test_file='../../Dataset-OLID/OLIDv1.0/test_data_subtask_a.csv', train_portion=0.8, trunc_type='post', verbose=1, vocab_size=7500)

Scores on val:
2592/2648 [============================>.] - ETA: 0s - loss: 0.5243 - acc: 0.7824 - rec: 0.6129 - prec: 0.6931 - f1: 0.6411
2648/2648 [==============================] - 2s 923us/sample - loss: 0.5210 - acc: 0.7836 - rec: 0.6149 - prec: 0.6940 - f1: 0.6427
[0.520951804797815, 0.7836103, 0.61486834, 0.69399035, 0.64274526]

Scores on test:
800/860 [==========================>...] - ETA: 0s - loss: 0.4997 - acc: 0.7600 - rec: 0.6504 - prec: 0.5585 - f1: 0.5911
860/860 [==============================] - 1s 947us/sample - loss: 0.4910 - acc: 0.7651 - rec: 0.6657 - prec: 0.5625 - f1: 0.6002
[0.4909574866294861, 0.7651163, 0.6657242, 0.56254524, 0.6002494]
```

- BiLSTM short, maxlen = 64
```
10528/10592 [============================>.] - ETA: 0s - loss: 0.2932 - acc: 0.8760 - rec: 0.7803 - prec: 0.8374 - f1: 0.7984
10560/10592 [============================>.] - ETA: 0s - loss: 0.2936 - acc: 0.8759 - rec: 0.7799 - prec: 0.8373 - f1: 0.7981
Epoch 00005: val_f1 did not improve from 0.63830

10592/10592 [==============================] - 47s 4ms/sample - loss: 0.2941 - acc: 0.8757 - rec: 0.7794 - prec: 0.8370 - f1: 0.7977 - val_loss: 0.5686 - val_acc: 0.7825 - val_rec: 0.5897 - val_prec: 0.7029 - val_f1: 0.6294

2592/2648 [============================>.] - ETA: 0s - loss: 0.5737 - acc: 0.7805 - rec: 0.5829 - prec: 0.6964 - f1: 0.6230
2648/2648 [==============================] - 2s 570us/sample - loss: 0.5686 - acc: 0.7825 - rec: 0.5869 - prec: 0.6987 - f1: 0.6265

SCORES:
[0.568619009051078, 0.7824773, 0.58690935, 0.6986639, 0.6265183]

Arguments:
----------
Namespace(LR=0.001, data_file='../../Dataset-OLID/OLIDv1.0/data_subtask_a.csv', dropout=0.5, emb_dim=300, emb_file='../../../0_embeddings/glove.6B/glove.6B.300d.txt', kernel_size=3, lstm_out=64, max_len=64, model_name='modelKeras', model_type='BiLSTM_short_model', num_epochs=5, num_filters=250, oov_tok='<OOV>', pad_type='post', preproc='remove_stopwords_and_punctuation_textblob', strides=1, test_file='../../Dataset-OLID/OLIDv1.0/test_data_subtask_a.csv', train_portion=0.8, trunc_type='post', verbose=1, vocab_size=7500)

Scores on val:
2592/2648 [============================>.] - ETA: 0s - loss: 0.5333 - acc: 0.7847 - rec: 0.5818 - prec: 0.7117 - f1: 0.6273
2648/2648 [==============================] - 2s 723us/sample - loss: 0.5287 - acc: 0.7866 - rec: 0.5858 - prec: 0.7136 - f1: 0.6307
[0.5287389767404049, 0.7866314, 0.58584815, 0.7136365, 0.63074505]

Scores on test:
768/860 [=========================>....] - ETA: 0s - loss: 0.4577 - acc: 0.8086 - rec: 0.5700 - prec: 0.6743 - f1: 0.6055
860/860 [==============================] - 1s 671us/sample - loss: 0.4578 - acc: 0.8105 - rec: 0.5841 - prec: 0.6740 - f1: 0.6140
[0.45783954775610636, 0.8104651, 0.5840562, 0.6739631, 0.61404926]

```


## Latest: 

- BiLSTM2_CNN3_short_model
```
10560/10592 [============================>.] - ETA: 0s - loss: 0.1405 - acc: 0.9455 - rec: 0.9151 - prec: 0.9223 - f1: 0.9147
Epoch 00018: val_f1 did not improve from 0.66817

10592/10592 [==============================] - 62s 6ms/sample - loss: 0.1407 - acc: 0.9454 - rec: 0.9151 - prec: 0.9223 - f1: 0.9147 - val_loss: 1.0885 - val_acc: 0.7564 - val_rec: 0.5873 - val_prec: 0.6481 - val_f1: 0.6061
Epoch 00018: early stopping
2648/2648 [==============================] - 2s 802us/sample - loss: 1.0885 - acc: 0.7564 - rec: 0.5864 - prec: 0.6415 - f1: 0.6032

SCORES:
[1.0884670001142334, 0.75641996, 0.5863989, 0.64148796, 0.60323817]

Arguments:
----------
Namespace(LR=0.001, data_file='../../Dataset-OLID/OLIDv1.0/data_subtask_a.csv', dropout=0.5, emb_dim=300, emb_file='../../../0_embeddings/glove.6B/glove.6B.300d.txt', kernel_size=3, lstm_out=32, max_len=64, model_name='modelKeras', model_type='BiLSTM2_CNN3_short_model', num_epochs=50, num_filters=16, oov_tok='<OOV>', pad_type='post', pool_size=2, preproc='remove_stopwords_and_punctuation_textblob', strides=1, test_file='../../Dataset-OLID/OLIDv1.0/test_data_subtask_a.csv', train_portion=0.8, trunc_type='post', verbose=1, vocab_size=7500)

Scores on val:
2648/2648 [==============================] - 4s 2ms/sample - loss: 0.4738 - acc: 0.7919 - rec: 0.6430 - prec: 0.7097 - f1: 0.6637
[0.47384217962217473, 0.79191846, 0.6429647, 0.7097382, 0.66365886]

Scores on test:
860/860 [==============================] - 1s 1ms/sample - loss: 0.4251 - acc: 0.8349 - rec: 0.5495 - prec: 0.7594 - f1: 0.6253
[0.42508711149526196, 0.83488375, 0.5495007, 0.75937015, 0.6252544]

```