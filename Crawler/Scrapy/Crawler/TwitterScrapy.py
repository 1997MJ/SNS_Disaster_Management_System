import snscrape.modules.twitter as sntwitter
import re
import sys
import os

sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
import utility.util as util
import utility.DB_Utility as db

class TwitterCrawlerClass:
    def __init__(self, keywords, start_time=None):
        self.keywords = keywords
        self.start_time = start_time
        self.service = "twitter"
        
    def run(self):
        """
        스크래핑 시작
        """
        print("twitter crawler start")
        response = self.get_comments()
        print(self.service + " 저장완료")

    
    def get_comments(self):
        for keyword in self.keywords:
            for tweet in sntwitter.TwitterSearchScraper(keyword).get_items():
                username = tweet.user.username
                main_text = tweet.content
                link = tweet.url
                dates = tweet.date
                dates = util.get_date_time_twitter(dates)
                if dates < self.start_time:
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