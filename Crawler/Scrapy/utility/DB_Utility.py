from datetime import datetime
import sqlite3
import MySQLdb
from mysql.connector import Error 
from datetime import date
import mysql.connector

DB_CONFIG = {
    'user': 'root',
    'password': '1234',
    'host': 'localhost',
    'database': 'crawlerdb',
}
## getDateTime() - 이 함수는 YYYY-MM-DD 형식으로 현재 날짜와 시간을 반환합니다.
def getDateTime():  
      return date.today()

## getMaxPostId() - 이 함수는 MySQL 데이터베이스의 'post' 테이블에서 'id' 열의 최대값을 검색합니다.
def getMaxPostId():
   with mysql.connector.connect(**DB_CONFIG) as conn:
        with conn.cursor() as cursor:
         query="""select IFNULL(max(id),0) from post;"""
         cursor.execute(query)
         data=cursor.fetchall()
         return data
        
        ## getMaxPostId() - 이 함수는 MySQL 데이터베이스의 'post' 테이블에서 'id' 열의 최대값을 검색합니다.
def getMaxHashtagId():
   with mysql.connector.connect(**DB_CONFIG) as conn:
        with conn.cursor() as cursor:
         query="""select IFNULL(max(id),0) from hashtag;"""
         cursor.execute(query)
         data=cursor.fetchall()
         return data
        
        

## newsSave(title,keyword,content,link,date) - 이 함수는 뉴스 관련 데이터를 MySQL 데이터베이스의 'navernews' 테이블에 삽입합니다.
def newsSave(title,keyword,content,link,date):
    with mysql.connector.connect(**DB_CONFIG) as conn:
        with conn.cursor() as cursor:
                query="""insert into navernews(title,keyword,content,link,date) values(%s,%s,%s,%s,%s);"""
                param=(title,keyword,content,link,date)
                cursor.execute(query,param)
                conn.commit()

                cursor.close()
                conn.close()

## snsSave(service,keyword,username,content,sns,link,date) - 이 함수는 소셜 미디어 게시물 관련 데이터를 MySQL 데이터베이스의 'post' 테이블에 삽입합니다.
def snsSave(service,keyword,username,content,sns,link,date):
    with mysql.connector.connect(**DB_CONFIG) as conn:
        with conn.cursor() as cursor:
                query="""insert into post(service,keyword,username,content,sns,link,date) values(%s,%s,%s,%s,%s,%s,%s);"""
                param=(service,keyword,username,content,sns,link,date)
                cursor.execute(query,param)
                conn.commit()

                cursor.close()
                conn.close()

## usePostSave(service,keyword,username,content,sns,link,date) - 이 함수는 사용자가 생성한 게시물 관련 데이터를 MySQL 데이터베이스의 'usepost' 테이블에 삽입합니다.        
def usePostSave(service,keyword,username,content,sns,link,date):

    with mysql.connector.connect(**DB_CONFIG) as conn:
        with conn.cursor() as cursor:
                query="""insert into usepost(service,keyword,username,content,sns,link,date) values(%s,%s,%s,%s,%s,%s,%s);"""
                param=(service,keyword,username,content,sns,link,date)
                cursor.execute(query,param)
                conn.commit()

                cursor.close()
                conn.close()

## hashtagSave(snsName,tag) - 이 함수는 해시태그 관련 데이터를 MySQL 데이터베이스의 'hashtag' 테이블에 삽입합니다.
def hashtagSave(snsName,tag,keyword):
   with mysql.connector.connect(**DB_CONFIG) as conn:
        with conn.cursor() as cursor:
                query="""insert into hashtag(id,snsName,tag,postid,keyword) 
                values( (select IFNULL(max(id),0)+1 from post),
                %s,%s,null,%s);"""
                param=(snsName,tag,keyword)
                cursor.execute(query,param)
                conn.commit()

 ## hashtagDelete(tag) - 이 함수는 topic_ban에 속한 topic을 제거함 
def hashtagDelete(tag):
   with mysql.connector.connect(**DB_CONFIG) as conn:
        with conn.cursor() as cursor:
                query="delete from hashtag where tag like '%"+tag+"%';"
                cursor.execute(query)
                conn.commit()               

## addHashtagSave(snsName,tag,postid) - 해당 게시물의 postid를 포함하여 해시태그 관련 데이터를 MySQL 데이터베이스의 'hashtag' 테이블에 삽입하는 기능입니다.       
def addHashtagSave(snsName,tag,postid,keyword):
        conn=MySQLdb.connect(
            user="root",
            passwd="1234",
            host="localhost",
            db="crawlerdb"
           )
        cursor = conn.cursor()
        query="""insert into hashtag(id,snsName,tag,postid,keyword) 
        values( (select IF(max>=9000 , max+1 , 9000) from (select max(id) as max from hashtag)as h),
        %s,%s,%s,%s);"""
        param=(snsName,tag,postid,keyword)
        cursor.execute(query,param)
        conn.commit()


## hashtagAddPostId(postid,id) - 이 함수는 주어진 해시태그 id에 대해 'hashtag' 테이블의 postid 값을 업데이트합니다.
def hashtagAddPostId(postid,id):
   with mysql.connector.connect(**DB_CONFIG) as conn:
        with conn.cursor() as cursor:
         query="update hashtag set postid='"+postid+"' where id='"+id+"';"
         cursor.execute(query)
         conn.commit()
        

## findContent(content) - 이 함수는 주어진 내용을 포함하는 레코드에 대해 'post' 테이블을 검색합니다.
def findContent(content): 
   with mysql.connector.connect(**DB_CONFIG) as conn:
        with conn.cursor() as cursor:
         query="select id from post where content like '%"+content+"%';"
         cursor.execute(query)
         data=cursor.fetchall()
         return data



## GetPost(id) - 이 함수는 주어진 id를 기반으로 'post' 테이블에서 특정 레코드를 검색합니다.
def GetPost(id): 
   with mysql.connector.connect(**DB_CONFIG) as conn:
        with conn.cursor() as cursor:
         query="select * from post where id= '"+id+"';"
         cursor.execute(query)
         data=cursor.fetchall()
         return data



## getUsePostId() - 이 함수는 MySQL 데이터베이스의 'usepost' 테이블에서 'id' 열의 최대값을 검색합니다.
def getUsePostId():
   with mysql.connector.connect(**DB_CONFIG) as conn:
        with conn.cursor() as cursor:
          query="""select IFNULL(max(id),0) from usepost;"""
          cursor.execute(query)
          data=cursor.fetchall()
          return data
        
        
def __init__(self):
    self.latest_link_key = None

def get_latest_link_key(self, keyword):
    with mysql.connector.connect(**DB_CONFIG) as conn:
        with conn.cursor() as cursor:
            # 해당 서비스와 검색어에 대한 가장 최근 link_key를 검색하는 쿼리
            query = f"SELECT id FROM post WHERE keyword='{keyword}' AND service='naverBlogCafe' LIMIT 1"
            # query = f"SELECT date FROM post WHERE keyword='{keyword}' ORDER BY id DESC LIMIT 1"
            
            # 쿼리 실행
            cursor.execute(query)
            
            # 결과 가져오기
            result = cursor.fetchone()
            
            # 결과가 있으면 link_key 반환, 없으면 0 반환
            if result:
                self.latest_link_key = result[0]
                print(result[0])
                return result[0]
            else:
                return 0
