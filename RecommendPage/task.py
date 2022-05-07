from __future__ import absolute_import, unicode_literals
from celery import shared_task
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


# # # 카페 태그 모델 (BERT) Load :
# # save_path = os.getcwd() + '\\nlp\\bert_clf_v2'
# # tags_model = tf.saved_model.load(save_path)

# # # 긍부정 분류 모델 (BiLSTM) Load :
# # train = np.load(os.getcwd()+'\\nlp\\x_train_okt_V3.npy', allow_pickle=True)
# # sentiment_model = load_model(os.getcwd()+'\\nlp\\bilstm_okt_v3.h5')

# # 정규 표현식 적용 및 제거된 리뷰 삭제

# def preprocessing(review_list):
#     review_list = pd.Series(review_list)

#     review_list = review_list.str.replace(pat=r'[^\w]',repl=r' ',regex=True)
#     review_list = review_list.str.replace(pat=r'([ㄱ-ㅎ ㅏ-ㅣ])+',repl=r' ',regex=True)
#     review_list = review_list.str.replace(pat=r'([a-z])+',repl=r' ',regex=True)

#     review_list = review_list.str.replace(pat=r'^ +', repl=r"", regex=True) # white space 데이터를 empty value로 변경
#     review_list.replace('', np.nan, inplace=True)
#     review_list.dropna(inplace=True)

#     review_list = review_list.tolist()
#     return review_list

# # 리뷰 하나마다의 문장 분리
# # 중립적인 문장 분리 함수

# def sent_split(sent):
#     ec = ['는데', '한데', '지만', '합니다만', '만', '네요', '요', '다']
    
#     # Okt 형태소 분석기
#     okt = Okt()
    
#     s = okt.pos(sent)

#     lst = []

#     for i in range(len(s)):
#         if 'Adjective' in s[i][1]:
#             lst.append(s[i][0])
#             for j in ec:
#                 if j in s[i][0]:
#                     lst.append(';')
#         else:
#             lst.append(s[i][0])

#     splited = ''.join(lst).split(';')

#     for i in splited:
#         if i == '' or i == ' ':
#             del splited[splited.index(i)]
#     for i in range(len(splited)):
#         spelled_sent = spell_checker.check(splited[i])
#         splited[i] = spelled_sent.checked

#     return splited

# # 리뷰를 sent_split 함수에 적용하는 함수

# def review_to_sentsplit(review_list):
#     review_list_split = []
#     for idx in range(len(review_list)):
#         tmp = sent_split(review_list[idx])
#         review_list_split.append(tmp)
#     review_list_split = sum(review_list_split, [])
#     return review_list_split

# # 리뷰를 Bert Tensor로 변환

# def tokenize_sentences(sentences, tokenizer, max_seq_len = 128):
#     tokenized_sentences = []

#     for sentence in sentences:
#         tokenized_sentence = tokenizer.encode(
#                             sentence,                  # Sentence to encode.
#                             add_special_tokens = True, # Add '[CLS]' and '[SEP]'
#                             max_length = max_seq_len,  # Truncate all sentences.
#                     )
        
#         tokenized_sentences.append(tokenized_sentence)

#     return tokenized_sentences


# def create_attention_masks(tokenized_and_padded_sentences):
#     attention_masks = []

#     for sentence in tokenized_and_padded_sentences:
#         att_mask = [int(token_id > 0) for token_id in sentence]
#         attention_masks.append(att_mask)

#     return np.asarray(attention_masks)


# def create_dataset(data_tuple, epochs=1, batch_size=32, buffer_size=10000, train=True):
#     dataset = tf.data.Dataset.from_tensor_slices(data_tuple)
#     if train:
#         dataset = dataset.shuffle(buffer_size=buffer_size)
#     dataset = dataset.repeat(epochs)
#     dataset = dataset.batch(batch_size)
#     if train:
#         dataset = dataset.prefetch(1)
    
#     return dataset


# def predict(review, MAX_LEN=128):
#     # 카페 태그 모델 (BERT) Load :
#     save_path = os.getcwd() + '\\nlp\\bert_clf_v2'
#     tags_model = tf.saved_model.load(save_path)
#     label_cols = ['dessert', 'beverage', 'coffee', 'atmosphere', 'child', 'dog', 'study']
#     tokenizer = BertTokenizer.from_pretrained('bert-base-multilingual-cased')

#     rv_input_ids = tokenize_sentences(review, tokenizer, MAX_LEN)
#     rv_input_ids = pad_sequences(rv_input_ids, maxlen=MAX_LEN, dtype="long", value=0, truncating="post", padding="post")
#     rv_attention_masks = create_attention_masks(rv_input_ids)

#     rv_input_ids = tf.convert_to_tensor(rv_input_ids, dtype=tf.int64)
#     rv_attention_masks = tf.convert_to_tensor(rv_attention_masks, dtype=tf.int64)

#     rv_dataset = create_dataset((rv_input_ids, rv_attention_masks), batch_size=1, train=False, epochs=1)

#     rv_steps = len(review)
#     preds = pd.DataFrame(columns=label_cols)
  
#     for i, (token_ids, masks) in enumerate(rv_dataset, rv_steps):
#         predictions = tags_model(token_ids, attention_mask=masks)
#         predictions = np.where(predictions >= 0.5, 1, 0) # sigmoid 값 2진

#         data = sum(predictions.copy().tolist(), [])
#         preds = preds.append(pd.Series(data, index=preds.columns), ignore_index=True)

#     return preds


# def sentiment_predict(line):

#     # Okt 형태소 분석기
#     okt = Okt()
#     line = okt.morphs(line) # 토큰화
#     # 긍부정 분류 모델 (BiLSTM) Load :
#     train = np.load(os.getcwd()+'\\nlp\\x_train_okt_V3.npy', allow_pickle=True)
#     sentiment_model = load_model(os.getcwd()+'\\nlp\\bilstm_okt_v3.h5')
    
#     # line = [word for word in line if not word in stopwords] # 불용어 제거(stopwords는 optional)
#     tokenizer = Tokenizer(27452, oov_token = 'OOV') # 이전 모델 학습 시 적용된 값들 불러오기
#     tokenizer.fit_on_texts(train)
#     encoded = tokenizer.texts_to_sequences([line]) # 정수 인코딩
#     pad_new = pad_sequences(encoded, maxlen = 100) # 패딩, maxlen 디폴트 100
#     predict_result = float(sentiment_model.predict(pad_new))

#     return predict_result


# def pos_neg_ratio(data):
#     label_index = ['dessert', 'beverage', 'coffee', 'atmosphere', 'child', 'dog', 'study']
#     label_cols = ['Positive', 'Negative', 'Tot_tag_count', 'Ratio']
#     pos_neg_sum = pd.DataFrame(index=label_index, columns=label_cols)
#     pos_neg_sum = pos_neg_sum.fillna(0)

#     for idx in data.index:
#         for col in list(data):
#             if (col == 'review') or (col == 'pos_neg'):
#                 continue
#             if (data.loc[idx][col] == 1):
#                 if(data.loc[idx]['pos_neg'] == 1):
#                     pos_neg_sum.loc[col]['Positive'] += 1
#                 else:
#                     pos_neg_sum.loc[col]['Negative'] += 1

#     pos_neg_sum['Tot_tag_count'] = pos_neg_sum['Positive'] + pos_neg_sum['Negative']
#     pos_neg_sum['Ratio'] = pos_neg_sum['Positive'] / pos_neg_sum['Tot_tag_count']

#     pos_neg_sum = pos_neg_sum.fillna(0)

#     return pos_neg_sum

# # 태그 추출 함수
# @shared_task
# def tags(review_list):
#     review_list = json.loads(review_list)
#     review_list = preprocessing(review_list)
#     review_list_split = review_to_sentsplit(review_list)
#     data = predict(review_list_split)
#     data['review'] = review_list_split
#     data = data[['review', 'dessert', 'beverage', 'coffee', 'atmosphere', 'child', 'dog', 'study']]
#     data['pos_neg'] = np.nan

#     for idx in range(len(data['review'])):
#         tmp = sentiment_predict(data['review'][idx])
#         if tmp > 0.5:
#             data['pos_neg'][idx] = 1
#         else:
#             data['pos_neg'][idx] = 0

#     pos_neg_sum = pos_neg_ratio(data)



#     caffe_tags = []
#     for idx in pos_neg_sum.index:
#         if (pos_neg_sum['Ratio'][idx] >= 0.7) and (pos_neg_sum['Tot_tag_count'][idx] >= 10):
#             caffe_tags.append(idx)
#     return caffe_tags

class PredictTask:
    def __init__(self, review):
        super().__init__()
        self.tags_model = None
        self.sentiment_model = None
        self.train = None
        self.review_list = review
        
    def __call__(self):
        if not self.tags_model and not self.sentiment_model and not self.train:
            logging.info('Loading Model...')
            save_path = os.getcwd() + '\\nlp\\bert_clf_v2'
            tags_model = tf.saved_model.load(save_path)
            train = np.load(os.getcwd()+'\\nlp\\x_train_okt_V3.npy', allow_pickle=True)
            sentiment_model = load_model(os.getcwd()+'\\nlp\\bilstm_okt_v3.h5')
            self.tags_model = tags_model
            self.sentiment_model = sentiment_model
            self.train = train
            logging.info('Model Loaded')
        # return self.run(*args, **kwargs)

    def preprocessing(review_list):
        review_list = pd.Series(review_list)

        review_list = review_list.str.replace(pat=r'[^\w]',repl=r' ',regex=True)
        review_list = review_list.str.replace(pat=r'([ㄱ-ㅎ ㅏ-ㅣ])+',repl=r' ',regex=True)
        review_list = review_list.str.replace(pat=r'([a-z])+',repl=r' ',regex=True)

        review_list = review_list.str.replace(pat=r'^ +', repl=r"", regex=True) # white space 데이터를 empty value로 변경
        review_list.replace('', np.nan, inplace=True)
        review_list.dropna(inplace=True)

        review_list = review_list.tolist()
        return review_list

    # 리뷰 하나마다의 문장 분리
    # 중립적인 문장 분리 함수
    def sent_split(sent):
        ec = ['는데', '한데', '지만', '합니다만', '만', '네요', '요', '다']
        
        # Okt 형태소 분석기
        okt = Okt()
        
        s = okt.pos(sent)

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
    def tokenize_sentences(sentences, tokenizer, max_seq_len = 128):
        tokenized_sentences = []

        for sentence in sentences:
            tokenized_sentence = tokenizer.encode(
                                sentence,                  # Sentence to encode.
                                add_special_tokens = True, # Add '[CLS]' and '[SEP]'
                                max_length = max_seq_len,  # Truncate all sentences.
                        )
            
            tokenized_sentences.append(tokenized_sentence)

        return tokenized_sentences

    def create_attention_masks(tokenized_and_padded_sentences):
        attention_masks = []

        for sentence in tokenized_and_padded_sentences:
            att_mask = [int(token_id > 0) for token_id in sentence]
            attention_masks.append(att_mask)

        return np.asarray(attention_masks)

    def create_dataset(data_tuple, epochs=1, batch_size=32, buffer_size=10000, train=True):
        dataset = tf.data.Dataset.from_tensor_slices(data_tuple)
        if train:
            dataset = dataset.shuffle(buffer_size=buffer_size)
        dataset = dataset.repeat(epochs)
        dataset = dataset.batch(batch_size)
        if train:
            dataset = dataset.prefetch(1)
        
        return dataset

    def predict(self, review, MAX_LEN=128):
        label_cols = ['dessert', 'beverage', 'coffee', 'atmosphere', 'child', 'dog', 'study']
        tokenizer = BertTokenizer.from_pretrained('bert-base-multilingual-cased')

        rv_input_ids = self.tokenize_sentences(review, tokenizer, MAX_LEN)
        rv_input_ids = pad_sequences(rv_input_ids, maxlen=MAX_LEN, dtype="long", value=0, truncating="post", padding="post")
        rv_attention_masks = self.create_attention_masks(rv_input_ids)

        rv_input_ids = tf.convert_to_tensor(rv_input_ids, dtype=tf.int64)
        rv_attention_masks = tf.convert_to_tensor(rv_attention_masks, dtype=tf.int64)

        rv_dataset = self.create_dataset((rv_input_ids, rv_attention_masks), batch_size=1, train=False, epochs=1)

        rv_steps = len(review)
        preds = pd.DataFrame(columns=label_cols)

        for i, (token_ids, masks) in enumerate(rv_dataset, rv_steps):
            predictions = self.tags_model(token_ids, attention_mask=masks)
            predictions = np.where(predictions >= 0.5, 1, 0) # sigmoid 값 2진

            data = sum(predictions.copy().tolist(), [])
            preds = preds.append(pd.Series(data, index=preds.columns), ignore_index=True)

        return preds

    def sentiment_predict(self, line):

        # Okt 형태소 분석기
        okt = Okt()
        line = okt.morphs(line) # 토큰화
        
        tokenizer = Tokenizer(27452, oov_token = 'OOV') # 이전 모델 학습 시 적용된 값들 불러오기
        tokenizer.fit_on_texts(self.train)
        encoded = tokenizer.texts_to_sequences([line]) # 정수 인코딩
        pad_new = pad_sequences(encoded, maxlen = 100) # 패딩, maxlen 디폴트 100
        predict_result = float(self.sentiment_model.predict(pad_new))

        return predict_result

    def pos_neg_ratio(data):
        label_index = ['dessert', 'beverage', 'coffee', 'atmosphere', 'child', 'dog', 'study']
        label_cols = ['Positive', 'Negative', 'Tot_tag_count', 'Ratio']
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

        pos_neg_sum['Tot_tag_count'] = pos_neg_sum['Positive'] + pos_neg_sum['Negative']
        pos_neg_sum['Ratio'] = pos_neg_sum['Positive'] / pos_neg_sum['Tot_tag_count']

        pos_neg_sum = pos_neg_sum.fillna(0)

        return pos_neg_sum

# 태그 추출 함수
@shared_task
def tags(review_list):
    prd = PredictTask(review_list)
    review_list = json.loads(review_list)
    review_list = prd.preprocessing(review_list)
    review_list_split = prd.review_to_sentsplit(review_list)
    data = prd.predict(review_list_split)
    data['review'] = review_list_split
    data = data[['review', 'dessert', 'beverage', 'coffee', 'atmosphere', 'child', 'dog', 'study']]
    data['pos_neg'] = np.nan

    for idx in range(len(data['review'])):
        tmp = prd.sentiment_predict(data['review'][idx])
        if tmp > 0.5:
            data['pos_neg'][idx] = 1
        else:
            data['pos_neg'][idx] = 0

    pos_neg_sum = prd.pos_neg_ratio(data)

    caffe_tags = []

    for idx in pos_neg_sum.index:
        if (pos_neg_sum['Ratio'][idx] >= 0.7) and (pos_neg_sum['Tot_tag_count'][idx] >= 10):
            caffe_tags.append(idx)

    return caffe_tags