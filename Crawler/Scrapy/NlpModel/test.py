import MySQLdb
import pandas as pd
from gensim.models import KeyedVectors
from konlpy.tag import Kkma

import  utility.DB_Utility as db
import kss
from sklearn.cluster import KMeans
from utility.util import clean_text
import time
import numpy as np
from gensim.models import Word2Vec
import seaborn as sns
import gensim
from gensim.models import KeyedVectors
from gensim.test.utils import datapath
import matplotlib.pyplot as plt

model=  KeyedVectors.load_word2vec_format("word2vec_model_result") # 불러옴
conn=MySQLdb.connect(
            user="root",
            passwd="1234",
            host="localhost",
            db="crawlerdb"
        )
cursor = conn.cursor()
query = "SELECT service,content,sns,keyword,date,link FROM post"

cursor.execute(query)
dataset= pd.DataFrame(cursor.fetchall(),columns=['service','content','sns','keyword','date','link'])  ##리스트로 변   dataset_twitter = []
dataset_twitter = []
dataset_instargram = []

for col,record in dataset.iterrows():
    if record['service'] == 'twitter':
        dataset_twitter.append(record)
    elif record['service'] == 'instargram':
        dataset_instargram.append(record)
dataset = dataset_twitter + dataset_instargram

data=dataset
ban_words = []
with open("Scrapy/TextFilter/ban.txt", encoding="UTF8") as f:
      ban_words = [line.rstrip("\n") for line in f]

data_content = []

# 금지된 단어를 포함하지 않는 필터링된 레코드의 '콘텐츠' 값 생성
for record in data:
  if all(ban_word not in record['content'] for ban_word in ban_words):
      if record['content'] not in data_content:
          data_content.append(record['content'])
data_content_all = ['코로나 신규 확진자가 발생했다.', 
                    '화재가 발생했다.', 
                    '홍수 피해가 발생했다.', 
                    '사고 났다.', 
                    '눈이 많이 내린다.', 
                    '산에 불이 났다.', 
                    '붕괴 사고가 발생하다.', 
                    '폭발하다.', 
                    '태풍이 발생했다.']

data_pre = len(data_content_all)


for index, content in enumerate(data_content):
  if content:
      cleaned_text = clean_text(content)
      sentences = kss.split_sentences(cleaned_text)
      data_content[index] = sentences
      data_content_all.extend(sentences)
  print("{}/{}".format(index, len(data)))
tokenList = [sent.split() for sent in data_content_all]
model2 = Word2Vec(vector_size=200, window=3, min_count=1, workers=4, sg=0)
model2.build_vocab(tokenList)
model2.build_vocab([list(model.key_to_index.keys())],update=True)

model2.wv.vectors_lockf=np.ones(len(model2.wv),dtype=np.float32)
model2.wv.intersect_word2vec_format("word2vec_model_result") # 학습된 코퍼스 추가

##model2.train(tokenList,total_examples=model2.corpus_count,epochs=15)
model2.wv.save_word2vec_format('word2vec_model_result') # 저장
content_vector = []
index = -1
word_vectors = model2.wv
content_vector = word_vectors.get_normed_vectors()

print(content_vector)