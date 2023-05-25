import re
from emoji import core
import pytz
from datetime import datetime

def clean_text(text):
    cleaned_text = re.sub('[a-zA-z]','',text)
    cleaned_text = re.sub('[\{\}\[\]\/?.,;:|\)*~`!^\-_+<>@\#$%&\\\=\(\'\"\♥\♡\ㅋ\ㅠ\ㅜ\ㄱ\ㅎ\ㄲ\ㅡ]','',cleaned_text)
    cleaned_text = re.sub('<.*?>', '', cleaned_text)
    
    ##이모티콘 제거 
    emoji_pattern = re.compile("["
            u"\U0001F600-\U0001F64F"  # emoticons
            u"\U0001F300-\U0001F5FF"  # symbols & pictographs
            u"\U0001F680-\U0001F6FF"  # transport & map symbols
            u"\U0001F1E0-\U0001F1FF"  # flags (iOS)
            u"\U00010000-\U0010FFFF"
                               "]+", flags=re.UNICODE)
    cleaned_text= emoji_pattern.sub(r'', cleaned_text) # no emoji
    return cleaned_text


def dt_format(dt):
    if len(str(dt)) == 1:
        return f'0{str(dt)}'
    else:
        return dt

def is_valid_form(time):
    # 2021-11-22-11-22
    time_arr = time.split('-')
    # 년,월,일,시간,분 확인 
    if len(time_arr)!= 5 : 
        return False
    [year,month,day,hours,minutes] = time_arr
    # 자리수 확인
    if(len(year) !=4 or len(month) != 2 or len(day) != 2 or len(hours) != 2 or len(minutes) != 2):
        return False
    if(year.isdigit() and month.isdigit() and day.isdigit() and hours.isdigit() and minutes.isdigit()):
        return True


def delete_ObjectId(post):
    del post['_id']
    return post

def ping_form(post):
    del post['_id']
    del post['sns']
    return post

def get_content(sns_text):
    """
    한글과 띄어쓰기를 제외한 모든 부분을 제거
    두 개 이상 공백 제거
    """
    hangul = re.compile('[^ ㄱ-ㅣ가-힣]+')
    removed = hangul.sub('', str(sns_text))
    return  re.sub(' +', ' ', removed)

def get_contentNtag(sns_text):
    hangulNnum = re.compile('[^ ㄱ-ㅣ가-힣0-9]+')
    removed = hangulNnum.sub('', str(sns_text))
    rmv = re.sub(' +', ' ', removed)
    cln_txt = clean_text(rmv)
    if cln_txt == '' or cln_txt == "" or cln_txt == ' ' or cln_txt == " ":
        return None
    return cln_txt

def get_date_time_twitter(dates):
    dates=str(dates)
    dates=dates[0:11]+"{}".format((int(dates.split(" ")[1][0:2])+9)%24)+dates[13:19]
    dates=get_date_time_zero(dates)
    return dates

def get_date_time_instagram(dates):
    #ex)2023-03-03T14:01:33.000Z
    # dates=str(dates)
    # dates=dates[0:10]+" "+dates[11:19]
    # dates=get_date_time_zero(dates)
    
    # UTC 시간 문자열을 datetime 객체로 변환하기
    utc_time = datetime.strptime(dates, '%Y-%m-%dT%H:%M:%S.%fZ')
    # UTC 시간을 한국 시간으로 변환하기
    kor_tz = pytz.timezone('Asia/Seoul')
    kor_time = utc_time.replace(tzinfo=pytz.utc).astimezone(kor_tz)
    # 시간대 정보 삭제하기
    kor_time = str(kor_time.replace(tzinfo=None))
    return kor_time

def get_date_time_zero(time):
    if(len(time.split('-')[-1].split(' ')[1].split(":")[0])==1):
        time=time[:10]+" 0"+time[11:]
    return time
