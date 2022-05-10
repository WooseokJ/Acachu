from __future__ import absolute_import, unicode_literals
from celery import shared_task
from celery import Task
from config.celery import app
import numpy as np
import pandas as pd
import os
import json
import logging
import tensorflow as tf
from tensorflow import keras
from tensorflow.keras.preprocessing.text import Tokenizer
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing.sequence import pad_sequences
from transformers import BertTokenizer
from konlpy.tag import Okt
from hanspell import spell_checker

from main.models import Store, Tag, StoreTag
class PredictTask(Task):
    def __init__(self):
        self.tags_model = None
        self.sentiment_model = None
        self.train = None
        self.tokenizer = None
        self.okt = None
    def __call__(self, *args, **kwargs):
        if not self.tags_model and not self.sentiment_model and not self.train:
            logging.info('Loading Model...')
            os.environ["CUDA_VISIBLE_DEVICES"] = "-1"
            save_path = os.getcwd() + '\\nlp\\bert_clf_v2'
            tags_model = tf.saved_model.load(save_path)
            train = np.load(os.getcwd()+'\\nlp\\x_train_okt_V3.npy',\
                            allow_pickle=True)
            sentiment_model = load_model(os.getcwd()+'\\nlp\\bilstm_okt_v3.h5')
            self.tags_model = tags_model
            self.sentiment_model = sentiment_model
            self.train = train
            self.tokenizer = BertTokenizer.from_pretrained('bert-base-multilingual-cased')
            self.okt = Okt()
            logging.info('Model Loaded')
        return self.run(*args, **kwargs)

    def preprocessing(self, review_list):
        review_list = pd.Series(review_list)
        review_list = review_list.str.replace(pat=r'[^\w]', repl=r' ', regex=True)
        review_list = review_list.str.replace(pat=r'([ㄱ-ㅎ ㅏ-ㅣ])+', \
                                              repl=r' ',\
                                              regex=True)
        review_list = review_list.str.replace(pat=r'([a-z])+', repl=r' ', regex=True)
        review_list = review_list.str.replace(pat=r'^ +', repl=r"", regex=True) # white space 데이터를 empty value로 변경
        review_list.replace('', np.nan, inplace=True)
        review_list.dropna(inplace=True)

        review_list = review_list.tolist()
        return review_list

    # 리뷰 하나마다의 문장 분리
    # 중립적인 문장 분리 함수
    def sent_split(self, sent):
        ec = ['는데', '한데', '지만', '합니다만', '만', '네요', '요', '다']
        
        # Okt 형태소 분석기
        s = self.okt.pos(sent)

        lst = []

        for i in range(len(s)):
            if 'Adjective' in s[i][1]:
                lst.append(s[i][0])
                for j in ec:
                    if j in s[i][0]:
                        lst.append(';')
            else:
                lst.append(s[i][0])

        splited = ''.join(lst).split(';')

        for i in splited:
            if i == '' or i == ' ':
                del splited[splited.index(i)]
        for i in range(len(splited)):
            spelled_sent = spell_checker.check(splited[i])
            splited[i] = spelled_sent.checked

        return splited

    # 리뷰를 sent_split 함수에 적용하는 함수
    def review_to_sentsplit(self, review_list):
        review_list_split = []
        for idx in range(len(review_list)):
            tmp = self.sent_split(review_list[idx])
            review_list_split.append(tmp)
        review_list_split = sum(review_list_split, [])
        return review_list_split

    # 리뷰를 Bert Tensor로 변환
    def tokenize_sentences(self, sentences, tokenizer, max_seq_len=128):
        tokenized_sentences = []

        for sentence in sentences:
            tokenized_sentence = tokenizer.encode(
                                 sentence,
                                 add_special_tokens=True,
                                 max_length=max_seq_len,
                                 )
            
            tokenized_sentences.append(tokenized_sentence)

        return tokenized_sentences
    
    def create_attention_masks(self, tokenized_and_padded_sentences):
        attention_masks = []

        for sentence in tokenized_and_padded_sentences:
            att_mask = [int(token_id > 0) for token_id in sentence]
            attention_masks.append(att_mask)

        return np.asarray(attention_masks)
    
    def create_dataset(self, data_tuple, epochs=1, batch_size=32, buffer_size=10000, train=True):
        dataset = tf.data.Dataset.from_tensor_slices(data_tuple)
        if train:
            dataset = dataset.shuffle(buffer_size=buffer_size)
        dataset = dataset.repeat(epochs)
        dataset = dataset.batch(batch_size)
        if train:
            dataset = dataset.prefetch(1)
        
        return dataset
    
    def predict(self, review, MAX_LEN=128):
        label_cols = ['dessert', 'beverage', 'coffee',\
                      'atmosphere', 'child', 'dog', 'study'
                     ]
        tokenizer = self.tokenizer

        rv_input_ids = self.tokenize_sentences(review, tokenizer, MAX_LEN)
        rv_input_ids = pad_sequences(rv_input_ids, maxlen=MAX_LEN, \
                                     dtype="long", value=0, \
                                     truncating="post", padding="post")
        rv_attention_masks = self.create_attention_masks(rv_input_ids)

        rv_input_ids = tf.convert_to_tensor(rv_input_ids, dtype=tf.int64)
        rv_attention_masks = tf.convert_to_tensor(rv_attention_masks,\
                                                  dtype=tf.int64)

        rv_dataset = self.create_dataset\
                    ((rv_input_ids, rv_attention_masks),\
                     batch_size=1,
                     train=False,
                     epochs=1)

        rv_steps = len(review)
        preds = pd.DataFrame(columns=label_cols)

        for i, (token_ids, masks) in enumerate(rv_dataset, rv_steps):
            predictions = self.tags_model(token_ids, attention_mask=masks)
            predictions = np.where(predictions >= 0.5, 1, 0) # sigmoid 값 2진

            data = sum(predictions.copy().tolist(), [])
            preds = preds.append(pd.Series\
                                (data, index=preds.columns),\
                                 ignore_index=True)

        return preds
    
    def sentiment_predict(self, line):

        # Okt 형태소 분석기
        # okt = Okt()
        line = self.okt.morphs(line)  # 토큰화        
        tokenizer = Tokenizer(27452, oov_token='OOV')  # 이전 모델 학습 시 적용된 값들 불러오기
        tokenizer.fit_on_texts(self.train)
        encoded = tokenizer.texts_to_sequences([line]) # 정수 인코딩
        pad_new = pad_sequences(encoded, maxlen=100) # 패딩, maxlen 디폴트 100
        predict_result = float(self.sentiment_model.predict(pad_new))

        return predict_result
    def pos_neg_ratio(self, data):
        label_index = ['dessert', 'beverage', 'coffee', \
                       'atmosphere', 'child', 'dog', 'study'
                      ]
        label_cols = ['Positive', 'Negative', \
                      'Tot_tag_count', 'Ratio'
                     ]
        pos_neg_sum = pd.DataFrame(index=label_index, columns=label_cols)
        pos_neg_sum = pos_neg_sum.fillna(0)

        for idx in data.index:
            for col in list(data):
                if (col == 'review') or (col == 'pos_neg'):
                    continue
                if (data.loc[idx][col] == 1):
                    if(data.loc[idx]['pos_neg'] == 1):
                        pos_neg_sum.loc[col]['Positive'] += 1
                    else:
                        pos_neg_sum.loc[col]['Negative'] += 1

        pos_neg_sum['Tot_tag_count'] = pos_neg_sum['Positive'] \
                                     + pos_neg_sum['Negative']
        pos_neg_sum['Ratio'] = pos_neg_sum['Positive']\
                              /pos_neg_sum['Tot_tag_count']

        pos_neg_sum = pos_neg_sum.fillna(0)

        return pos_neg_sum
# 태그 추출 함수
@shared_task(bind=True, base=PredictTask)
def tags(self, review_list, store_id):
    review_list = json.loads(review_list)
    print('... review received ...')
    review_list = self.preprocessing(review_list)
    print('... preprocessed completed ...')
    review_list_split = self.review_to_sentsplit(review_list)
    print('... review spliting completed ...')
    data = self.predict(review_list_split)
    print('... category predicted completed ...')
    data['review'] = review_list_split
    data = data[['review', 'dessert', 'beverage', 'coffee',
                 'atmosphere', 'child', 'dog', 'study']]
    data['pos_neg'] = np.nan
    for idx in range(len(data['review'])):
        tmp = self.sentiment_predict(data['review'][idx])
        if tmp > 0.5:
            data['pos_neg'][idx] = 1
        else:
            data['pos_neg'][idx] = 0
    print('...sentiment analysis completed...')
    print('... makes dataframe completed ...')
    pos_neg_sum = self.pos_neg_ratio(data)
    print('... extract pos_neg_ratio complted ...')
    print('... extracting final category ...')
    caffe_tags = []

    for idx in pos_neg_sum.index:
        if (pos_neg_sum['Ratio'][idx] >= 0.7) \
            and (pos_neg_sum['Tot_tag_count'][idx] >= 10):
            caffe_tags.append(idx)
    tag_names = {'dessert': '디저트',
                 'beverage': '음료',
                 'coffee': '커피',
                 'atmosphere': '분위기',
                 'child': '유아동반',
                 'dog': '애견동반',
                 'study': '카공'}
    for i in range(len(caffe_tags)):
        caffe_tags[i] = tag_names[caffe_tags[i]]
    store = Store.objects.get(store_id=store_id)
    StoreTag.objects.filter(store__store_id=store_id).delete()
    for caffe_tag in caffe_tags:
        t = Tag.objects.get(tag_name=caffe_tag)
        StoreTag.objects.create(store=store, tag=t)

    return caffe_tags
