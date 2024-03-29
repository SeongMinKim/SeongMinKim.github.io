---
title: (데이터 자격증) SQLD 준비 후기와 팁
date: 2022-07-13 22:30:00 +0900
categories: [자유게시판, 자기개발]
tags: [ADsP, SQLD, SQL, 자격증]
---

> **3줄 요약**
<br>**어떤 시험?** SQL 써본 사람, 앞으로 쓸 사람에게 추천!
<br>**공부법?** 문제풀이와 유튜브 해설강의 병행
<br>**이것만은 꼭!** 기출문제는 많이 볼수록 좋아요
{: .prompt-tip }

# SQLD

> SQL 개발자(SQLD : SQL Developer)란 데이터베이스와 데이터 모델링에 대한 지식을 바탕으로 응용 소프트웨어를 개발하면서 데이터를 조작하고 추출하는데 있어서 정확하고 최적의 성능을 발휘하는 SQL을 작성할 수 있는 개발자를 말한다.[^1]

## 자격 소개

SQL 개발자 자격검정은 DBMS에서 데이터를 처리하기 위한 언어인 SQL에 대한 기본적인 이해를 갖추었는지 측정하는 시험입니다. 데이터모델의 이해 및 분석, SQL 이해 및 활용 2개 과목에 대해 평가하며, 시험에 응시하기 위한 별도의 자격 조건은 없습니다.

데이터베이스 분야만 집중적으로 검증하는 시험으로, ADsP나 DAsP 같은 다른 엔트리 레벨의 데이터자격검정보다는 전문성을 인정받는 편입니다. 수험생이 많은 편이며, 상위 등급 시험인 SQL 전문가(SQLP)를 준비하기 위해 응시하는 경우도 있습니다.

특이한 점은 ADsP, DAsP는 취득하는 즉시 영구적인 자격을 얻게되지만 SQLD는 최초 자격 획득시 2년간 자격을 유지하며, 자격 만료 전에 추가 교육을 이수해야만 영구 자격을 획득하게 됩니다.

## 시험 일정

한국데이터산업진흥원(Korea Data Agency) 주관으로 연 4회 시행되며, 분기에 1회 접수를 받습니다. 시험은 토요일 오전 10시에 시작합니다. 2022년 시험 일정은 아래 표를 참고해주세요.

|회차|접수기간|시험일|결과발표|
|---|---|---|---|
|44회|2/14 ~ 18|3/12|4/8|
|45회|5/2 ~ 9|5/28|6/24|
|46회|8/8 ~ 12|9/4|9/30|
|47회|10/10 ~ 17|11/5|12/2|

## 합격 기준

시험은 객관식 총 50문항/100점 만점(문제당 배점 각 2점)의 필기시험으로 진행됩니다. 총 60점(30문제) 이상을 획득하면 합격이며, 단 과목별 과락(40% 미만 취득)이 없어야 합니다. 과목별 문항수는 아래 표를 참고해주세요.

|구분|과목명|문항수|배점|시험시간|
|---|---|---|---|---|
|필기|데이터 모델링의 이해|10|20||
||SQL 기본 및 활용|40|20||
||총계|50|100|총 90분|

시험 과목별 세부 내용은 아래 표를 확인해 주세요.

|시험과목|세부 항목|
|---|---|
|데이터 모델링의 이해|데이터 모델링의 이해|
||데이터 모델과 성능|
|SQL 기본 및 활용|SQL 기본|
||SQL 활용|
||SQL 최적화 기본 원리|

# 공부법

## 주교재 선정

SQLD는 응시자가 많은 데이터 자격증인만큼 시중에 여러 수험서가 있습니다. ADsP에 민트책이 있듯이 SQLD에는 **노랭이**가 있습니다. 아래는 검토했던 교재 후보입니다.

### SQL 자격검정 실전문제 (한국데이터산업진흥원)✔️

시험을 출제한 한국데이터산업진흥원에서 집필한 실전문제집입니다. 표지가 노란색이라 **노랭이**라는 별칭이 있습니다.

![](/assets/img/2022-07-13/2022-07-13-certificate-sqld-book1.jpg)*SQL 자격검정 실전문제 / 279 페이지 / 정가 18,000원*

+ 아마도 가장 많은 응시자가 선택하는 교재입니다. SQLD는 문제은행식으로 출제되기 때문에 실전문제와 기출문제를 많이 풀어볼수록 좋습니다.

- 문제집이기 때문에 SQL 개념이 부족하시다면 개념서를 별도로 구입하시거나 구글링, 유튜브 검색해가면서 개념 공부를 먼저 하시는게 좋습니다. SQLP 수험생을 위한 교재이기도 하므로 실제 SQLD에 출제되는 수준보다 문제 난이도가 높은 편입니다.

### 2022 유선배 SQL개발자(SQLD) 과외노트 (시대고시기획)

SQL 유튜브 채널을 운영중이신 정미나님께서 집필하신 수험서입니다. 일명 **유선배**라고도 불립니다.

![](/assets/img/2022-07-13/2022-07-13-certificate-sqld-book2.jpg)*유선배 SQL개발자(SQLD) 과외노트 / 374 페이지 / 정가 22,000원*

+ 개념과 예상문제가 같이 포함된 수험서입니다. 편집이 깔끔하게 되어있고, 쿼리를 직접 날려볼 수 있게 오라클 환경설정 가이드도 있습니다.

- 설명이 충분하지 않다는 후기가 있습니다. 설명이 쉽지는 않은 편이라 비전공자가 독학하기에는 다소 어려울 수 있습니다.

### 시험장에 몰래 가져갈 이경오의 SQL+ SQLD 비밀노트 (한빛미디어)

![](/assets/img/2022-07-13/2022-07-13-certificate-sqld-book3.jpg)*이경오의 SQL+ SQLD 비밀노트 / 556 페이지 / 정가 32,000원*

앞서 언급드린 책 외에 SQL을 더 공부하고 이해하는 차원에서 추천하는 책입니다.

+ 공공 데이터 기반 실습 내용이 포함되어 있어 시험이 아닌 실제 데이터를 교재를 따라가며 조작할 수 있습니다.

- 책이 두꺼운 편입니다. SQLD 자격증을 위한 교재로도 쓸 수 있겠지만, 데이터 초심자가 실무에서 데이터를 다루기 위한 연습용으로 쓴다면 더 좋을 것 같습니다.

### 부교재 : 유튜브, 기출문제 블로그

SQL은 기초(2과목 SQL 기본 챕터 정도)적인 이해는 있었고 SQLD가 문제은행식으로 출제되기 때문에 주교재로 문제집을 선택했습니다. 그래서인지 공부하면서 유튜브나 블로그의 도움을 정말 많이 받았습니다. 도움이 되었던 유튜브 채널과 블로그를 공유드립니다. 어떻게 활용했는지는 공부법 챕터에서 설명드리겠습니다.

> **추천 유튜브 채널과 블로그**
<br>**[김강민 SQLP](https://www.youtube.com/channel/UCosmeBx3OuKP1YwGmT6ar2Q)**
<br>**[전광철 OCP](https://youtu.be/_dx3fPb766E)**
<br>**[SQL전문가 정미나](https://www.youtube.com/c/SQL%EC%A0%84%EB%AC%B8%EA%B0%80%EC%A0%95%EB%AF%B8%EB%82%98)**
<br>**[Study with yuna](https://yunamom.tistory.com/category/%EC%9E%90%EA%B2%A9%EC%A6%9D/SQLD%20%EC%9E%90%EA%B2%A9%EC%A6%9D)**
{: .prompt-tip }

## 공부 기간 : 약 2주

|<span style="color:red">일</span>|월|화|수|목|금|<span style="color:#0000ff">토</span>|
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
|**5/**<span style="color:red">**1**</span>|2|3|4|5|6|<span style="color:#0000ff">7</span><br>**<u>정처기(실기)</u>**|
|<span style="color:red">8</span>|9|10|11|12|13|<span style="color:#0000ff">14</span>|
|<span style="color:red; background-color:#fff5b1">15</span>|<span style="background-color:#fff5b1">16</span>|<span style="background-color:#fff5b1">17</span>|<span style="background-color:#fff5b1">18</span>|<span style="background-color:#fff5b1">19</span>|<span style="background-color:#fff5b1">20</span>|<span style="color:#0000ff; background-color:#fff5b1">21</span>|
|<span style="color:red; background-color:#fff5b1">22</span>|<span style="background-color:#fff5b1">23</span>|<span style="background-color:#fff5b1">24</span>|<span style="background-color:#fff5b1">25</span>|<span style="background-color:#fff5b1">26</span>|<span style="background-color:#fff5b1">27</span>|<span style="color:#0000ff">28</span><br>**<u>DAsP</u>**|

5월 7일에 정보처리기사 실기를 치고 방전된 나머지 며칠 쉬다가 주말부터 공부를 시작했습니다. SQLD 시험 준비 직전까지 정보처리기사 실기를 준비했기 때문에 SQL 기초 개념은 숙지한 상태로 공부를 시작할 수 있었습니다. 당시 회사 업무가 바빠서 평일에는 퇴근 후 2~3시간 정도 공부하고, 주말에는 8시간/일 정도 공부했습니다.

## 주차별 공부법

가장 먼저 SQLD 시험 범위에 등장하는 개념에 대해 내가 얼마나 알고 있는지 점검하고 문제를 풀면서 유튜브 해설강의에서 설명하는 개념을 이해해나가는 식으로 진행했습니다.

### 1주차 : SQLD 최종 정리강의 → 문제풀이 및 해설강의 시청

첫 날에는 유튜브 **[김강민 SQLP](https://www.youtube.com/channel/UCosmeBx3OuKP1YwGmT6ar2Q)**에 올라와있는 SQLD 최종 정리강의를 처음부터 끝까지 들으면서 SQLD에 등장하는 용어를 전체적으로 살펴봤습니다. 아는 것도 있었지만 낯선게 더 많았습니다. 동영상 두 개, 약 1시간 반 정도 분량인데 한 번 보시면 내가 SQLD를 칠 준비가 어느 정도 됐는지 대략 감이 오실거라 생각합니다.~~전투력 측정~~

강의를 다 보고나서는 노랭이책을 처음부터 풀기 시작했습니다. 문제는 각 장을 풀되, 2회차때 다시 풀어보기 위해 연습장에 따로 답을 적고 채점하는 식으로 풀었습니다. 틀린 문제나 헷갈리는 문제는 유튜브 **[전광철 OCP](https://youtu.be/_dx3fPb766E)**에서 해설강의를 봤습니다. 실전문제집 모든 문제의 해설강의가 올라와있는 보석💎같은 채널입니다.(감사합니다 선생님🙇‍♂️) 질문 댓글에도 친절하게 답변해 주시니 참고하세요.

### 2주차 : 문제풀이 1회독 → 문제풀이 2회독 → 블로그 문제로 마무리

2과목 SQL 활용 파트부터는 모르는 내용이 너무 많고 풀기 어려운 문제가 많아져 당황스러웠습니다. 때문에 전광철 OCP 채널에서 모든 문제의 해설강의를 봤습니다. 해설강의에 개념 설명도 일부 포함되어 있는데, 개념서가 따로 없었기 때문에 이런 설명을 같이 듣는게 도움이 됐습니다. (해설이 잘못된 경우도 있는데 이런 경우는 정정 댓글이 달려있으니 참고하세요.)

해설강의를 듣고도 이해가 어려울때는 유튜브 **[SQL전문가 정미나](https://www.youtube.com/c/SQL%EC%A0%84%EB%AC%B8%EA%B0%80%EC%A0%95%EB%AF%B8%EB%82%98)** 채널(유선배 교재를 집필하신 분입니다!)에서 해당 개념을 검색해서 설명 영상을 참고했습니다. 개념 설명을 쉽게 해주시고 직접 SQL 구문을 써서 보여주시는 점이 좋았습니다. 동영상 길이가 짧은 편이라 이동하면서 틈틈이 봤습니다.

공부하다가 궁금한 점은 **[데이터 전문가 포럼](https://cafe.naver.com/sqlpd)**을 검색해보거나 질문을 올려서 확인했습니다.

> 노랭이 책으로 공부하는 분들이 많아서 이미 올라온 질문글이 있을 수 있습니다. <u>노랭이 p000 00번</u> 이런식으로 검색해보세요. 
{: .prompt-tip }

문제풀이 2회차까지 마치고 나니 시험 전날 저녁이었는데, 남은 시간은 **[블로그](https://yunamom.tistory.com/category/%EC%9E%90%EA%B2%A9%EC%A6%9D/SQLD%20%EC%9E%90%EA%B2%A9%EC%A6%9D)**에서 기출문제를 풀었습니다. 웹에서 기출문제를 풀기 쉽게 되어있습니다. 최근 시험을 골라 3회분 정도 풀어봤습니다.

# 시험 후기

## 시험 준비물

- 필수 : 신분증, 검정색 사인펜
- 선택 : 수험표 (고사장을 알려면 수험번호를 알아야하는데, 데이터산업진흥원에서 시험 접수하면 문자로도 보내주기 때문에 필수는 아닙니다.)

## 현장 후기

다른 데이터자격검정과 마찬가지로 시험은 10시 정각에 시작하며, 10시 30분부터 퇴실할 수 있습니다. 45회차에 응시했고 경기고에서 시험을 봤는데 경사가 심하고 정문부터 시험장 건물까지 거리가 꽤 있어서 추천드리지 않습니다. 체감 난이도는 높지 않았습니다.

- 문제은행식 출제라서 그런지 노랭이책에서 봤던 문제가 많이 나온 느낌이었습니다.
- 시험장까지 택시를 타고 가면서 아내에게(같이 시험봤습니다😅)시험에 나올만한 개념을 설명해줬는데(NULL의 연산, NULL 함수, 속성 종류, 집합 연산자 등) 시험에 많이 나왔습니다. 공부하시면서 "이거 왠지 나올 것 같은데?" 싶은 것들을 마킹해놨다가 시험 직전에 보시는 것도 도움이 될 것 같습니다.

# 지극히 주관적인 총평

## 취득 난이도 : 🌕🌕🌑🌑🌑

학습량을 고려하면 난이도 점수를 더 줘야겠지만 준비하는 과정이 즐겁고 유익했기 때문에 난이도를 낮췄습니다. 공부하면서 SQL과 조금 더 친해진 느낌이 들었습니다. 다른 후기들도 보면 ADsP나 DAsP보다 공부한 보람과 재미가 있었다는(?) 내용이 많았습니다. 

## 유용성 : 🌕🌕🌕🌑🌑

데이터 관련업과 연관이 있으시다면 따놓아서 손해볼 일은 없을 것 같습니다. 다른 데이터자격검정 준전문가 자격증보다는 높은 평가를 받는 것 같고, SQL을 잘 모른다면 준비하면서 공부하는 것 만으로도 도움이 될 것입니다. 아무쪼록 이 글을 보시는 분들께 바라는 결과가 있으시길 바랍니다🙏

---

[^1]: <https://www.dataq.or.kr/www/sub/a_04.do>