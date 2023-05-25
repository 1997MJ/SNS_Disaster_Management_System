# 🔔 재난 키워드 분석 "재난 관리 웹사이트"

재난 상황을 한눈에 알아볼 수 있는 재난 사이트

<br>
  
## 📄 프로젝트 소개
 소셜 미디어의 실시간 데이터를 통해 재난 상황을 한눈에 보여주는 웹사이트

## 🎯 프로젝트 기획의도
근 코로나바이러스 감염증(COVID-19), 태풍 힌남노(Hinnamnor), 이태원 압사 사고, 튀르키예-시리아 지진 등 재난 상황이 빈번하게 발생하면서 뉴스, 소셜 미디어, 재난 문자, 재난 상황에 있는 사람에게 연락하는 방법 등으로 재난 상황을 알 수 있었다. 이렇게 다양한 방법이 있지만 소셜 미디어를 포함해 한눈에 재난 상황을 볼 수 있는 매체는 없었다 이에 따라 이런 문제들을 해결하는 웹사이트의 필요성을 느낌


## 📅 개발 기간
2023.01.05 ~ 2023.05.23

## 🔧 기술 스택
- Front-End : Html, css, JavaScript
- Back-End : Spring Boot, Java
- DB : MySQL
- Server : Apache

## 📚 주요 기능
#### 1. sns 데이터 수집 
- 각 api를 통해 인스타그램/트위터/네이버 블로그/네이버 뉴스 크롤링

#### 2. 데이터 필터링 
- word2vec 모델을 통해 데이터 벡터화
- kmeans-클러스터링을 통해 데이터 군집화

#### 3. 데이터 저장
- MYSQL을 연결하여 데이터 저장 및 활용


#### 사용 방법
- word2vec 모델 압축을 풀어주세요
- pips.txt를 통해 모듈을 설치해주세요



#### 메인 페이지 
<img width="80%" src="https://user-images.githubusercontent.com/86345166/240898171-4ed4dee0-92a0-49e3-b0b7-175c003b3c9c.png"/>

-각 SNS인 트위터, 인스타그램, 네이버 블로그에서 크롤링과 필터링 과정을 거친 해시태그 데이터 개수를 확인할 수 있다. 죄측에 위치한 today average는 각 SNS 데이터의 총합을 나타냄

-인기 검색어로 크롤링과 필터링 과정을 거친 데이터들에서 언급된 빈도수가 높은 순으로 해당 단어와 언급량을 수로 나타내며 이를 내림차순으로 1위부터 7위까지 나열함

-인기 검색어에서 설명했듯이 유의미한 데이터를 수치로 내림차순 해 나타냄

-실시간 재난 차트로 언급된 유의미한 데이터에서 해당하는 재난 키워드의 양을 차트로 나타냄

-재난에 관련해 궁금한 점을 질문하면 질문에 대한 답변을 통해 궁금증 해소 역할을 하는 재난 관련 챗봇
#### 토픽 별 재난 현황 페이지
<img width="80%" src="https://user-images.githubusercontent.com/86345166/240898182-ae78bd04-944e-470b-a2ad-644efc14a501.png"/>

-실시간 키워드 차트로 실시간으로 재난 키워드의 언급량에 따른 차트를 확인할 수 있음

-실시간 재난 문자 방송으로 재난 안전포털에서 재난과 긴급단계에 따라 재난 상황을 알려주는 재난 문자 데이터를 가져와 제공하는 모습을 확인할 수 있음


-검색한 키워드(토픽)와 관련해 수집해온 모든 게시글 데이터가 표시되며 해당 게시글을 a태그(링크)로 설정하였기 때문에 해당 내용을 누르게 되면 그 SNS 게시글로 이동하게 됨