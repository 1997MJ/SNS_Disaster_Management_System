import Crawler.instagramScrapy as instagram
import Crawler.TwitterScrapy as twitter
import Crawler.NaverNewsScrapy as navernews
import Crawler.NaverblogScrapy as naverblog

import NlpModel.nlpapp as nlpapp
import time
import utility.DB_Utility as db
import schedule
from datetime import datetime, timedelta
import TopicFilter

def startCrawler():
      try:
        max_post_id= db.getMaxPostId()
        max_hashtag_id= db.getMaxHashtagId()

        keywords = ['교통사고','화재','폭설','태풍','지진','압사']
       
        # 가장 최신 포스트 시간 가져오기
        now = datetime.now()- timedelta(minutes=10) ## 10분 전 시간 저장
        start_time=now.strftime('%Y-%m-%d %H:%M:%S')
        
        # 인스타그램 크롤링 시작
        instar_cralwer= instagram.instagramCrawlerClass(keywords,start_time=start_time)
        instar_cralwer.run()

        # 트위터 크롤링 시작
        twitter_cralwer=twitter.TwitterCrawlerClass(keywords,start_time=start_time)
        twitter_cralwer.run()

        # 네이버 뉴스 크롤링 시작
        NaverNews_cralwer=navernews.NaverNewsCrawlerClass(keywords,start_time=start_time)
        NaverNews_cralwer.run()

        # 네이버 블로그 카페 크롤링 시작
        NaverBlogCafe_cralwer = naverblog.naverBlogCafeCrawlerClass(keywords)
        NaverBlogCafe_cralwer.run()

        # nlp 실행 (사용할 usepost 및 hashtag 추가)
        print("nlp 모델 실행")
        nlpapp.scheduled_task(3000,max_post_id)
        print("토픽 필터링 실행")
        TopicFilter.TopicFiltering(max_hashtag_id)
        print("토픽 필터링 완료")
      except Exception as e:
        print(e)

##현재 post id의 가장 큰 값을 가져옴 -> usepost에 누적 저장되지 않게 하기 위함

schedule.every(0).minutes.do(startCrawler) #10분마다 계속 실행

# 스케쥴 시작 (실제 실행코드)
while True:
    schedule.run_pending()
    time.sleep(10)
