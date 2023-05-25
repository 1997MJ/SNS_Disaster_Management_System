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

def nlp(data,model):

  ban_words = []
  with open("Scrapy/TextFilter/ban.txt", encoding="UTF8") as f:
        ban_words = [line.rstrip("\n") for line in f]

  start = time.time()

  if len(data) <= 20:
      print("[Error] Too little data to learn", '데이터 수: ' , len(data))
      return data
  
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

 # data_content 목록의 각 요소에서 텍스트를 정리하고 
 # 정리된 텍스트를 문장으로 분할하고 결과 문장을 data_content의 동일한 인덱스에 저장
 # 또한 모든 분할 문장을 data_content_all 목록에 연결
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
  model2.wv.save_word2vec_format('word2vec_model_result') # 저장

  content_vector = []
  index = -1

  word_vectors = model2.wv
  content_vector = word_vectors.get_normed_vectors()

  # KMeans 클러스터링을 사용
  if len(content_vector) > 200:
    n_clusters = 10
  elif len(content_vector) > 50:
      n_clusters = 10
  elif len(content_vector) > 21:
      n_clusters = 10
  else:
      n_clusters = 0

  if n_clusters > 0:
      kmeans = KMeans(n_clusters=n_clusters, init='k-means++',n_init=10).fit(content_vector)
  else:
      kmeans = None
  
  
  target_label_ = [] 
 
  for i in range(data_pre):
    target_label_.append(kmeans.labels_[i])

  data_content_all_meaningful = []

#  설정한 범주안에 있는 값을 저장
  for index in range(len(data_content_all)):
    if target_label_[0] == kmeans.labels_[index] or target_label_[1] == kmeans.labels_[index] or target_label_[2] == kmeans.labels_[index] or target_label_[3] == kmeans.labels_[index] or target_label_[4] == kmeans.labels_[index] or target_label_[5] == kmeans.labels_[index] or target_label_[6] == kmeans.labels_[index] or target_label_[7] == kmeans.labels_[index] or target_label_[8] == kmeans.labels_[index]:
      if len(data_content_all[index]) >= 10:
        data_content_all_meaningful.append(data_content_all[index])
        print('Append meaningful data')


  # ban 단어 포함 시 content 제거
  for sentence in data_content_all_meaningful[:]:
    for ban_word in ban_words:
      if ban_word in sentence and sentence in data_content_all_meaningful:
        data_content_all_meaningful.remove(sentence)
        print('Delete ban words')


  print('data_content_all_meaningful:', len(data_content_all_meaningful) - 7)

  # data_content_all_meaningful 문장 목록의 일부인지 여부에 따라 data_content의 문장을 필터링 정리
  for content in data_content:
    for sentence in content[:]:
      if sentence not in data_content_all_meaningful:
        content.remove(sentence)
      
      
  data_result = []
  count = 0

  for index in range(len(data_content)):
    if len(data_content[index]) != 0:
        data_sentence = ''.join(sentence for sentence in data_content[index])
        data_result.append(data_sentence)

  print('data result:', len(data_result))
  print("----------------------------------------------------------------------------------------")
  print("모델 학습 시간 :", time.time() - start)  # 현재시각 - 시작시간 = 실행 시간
 
  return data_result

