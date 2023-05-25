
import MySQLdb
import pandas as pd


import utility.DB_Utility as db



def TopicFiltering(max_hashtag_id):
  ban_words = []
  with open("Scrapy/TextFilter/topic_ban.txt", encoding="UTF8") as f:
        ban_words = [line.rstrip("\n") for line in f]

      ## mysql 연결
  conn=MySQLdb.connect(
      user="root",
      passwd="1234",
      host="localhost",
      db="crawlerdb"
  )
  cursor = conn.cursor()
  query = "SELECT tag FROM hashtag where seq >= %s"

  cursor.execute(query,max_hashtag_id)
  dataset= pd.DataFrame(cursor.fetchall(),columns=['tag'])

  for word in ban_words:
    mask = dataset[dataset['tag'].str.contains(word)]
    if (mask.size>0):
       print(word+" 삭제")
       db.hashtagDelete(word)


