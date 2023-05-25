from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
import time
import pyautogui
import pyperclip
# chrome driver auto update
from webdriver_manager.chrome import ChromeDriverManager

from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import re
import json
import pandas as pd

import requests

import sys
import os
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
import utility.util as util
import utility.DB_Utility as db

class instagramCrawlerClass: 
 
 def __init__(self, keywords,start_time=None):
        self.keywords = keywords
        self.start_time = start_time
        self.service="instagram"
 def run(self):
        """
        스크래핑 시작
        """
        is_driver = self.setDriver()
        if(is_driver):
            response = self.getComments()
            return response
        else:
            print('실패')
            return []
 def setDriver(self):
        """
        로그인 상태의 드라이버 생성
        """
         # protect from webpage off
        chrome_options = Options()
        chrome_options.add_experimental_option('detach', True)

        # remove unnecessary error message
        chrome_options.add_experimental_option('excludeSwitches', ['enable-logging'])

        # auto upgrade recent chromeDriver -ver
        service = Service(executable_path=ChromeDriverManager().install())
        driver = webdriver.Chrome(service=service, options=chrome_options)

        # wait webpage loding
        driver.implicitly_wait(5)
        # driver.maximize_window() # screen size max

        # open webpage
        driver.get('http://www.instagram.com/accounts/login/')

        is_success_login = False
        service= "instagram"

        try: 
            # find id
            id = driver.find_element(By.CSS_SELECTOR, '#loginForm > div > div:nth-child(1) > div > label > input')
            id.click()
            # id.send_keys('mso82300@gmail.com')
            pyperclip.copy('mso82300@gmail.com')
            pyautogui.hotkey('ctrl', 'v')
            time.sleep(2)

            # find pw
            pw = driver.find_element(By.CSS_SELECTOR, '#loginForm > div > div:nth-child(2) > div > label > input')
            pw.click()
            # pw.send_keys('chlghddlf1@')
            pyperclip.copy('chlghddlf123')
            pyautogui.hotkey('ctrl', 'v')
            time.sleep(1)

            # find login_btn
            login_btn = driver.find_element(By.CSS_SELECTOR, '#loginForm > div > div:nth-child(3)' or '#loginForm > div > div:nth-child(4)')
            login_btn.click()
            # time.sleep(1)
            is_success_login = True
        except:
            print("instagram login fail")
            is_success_login = False

        if is_success_login == True:
            # if alarm is existence: click alarm_btn
            try:
                later_btn = driver.find_element(By.CSS_SELECTOR, '._a9--._a9_1') 
                later_btn.click()
                time.sleep(1)
            # if alarm is not existence: search the keyword
            except:
                print('page no alarm_btn')
            self.driver=driver
            return True
        elif is_success_login == False:
            return False
     
 def getComments(self):
    print(self.start_time,'분 이후')
    for keyword in self.keywords:
       
        tag_url = "https://www.instagram.com/explore/tags/{}/".format(keyword)

        self.driver.get(tag_url)
        time.sleep(2)
        # first_post = driver.find_element(By.CSS_SELECTOR, 'div._aagw')
        # first_post = self.driver.find_element(By.CSS_SELECTOR, 'div._ac7v._aang > div._aabd._aa8k._aanf')
        first_post = self.driver.find_element(By.CSS_SELECTOR, 'div._ac7v._al3n > div._aabd._aa8k._al3l')
        first_post.click()
        time.sleep(1)


        instagram_tags = []
        instagram_tag_dates = []

       
        check_arrow = True
        count_extract = 0
        url_text = ''
       
        upload_id_object_css="div._aaqt > div.x9f619.xjbqb8w.x78zum5.x168nmei.x13lgxp2.x5pf9jr.xo71vjh.x1n2onr6.x1plvlek.xryxfnj.x1c4vz4f.x2lah0s.x1q0g3np.xqjyukv.x6s0dn4.x1oa3qoh.x1nhvcw1 > span.x1lliihq.x1plvlek.xryxfnj.x1n2onr6.x193iq5w.xeuugli.x1fj9vlw.x13faqbe.x1vvkbs.x1s928wv.xhkezso.x1gmr53x.x1cpjm7i.x1fgarty.x1943h6x.x1i0vuye.xvs91rp.x1s688f"
        date_object_css="time._a9ze._a9zf"
        main_text_object_css="div._a9zr > div._a9zs > h1._aacl._aaco._aacu._aacx._aad7._aade"
        tag_css="a.x1i10hfl.xjbqb8w.x6umtig.x1b1mbwd.xaqea5y.xav7gou.x9f619.x1ypdohk.xt0psk2.xe8uvvx.xdj266r.x11i5rnm.xat24cr.x1mh8g0r.xexx8yu.x4uap5.x18d9i69.xkhd6sd.x16tdsg8.x1hl2dhg.xggy1nq.x1a2a7pz._aa9_._a6hd"
        print_flag=True

        next_arrow_btn_css1="div._aear > div._aaqg._aaqh > button._abl-"
       
        wish_num=100
        
        for index in range(9):
            WebDriverWait(self.driver, 100).until(EC.presence_of_element_located((By.CSS_SELECTOR, next_arrow_btn_css1)))
            time.sleep(1)
            next_arrow_btn = self.driver.find_element(By.CSS_SELECTOR, next_arrow_btn_css1)
            next_arrow_btn.send_keys(Keys.ENTER)
        
        while True: 
            print(f"count_extract - {count_extract} / wish_num - {wish_num}")
            if count_extract > wish_num:
                self.driver.close()
                self.driver.quit()
                print("수가 많아서 종료...")
                break
            
            
            
            time.sleep(1)
            # 위치정보
            if check_arrow == False:
                break
            # 올린사람 ID
            try:
                upload_id_object = self.driver.find_element(By.CSS_SELECTOR, upload_id_object_css)
                upload_id = upload_id_object.text
                # 현재 게시글 url
                url_text = self.driver.current_url
            except:
                upload_id = None
            # print(upload_id)

            # 날짜
            try:
                date_object = self.driver.find_element(By.CSS_SELECTOR, date_object_css)
                date_text = date_object.text
                date_time = date_object.get_attribute("datetime")
                date_title = date_object.get_attribute("title")
            except:
                date_text = None
                date_time = None
                date_title = None
            # print(date_time)


            datetime=util.get_date_time_instagram(date_time)
            if(datetime<self.start_time):
                print('기준 시간을 넘어가서 인스타 크롤링 종료')
                break

            # 본문
            try:
                main_text_object = self.driver.find_element(By.CSS_SELECTOR, main_text_object_css)
                main_text = main_text_object.text
            except:
                main_text = None
            # print(main_text)
       

            ## 본문 속 태그
            try:
                tag_list = self.driver.find_elements(By.CSS_SELECTOR, tag_css) # C7I1f X7jCj
                for tag in tag_list:
                    tag_raw = tag.text
                    tags = re.findall('#[A-Za-z0-9가-힣]+', tag_raw) 
                    extract_tags = ''.join(tags).replace("#"," ") # "#" 제거
                    extract_tag = util.get_contentNtag(extract_tags)
                    # 해시태그 저장
                    
                    db.hashtagSave(self.service, extract_tag,keyword)
            except:
                pass
            # print(extract_tags)

            sns=re.sub('<.+?>', '', str(main_text), 0).strip()
            content=util.get_content(main_text)
            db.snsSave(self.service,keyword,upload_id,content,sns,url_text,datetime)

            print('======저장완료=====')

            try:
                WebDriverWait(self.driver, 100).until(EC.presence_of_element_located((By.CSS_SELECTOR, next_arrow_btn_css1)))
                time.sleep(1)
                next_arrow_btn = self.driver.find_element(By.CSS_SELECTOR, next_arrow_btn_css1)
                next_arrow_btn.send_keys(Keys.ENTER)

                print("click next arrow button")
            except:
                check_arrow = False

            count_extract += 1

        