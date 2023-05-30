# 네이버 검색 API 예제 - 블로그 검색
import urllib.request
import json
from datetime import datetime
import utility.util as util
import utility.DB_Utility as db
class naverBlogCafeCrawlerClass: 
    def __init__(self, keywords,start_time=None):
        self.keywords = keywords
        self.start_time = start_time
        self.service="naverBlogCafe"
        
    def run(self): 
        client_id = ""
        client_secret = ""
        
        for keyword in self.keywords:
            # 블로그
            encText = urllib.parse.quote(keyword)
            url = f"https://openapi.naver.com/v1/search/blog?query={encText}&sort=date&display=50"  # JSON 결과

            request = urllib.request.Request(url)
            request.add_header("X-Naver-Client-Id",client_id)
            request.add_header("X-Naver-Client-Secret",client_secret)

            response = urllib.request.urlopen(request)  
            rescode = response.getcode()
            
            if(rescode==200):
                response_body = response.read().decode('utf-8')
                result = json.loads(response_body)
                if result.get('items'):
                    for item in result['items']:
                        # 링크
                        link = item['link']
                        link_key = link.split('/')[-1]
                        
                        # DB에 저장된 가장 최신 link_key 가져오기
                        latest_link_key = db.get_latest_link_key(self, keyword)

                        if link_key == latest_link_key:
                            print('======저장 겹침=====')
                            break

                        print("Link:", link)
                        
                        # 제목
                        title = item['title'].replace('</b>','').replace('<b>','')
                        print("Title:", title)
                        
                        # 내용요약
                        description = item['description'].replace('</b>','').replace('<b>','')
                        content = util.get_content(description)
                        print("Description:", description)

                        now = datetime.now() ## 10분 전 시간 저장
                        current_date=now.strftime('%Y-%m-%d %H:%M:%S')
                        db.snsSave(self.service, keyword,  link_key, content, description, link, current_date)
                        print('======저장완료=====')
                        print()
                        
                        
                else:
                    print("검색 결과가 없습니다.")
            else:
                print("Error Code:" + rescode)