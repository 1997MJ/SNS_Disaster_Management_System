

from konlpy.tag import Kkma
from konlpy.utils import pprint
from gensim.models.word2vec import Word2Vec

# import warnings
# warnings.filterwarnings("ignore")


# data = [["KB�������ְ� KB����, KBĳ��Ż, KB�ε����Ź �� 3�� �迭�� ��ǥ�� ���� �����ߴ�. ���� ū ������ ��ȴ� KB���� ��ǥ�̻� �ĺ����� ������ KB���� �λ��� �� KB�������� �������� �����ߴ�. �� �ĺ��� ������ȸ ���� ���� ���� ���ӵǸ� �������ھ��� ���� ���� �ְ�濵��(CEO)�� �����Ѵ�. KB������ 19�� �迭�� ��ǥ�̻��ĺ� ��õ����ȸ(���� ������)�� ���� KB���ǡ�KBĳ��Ż��KB�ε����Ź �� 7�� �迭�� ��ǥ �ĺ��� �����ߴٰ� ������. KB���� ���� ��ǥ�̻� �ĺ����� ������ KB���� �λ��� �� KB�������� ������� �輺�� KB���� �λ����� ��õ�ߴ�. KB������ ������ ���� ��ǥü���� �����Ѵ�. KBĳ��Ż���� Ȳ���� KBĳ��Ż ����, KB�ε����Ź���� ��û�� KB�������� ������ ���������׷��ǥ�� ���� ��ǥ�̻� �ĺ��� �����ƴ�. ������ KB���غ��� ��ǥ, ����Ρ������� KB�ڻ��� ��ǥ, ���ذ� KB�ſ����� ��ǥ�� �缱���ƴ�. KB����Ÿ�ý����� �̸� ���� ���� ������ �λ縦 ã�� ���� ��õ�� ��ȹ�̴�. ������ �λ����� KB���� ��ǥ�� �����ϸ� ���ǻ� ���ʷ� ���� CEO�� ź���Ѵ�. �� �ĺ��� KB�������ֿ��� WM(�ڻ����)�� ����ũ, ���� �� ������ �η� ���ƴ�. �׷� WM �ι� �ó��������� �̲��� �������� �����ϰ� �ִٴ� ���� ���� �� �޴´�. �輺�� �λ����� ��ǥ���� ��������(IB) ��������. �����ڻ� �ٺ�ȭ�� ���� ���� ������ �ٲ� �� �ִ� �������� ����ٴ� �򰡸� �޴´�. ���� ��ǥ�� 20��21�� �迭�� ��ǥ�̻��ĺ� ��õ����ȸ�� ���� �ɻ�� ��õ�� ���� ������ȸ���� Ȯ���� ��ȹ�̴�. ���� ��ǥ �ӱ�� 2��, �缱�� ��ǥ �ӱ�� 1���̴�."],
# ["���� ���ǵ����� ��īī�� īǮ���� �ݴ��ϴ� ���� �ýþ��� �����ڵ��� 20�� ��Ը� ��ȸ�� ���δ�. �ýñ�� �� �� ���� �н� ���� ���� ���谡 ���ѷ������ ������ ��� ��ȸ?���� �ð��� ��?��� �ð��� ���� �� �ð� ���ǵ� �ֺ��� �ؽ��� ����ü���� ����ȴ�. 19�� ������ �ýþ��� � ������ 20�� ���� 2�� �����ýó뵿���տ���, ���������ýó뵿���տ���, ���������ýÿ�ۻ�����տ���ȸ �� 4�� ��ü�� ���� ���ǵ� ��ȸ �� �ǻ���ο��� 3�� ��ȸ�� ����. ����ǥ �����ýó뵿���տ��� �������� ��ȸ�� �Ϸ� �յΰ� ���� ����ȸ�߿��� ���׵��� ����� �ѷ� ������ �� �͡��̶�� ���ߴ�. ����ȸ�� �����ϰڴٴ� ���� ��ȹ�� �״�� ����Ǵ��ġ��� ������ �� �������� ���׷��١��鼭�� ������ (������) ������ �� �� ��������, �ϴ� ������ �ּ��� ���� ���� 1ȣ�� ��ȸ�� �ݵ�� ������ �͡��̶�� �����ߴ�. �� �������� �������� ���ֵ��� ������ ������ �ýð� ������ �����Ѵ١��� �������� 4��, 5�� ��ȸ ������ ������ �� ������ �ý� ������ ������ �͡��̶�� ���ߴ�. �̾� ���ڲ� �ùο��� ������ ����˼������� �������� ��Ű�� ���� ���ǵ� ��ȸ �տ� ���� ���ۿ� ���� ������ ��Ȳ�� ��Ʒ� �ֽñ� �ٶ��١��� ���ٿ���."],
#        ["'������ ã����' Ȩ�������� ������ ���ַ� ���� ���� ���ð��� ������� �ִ�. 19�� ���� 9��20�� ���� '������ ã����' Ȩ���������� ������ ���� ������ ���� �̿��� �Ұ����� ���´�. ���� ����Ʈ ������ ���� 4641���� ���Ѵ�. �ݰ����� ������ 11�� �� ���� �Һ��ڰ� ã�ư��� ���� ���� ������� �� 9��8130����� ������ ��Ÿ����.������ 12������ �����ޱ��� ��������� ã���ֱ� �ȳ� Ȱ���� ���� �� 3��125���(240��5000��)�� ������ ã�Ҵ�. ���Ǻ��δ� ������ȸ�簡 �� 2��7907���(222����), ���غ���ȸ�簡 2218���(18�� 5000��)�� ã�����. �ݰ����� 20�Ϻ��� ���� '������ ã����' ���񽺸� ������ ã�� ����������� �� ����ȸ�� �¶��� û���ý��ۿ� �ٷ� ������ ���ֵ��� ��ũ�� �����Ѵٰ� ������. ���� ���� ����� û�� �ÿ��� �Һ��ڰ� ���������� �ش� ����ȸ�� Ȩ������, �ݼ���, ��� ���������� ��� ����� ���� ã�� ������ �����ؾ� �ϴ� ������ �־���. �����δ� '������ ã����' Ȩ�������� ������ �̸�, �޴��� ��ȣ, �ֹε�Ϲ�ȣ�� �Է� �� �޴��� ������ ��ġ�� ������ 25����, ���غ��� 16���� �� ��� 41�� ����ȸ�縦 ������� ���� ������� ��ȸ�� �� �ִ�. ���� ������� �ִ� ��� �ش� ����翡 ����� ����û���� �ϸ� ������ 3�� �̳� �ݾ��� �����Ѵ�. �� �̹� ������� û���� �ɻ� ���̰ų� �������� ������ û���� �� ���� ������� ��ȸ���� �ʴ´�."],
#        ["KB������ �輺�� KB���� IB�Ѱ� �λ���� ������ KB���� WM �ι� �λ����� ���� ��ǥ�� ���� �����ߴٰ� 19�� ������. ������, ������ ��ǥ�̻簡 �ڸ����� ���������� ���� ��ǥ�̻� ü���� �����ȴ�. �̴� WM�� IB�� �ι��� ���� �����ϱ� �������� Ǯ�̵ȴ�. Ư�� �� ���� ��ǥ�� ���Ǿ��� ù ���� �ְ�濵��(CEO)�̴�. �� ���� ��ǥ�� ����� �濵�а����濵���п� ������� 1986�� ü�̽�����ư ��������, ��������, �Ｚȭ�� ���� ���� 2004�� ó������ KB�������࿡ ���Դ�. ��� ��������ũ ������ �������� 2012�⿣ WM������, 2014�� ����ũ�����׷� ������, 2015�� KB�������� ����ũ����å���� �λ��� �� ����ũ�����׷� �������� �þҰ� 2016�⿣ ���ű׷� �������� �þҴ�. �۳���� KB���� WM�Ѱ� �λ��� �� ���� WM�׷� ������ �� KB���� WM�ι� �λ����� �ð� �ִ�. KB�������ִ� �� ���� ��ǥ�� ���� WM, ����ũ, ���� �� ������ ���� ������ �������� ���� Ȯ�뿡 ���� ���࿪���� �����ϰ� �ִٰ� ������. �׷� WM �ι��� �ó��������� ���������ϸ� �������� �����ߴٴ� �򰡴�. �� IB�Ѱ� �λ����� �輺�� ���� ��ǥ�� IB�ι��� �Ѱ��Ѵ�. �� ���� ��ǥ�̻�� ������ �����а��� �����ϰ� 1988�� ������ǿ� �Ի��� ���� �Ѵ������������� ���� 2008�� KB�������� ����������������� �Ӹ�ƴ�. ���� 2015����� KB�������� IB�ι����� ���� ��������. KB�������ִ� �� ���� ��ǥ�� ���� IB �������� �����ڻ� �ٺ�ȭ ���� ���� ���� ������ ������ų �� �ִ� ������ �������� �����ߴٰ� ���ߴ�."], 
#         ["""���α���������� ���� 18�� ���� û��õ�� �������� ��2�� ���α��� ������ ����ȸ�� �����ߴټ� 19�� ������.

# �̹� ����ȸ�� ���α���, ����, ��Ȱ��� �� �� �о� ���������� ������ ���, ��å���α��� ������ ���⼺�� ���ؼ� �ǰ��� û���ϱ� ���� ���õƴ�. �̳� �� ������ "�ҵ���ȭ�� ������ ��ȭ ������ ���Ρ�������, �ڿ����ڵ��� ������ ������� Ŀ���� ��� ��ȸ���������μ� ���α����� ������ �߿��� ����"�̶��, "���� 8��� �����ڰ� 263�����̰� �̵��� 74%�� ��ü���� ��Ȳ���� �������� ���� �̿��� ����� ���������� �� �ʿ��� ���α��� ������ ���� ����ؾ� �Ѵ�"�� �����ߴ�.

# �̾ �� ������ "���� �������� �ǰ��� �ݿ��Ͽ� �������� ���� ������ �Բ� ��������, ������, ���ջ�� �� ��Ȱ����� �����ϵ��� �����ڴ�"�� ������. �̳� �����ڵ��� '��å���α��������� ���� ���⼺'�� ���Ͽ� �پ��� �ǰ��� �����ߴ�.

# ������� �̳� ����ȸ�� �پ��� ������� �������� �����ڰ� ü���� �� �ִ� �������� ��� ������ ���� ���� ����ϰ�, ���������� ���α��� ������ ������ �ǰ��� û���� ��ȹ�̴�.
# """],
#        ["""JB�������ִ� ���� ȸ�� �ĺ��ڷ� ���ȫ JB�ڻ��� ��ǥ(����)�� �����ߴ�.

# 19�� JB�������� �ӿ��ĺ���õ����ȸ�� ���� �ĺ����� ���� PT��ǥ�� ���������� ������ ��, �� ��ǥ�� ���� �ĺ��ڷ� �����ߴ�.

# �̳� PT��ǥ�� ������������ �ĺ����� JB�����׷��� ���� ������ ������, ������, ����� ��ȸ�� å�� �� �ĺ����� ������ ���� ��������, �� ��ǥ�� ������ ��� �����, �ڻ���� �� ������ �ӿ� ������ �������� ���� ���ݿ� ���� �������� ���İ� ���� �İ��� ���߰� �ִٴ� ���� ���� �򰡵ƴ�.

# JB�������� ������ �����ڴ� "�� �ĺ��ڰ� 20�� �̻� ��������� ������ ������ �������� ������ ���� �������� �İ� �� �� �ƴ϶� �����ʰ� ����ɷµ� Ź���ϴ�"�� "�޺��ϴ� ����ȯ�濡 �����ϰ� �迭�� �� �ó��� â���� ���� �����ġ�� �ش�ȭ�ϴ� �� JB�����׷��� �ְ��� �Ҹ����� �����׷����� ������ų ������"��� ������. �̿� ���� �� �����ڴ� ���� 3�� ����������ȸ�� �̻�ȸ�� ���� ��ǥ�̻� ȸ������ ���� �� �����̴�.
# """], 
#         ["""1800�� �ٷ����� 2018�� �ͼ� �ٷμҵ濡 ���� �������� �Ű�Ⱓ�� �� �޿� ������ �ٰ��Դ�.

# ���� �������꿡�� �߼ұ�� ��� û�⿡ ���� �ҵ漼 ������ Ȯ��ǰ� ������������ ����׿� ���� �ſ�ī�� ���׿� �ҵ������ ����Ǵ� �� ���ο� ������ ����Ǳ� ������ �ٲ� ���� ������ �Ĳ��� ì��� ���� �߿��ϴ�.

# ����û�� ���� �ٷμҵ��� �߻��� �ٷ��ڴ� ���� 2���� �޿��� ���޹��� ������ ���������� �Ű��ؾ� �Ѵٰ� 20�� ������.

# �޿��غ��� �޶����� �ֿ� ���� �׸�

# ���� ����������ʹ� �߼ұ�� ��� û�⿡ ���� �ҵ漼 ������ ���� �� �ִ� ��� ������ ���� 29������ 34���� Ȯ��ȴ�. �������� 70%���� 90%�� Ȯ��ǰ� ���� ����Ⱓ�� 3�⿡�� 5������ Ȯ��ȴ�.

# �ѱ޿��� 7000���� ���� �ٷ��ڴ� ������������ �ſ�ī��� ������ ��� �ش� ����� �ִ� 100�������� �߰� �ҵ���� ���� �� �ִ�. �� 7��1�� ���� ����������� ������ �ݾ��� �ҵ������ 30%�� ����Ǳ� �����̴�.

# �ǰ����� ����Ư�� ����ڷ� ��ϵ� �ξ簡���� ���� ������ �Ƿ��� ���� 700���� �ѵ��� �����ǰ� ���غ��� ���װ����� ���� �� �ְ� �ƴ�.

# �ѱ޿����� 5500�����̰ų� ���ռҵ�ݾ��� 4000���� �ʰ� �ٷ����� ��� ������ ���װ������� 10%���� 12%�� �λ�ȴ�. ������ ���װ��� �ѵ��� 750�����̸� �Ӵ��� ��༭�� �ּ����� ���Ⱓ �� ������ ��Ȯ�� �����ؾ� ������ ���� �� �ִ�.

# ���������� 3��� ������ ���� ���������� ��ȯ ���� ����ᵵ ���� ����������� ����� ���װ����� ���� �� ������, ������ �ٷ����� �ʰ��ٷμ��� ����� ���� �� ������ �Ǵ� ������ �޿����� 150���� ���Ͽ��� 190���� ���Ϸ� ����ȴ�.

# 6�� ���� �ڳ� ���װ����� �Ƶ����� ���޿� ���� ���غ��� �����ȴ�. �� ����������ʹ� ������ü�� �����ο��� ������ �ҵ浵 �Ű��� ���Եȴ�."""]
#        ]
from gensim.models import KeyedVectors
# kkma = Kkma()

# sentences = []
# list_vec = []
# for da in data:
# #     print(da)
#     sentences.append(kkma.sentences(da[0]))
#     for s in sentences:
#         for w in s:
#             list_vec.append(kkma.nouns(w))

# word_list = []
# for l in list_vec:
#     empty_vec = []
#     for w in l:
#         if len(w)>=2:
#             empty_vec.append(w)   
#     word_list.append(empty_vec)        

# import pandas as pd
# f= pd.read_csv(r"C:\Users\mm411\OneDrive\���� ȭ��\cralwer\Scrapy\data.tsv","\t")

# with open(r"C:\Users\mm411\OneDrive\���� ȭ��\cralwer\Scrapy\data.tsv", 'r') as inp, open('word2vec-format.txt', 'w') as outp:
#     line_count = '...'    # line count of the tsv file (as string)
#     dimensions = '...'    # vector size (as string)
#     outp.write(' '.join([line_count, dimensions]) + '\n')
#     for line in inp:
#         words = line.strip().split()
#         outp.write(' '.join(words) + '\n')
# print(f)
#model = KeyedVectors.load_word2vec_format("Scrapy//ko//ko.bin")
# embedding_model = Word2Vec(word_list, size=100, window = 5, min_count=2, workers=3, iter=1000, sg=1, sample=1e-3)

# from sklearn.cluster import KMeans

# word_vectors = embedding_model.wv.syn0 # ������ feature vector
# num_clusters = int(word_vectors.shape[0]/50) # ���� ũ���� 1/5�� ��� 5�ܾ�
# print(num_clusters)
# num_clusters = int(num_clusters)

# kmeans_clustering = KMeans(n_clusters=num_clusters)
# idx = kmeans_clustering.fit_predict(word_vectors)

# idx = list(idx)
# names = embedding_model.wv.index2word
# word_centroid_map = {names[i]: idx[i] for i in range(len(names))}

# for c in range(num_clusters):
#     # Ŭ������ ��ȣ�� ���
#     print("\ncluster {}".format(c))
    
#     words = []
#     cluster_values = list(word_centroid_map.values())
#     for i in range(len(cluster_values)):
#         if (cluster_values[i] == c):
#             words.append(list(word_centroid_map.keys())[i])            
#     print(words)


# import chardet    

# with open(r"C:\Users\mm411\OneDrive\���� ȭ��\cralwer\Scrapy\NlpModel\nlpmodel.model", 'rb') as rawdata:
#     result = chardet.detect(rawdata.read(10000))

# # check what the character encoding might be
# print(result)

# import pandas as pd

# f=open("word2vec-format.txt","r")
# # print(f)
# from gensim.models import KeyedVectors


# #wv = KeyedVectors.load(r"C:\Users\mm411\OneDrive\���� ȭ��\cralwer\Scrapy\kumed-w2v-300.model")
# model = KeyedVectors.load(r"C:\Users\mm411\OneDrive\���� ȭ��\cralwer\Scrapy\word2vec-KCC150.model")
# model_result = model.wv.most_similar("��ǳ")
# print('model_result =', model_result)

# import kss
# # s="ȸ�� ���� �е�� �ٳ�Դµ� �����⵵ ���� ���ĵ� ���־���� �ٸ�, ���� �䳢���� ���� �������� ����� �� �ö󰡾� �ϴµ� �ٵ� ���������� ��Ȥ�� �Ѿ �� �ߴ�ϴ� ������ ���� �䳢���� �ܺ� ���."
# # sents=[]
# # for sent in kss.split_sentences(s):
# #     sents.append(sent)

# # print(sents[0])
# # print(sents[1])
# # print(sents[2])
# import re
# pattern = '#([0-9a-zA-Z��-�R]*)'
# hash_w = re.compile(pattern)

# str="���� ���Ҹ��� �������� �� �ȶ����� ����.�߰��� ���η� �ٲ�µ��������� �ƴ��٤���#����_�û�ȸ https://t.co/7mYslwZIP"
# hash_tag = hash_w.findall(str)
# print("�ؽ��±� ����: ", hash_tag)
# for tag in hash_tag:
#     print("tag => ", tag)

# #print(str)


# # str3="2023-02-25 10:00:46+00:00"

# # str3=str3[0:11]+ "{}".format(int(str3.split(" ")[1][0:2])+9)+str3[13:19]
# # print(str3)

# # # str2="2023-02-20T13:38:08.000Z"

# # # str2=str2[:10]+" "+str2[11:19]
# # # print(str2)

# import requests
# from datetime import datetime
# from dateutil.tz import gettz
# from datetime import timedelta
# #from fasttext
# import gensim
# import pymongo
# from flask_cors import CORS
# import random
# import sqlite3
# import MySQLdb
# from mysql.connector import Error 
# from gensim.test.utils import common_texts
# import pandas as pd


# def scheduledTask(number=160,minutes=30):
#     print('�н��� ������ �ִ� ���� ����:',number)
#     dataset = []
#     try:
#         conn=MySQLdb.connect(
#             user="root",
#             passwd="1234",
#             host="localhost",
#             db="crawlerdb"
#            )
#         cursor = conn.cursor()
#         sql = "SELECT snsname,content FROM post"
#         cursor.execute(sql)
#         dataset=list(cursor.fetchall())
#         dataset_naver = []
#         dataset_twitter = []
#         dataset_instargram = []
#         for element in dataset:
#             if element[0] == 'twitter':
#                 dataset_twitter.append(element[1])
#             elif element[0] == 'instagram':
#                 dataset_instargram.append(element[1])
#         dataset = dataset_twitter + dataset_instargram
#         print(dataset)
#         if len(dataset) > number:
#             if len(dataset_instargram) >= int(number/4) and len(dataset_twitter) >= int(number/4) and len(dataset_naver) >= int(number/2):
#                 dataset = random.sample(dataset_instargram,int(number/4)) + random.sample(dataset_twitter,int(number/4)) + random.sample(dataset_naver,int(number/2))
#             elif len(dataset_twitter) >= int(number/7) and len(dataset_naver) >= int(number/3):
#                 dataset = random.sample(dataset_twitter,int(number/7)) + random.sample(dataset_naver,int(number/3))
#             else:
#                 dataset = random.sample(dataset,number)
#         #Ds=pd.DataFrame(dataset,columns=['data'])
#         #Ds.to_csv("save.csv", index = False)
      
#         # trained_dataset = nlp(dataset,model)
#         # trained_number = len(trained_dataset)
#         # print('�н��� ������ ����',trained_number)

#         # for post in trained_dataset:
#         #      conn.insert_one(post)
#     except Exception as e:
#         print(e)

# scheduledTask()

# import plotly.express as px
# import kss
# from sklearn.cluster import KMeans

# model=  KeyedVectors.load_word2vec_format("word2vec_model_result") # �ҷ���

# data_content_all = ['�ڷγ� �ű� Ȯ���ڰ� �߻��ߴ�.', 'ȭ�簡 �߻��ߴ�.', 'ȫ�� ���ذ� �߻��ߴ�.', '��� ����.', '���� ���� ������.', '�꿡 ���� ����.', '�ر� ��� �߻��ϴ�.', '�����ϴ�.', '��ǳ�� �߻��ߴ�.']
# data_pre = len(data_content_all)

# content_vector = []
# word_vectors = model
# content_vector = word_vectors.get_normed_vectors()



# df=content_vector
# target_label_=[]

# # for i in range(data_pre):
# #  target_label_.append(kmeans.labels_[i])
# print(df)
  
# if len(content_vector) > 200:
#     kmeans = KMeans(n_clusters=10, init='k-means++').fit(content_vector)
# elif len(content_vector)  > 50:
#     kmeans = KMeans(n_clusters=10, init='k-means++').fit(content_vector)
# elif len(content_vector)  > 21:
#     kmeans = KMeans(n_clusters=10, init='k-means++').fit(content_vector)
# fig = px.scatter_3d(
#     df, x='sepal_length', y='sepal_width', z='petal_width',
#     color = kmeans.labels_
# )
# fig.show()



# ## ���� üũ �Լ�
# def local_check(str):
#    print(str)





# from konlpy.tag import Kkma
# text="���� ���� �Դ´�."
# Kkma =  Kkma()

# text=Kkma.nouns(text)
# for i in text:
#     print(i)


# import re
# main_text="#����#���� �����������̷�����¥"
# # ''�±� �и�����
# hashtags=[]
# if '#' in main_text:
#     pattern = '#([0-9a-zA-Z��-�R]*)'
#     hash_w = re.compile(pattern)
#     hash_tag = hash_w.findall(main_text)
#     for tag in hash_tag:
#            if tag!="":
#                hashtags.append(tag)
#                main_text=main_text.replace('#'+tag,'')


# print(main_text)
# print(hashtags)
# import kss
# # list=['abc','def','ghp']
# str="���� ���� �Ծ��� �׷��� ����"
# list=list+kss.split_sentences(str)
# print(list)

# import sys
# import os
# sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
# import utility.util as util
# import utility.DB_Utility as db
# import numpy as np
# minmaxCountList=db.minmaxCount()[0]
# min=minmaxCountList[0]
# max=minmaxCountList[1]
# CountList=np.array(range(min,max))
# CountList= np.delete(CountList,0)
# print(CountList)
# content="�ڷγ�"
# param=('%%%s%%'%content)
# print(param)
# a=db.GetPost(str(14))[0][0]
# print(a)
# post="��Ʈ���ν�Ȳ?��Ʈ���ν�Ȳ�ȳ��ϼ���?�����ϴ����ε����Դϴ���?�ð�?��Ʈ����?��Ȳ��?����?�����帮��?�մϴ������ϼż�?�����Ͻñ�?�ٶ��ϴٱ���?����?��?����?����?���������ε���?�ݵ��ϰ�?�ֱ�?��������Ʈ���ο�?������?����?�������?�Ͽ����߰��ż���?�ϱ⿡��?����?�߼�?��ȯ��?�Ͼ��?�ʾ�����������?��?�ڸ���?�����ƴ϶��?�Ͽ��ٰ�к���?����ϸ�?��Ʈ���ε�?��κ���?����?�߼���ȯ��?�Ϸ���?�ð���?�ʿ��ϴٰ�?�����ѴٸŸ�?�����?�ؿ���?�ٽ�?��?��?����ϰڴ���?�ð�?��Ʈ����?����?����̴���?�ð�?��?������?����ť�پ���ť��?�����ֶ�?��������?��������?��Ʈ��?���ϰ�?��������?����?����?��?�ϳ��ٱ׷���?�ϴ���?����?����?����?ũ�⿡?������?�ż���?��?�����?�ɰ���?���̳ʽ���?������?��������?�����Ѵٺ��ε�?����ť��?���Ҹż�?�޾Ƽ�?�����?����?���Ҿ��ٱ���?����ť��?����Ͽ�?������?�����ϰ�?���Դ������?��?�ö�?��?�ִ�?������?������?������������?�����Ȳ��?�����غ�?��?�����?�ٽ�?����?������?�ִٰ�?�����Ͽ��ٸ�?��������?������?�Ű��?��ǥ��?����?����?���ũ�ν���?�߻��ϱ⿡?�ð���?�ʿ��ϴ�?�����Ͽ�?����?�ڸ���?�شٸ�?��?��?�ٽ�?�����ص�?����?�ʰڴٰ�?�����Ͽ���?�����̴��ķ���õ�����?�ڼ���?������?��α׿���?Ȯ�����ּ����ν�Ÿ�׷�?�����ʿ���?��α׸�ũ��?Ȯ�����ּ��䵶���ϴ�����?����?��α�?����������?��Ʈ����?��Ʈ����?����?����?����?����?����?����?����?������?���ڵǱ�?�ֽ�?���ڰ���?����?����Ʈ?�ڷγ�?����?å?å��õ?������õ?����������"

# idList=db.findContent(post)
# for index,id in enumerate(idList):
#     postList=db.GetPost(str(id[0]))
#     service=postList[0][0]
#     keyword=postList[0][1]
#     username=postList[0][2]
#     content=postList[0][4]
#     sns=postList[0][5]
#     link=postList[0][6]
#     date=postList[0][7]

print("�ȳ�")