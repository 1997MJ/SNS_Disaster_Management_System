
import re
import sys
import os
import tweepy
import pandas as pd
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
import utility.util as util
import utility.DB_Utility as db

# 트위터 Application에서 발급 받은 key 정보들 문자열로 입력
consumer_key = ""
consumer_secret = ''
access_token = ''
access_token_secret = ''

# 1. 트위터 키 입력
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)

# 2. 액세스 요청
auth.set_access_token(access_token, access_token_secret)

# 3. twitter API 생성
api = tweepy.API(auth)
class TwitterCrawlerClass:
    def __init__(self, keywords, start_time=None):
        self.keywords = keywords
        self.start_time = start_time
        self.service = "twitter"
        
    def run(self):
        """
        스크래핑 시작
        """
        print("twitter crawler start2")
        response = self.get_comments()
        print(self.service + " 저장완료")

    
    def get_comments(self):
        for keyword in self.keywords:
          for tweet in api.search_tweets(keyword,max_results = 100):
                username="user"
                link="url"
                main_text =  tweet.text
                sns="sns"
                dates = util.get_date_time_twitter(tweet.created_at)
                if dates < self.start_time:
                    print("종료")
                    break

                # ''태그 분리과정
                hashtags = re.findall('#([0-9a-zA-Z가-힣]*)', main_text)
                for tag in hashtags:
                    if tag != "":
                        db.hashtagSave(self.service, tag,keyword)
                        main_text = main_text.replace('#' + tag, '')

                # 시간 전처리 과정
                sns = re.sub('<.+?>', '', str(main_text), 0).strip()
                content = util.get_content(main_text)
                db.snsSave(self.service, keyword, username, content, sns, link, dates)

        # print(service + " 데이터 전송완료")
