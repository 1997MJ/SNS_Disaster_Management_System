import tweepy
import pandas as pd

# 트위터 Application에서 발급 받은 key 정보들 문자열로 입력
consumer_key = "F461VVGA91pv2Gfy1WvkxetLO"
consumer_secret = 'Gp2GRRuaKf1u2RWpPfch8kYkdSt8YJRwmB3i3yZqTb9C30Rt9k'
access_token = '1592500962065002496-lIVpGackch3MP67Bt7HQOHtgDCVW5f'
access_token_secret = '1AHnM2rs7c0ipcHjyG0HpzFtFTPyfMvvfxZhFLNTAKNYc'

# 1. 트위터 키 입력
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)

# 2. 액세스 요청
auth.set_access_token(access_token, access_token_secret)

# 3. twitter API 생성
api = tweepy.API(auth)

#--------------------------
# twitter_search
#--------------------------
def twitter_search( keyword):
    result = []  # 크롤링 텍스트를 저장 할 리스트 변수

    for i in range(1, 4):  # 1~3 페이지 크롤링
        result = []
        for tweet in api.search_tweets(keyword):
            print(tweet.created_at)   
            print(tweet.entities['media'][0]['url'])
            dates= str(tweet.created_at)
            dates=dates[0:11]+"{}".format((int(dates.split(" ")[1][0:2])+9)%24)+dates[13:19]
            print(dates)

            break
            username = tweet.id_str
            main_text = tweet.text
            link = "empty"
            dates = tweet.created_at
            print(username,main_text,dates)
        break



#--------------------------
# Main
#--------------------------
if __name__ == "__main__":

    keyword = '지진'  # 키워드 입력
    twitter_search(keyword)

