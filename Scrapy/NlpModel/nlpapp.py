import MySQLdb
import pandas as pd
from gensim.models import KeyedVectors
from konlpy.tag import Kkma
from . import nlpmodel
import utility.DB_Utility as db
import random

def scheduled_task(number,max_post_id):
    ## 꼬꼬마 사용 -> 명사로 분리하기 위해
    _Kkma =  Kkma()
    ## word2vec 사용
    model=  KeyedVectors.load_word2vec_format("word2vec_model_result") # 불러옴
   
    print('학습할 데이터 최대 개수 지정:',number,"max_post_id:",max_post_id)
    try:
        ## mysql 연결
        conn=MySQLdb.connect(
            user="root",
            passwd="1234",
            host="localhost",
            db="crawlerdb"
        )
        cursor = conn.cursor()
        query = "SELECT service,content,sns,keyword,date,link FROM post where id >= %s"
        param=(max_post_id)
        cursor.execute(query,param)
        dataset= pd.DataFrame(cursor.fetchall(),columns=['service','content','sns','keyword','date','link'])
       
        ##리스트로 변환
        dataset_twitter = []
        dataset_instagram = []
        dataset_naverblogcafe = []
        for col,record in dataset.iterrows():
            if record['service'] == 'twitter':
                dataset_twitter.append(record)
            elif record['service'] == 'instagram':
                dataset_instagram.append(record)
            elif record['service'] == 'naverBlogCafe':
                dataset_instagram.append(record)
        dataset = dataset_twitter + dataset_instagram+dataset_naverblogcafe

        if len(dataset) > number:
            if len(dataset_instagram) >= int(number/4) and len(dataset_twitter) >= int(number/4) and len(dataset_naverblogcafe) >= int(number/2):
                dataset = random.sample(dataset_instagram,int(number/4)) + random.sample(dataset_twitter,int(number/4)) + random.sample(dataset_naverblogcafe,int(number/2))
            elif len(dataset_twitter) >= int(number/7) and len(dataset_naverblogcafe) >= int(number/3):
                dataset = random.sample(dataset_twitter,int(number/7)) + random.sample(dataset_naverblogcafe,int(number/3))
            else:
                dataset = random.sample(dataset,number)
          


        dataset_number = len(dataset)
        print('학습 전 데이터 개수',dataset_number)


        trained_dataset =  nlpmodel.nlp(dataset,model)
        trained_number = len(trained_dataset)
        print('학습된 데이터 개수',trained_number)

        for post in trained_dataset:
           idList=db.findContent(post) #content를 통해 id값을 찾음
    
           for index,id in enumerate(idList): ## id값을 통해 post 값을 찾음

                postList=db.GetPost(str(id[0]))

                (id, service, keyword, username, content, sns, link, date) = postList[0]

                #usepost 테이블에 저장
                db.usePostSave(service,keyword,username,content,sns,link,date)
   
                ## 현재 post id값 가져오기
                postid=db.getUsePostId()

                # hashtag 테이블에 postid 컬럼의 null공간을 postid값으로 변경
                db.hashtagAddPostId(str(postid[0][0]),str(id))
             
                #kkma를 통해 content 분리
                contentList=_Kkma.nouns(content) 
      

                #분리한 content를 hashtag테이블에 저장
                for cont in contentList:  
                    if(len(cont)>=2):

                        db.addHashtagSave(service,cont,postid[0][0],keyword)
                
                ## break 문으로 중복 값 제거
                break
        print("nlp 분석 저장 데이터가 모두 usepost,hashtag 에 저장됐습니다.. ")

    except Exception as e:
        print(e)
