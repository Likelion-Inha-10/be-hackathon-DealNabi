# be-hackathon-DealNabi
#### 대한민국에서 인기를 끌고 있는 상위 N개의 동영상에 대하여 
#### 그 "순위", "영상제목", "영상설명", 채널명", "조회수"를 조회하고 
#### 각 영상의 "최상위 댓글"을 조회하여야 한다.
----------------------------------------------------------------------

## 클래스 별 기능

### 1. get_id : 실시간 인기 동영상 상위 N개의 동영상 ID 조회
> input: N \
> output: video_list 

### 2. get_info : 실시간 인기 동영상 상위 N개의 "영상 제목", "영상 설명", "채널명", "조회수" 정보 조회
> input: N \
> output: video_title,video_des,video_channelTitle,video_viewCount

### 3. get_comment: 해당 동영상의 댓글 조회
> input: video_list \
> output: return comment_lsit & comment_list.txt 파일 생성

### 4. wdcloud: 조회된 댓글로 단어구름 형성
> input: comment_list.txt \
> output: wordcloud.png

### 5. info2table
> input: video_title,video_des,video_channelTitle,video_viewCount \
> output: exl 파일 생성

---------------------------------------------------------------------

## 고난과 역경 . . .

### 1. python 버전 통일 (downgrade)
> sol1 : 삭제 후 재설치 (반드시 Add Python to PATH 체크박스 표시!!!) \
> sol2 : 가상환경 

### 2. request의 사용법
> API 별 Required parameters 체크 필수 ! \
> response 에서 복잡한 다중 딕셔너리 형식 받을 때 주의! ex. snippet \
> ![image](https://user-images.githubusercontent.com/87406368/167616837-f28af553-d79b-44a5-9784-776922e82a06.png) \
> ![image](https://user-images.githubusercontent.com/87406368/167617046-ee0e2ba7-544e-4c7b-b874-723afe75540e.png)



### 3. selenium 이냐, request 냐 ?!
> selenium : 브라우저 상에서 마우스를 내리면서 동적으로 생성된 정보를 가져오는 모듈 (시간이 오래걸림) \
> request : request, params, response 를 통해 공공 데이터 API 이용 (범용성 good)

### 4. 단어구름 noum_list 의 반환 형태 
> 리스트에 담긴 튜플 형태 {(단어1,빈도수1),(단어2,빈도수2)...}

### 5. 파이썬 문법
> 즉시 사용하고 버리는 일시적인 익명 함수 lambda \
> ![image](https://user-images.githubusercontent.com/87406368/167620144-8893ca89-9c7c-47eb-b93e-93566e386474.png) \
> ▶리스트 내포 for문 사용\
> ```
> [ 표현식 for 항목 in 리스트 or 튜플 if 조건문 ]
> ```

### 6. 단어구름 준비 과정
> 입력해야 했던 명령어 : \
> sudo apt-get install openjdk-7-jdk \
> sudo apt-get install python-dev\
> sudo pip3 install konlpy 
>
>1)	M1 macOS 특성상 apt-get가 아닌 homebrew를 통해 설치해야 했음.
>2)	Brew install 명령어가 입력되지 않았음. 이후 구글링 통해 eval $(/opt/homebrew/bin/brew shellenv)를 입력했더니 구동됨.
>3)	Brew install openjdk-7-jdk 명령어가 실행되지 않았음.
>4)	M1 macOS 에서 구동되는 JDK를 따로 설치함.
>5)	자바경로 설정 과정에서 ~/.zshrc 파일이 없어서 touch 명령어로 직접 만들어줘야 했음.
>6)	다음날 JDK 관련 오류가 발생하여 17버전으로 다시 설치함.
>
>*6번 오류가 발생한 이유는 지금도 모르겠음. 당시 오류 매세지는 다음과 같았음. \
><img width="1145" alt="스크린샷 2022-05-10 오후 8 49 31" src="https://user-images.githubusercontent.com/96401830/167622444-8e611df3-0ec8-4a09-a2ee-29460217958e.png">\
>
>코드를 분해해본 결과 JDK가 필요한 konlpy를 이용하는 코드에서 문제가 발생하는 것을 발견함. \
>이후 버전을 달리하여 다시 설치함으로 문제를 해결함

